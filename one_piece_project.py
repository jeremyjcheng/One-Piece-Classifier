import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import timm
import matplotlib.pyplot as plt
import numpy as np
import os

# Custom Dataset Class
class OnePieceDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data = ImageFolder(data_dir)
        self.transform = transform

    def __getitem__(self, idx):
        img, label = self.data[idx]
        
        # Convert to RGB if image has transparency
        img = img.convert("RGBA").convert("RGB")
        
        if self.transform:
            img = self.transform(img)
        
        return img, label

    def __len__(self):
        return len(self.data)



# Data directory
data_dir = '/Users/jeremycheng/Downloads/OnePieceDataset/Data/Data'

# Image Transformations
transform = transforms.Compose([
    transforms.Resize((128, 128)), 
    transforms.ToTensor(),
])

# Full Dataset
dataset = OnePieceDataset(data_dir, transform)
#print(f"Total dataset size: {len(dataset)}")

# Split Dataset into Train, Validation, and Test
train_size = int(0.7 * len(dataset))  # 70% for training
val_size = int(0.15 * len(dataset))   # 15% for validation
test_size = len(dataset) - train_size - val_size  # Remaining for testing

train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])
#print(f"Train size: {len(train_dataset)}, Val size: {len(val_dataset)}, Test size: {len(test_dataset)}")

# DataLoaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Model Definition
class SimpleOnePieceClassifier(nn.Module):
    def __init__(self, num_classes=17):
        super(SimpleOnePieceClassifier, self).__init__()
        self.base_model = timm.create_model('efficientnet_b0', pretrained=True)
        self.features = nn.Sequential(*list(self.base_model.children())[:-1])
        enet_out_size = 1280
        self.classifier = nn.Linear(enet_out_size, num_classes)

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)  # Flatten the feature maps
        output = self.classifier(x)
        return output

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# Model, Loss Function, and Optimizer
num_classes = len(dataset.data.classes)
model = SimpleOnePieceClassifier(num_classes=num_classes)
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training Loop
num_epochs = 5
train_losses, val_losses = [], []

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * images.size(0)
    
    train_loss = running_loss / len(train_loader.dataset)
    train_losses.append(train_loss)
    
    #Validation
    model.eval()
    running_loss = 0.0
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            running_loss += loss.item() * images.size(0)
    val_loss = running_loss / len(val_loader.dataset)
    val_losses.append(val_loss)

    print(f"Epoch [{epoch+1}/{num_epochs}], Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")
