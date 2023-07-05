# Usage: python image_from_text.py --text='artificial intelligence' --no-mega
from cog import  BasePredictor, Input, Path
import os
from PIL import Image
from min_dalle import MinDalle
import torch
import requests
import json

CACHE_DIR = 'weights'

# Shorthand identifier for a transformers model.
# See https://huggingface.co/models?library=transformers for a list of models.
MODEL_NAME = 'openai/clip-vit-base-patch32'


class Predictor(BasePredictor):
    def setup(self):
        self.image_path = 'images'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = MinDalle(
            is_mega=False,
            models_root='pretrained',
            is_reusable=True,
            is_verbose=True,
            dtype=torch.float32,
            device='cuda' if torch.cuda.is_available() else 'cpu'
        )

    def ascii_from_image(self, image: Image.Image, size: int = 128) -> str:
        gray_pixels = image.resize((size, int(0.55 * size))).convert('L').getdata()
        chars = list('.,;/IOX')
        chars = [chars[i * len(chars) // 256] for i in gray_pixels]
        chars = [chars[i * size: (i + 1) * size] for i in range(size // 2)]
        return '\n'.join(''.join(row) for row in chars)


    def save_image(self, image: Image.Image, path: str, image_name: str):
        if os.path.isdir(path):
            path = os.path.join(path, image_name)
        elif not path.endswith('.png'):
            path += '.png'
        print("saving image to:", path)
        image.save(path)
        return path


    def generate_image(
        self, 
        is_mega: bool,
        prompt: str,
        seed: int,
        grid_size: int,
        top_k: int,
        image_path: str,
        fp16: bool,
    ):
        image_name = prompt.replace(" ", "-")
        image_name = f"{image_name}.png"
        print(f"generate image:{prompt} {self.image_path}/{image_name}")
        image = self.model.generate_image(
            prompt, 
            seed, 
            grid_size, 
            top_k=top_k, 
            is_verbose=True,
        )
        return self.save_image(image=image, path=self.image_path, image_name=image_name)
        # print(self.ascii_from_image(image, size=128))


    def predict(
        self,
          prompt: str = Input(description="Text Prompt that generates an image")
    ) -> str:
        print(f"generate image:{prompt}")
        saved_image_path = self.generate_image(
            is_mega=False,
            prompt=prompt,
            seed=-1,
            grid_size=1,
            top_k=256,
            image_path=self.image_path,
            fp16=False,
        )
        return saved_image_path
