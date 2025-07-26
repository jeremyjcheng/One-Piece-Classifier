#!/usr/bin/env python3
"""
Standalone training script for One Piece Character Classifier
Run this to train the model with detailed progress tracking
"""

import os
import sys
import time
import datetime
from pathlib import Path

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model import (
    FastOnePieceClassifier, 
    train_model, 
    train_loader, 
    val_loader, 
    device, 
    optimizer, 
    criterion, 
    scheduler,
    num_classes
)

def main():
    """Main training function"""
    print("🏴‍☠️  One Piece Character Classifier - Training Script")
    print("=" * 60)
    
    # Check if dataset exists
    data_dir = '/Users/jeremycheng/Downloads/OnePieceDataset/Data/Data'
    if not os.path.exists(data_dir):
        print(f"❌ Dataset not found at: {data_dir}")
        print("Please download the One Piece dataset and update the path in model.py")
        return
    
    print(f"✅ Dataset found at: {data_dir}")
    print(f"📊 Number of classes: {num_classes}")
    print(f"⚡ Using device: {device}")
    
    # Create model
    model = FastOnePieceClassifier(num_classes=num_classes)
    model.to(device)
    
    print(f"\n📋 Model Architecture:")
    print(f"   Base Model: MobileNetV3-Small")
    print(f"   Input Size: 224x224")
    print(f"   Output Classes: {num_classes}")
    print(f"   Parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    # Training configuration
    num_epochs = 15  # Increased for better performance
    print(f"\n🎯 Training Configuration:")
    print(f"   Epochs: {num_epochs}")
    print(f"   Batch Size: 16")
    print(f"   Learning Rate: 0.001")
    print(f"   Optimizer: AdamW")
    print(f"   Scheduler: ReduceLROnPlateau (patience=2)")
    
    # Estimate training time
    print(f"\n⏱️  Time Estimation:")
    print(f"   Training samples: {len(train_loader.dataset)}")
    print(f"   Validation samples: {len(val_loader.dataset)}")
    print(f"   Batches per epoch: {len(train_loader)}")
    
    # Rough time estimate (assuming ~2s per batch on CPU, ~0.5s on GPU)
    if 'cuda' in str(device):
        estimated_time_per_epoch = len(train_loader) * 0.5  # seconds
    else:
        estimated_time_per_epoch = len(train_loader) * 2.0  # seconds
    
    total_estimated_time = estimated_time_per_epoch * num_epochs
    print(f"   Estimated time per epoch: {estimated_time_per_epoch/60:.1f} minutes")
    print(f"   Total estimated time: {total_estimated_time/60:.1f} minutes ({total_estimated_time/3600:.1f} hours)")
    
    # Ask for confirmation
    print(f"\n🚀 Ready to start training? (y/n): ", end="")
    response = input().lower().strip()
    
    if response not in ['y', 'yes']:
        print("❌ Training cancelled.")
        return
    
    # Start training
    print(f"\n🚀 Starting training...")
    print("=" * 60)
    
    start_time = time.time()
    
    try:
        # Train the model
        train_losses, val_losses = train_model(
            model=model,
            train_loader=train_loader,
            val_loader=val_loader,
            num_epochs=num_epochs,
            device=device,
            optimizer=optimizer,
            criterion=criterion,
            scheduler=scheduler
        )
        
        # Training completed successfully
        total_time = time.time() - start_time
        print(f"\n🎉 Training completed successfully!")
        print(f"⏱️  Total training time: {datetime.timedelta(seconds=int(total_time))}")
        print(f"💾 Model saved as: One_Piece_Model.pth")
        print(f"📊 Training curves saved as: training_curves.png")
        
        # Final statistics
        final_val_accuracy = 100 * (1 - val_losses[-1])
        print(f"📈 Final validation accuracy: {final_val_accuracy:.1f}%")
        
        if final_val_accuracy > 90:
            print("🌟 Excellent performance! Model is ready for deployment.")
        elif final_val_accuracy > 80:
            print("👍 Good performance! Model should work well.")
        else:
            print("⚠️  Performance could be improved. Consider training for more epochs.")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Training interrupted by user.")
        print(f"💾 Partial model saved as: One_Piece_Model.pth")
        
    except Exception as e:
        print(f"\n❌ Training failed with error: {e}")
        print("Please check the dataset path and try again.")

if __name__ == "__main__":
    main() 