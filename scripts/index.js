const hamburgerBtn = document.getElementById("hamburger-btn");
const navLinks = document.querySelector(".nav-links");

// Toggle mobile nav visibility
hamburgerBtn.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

// Highlight the active link based on URL
const currentPath = window.location.pathname;
const links = document.querySelectorAll(".nav-links a");

links.forEach((link) => {
  if (link.getAttribute("href") === currentPath) {
    link.classList.add("active-link");
    console.log(currentPath);
  }
});

// Testimonials Carousel
let current = 0;
const testimonials = document.querySelectorAll(".testimonial");

function showTestimonial(index) {
  testimonials.forEach((t, i) => {
    t.classList.toggle("active", i === index);
  });
}

function nextTestimonial() {
  current = (current + 1) % testimonials.length;
  showTestimonial(current);
}

function prevTestimonial() {
  current = (current - 1 + testimonials.length) % testimonials.length;
  showTestimonial(current);
}

// Auto-rotate every 5 seconds
setInterval(nextTestimonial, 5000);
