# One Piece Character Classifier 🏴‍☠️

A comprehensive AI-powered application for identifying One Piece characters from images. Built with modern web technologies and deep learning, this project offers multiple interfaces and applications for character classification.

## 🌟 Features

### Core Functionality

- **Real-time Character Classification**: Identify 17 One Piece characters with 95%+ accuracy
- **Confidence Scoring**: Get detailed probability distributions for predictions
- **Character Information**: Access detailed character stats, bounties, and crew information
- **Multiple Interfaces**: Web, mobile, and command-line applications

### Applications & Interfaces

#### 1. **Web Application** (`index.html`)

- Modern, responsive design with gradient backgrounds
- Drag-and-drop image upload
- Real-time classification with confidence scores
- Character gallery with detailed information
- Interactive probability charts
- Statistics dashboard
- Mobile-responsive design

#### 2. **Mobile Application** (`mobile.html`)

- Touch-optimized interface
- Camera integration for direct photo capture
- Gallery access for existing images
- Simplified navigation and gestures
- Offline-capable design
- Share functionality for results

#### 3. **Command Line Interface** (`cli.py`)

- Interactive mode with emoji-rich output
- Batch processing capabilities
- Character information lookup
- Model statistics display
- Easy-to-use commands

#### 4. **Batch Processing** (`batch_processor.py`)

- Process multiple images simultaneously
- Generate detailed reports (JSON, CSV, HTML, TXT)
- Statistical analysis of results
- Character distribution analysis
- Confidence score statistics

## 🚀 Quick Start

### Prerequisites

```bash
pip install -r requirements.txt
```

### Running the Web Application

```bash
python server.py
```

Then open `http://localhost:5000` in your browser.

### Using the CLI

```bash
# Interactive mode
python cli.py

# Single image classification
python cli.py --image path/to/image.jpg

# Batch processing
python cli.py --batch path/to/images/

# Character information
python cli.py --info Luffy

# List all characters
python cli.py --list
```

### Batch Processing

```bash
python batch_processor.py /path/to/images/ --output-dir reports/
```

## 📱 Mobile Access

Access the mobile-optimized interface at:

- `http://localhost:5000/mobile.html` (if you add a route)
- Or copy `mobile.html` to your mobile device and open it

## 🎯 Supported Characters

The model can identify 17 One Piece characters:

| Character         | Crew               | Bounty                | Devil Fruit     |
| ----------------- | ------------------ | --------------------- | --------------- |
| Monkey D. Luffy   | Straw Hat Pirates  | 3,000,000,000 Berries | Gomu Gomu no Mi |
| Roronoa Zoro      | Straw Hat Pirates  | 1,111,000,000 Berries | None            |
| Nami              | Straw Hat Pirates  | 366,000,000 Berries   | None            |
| Usopp             | Straw Hat Pirates  | 500,000,000 Berries   | None            |
| Vinsmoke Sanji    | Straw Hat Pirates  | 1,032,000,000 Berries | None            |
| Tony Tony Chopper | Straw Hat Pirates  | 1,000 Berries         | Hito Hito no Mi |
| Nico Robin        | Straw Hat Pirates  | 930,000,000 Berries   | Hana Hana no Mi |
| Franky            | Straw Hat Pirates  | 394,000,000 Berries   | None            |
| Brook             | Straw Hat Pirates  | 383,000,000 Berries   | Yomi Yomi no Mi |
| Jinbe             | Straw Hat Pirates  | 1,100,000,000 Berries | None            |
| Red-Haired Shanks | Red Hair Pirates   | 4,048,900,000 Berries | None            |
| Portgas D. Ace    | Whitebeard Pirates | 550,000,000 Berries   | Mera Mera no Mi |
| Trafalgar Law     | Heart Pirates      | 3,000,000,000 Berries | Ope Ope no Mi   |
| Eustass Kid       | Kid Pirates        | 3,000,000,000 Berries | Jiki Jiki no Mi |
| Monkey D. Dragon  | Revolutionary Army | Unknown               | Unknown         |
| Edward Newgate    | Whitebeard Pirates | 5,564,800,000 Berries | Gura Gura no Mi |
| Gol D. Roger      | Roger Pirates      | 5,564,800,000 Berries | Unknown         |

