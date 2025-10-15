---
layout: default
title: Tools
permalink: /tools/
---

# DevSecOps Tools Library

Actionable picks to streamline secure delivery. We focus on gear and workflows that reduce friction while keeping guardrails in place.

{% assign tool_items = site.tools | sort: 'title' %}
{% if tool_items.size > 0 %}
<section class="featured-articles">
  <div class="articles-grid">
    {% for item in tool_items %}
    <article class="article-card">
      <h2 class="article-title">
        <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      </h2>
      {% if item.excerpt %}
      <p class="article-excerpt">{{ item.excerpt }}</p>
      {% endif %}
      <div class="article-meta">
        {% if item.brand %}
        <span>Featured vendor: {{ item.brand }}</span>
        {% endif %}
      </div>
      <div style="margin-top: 1rem;">
        <a href="{{ item.url | relative_url }}" class="read-more">Implementation Guide →</a>
      </div>
      {% if item.affiliate_short_url or item.affiliate_url %}
      <div style="margin-top: 0.5rem;">
        <a href="{{ item.affiliate_short_url | default: item.affiliate_url }}" class="read-more" target="_blank" rel="nofollow sponsored noopener">Buy Hardware →</a>
      </div>
      {% endif %}
    </article>
    {% endfor %}
  </div>
</section>
{% else %}
<p><em>No toolkits published yet. Bookmark this page for upcoming automation playbooks.</em></p>
{% endif %}

---

[← Back to Home]({{ '/' | relative_url }}) | [Visit Gear Library]({{ '/gear/' | relative_url }}) | [Browse Blog]({{ '/blog/' | relative_url }})
