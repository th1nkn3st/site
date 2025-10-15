---
layout: default
title: "Anker Prime 67W Compact Fast Charger"
excerpt: "Compact GaN charger for laptops, tablets, and phones with 3-port power delivery."
brand: "Anker"
affiliate_short_url: "https://amzn.to/4qhzGlu"
images:
  - /assets/images/gear/anker_prime_67w/71j613eZuhL._AC_SL1500_.jpg
  - /assets/images/gear/anker_prime_67w/71t4F2imtJL._AC_SL1500_.jpg
  - /assets/images/gear/anker_prime_67w/71A6bCyJUEL._AC_SL1500_.jpg
  - /assets/images/gear/anker_prime_67w/71tKgHAtFZL._AC_SL1500_.jpg
---

[← Back to Gear](/gear/) | [Shop Now →]({{ page.affiliate_short_url }})

---

<h1 class="product-title">{{ page.title }}</h1>

<div class="product-hero">
  <div class="product-info">
    <p>Consolidate multiple charging bricks into one compact GaN-powered charger with intelligent power distribution.</p>
    
    <h3>Key Features</h3>
    <ul>
      <li>3 ports: 2× USB-C, 1× USB-A</li>
      <li>67W total output with dynamic power allocation</li>
      <li>Compact design with foldable prongs</li>
      <li>ActiveShield 2.0 temperature monitoring</li>
    </ul>
  </div>

  <div class="carousel-container">
    <div class="carousel-slides" id="carouselSlides">
      {% for img in page.images %}
      <div class="carousel-slide">
        <img src="{{ img }}" alt="{{ page.title }}" loading="lazy">
      </div>
      {% endfor %}
    </div>
    <button class="carousel-btn prev" onclick="moveSlide(-1)">‹</button>
    <button class="carousel-btn next" onclick="moveSlide(1)">›</button>
  </div>

  <div class="carousel-thumbnails" id="carouselThumbnails"></div>
</div>

<script>
let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');
const totalSlides = slides.length;
const slidesContainer = document.getElementById('carouselSlides');
const thumbnailsContainer = document.getElementById('carouselThumbnails');

// Create thumbnails
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

// Initialize
updateCarousel();

// Auto-advance every 5 seconds (optional)
setInterval(() => moveSlide(1), 5000);
</script>

---

## Technical Specs

| Specification | Details |
|---------------|---------|
| Model | Anker 736 (Nano II 100W) |
| Dimensions | 2.64" × 1.24" × 2.24" |
| Weight | 7.26 oz (206 g) |
| Input | 100–240V ~ 2.1A, 50/60Hz |
| Ports | USB-C 1, USB-C 2, USB-A |
| Max Single Port | 100W (USB-C 1 or C2), 22.5W (USB-A) |
| Safety | IEC62368 certified, over-voltage/current/short protection |
| Warranty | 18 months |

---

## Power Allocation

| Ports Active | USB-C 1 | USB-C 2 | USB-A | Use Case |
|--------------|---------|---------|-------|----------|
| **Single** | 100W | 100W | 22.5W | Fast charge one laptop |
| **C1 + C2** | 60W | 40W | — | Laptop + tablet |
| **C1 + A** | 80W | — | 18W | Laptop + phone |
| **C2 + A** | — | 60W | 22.5W | Tablet + phone |
| **All Three** | 45W | 30W | 18W | Laptop + tablet + phone |

**Tip:** Connect high-power devices (laptops) to USB-C 1 for priority power allocation.

---

## Setup Guide

### Desk Setup

1. **Primary Device (USB-C 1):** Connect your main laptop here for 45–100W fast charging
2. **Secondary Device (USB-C 2):** Tablets, secondary laptops, or power banks
3. **Accessories (USB-A):** Phones, wireless earbuds, smartwatches

### Cable Management

- Use **100W-rated USB-C cables** for laptops
- Label cables with device names to avoid confusion
- Store cables with velcro ties or cable clips

### Power Optimization

- Mount on surge-protected power strip for equipment protection
- Use right-angle adapters if outlets are recessed
- Document your port mapping for team consistency

---

## Compatible Devices

**Laptops:** MacBook Pro/Air, Dell XPS, ThinkPad X1, Framework, Surface  
**Tablets:** iPad Pro/Air, Surface Go, Pixel Tablet  
**Phones:** iPhone 13+, Samsung Galaxy, Google Pixel  
**Accessories:** AirPods, Apple Watch (with puck), power banks

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
