/* Toggle between hiding and showing the dropdown content */
function toggleDropdown(dropdownId) {
    var dropdownContent = document.getElementById(dropdownId);
    if (dropdownContent.classList.contains("show")) {
      dropdownContent.classList.remove("show");
    } else {
      // Close all other dropdowns before opening this one
      closeAllDropdowns();
      dropdownContent.classList.add("show");
    }
    }
  
/* Set the selected category */
 function selectCategory(category, dropdownId) {
   var button = document.getElementById(dropdownId);
   button.textContent = category; // Update the button text with the selected category
   toggleDropdown(dropdownId); // Close the dropdown after selection (optional)
  }
  
/* Close all dropdown menus */
  function closeAllDropdowns() {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
  
// Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      closeAllDropdowns();
    }
  }

var animatedElement = document.createElement('div');
animatedElement.id = 'animated-element';
document.body.appendChild(animatedElement);