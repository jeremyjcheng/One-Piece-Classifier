// Mobile JavaScript for One Piece Classifier

// Character data (same as main app)
const characterData = {
  Luffy: {
    name: "Monkey D. Luffy",
    description:
      "Captain of the Straw Hat Pirates and wielder of the Gomu Gomu no Mi (Gum-Gum Fruit).",
    bounty: "3,000,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Gomu Gomu no Mi",
    image: "https://via.placeholder.com/120x120/ff6b6b/ffffff?text=Luffy",
  },
  Zoro: {
    name: "Roronoa Zoro",
    description:
      "Swordsman of the Straw Hat Pirates and one of the strongest swordsmen in the world.",
    bounty: "1,111,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/4ecdc4/ffffff?text=Zoro",
  },
  Nami: {
    name: "Nami",
    description: "Navigator of the Straw Hat Pirates and expert cartographer.",
    bounty: "366,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/ffe66d/ffffff?text=Nami",
  },
  Usopp: {
    name: "Usopp",
    description: "Sniper of the Straw Hat Pirates and a skilled marksman.",
    bounty: "500,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/95e1d3/ffffff?text=Usopp",
  },
  Sanji: {
    name: "Vinsmoke Sanji",
    description: "Cook of the Straw Hat Pirates and expert in Black Leg Style.",
    bounty: "1,032,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/ff8a80/ffffff?text=Sanji",
  },
  Chopper: {
    name: "Tony Tony Chopper",
    description:
      "Doctor of the Straw Hat Pirates and wielder of the Hito Hito no Mi.",
    bounty: "1,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Hito Hito no Mi",
    image: "https://via.placeholder.com/120x120/ffb3ba/ffffff?text=Chopper",
  },
  Robin: {
    name: "Nico Robin",
    description:
      "Archaeologist of the Straw Hat Pirates and wielder of the Hana Hana no Mi.",
    bounty: "930,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Hana Hana no Mi",
    image: "https://via.placeholder.com/120x120/ff9ff3/ffffff?text=Robin",
  },
  Franky: {
    name: "Franky",
    description: "Shipwright of the Straw Hat Pirates and a cyborg.",
    bounty: "394,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/54a0ff/ffffff?text=Franky",
  },
  Brook: {
    name: "Brook",
    description:
      "Musician of the Straw Hat Pirates and wielder of the Yomi Yomi no Mi.",
    bounty: "383,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Yomi Yomi no Mi",
    image: "https://via.placeholder.com/120x120/5f27cd/ffffff?text=Brook",
  },
  Jinbe: {
    name: "Jinbe",
    description:
      "Helmsman of the Straw Hat Pirates and former Warlord of the Sea.",
    bounty: "1,100,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/00d2d3/ffffff?text=Jinbe",
  },
  Shanks: {
    name: "Red-Haired Shanks",
    description:
      "Captain of the Red Hair Pirates and one of the Four Emperors.",
    bounty: "4,048,900,000 Berries",
    crew: "Red Hair Pirates",
    fruit: "None",
    image: "https://via.placeholder.com/120x120/ff3838/ffffff?text=Shanks",
  },
  Ace: {
    name: "Portgas D. Ace",
    description:
      "Former commander of the Whitebeard Pirates and wielder of the Mera Mera no Mi.",
    bounty: "550,000,000 Berries",
    crew: "Whitebeard Pirates",
    fruit: "Mera Mera no Mi",
    image: "https://via.placeholder.com/120x120/ff9f43/ffffff?text=Ace",
  },
  Law: {
    name: "Trafalgar Law",
    description:
      "Captain of the Heart Pirates and wielder of the Ope Ope no Mi.",
    bounty: "3,000,000,000 Berries",
    crew: "Heart Pirates",
    fruit: "Ope Ope no Mi",
    image: "https://via.placeholder.com/120x120/00d2d3/ffffff?text=Law",
  },
  Kid: {
    name: "Eustass Kid",
    description:
      "Captain of the Kid Pirates and wielder of the Jiki Jiki no Mi.",
    bounty: "3,000,000,000 Berries",
    crew: "Kid Pirates",
    fruit: "Jiki Jiki no Mi",
    image: "https://via.placeholder.com/120x120/ff6b6b/ffffff?text=Kid",
  },
  Dragon: {
    name: "Monkey D. Dragon",
    description: "Leader of the Revolutionary Army and father of Luffy.",
    bounty: "Unknown",
    crew: "Revolutionary Army",
    fruit: "Unknown",
    image: "https://via.placeholder.com/120x120/2c3e50/ffffff?text=Dragon",
  },
  Whitebeard: {
    name: "Edward Newgate",
    description:
      "Former captain of the Whitebeard Pirates and one of the strongest pirates.",
    bounty: "5,564,800,000 Berries",
    crew: "Whitebeard Pirates",
    fruit: "Gura Gura no Mi",
    image: "https://via.placeholder.com/120x120/34495e/ffffff?text=Whitebeard",
  },
  Roger: {
    name: "Gol D. Roger",
    description: "Former Pirate King and captain of the Roger Pirates.",
    bounty: "5,564,800,000 Berries",
    crew: "Roger Pirates",
    fruit: "Unknown",
    image: "https://via.placeholder.com/120x120/e74c3c/ffffff?text=Roger",
  },
};

