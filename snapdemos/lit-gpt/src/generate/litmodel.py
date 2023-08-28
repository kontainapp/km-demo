import json
import sys
import time
import warnings
from pathlib import Path
from typing import Optional, Literal

import lightning as L
import torch
from lightning.fabric.strategies import FSDPStrategy

# support running without installing as a package
wd = Path(__file__).parent.parent.resolve()
sys.path.append(str(wd))

from lit_gpt import GPT, Tokenizer, Config
from lit_gpt.model import Block
from lit_gpt.utils import lazy_load, check_valid_checkpoint_dir, quantization
from generate.base import generate

class LitModel:
    def __init__(self, 
                checkpoint_dir: Path = Path("checkpoints/stabilityai/stablelm-base-alpha-3b"),
                quantize: Optional[Literal["bnb.nf4", "bnb.nf4-dq", "bnb.fp4", "bnb.fp4-dq", "bnb.int8", "gptq.int4"]] = None,
                strategy: str = "auto",
                devices: int = 1,
                precision: str = "bf16-true",
                 ):
        self.checkpoint_dir = checkpoint_dir
        self.quantize = quantize
        self.strategy = strategy
        self.devices = devices
        self.precision = precision
        self.model = None
        self.fabric = None
        self.tokenizer = None

    def __str__(self):
        return f"{self.checkpoint_dir}({self.quantize}{self.devices}{self.strategy}{self.precision})"

    def load(self):
        """Generates text samples based on a pre-trained model and tokenizer.

        Args:
            prompt: The prompt string to use for generating the samples.
            num_samples: The number of text samples to generate.
            max_new_tokens: The number of generation steps to take.
            top_k: The number of top most probable tokens to consider in the sampling process.
            temperature: A value controlling the randomness of the sampling process. Higher values result in more random
                samples.
            checkpoint_dir: The checkpoint directory to load.
            quantize: Whether to quantize the model and using which method:
                - bnb.nf4, bnb.nf4-dq, bnb.fp4, bnb.fp4-dq: 4-bit quantization from bitsandbytes
                - bnb.int8: 8-bit quantization from bitsandbytes
                - gptq.int4: 4-bit quantization from GPTQ
                for more details, see https://github.com/Lightning-AI/lit-gpt/blob/main/tutorials/quantize.md
            strategy: Indicates the Fabric strategy setting to use.
            devices: How many devices to use.
            precision: Indicates the Fabric precision setting to use.
        """
        if self.strategy == "fsdp":
            self.strategy = FSDPStrategy(auto_wrap_policy={Block}, cpu_offload=False)
        self.fabric = L.Fabric(devices=self.devices, precision=self.precision, strategy=self.strategy)
        self.fabric.launch()

        check_valid_checkpoint_dir(self.checkpoint_dir)

        with open(self.checkpoint_dir / "lit_config.json") as fp:
            config = Config(**json.load(fp))

        if self.quantize is not None and self.devices > 1:
            raise NotImplementedError
        if self.quantize == "gptq.int4":
            model_file = "lit_model_gptq.4bit.pth"
            if not (self.checkpoint_dir / model_file).is_file():
                raise ValueError("Please run `python quantize/gptq.py` first")
        else:
            model_file = "lit_model.pth"
        checkpoint_path = self.checkpoint_dir / model_file

        self.fabric.print(f"Loading model {str(checkpoint_path)!r} with {config.__dict__}", file=sys.stderr)
        t0 = time.time()
        with self.fabric.init_module(empty_init=True), quantization(self.quantize):
            self.model = GPT(config)
        self.fabric.print(f"Time to instantiate model: {time.time() - t0:.02f} seconds.", file=sys.stderr)

        t0 = time.time()
        with lazy_load(checkpoint_path) as checkpoint:
            self.model.load_state_dict(checkpoint.get("model", checkpoint), strict=self.quantize is None)
        self.fabric.print(f"Time to load the model weights: {time.time() - t0:.02f} seconds.", file=sys.stderr)

        self.model.eval()
        self.model = self.fabric.setup_module(self.model)

        self.tokenizer = Tokenizer(self.checkpoint_dir)

        print(f"model: {type(self.model)}")
        print(f"tokenizer: {type(self.tokenizer)}")
        print(f"fabric: {type(self.fabric)}")

        return
    
    def gen(self,
            prompt: str = "Hello, my name is",
            *,
            num_samples: int = 1,
            max_new_tokens: int = 50,
            top_k: int = 200,
            temperature: float = 0.8,
            )-> str:
        #-----
        # everything below is for generation
        encoded = self.tokenizer.encode(prompt, device=self.fabric.device)
        prompt_length = encoded.size(0)
        max_returned_tokens = prompt_length + max_new_tokens
        assert max_returned_tokens <= self.model.config.block_size, (
            max_returned_tokens,
            self.model.config.block_size,
        )  # maximum rope cache length

        L.seed_everything(1234)
        output = ""
        for i in range(num_samples):
            t0 = time.perf_counter()
            y = generate(
                self.model,
                encoded,
                max_returned_tokens,
                max_seq_length=max_returned_tokens,
                temperature=temperature,
                top_k=top_k,
            )
            t = time.perf_counter() - t0

            self.model.reset_cache()
            tmpout = self.tokenizer.decode(y)
            self.fabric.print(tmpout)
            output = output + tmpout
            tokens_generated = y.size(0) - prompt_length
            self.fabric.print(
                f"Time for inference {i + 1}: {t:.02f} sec total, {tokens_generated / t:.02f} tokens/sec", file=sys.stderr
            )
        if self.fabric.device.type == "cuda":
            self.fabric.print(f"Memory used: {torch.cuda.max_memory_allocated() / 1e9:.02f} GB", file=sys.stderr)
        return str(output)
