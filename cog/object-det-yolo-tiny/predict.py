from typing import List, Optional
from cog import BasePredictor, Input
from transformers import YolosImageProcessor, YolosForObjectDetection
from PIL import Image
import torch
import requests
import json

CACHE_DIR = 'weights'

# Shorthand identifier for a transformers model.
# See https://huggingface.co/models?library=transformers for a list of models.
MODEL_NAME = 'distilbert-base-uncased-finetuned-sst-2-english'

class Predictor(BasePredictor):
    def setup(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YolosForObjectDetection.from_pretrained('hustvl/yolos-tiny')
        self.image_processor = YolosImageProcessor.from_pretrained("hustvl/yolos-tiny")

    def predict(
        self,
        image_url: str = Input(description=f"Url to image."),
        ) -> str: #-> List[str]:

        image = Image.open(requests.get(image_url, stream=True).raw)
        inputs = self.image_processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        # model predicts bounding boxes and corresponding COCO classes
        logits = outputs.logits
        bboxes = outputs.pred_boxes

        target_sizes = torch.tensor([image.size[::-1]])
        results = self.image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[0]
        output_arr = []

        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            print(
                f"Detected {self.model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )
            output_arr.append(
                f"Detected {self.model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )

        return json.dumps(output_arr, indent=3)