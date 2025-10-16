---
layout: default
title: Categories
permalink: /categories/
---

# Browse by Category

Explore content organized by category. Find articles, reviews, and guides in each topic area.

{% comment %} Collect all categories from all content types {% endcomment %}
{% assign all_items = site.posts | concat: site.gaming | concat: site.geek | concat: site.diy | concat: site.gear | concat: site.tools %}
{% assign all_categories = "" | split: "" %}
{% for item in all_items %}
  {% if item.categories %}
    {% assign all_categories = all_categories | concat: item.categories %}
  {% endif %}
{% endfor %}
{% assign unique_categories = all_categories | uniq | sort %}

{% if unique_categories.size > 0 %}
<div class="category-list">
  {% for category in unique_categories %}
    <a href="#{{ category | slugify }}" class="category-link">{{ category }}</a>
  {% endfor %}
</div>

<hr class="section-divider">

{% for category in unique_categories %}
  {% assign category_slug = category | slugify %}
  {% assign categorized_items = all_items | where_exp: "item", "item.categories contains category" | sort: 'date' | reverse %}
  
  <section id="{{ category_slug }}" class="category-section">
    <h2 class="category-heading">
      {{ category }} <span class="category-count">({{ categorized_items.size }})</span>
    </h2>
    
    <div class="category-items">
      {% for item in categorized_items %}
      <article class="category-item">
        <h3 class="category-item-title">
          <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
        </h3>
        {% if item.date %}
        <time class="category-item-date" datetime="{{ item.date | date_to_xmlschema }}">
          {{ item.date | date: "%B %d, %Y" }}
        </time>
        {% endif %}
        {% if item.excerpt %}
        <p class="category-item-excerpt">{{ item.excerpt | strip_html | truncatewords: 20 }}</p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
{% endfor %}

{% else %}
<p class="empty-state"><em>No categorized content yet. Check back soon!</em></p>
{% endif %}

---

<nav class="section-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a> | 
  <a href="{{ '/tags/' | relative_url }}">Browse by Tag</a>
</nav>
