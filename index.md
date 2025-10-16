---
layout: default
title: Home
---

<section class="hero">
    <div class="hero-content">
        <img src="{{ '/assets/logo.svg' | relative_url }}" alt="Th1nkN3st Logo" class="hero-logo">
        
        <h1 class="hero-title">Welcome to Th1nkN3st</h1>
        <p class="hero-tagline">Smart Tech • Gaming • Geek Culture • DIY • DevSecOps</p>
        
        <p class="hero-description">
            Your hub for curated tech reviews, gaming gear, geek culture, DIY projects, and DevSecOps tools. Real insights from enthusiasts, zero marketing fluff.
        </p>
    </div>
</section>

{% comment %} Latest Posts Section - Mix of posts, gaming, geek, diy {% endcomment %}
{% assign all_posts = site.posts | concat: site.gaming | concat: site.geek | concat: site.diy | sort: 'date' | reverse %}

<section class="homepage-section">
    <div class="section-header">
        <h2 class="section-title">Latest Posts</h2>
        <p class="section-subtitle">Fresh content across gaming, geek culture, DIY, and DevSecOps</p>
    </div>
    
    {% if all_posts.size > 0 %}
    <div class="content-grid">
        {% for item in all_posts limit:6 %}
          {% include card.html item=item type="article" show_date=true %}
        {% endfor %}
    </div>
    <div class="section-cta">
        <a href="{{ '/blog/' | relative_url }}" class="btn-primary">View All Posts →</a>
    </div>
    {% else %}
    <p class="empty-state"><em>Content coming soon! Check back for reviews, guides, and insights.</em></p>
    {% endif %}
</section>

{% comment %} Trending Gear Section {% endcomment %}
{% assign gear_items = site.gear | where_exp: "item", "item.slug != '_TEMPLATE'" | sort: 'title' %}

<section class="homepage-section">
    <div class="section-header">
        <h2 class="section-title">Trending Gear</h2>
        <p class="section-subtitle">Curated tech gear and gadgets we actually use</p>
    </div>
    
    {% if gear_items.size > 0 %}
    <div class="content-grid">
        {% for item in gear_items limit:6 %}
          {% include card.html item=item type="gear" show_date=false %}
        {% endfor %}
    </div>
    <div class="section-cta">
        <a href="{{ '/gear/' | relative_url }}" class="btn-primary">Browse All Gear →</a>
    </div>
    {% else %}
    <p class="empty-state"><em>Gear reviews coming soon! Stay tuned for our top recommendations.</em></p>
    {% endif %}
</section>

{% comment %} From the Labs Section - DIY Projects {% endcomment %}
{% assign diy_items = site.diy | sort: 'date' | reverse %}

<section class="homepage-section">
    <div class="section-header">
        <h2 class="section-title">From the Labs</h2>
        <p class="section-subtitle">Hands-on DIY projects and maker experiments</p>
    </div>
    
    {% if diy_items.size > 0 %}
    <div class="content-grid">
        {% for item in diy_items limit:6 %}
          {% include card.html item=item type="article" show_date=true %}
        {% endfor %}
    </div>
    <div class="section-cta">
        <a href="{{ '/diy/' | relative_url }}" class="btn-primary">View All DIY Projects →</a>
    </div>
    {% else %}
    <p class="empty-state"><em>DIY projects in the works! Check back for build guides and maker content.</em></p>
    {% endif %}
</section>


