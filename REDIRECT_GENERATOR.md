# 🔗 Redirect Generator Documentation

Automated tool for creating branded affiliate shortlink pages for Th1nkN3st.

## 🎯 Purpose

Generate clean, professional redirect URLs like:
- `https://www.th1nkn3st.com/go/anker67/` → `https://amzn.to/4qhzGlu`
- `https://www.th1nkn3st.com/go/logitechg305/` → `https://amzn.to/47b37wC`

## ⚡ Quick Start

```bash
# 1. Edit your product data
nano redirects.csv

# 2. Generate redirect pages
python3 generate_redirects.py redirects.csv

# 3. Test locally
bundle exec jekyll serve
# Visit http://localhost:4000/go/yourslug/

# 4. Deploy
git add go/ redirects.csv
git commit -m "Add new affiliate redirects"
git push
```

## 📝 Data Formats

### CSV Format (Recommended)

**File**: `redirects.csv`

```csv
slug,affiliate_link,product_name
anker67,https://amzn.to/4qhzGlu,Anker Prime 67W
logitechg305,https://amzn.to/47b37wC,Logitech G305
samsungg9,https://amzn.to/477v8VR,Samsung Odyssey G9
```

**Usage**:
```bash
python3 generate_redirects.py redirects.csv
```

### JSON Format (Alternative)

**File**: `redirects.json`

```json
{
  "redirects": [
    {
      "slug": "anker67",
      "affiliate_link": "https://amzn.to/4qhzGlu",
      "product_name": "Anker Prime 67W"
    },
    {
      "slug": "logitechg305",
      "affiliate_link": "https://amzn.to/47b37wC",
      "product_name": "Logitech G305"
    }
  ]
}
```

**Usage**:
```bash
python3 generate_redirects.py redirects.json
```

## 🔧 Script Features

✅ **Batch Generation**: Create multiple redirects at once  
✅ **Auto-formatting**: Proper YAML front matter & HTML  
✅ **Overwrite Safe**: Re-run anytime to update existing files  
✅ **Validation**: Skips invalid entries automatically  
✅ **Clean Output**: Shows exactly what was created  

## 📋 Field Descriptions

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `slug` | ✅ Yes | URL-friendly identifier | `anker67`, `logitechg305` |
| `affiliate_link` | ✅ Yes | Full Amazon shortlink | `https://amzn.to/4qhzGlu` |
| `product_name` | ⚠️ Optional | Product display name | `Anker Prime 67W` |

**Notes**:
- `slug` becomes the URL: `/go/{slug}/`
- `product_name` defaults to `slug` if not provided
- Script validates required fields and skips invalid rows

## 🎨 Generated HTML Structure

Each redirect page includes:

```html
---
layout: default
title: "Redirecting to {product_name}..."
permalink: /go/{slug}/
---

<meta http-equiv="refresh" content="0; url={affiliate_link}">
<link rel="canonical" href="https://www.th1nkn3st.com/go/{slug}/" />

<section style="text-align:center;margin:80px auto;max-width:600px;">
  <p>Redirecting you to Amazon...</p>
  <p style="font-size:0.9rem;color:#888;">
    As an Amazon Associate, Th1nkN3st earns from qualifying purchases.
  </p>
  <p>If you're not redirected automatically, 
     <a href="{affiliate_link}">click here</a>.
  </p>
</section>
```

## 🔄 Typical Workflows

### Adding One Product

```bash
# Add line to CSV
echo "newslug,https://amzn.to/XXXXX,Product Name" >> redirects.csv

# Regenerate all
python3 generate_redirects.py redirects.csv

# Test & deploy
git add go/ redirects.csv && git commit -m "Add redirect for Product Name" && git push
```

### Bulk Update

```bash
# Edit CSV with multiple new products
nano redirects.csv

# Generate all redirects (overwrites existing)
python3 generate_redirects.py redirects.csv

# Review changes
git diff go/

# Deploy
git add go/ redirects.csv && git commit -m "Bulk update redirects" && git push
```

### Testing Before Deploy

```bash
# Generate redirects
python3 generate_redirects.py redirects.csv

# Start local server
bundle exec jekyll serve

# Test in browser
open http://localhost:4000/go/yourslug/

# Should redirect to your affiliate link
```

## 🐛 Troubleshooting

### "File not found" Error
```bash
# Make sure file exists
ls -la redirects.csv

# Check you're in the right directory
pwd
# Should show: /home/will/devops/th1nkn3st/site
```

### "No valid redirects found"
```bash
# Check CSV format (must have header row)
head -2 redirects.csv
# Should show:
# slug,affiliate_link,product_name
# anker67,https://amzn.to/4qhzGlu,Anker Prime 67W

# Check for required fields
cat redirects.csv | grep -v "^slug" | cut -d',' -f1,2
```

### Redirect Not Working
```bash
# Rebuild Jekyll site
bundle exec jekyll clean
bundle exec jekyll build

# Check file was generated
ls -la _site/go/yourslug/

# Should show: index.html
```

## 📂 File Structure

```
site/
├── generate_redirects.py    # Generator script
├── redirects.csv             # CSV data source
├── redirects.json            # JSON data source (alternative)
└── go/
    ├── README.md             # Documentation
    ├── _template.html        # Manual template
    ├── anker67.html          # Generated redirect
    ├── logitechg305.html     # Generated redirect
    └── samsungg9.html        # Generated redirect
```

## 🚀 Advanced Usage

### Custom Output Directory

Edit script line 86 to change output location:
```python
go_dir = Path(__file__).parent / 'go'  # Change 'go' to your dir
```

### Adding Custom Fields

Extend the template in `REDIRECT_TEMPLATE` variable and add fields to CSV/JSON.

### Integration with CI/CD

```yaml
# .github/workflows/generate-redirects.yml
- name: Generate redirects
  run: python3 generate_redirects.py redirects.csv
  
- name: Commit changes
  run: |
    git add go/
    git commit -m "Auto-generate redirects" || true
```

## 📊 Example Output

```
$ python3 generate_redirects.py redirects.csv

Reading CSV file: redirects.csv

Generating 3 redirect file(s)...

  ✓ Created: go/anker67.html → https://amzn.to/4qhzGlu
  ✓ Created: go/logitechg305.html → https://amzn.to/47b37wC
  ✓ Created: go/samsungg9.html → https://amzn.to/477v8VR

✅ Successfully generated 3 redirect file(s)

Next steps:
  1. Test locally: http://localhost:4000/go/<slug>/
  2. Commit: git add go/ && git commit -m 'Add affiliate redirects'
  3. Push: git push
  4. Test live: https://www.th1nkn3st.com/go/<slug>/
```

## 📜 License

Part of the Th1nkN3st site project. For internal use.

---

**Version**: 1.0  
**Last Updated**: October 16, 2025  
**Author**: Th1nkN3st Team
