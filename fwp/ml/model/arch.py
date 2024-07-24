import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        """
        Replacing the custom CNN architecture with VGG16 for Image classification
        """
        super(Net, self).__init__()
        
        # Load VGG16 model with pretrained weights
        self.model = models.vgg16(pretrained=True)
        
        # Replace the final fully connected layer to match the number of classes in your dataset
        num_features = self.model.classifier[6].in_features
        self.model.classifier[6] = nn.Linear(num_features, 2)  # Assuming 2 classes: Original and Fake

    def forward(self, x):
        return self.model(x)
