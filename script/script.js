function toggleMode() {
  var themeStyle = document.getElementById("theme-style");
  if (themeStyle.getAttribute("href") === "styles.css") {
      themeStyle.href = "css/styles-dark.css";
  } else {
      themeStyle.href = "css/styles.css";
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