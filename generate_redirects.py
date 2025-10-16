#!/usr/bin/env python3
"""
Th1nkN3st Redirect Page Generator
Automatically creates /go/ redirect HTML files for affiliate links.

Usage:
    python generate_redirects.py redirects.csv
    python generate_redirects.py redirects.json
"""

import sys
import json
import csv
from pathlib import Path
from typing import List, Dict

# Template for redirect HTML
REDIRECT_TEMPLATE = """---
layout: default
title: "Redirecting to {product_name}..."
permalink: /go/{slug}/
---

<meta http-equiv="refresh" content="0; url={affiliate_link}">
<link rel="canonical" href="https://www.th1nkn3st.com/go/{slug}/" />

<section style="text-align:center;margin:80px auto;max-width:600px;">
  <p>Redirecting you to Amazon...</p>
  <p style="font-size:0.9rem;color:#888;">As an Amazon Associate, Th1nkN3st earns from qualifying purchases.</p>
  <p>If you're not redirected automatically, <a href="{affiliate_link}">click here</a>.</p>
</section>
"""


def read_csv(file_path: Path) -> List[Dict[str, str]]:
    """Read redirects from CSV file."""
    redirects = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip empty rows or rows without required fields
            if row.get('slug') and row.get('affiliate_link'):
                redirects.append({
                    'slug': row['slug'].strip(),
                    'affiliate_link': row['affiliate_link'].strip(),
                    'product_name': row.get('product_name', row['slug']).strip()
                })
    return redirects


def read_json(file_path: Path) -> List[Dict[str, str]]:
    """Read redirects from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle both array format and object with redirects key
    if isinstance(data, list):
        redirects = data
    elif isinstance(data, dict) and 'redirects' in data:
        redirects = data['redirects']
    else:
        raise ValueError("JSON must be an array or have a 'redirects' key")
    
    # Validate required fields
    validated = []
    for item in redirects:
        if item.get('slug') and item.get('affiliate_link'):
            validated.append({
                'slug': item['slug'].strip(),
                'affiliate_link': item['affiliate_link'].strip(),
                'product_name': item.get('product_name', item['slug']).strip()
            })
    
    return validated


def generate_redirect_file(redirect: Dict[str, str], output_dir: Path) -> Path:
    """Generate a single redirect HTML file."""
    slug = redirect['slug']
    file_path = output_dir / f"{slug}.html"
    
    # Generate HTML content
    content = REDIRECT_TEMPLATE.format(
        slug=slug,
        affiliate_link=redirect['affiliate_link'],
        product_name=redirect['product_name']
    )
    
    # Write file
    file_path.write_text(content, encoding='utf-8')
    return file_path


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python generate_redirects.py <redirects.csv|redirects.json>")
        print("\nCSV format: slug,affiliate_link,product_name")
        print("JSON format: [{\"slug\": \"...\", \"affiliate_link\": \"...\", \"product_name\": \"...\"}]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    # Determine file type and read data
    if input_file.suffix.lower() == '.csv':
        print(f"Reading CSV file: {input_file}")
        redirects = read_csv(input_file)
    elif input_file.suffix.lower() == '.json':
        print(f"Reading JSON file: {input_file}")
        redirects = read_json(input_file)
    else:
        print(f"Error: Unsupported file type: {input_file.suffix}")
        print("Supported types: .csv, .json")
        sys.exit(1)
    
    if not redirects:
        print("Error: No valid redirects found in file")
        sys.exit(1)
    
    # Create go/ directory if it doesn't exist
    go_dir = Path(__file__).parent / 'go'
    go_dir.mkdir(exist_ok=True)
    
    # Generate redirect files
    print(f"\nGenerating {len(redirects)} redirect file(s)...\n")
    
    created_files = []
    for redirect in redirects:
        file_path = generate_redirect_file(redirect, go_dir)
        created_files.append(file_path)
        print(f"  ✓ Created: go/{redirect['slug']}.html → {redirect['affiliate_link']}")
    
    print(f"\n✅ Successfully generated {len(created_files)} redirect file(s)")
    print(f"\nNext steps:")
    print(f"  1. Test locally: http://localhost:4000/go/<slug>/")
    print(f"  2. Commit: git add go/ && git commit -m 'Add affiliate redirects'")
    print(f"  3. Push: git push")
    print(f"  4. Test live: https://www.th1nkn3st.com/go/<slug>/")


if __name__ == '__main__':
    main()
