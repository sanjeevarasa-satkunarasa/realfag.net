function toggleMode() {
  var themeStyle = document.getElementById("theme-style");
  if (themeStyle.getAttribute("href") === "css/styles.css") {
      themeStyle.href = "css/styles-dark.css";
      document.getElementById("dark_button_img").src = "/media/light_darkmode.png";
  } else if (themeStyle.getAttribute("href") === "css/styles-dark.css"){
      themeStyle.href = "css/styles.css";
      document.getElementById("dark_button_img").src = "/media/dark_darkmode.png";
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

function closeBanner() {
  document.querySelector(".banner").style.display = "none";
}