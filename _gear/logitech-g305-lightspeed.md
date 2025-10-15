---
layout: default
title: "Logitech G305 LIGHTSPEED Wireless Gaming Mouse"
excerpt: "Ultra-lightweight wireless gaming mouse with HERO sensor and 250-hour battery life."
brand: "Logitech G"
affiliate_short_url: "https://amzn.to/47b37wC"
images:
  - /assets/images/gear/logitech_g305_wless/image_1_.jpg
  - /assets/images/gear/logitech_g305_wless/image_2_.jpg
  - /assets/images/gear/logitech_g305_wless/image_3.jpg
  - /assets/images/gear/logitech_g305_wless/image_4.jpg
---

[← Back to Gear](/gear/) | [Shop Now →]({{ page.affiliate_short_url }})

---

<h1 class="product-title">{{ page.title }}</h1>

<div class="product-hero">
  <div class="product-info">
    <p>Ultra-fast LIGHTSPEED wireless technology meets HERO sensor efficiency in a lightweight design built for competitive gaming and productivity.</p>
    
    <h3>Key Features</h3>
    <ul>
      <li>Lightweight 99g design for high maneuverability</li>
      <li>LIGHTSPEED wireless with 1ms report rate</li>
      <li>HERO sensor: 12,000 DPI, 400 IPS precision</li>
      <li>250 hours battery life on single AA battery</li>
      <li>6 programmable buttons with onboard memory</li>
      <li>Ambidextrous design with portable form factor</li>
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

// Auto-advance every 5 seconds
setInterval(() => moveSlide(1), 5000);
</script>

---

## Technical Specs

| Specification | Details |
|---------------|---------|
| Model | Logitech G305 (910-005280) |
| Dimensions | 4.59" L × 2.45" W × 0.1" H |
| Weight | 3.36 oz (99 g) |
| Sensor | HERO optical sensor |
| DPI Range | Up to 12,000 DPI |
| Tracking Speed | > 400 IPS |
| Report Rate | 1ms (1000 Hz) |
| Connectivity | LIGHTSPEED Wireless (USB receiver) |
| Wireless Range | 10 meters |
| Battery | 1× AA (included) |
| Battery Life | 250 hours continuous use |
| Buttons | 6 programmable buttons |
| Onboard Memory | Yes |
| Orientation | Ambidextrous |
| Compatibility | Windows, Mac, PC, Laptop |

---

## Why This Mouse

### Performance
- **LIGHTSPEED Wireless**: Proprietary wireless tech delivers lag-free, 1ms response time—indistinguishable from wired
- **HERO Sensor**: Next-gen optical sensor with 10x power efficiency and pixel-precise tracking up to 12,000 DPI
- **Competition Ready**: Tournament-approved wireless performance with mechanical button tensioning

### Design
- **Ultra-Lightweight**: At 99g, provides effortless control for extended gaming or work sessions
- **Ambidextrous**: Symmetrical design works for left and right-handed users
- **Portable**: Compact form factor with built-in USB receiver storage

### Battery Life
- **250 Hours**: Weeks of continuous use on a single AA battery
- **Power Efficient**: HERO sensor technology extends battery life 10x over previous generations
- **No Interruptions**: Low-battery indicator prevents mid-game surprises

---

## Setup Guide

### Initial Configuration

1. **Install Battery**: Insert included AA battery (or use AAA with adapter for lighter weight)
2. **Connect Receiver**: Plug USB wireless receiver into PC/laptop
3. **Power On**: Slide power switch on mouse bottom
4. **Install G HUB** (optional): Download Logitech G HUB software for advanced customization

### Software Customization (G HUB)

- **DPI Settings**: Configure up to 5 DPI levels (200–12,000 range)
- **Button Programming**: Assign macros, commands, or hotkeys to 6 buttons
- **Onboard Memory**: Save profiles directly to mouse for use on any PC
- **Surface Tuning**: Calibrate sensor for your specific mousepad

### Pro Tips

- **Weight Reduction**: Replace AA with AAA battery + adapter to reach 84g
- **DPI Optimization**: Most FPS pros use 400–800 DPI with large mousepads
- **Polling Rate**: Default 1000 Hz is optimal; higher rates don't provide benefit with wireless
- **Battery Life**: Disable RGB lighting (if present) and lower DPI to extend battery life

---

## Use Cases

**Gaming:** Competitive FPS (CS:GO, Valorant), MOBAs, battle royale  
**Productivity:** CAD work, photo editing, general office use  
**Travel:** Portable design fits in laptop bags; built-in receiver storage  
**Multi-Device:** Pair with laptop during travel, desktop at home

---

## Compatible Devices

**Operating Systems:** Windows 7+, macOS 10.11+, Chrome OS  
**Connection:** USB-A port (or use USB-C adapter)  
**Ideal Pairing:** Gaming laptops, ultrabooks, desktop PCs, hackintoshes

---

## Purchase

<a href="{{ page.affiliate_short_url }}" class="read-more" target="_blank" rel="nofollow sponsored noopener">Buy on Amazon →</a>

> As an Amazon Associate, Th1nkN3st earns from qualifying purchases. Using our links supports our reviews—thank you!

---

## Related Items

- [Anker Prime 67W Compact Fast Charger](/gear/anker-prime-67w/) - Keep your gaming laptop charged
- [Browse All Gear](/gear/)
- [DevSecOps Tools](/tools/)

---

[← Back to Gear](/gear/) | [Tools Library](/tools/) | [Home](/)
