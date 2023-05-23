# ref: https://towardsdatascience.com/how-fast-gpu-computation-can-be-41e8cff75974
# we measure linear transformation time for GPU
import torch
import torch.nn
import time
in_row, in_f, out_f = 256, 1024, 2048 # 2,2,3
loop_times = 10000

# Now, let's see how many seconds will take the CPU to finish the 10,000 transformations:
s       = time.time()
tensor  = torch.randn(in_row, in_f).cuda()
l_trans = torch.nn.Linear(in_f, out_f).cuda()
for _ in range(loop_times):
    l_trans(tensor)
torch.cuda.synchronize()
print('CUDA take time:',time.time()-s)