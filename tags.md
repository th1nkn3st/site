---
layout: default
title: Tags
permalink: /tags/
---

# Browse by Tag

Explore content organized by tags. Click any tag to see related articles and reviews.

{% comment %} Collect all tags from all content types {% endcomment %}
{% assign all_items = site.posts | concat: site.gaming | concat: site.geek | concat: site.diy | concat: site.gear | concat: site.tools %}
{% assign all_tags = "" | split: "" %}
{% for item in all_items %}
  {% if item.tags %}
    {% assign all_tags = all_tags | concat: item.tags %}
  {% endif %}
{% endfor %}
{% assign unique_tags = all_tags | uniq | sort %}

{% if unique_tags.size > 0 %}
<div class="tag-cloud">
  {% for tag in unique_tags %}
    <a href="#{{ tag | slugify }}" class="tag-link">{{ tag }}</a>
  {% endfor %}
</div>

<hr class="section-divider">

{% for tag in unique_tags %}
  {% assign tag_slug = tag | slugify %}
  {% assign tagged_items = all_items | where_exp: "item", "item.tags contains tag" | sort: 'date' | reverse %}
  
  <section id="{{ tag_slug }}" class="tag-section">
    <h2 class="tag-heading">
      {{ tag }} <span class="tag-count">({{ tagged_items.size }})</span>
    </h2>
    
    <div class="tag-items">
      {% for item in tagged_items %}
      <article class="tag-item">
        <h3 class="tag-item-title">
          <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
        </h3>
        {% if item.date %}
        <time class="tag-item-date" datetime="{{ item.date | date_to_xmlschema }}">
          {{ item.date | date: "%B %d, %Y" }}
        </time>
        {% endif %}
        {% if item.excerpt %}
        <p class="tag-item-excerpt">{{ item.excerpt | strip_html | truncatewords: 20 }}</p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
{% endfor %}

{% else %}
<p class="empty-state"><em>No tagged content yet. Check back soon!</em></p>
{% endif %}

---

<nav class="section-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a> | 
  <a href="{{ '/categories/' | relative_url }}">Browse by Category</a>
</nav>
