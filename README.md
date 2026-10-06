# Th1nkN3st

**Smart Tools • Real Insights • Zero Hype**

Welcome to the source repository for [Th1nkN3st](https://www.th1nkn3st.com) — a curated tech and automation content platform focused on DevSecOps tools, automation gadgets, and practical insights for professionals.

## 🎯 About

Th1nkN3st is a content brand dedicated to cutting through the noise in the tech world. We review and recommend:

- **DevSecOps Tools** — Security automation, monitoring, and infrastructure tools
- **Automation Gadgets** — Productivity enhancers and workflow optimizers
- **Tech Insights** — Practical guides and honest reviews

Our mission: Help tech professionals discover tools that actually work, with zero marketing fluff.

## 🎮 Games and Apps

Every Th1nkN3st game or app gets three pages from one data file:

| URL | What it is |
| --- | --- |
| `/<slug>/` | Landing page: hero, features, store buttons |
| `/<slug>/privacy/` | Privacy policy, for the store listing and the in-app link |
| `/<slug>/support/` | FAQ and contact, for the App Store "Support URL" |

### Adding an app

```bash
python new_app.py my-app "My App"              # data file + all three pages
python new_app.py my-app "My App" --card-only  # homepage card only, pages later
```

Then fill in `_data/apps/my-app.yml`. The comments in
[`_app_template/app.yml`](_app_template/app.yml) explain every field. Put
images in `assets/images/my-app/`.

- **Homepage and contact page** list apps automatically, sorted by `order`.
  An app's card links to its pages once the `my-app/` folder exists.
- **Store buttons** appear when `status` is `Available` (or `Beta`, which
  also shows the `testing` link). Before that, the page says "coming soon to …".
- **Privacy policy** is generated from the `privacy:` block. Keep it truthful:
  list every permission, third-party SDK (ads, analytics, crash reporting), and
  any data that leaves the device, and bump `effective` when it changes.
- **Look** comes from the `theme:` colours. Anything left out uses the studio palette.
- **Extra intro text** goes in the body of `my-app/index.md`.

Pull requests run the GitHub Pages build plus `python new_app.py --check _site`,
so a broken page fails the PR instead of the live site.

## 🏗️ Tech Stack

- **Generator**: Jekyll 3.9.5 (GitHub Pages compatible)
- **Hosting**: GitHub Pages
- **Theme**: Custom dark theme based on jekyll-theme-hacker
- **Domain**: [th1nkn3st.com](https://www.th1nkn3st.com)

## 📁 Repository Structure

```
site/
├── _config.yml           # Jekyll configuration
├── _layouts/             # Custom page layouts
│   ├── default.html      # Main site layout
│   └── post.html         # Blog post layout
├── _posts/               # Blog posts (YYYY-MM-DD-title.md format)
├── assets/               # CSS, images, and static files
│   ├── custom.css        # Custom styling
│   ├── homepage.css      # Homepage-specific styles
│   └── logo.svg          # Site logo
├── index.md              # Homepage
├── blog.md               # Blog index
├── tools.md              # Tools page
├── gear.md               # Gear recommendations
├── contact.md            # Contact page
└── robots.txt            # SEO configuration
```

## � Local Development

Want to run the site locally? Here's how:

### Prerequisites

- Ruby 3.0 or higher
- Bundler gem

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/th1nkn3st/site.git
   cd site
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Serve locally**
   ```bash
   bundle exec jekyll serve
   ```

4. **View in browser**
   ```
   Open http://localhost:4000
   ```

The site will auto-reload when you make changes to files.

### Building for Production

```bash
bundle exec jekyll build
```

The static site will be generated in the `_site/` directory.

## 📝 Content Guidelines

### Adding a Blog Post

Create a new file in `_posts/` following this format:

**Filename**: `YYYY-MM-DD-post-title.md`

**Front Matter**:
```yaml
---
layout: post
title: "Your Post Title"
date: 2025-10-15
categories: [devsecops, tools, automation]
tags: [security, productivity, review]
---

Your content here...
```

## 🚢 Deployment

This site is automatically deployed via **GitHub Pages**:

1. Push changes to the `main` branch
2. GitHub Pages automatically builds and deploys
3. Changes are live at [th1nkn3st.com](https://www.th1nkn3st.com) within minutes

No manual build or deployment steps required!

## � Security

We take security seriously. If you discover a security vulnerability, please see our [Security Policy](SECURITY.md) or contact us at:

📧 **devsecopstips@gmail.com**

For general inquiries, feedback, or collaboration opportunities, feel free to reach out!

## 🤝 Contributing

While this is primarily a personal content platform, we welcome:

- **Bug reports** — Found a broken link or display issue? Open an issue!
- **Suggestions** — Have ideas for content or improvements? Let us know!
- **Tool recommendations** — Know a great tool we should review? Contact us!

We're not accepting pull requests for content at this time, but technical improvements are always appreciated.

## 📄 License & Disclosure

### Content License
All content, articles, and original writing © 2025 Th1nkN3st. All rights reserved.

### Affiliate Disclosure
Th1nkN3st participates in affiliate programs including Amazon Associates. We may earn commissions from qualifying purchases made through our links. Our reviews remain honest and unbiased regardless of affiliate relationships.

### Code License
The Jekyll site structure and custom code in this repository are available for reference and learning. Please don't copy our design or branding, but feel free to learn from the implementation.

## 📞 Connect

- **Website**: [th1nkn3st.com](https://www.th1nkn3st.com)
- **Email**: devsecopstips@gmail.com
- **Twitter**: [@th1nkn3st](https://twitter.com/th1nkn3st)
- **LinkedIn**: [company/th1nkn3st](https://linkedin.com/company/th1nkn3st)
- **Pinterest**: [th1nkn3st](https://pinterest.com/th1nkn3st)

## 🌟 Support

Enjoying our content? Here's how you can support:

- **Subscribe** to our [RSS feed](/feed.xml)
- **Share** our articles with your network
- **Use our affiliate links** when purchasing recommended tools
- **Follow us** on social media

---

**Built with ❤️ for the DevSecOps community**

*Smart tools. Real insights. Zero hype.*

