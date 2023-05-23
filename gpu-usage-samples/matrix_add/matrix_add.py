# this example just compares the matrix addition time taken on CPU vs GPU
import torch
import time
from torch import mps

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

print(f"Using {device} device")

###CPU
start_time = time.time()
a = torch.ones(4000,4000)
for _ in range(100000):
    a += a
elapsed_time = time.time() - start_time

print('CPU time = ',elapsed_time)

###GPU
start_time = time.time()
if torch.has_cuda:
    torch.cuda.synchronize()
elif torch.has_mps:
    torch.mps.synchronize()

b = torch.ones(4000,4000).to(device)
for _ in range(100000):
    b += b
elapsed_time = time.time() - start_time

print('GPU time = ',elapsed_time)
