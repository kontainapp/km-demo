import torch
import torchvision.models as models
from torchvision.models import ResNet18_Weights
import torchvision.transforms as transforms
from PIL import Image

# Load the pre-trained ResNet-18 model
# way 1 to load it
# model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
# below 2 is best way to load it
# model = models.resnet18(pretrained=True)
model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
model.eval()  # Set the model to evaluation mode

# Load and preprocess the image
image_path = './cup.jpg'
image = Image.open(image_path)
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

# Make predictions
with torch.no_grad():
    output = model(input_batch)

# Load the class labels
with open('imagenet-simple-labels.json') as f:
    labels = [line.strip() for line in f.readlines()]

# Get the predicted class index
_, predicted_idx = torch.max(output, 1)
print(predicted_idx.item())
predicted_label = labels[predicted_idx.item()]

# Print the predicted label
print(f"Predicted label: {predicted_label}")
