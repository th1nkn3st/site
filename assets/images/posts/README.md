# Blog Post Images

This directory contains images organized by article identifier.

## Structure

Each article has its own folder named with an article identifier (e.g., `A1`, `A2`, `A3`).

```
posts/
├── A1/              # Article 1 (AI Compliance)
│   ├── hero.png     # Hero graphic for top of article
│   ├── A1-G1.png   # Graph 1
│   ├── A1-G2.png   # Graph 2
│   └── ...
├── A2/              # Article 2 (future article)
│   └── ...
└── README.md        # This file
```

## Naming Convention

- **Hero graphic**: `hero.png` (always at the top of the article)
- **Other graphics**: `{ArticleID}-G{Number}.png`
  - Example: `A1-G1.png`, `A1-G2.png`, etc.

## Adding Images to a New Article

1. Create a new folder: `A{N}/` (increment N for each new article)
2. Add your images following the naming convention
3. Reference images in your markdown using: `/assets/images/posts/{ArticleID}/{filename}`

## Example Usage in Markdown

```markdown
![Hero Image](/assets/images/posts/A1/hero.png)

![Graph 1](/assets/images/posts/A1/A1-G1.png)
```

