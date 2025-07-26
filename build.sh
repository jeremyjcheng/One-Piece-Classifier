#!/bin/bash
# Force Python 3.9 installation
echo "Installing Python 3.9..."
pyenv install 3.9.16
pyenv global 3.9.16

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt 