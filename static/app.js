// Character data with updated information
const characterData = {
  luffy: {
    name: "Monkey D. Luffy",
    image: "/static/op_dateset/Data/Data/Luffy/1.jpg",
    description:
      "Captain of the Straw Hat Pirates and wielder of the Gomu Gomu no Mi (Gum-Gum Fruit). Known for his rubber powers and unwavering determination to become the Pirate King.",
    bounty: "3,000,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Gomu Gomu no Mi",
  },
  zoro: {
    name: "Roronoa Zoro",
    image: "/static/op_dateset/Data/Data/Zoro/1.jpg",
    description:
      "Swordsman and first mate of the Straw Hat Pirates. A master of the Three Sword Style and aspiring to become the world's greatest swordsman.",
    bounty: "1,111,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
  },
  nami: {
    name: "Nami",
    image: "/static/op_dateset/Data/Data/Nami/1.jpeg",
    description:
      "Navigator of the Straw Hat Pirates and expert cartographer. Skilled with the Clima-Tact and has a deep understanding of weather patterns.",
    bounty: "366,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
  },
  usopp: {
    name: "Usopp",
    image: "/static/op_dateset/Data/Data/Usopp/1.png",
    description:
      "Sniper of the Straw Hat Pirates and skilled inventor. Known for his incredible marksmanship and creative Pop Green ammunition.",
    bounty: "500,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
  },
  sanji: {
    name: "Vinsmoke Sanji",
    image: "/static/op_dateset/Data/Data/Sanji/1.jpg",
    description:
      "Chef and third strongest fighter of the Straw Hat Pirates. Master of the Black Leg Style and former member of the Vinsmoke family.",
    bounty: "1,032,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
  },
  chopper: {
    name: "Tony Tony Chopper",
    image: "/static/op_dateset/Data/Data/Chopper/1.png",
    description:
      "Doctor and reindeer of the Straw Hat Pirates. Ate the Hito Hito no Mi (Human-Human Fruit) and can transform into various forms.",
    bounty: "1,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Hito Hito no Mi",
  },
  robin: {
    name: "Nico Robin",
    image: "/static/op_dateset/Data/Data/Robin/1.png",
    description:
      "Archaeologist of the Straw Hat Pirates and wielder of the Hana Hana no Mi (Flower-Flower Fruit). The last survivor of Ohara.",
    bounty: "930,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Hana Hana no Mi",
  },
  franky: {
    name: "Franky",
    image: "/static/op_dateset/Data/Data/Franky/1.png",
    description:
      "Shipwright of the Straw Hat Pirates and a cyborg. Built the Thousand Sunny and is known for his radical personality and cola-powered attacks.",
    bounty: "394,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
  },
  brook: {
    name: "Brook",
    image: "/static/op_dateset/Data/Data/Brook/1.png",
    description:
      "Musician and skeleton of the Straw Hat Pirates. Ate the Yomi Yomi no Mi (Revive-Revive Fruit) and is a master swordsman and musician.",
    bounty: "383,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "Yomi Yomi no Mi",
  },
  jinbei: {
    name: "Jinbe",
    image: "/static/op_dateset/Data/Data/Jinbei/1.jpg",
    description:
      "Helmsman of the Straw Hat Pirates and former Warlord of the Sea. A fish-man karate master and former captain of the Sun Pirates.",
    bounty: "1,100,000,000 Berries",
    crew: "Straw Hat Pirates",
    fruit: "None",
  },
  shanks: {
    name: "Red-Haired Shanks",
    image: "/static/op_dateset/Data/Data/Shanks/1.png",
    description:
      "Captain of the Red Hair Pirates and one of the Four Emperors. Former member of the Roger Pirates and mentor to Luffy.",
    bounty: "4,048,900,000 Berries",
    crew: "Red Hair Pirates",
    fruit: "None",
  },
  ace: {
    name: "Portgas D. Ace",
    image: "/static/op_dateset/Data/Data/Ace/1.jpg",
    description:
      "Former commander of the Whitebeard Pirates and wielder of the Mera Mera no Mi (Flame-Flame Fruit). Brother of Luffy and Sabo.",
    bounty: "5,500,000,000 Berries",
    crew: "Whitebeard Pirates",
    fruit: "Mera Mera no Mi",
  },
  law: {
    name: "Trafalgar Law",
    image: "/static/op_dateset/Data/Data/Law/1.png",
    description:
      "Captain of the Heart Pirates and wielder of the Ope Ope no Mi (Op-Op Fruit). A former Warlord and ally of the Straw Hats.",
    bounty: "3,000,000,000 Berries",
    crew: "Heart Pirates",
    fruit: "Ope Ope no Mi",
  },
  akainu: {
    name: "Sakazuki (Akainu)",
    image: "/static/op_dateset/Data/Data/Akainu/1.png",
    description:
      "Fleet Admiral of the Marines and wielder of the Magu Magu no Mi (Magma-Magma Fruit). Known for his absolute justice ideology.",
    bounty: "Unknown",
    crew: "Marines",
    fruit: "Magu Magu no Mi",
  },
  crocodile: {
    name: "Sir Crocodile",
    image: "/static/op_dateset/Data/Data/Crocodile/1.png",
    description:
      "Former Warlord and wielder of the Suna Suna no Mi (Sand-Sand Fruit). Leader of Baroque Works and former ruler of Alabasta.",
    bounty: "1,965,000,000 Berries",
    crew: "Cross Guild",
    fruit: "Suna Suna no Mi",
  },
  kurohige: {
    name: "Marshall D. Teach (Blackbeard)",
    image: "/static/op_dateset/Data/Data/Kurohige/1.png",
    description:
      "Captain of the Blackbeard Pirates and wielder of the Yami Yami no Mi (Dark-Dark Fruit). One of the Four Emperors.",
    bounty: "3,996,000,000 Berries",
    crew: "Blackbeard Pirates",
    fruit: "Yami Yami no Mi",
  },
  mihawk: {
    name: "Dracule Mihawk",
    image: "/static/op_dateset/Data/Data/Mihawk/1.png",
    description:
      "World's Greatest Swordsman and former Warlord of the Sea. Wielder of the legendary sword Yoru and member of Cross Guild.",
    bounty: "3,590,000,000 Berries",
    crew: "Cross Guild",
    fruit: "None",
  },
  rayleigh: {
    name: "Silvers Rayleigh",
    image: "/static/op_dateset/Data/Data/Rayleigh/1.png",
    description:
      "Former first mate of the Roger Pirates and mentor to Luffy. Known as the 'Dark King' and a master of all three types of Haki.",
    bounty: "Unknown",
    crew: "Roger Pirates (Former)",
    fruit: "None",
  },
};

