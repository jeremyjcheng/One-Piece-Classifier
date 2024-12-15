import torch
import torch.nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import timm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os

class OnePieceDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data = ImageFolder(data_dir, transform=transform)
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
    
    @property
    def classes(self):
        return self.data.classes


data_dir = '/Users/jeremycheng/Downloads/OnePieceDataset/Data/Data'

subdirs = [name for name in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, name))]

dataset = ImageFolder(data_dir)

target_to_class = {value: key for key, value in dataset.class_to_idx.items()}
print(target_to_class)
