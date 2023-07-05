from cog import  BasePredictor, Input, Path
import torch
import torchvision.models as models
from torchvision.models import ResNet18_Weights
import torchvision.transforms as transforms
from PIL import Image


# ref: https://github.com/replicate/cog/blob/main/docs/python.md
# You define how Cog runs predictions on your model by defining a class that inherits from BasePredictor. It looks something like this:
# Your Predictor class should define two methods: setup() and predict().
class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        #self.model = torch.load("./weights.pth")
        self.model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
        self.model.eval()  # Set the model to evaluation mode
    
    def preprocess(self, image):
        print(type(image))
        image = Image.open(image)
        preprocess = transforms.Compose([
            transforms.Resize(256),         # Resize the image to 256x256 pixels
            transforms.CenterCrop(224),     # Crop the image to 224x224 pixels around the center
            transforms.ToTensor(),          # Convert the image to a tensor
            transforms.Normalize(           # Normalize the image's RGB channels
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
            ) 
        ])

        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension
        return input_batch

    def postprocess(self, output):
        # Load the class labels
        with open('imagenet-simple-labels.json') as f:
            labels = [line.strip() for line in f.readlines()]

        # Get the predicted class index
        _, predicted_idx = torch.max(output, 1)
        predicted_label = labels[predicted_idx.item()]
        return predicted_label


    # The arguments and types the model takes as input
    def predict(self,
          image: Path = Input(description="Image that needs classification")
    ) -> str:
        """Run a single prediction on the model"""
        # processed_image = preprocess(image)
        # output = self.model(processed_image)
        # return postprocess(output)

        # Load and preprocess the image
        # image = './cup.jpg'

        # Make predictions
        input_batch = self.preprocess(image)

        with torch.no_grad():
            output = self.model(input_batch)

        predicted_label = self.postprocess(output)
        print(predicted_label)
        return predicted_label
