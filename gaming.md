---
layout: default
title: Gaming
permalink: /gaming/
---

# Gaming

Level up with curated gaming gear, reviews, and recommendations. From peripherals to setups, we cover what gamers actually use.

{% assign empty_array = "" | split: "" %}
{% assign gaming_items = site.gaming | default: empty_array | sort: 'date' | reverse %}
{% if gaming_items.size > 0 %}
<div class="content-grid">
  {% for item in gaming_items %}
    {% include card.html item=item type="article" show_date=true show_tags=true %}
  {% endfor %}
</div>
{% else %}
<p class="empty-state"><em>No gaming content published yet. Check back soon for reviews, guides, and gear recommendations!</em></p>
{% endif %}

---

<nav class="section-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a> | 
  <a href="{{ '/geek/' | relative_url }}">Geek Culture</a> | 
  <a href="{{ '/diy/' | relative_url }}">DIY Projects</a>
</nav>
