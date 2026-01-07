// Get references to toggle icon and menu elements
const navbarIcon = document.querySelector(".toggle-icon"),
  barIcon = document.querySelector(".bar-icon"),
  crossIcon = document.querySelector(".cross-icon"),
  navMenu = document.querySelector(".navbar-menu");
// Toggle mobile menu and switch icons on click
navbarIcon.addEventListener("click", () => {
  const isOpen = navMenu.classList.toggle("mobile-menu");
  if (isOpen) {
    // Show close icon, hide hamburger icon
    barIcon.style.setProperty("display", "none", "important");
    crossIcon.style.setProperty("display", "block", "important");
  } else {
    // Show hamburger icon, hide close icon
    barIcon.style.setProperty("display", "block", "important");
    crossIcon.style.setProperty("display", "none", "important");
  }
});