#!/bin/bash
# Quick helper script to add a single redirect
# Usage: ./add_redirect.sh slug affiliate_link "Product Name"

if [ $# -lt 2 ]; then
    echo "Usage: ./add_redirect.sh <slug> <affiliate_link> [product_name]"
    echo ""
    echo "Example:"
    echo "  ./add_redirect.sh anker67 https://amzn.to/4qhzGlu 'Anker Prime 67W'"
    echo ""
    echo "Or use the bulk generator:"
    echo "  python3 generate_redirects.py redirects.csv"
    exit 1
fi

SLUG="$1"
LINK="$2"
NAME="${3:-$SLUG}"

# Add to CSV (append if exists, create if not)
if [ ! -f redirects.csv ]; then
    echo "slug,affiliate_link,product_name" > redirects.csv
fi

# Check if slug already exists
if grep -q "^${SLUG}," redirects.csv; then
    echo "⚠️  Slug '$SLUG' already exists in redirects.csv"
    echo "   Edit the file manually or delete the line to replace it"
    exit 1
fi

# Append new redirect
echo "${SLUG},${LINK},${NAME}" >> redirects.csv

echo "✅ Added to redirects.csv:"
echo "   Slug: ${SLUG}"
echo "   Link: ${LINK}"
echo "   Name: ${NAME}"
echo ""
echo "Next steps:"
echo "  1. Generate: python3 generate_redirects.py redirects.csv"
echo "  2. Test: http://localhost:4000/go/${SLUG}/"
echo "  3. Deploy: git add go/ redirects.csv && git commit && git push"
