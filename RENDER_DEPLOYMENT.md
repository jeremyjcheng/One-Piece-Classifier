# 🚀 One Piece Character Classifier - Render Deployment Guide

## Overview

This guide will help you deploy your One Piece Character Classifier to Render, a cloud platform that's perfect for ML applications with large model files.

## ✅ Why Render?

- **No file size limits** (unlike Hugging Face Spaces)
- **Better ML support** with full Python environment
- **Automatic HTTPS** and custom domains
- **Free tier available** for testing
- **Easy Git integration**

## 📋 Prerequisites

1. **Render Account**: Sign up at [render.com](https://render.com)
2. **GitHub Repository**: Your code should be on GitHub
3. **Model File**: Ensure `One_Piece_Model.pth` is in your repo

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository

Your repository should contain:

```
one_piece_classifier/
├── app.py                 # Main Flask application
├── model.py              # Model loading and prediction
├── face_detector.py      # Face detection utilities
├── requirements.txt      # Python dependencies
├── render.yaml          # Render configuration
├── One_Piece_Model.pth  # Trained model (8.8MB)
├── static/              # Frontend assets
│   ├── style.css
│   ├── app.js
│   └── gallery/
├── index.html           # Main interface
└── README.md           # Documentation
```

### Step 2: Connect to Render

1. **Login to Render**: Go to [dashboard.render.com](https://dashboard.render.com)
2. **New Web Service**: Click "New" → "Web Service"
3. **Connect Repository**:
   - Choose "Connect a repository"
   - Select your GitHub repo
   - Grant Render access if needed

### Step 3: Configure the Service

Fill in these settings:

**Basic Settings:**

- **Name**: `one-piece-classifier`
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)

**Build & Deploy Settings:**

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Auto-Deploy**: ✅ Enabled

**Environment Variables:**

- `PYTHON_VERSION`: `3.9.16`

### Step 4: Deploy

1. **Click "Create Web Service"**
2. **Wait for Build**: This takes 5-10 minutes
3. **Monitor Logs**: Check the build logs for any errors

## 🔧 Configuration Files

### render.yaml

```yaml
services:
  - type: web
    name: one-piece-classifier
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
```

### app.py

- Uses `gunicorn` for production
- Handles environment variables
- Compatible with Render's Python environment

### requirements.txt

- Includes `gunicorn` for production server
- All ML dependencies (PyTorch, OpenCV, etc.)
- Specific versions for stability

## 🌐 Access Your App

After successful deployment:

- **URL**: `https://your-app-name.onrender.com`
- **Custom Domain**: Add in Render dashboard
- **HTTPS**: Automatically enabled

## 📊 Monitoring

- **Logs**: Available in Render dashboard
- **Metrics**: Response times, errors, etc.
- **Uptime**: 99.9% SLA on paid plans

## 🔄 Updates

To update your app:

1. **Push to GitHub**: `git push origin main`
2. **Auto-deploy**: Render automatically rebuilds
3. **Manual deploy**: Available in dashboard

## 🛠️ Troubleshooting

### Common Issues:

**1. Build Failures**

- Check `requirements.txt` for version conflicts
- Ensure all dependencies are listed
- Check Python version compatibility

**2. Model Loading Errors**

- Verify `One_Piece_Model.pth` is in repository
- Check file permissions
- Ensure model path is correct in code

**3. Memory Issues**

- Upgrade to paid plan for more RAM
- Optimize model loading
- Consider model compression

**4. Timeout Errors**

- Increase timeout in Render settings
- Optimize model inference
- Use caching for repeated requests

### Debug Commands:

```bash
# Check local build
pip install -r requirements.txt
python app.py

# Test model loading
python -c "from model import load_model; load_model()"

# Verify file structure
ls -la
du -sh One_Piece_Model.pth
```

## 💰 Pricing

- **Free Tier**: 750 hours/month, 512MB RAM
- **Paid Plans**: From $7/month for more resources
- **Custom Plans**: For high-traffic applications

## 🎯 Best Practices

1. **Use specific versions** in requirements.txt
2. **Test locally** before deploying
3. **Monitor logs** after deployment
4. **Set up alerts** for errors
5. **Use environment variables** for secrets

## 🆘 Support

- **Render Docs**: [docs.render.com](https://docs.render.com)
- **Community**: [Render Community](https://community.render.com)
- **Status**: [status.render.com](https://status.render.com)

## 🎉 Success!

Your One Piece Character Classifier will be live at:
`https://your-app-name.onrender.com`

The app will automatically:

- Load your trained model
- Handle face detection
- Provide character predictions
- Serve the beautiful UI

Happy deploying! 🏴‍☠️
