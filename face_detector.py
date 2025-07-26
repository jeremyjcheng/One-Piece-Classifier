#!/usr/bin/env python3
import cv2
import numpy as np
import os

class FaceDetector:
    def __init__(self):
        # Load multiple pre-trained face detection models for better detection
        self.face_cascades = []
        self.face_net = None
        
        # Try to load different cascade classifiers
        cascade_paths = [
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml',
            cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml',
            cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml',
            cv2.data.haarcascades + 'haarcascade_frontalface_alt_tree.xml'
        ]
        
        for path in cascade_paths:
            if os.path.exists(path):
                cascade = cv2.CascadeClassifier(path)
                if not cascade.empty():
                    self.face_cascades.append(cascade)
        
        # Try to load DNN-based face detection (more accurate)
        try:
            # Load pre-trained face detection model
            model_path = cv2.data.haarcascades.replace('haarcascades', 'dnn_face_detector')
            if os.path.exists(model_path):
                self.face_net = cv2.dnn.readNet(
                    os.path.join(model_path, 'opencv_face_detector_uint8.pb'),
                    os.path.join(model_path, 'opencv_face_detector.pbtxt')
                )
        except:
            pass
        
        # If no cascades loaded, try alternative path
        if not self.face_cascades:
            try:
                # Try to load from OpenCV installation
                cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                if not cascade.empty():
                    self.face_cascades.append(cascade)
            except:
                pass
        
        # If still no cascades, create a dummy one
        if not self.face_cascades:
            print("Warning: No face cascade classifiers found. Face detection will be disabled.")
            self.face_cascades = []
    
    def detect_faces_dnn(self, image):
        """Detect faces using DNN-based model (more accurate)"""
        if self.face_net is None:
            return []
        
        try:
            height, width = image.shape[:2]
            
            # Create blob from image
            blob = cv2.dnn.blobFromImage(
                image, 1.0, (300, 300), [104, 117, 123], False, False
            )
            
            # Set input and get detections
            self.face_net.setInput(blob)
            detections = self.face_net.forward()
            
            faces = []
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                
                if confidence > 0.5:  # Confidence threshold
                    # Get bounding box coordinates
                    box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                    x, y, w, h = box.astype(int)
                    
                    # Ensure coordinates are within image bounds
                    x = max(0, x)
                    y = max(0, y)
                    w = min(w, width - x)
                    h = min(h, height - y)
                    
                    if w > 0 and h > 0:
                        faces.append((x, y, w, h))
            
            return faces
            
        except Exception as e:
            print(f"DNN face detection error: {e}")
            return []
    
    def detect_faces_cascade(self, image):
        """Detect faces using cascade classifiers"""
        if not self.face_cascades:
            return []
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        all_faces = []
        
        # Try different parameters for each cascade
        parameters_list = [
            {'scaleFactor': 1.1, 'minNeighbors': 5, 'minSize': (30, 30)},
            {'scaleFactor': 1.05, 'minNeighbors': 3, 'minSize': (20, 20)},
            {'scaleFactor': 1.2, 'minNeighbors': 4, 'minSize': (25, 25)},
            {'scaleFactor': 1.15, 'minNeighbors': 6, 'minSize': (35, 35)},
            {'scaleFactor': 1.08, 'minNeighbors': 4, 'minSize': (40, 40)},
            {'scaleFactor': 1.12, 'minNeighbors': 7, 'minSize': (50, 50)}
        ]
        
        for cascade in self.face_cascades:
            for params in parameters_list:
                faces = cascade.detectMultiScale(
                    gray,
                    scaleFactor=params['scaleFactor'],
                    minNeighbors=params['minNeighbors'],
                    minSize=params['minSize']
                )
                
                if len(faces) > 0:
                    all_faces.extend(faces)
        
        # Remove duplicate detections
        if all_faces:
            faces_list = [tuple(face) for face in all_faces]
            filtered_faces = []
            
            for face in faces_list:
                x, y, w, h = face
                is_duplicate = False
                
                for existing_face in filtered_faces:
                    ex, ey, ew, eh = existing_face
                    # Check if faces overlap significantly
                    overlap_x = max(0, min(x + w, ex + ew) - max(x, ex))
                    overlap_y = max(0, min(y + h, ey + eh) - max(y, ey))
                    overlap_area = overlap_x * overlap_y
                    
                    if overlap_area > 0.5 * min(w * h, ew * eh):
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    filtered_faces.append(face)
            
            return filtered_faces
        
        return []
    
    def detect_faces(self, image):
        """Detect faces using DNN first, fallback to cascade"""
        # Try DNN first (more accurate)
        faces = self.detect_faces_dnn(image)
        
        # If no faces found, try cascade
        if len(faces) == 0:
            faces = self.detect_faces_cascade(image)
        
        return faces
    
    def _get_optimal_crop(self, image, faces):
        """Get optimal crop that ensures faces are well-positioned with more context"""
        height, width = image.shape[:2]
        
        if len(faces) == 0:
            # No faces detected, use center crop with more context
            return self._center_crop_with_context(image)
        
        # Use the largest face detected
        largest_face = max(faces, key=lambda x: x[2] * x[3])
        x, y, w, h = largest_face
        
        # Calculate optimal padding to ensure face is well-centered
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        
        # Calculate crop dimensions with much more context around the face
        crop_width = max(w * 4, width // 2)  # 4x face width for more context
        crop_height = max(h * 5, height // 2)  # 5x face height for better framing
        
        # Calculate crop coordinates to center the face
        crop_x = max(0, face_center_x - crop_width // 2)
        crop_y = max(0, face_center_y - crop_height // 2)
        
        # Ensure crop doesn't exceed image boundaries
        crop_x2 = min(width, crop_x + crop_width)
        crop_y2 = min(height, crop_y + crop_height)
        
        # Adjust if we hit boundaries
        if crop_x2 == width:
            crop_x = max(0, width - crop_width)
        if crop_y2 == height:
            crop_y = max(0, height - crop_height)
        
        # Ensure all coordinates are integers
        crop_x = int(crop_x)
        crop_y = int(crop_y)
        crop_x2 = int(crop_x2)
        crop_y2 = int(crop_y2)
        
        return image[crop_y:crop_y2, crop_x:crop_x2]
    
    def _center_crop_with_context(self, image):
        """Create a center crop with more context when no faces are detected"""
        height, width = image.shape[:2]
        center_x, center_y = width // 2, height // 2
        
        # Create a larger crop around center for more context
        crop_size = min(width, height) * 0.9  # 90% of the smaller dimension
        crop_size = int(crop_size)  # Ensure integer
        x1 = max(0, center_x - crop_size // 2)
        y1 = max(0, center_y - crop_size // 2)
        x2 = min(width, center_x + crop_size // 2)
        y2 = min(height, center_y + crop_size // 2)
        
        return image[y1:y2, x1:x2]
    
    def crop_face(self, image_path, target_size=(300, 400), padding=0.2):
        """Crop image to focus on the detected face with optimal positioning"""
        try:
            # Read image
            if isinstance(image_path, str):
                image = cv2.imread(image_path)
            else:
                # If image_path is already an image array
                image = image_path
            
            if image is None:
                print("Error: Could not read image")
                return None
            
            # Detect faces using improved detection
            faces = self.detect_faces(image)
            
            # Get optimal crop with more context
            cropped = self._get_optimal_crop(image, faces)
            
            # Ensure we have a valid crop
            if cropped.size == 0:
                print("Error: Empty crop detected")
                return None
            
            # Resize to target size while maintaining aspect ratio
            h, w = cropped.shape[:2]
            target_w, target_h = target_size
            
            # Calculate scaling to fit in target size
            scale = min(target_w / w, target_h / h)
            new_w = int(w * scale)
            new_h = int(h * scale)
            
            # Resize
            resized = cv2.resize(cropped, (new_w, new_h))
            
            # Create final image with target size and center the resized image
            final_image = np.zeros((target_h, target_w, 3), dtype=np.uint8)
            
            # Calculate position to center the resized image
            y_offset = (target_h - new_h) // 2
            x_offset = (target_w - new_w) // 2
            
            # Place the resized image in the center
            final_image[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
            
            return final_image
            
        except Exception as e:
            print(f"Error in crop_face: {e}")
            return None 