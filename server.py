from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
from model import model, dataset, transform, device, predict  # Import necessary components

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    image_data = data['image']

    # Convert Base64 string to PIL Image
    image = Image.open(io.BytesIO(base64.b64decode(image_data.split(",")[1]))).convert("RGB")

    # Transform the image for the model
    transformed_image = transform(image).unsqueeze(0).to(device)

    # Use the model to predict the character
    probabilities = predict(model, transformed_image, device)
    class_names = dataset.data.classes
    predicted_class = class_names[probabilities.argmax()]

    return jsonify({'character': predicted_class})

if __name__ == "__main__":
    app.run(debug=True)