// DOM elements
const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("file-input");
const previewContainer = document.getElementById("preview-container");
const preview = document.getElementById("preview");
const resultContainer = document.getElementById("result-container");
const loadingOverlay = document.getElementById("loading-overlay");
const galleryGrid = document.getElementById("gallery-grid");

// Initialize gallery
function initializeGallery() {
  galleryGrid.innerHTML = "";

  Object.entries(characterData).forEach(([key, character]) => {
    const galleryItem = document.createElement("div");
    galleryItem.className = "gallery-item";

    galleryItem.innerHTML = `
      <img src="${character.image}" alt="${character.name}" loading="lazy">
      <div class="gallery-item-content">
        <h3>${character.name}</h3>
        <p>${character.description}</p>
        <div class="gallery-stats">
          <span><strong>Bounty:</strong> ${character.bounty}</span>
          <span><strong>Crew:</strong> ${character.crew}</span>
          <span><strong>Devil Fruit:</strong> ${character.fruit}</span>
        </div>
      </div>
    `;

    galleryGrid.appendChild(galleryItem);
  });
}

// File handling
function handleFile(file) {
  if (!file.type.startsWith("image/")) {
    alert("Please select an image file.");
    return;
  }

  const reader = new FileReader();
  reader.onload = function (e) {
    preview.src = e.target.result;
    previewContainer.style.display = "block";
    resultContainer.style.display = "none";

    // Auto-predict when file is loaded
    const imageData = e.target.result.split(",")[1]; // Remove data URL prefix
    predictCharacter(imageData);
  };
  reader.readAsDataURL(file);
}

// Drag and drop functionality
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
  const files = e.dataTransfer.files;
  if (files.length > 0) {
    handleFile(files[0]);
  }
});

fileInput.addEventListener("change", (e) => {
  if (e.target.files.length > 0) {
    handleFile(e.target.files[0]);
  }
});

// Close preview
function closePreview() {
  previewContainer.style.display = "none";
  resultContainer.style.display = "none";
}

// Show loading
function showLoading() {
  loadingOverlay.style.display = "flex";
}

// Hide loading
function hideLoading() {
  loadingOverlay.style.display = "none";
}

// Predict character
async function predictCharacter(imageData) {
  try {
    showLoading();

    const response = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ image: imageData }),
    });

    const result = await response.json();
    hideLoading();

    if (result.success) {
      displayResult(result);
    } else {
      alert("Error: " + result.error);
    }
  } catch (error) {
    hideLoading();
    console.error("Error:", error);
    alert("An error occurred while processing the image.");
  }
}

// Display result
function displayResult(result) {
  const character = characterData[result.character.toLowerCase()];

  if (character) {
    document.getElementById("result-character").textContent = character.name;
    document.getElementById("character-name").textContent = character.name;
    document.getElementById("character-description").textContent =
      character.description;
    document.getElementById("character-bounty").textContent = character.bounty;
    document.getElementById("character-crew").textContent = character.crew;
    document.getElementById("character-fruit").textContent = character.fruit;
    document.getElementById("character-image").src = character.image;
    document.getElementById("confidence-badge").textContent = `Confidence: ${(
      result.confidence * 100
    ).toFixed(1)}%`;

    resultContainer.style.display = "block";
  }
}

// Handle form submission
document.addEventListener("DOMContentLoaded", function () {
  initializeGallery();

  // Smooth scrolling for navigation
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Mobile menu toggle
  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector(".nav-menu");

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });

  // Close mobile menu when clicking on a link
  document.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("active");
      navMenu.classList.remove("active");
    });
  });
});
