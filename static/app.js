// Character data for enhanced UI
const characterData = {
  Luffy: {
    name: "Monkey D. Luffy",
    description:
      "Captain of the Straw Hat Pirates and wielder of the Gomu Gomu no Mi (Gum-Gum Fruit).",
    bounty: "3,000,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Gomu Gomu no Mi",
    image: "/characters/Luffy",
  },
  Zoro: {
    name: "Roronoa Zoro",
    description:
      "Swordsman of the Straw Hat Pirates and one of the strongest swordsmen in the world.",
    bounty: "1,111,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "/characters/Zoro",
  },
  Nami: {
    name: "Nami",
    description: "Navigator of the Straw Hat Pirates and expert cartographer.",
    bounty: "366,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "/characters/Nami",
  },
  Usopp: {
    name: "Usopp",
    description: "Sniper of the Straw Hat Pirates and a skilled marksman.",
    bounty: "500,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "/characters/Usopp",
  },
  Sanji: {
    name: "Vinsmoke Sanji",
    description: "Cook of the Straw Hat Pirates and expert in Black Leg Style.",
    bounty: "1,032,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "/characters/Sanji",
  },
  Chopper: {
    name: "Tony Tony Chopper",
    description:
      "Doctor of the Straw Hat Pirates and wielder of the Hito Hito no Mi.",
    bounty: "1,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Hito Hito no Mi",
    image: "/characters/Chopper",
  },
  Robin: {
    name: "Nico Robin",
    description:
      "Archaeologist of the Straw Hat Pirates and wielder of the Hana Hana no Mi.",
    bounty: "930,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Hana Hana no Mi",
    image: "/characters/Robin",
  },
  Franky: {
    name: "Franky",
    description: "Shipwright of the Straw Hat Pirates and a cyborg.",
    bounty: "394,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "/characters/Franky",
  },
  Brook: {
    name: "Brook",
    description:
      "Musician of the Straw Hat Pirates and wielder of the Yomi Yomi no Mi.",
    bounty: "383,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Yomi Yomi no Mi",
    image: "/characters/Brook",
  },
  Jinbe: {
    name: "Jinbe",
    description:
      "Helmsman of the Straw Hat Pirates and former Warlord of the Sea.",
    bounty: "1,100,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
    image: "/characters/Jinbe",
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

// Navigation functionality
document.addEventListener("DOMContentLoaded", () => {
  // Mobile menu toggle
  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector(".nav-menu");
  const navLinks = document.querySelectorAll(".nav-link");

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });

  // Close mobile menu when clicking on a link
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("active");
      navMenu.classList.remove("active");
    });
  });

  // Smooth scrolling for navigation links
  navLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const targetId = link.getAttribute("href");
      const targetSection = document.querySelector(targetId);

      if (targetSection) {
        targetSection.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }

      // Update active link
      navLinks.forEach((l) => l.classList.remove("active"));
      link.classList.add("active");
    });
  });

  // Initialize gallery
  initializeGallery();

  // Initialize drag and drop functionality
  initializeDragAndDrop();
});

// Initialize gallery with character cards
function initializeGallery() {
  const galleryGrid = document.getElementById("gallery-grid");

  Object.entries(characterData).forEach(([key, character]) => {
    const galleryItem = document.createElement("div");
    galleryItem.className = "gallery-item";
    galleryItem.innerHTML = `
            <img src="${character.image}" alt="${character.name}">
            <div class="gallery-item-content">
                <h3>${character.name}</h3>
                <p>${character.description}</p>
                <div class="gallery-stats">
                    <span><strong>Bounty:</strong> ${character.bounty}</span>
                    <span><strong>Crew:</strong> ${character.crew}</span>
                </div>
            </div>
        `;
    galleryGrid.appendChild(galleryItem);
  });
}