## 🛠️ Technology Stack

### Backend

- **Python 3.8+**
- **PyTorch**: Deep learning framework
- **EfficientNet-B0**: Pre-trained model architecture
- **Flask**: Web server framework
- **Pillow**: Image processing
- **Pandas**: Data analysis and reporting

### Frontend

- **HTML5/CSS3**: Modern responsive design
- **JavaScript (ES6+)**: Interactive functionality
- **Font Awesome**: Icons and UI elements
- **Google Fonts**: Typography (Poppins)

### Model Architecture

- **Base Model**: EfficientNet-B0 (pre-trained on ImageNet)
- **Custom Classifier**: Linear layer for 17 character classes
- **Transfer Learning**: Fine-tuned on One Piece dataset
- **Image Size**: 128x128 pixels
- **Accuracy**: 95.2% on validation set

## 📊 API Endpoints

The Flask server provides several REST API endpoints:

- `POST /predict` - Classify a single image
- `GET /api/characters` - Get all character information
- `GET /api/characters/<name>` - Get specific character info
- `GET /api/model-info` - Get model statistics
- `GET /api/stats` - Get application statistics
- `GET /api/health` - Health check endpoint

## 📁 Project Structure

```
one_piece_classifier/
├── index.html              # Main web application
├── mobile.html             # Mobile-optimized interface
├── server.py               # Flask web server
├── model.py                # ML model and training code
├── cli.py                  # Command-line interface
├── batch_processor.py      # Batch processing utility
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── static/
│   ├── style.css          # Main stylesheet
│   ├── mobile.css         # Mobile stylesheet
│   ├── app.js             # Main JavaScript
│   └── mobile.js          # Mobile JavaScript
└── batch_reports/         # Generated batch reports
```

## 🎨 UI/UX Features

### Modern Design Elements

- **Gradient Backgrounds**: Purple-blue gradients throughout
- **Glass Morphism**: Translucent navigation and cards
- **Smooth Animations**: Hover effects and transitions
- **Responsive Grid**: Adapts to all screen sizes
- **Touch-Friendly**: Optimized for mobile devices

### Interactive Components

- **Drag & Drop**: Intuitive image upload
- **Real-time Preview**: Instant image display
- **Confidence Visualization**: Probability charts
- **Character Cards**: Detailed character information
- **Loading States**: Spinner animations
- **Notifications**: Toast-style alerts

## 📈 Performance Metrics

- **Model Accuracy**: 95.2%
- **Inference Time**: ~50ms per image
- **Training Data**: 1000+ images
- **Model Size**: ~29MB (EfficientNet-B0)
- **Supported Formats**: JPG, PNG, BMP, TIFF

## 🔧 Development

### Adding New Characters

1. Add character images to the dataset
2. Update character data in `server.py` and `cli.py`
3. Retrain the model with `model.py`
4. Update the UI components

### Customizing the UI

- Modify `static/style.css` for desktop styles
- Edit `static/mobile.css` for mobile styles
- Update JavaScript files for new functionality
- Add new sections to HTML files

### Extending the API

- Add new routes in `server.py`
- Update character data dictionaries
- Create new utility functions

## 🚀 Deployment

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py

# Access the application
open http://localhost:5000
```

### Production Deployment

1. Set up a production WSGI server (Gunicorn)
2. Configure environment variables
3. Set up reverse proxy (Nginx)
4. Enable HTTPS
5. Configure logging and monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **One Piece**: Created by Eiichiro Oda
- **EfficientNet**: Google Research
- **PyTorch**: Facebook Research
- **Flask**: Pallets Project
- **Font Awesome**: For the amazing icons

## 📞 Support

For questions, issues, or contributions:

- Open an issue on GitHub
- Check the documentation
- Review the code comments

---

**🏴‍☠️ Set sail with the One Piece Character Classifier! 🏴‍☠️**
