---
layout: default
title: DIY
permalink: /diy/
---

# DIY Projects

Build, hack, and create with our hands-on DIY projects. From smart home automation to custom PC builds, we document what works.

{% assign empty_array = "" | split: "" %}
{% assign diy_items = site.diy | default: empty_array | sort: 'date' | reverse %}
{% if diy_items.size > 0 %}
<div class="content-grid">
  {% for item in diy_items %}
    {% include card.html item=item type="article" show_date=true show_tags=true %}
  {% endfor %}
</div>
{% else %}
<p class="empty-state"><em>No DIY projects published yet. Check back soon for step-by-step guides and maker projects!</em></p>
{% endif %}

---

<nav class="section-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a> | 
  <a href="{{ '/gaming/' | relative_url }}">Gaming</a> | 
  <a href="{{ '/geek/' | relative_url }}">Geek Culture</a>
</nav>
