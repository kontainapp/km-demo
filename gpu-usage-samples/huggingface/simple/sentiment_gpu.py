import torch
from transformers import pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"
sentiment_pipeline = pipeline("sentiment-analysis", device=device)
data = ["I love you", "I hate you"]
print(data)
print(sentiment_pipeline(data))
