function toggleMode() {
  var themeStyle = document.getElementById("theme-style");
  if (themeStyle.getAttribute("href") === "styles.css") {
      themeStyle.href = "css/styles-dark.css";
  } else {
      themeStyle.href = "css/styles.css";
  }
}