#!/bin/bash
# Force Python 3.10 installation
echo "Installing Python 3.10.12..."
pyenv install 3.10.12
pyenv global 3.10.12

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt 