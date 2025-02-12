function toggleDropdown() {
  document.getElementById("dropdown-content").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
          }
      }
  }
}

function popUp() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}

function popUpClose() {
  var popup = document.getElementById("myPopup");
  popup.classList.remove("show");
}

window.addEventListener('click', function(event) {
  var popup = document.getElementById("myPopup");
  if (!event.target.closest('.popup') && !popup.contains(event.target)) {
      popup.classList.remove('show');
  }
});

document.getElementById("problemForm").addEventListener("submit", function() {
  popUpClose();
});
