import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import timm
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Custom Dataset Class
class OnePieceDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data = ImageFolder(data_dir)
        self.transform = transform

    def __getitem__(self, idx):
        img, label = self.data[idx]
        img = img.convert("RGBA").convert("RGB")  # Convert to RGB
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

# Split Dataset into Train, Validation, and Test
train_size = int(0.7 * len(dataset))  # 70% for training
val_size = int(0.15 * len(dataset))   # 15% for validation
test_size = len(dataset) - train_size - val_size

train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])

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
        x = torch.flatten(x, 1)
        output = self.classifier(x)
        return output


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Model, Loss Function, and Optimizer
num_classes = len(dataset.data.classes)
model = SimpleOnePieceClassifier(num_classes=num_classes)
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Path to save/load model
model_path = '/Users/jeremycheng/Desktop/Desktop - Jeremy’s MacBook Pro/One_Piece_Model.pth'

# Check if model exists
if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path))
    model.eval()
    print("Model loaded successfully. Skipping training...")
else:
    print("Training model...")
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

        # Validation
        model.eval()
        running_loss = 0.0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                running_loss += loss.item() * images.size(0)
        val_loss = running_loss / len(val_loader.dataset)
        val_losses.append(val_loss)

        print(f"Epoch [{epoch+1}/{num_epochs}], Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")

    torch.save(model.state_dict(), model_path)
    print("Model saved successfully!")

# Preprocessing and Prediction Functions
def preprocess_image(image_path, transform):
    image = Image.open(image_path).convert("RGB")
    return image, transform(image).unsqueeze(0)

def predict(model, image_tensor, device):
    model.eval()
    with torch.no_grad():
        image_tensor = image_tensor.to(device)
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
    return probabilities.cpu().numpy().flatten()

def visualize_predictions(original_image, probabilities, class_names):
    fig, axarr = plt.subplots(1, 2, figsize=(14, 7))

    # Display original image
    axarr[0].imshow(original_image)
    axarr[0].axis("off")

    # Plot probabilities
    axarr[1].barh(class_names, probabilities)
    axarr[1].set_xlabel("Probability")
    axarr[1].set_title("Class Predictions")
    axarr[1].set_xlim(0, 1)

    plt.tight_layout()
    plt.show()

# Test Inference
# test_image = '/Users/jeremycheng/Downloads/OnePieceDataset/Data/Data/Shanks/1.png'
# original_image, image_tensor = preprocess_image(test_image, transform)
# probabilities = predict(model, image_tensor, device)
# class_names = dataset.data.classes
# visualize_predictions(original_image, probabilities, class_names)
