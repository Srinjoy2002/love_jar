let tasks = [];
let username = localStorage.getItem("username") || "";

// Login function
function login() {
  username = document.getElementById("username").value;
  if (username.trim() !== "") {
    localStorage.setItem("username", username);
    document.getElementById("login-screen").classList.add("hidden");
    document.getElementById("main-app").classList.remove("hidden");
    loadSecretMessage();
    updateJar();
  }
}

// Parse wishes from uploaded text—remove leading numbering or bullet points
function parseWishes(text) {
  const lines = text.split(/\r?\n/);
  return lines
    .map(line => line.trim().replace(/^[\d\.\-\)\s]*\s*/, ''))
    .filter(line => line !== "");
}

// File upload handler (TXT or DOCX)
function uploadFile(event) {
  const file = event.target.files[0];
  if (!file) return;
  
  const fileName = file.name.toLowerCase();
  if (fileName.endsWith(".txt")) {
    const reader = new FileReader();
    reader.onload = function(e) {
      const text = e.target.result;
      tasks = parseWishes(text);
      updateJar();
    };
    reader.readAsText(file);
  } else if (fileName.endsWith(".docx")) {
    file.arrayBuffer().then(buffer => {
      mammoth.extractRawText({ arrayBuffer: buffer })
        .then(function(result) {
          tasks = parseWishes(result.value);
          updateJar();
        })
        .catch(function(err) {
          console.error("Error reading DOCX:", err);
        });
    });
  } else {
    alert("Please upload a TXT or DOCX file.");
  }
}

// Load a dummy list of 50 wishes if needed
function loadDummyWishes() {
  tasks = [];
  for (let i = 1; i <= 50; i++) {
    tasks.push(`Wish ${i}: Enjoy a special moment together.`);
  }
  updateJar();
}

// Update jar display with realistic paper chits and random rotation
function updateJar() {
  document.getElementById("task-count").innerText = `${tasks.length} wish${tasks.length === 1 ? "" : "es"} loaded`;
  const chitsContainer = document.getElementById("chits");
  chitsContainer.innerHTML = "";
  tasks.forEach(() => {
    const chit = document.createElement("div");
    chit.classList.add("chit");
    // Apply a random rotation between -5 and 5 degrees
    const rotation = (Math.random() * 10 - 5).toFixed(1) + "deg";
    chit.style.setProperty("--rotation", rotation);
    chit.classList.add("rotate");
    chitsContainer.appendChild(chit);
  });
}

// Animate hand picking a wish, show the popup, and remove the wish
function pickTask() {
  if (tasks.length < 1) {
    alert("No more wishes! Please upload a new list or load dummy wishes.");
    return;
  }
  // Choose a random wish and remove it from the array
  const index = Math.floor(Math.random() * tasks.length);
  const randomTask = tasks.splice(index, 1)[0];
  updateJar();

  // Prepare paper element with the chosen wish
  const paper = document.getElementById("paper");
  paper.querySelector(".paper-content").innerText = randomTask;
  paper.classList.remove("hidden");
  paper.style.animation = "paperAppear 0.5s forwards";

  // Animate hand picking the paper
  const handContainer = document.getElementById("hand-container");
  handContainer.classList.remove("hidden");
  const hand = document.querySelector(".hand");
  hand.style.animation = "handPick 1.5s forwards";

  // After hand animation ends, show popup and hide paper
  hand.addEventListener("animationend", function handleAnimationEnd() {
    hand.style.animation = "";
    handContainer.classList.add("hidden");
    showPopup(randomTask);
    setTimeout(() => {
      paper.classList.add("hidden");
    }, 1000);
    hand.removeEventListener("animationend", handleAnimationEnd);
  });
}

// Show popup modal with the chosen wish
function showPopup(taskText) {
  document.getElementById("popup-text").innerText = taskText;
  const popup = document.getElementById("popup");
  popup.classList.remove("hidden");
  popup.style.display = "flex";
}

// Close popup modal and trigger celebration animation
function closePopup() {
  const popup = document.getElementById("popup");
  popup.classList.add("hidden");
  popup.style.display = "none";
  showCelebration();
}

// Celebration animation: Confetti, party poppers, and stars
function showCelebration() {
  const celebration = document.getElementById("celebration");
  celebration.classList.remove("hidden");
  celebration.innerHTML = "";
  const totalShapes = 80;
  const shapeTypes = ["confetti", "popper", "star"];
  
  for (let i = 0; i < totalShapes; i++) {
    const randomType = shapeTypes[Math.floor(Math.random() * shapeTypes.length)];
    const shape = document.createElement("div");
    shape.classList.add(randomType);
    
    // For confetti and poppers, assign a random color
    if (randomType === "confetti" || randomType === "popper") {
      const colors = ["#ff4d6d", "#ff8fab", "#ffccd5", "#fff0f6", "#fdd7b0", "#0ff", "#ff0", "#0f0"];
      const randomColor = colors[Math.floor(Math.random() * colors.length)];
      if (randomType === "confetti") {
        shape.style.background = randomColor;
      }
      if (randomType === "popper") {
        shape.style.background = `linear-gradient(45deg, ${randomColor}, ${
          colors[Math.floor(Math.random() * colors.length)]
        })`;
      }
    }
    if (randomType === "star") {
      const starColors = ["#ff4d6d", "#ff8fab", "#ffccd5", "#fdd7b0", "#0ff", "#0f0", "#ff0"];
      const starColor = starColors[Math.floor(Math.random() * starColors.length)];
      shape.style.setProperty("--starColor", starColor);
    }
    
    shape.style.left = Math.random() * 100 + "vw";
    shape.style.top = Math.random() * 100 + "vh";
    shape.style.animationDelay = (Math.random() * 1) + "s";
    celebration.appendChild(shape);
  }
  // Remove celebration after 5.5s (slightly longer than the 5s duration)
  setTimeout(() => {
    celebration.classList.add("hidden");
    celebration.innerHTML = "";
  }, 5500);
}

/** 
 * Toggle the jar lid's "open" class so it stays open until toggled again.
 */
function toggleLid() {
  const lid = document.querySelector(".jar-lid");
  lid.classList.toggle("open");
}

// Secret Message Section (stored in localStorage)
function saveMessage() {
  const message = document.getElementById("messageInput").value;
  localStorage.setItem("secretMessage", message);
  document.getElementById("saved-message").innerText = message;
}
function loadSecretMessage() {
  const savedMessage = localStorage.getItem("secretMessage");
  if (savedMessage) {
    document.getElementById("saved-message").innerText = savedMessage;
  }
}
