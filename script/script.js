function toggleModeIndex() {
  let themeStyle = document.getElementById("theme-style");
  if (themeStyle.getAttribute("href") === "css/styles.css") {
      themeStyle.href = "css/styles-dark.css";
      document.getElementById("dark_mode_icon").src = "/media/dark_mode_dark.png"
      document.getElementById("dark_mode_discord").src = "/media/discord_logo_dark.png"
  } else if (themeStyle.getAttribute("href") === "css/styles-dark.css"){
      themeStyle.href = "css/styles.css";
      document.getElementById("dark_mode_icon").src = "/media/dark_mode_light.png"
      document.getElementById("dark_mode_discord").src = "/media/discord_logo_light.png"
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