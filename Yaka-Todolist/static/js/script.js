// menu beurger
    document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger-menu');
    const mobileMenu = document.querySelector('.mobile-menu');

// mes clics sur le menu hamburger
    hamburger.addEventListener('click', function () {
        mobileMenu.classList.toggle('active');
    });
});