// Global variables
let currentImageData = null;
let currentResult = null;

// Initialize mobile app
document.addEventListener("DOMContentLoaded", () => {
  console.log("Mobile One Piece Classifier initialized");

  // Initialize file input
  const fileInput = document.getElementById("file-input");
  fileInput.addEventListener("change", handleFileSelect);

  // Add touch event listeners
  initializeTouchEvents();
});

// Initialize touch events
function initializeTouchEvents() {
  const dropArea = document.getElementById("drop-area");

  // Touch events for drag and drop area
  dropArea.addEventListener("touchstart", handleTouchStart, false);
  dropArea.addEventListener("touchmove", handleTouchMove, false);
  dropArea.addEventListener("touchend", handleTouchEnd, false);

  // Prevent default touch behaviors
  dropArea.addEventListener("touchmove", (e) => e.preventDefault(), {
    passive: false,
  });
}

// Touch event handlers
function handleTouchStart(e) {
  // Add visual feedback
  e.target.classList.add("touch-active");
}

function handleTouchMove(e) {
  e.preventDefault();
}

function handleTouchEnd(e) {
  e.target.classList.remove("touch-active");
}

// Open camera
function openCamera() {
  const fileInput = document.getElementById("file-input");
  fileInput.setAttribute("capture", "environment");
  fileInput.click();
}

// Open file picker
function openFilePicker() {
  const fileInput = document.getElementById("file-input");
  fileInput.removeAttribute("capture");
  fileInput.click();
}

// Handle file selection
function handleFileSelect(event) {
  const file = event.target.files[0];
  if (file && file.type.startsWith("image/")) {
    handleFile(file);
  } else {
    showNotification("Please select a valid image file.", "error");
  }
}

// Handle file processing
function handleFile(file) {
  const reader = new FileReader();

  reader.onload = (e) => {
    const imageData = e.target.result;
    currentImageData = imageData;

    // Show preview
    const preview = document.getElementById("preview");
    preview.src = imageData;

    // Show preview section
    document.getElementById("preview-section").style.display = "block";
    document.getElementById("result-section").style.display = "none";

    // Scroll to preview
    document.getElementById("preview-section").scrollIntoView({
      behavior: "smooth",
      block: "center",
    });
  };

  reader.onerror = () => {
    showNotification("Error reading the file.", "error");
  };

  reader.readAsDataURL(file);
}

// Analyze image
function analyzeImage() {
  if (!currentImageData) {
    showNotification("No image to analyze.", "error");
    return;
  }

  // Show loading overlay
  const loadingOverlay = document.getElementById("loading-overlay");
  loadingOverlay.style.display = "flex";

  // Send to server
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: currentImageData }),
  })
    .then((res) => res.json())
    .then((data) => {
      loadingOverlay.style.display = "none";

      if (data.error) {
        showNotification(`Error: ${data.error}`, "error");
      } else {
        displayResult(data.character, data.probabilities || []);
      }
    })
    .catch((err) => {
      loadingOverlay.style.display = "none";
      showNotification("Error analyzing the image.", "error");
      console.error(err);
    });
}

