const hamburger = document.getElementById('hamburger-icon');
const navUL = document.getElementById('nav-bar');
const nav = document.querySelector("#main-header");
let lastscrollY = window.scrollY;

hamburger.addEventListener('click', () => {
    navUL.classList.toggle('show');
});

window.addEventListener("scroll", () => {
    if (lastscrollY < window.scrollY) {
        nav.classList.add("nav-hidden");
    } else {
        nav.classList.remove("nav-hidden");
    }

    lastscrollY = window.scrollY;
});


