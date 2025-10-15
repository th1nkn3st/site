# Maintainer Guide

**For Th1nkN3st Site Maintainers**

This is a quick reference for maintaining the Th1nkN3st site. For detailed documentation, see the `internal-docs/` directory.

## 📁 Internal Documentation

All sensitive documentation is kept in the `internal-docs/` directory, which is **gitignored** and never committed to the public repository.

### Quick Links

- **[INDEX.md](internal-docs/INDEX.md)** - Full documentation index
- **[SECURITY_CHECKLIST.md](internal-docs/SECURITY_CHECKLIST.md)** - Complete security procedures
- **[SECURITY_QUICKSTART.md](internal-docs/SECURITY_QUICKSTART.md)** - Quick commands reference
- **[SECURITY_FIXES_COMPLETE.md](internal-docs/SECURITY_FIXES_COMPLETE.md)** - Implementation report
- **[CSP_CONFIG.md](internal-docs/CSP_CONFIG.md)** - Content Security Policy config
- **[REPO_STATUS.md](internal-docs/REPO_STATUS.md)** - Public vs private files

## 🚀 Quick Start

### Daily Development
```bash
# Start local server
bundle exec jekyll serve

# Open browser to http://localhost:4000
```

### Before Committing
```bash
# Check what will be committed (internal-docs should NOT appear)
git status

# Verify internal-docs is ignored
git check-ignore -v internal-docs/

# Stage public files only
git add <files>
git commit -m "your message"
```

### Security Maintenance
```bash
# Weekly security check
bundle audit check --update

# Check for outdated dependencies
bundle outdated

# Update dependencies
bundle update
```

## 🔒 Important Reminders

### ✅ Safe to Commit (Public)
- `README.md` - Public project overview
- `SECURITY.md` - Vulnerability disclosure
- Jekyll content and configs
- GitHub Actions workflows
- Site content and assets

### ❌ Never Commit (Private)
- `internal-docs/` directory - **GITIGNORED**
- Any files with API keys or tokens
- `.env` files
- Personal or sensitive information

## 📝 Common Tasks

### Adding a Blog Post
1. Create file: `_posts/YYYY-MM-DD-title.md`
2. Add front matter (see README.md)
3. Write content
4. Test locally: `bundle exec jekyll serve`
5. Commit and push

### Updating Security Docs
1. Edit files in `internal-docs/`
2. These stay local (never committed)
3. Keep documentation current
4. Update INDEX.md if adding new docs

### Deployment
1. Push to `main` branch
2. GitHub Pages auto-deploys
3. Changes live in 2-5 minutes
4. Check https://www.th1nkn3st.com

## 🆘 Need Help?

1. Check `internal-docs/INDEX.md` for full documentation
2. Review `internal-docs/SECURITY_QUICKSTART.md` for common commands
3. See public `README.md` for general development info

## 📞 Contacts

- **Email**: devsecopstips@gmail.com
- **GitHub**: th1nkn3st/site

---

**Note:** This file is safe to commit. It only references the internal-docs directory without exposing sensitive information.
