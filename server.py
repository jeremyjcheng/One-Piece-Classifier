from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image
import io
import base64
from model import model, dataset, transform, device, predict

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Serve index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static files (app.js, style.css)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        image_data = data['image']
        image = Image.open(io.BytesIO(base64.b64decode(image_data.split(",")[1]))).convert("RGB")
        transformed_image = transform(image).unsqueeze(0).to(device)
        probabilities = predict(model, transformed_image, device)
        class_names = dataset.data.classes
        predicted_class = class_names[probabilities.argmax()]

        return jsonify({'character': predicted_class})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
