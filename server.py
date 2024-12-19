from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS
from PIL import Image
import io
import base64
from model import model, dataset, transform, device, predict

app = Flask(__name__, static_folder='.', static_url_path='')

# Enable CORS globally
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Serve index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static files
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# Prediction endpoint
@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict_route():
    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response, 200

    try:
        # Log request received
        print("Prediction request received")

        # Get image data
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        # Decode and process image
        image_data = data['image']
        image = Image.open(io.BytesIO(base64.b64decode(image_data.split(",")[1]))).convert("RGB")
        transformed_image = transform(image).unsqueeze(0).to(device)

        # Run model prediction
        probabilities = predict(model, transformed_image, device)
        class_names = dataset.data.classes
        predicted_class = class_names[probabilities.argmax()]
        print(f"Predicted class: {predicted_class}")

        # Add CORS headers to response
        response = jsonify({'character': predicted_class})
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    except Exception as e:
        print(f"Error: {e}")
        response = jsonify({'error': str(e)})
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response, 500

if __name__ == "__main__":
    app.run(debug=True)