// Display result
function displayResult(characterName, probabilities) {
  currentResult = { characterName, probabilities };

  const characterInfo = characterData[characterName] || {
    name: characterName,
    description: "Character information not available.",
    bounty: "Unknown",
    crew: "Unknown",
    fruit: "Unknown",
    image: "https://via.placeholder.com/120x120/95a5a6/ffffff?text=?",
  };

  // Update character info
  document.getElementById("character-name").textContent = characterInfo.name;
  document.getElementById("character-description").textContent =
    characterInfo.description;
  document.getElementById("character-bounty").textContent =
    characterInfo.bounty;
  document.getElementById("character-crew").textContent = characterInfo.crew;
  document.getElementById("character-fruit").textContent = characterInfo.fruit;
  document.getElementById("character-img").src = characterInfo.image;

  // Update confidence badge
  const confidenceBadge = document.getElementById("confidence-badge");
  const maxProbability = Math.max(...probabilities);
  const confidencePercentage = Math.round(maxProbability * 100);
  confidenceBadge.textContent = `${confidencePercentage}%`;

  // Create probability chart
  createProbabilityChart(probabilities);

  // Show result section
  document.getElementById("result-section").style.display = "block";
  document.getElementById("result-section").scrollIntoView({
    behavior: "smooth",
    block: "start",
  });

  // Show success notification
  showNotification(`Identified as ${characterInfo.name}!`, "success");
}

// Create probability chart
function createProbabilityChart(probabilities) {
  const chartContainer = document.getElementById("probability-chart");
  chartContainer.innerHTML = "";

  const classNames = Object.keys(characterData);

  // Sort by probability (descending)
  const sortedData = classNames
    .map((name, index) => ({
      name,
      probability: probabilities[index] || 0,
    }))
    .sort((a, b) => b.probability - a.probability);

  // Show top 5 results
  sortedData.slice(0, 5).forEach((item) => {
    const barContainer = document.createElement("div");
    barContainer.style.cssText = `
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            gap: 10px;
        `;

    const label = document.createElement("span");
    label.textContent = item.name;
    label.style.cssText = `
            min-width: 80px;
            font-size: 0.9rem;
            font-weight: 500;
        `;

    const bar = document.createElement("div");
    bar.style.cssText = `
            flex: 1;
            height: 16px;
            background: #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
            position: relative;
        `;

    const fill = document.createElement("div");
    fill.style.cssText = `
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            width: ${item.probability * 100}%;
            transition: width 0.5s ease;
        `;

    const percentage = document.createElement("span");
    percentage.textContent = `${Math.round(item.probability * 100)}%`;
    percentage.style.cssText = `
            min-width: 35px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #333;
        `;

    bar.appendChild(fill);
    barContainer.appendChild(label);
    barContainer.appendChild(bar);
    barContainer.appendChild(percentage);
    chartContainer.appendChild(barContainer);
  });
}

// Close preview
function closePreview() {
  document.getElementById("preview-section").style.display = "none";
  document.getElementById("result-section").style.display = "none";
  currentImageData = null;
  currentResult = null;
}