// Initialize drag and drop functionality
function initializeDragAndDrop() {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("file-input");
  const preview = document.getElementById("preview");
  const previewContainer = document.getElementById("preview-container");
  const resultContainer = document.getElementById("result-container");
  const loadingOverlay = document.getElementById("loading-overlay");

  // Drag and Drop Handlers
  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("dragover");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("dragover");
  });

  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("dragover");
    const file = e.dataTransfer.files[0];
    handleFile(file);
  });

  dropArea.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", () => handleFile(fileInput.files[0]));

  function handleFile(file) {
    if (!file || !file.type.startsWith("image/")) {
      showNotification("Please upload a valid image file.", "error");
      return;
    }

    const reader = new FileReader();
    reader.onload = () => {
      preview.src = reader.result;
      previewContainer.style.display = "block";
      resultContainer.style.display = "none";

      // Show loading overlay
      loadingOverlay.style.display = "flex";

      // Send to server
      fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: reader.result }),
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
          showNotification("Error identifying the character.", "error");
          console.error(err);
        });
    };

    reader.onerror = () => {
      showNotification("Error reading the file.", "error");
    };

    reader.readAsDataURL(file);
  }
}

// Display classification result
function displayResult(characterName, probabilities) {
  const resultContainer = document.getElementById("result-container");
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
  confidenceBadge.textContent = `${confidencePercentage}% Confidence`;

  // Create probability chart
  createProbabilityChart(probabilities);

  // Show result container
  resultContainer.style.display = "block";
  resultContainer.scrollIntoView({ behavior: "smooth" });

  // Show success notification
  showNotification(
    `Successfully identified as ${characterInfo.name}!`,
    "success"
  );
}

// Create probability chart
function createProbabilityChart(probabilities) {
  const chartContainer = document.getElementById("probability-chart");
  chartContainer.innerHTML = "";

  // Sample class names (you should get these from your model)
  const classNames = Object.keys(characterData);

  // Create chart bars
  probabilities.forEach((prob, index) => {
    if (index < classNames.length) {
      const barContainer = document.createElement("div");
      barContainer.style.cssText = `
                display: flex;
                align-items: center;
                margin-bottom: 10px;
                gap: 10px;
            `;

      const label = document.createElement("span");
      label.textContent = classNames[index];
      label.style.cssText = `
                min-width: 100px;
                font-size: 0.9rem;
                font-weight: 500;
            `;

      const bar = document.createElement("div");
      bar.style.cssText = `
                flex: 1;
                height: 20px;
                background: #e0e0e0;
                border-radius: 10px;
                overflow: hidden;
                position: relative;
            `;

      const fill = document.createElement("div");
      fill.style.cssText = `
                height: 100%;
                background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
                width: ${prob * 100}%;
                transition: width 0.5s ease;
            `;

      const percentage = document.createElement("span");
      percentage.textContent = `${Math.round(prob * 100)}%`;
      percentage.style.cssText = `
                min-width: 40px;
                font-size: 0.8rem;
                font-weight: 600;
                color: #333;
            `;

      bar.appendChild(fill);
      barContainer.appendChild(label);
      barContainer.appendChild(bar);
      barContainer.appendChild(percentage);
      chartContainer.appendChild(barContainer);
    }
  });
}

// Close preview
function closePreview() {
  document.getElementById("preview-container").style.display = "none";
  document.getElementById("result-container").style.display = "none";
}

// Show notification
function showNotification(message, type = "info") {
  // Create notification element
  const notification = document.createElement("div");
  notification.className = `notification notification-${type}`;
  notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 10px;
        color: white;
        font-weight: 500;
        z-index: 3000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
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
    notification.style.transform = "translateX(0)";
  }, 100);

  // Remove after 3 seconds
  setTimeout(() => {
    notification.style.transform = "translateX(100%)";
    setTimeout(() => {
      document.body.removeChild(notification);
    }, 300);
  }, 3000);
}

// Scroll to top functionality
window.addEventListener("scroll", () => {
  const scrollTop = document.createElement("button");
  scrollTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
  scrollTop.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        cursor: pointer;
        display: none;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        z-index: 1000;
        transition: all 0.3s ease;
    `;

  if (window.scrollY > 300) {
    if (!document.querySelector(".scroll-top")) {
      document.body.appendChild(scrollTop);
      scrollTop.classList.add("scroll-top");
    }
    document.querySelector(".scroll-top").style.display = "flex";
  } else {
    const existingScrollTop = document.querySelector(".scroll-top");
    if (existingScrollTop) {
      existingScrollTop.style.display = "none";
    }
  }
});

// Add scroll to top click handler
document.addEventListener("click", (e) => {
  if (e.target.closest(".scroll-top")) {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }
});
