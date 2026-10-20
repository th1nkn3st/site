#!/usr/bin/env python3
"""Add a new app to the site, or check that every app's pages were built.

    python new_app.py SLUG "App Name"               Create the data file and the
                                                    /SLUG/, privacy, and support pages.
    python new_app.py SLUG "App Name" --card-only   Homepage card only; add pages later
                                                    by running again without --card-only.
    python new_app.py --check _site                 After `jekyll build`, confirm every
                                                    app's pages were built.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "_app_template"
DATA_DIR = ROOT / "_data" / "apps"
PAGES = (("", "index.md"), ("privacy/", "privacy.md"), ("support/", "support.md"))
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fill(template_name, slug, name):
    text = (TEMPLATE_DIR / template_name).read_text(encoding="utf-8")
    return text.replace("APP NAME", name).replace("SLUG", slug)


def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"  created {path.relative_to(ROOT).as_posix()}")


def create(slug, name, card_only):
    if not SLUG_PATTERN.match(slug):
        sys.exit(f"Slug must be lowercase letters, digits, and hyphens, e.g. my-app. Got: {slug}")

    data_file = DATA_DIR / f"{slug}.yml"
    page_dir = ROOT / slug
    if page_dir.exists() or (card_only and data_file.exists()):
        sys.exit(f"{slug} already exists. Pick another slug.")

    if data_file.exists():
        print(f"  kept existing {data_file.relative_to(ROOT).as_posix()}")
    else:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        write(data_file, fill("app.yml", slug, name))

    if not card_only:
        page_dir.mkdir()
        for _, stub in PAGES:
            write(page_dir / stub, fill(stub, slug, name))
        (ROOT / "assets" / "images" / slug).mkdir(parents=True, exist_ok=True)

    print(f"\nNext: fill in _data/apps/{slug}.yml (status, summary, stores, privacy, theme).")
    if card_only:
        print(f"{name} will appear as a homepage card with no pages.")
    else:
        print(f"Put images in assets/images/{slug}/. Once merged, these pages go live:")
        for sub, _ in PAGES:
            print(f"  https://www.th1nkn3st.com/{slug}/{sub}")


def check(site_dir):
    if not site_dir.is_dir():
        sys.exit(f"{site_dir} not found. Run `jekyll build` first.")

    problems = []
    for data_file in sorted(DATA_DIR.glob("*.yml")):
        slug = data_file.stem
        if not (ROOT / slug).is_dir():
            continue
        for sub, stub in PAGES:
            if not (site_dir / slug / sub / "index.html").is_file():
                problems.append(f"/{slug}/{sub} was not built. Is {slug}/{stub} missing?")

    for page in site_dir.rglob("*.html"):
        if "data-app-error" in page.read_text(encoding="utf-8", errors="ignore"):
            problems.append(f"{page.relative_to(site_dir).as_posix()} names an app with no file in _data/apps/.")

    if problems:
        print("App page problems:\n  " + "\n  ".join(problems))
        sys.exit(1)
    print("All app pages built.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", nargs="?", help="URL name for the app, e.g. my-app")
    parser.add_argument("name", nargs="?", help='display name, e.g. "My App"')
    parser.add_argument("--card-only", action="store_true", help="create only the homepage card")
    parser.add_argument("--check", metavar="SITE_DIR", type=Path, help="check a built site instead")
    args = parser.parse_args()

    if args.check:
        check(args.check)
    elif args.slug and args.name:
        create(args.slug, args.name, args.card_only)
    else:
        parser.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
