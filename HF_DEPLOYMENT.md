# Deploying to Hugging Face Spaces

This guide will help you deploy your One Piece Character Classifier to Hugging Face Spaces.

## 🚀 Quick Deployment Steps

### 1. **Create a Hugging Face Account**

- Go to [huggingface.co](https://huggingface.co)
- Sign up for a free account
- Verify your email

### 2. **Create a New Space**

- Click "New Space" on your profile
- Choose "Gradio" as the SDK
- Name it: `one-piece-classifier`
- Set visibility to "Public"
- Click "Create Space"

### 3. **Upload Your Code**

- Clone your repository to your local machine
- Push all files to the new Space repository
- The Space will automatically build and deploy

## 📁 Required Files for HF Spaces

Your repository should contain these files:

```
one_piece_classifier/
├── app.py                 # Main Flask application
├── model.py              # PyTorch model definition
├── face_detector.py      # OpenCV face detection
├── requirements.txt      # Python dependencies
├── One_Piece_Model.pth  # Trained model weights
├── index.html           # Main web interface
├── static/              # Static assets
│   ├── app.js          # Frontend JavaScript
│   ├── style.css       # Styling
│   └── gallery/        # Character images
├── README.md           # Project documentation
├── .gitattributes     # Git LFS configuration
└── HF_DEPLOYMENT.md   # This file
```

## 🔧 Configuration

### Port Configuration

- HF Spaces uses port `7860` by default
- The `app.py` file is configured to run on this port

### Model Loading

- The model file (`One_Piece_Model.pth`) will be loaded from the repository
- Make sure the model path in `model.py` is correct

### Dependencies

- All required packages are listed in `requirements.txt`
- HF Spaces will automatically install them

## 🎯 Deployment Process

### Step 1: Prepare Your Repository

```bash
# Make sure all files are committed
git add .
git commit -m "Prepare for HF Spaces deployment"
git push origin main
```

### Step 2: Create HF Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose "Gradio" SDK
4. Set Space name: `one-piece-classifier`
5. Set visibility to "Public"
6. Click "Create Space"

### Step 3: Connect Repository

1. In your new Space, go to "Settings"
2. Under "Repository", click "Connect to existing repository"
3. Select your GitHub repository
4. The Space will automatically sync and build

### Step 4: Monitor Deployment

1. Check the "Logs" tab for build progress
2. Wait for the build to complete (usually 5-10 minutes)
3. Your app will be available at: `https://huggingface.co/spaces/your-username/one-piece-classifier`

## 🔍 Troubleshooting

### Common Issues

#### 1. **Build Fails**

- Check the logs for error messages
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

#### 2. **Model Not Loading**

- Check if `One_Piece_Model.pth` is properly uploaded
- Verify the model path in `model.py`
- Ensure the model file is under 10GB (HF limit)

#### 3. **Port Issues**

- Make sure `app.py` runs on port `7860`
- Check that the host is set to `"0.0.0.0"`

#### 4. **Memory Issues**

- HF Spaces has memory limits
- Consider using a smaller model if needed
- Optimize image processing

### Debugging Tips

1. **Check Logs**: Always check the build logs first
2. **Test Locally**: Make sure it works locally before deploying
3. **Incremental Deployment**: Deploy in stages to isolate issues
4. **Monitor Resources**: Watch CPU/memory usage

## 📊 Performance Optimization

### For HF Spaces

- **Use CPU efficiently**: Optimize model inference
- **Minimize dependencies**: Only include necessary packages
- **Cache model**: Load model once at startup
- **Optimize images**: Compress static assets

### Recommended Settings

- **Hardware**: CPU (free tier) or GPU (paid)
- **Memory**: 16GB RAM recommended
- **Storage**: 50GB available

## 🌟 Features Available on HF Spaces

### Free Tier

- ✅ **CPU inference**
- ✅ **Basic monitoring**
- ✅ **Community features**
- ✅ **Git integration**
- ✅ **Custom domains**

### Pro Features (Paid)

- ✅ **GPU acceleration**
- ✅ **Higher memory limits**
- ✅ **Advanced monitoring**
- ✅ **Priority support**

## 🔗 Useful Links

- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [PyTorch Model Serving](https://pytorch.org/serve/)
- [OpenCV Installation](https://opencv-python-tutroals.readthedocs.io/)

## 🎉 Success!

Once deployed, your One Piece Character Classifier will be:

- 🌐 **Publicly accessible** at your HF Space URL
- 🤖 **Fully functional** with real AI predictions
- 📱 **Mobile responsive** for all devices
- 🚀 **Scalable** and reliable

Share your Space URL with the One Piece community! 🏴‍☠️
