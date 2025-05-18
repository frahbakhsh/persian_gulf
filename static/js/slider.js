document.addEventListener('DOMContentLoaded', function() {
    // اسکریپت اسلایدر
    const slides = document.querySelectorAll('.slide');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const yearButtons = document.querySelectorAll('.year-button');
    
    let currentIndex = 0;
    const totalSlides = slides.length;
    
    // Function to update the active slide
    function updateSlider() {
        slides.forEach((slide, index) => {
            if (index === currentIndex) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });
        
        // Update active year button
        yearButtons.forEach((button, index) => {
            if (index === currentIndex) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });
    }
    
    // Previous button click event
    prevButton.addEventListener('click', function() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        updateSlider();
    });
    
    // Next button click event
    nextButton.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateSlider();
    });
    
    // Year button click events
    yearButtons.forEach(button => {
        button.addEventListener('click', function() {
            currentIndex = parseInt(this.getAttribute('data-index'));
            updateSlider();
        });
    });
    
    // Initialize slider
    updateSlider();

    // اسکریپت منو
    const menuToggle = document.querySelector('.menu-toggle');
    const mainMenu = document.querySelector('.main-menu');
    
    menuToggle.addEventListener('click', function() {
        mainMenu.classList.toggle('show');
    });

    // بستن منو در هنگام کلیک روی لینک‌ها
    const menuLinks = document.querySelectorAll('.main-menu a');
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            mainMenu.classList.remove('show');
        });
    });

    // بستن منو در هنگام کلیک خارج از منو
    document.addEventListener('click', function(event) {
        const isClickInsideMenu = mainMenu.contains(event.target);
        const isClickOnToggle = menuToggle.contains(event.target);
        
        if (!isClickInsideMenu && !isClickOnToggle && mainMenu.classList.contains('show')) {
            mainMenu.classList.remove('show');
        }
    });
});