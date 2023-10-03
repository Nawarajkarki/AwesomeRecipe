const seeMoreButtons = document.querySelectorAll('.see-more-button');

seeMoreButtons.forEach(button => {
    button.addEventListener('click', () => {
        localStorage.setItem('scrollPosition', window.pageYOffset);
    });
});

window.addEventListener('load', () => {
    const scrollPosition = localStorage.getItem('scrollPosition');
    if (scrollPosition) {
        window.scrollTo(0, scrollPosition);
        localStorage.removeItem('scrollPosition');
    }
});