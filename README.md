# th1nkn3st

**A nest for curious minds.**

Source for [www.th1nkn3st.com](https://www.th1nkn3st.com), the th1nkn3st studio and game showcase. Built with Jekyll and hosted on GitHub Pages.

## Public pages

| Route | Purpose |
|---|---|
| `/` | Studio introduction, featured Crownlines game, text-only upcoming projects |
| `/crownlines/` | Gameplay previews, features, first campaign and gift, FAQ |
| `/crownlines/privacy/` | Crownlines privacy policy |
| `/crownlines/support/` | FAQ and contact |
| `/crownlines/licenses/` | Software, font and music credits |
| `/contact/` | Studio enquiries and game support |
| `/print-profit/` | Android calculator for 3D-print sellers, Free/Pro offer and testing contact |
| `/print-profit/privacy/`, `/print-profit/support/`, `/print-profit/terms/` | App policy, support and purchase/estimate terms |

The Chaos System and TISA have brief, text-only coming-soon pages. Their logos and detailed previews are not public.

## Develop and check

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`. Before publication:

```sh
bundle exec jekyll build
python new_app.py --check _site
python tools/check_site.py _site
```

The pull-request build performs the native GitHub Pages build and both checks. The launch checker validates required pages, links, assets, anchors, and the restriction on unreleased-game artwork.

## Content and deployment

Game information lives in `_data/apps/`. Crownlines has its own launch layout; shared templates render support and privacy pages. Only change availability to `Available` or `Beta` when the relevant store or testing link is actually ready.

GitHub Pages publishes `main` at the custom domain in `CNAME`. Use a pull request, pass the checks, then merge. The site provides project information and support; it has no checkout, user accounts, or paid hosted service. Purchases, if introduced, belong on the external storefront.

Private notes, local previews and retired material belong outside version control. Nothing under `internal-docs/`, `tmp/`, `.env*`, or local credential files may be committed. Historical tech/affiliate content is retired from the current site; this cleanup does not rewrite old Git history.

## Rights and contact

Site content and studio artwork are proprietary; see [LICENSE](LICENSE). Third-party font notices and asset provenance are listed in [NOTICE.md](NOTICE.md). Public source visibility does not grant permission to reuse studio or game branding.

Studio and support: **hello@th1nkn3st.com**. Security reports: [SECURITY.md](SECURITY.md). Public brand guidance: [BRAND.md](BRAND.md).
