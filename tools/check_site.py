"""Check the generated launch pages and prevent accidental teaser artwork release.

Run after the native Jekyll build: python tools/check_site.py _site
Use --baseurl /repository for a GitHub Pages project-path build.
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.references = []
        self.images = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        for attr in ("href", "src"):
            if attr in values:
                self.references.append(values[attr])
        if tag == "img":
            self.images.append(values.get("src", ""))


def check(root, baseurl):
    routes = ("/", "/contact/", "/crownlines/", "/crownlines/privacy/",
              "/crownlines/support/", "/crownlines/licenses/",
              "/games/the-chaos-system/", "/games/project-arc/")
    failures = []
    parsed = {}

    def file_for(url):
        if baseurl and (url == baseurl or url.startswith(baseurl + "/")):
            url = url[len(baseurl):] or "/"
        value = url.lstrip("/")
        candidate = root / value
        return candidate / "index.html" if candidate.is_dir() else candidate

    for route in routes:
        file = file_for(baseurl + route)
        if not file.is_file():
            failures.append(f"Missing required page: {baseurl}{route}")
            continue
        text = file.read_text(encoding="utf-8")
        if "{{" in text or "{%" in text or "data-app-error" in text:
            failures.append(f"Unrendered template or missing app data: {route}")
        parsed[baseurl + route] = Page(text)

    for route, page in parsed.items():
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            target_path = unquote(url.path) if url.path else route
            if not target_path.startswith("/"):
                failures.append(f"Use a baseurl-aware absolute path: {route} -> {reference}")
                continue
            target = file_for(target_path)
            if not target.is_file():
                failures.append(f"Broken link or asset: {route} -> {reference}")
            elif url.fragment and target.suffix == ".html":
                target_page = parsed.get(target_path) or Page(target.read_text(encoding="utf-8"))
                if unquote(url.fragment) not in target_page.ids:
                    failures.append(f"Missing anchor: {route} -> {reference}")

    for route in ("/games/the-chaos-system/", "/games/project-arc/"):
        page = parsed.get(baseurl + route)
        if page and any("/assets/branding/th1nkn3st/" not in image for image in page.images):
            failures.append(f"Teaser exposes non-studio artwork: {route}")

    for file in root.rglob("*"):
        if not file.is_file():
            continue
        relative = file.relative_to(root)
        if any(part in ("internal-docs", "tmp", "node_modules", ".git") for part in relative.parts) or file.suffix in (".py", ".ps1") or file.name.startswith(".env"):
            failures.append(f"Private or development file in published output: {relative}")
        if any(part in ("go", "gear", "_gear", "_posts") for part in relative.parts):
            failures.append(f"Retired affiliate or blog content in published output: {relative}")
        if "the-chaos-system" in file.parts and file.suffix.lower() in (".png", ".jpg", ".webp", ".svg"):
            failures.append(f"Unreleased game artwork in published output: {file.relative_to(root)}")
        if file.suffix == ".html" and "/assets/images/the-chaos-system/" in file.read_text(encoding="utf-8", errors="ignore"):
            failures.append(f"Unreleased artwork reference: {file.relative_to(root)}")

    if failures:
        raise SystemExit("Launch site checks failed:\n" + "\n".join(failures))
    print(f"PASS: {len(routes)} launch pages, internal links/anchors/assets and teaser artwork restrictions.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    check(args.site.resolve(), args.baseurl.rstrip("/"))
