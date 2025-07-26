#!/usr/bin/env python3
"""
Compatibility test script for One Piece Classifier
Tests all major dependencies to ensure they work with Python 3.13
"""

import sys
import importlib

def test_imports():
    """Test all major package imports"""
    packages = [
        'flask',
        'flask_cors',
        'PIL',
        'cv2',
        'numpy',
        'torch',
        'torchvision',
        'timm',
        'matplotlib',
        'sklearn',
        'pandas',
        'gunicorn'
    ]
    
    print("🧪 Testing package imports...")
    failed_imports = []
    
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed imports: {failed_imports}")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_torch_compatibility():
    """Test PyTorch compatibility"""
    print("\n🔥 Testing PyTorch compatibility...")
    
    try:
        import torch
        import torchvision
        
        print(f"✅ PyTorch version: {torch.__version__}")
        print(f"✅ TorchVision version: {torchvision.__version__}")
        print(f"✅ CUDA available: {torch.cuda.is_available()}")
        
        # Test basic tensor operations
        x = torch.randn(2, 3)
        y = torch.randn(2, 3)
        z = x + y
        print("✅ Basic tensor operations work")
        
        return True
    except Exception as e:
        print(f"❌ PyTorch test failed: {e}")
        return False

def test_model_loading():
    """Test model loading compatibility"""
    print("\n🤖 Testing model loading...")
    
    try:
        from model import model, dataset, transform, device
        
        print(f"✅ Model loaded successfully")
        print(f"✅ Device: {device}")
        print(f"✅ Number of classes: {len(dataset.data.classes)}")
        print(f"✅ Classes: {dataset.data.classes}")
        
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def test_face_detector():
    """Test face detector compatibility"""
    print("\n👤 Testing face detector...")
    
    try:
        from face_detector import FaceDetector
        
        detector = FaceDetector()
        print("✅ Face detector initialized successfully")
        
        return True
    except Exception as e:
        print(f"❌ Face detector failed: {e}")
        return False

def main():
    """Run all compatibility tests"""
    print("🚀 Starting compatibility tests for One Piece Classifier")
    print("=" * 60)
    
    tests = [
        ("Package Imports", test_imports),
        ("PyTorch Compatibility", test_torch_compatibility),
        ("Model Loading", test_model_loading),
        ("Face Detector", test_face_detector)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed!")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All compatibility tests passed! Your setup is ready for deployment.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 