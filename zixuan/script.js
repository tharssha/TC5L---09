const slides = document.querySelectorAll('.Slides');

let currentSlide = 0;

function showSlide(n) {
  slides.forEach(slide => slide.style.display = 'none');
  slides[n].style.display = 'block';
}

function nextSlide() {
  currentSlide++;   

  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }
  showSlide(currentSlide);   

}

setInterval(nextSlide, 3000); // Change the interval here to adjust the slide transition time (in milliseconds)
showSlide(currentSlide); // Show the first slide initially