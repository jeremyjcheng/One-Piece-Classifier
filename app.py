from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import base64
import io
from PIL import Image
import numpy as np
import cv2
import os
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model import model, dataset, transform, device, predict
from face_detector import FaceDetector

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

# Initialize model and face detector
print("Initializing model and face detector...")
face_detector = FaceDetector()
print("✅ Model and face detector initialized successfully!")

# Character data for additional info
CHARACTER_DATA = {
    "Luffy": {
        "name": "Monkey D. Luffy",
        "crew": "Straw Hat Pirates",
        "position": "Captain",
        "devil_fruit": "Gum-Gum Fruit (Gomu Gomu no Mi)",
        "bounty": "3,000,000,000 Berries"
    },
    "Zoro": {
        "name": "Roronoa Zoro",
        "crew": "Straw Hat Pirates", 
        "position": "Swordsman",
        "devil_fruit": "None",
        "bounty": "1,111,000,000 Berries"
    },
    "Nami": {
        "name": "Nami",
        "crew": "Straw Hat Pirates",
        "position": "Navigator",
        "devil_fruit": "None",
        "bounty": "366,000,000 Berries"
    },
    "Usopp": {
        "name": "Usopp",
        "crew": "Straw Hat Pirates",
        "position": "Sniper",
        "devil_fruit": "None",
        "bounty": "500,000,000 Berries"
    },
    "Sanji": {
        "name": "Vinsmoke Sanji",
        "crew": "Straw Hat Pirates",
        "position": "Cook",
        "devil_fruit": "None",
        "bounty": "1,032,000,000 Berries"
    },
    "Chopper": {
        "name": "Tony Tony Chopper",
        "crew": "Straw Hat Pirates",
        "position": "Doctor",
        "devil_fruit": "Human-Human Fruit (Hito Hito no Mi)",
        "bounty": "1,000 Berries"
    },
    "Robin": {
        "name": "Nico Robin",
        "crew": "Straw Hat Pirates",
        "position": "Archaeologist",
        "devil_fruit": "Flower-Flower Fruit (Hana Hana no Mi)",
        "bounty": "930,000,000 Berries"
    },
    "Franky": {
        "name": "Franky",
        "crew": "Straw Hat Pirates",
        "position": "Shipwright",
        "devil_fruit": "None",
        "bounty": "394,000,000 Berries"
    },
    "Brook": {
        "name": "Brook",
        "crew": "Straw Hat Pirates",
        "position": "Musician",
        "devil_fruit": "Revive-Revive Fruit (Yomi Yomi no Mi)",
        "bounty": "383,000,000 Berries"
    },
    "Jinbei": {
        "name": "Jinbei",
        "crew": "Straw Hat Pirates",
        "position": "Helmsman",
        "devil_fruit": "None",
        "bounty": "1,100,000,000 Berries"
    },
    "Ace": {
        "name": "Portgas D. Ace",
        "crew": "Whitebeard Pirates",
        "position": "2nd Division Commander",
        "devil_fruit": "Flame-Flame Fruit (Mera Mera no Mi)",
        "bounty": "550,000,000 Berries"
    },
    "Law": {
        "name": "Trafalgar Law",
        "crew": "Heart Pirates",
        "position": "Captain",
        "devil_fruit": "Op-Op Fruit (Ope Ope no Mi)",
        "bounty": "3,000,000,000 Berries"
    },
    "Shanks": {
        "name": "Red-Haired Shanks",
        "crew": "Red Hair Pirates",
        "position": "Captain",
        "devil_fruit": "None",
        "bounty": "4,048,900,000 Berries"
    },
    "Mihawk": {
        "name": "Dracule Mihawk",
        "crew": "None (Warlord)",
        "position": "Former Warlord",
        "devil_fruit": "None",
        "bounty": "3,590,000,000 Berries"
    },
    "Crocodile": {
        "name": "Sir Crocodile",
        "crew": "Cross Guild",
        "position": "Co-Leader",
        "devil_fruit": "Sand-Sand Fruit (Suna Suna no Mi)",
        "bounty": "1,965,000,000 Berries"
    },
    "Akainu": {
        "name": "Sakazuki (Akainu)",
        "crew": "Marines",
        "position": "Fleet Admiral",
        "devil_fruit": "Magma-Magma Fruit (Magu Magu no Mi)",
        "bounty": "Unknown"
    },
    "Kurohige": {
        "name": "Marshall D. Teach (Blackbeard)",
        "crew": "Blackbeard Pirates",
        "position": "Captain",
        "devil_fruit": "Dark-Dark Fruit (Yami Yami no Mi) + Tremor-Tremor Fruit (Gura Gura no Mi)",
        "bounty": "3,996,000,000 Berries"
    },
    "Rayleigh": {
        "name": "Silvers Rayleigh",
        "crew": "Roger Pirates (Former)",
        "position": "First Mate",
        "devil_fruit": "None",
        "bounty": "Unknown"
    }
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')



@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        print("Request received: Starting image processing...")
        data = request.get_json()
        
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Decode Base64 image
        print("Decoding Base64 image...")
        image_data = data['image']
        try:
            if ',' in image_data:
                base64_data = image_data.split(",")[1]
            else:
                base64_data = image_data
            image = Image.open(io.BytesIO(base64.b64decode(base64_data))).convert("RGB")
            print("Image successfully decoded")
        except Exception as e:
            print(f"Error decoding image: {e}")
            return jsonify({'error': 'Failed to decode image data'}), 400
        
        # Face detection
        print("Attempting face detection...")
        try:
            # Convert PIL to OpenCV format
            opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            face_detected, cropped_image = face_detector.detect_face(opencv_image)
            
            if face_detected:
                print("Face detection successful, using cropped image")
                # Convert back to PIL for model
                image = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
            else:
                print("No face detected, using original image")
        except Exception as e:
            print(f"Face detection error: {e}, using original image")
        
        # Transform image for model
        print("Transforming image for model...")
        try:
            transformed_image = transform(image).unsqueeze(0).to(device)
            print("Image successfully transformed")
        except Exception as e:
            print(f"Error transforming image: {e}")
            return jsonify({'error': 'Failed to process image for model'}), 400
        
        # Run prediction
        print("Running model prediction...")
        try:
            probabilities = predict(model, transformed_image, device)
            class_names = dataset.data.classes
            predicted_class = class_names[probabilities.argmax().item()]
            print(f"Prediction probabilities: {probabilities.cpu().numpy()}")
            print(f"Predicted class: {predicted_class}")
        except Exception as e:
            print(f"Error during prediction: {e}")
            return jsonify({'error': 'Failed to run prediction'}), 500
        
        # Get character info
        character_info = CHARACTER_DATA.get(predicted_class, {})
        
        # Calculate confidence (max probability)
        confidence = probabilities.max().item()
        
        return jsonify({
            'success': True,
            'character': predicted_class,
            'confidence': confidence,
            'probabilities': probabilities.cpu().numpy().tolist(),
            'character_info': character_info
        })
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/model-info')
def model_info():
    return jsonify({
        'model_path': 'One_Piece_Model.pth',
        'model_type': 'MobileNetV2',
        'num_classes': len(dataset.data.classes),
        'classes': dataset.data.classes,
        'device': str(device)
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'face_detector_loaded': face_detector is not None
    })

@app.route('/api/process_face', methods=['POST'])
def process_face():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Decode image
        image_data = data['image']
        if ',' in image_data:
            base64_data = image_data.split(",")[1]
        else:
            base64_data = image_data
        
        image = Image.open(io.BytesIO(base64.b64decode(base64_data))).convert("RGB")
        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Detect face
        face_detected, cropped_image = face_detector.detect_face(opencv_image)
        
        if face_detected:
            # Convert back to base64
            pil_image = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
            buffer = io.BytesIO()
            pil_image.save(buffer, format='JPEG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            
            return jsonify({
                'success': True,
                'face_detected': True,
                'processed_image': f"data:image/jpeg;base64,{img_str}"
            })
        else:
            return jsonify({
                'success': True,
                'face_detected': False,
                'message': 'No face detected in image'
            })
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5001))) 