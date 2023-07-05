from min_dalle import MinDalle
import torch

device='cuda' if torch.cuda.is_available() else 'cpu'
print(device)

model = MinDalle(
    models_root='./pretrained',
    dtype=torch.float16,
    device=device,
    is_mega=False, 
    is_reusable=True
)

image = model.generate_image(
    text='Nuclear explosion broccoli',
    seed=-1,
    grid_size=4,
    is_seamless=False,
    temperature=1,
    top_k=256,
    supercondition_factor=32,
    is_verbose=False
)

display(image)
