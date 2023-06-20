from ctypes import *
from os import getenv

from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import torch
from transformers import pipeline, set_seed

kontain = CDLL("libkontain.so")

device = "cuda:0" # if torch.cuda.is_available() else "cpu"
generator = pipeline('text-generation', model='gpt2', pad_token_id=50256, device=device)

content = "early in the morning"
set_seed(42)
output = generator(content, max_length=30, num_return_sequences=1)
print(output)

if getenv("MAKE_SNAPSHOT") != None:
    print(kontain.snapshot("pytorch", "sentiment", 0))

content = "late in the afternoon"
output = generator(content, max_length=30, num_return_sequences=1)
print(output)

# from transformers import GPT2Tokenizer, GPT2Model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2')
# text = "Once upon a time, "
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
