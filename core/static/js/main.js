document.querySelectorAll(".navbar-nav a.nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    const collapse = document.getElementById("navMenu");
    if (collapse.classList.contains("show")) {
      bootstrap.Collapse.getOrCreateInstance(collapse).hide();
    }
  });
});