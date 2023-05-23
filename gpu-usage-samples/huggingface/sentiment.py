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

sentiment_pipeline = pipeline("sentiment-analysis", device=device)
data = ["I love you", "I hate you"]
print(data)
print(sentiment_pipeline(data))
