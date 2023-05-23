import torch
from transformers import pipeline

from torch import mps

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

print(f"Using {device} device")

generator = pipeline("text-generation", model="distilgpt2", device=device)
output=generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(output)
