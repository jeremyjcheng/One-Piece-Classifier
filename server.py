from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS  # Import CORS
from PIL import Image
import io
import base64
from model import model, dataset, transform, device, predict

app = Flask(__name__, static_folder='.', static_url_path='')

# Enable CORS for all routes, including OPTIONS preflight requests
CORS(app)

# Serve index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static files (app.js, style.css)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

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

        return jsonify({'character': predicted_class}), 200

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
