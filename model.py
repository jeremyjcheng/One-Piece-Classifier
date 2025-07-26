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
import time
from tqdm import tqdm
import datetime

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

# Image Transformations - optimized for faster training
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Standard size for better performance
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # ImageNet normalization
])

# Full Dataset
dataset = OnePieceDataset(data_dir, transform)

# Split Dataset into Train, Validation, and Test
train_size = int(0.7 * len(dataset))  # 70% for training
val_size = int(0.15 * len(dataset))   # 15% for validation
test_size = len(dataset) - train_size - val_size

train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])

# DataLoaders with optimized batch size (num_workers=0 to avoid multiprocessing issues)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=0)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False, num_workers=0)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False, num_workers=0)

# Enhanced Model Definition - Using MobileNetV2 for even faster training
class FastOnePieceClassifier(nn.Module):
    def __init__(self, num_classes=17):
        super(FastOnePieceClassifier, self).__init__()
        # Use MobileNetV2 for even faster training
        self.base_model = timm.create_model('mobilenetv2_100', pretrained=True, num_classes=0)
        
        # Get the actual output size from the base model
        with torch.no_grad():
            dummy_input = torch.randn(1, 3, 224, 224)
            features = self.base_model(dummy_input)
            feature_size = features.shape[1]
        
        # Add a simple classifier head (no pooling/flatten needed)
        self.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(feature_size, num_classes)
        )

    def forward(self, x):
        x = self.base_model(x)
        x = self.classifier(x)
        return x


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Model, Loss Function, and Optimizer
num_classes = len(dataset.data.classes)
model = FastOnePieceClassifier(num_classes=num_classes)
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)  # AdamW for better convergence
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=2)

# Path to save/load model
model_path = 'One_Piece_Model.pth'

# Training function with progress tracking
def train_model(model, train_loader, val_loader, num_epochs, device, optimizer, criterion, scheduler):
    """Train the model with detailed progress tracking"""
    best_val_loss = float('inf')
    train_losses, val_losses = [], []
    
    print(f"\n🚀 Starting training for {num_epochs} epochs...")
    print(f"📊 Training samples: {len(train_loader.dataset)}")
    print(f"📊 Validation samples: {len(val_loader.dataset)}")
    print(f"🎯 Classes: {num_classes}")
    print(f"⚡ Device: {device}")
    print("=" * 60)
    
    # Estimate total training time
    start_time = time.time()
    
    for epoch in range(num_epochs):
        epoch_start_time = time.time()
        
        # Training phase
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0
        
        print(f"\n📚 Epoch {epoch+1}/{num_epochs}")
        print("Training...")
        
        train_pbar = tqdm(train_loader, desc=f"Epoch {epoch+1} [Train]", 
                          unit="batch", ncols=100)
        
        for batch_idx, (images, labels) in enumerate(train_pbar):
            images, labels = images.to(device), labels.to(device)
            
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            train_total += labels.size(0)
            train_correct += (predicted == labels).sum().item()
            
            # Update progress bar
            train_pbar.set_postfix({
                'Loss': f'{loss.item():.4f}',
                'Acc': f'{100 * train_correct / train_total:.1f}%'
            })
        
        avg_train_loss = train_loss / len(train_loader)
        train_accuracy = 100 * train_correct / train_total
        
        # Validation phase
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0
        
        print("Validating...")
        val_pbar = tqdm(val_loader, desc=f"Epoch {epoch+1} [Val]", 
                        unit="batch", ncols=100)
        
        with torch.no_grad():
            for images, labels in val_pbar:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                
                val_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                val_total += labels.size(0)
                val_correct += (predicted == labels).sum().item()
                
                # Update progress bar
                val_pbar.set_postfix({
                    'Loss': f'{loss.item():.4f}',
                    'Acc': f'{100 * val_correct / val_total:.1f}%'
                })
        
        avg_val_loss = val_loss / len(val_loader)
        val_accuracy = 100 * val_correct / val_total
        
        # Update learning rate
        scheduler.step(avg_val_loss)
        
        # Save best model
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            torch.save(model.state_dict(), model_path)
            print(f"💾 Best model saved! (Val Loss: {avg_val_loss:.4f})")
        
        # Calculate time estimates
        epoch_time = time.time() - epoch_start_time
        elapsed_time = time.time() - start_time
        avg_epoch_time = elapsed_time / (epoch + 1)
        remaining_epochs = num_epochs - (epoch + 1)
        estimated_remaining = remaining_epochs * avg_epoch_time
        
        # Store losses
        train_losses.append(avg_train_loss)
        val_losses.append(avg_val_loss)
        
        # Print epoch summary
        print(f"\n📈 Epoch {epoch+1} Summary:")
        print(f"   Train Loss: {avg_train_loss:.4f} | Train Acc: {train_accuracy:.1f}%")
        print(f"   Val Loss: {avg_val_loss:.4f} | Val Acc: {val_accuracy:.1f}%")
        print(f"   Learning Rate: {optimizer.param_groups[0]['lr']:.6f}")
        print(f"   Epoch Time: {epoch_time:.1f}s")
        print(f"   Estimated Time Remaining: {datetime.timedelta(seconds=int(estimated_remaining))}")
        print("-" * 60)
    
    total_time = time.time() - start_time
    print(f"\n🎉 Training completed in {datetime.timedelta(seconds=int(total_time))}")
    print(f"📊 Final Validation Accuracy: {val_accuracy:.1f}%")
    
    return train_losses, val_losses

# Check if model exists
model_exists = False
print(f"Looking for model file at: {os.path.abspath(model_path)}")
if os.path.exists(model_path):
    try:
        model.load_state_dict(torch.load(model_path, weights_only=True))
        model.eval()
        print("✅ Model loaded successfully. Skipping training...")
        model_exists = True
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        print("🔄 Will train a new model...")
else:
    print("📝 No trained model found. Will train a new model...")

# Only train if no model exists or loading failed
if not model_exists:
    print("\n🚀 Starting model training...")
    print("=" * 60)
    
    # Train the model
    train_losses, val_losses = train_model(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        num_epochs=10,  # Increased epochs for better performance
        device=device,
        optimizer=optimizer,
        criterion=criterion,
        scheduler=scheduler
    )
    
    # Plot training curves
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(train_losses, label='Train Loss')
    plt.plot(val_losses, label='Val Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot([100 * (1 - loss) for loss in train_losses], label='Train Accuracy')
    plt.plot([100 * (1 - loss) for loss in val_losses], label='Val Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('training_curves.png', dpi=300, bbox_inches='tight')
    print("📊 Training curves saved as 'training_curves.png'")

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
    axarr[0].set_title("Input Image")

    # Plot probabilities
    sorted_indices = np.argsort(probabilities)[::-1]
    top_5_indices = sorted_indices[:5]
    
    y_pos = np.arange(len(top_5_indices))
    axarr[1].barh(y_pos, probabilities[top_5_indices])
    axarr[1].set_yticks(y_pos)
    axarr[1].set_yticklabels([class_names[i] for i in top_5_indices])
    axarr[1].set_xlabel("Probability")
    axarr[1].set_title("Top 5 Predictions")
    axarr[1].set_xlim(0, 1)

    plt.tight_layout()
    plt.show()

# Test Inference (uncomment to test)
# test_image = '/Users/jeremycheng/Downloads/OnePieceDataset/Data/Data/Shanks/1.png'
# if os.path.exists(test_image):
#     original_image, image_tensor = preprocess_image(test_image, transform)
#     probabilities = predict(model, image_tensor, device)
#     class_names = dataset.data.classes
#     visualize_predictions(original_image, probabilities, class_names)
