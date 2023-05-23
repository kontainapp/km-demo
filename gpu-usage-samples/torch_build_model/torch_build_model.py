# ref: https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html
# !pip install torch torchvision
import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# In the following sections, 
# # we'll build a neural network to classify images in the FashionMNIST dataset.

# We want to be able to train our model on a hardware accelerator like the GPU or MPS, 
# if available.
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

print(f"Using {device} device")

# We define our neural network by subclassing nn.Module, and 
# initialize the neural network layers in __init__
#
# Every nn.Module subclass implements the operations on input data in the forward method.
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

# We create an instance of NeuralNetwork, and move it to the device, and print its structure.
model = NeuralNetwork().to(device)
print(model)

# To use the model, we pass it the input data. This executes the model's forward, along with some background operations. Do not call model.forward() directly!
# Calling the model on the input returns a 2-dimensional tensor with dim=0 corresponding to each output of 10 raw predicted values for each class, and dim=1 corresponding to the individual values of each output. 
# We get the prediction probabilities by passing it through an instance of the nn.Softmax module.
X = torch.rand(1, 28, 28, device=device)
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")

# Let's break down the layers in the FashionMNIST model. 
# To illustrate it, we will take a sample minibatch of 3 images of size 28x28 
# and see what happens to it as we pass it through the network.
input_image = torch.rand(3,28,28)
print(input_image.size())

# nn.Flatten
# We initialize the nn.Flatten layer to convert each 2D 28x28 image into a 
# contiguous array of 784 pixel values ( the minibatch dimension (at dim=0) is maintained).
flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())

### nn.Linear
# nn.Linear
# The linear layer is a module that applies a linear transformation 
# on the input using its stored weights and biases.
layer1 = nn.Linear(in_features=28*28, out_features=20)
hidden1 = layer1(flat_image)
print(hidden1.size())

## nn.ReLU
# Non-linear activations are what create the complex mappings between the model's 
# inputs and outputs. They are applied after linear transformations to introduce nonlinearity, 
# helping neural networks learn a wide variety of phenomena. In this model, 
# we use nn.ReLU between our linear layers, but there's other activations 
# to introduce non-linearity in your model.
print(f"Before ReLU: {hidden1}\n\n")
hidden1 = nn.ReLU()(hidden1)
print(f"After ReLU: {hidden1}")

# nn.Sequential
# nn.Sequential is an ordered container of modules. 
# The data is passed through all the modules in the same order as defined. 
# You can use sequential containers to put together a quick network like seq_modules.
seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)
input_image = torch.rand(3,28,28)
logits = seq_modules(input_image)

## nn.Softmax
# The last linear layer of the neural network returns logits - raw values in [-\infty, \infty] - 
# which are passed to the nn.Softmax module. The logits are scaled to values [0, 1] representing 
# the model's predicted probabilities for each class. 
# dim parameter indicates the dimension along which the values must sum to 1.
softmax = nn.Softmax(dim=1)
pred_probab = softmax(logits)

## Model Parameters
# Many layers inside a neural network are parameterized, i.e. have associated 
# weights and biases that are optimized during training. 
# Subclassing nn.Module automatically tracks all fields defined inside your model object, 
# and makes all parameters accessible using your model's parameters() or named_parameters() 
# methods.

# In this example, we iterate over each parameter, 
# and print its size and a preview of its values.
print(f"Model structure: {model}\n\n")

for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")
