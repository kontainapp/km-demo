import torch
from transformers import pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"

generator = pipeline("text-generation", model="distilgpt2", device=device)
output=generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(output)