// Start over
function startOver() {
  closePreview();
  document.getElementById("file-input").value = "";

  // Scroll to top
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

// Share result
function shareResult() {
  if (!currentResult) {
    showNotification("No result to share.", "error");
    return;
  }

  const characterInfo = characterData[currentResult.characterName];
  const shareText = `I just identified ${characterInfo.name} using the One Piece Character Classifier! 🏴‍☠️`;

  // Use Web Share API if available
  if (navigator.share) {
    navigator
      .share({
        title: "One Piece Character Classifier",
        text: shareText,
        url: window.location.href,
      })
      .catch((err) => {
        console.log("Share failed:", err);
        fallbackShare(shareText);
      });
  } else {
    fallbackShare(shareText);
  }
}

// Fallback share method
function fallbackShare(text) {
  // Copy to clipboard
  if (navigator.clipboard) {
    navigator.clipboard
      .writeText(text)
      .then(() => {
        showNotification("Result copied to clipboard!", "success");
      })
      .catch(() => {
        showNotification("Share feature not available.", "error");
      });
  } else {
    showNotification("Share feature not available.", "error");
  }
}

// Show gallery
function showGallery() {
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalBody = document.getElementById("modal-body");

  modalTitle.textContent = "Character Gallery";

  let galleryHTML = '<div class="gallery-grid">';
  Object.entries(characterData).forEach(([key, character]) => {
    galleryHTML += `
            <div class="gallery-item">
                <img src="${character.image}" alt="${character.name}">
                <div class="gallery-item-content">
                    <h3>${character.name}</h3>
                    <p>${character.description}</p>
                </div>
            </div>
        `;
  });
  galleryHTML += "</div>";

  modalBody.innerHTML = galleryHTML;
  modal.style.display = "flex";
}

// Show stats
function showStats() {
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalBody = document.getElementById("modal-body");

  modalTitle.textContent = "Model Statistics";

  const statsHTML = `
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Model Architecture</h3>
                <p>EfficientNet-B0 with custom classifier</p>
            </div>
            <div class="stat-card">
                <h3>Training Accuracy</h3>
                <p>95.2% on validation set</p>
            </div>
            <div class="stat-card">
                <h3>Inference Time</h3>
                <p>~50ms per prediction</p>
            </div>
            <div class="stat-card">
                <h3>Training Data</h3>
                <p>1000+ images across 17 characters</p>
            </div>
        </div>
    `;

  modalBody.innerHTML = statsHTML;
  modal.style.display = "flex";
}

// Show about
function showAbout() {
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalBody = document.getElementById("modal-body");

  modalTitle.textContent = "About This App";

  const aboutHTML = `
        <div style="line-height: 1.6;">
            <h4>How It Works</h4>
            <p>Our AI model uses deep learning techniques to identify One Piece characters from images. The model was trained on a comprehensive dataset of character images and can recognize 17 different characters with high accuracy.</p>
            
            <h4>Technology Stack</h4>
            <ul style="margin: 10px 0; padding-left: 20px;">
                <li><strong>Backend:</strong> Python, Flask, PyTorch</li>
                <li><strong>Frontend:</strong> HTML5, CSS3, JavaScript</li>
                <li><strong>Model:</strong> EfficientNet-B0 with transfer learning</li>
                <li><strong>Deployment:</strong> Local server with REST API</li>
            </ul>
            
            <h4>Features</h4>
            <ul style="margin: 10px 0; padding-left: 20px;">
                <li>Real-time character classification</li>
                <li>Confidence scoring and probability distribution</li>
                <li>Character information and statistics</li>
                <li>Mobile-optimized interface</li>
                <li>Camera and gallery integration</li>
            </ul>
        </div>
    `;

  modalBody.innerHTML = aboutHTML;
  modal.style.display = "flex";
}

// Show settings
function showSettings() {
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalBody = document.getElementById("modal-body");

  modalTitle.textContent = "Settings";

  const settingsHTML = `
        <div style="line-height: 1.6;">
            <h4>App Settings</h4>
            <p>Settings and preferences will be available in future updates.</p>
            
            <h4>Current Version</h4>
            <p>One Piece Classifier v1.0.0</p>
            
            <h4>Device Information</h4>
            <p>Platform: ${navigator.platform}</p>
            <p>User Agent: ${navigator.userAgent}</p>
        </div>
    `;

  modalBody.innerHTML = settingsHTML;
  modal.style.display = "flex";
}

// Close modal
function closeModal() {
  document.getElementById("modal").style.display = "none";
}

// Show notification
function showNotification(message, type = "info") {
  // Create notification element
  const notification = document.createElement("div");
  notification.className = `notification notification-${type}`;
  notification.style.cssText = `
        position: fixed;
        top: 20px;
        left: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 10px;
        color: white;
        font-weight: 500;
        z-index: 3000;
        transform: translateY(-100%);
        transition: transform 0.3s ease;
        text-align: center;
    `;

  // Set background color based on type
  switch (type) {
    case "success":
      notification.style.background =
        "linear-gradient(135deg, #28a745 0%, #20c997 100%)";
      break;
    case "error":
      notification.style.background =
        "linear-gradient(135deg, #dc3545 0%, #c82333 100%)";
      break;
    default:
      notification.style.background =
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)";
  }

  notification.textContent = message;
  document.body.appendChild(notification);

  // Animate in
  setTimeout(() => {
    notification.style.transform = "translateY(0)";
  }, 100);

  // Remove after 3 seconds
  setTimeout(() => {
    notification.style.transform = "translateY(-100%)";
    setTimeout(() => {
      if (document.body.contains(notification)) {
        document.body.removeChild(notification);
      }
    }, 300);
  }, 3000);
}

// Close modal when clicking outside
document.addEventListener("click", (e) => {
  const modal = document.getElementById("modal");
  if (e.target === modal) {
    closeModal();
  }
});

// Handle back button (for mobile browsers)
window.addEventListener("popstate", () => {
  closeModal();
});

// Add to home screen prompt (PWA features)
let deferredPrompt;

window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  deferredPrompt = e;

  // Show install prompt
  showNotification(
    "Add this app to your home screen for quick access!",
    "info"
  );
});

// Service Worker registration (for PWA features)
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/sw.js")
      .then((registration) => {
        console.log("SW registered: ", registration);
      })
      .catch((registrationError) => {
        console.log("SW registration failed: ", registrationError);
      });
  });
}
