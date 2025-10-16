# 🔗 Branded Affiliate Shortlinks

This directory contains redirect pages for clean, branded affiliate links.

## 📋 How It Works

Each `.html` file in this directory creates a shortlink like:
- `https://www.th1nkn3st.com/go/anker67/` → redirects to Amazon affiliate link
- `https://www.th1nkn3st.com/go/logitechg305/` → redirects to Amazon affiliate link
- etc.

## ✨ Benefits

✅ **Professional**: Clean URLs for social media posts  
✅ **Private**: Hides affiliate IDs from public view  
✅ **Flexible**: Change destination URLs without updating posts  
✅ **Trackable**: Monitor clicks via analytics  

## � Quick Start (Automated Method)

**Use the generator script to create multiple redirects at once!**

### Option 1: CSV File

1. **Edit `redirects.csv`** in the root directory:
   ```csv
   slug,affiliate_link,product_name
   anker67,https://amzn.to/4qhzGlu,Anker Prime 67W
   newproduct,https://amzn.to/XXXXXX,Product Name
   ```

2. **Run the generator**:
   ```bash
   python3 generate_redirects.py redirects.csv
   ```

### Option 2: JSON File

1. **Edit `redirects.json`** in the root directory:
   ```json
   {
     "redirects": [
       {
         "slug": "anker67",
         "affiliate_link": "https://amzn.to/4qhzGlu",
         "product_name": "Anker Prime 67W"
       }
     ]
   }
   ```

2. **Run the generator**:
   ```bash
   python3 generate_redirects.py redirects.json
   ```

The script will:
- ✅ Generate all redirect HTML files in `go/`
- ✅ Add proper YAML front matter
- ✅ Include affiliate disclosure
- ✅ Overwrite existing files (safe to re-run)

## 📝 Manual Method (Single Redirect)

1. **Copy the template**:
   ```bash
   cp go/_template.html go/yourproduct.html
   ```

2. **Edit three things**:
   - `title:` - Change to your product name
   - `permalink:` - Change to `/go/yourslug/`
   - Both redirect URLs - Update to your Amazon shortlink

3. **Build and test**:
   ```bash
   bundle exec jekyll build
   # Visit https://www.th1nkn3st.com/go/yourslug/
   ```

## 🎯 Current Redirects

| Shortlink | Product | Destination |
|-----------|---------|-------------|
| `/go/anker67/` | Anker Prime 67W Charger | `https://amzn.to/4qhzGlu` |
| `/go/logitechg305/` | Logitech G305 Mouse | `https://amzn.to/47b37wC` |
| `/go/samsungg9/` | Samsung Odyssey G9 Monitor | `https://amzn.to/477v8VR` |

## � Workflow for Adding Products

1. Add new entries to `redirects.csv` or `redirects.json`
2. Run: `python3 generate_redirects.py redirects.csv`
3. Test locally: `http://localhost:4000/go/yourslug/`
4. Commit: `git add go/ redirects.csv && git commit -m "Add new redirects"`
5. Push: `git push`
6. Test live: `https://www.th1nkn3st.com/go/yourslug/`

## �🔒 Important Notes

- All redirects include affiliate disclosure per FTC guidelines
- Instant redirect (0 second delay)
- Fallback link provided for accessibility
- SEO-friendly with canonical URL
- Script overwrites existing files (safe to re-run)

## 📚 Files in This System

- `go/_template.html` - Manual template for reference
- `go/*.html` - Generated redirect pages
- `../generate_redirects.py` - Automated generator script
- `../redirects.csv` - CSV data source (recommended)
- `../redirects.json` - JSON data source (alternative)

---

**Generator Script**: `../generate_redirects.py`  
**Last Updated**: October 16, 2025
