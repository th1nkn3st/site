---
layout: default
title: Blog
permalink: /blog/
---

# Latest Articles

Stay up-to-date with our latest insights, reviews, and recommendations for DevSecOps tools, automation techniques, and productivity enhancements.

<div class="posts">
  {% for post in site.posts %}
    <article class="post">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
      
      {% if post.excerpt %}
        <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
      {% endif %}
      
      <div class="post-tags">
        {% for tag in post.tags %}
          <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
      
      <a href="{{ post.url | relative_url }}" class="read-more">Read More →</a>
    </article>
  {% endfor %}
</div>

{% if site.posts.size == 0 %}
<div class="no-posts">
  <p><em>No posts yet. Check back soon for our latest insights on DevSecOps tools and automation!</em></p>
</div>
{% endif %}

---

## Categories

Browse articles by topic:

- **DevSecOps**: Security-first development and operations practices
- **Automation**: Tools and techniques for workflow optimization  
- **Reviews**: Honest evaluations of tools and technologies
- **Guides**: Step-by-step implementation tutorials
- **Industry**: Trends, news, and professional insights

## Subscribe

Stay updated with our latest content:

- **RSS Feed**: [{{ site.url }}{{ site.baseurl }}/feed.xml]({{ site.url }}{{ site.baseurl }}/feed.xml)
- **Social Media**: Follow us on [Twitter](https://twitter.com/th1nkn3st), [LinkedIn](https://linkedin.com/company/th1nkn3st)