---
layout: default
title: Geek Culture
permalink: /geek/
---

# Geek Culture

Dive into the world of geek culture—tech trends, collectibles, fandoms, and everything that makes us nerdy. Embrace your inner geek.

# Geek Culture

Dive into the latest tech trends, collectibles, and fandoms. We explore the things that make us gleefully nerdy.

{% assign empty_array = "" | split: "" %}
{% assign geek_items = site.geek | default: empty_array | sort: 'date' | reverse %}
{% if geek_items.size > 0 %}
<div class="content-grid">
  {% for item in geek_items %}
    {% include card.html item=item type="article" show_date=true show_tags=true %}
  {% endfor %}
</div>
{% else %}
<p class="empty-state"><em>No geek culture content published yet. Check back soon for the latest in tech trends, collectibles, and more!</em></p>
{% endif %}

---

<nav class="section-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a> | 
  <a href="{{ '/gaming/' | relative_url }}">Gaming</a> | 
  <a href="{{ '/diy/' | relative_url }}">DIY Projects</a>
</nav>
