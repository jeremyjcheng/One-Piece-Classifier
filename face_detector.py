#!/usr/bin/env python3
import cv2
import numpy as np

class FaceDetector:
    def __init__(self):
        # Load pre-trained face detection model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def detect_faces(self, image):
        """Detect faces in the image"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        # If no faces detected, try with different parameters
        if len(faces) == 0:
            faces = self.face_cascade.detectMultiScale(
                gray, 
                scaleFactor=1.05, 
                minNeighbors=3, 
                minSize=(20, 20)
            )
        
        return faces
    
    def crop_face(self, image_path, target_size=(300, 400), padding=0.2):
        """Crop image to focus on the detected face"""
        # Read image
        if isinstance(image_path, str):
            image = cv2.imread(image_path)
        else:
            # If image_path is already an image array
            image = image_path
        
        if image is None:
            return None
        
        # Detect faces
        faces = self.detect_faces(image)
        
        if len(faces) == 0:
            # No face detected, return center crop
            height, width = image.shape[:2]
            center_x, center_y = width // 2, height // 2
            
            # Create a square crop around center
            crop_size = min(width, height) // 2
            x1 = max(0, center_x - crop_size)
            y1 = max(0, center_y - crop_size)
            x2 = min(width, center_x + crop_size)
            y2 = min(height, center_y + crop_size)
            
            cropped = image[y1:y2, x1:x2]
        else:
            # Use the largest face detected
            largest_face = max(faces, key=lambda x: x[2] * x[3])
            x, y, w, h = largest_face
            
            # Add padding around the face
            pad_x = int(w * padding)
            pad_y = int(h * padding)
            
            # Calculate crop coordinates with padding
            x1 = max(0, x - pad_x)
            y1 = max(0, y - pad_y)
            x2 = min(image.shape[1], x + w + pad_x)
            y2 = min(image.shape[0], y + h + pad_y)
            
            cropped = image[y1:y2, x1:x2]
        
        # Resize to target size
        resized = cv2.resize(cropped, target_size)
        
        return resized 