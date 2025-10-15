#!/bin/bash
# Pre-commit hook to prevent committing secrets
# To install: cp .github/hooks/pre-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

echo "🔍 Running security checks..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check for common secret patterns
SECRETS_FOUND=0

echo "Checking for API keys and secrets..."

# Patterns to check
PATTERNS=(
    "api[_-]?key.*['\"][a-zA-Z0-9]{20,}['\"]"
    "secret.*['\"][a-zA-Z0-9]{20,}['\"]"
    "password.*['\"][^'\"]{8,}['\"]"
    "aws_access_key_id"
    "aws_secret_access_key"
    "private[_-]?key"
    "-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----"
    "AKIA[0-9A-Z]{16}"
    "ghp_[a-zA-Z0-9]{36}"
    "gho_[a-zA-Z0-9]{36}"
)

# Get list of staged files (excluding this hook itself)
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -v "pre-commit.sh")

for pattern in "${PATTERNS[@]}"; do
    for file in $STAGED_FILES; do
        if [ -f "$file" ]; then
            matches=$(grep -iE "$pattern" "$file" 2>/dev/null)
            if [ $? -eq 0 ]; then
                echo -e "${RED}⚠️  Potential secret found in $file${NC}"
                echo -e "${YELLOW}Pattern: $pattern${NC}"
                echo "$matches"
                SECRETS_FOUND=1
            fi
        fi
    done
done

# Check for large files
echo "Checking for large files (>5MB)..."
LARGE_FILES=$(git diff --cached --name-only --diff-filter=ACM | xargs -I {} find {} -type f -size +5M 2>/dev/null)
if [ ! -z "$LARGE_FILES" ]; then
    echo -e "${YELLOW}⚠️  Large files detected:${NC}"
    echo "$LARGE_FILES"
    echo -e "${YELLOW}Consider using Git LFS for large files${NC}"
fi

# Check for .env files
echo "Checking for .env files..."
ENV_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E "\.env$|\.env\.")
if [ ! -z "$ENV_FILES" ]; then
    echo -e "${RED}⚠️  .env file detected:${NC}"
    echo "$ENV_FILES"
    echo -e "${RED}These files should never be committed!${NC}"
    SECRETS_FOUND=1
fi

# Final result
if [ $SECRETS_FOUND -eq 1 ]; then
    echo -e "${RED}❌ Commit blocked! Potential secrets detected.${NC}"
    echo -e "${YELLOW}If these are false positives, you can:${NC}"
    echo -e "${YELLOW}1. Remove the secrets and commit again${NC}"
    echo -e "${YELLOW}2. Use 'git commit --no-verify' to bypass (NOT RECOMMENDED)${NC}"
    exit 1
else
    echo -e "${GREEN}✅ No secrets detected. Commit proceeding...${NC}"
    exit 0
fi
