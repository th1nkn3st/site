---
layout: default
title: Gear
permalink: /gear/
---

# Tech Gear & Gadgets

Curated picks for the hybrid workbench and road-warrior kit. Every recommendation is hands-on tested or team-approved, with affiliate links that help keep Th1nkN3st running.

{% assign gear_items = site.gear | sort: 'title' %}
{% if gear_items.size > 0 %}
<section class="featured-articles">
  <div class="articles-grid">
    {% for item in gear_items %}
    <article class="article-card">
      <h2 class="article-title">
        <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      </h2>
      {% if item.excerpt %}
      <p class="article-excerpt">{{ item.excerpt }}</p>
      {% endif %}
      <div class="article-meta">
        {% if item.brand %}
        <span>Brand: {{ item.brand }}</span>
        {% endif %}
      </div>
      <div style="margin-top: 1rem;">
        <a href="{{ item.url | relative_url }}" class="read-more">View Details →</a>
      </div>
      {% if item.affiliate_short_url or item.affiliate_url %}
      <div style="margin-top: 0.5rem;">
        <a href="{{ item.affiliate_short_url | default: item.affiliate_url }}" class="read-more" target="_blank" rel="nofollow sponsored noopener">Shop Now →</a>
      </div>
      {% endif %}
    </article>
    {% endfor %}
  </div>
</section>
{% else %}
<p><em>No gear highlights published yet. Check back soon for our favorite workstation upgrades.</em></p>
{% endif %}

---

[← Back to Home]({{ '/' | relative_url }}) | [Visit Tools Library]({{ '/tools/' | relative_url }}) | [Browse Blog]({{ '/blog/' | relative_url }})
