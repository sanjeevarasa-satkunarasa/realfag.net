function toggleMode() {
  var themeStyle = document.getElementById("theme-style");
  if (themeStyle.getAttribute("href") === "styles.css") {
      themeStyle.href = "styles-dark.css";
  } else {
      themeStyle.href = "styles.css";
  }
}