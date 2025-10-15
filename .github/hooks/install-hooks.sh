#!/bin/bash
# Install Git hooks for security

echo "🔧 Installing security hooks..."

# Check if .git directory exists
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository"
    exit 1
fi

# Copy pre-commit hook
if [ -f ".github/hooks/pre-commit.sh" ]; then
    cp .github/hooks/pre-commit.sh .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "✅ Pre-commit hook installed"
else
    echo "❌ Error: .github/hooks/pre-commit.sh not found"
    exit 1
fi

echo ""
echo "🎉 Security hooks installed successfully!"
echo ""
echo "The pre-commit hook will check for:"
echo "  - API keys and secrets"
echo "  - .env files"
echo "  - Large files (>5MB)"
echo ""
echo "To bypass the hook (not recommended):"
echo "  git commit --no-verify"
