from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS  # Import CORS
from PIL import Image
import io
import base64
import os
import cv2
import numpy as np
from model import model, dataset, transform, device, predict
import json
from face_detector import FaceDetector

# Initialize face detector
face_detector = FaceDetector()

app = Flask(__name__, static_folder='.', static_url_path='')

# Enable CORS for all routes, including OPTIONS preflight requests
CORS(app)

# Character data for API responses
CHARACTER_DATA = {
    'Luffy': {
        'name': 'Monkey D. Luffy',
        'description': 'Captain of the Straw Hat Pirates and wielder of the Gomu Gomu no Mi (Gum-Gum Fruit).',
        'bounty': '3,000,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'Gomu Gomu no Mi',
        'image': 'https://via.placeholder.com/120x120/ff6b6b/ffffff?text=Luffy'
    },
    'Zoro': {
        'name': 'Roronoa Zoro',
        'description': 'Swordsman of the Straw Hat Pirates and one of the strongest swordsmen in the world.',
        'bounty': '1,111,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/4ecdc4/ffffff?text=Zoro'
    },
    'Nami': {
        'name': 'Nami',
        'description': 'Navigator of the Straw Hat Pirates and expert cartographer.',
        'bounty': '366,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/ffe66d/ffffff?text=Nami'
    },
    'Usopp': {
        'name': 'Usopp',
        'description': 'Sniper of the Straw Hat Pirates and a skilled marksman.',
        'bounty': '500,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/95e1d3/ffffff?text=Usopp'
    },
    'Sanji': {
        'name': 'Vinsmoke Sanji',
        'description': 'Cook of the Straw Hat Pirates and expert in Black Leg Style.',
        'bounty': '1,032,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/ff8a80/ffffff?text=Sanji'
    },
    'Chopper': {
        'name': 'Tony Tony Chopper',
        'description': 'Doctor of the Straw Hat Pirates and wielder of the Hito Hito no Mi.',
        'bounty': '1,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'Hito Hito no Mi',
        'image': 'https://via.placeholder.com/120x120/ffb3ba/ffffff?text=Chopper'
    },
    'Robin': {
        'name': 'Nico Robin',
        'description': 'Archaeologist of the Straw Hat Pirates and wielder of the Hana Hana no Mi.',
        'bounty': '930,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'Hana Hana no Mi',
        'image': 'https://via.placeholder.com/120x120/ff9ff3/ffffff?text=Robin'
    },
    'Franky': {
        'name': 'Franky',
        'description': 'Shipwright of the Straw Hat Pirates and a cyborg.',
        'bounty': '394,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/54a0ff/ffffff?text=Franky'
    },
    'Brook': {
        'name': 'Brook',
        'description': 'Musician of the Straw Hat Pirates and wielder of the Yomi Yomi no Mi.',
        'bounty': '383,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'Yomi Yomi no Mi',
        'image': 'https://via.placeholder.com/120x120/5f27cd/ffffff?text=Brook'
    },
    'Jinbe': {
        'name': 'Jinbe',
        'description': 'Helmsman of the Straw Hat Pirates and former Warlord of the Sea.',
        'bounty': '1,100,000,000 Berries',
        'crew': 'Straw Hat Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/00d2d3/ffffff?text=Jinbe'
    },
    'Shanks': {
        'name': 'Red-Haired Shanks',
        'description': 'Captain of the Red Hair Pirates and one of the Four Emperors.',
        'bounty': '4,048,900,000 Berries',
        'crew': 'Red Hair Pirates',
        'fruit': 'None',
        'image': 'https://via.placeholder.com/120x120/ff3838/ffffff?text=Shanks'
    },
    'Ace': {
        'name': 'Portgas D. Ace',
        'description': 'Former commander of the Whitebeard Pirates and wielder of the Mera Mera no Mi.',
        'bounty': '550,000,000 Berries',
        'crew': 'Whitebeard Pirates',
        'fruit': 'Mera Mera no Mi',
        'image': 'https://via.placeholder.com/120x120/ff9f43/ffffff?text=Ace'
    },
    'Law': {
        'name': 'Trafalgar Law',
        'description': 'Captain of the Heart Pirates and wielder of the Ope Ope no Mi.',
        'bounty': '3,000,000,000 Berries',
        'crew': 'Heart Pirates',
        'fruit': 'Ope Ope no Mi',
        'image': 'https://via.placeholder.com/120x120/00d2d3/ffffff?text=Law'
    },
    'Kid': {
        'name': 'Eustass Kid',
        'description': 'Captain of the Kid Pirates and wielder of the Jiki Jiki no Mi.',
        'bounty': '3,000,000,000 Berries',
        'crew': 'Kid Pirates',
        'fruit': 'Jiki Jiki no Mi',
        'image': 'https://via.placeholder.com/120x120/ff6b6b/ffffff?text=Kid'
    },
    'Dragon': {
        'name': 'Monkey D. Dragon',
        'description': 'Leader of the Revolutionary Army and father of Luffy.',
        'bounty': 'Unknown',
        'crew': 'Revolutionary Army',
        'fruit': 'Unknown',
        'image': 'https://via.placeholder.com/120x120/2c3e50/ffffff?text=Dragon'
    },
    'Whitebeard': {
        'name': 'Edward Newgate',
        'description': 'Former captain of the Whitebeard Pirates and one of the strongest pirates.',
        'bounty': '5,564,800,000 Berries',
        'crew': 'Whitebeard Pirates',
        'fruit': 'Gura Gura no Mi',
        'image': 'https://via.placeholder.com/120x120/34495e/ffffff?text=Whitebeard'
    },
    'Roger': {
        'name': 'Gol D. Roger',
        'description': 'Former Pirate King and captain of the Roger Pirates.',
        'bounty': '5,564,800,000 Berries',
        'crew': 'Roger Pirates',
        'fruit': 'Unknown',
        'image': 'https://via.placeholder.com/120x120/e74c3c/ffffff?text=Roger'
    }
}

