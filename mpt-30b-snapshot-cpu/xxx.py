from os import getenv
import time, sys
start = time.clock_gettime(time.CLOCK_REALTIME)

import torch
import transformers

name = 'mosaicml/mpt-30b'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
# config.attn_config['attn_impl'] = 'triton'  # change this to use triton-based FlashAttention
config.init_device = 'cuda:0' # For fast initialization directly on GPU!

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  torch_dtype=torch.bfloat16, # Load model weights in bfloat16
  trust_remote_code=True,
)


tokenizer = transformers.AutoTokenizer.from_pretrained('mosaicml/mpt-30b', learned_pos_emb=False)
pipe = transformers.pipeline('text-generation', model=model, tokenizer=tokenizer, device='cuda:0')


print("Prep: ", time.clock_gettime(time.CLOCK_REALTIME) - start)

if getenv("MAKE_SNAPSHOT") != None:
    from ctypes import CDLL
    kontain = CDLL("libkontain.so")
    print(kontain.snapshot("pytorch", "mpt", 0))


prompt = "Early in the morning"

start = time.clock_gettime(time.CLOCK_REALTIME)

with torch.autocast('cuda', dtype=torch.bfloat16):
   print(pipe(prompt, max_new_tokens=100, do_sample=True, use_cache=True))

print("Compute: ", time.clock_gettime(time.CLOCK_REALTIME) - start)
