#!/bin/bash
# Force Python 3.13 installation
echo "Installing Python 3.13.4..."
pyenv install 3.13.4
pyenv global 3.13.4

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt 