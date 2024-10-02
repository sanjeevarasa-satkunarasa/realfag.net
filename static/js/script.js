function toggleMode(isVGS) {
  const themeStyle = document.getElementById("theme-style");
  let currentMode;

  if (isVGS) {
      // VGS file toggle logic
      if (themeStyle.getAttribute("href") === "/static/css/school-light.css") {
          themeStyle.href = "/static/css/school-dark.css";
          currentMode = "dark";
      } else {
          themeStyle.href = "/static/css/school-light.css";
          currentMode = "light";
      }
  } else {
      // Index file toggle logic
      if (themeStyle.getAttribute("href") === "/static/css/styles.css") {
          themeStyle.href = "/static/css/styles-dark.css";
          currentMode = "dark";
      } else {
          themeStyle.href = "/static/css/styles.css";
          currentMode = "light";
      }
  }

  updateImageSources(currentMode);
  localStorage.setItem('theme', currentMode);
}

function applySavedTheme(isVGS) {
  const savedTheme = localStorage.getItem('theme') || 'light'; // Default to light if no theme is saved
  const themeStyle = document.getElementById("theme-style");

  if (isVGS) {
      themeStyle.href = savedTheme === 'dark' ? "/static/css/school-dark.css" : "/static/css/school-light.css";
  } else {
      themeStyle.href = savedTheme === 'dark' ? "/static/css/styles-dark.css" : "/static/css/styles.css";
  }

  updateImageSources(savedTheme);
}

function updateImageSources(theme) {
  const darkModeIcon = document.getElementById("dark_mode_icon");
  const darkModeDiscord = document.getElementById("dark_mode_discord");
  const favicon = document.getElementById("favicon");

  if (theme === "dark") {
      darkModeIcon.src = "/static/images/dark_mode_dark.webp";
      darkModeDiscord.src = "/static/images/discord_logo_dark.webp";
      favicon.src = "/static/images/favicon_dark.ico";
  } else {
      darkModeIcon.src = "/static/images/dark_mode_light.webp";
      darkModeDiscord.src = "/static/images/discord_logo_light.webp";
      favicon.src = "/static/images/favicon_light.ico";
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

document.addEventListener("DOMContentLoaded", function() {
  // Your code here
});
