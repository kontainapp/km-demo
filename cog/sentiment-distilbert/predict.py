from typing import List, Optional
from cog import BasePredictor, Input
from transformers import pipeline, set_seed
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import torch

CACHE_DIR = 'weights'

# Shorthand identifier for a transformers model.
# See https://huggingface.co/models?library=transformers for a list of models.
MODEL_NAME = 'distilbert-base-uncased-finetuned-sst-2-english'

class Predictor(BasePredictor):
    def setup(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
        self.model = self.model.to(self.device)
        self.pipeline = TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer)

    def predict(
        self,
        content: str = Input(description=f"Sentence to classify sentiment."),
        n: int = Input(description="Number of output sequences to generate", default=1, ge=1, le=5),
        max_length: int = Input(
            description="Maximum number of tokens to generate. A word is generally 2-3 tokens",
            ge=1,
            default=50
        ),
        temperature: float = Input(
            description="Adjusts randomness of outputs, greater than 1 is random and 0 is deterministic, 0.75 is a good starting value.",
            ge=0.01,
            le=5,
            default=0.75,
        ),
        top_p: float = Input(
            description="When decoding text, samples from the top p percentage of most likely tokens; lower to ignore less likely tokens",
            ge=0.01,
            le=1.0,
            default=1.0
        ),
        repetition_penalty: float = Input(
            description="Penalty for repeated words in generated text; 1 is no penalty, values greater than 1 discourage repetition, less than 1 encourage it.",
            ge=0.01,
            le=5,
            default=1
        )
        ) -> str: #-> List[str]:
        set_seed(42)
        # output = self.generator(prompt, max_length=50, 
        #                     num_return_sequences=1,
        #                     temperature=temperature,
        #                     top_p=top_p,
        #                     repetition_penalty=repetition_penalty)

        output = self.pipeline(content)

        return str(output)