# One Piece Classifier
This is a web-based application designed to provide an engaging user experience by enabling users to upload images of One Piece characters. web-based application designed to provide an engaging user experience by enabling users to upload images of One Piece characters. 

Here is the link to the kaggle dataset: https://www.kaggle.com/datasets/ibrahimserouis99/one-piece-image-classifier

# Features
Drag-and-Drop Functionality: Users can easily upload images by dragging and dropping them onto the application or selecting them manually.
Real-Time Predictions: The application processes the uploaded image and predicts the character using a deep learning model.
Responsive Design: The user interface is optimized for various screen sizes, ensuring a seamless experience across devices.

# Technology Stack
Frontend: HTML, CSS, and JavaScript for the user interface.
Backend: Flask for handling API requests and serving the model.
Machine Learning: PyTorch for training and deploying a transfer learning model (EfficientNet-B0).
Dataset: Images of One Piece characters used for training, validation, and testing.

# How It Works
The user uploads an image of a One Piece character.
The image is preprocessed and sent to the backend API using a POST request.
The trained model processes the image and returns the predicted character's name.
The result is displayed on the interface.

# Installation and Setup
1. Clone the repository:
```git clone [<repository-url>](https://github.com/jeremyjcheng/One-Piece-Classifier)```
2. Navigate to the project directory:
```cd one_piece_classifier```
3. Install the required dependencies:
```pip install -r requirements.txt```
4. Start the Flask server:
```python server.py```
5. Open http://127.0.0.1:5000 in your web browser.

Model Training
The character classification model was trained using transfer learning with the EfficientNet-B0 architecture. The training process involved:

# Preprocessing the dataset (resizing and normalizing images).
Splitting the dataset into training, validation, and test sets.
Fine-tuning the pre-trained model to classify One Piece characters.

# Future Enhancements
Expand the dataset to include more characters and scenarios.
Add multi-language support to cater to a global audience.
Integrate additional deep learning techniques to improve model accuracy.
