# 🎯 Redirect System - Quick Reference

## 📦 What You Got

✅ **Automated Generator** - Create redirects from CSV/JSON  
✅ **Helper Script** - Add single redirects quickly  
✅ **Template** - Manual creation option  
✅ **Documentation** - Full usage guide  

## ⚡ Three Ways to Create Redirects

### 1️⃣ Bulk Generation (RECOMMENDED)

```bash
# Edit CSV with all your products
nano redirects.csv

# Generate all redirect files
python3 generate_redirects.py redirects.csv

# Done! All HTML files created in go/
```

### 2️⃣ Quick Single Add

```bash
# Add one product quickly
./add_redirect.sh myproduct https://amzn.to/XXXXX "Product Name"

# Then generate
python3 generate_redirects.py redirects.csv
```

### 3️⃣ Manual Creation

```bash
# Copy template
cp go/_template.html go/myproduct.html

# Edit the file manually
nano go/myproduct.html
```

## 📋 CSV Format

```csv
slug,affiliate_link,product_name
anker67,https://amzn.to/4qhzGlu,Anker Prime 67W
myproduct,https://amzn.to/XXXXX,My Product
```

## 🔄 Complete Workflow

```bash
# 1. Add products to CSV
echo "newproduct,https://amzn.to/XXXXX,New Product" >> redirects.csv

# 2. Generate redirect files
python3 generate_redirects.py redirects.csv

# 3. Test locally
bundle exec jekyll serve
# Visit http://localhost:4000/go/newproduct/

# 4. Commit and push
git add go/ redirects.csv
git commit -m "Add redirect for New Product"
git push

# 5. Test live (wait 1-2 min for GitHub Pages)
# Visit https://www.th1nkn3st.com/go/newproduct/
```

## 📚 Files Overview

| File | Purpose |
|------|---------|
| `generate_redirects.py` | Main generator script |
| `add_redirect.sh` | Quick helper for single adds |
| `redirects.csv` | Product data (recommended) |
| `redirects.json` | Product data (alternative) |
| `REDIRECT_GENERATOR.md` | Full documentation |
| `go/_template.html` | Manual template |
| `go/README.md` | Directory documentation |
| `go/*.html` | Generated redirect pages |

## 🎨 Example: Adding 5 Products at Once

**Step 1**: Edit `redirects.csv`
```csv
slug,affiliate_link,product_name
anker67,https://amzn.to/4qhzGlu,Anker Prime 67W
logitechg305,https://amzn.to/47b37wC,Logitech G305
samsungg9,https://amzn.to/477v8VR,Samsung Odyssey G9
newkeyboard,https://amzn.to/XXXXXX,Mechanical Keyboard
newmouse,https://amzn.to/YYYYYY,Gaming Mouse
```

**Step 2**: Generate
```bash
python3 generate_redirects.py redirects.csv
```

**Step 3**: Deploy
```bash
git add go/ redirects.csv
git commit -m "Add 5 new affiliate redirects"
git push
```

**Done!** ✨

## 💡 Pro Tips

1. **Keep CSV in Git** - Track all your affiliate links in version control
2. **Re-run Anytime** - Script safely overwrites existing files
3. **Test Locally First** - Always verify redirects work before pushing
4. **Short Slugs** - Use memorable, short slugs for social media
5. **Update Links** - Just edit CSV and regenerate to update affiliate URLs

## 🔧 Common Commands

```bash
# Show usage
python3 generate_redirects.py

# Generate from CSV
python3 generate_redirects.py redirects.csv

# Generate from JSON
python3 generate_redirects.py redirects.json

# Add single redirect
./add_redirect.sh slug https://amzn.to/XXX "Name"

# Test locally
bundle exec jekyll serve

# View generated files
ls -la go/

# Check git status
git status go/
```

## 📖 Full Documentation

See `REDIRECT_GENERATOR.md` for complete documentation including:
- Troubleshooting
- Advanced usage
- Custom fields
- CI/CD integration

---

**Need Help?**  
Check `REDIRECT_GENERATOR.md` or `go/README.md`

**Quick Start**:  
`python3 generate_redirects.py redirects.csv`
