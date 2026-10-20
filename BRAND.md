# th1nkn3st — Thought Nest

**A nest for curious minds.**

th1nkn3st is the studio. Crownlines, The Chaos System, and TISA: The Journey Begins are individual games with their own titles, visuals and audiences. Their common thread is curiosity: think through a duel, explore a fantasy world, or discover life beyond Earth.

## Identity

Use `th1nkn3st` exactly in the reusable wordmark, pronounced Thinknest. The Thought Nest emblem has interwoven strokes holding three distinct idea forms. Approved originals and provenance are in `assets/branding/th1nkn3st/`. Keep the original imagery intact. The palette is black, warm white, aqua, tangerine and leaf green; the product pages keep their own palettes.

Use `th1nkn3st™` for the principal studio signature. There is no LLC or registered-trademark claim. The owner reports searches for th1nkn3st and Cursed System; searches for Crownlines, Project Arc/TISA and the newer The Chaos System name have not been established. A reported search must not be described as registration or legal clearance. Do not use ®.

## Portfolio

**Public reveal policy (owner, October 20, 2026):** Crownlines is the featured game and receives the complete launch page, gameplay previews, campaign/gift information, help, privacy and credits. The Chaos System and TISA receive only a brief description and **Coming soon**. No logos, artwork, expanded feature lists or detailed previews for those two games. This supersedes the earlier three-visual-card draft. Their minimal existing routes remain reachable, but the homepage does not promote deeper reveals. Artwork is kept out of publishable assets, not merely hidden with CSS.

| Public title | Existing project | Position |
|---|---|---|
| Crownlines | crownlines | Offline tactical duels; Android coming soon |
| The Chaos System | cursed_system | One-sentence teaser; coming soon |
| TISA: The Journey Begins | project-arc | One-sentence teaser; coming soon |

Use the studio emblem as an endorsement, not as a replacement for a game's product icon. Do not force all games into a shared universe. Speak in a studio voice without personal names, family details, locations or employer information. Use clear descriptions of play, real status labels, and available links. Label concept and promotional artwork; never present it as a gameplay screenshot. No invented release dates, testimonials or store availability.

## Site ownership

This is the GitHub Pages/Jekyll site in `D:/devapps/th1nkn3st/site-crownlines`, branch `app-pages`, remote `th1nkn3st/site`. The sibling `site` checkout has an older tech-content branch; it is not the source of these changes. The existing app data model and Crownlines privacy/support routes remain in place. Preserve historical posts and their URLs when promoting the new portfolio.

For a new game, add an entry in `_data/apps/`, then a project page with `layout: project`. Set `url` to its permalink. Featured entries appear on the home page; a utility can remain in the registry with `featured: false`. Use the existing `new_app.py` flow for released products that need dedicated privacy/support pages. Do not publish guessed privacy policies for unreleased games.

The native GitHub Pages build workflow is the release check. It runs `new_app.py --check _site` and `tools/check_site.py _site` to validate eight essential routes, local assets, anchors and the teaser artwork restriction. Local LiquidJS rendering in ignored `internal-docs/brand-preview/` writes to ignored `tmp/launch-preview/`; it is a visual preview, not a replacement Jekyll compiler. No automatic deployment, commit or push is part of this brand pass.
