const prevButton = document.querySelector('.prev a');
        const exitButton = document.querySelector('.exit a');

        prevButton.addEventListener('click', () => {
            const scrollPosition = localStorage.getItem('scrollPosition');
            if (scrollPosition) {
                window.location.href = `/home#${scrollPosition}`;
            } else {
                window.location.href = '/home';
            }
        });

        exitButton.addEventListener('click', () => {
            const scrollPosition = localStorage.getItem('scrollPosition');
            if (scrollPosition) {
                window.location.href = `/home#${scrollPosition}`;
            } else {
                window.location.href = '/home';
            }
        });