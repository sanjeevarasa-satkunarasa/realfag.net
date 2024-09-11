function toggleMode(isVGS) {
  let themeStyle = document.getElementById("theme-style");
  let currentMode;

  if (isVGS) {
    // VGS file toggle logic
    if (themeStyle.getAttribute("href") === "/css/VGS-light.css") {
      themeStyle.href = "/css/VGS-dark.css";
      currentMode = "dark";
    } else {
      themeStyle.href = "/css/VGS-light.css";
      currentMode = "light";
    }
  } else {
    // Index file toggle logic
    if (themeStyle.getAttribute("href") === "css/styles.css") {
      themeStyle.href = "css/styles-dark.css";
      currentMode = "dark";
    } else {
      themeStyle.href = "css/styles.css";
      currentMode = "light";
    }
  }

  // Update image sources for both cases
  if (currentMode === "dark") {
    document.getElementById("dark_mode_icon").src = "/media/dark_mode_dark.png";
    document.getElementById("dark_mode_discord").src = "/media/discord_logo_dark.png";
    document.getElementById("favicon").src = "/media/favicon_dark.ico";
  } else {
    document.getElementById("dark_mode_icon").src = "/media/dark_mode_light.png";
    document.getElementById("dark_mode_discord").src = "/media/discord_logo_light.png";
    document.getElementById("favicon").src = "/media/favicon_light.ico";
  }

  // Save preference to localStorage
  localStorage.setItem('theme', currentMode);
}

// On page load, apply the saved theme
function applySavedTheme(isVGS) {
  let savedTheme = localStorage.getItem('theme') || 'light'; // Default to light if no theme is saved
  let themeStyle = document.getElementById("theme-style");

  if (isVGS) {
    themeStyle.href = savedTheme === 'dark' ? "/css/VGS-dark.css" : "/css/VGS-light.css";
  } else {
    themeStyle.href = savedTheme === 'dark' ? "css/styles-dark.css" : "css/styles.css";
  }

  // Update images based on saved theme
  if (savedTheme === 'dark') {
    document.getElementById("dark_mode_icon").src = "/media/dark_mode_dark.png";
    document.getElementById("dark_mode_discord").src = "/media/discord_logo_dark.png";
    document.getElementById("favicon").src = "/media/favicon_dark.ico";
  } else {
    document.getElementById("dark_mode_icon").src = "/media/dark_mode_light.png";
    document.getElementById("dark_mode_discord").src = "/media/discord_logo_light.png";
    document.getElementById("favicon").src = "/media/favicon_light.ico";
  }
}

function popUp() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}

function popUpClose() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("hide");
}