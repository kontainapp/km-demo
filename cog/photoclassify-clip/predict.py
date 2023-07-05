from cog import  BasePredictor, Input, Path
from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel
import torch
import numpy
from json import JSONEncoder
import json

CACHE_DIR = 'weights'

# Shorthand identifier for a transformers model.
# See https://huggingface.co/models?library=transformers for a list of models.
MODEL_NAME = 'openai/clip-vit-base-patch32'

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

class Predictor(BasePredictor):
    def setup(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = CLIPModel.from_pretrained(pretrained_model_name_or_path=MODEL_NAME)
        self.model = self.model.to(self.device)
        self.processor = CLIPProcessor.from_pretrained(pretrained_model_name_or_path=MODEL_NAME)

    def predict(
        self,
          image: str = Input(description="Image that needs classification")
    ) -> str:
        image = Image.open(requests.get(image, stream=True).raw)

        inputs = self.processor(text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True)

        outputs = self.model(**inputs)
        logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        # probs is a tensor array of 2

        print(probs)
        narray = probs.detach().cpu().numpy()
        print(narray.tolist())
        print(numpy.array2string(narray))
        jsonoutput = json.dumps(narray, cls=NumpyArrayEncoder)
        return jsonoutput
