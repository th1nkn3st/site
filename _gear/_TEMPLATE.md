---
layout: default
title: "Product Name Here"
excerpt: "Short description for listing page."
brand: "Brand Name"
affiliate_short_url: "https://amzn.to/YOUR-LINK"
images:
  - /assets/images/gear/product-folder/image1.jpg
  - /assets/images/gear/product-folder/image2.jpg
  - /assets/images/gear/product-folder/image3.jpg
  - /assets/images/gear/product-folder/image4.jpg
---

[← Back to Gear](/gear/) | [Shop Now →]({{ page.affiliate_short_url }})

---

<h1 style="text-align: center; margin: 2rem 0;">{{ page.title }}</h1>

<div class="product-hero">
  <div class="product-info">
    <p>Main product description paragraph goes here. Keep it concise and focused on the value proposition.</p>
    
    <h3>Key Features</h3>
    <ul>
      <li>Feature 1</li>
      <li>Feature 2</li>
      <li>Feature 3</li>
      <li>Feature 4</li>
    </ul>
  </div>

  <div>
    <div class="carousel-container">
      <div class="carousel-slides" id="carouselSlides">
        {% for img in page.images %}
        <div class="carousel-slide">
          <img src="{{ img }}" alt="Product image" loading="lazy">
        </div>
        {% endfor %}
      </div>
      <button class="carousel-btn prev" onclick="moveSlide(-1)">‹</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">›</button>
    </div>

    <div class="carousel-thumbnails" id="carouselThumbnails"></div>
  </div>
</div>

<script>
let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');
const totalSlides = slides.length;
const slidesContainer = document.getElementById('carouselSlides');
const thumbnailsContainer = document.getElementById('carouselThumbnails');

slides.forEach((slide, index) => {
  const thumb = document.createElement('div');
  thumb.className = 'carousel-thumbnail';
  thumb.onclick = () => goToSlide(index);
  const img = slide.querySelector('img').cloneNode(true);
  thumb.appendChild(img);
  thumbnailsContainer.appendChild(thumb);
});

function updateCarousel() {
  slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
  document.querySelectorAll('.carousel-thumbnail').forEach((thumb, index) => {
    thumb.classList.toggle('active', index === currentSlide);
  });
}

function moveSlide(direction) {
  currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
  updateCarousel();
}

function goToSlide(index) {
  currentSlide = index;
  updateCarousel();
}

updateCarousel();
setInterval(() => moveSlide(1), 5000);
</script>

---

## Technical Specs

| Specification | Details |
|---------------|---------|
| Model | Model Number |
| Dimensions | X" × Y" × Z" |
| Weight | X oz (X g) |
| Input | Voltage specs |
| Ports | Port types |
| Max Output | Power specs |
| Safety | Certifications |
| Warranty | Duration |

---

## Power Allocation
_(Optional - remove if not applicable)_

| Mode | Port 1 | Port 2 | Use Case |
|------|--------|--------|----------|
| Single | 100W | — | Description |
| Dual | 60W | 40W | Description |

---

## Setup Guide

### Installation

1. Step 1
2. Step 2
3. Step 3

### Tips

- Tip 1
- Tip 2
- Tip 3

---

## Compatible Devices

**Category 1:** Device list  
**Category 2:** Device list  
**Category 3:** Device list

---

## Purchase

<a href="{{ page.affiliate_short_url }}" class="read-more" target="_blank" rel="nofollow sponsored noopener">Buy on Amazon →</a>

> As an Amazon Associate, Th1nkN3st earns from qualifying purchases. Using our links supports our reviews—thank you!

---

## Related Items

- [Browse All Gear](/gear/)
- [DevSecOps Tools](/tools/)
- [Latest Blog Posts](/blog/)

---

[← Back to Gear](/gear/) | [Tools Library](/tools/) | [Home](/)
