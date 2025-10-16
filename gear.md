---
layout: default
title: Gear
permalink: /gear/
---

# Tech Gear & Gadgets

Curated picks for the hybrid workbench and road-warrior kit. Every recommendation is hands-on tested or team-approved, with affiliate links that help keep Th1nkN3st running.

{% assign gear_items = site.gear | where_exp: "item", "item.slug != '_TEMPLATE'" | sort: 'title' %}
{% if gear_items.size > 0 %}
<div class="content-grid">
  {% for item in gear_items %}
    {% include card.html item=item type="gear" show_date=false %}
  {% endfor %}
</div>
{% else %}
<p class="empty-state"><em>No gear highlights published yet. Check back soon for our favorite workstation upgrades.</em></p>
{% endif %}

---

<nav class="section-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a> | 
  <a href="{{ '/tools/' | relative_url }}">Visit Tools Library</a> | 
  <a href="{{ '/blog/' | relative_url }}">Browse Blog</a>
</nav>