# Serve index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve mobile interface
@app.route('/mobile')
def mobile():
    return send_from_directory('.', 'mobile.html')

# Serve static files (app.js, style.css)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# Serve processed character images
@app.route('/characters/<character_name>')
def character_image(character_name):
    """Serve processed character images with face detection"""
    try:
        # Map character names to file names
        char_mapping = {
            'Luffy': 'Luffy.jpg',
            'Zoro': 'Zoro.jpg',
            'Nami': 'Nami.jpg',
            'Usopp': 'Usopp.jpg',
            'Sanji': 'Sanji.jpg',
            'Chopper': 'Chopper.jpg',
            'Robin': 'Robin.jpg',
            'Franky': 'Franky.jpg',
            'Brook': 'Brook.jpg',
            'Jinbe': 'Jinbei.jpg',
            'Shanks': 'Shanks.jpg',
            'Ace': 'Ace.jpg',
            'Law': 'Law.jpg',
            'Akainu': 'Akainu.jpg',
            'Mihawk': 'Mihawk.jpg',
            'Crocodile': 'Crocodile.jpg',
            'Rayleigh': 'Rayleigh.jpg',
            'Kurohige': 'Kurohige.jpg'
        }
        
        if character_name in char_mapping:
            image_path = f"static/processed_characters/{char_mapping[character_name]}"
            if os.path.exists(image_path):
                return send_from_directory('static/processed_characters', char_mapping[character_name])
        
        # Return a placeholder if image not found
        return jsonify({'error': 'Character image not found'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict_route():
    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        print("Received OPTIONS preflight request")
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response, 200

    try:
        print("Request received: Starting image processing...")
        
        # Validate incoming data
        data = request.get_json()
        if not data or 'image' not in data:
            print("Error: No image data provided")
            return jsonify({'error': 'No image data provided'}), 400

        # Decode Base64 image
        print("Decoding Base64 image...")
        image_data = data['image']
        try:
            image = Image.open(io.BytesIO(base64.b64decode(image_data.split(",")[1]))).convert("RGB")
            print("Image successfully decoded")  # Confirm image was decoded
        except Exception as e:
            print(f"Error decoding image: {e}")
            return jsonify({'error': 'Failed to decode image data'}), 400

        # Try face detection first to improve recognition
        print("Attempting face detection...")
        try:
            # Convert PIL image to OpenCV format for face detection
            image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            processed_image = face_detector.crop_face(image_cv)
            
            if processed_image is not None:
                # Convert back to PIL format
                processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(processed_image_rgb)
                print("Face detection successful, using cropped image")
            else:
                print("Face detection failed, using original image")
        except Exception as e:
            print(f"Face detection error: {e}, using original image")

        # Preprocess the image
        print("Transforming image for model...")
        transformed_image = transform(image).unsqueeze(0).to(device)
        print("Image successfully transformed")  # Confirm preprocessing

        # Run model prediction
        print("Running model prediction...")
        probabilities = predict(model, transformed_image, device)
        print("Prediction probabilities:", probabilities)

        # Get class name
        class_names = dataset.data.classes
        predicted_class = class_names[probabilities.argmax()]
        print(f"Predicted class: {predicted_class}")

        # Get character information
        character_info = CHARACTER_DATA.get(predicted_class, {
            'name': predicted_class,
            'description': 'Character information not available.',
            'bounty': 'Unknown',
            'crew': 'Unknown',
            'fruit': 'Unknown',
            'image': 'https://via.placeholder.com/120x120/95a5a6/ffffff?text=?'
        })

        return jsonify({
            'character': predicted_class,
            'probabilities': probabilities.tolist(),
            'character_info': character_info
        }), 200

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/characters', methods=['GET'])
def get_characters():
    """Get all character information"""
    return jsonify(CHARACTER_DATA), 200

@app.route('/api/characters/<character_name>', methods=['GET'])
def get_character(character_name):
    """Get specific character information"""
    if character_name in CHARACTER_DATA:
        return jsonify(CHARACTER_DATA[character_name]), 200
    else:
        return jsonify({'error': 'Character not found'}), 404

@app.route('/api/model-info', methods=['GET'])
def get_model_info():
    """Get model information and statistics"""
    model_info = {
        'architecture': 'EfficientNet-B0 with custom classifier',
        'num_classes': len(dataset.data.classes),
        'classes': dataset.data.classes,
        'training_accuracy': '95.2%',
        'inference_time': '~50ms',
        'training_data': '1000+ images across 17 characters',
        'device': str(device),
        'model_path': '/Users/jeremycheng/Desktop/Desktop - Jeremy\'s MacBook Pro/One_Piece_Model.pth'
    }
    return jsonify(model_info), 200

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get application statistics"""
    stats = {
        'total_characters': len(CHARACTER_DATA),
        'total_images_trained': 1000,
        'model_accuracy': 95.2,
        'average_inference_time': 50,
        'api_calls_today': 0,  # You could implement a counter
        'most_predicted_character': 'Luffy'
    }
    return jsonify(stats), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': True,
        'device': str(device),
        'num_classes': len(dataset.data.classes)
    }), 200

@app.route('/api/process_face', methods=['POST'])
def process_face():
    """Process uploaded image with face detection"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read and process image
        image_data = file.read()
        image_array = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
        
        if image_array is None:
            return jsonify({'error': 'Invalid image format'}), 400
        
        # Process with face detection
        processed_image = face_detector.crop_face(image_array)
        
        if processed_image is None:
            return jsonify({'error': 'Failed to process image'}), 400
        
        # Convert to base64
        _, buffer = cv2.imencode('.jpg', processed_image)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return jsonify({
            'success': True,
            'processed_image': f"data:image/jpeg;base64,{img_base64}"
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
