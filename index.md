---
layout: default
title: Home
---

<section class="hero">
    <div class="hero-content">
        <img src="{{ '/assets/logo.svg' | relative_url }}" alt="Th1nkN3st Logo" class="hero-logo">
        
        <h1 class="hero-title">Welcome to Th1nkN3st</h1>
        <p class="hero-tagline">Smart Tools • Real Insights • Zero Hype</p>
        
        <p class="hero-description">
            We curate the best DevSecOps tools, automation gadgets, and tech insights that make your workflow smarter and more secure. Professional recommendations you can trust.
        </p>
        
        <div class="coming-soon-badge">
            🚀 Coming soon: In-depth reviews, guides, and curated finds
        </div>
    </div>
</section>

<section class="featured-articles">
    <div class="section-header">
        <h2 class="section-title">Featured Articles</h2>
        <p class="section-subtitle">Latest insights on DevSecOps tools, automation techniques, and productivity gear</p>
    </div>
    
    <div class="articles-grid">
        {% for post in site.posts limit:3 %}
        <article class="article-card">
            {% if post.tags.first %}
            <span class="article-tag">{{ post.tags.first }}</span>
            {% endif %}
            <h3 class="article-title">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            {% if post.excerpt %}
            <p class="article-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
            {% endif %}
            <div class="article-meta">
                <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
            </div>
        </article>
        {% endfor %}
        
        {% if site.posts.size == 0 %}
        <article class="article-card">
            <span class="article-tag">DEVSECOPS</span>
            <h3 class="article-title">Essential Security Tools for Modern Tech</h3>
            <p class="article-excerpt placeholder-text">Coming soon: Curated list of essential security tools...</p>
            <div class="article-meta">Coming Soon</div>
        </article>
        
        <article class="article-card">
            <span class="article-tag">AUTOMATION</span>
            <h3 class="article-title">Infrastructure as Code: Best Tools</h3>
            <p class="article-excerpt placeholder-text">Coming soon: Comprehensive guide to IaC tools...</p>
            <div class="article-meta">Coming Soon</div>
        </article>
        
        <article class="article-card">
            <span class="article-tag">GEAR REVIEW</span>
            <h3 class="article-title">Smart Home Gadgets for Tech Professionals</h3>
            <p class="article-excerpt placeholder-text">Coming soon: Reviews of productivity-enhancing gear...</p>
            <div class="article-meta">Coming Soon</div>
        </article>
        {% endif %}
    </div>
    
    <div style="text-align: center; margin-top: 2rem;">
        <a href="{{ '/blog/' | relative_url }}" class="read-more" style="font-size: 1.125rem;">View All Articles →</a>
    </div>
</section>

<section class="disclosure">
    <h3 class="disclosure-title">Affiliate Disclosure</h3>
    <p class="disclosure-text">
        <strong>Amazon Associates:</strong> As an Amazon Associate, Th1nkN3st earns from qualifying purchases (Store ID: th1nkn3st-20). We may earn commissions when you use our affiliate links.
    </p>
    <p class="disclosure-text">
        We only recommend products and services we genuinely believe in. Our reviews are honest and unbiased, regardless of affiliate relationships.
    </p>
</section>
