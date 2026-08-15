# The Sussex Cove Gardening Company · website

The website for The Sussex Cove Gardening Company (Alex, gardener, Shoreham-by-Sea / Worthing coast).

Hosted free on **GitHub Pages**, published from the `docs/` folder on `main`. There is no server, no
database and no build pipeline to babysit: pushing to `main` publishes within a minute or two.

---

## For Alex: pointing your domain at the site

Your site is published at the GitHub Pages address shown in **Settings → Pages** of this repository.
To make `thesussexcovegardeningcompany.co.uk` show it instead, sign in to **GoDaddy** and edit the DNS
for that domain (My Products → Domains → the domain → DNS).

**Your email is not affected by any of this.** Leave every `MX`, `TXT` and `autodiscover` record exactly
as it is. Only the records below change.

1. **Delete** the existing `A` records for `@` (they currently point at GoDaddy's parking page).
2. **Add four new `A` records**, all with Name `@`:

   | Type | Name | Value |
   |------|------|-------|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |

3. **Add one `CNAME` record**: Name `www`, Value `<your-github-username>.github.io`
4. In this repository on GitHub: **Settings → Pages → Custom domain**, enter
   `thesussexcovegardeningcompany.co.uk` and save. Once it verifies, tick **Enforce HTTPS**.

DNS can take up to an hour. GitHub then issues a free SSL certificate automatically.

Afterwards, two five-minute jobs worth doing:

- Update the website field on your **Google Business Profile** to the domain.
- Keep asking happy customers for Google reviews. That does more for being found than the website does.

---

## Structure

- `docs/` · **the published site**. Everything in here is what visitors get.
  - `index.html` (built; fonts embedded as data URIs, so there are no font requests)
  - `logo.webp` · the round badge with the ring lettering, 768px, used only by the large About instance
  - `logo-sm.webp` · the same badge at 192px, used by the header (46px) and footer (64px). Two sizes on
    purpose: the header mark loads immediately and above the fold, so pointing it at the 768px master put
    82 KB in the critical path to paint a 46px icon and cost ~250 ms of load time, measured. Keep them split.
  - `medallion.webp` · the round scene with no lettering (the hero image, and the largest paint element)
  - `favicon.png`, `apple-touch-icon.png`, `og-image.png` (social share card), `robots.txt`, `sitemap.xml`
  - `.nojekyll` · stops GitHub trying to run Jekyll over the folder
- `src/page.html` · **the file to edit**. The same page, but with a `/*__FONTS__*/` placeholder instead of
  ~135 KB of base64, and `__LOGO_SM_SRC__` / `__LOGO_SRC__` / `__MEDALLION_SRC__` placeholders for the
  images (mapped in `build.py`'s `IMAGES` list).
- `src/build.py` · assembles the page. Run from `src/`:

```bash
cd src && python3 build.py index > ../docs/index.html
```

  `build.py artifact` emits a body-only variant with the images inlined, for single-file previews.
- `src/make-og.py` · regenerates `docs/og-image.png` (the social share card) from the badge and the brand
  fonts. Run: `python3 make-og.py <scratch-dir> <out.png>`.
- `src/fonts/` · woff2 subsets plus the generated `fonts.css` (Cormorant Garamond, Julius Sans One, Jost).
- `artwork/` · Alex's original artwork as supplied (`logo-badge-master.jpg` was "Logo Image 2",
  `medallion-master.png` was "Center main"). Masters: do not edit, cut from these.

## The logo artwork

Both originals are square with opaque backgrounds. Each was cut to its circle so it sits on any section
background (the footer is dark navy, so a square white image would have shown as a box):

- **`logo-badge-master.jpg` → `logo.webp` / `logo-sm.webp`**: the badge's outer ring touches all four
  frame edges, so an exact circular alpha mask (supersampled 4x for a smooth edge) was enough.
- **`medallion-master.png` → `medallion.webp`**: the leaves overhang the circle, so a hard circular crop
  would have sliced them off. Instead: crop off a 6px grey screenshot band at the bottom, least-squares
  fit the circle from its clean top arc, then keep everything inside the circle opaque and matte the
  outside by colour distance from the cream background (#FCF8F5). That keeps the overhanging leaves with
  clean antialiased edges.

Both are WebP: the badge is 82 KB as WebP versus 581 KB as PNG. WebP works in every browser since Safari
14 (2020), and the page already needs a 2020+ browser for `clamp()` and `backdrop-filter`.

## Design

Palette and type come from the logo: ink `#31465a`, chalk `#f7f4ec`, sage `#93a48d`, sea `#c2d3d8`, plus
Alex's brand teal `#395e5c` for accents. Julius Sans One matches the tracked caps on his business card;
Cormorant Garamond and Jost carry headings and body text.

The hero is the medallion over an illustrated coastal wash (sky, a soft-gradient horizon, foreshore,
framing leaves, drifting gulls). It originally also had hand-drawn chalk cliffs and a pier; those were
removed when the real artwork went in, because the medallion depicts cliffs and a pier itself and the
background was duplicating its subject.

Includes: LocalBusiness structured data (address, areas served, services, socials, Google listing),
Open Graph and Twitter cards, reduced-motion support, a mobile menu, scroll reveals and gentle parallax.

## Local preview

```bash
python3 -m http.server 4180 --directory docs
```

Then open <http://localhost:4180>.

## Still open

- The Facebook button points at a share link; a canonical page URL would be better.
- An Instagram "recent work" feed was discussed but not built. It needs a professional/creator account
  (Alex has one), a one-time authorisation, and a scheduled job to pull recent posts.
- Alex's own fonts (June Light for the logo, Mendl Sans for text) are not used: a desktop font purchase
  does not normally include a web-embedding licence, so that needs checking before they can go in. The
  current faces were chosen to match closely.
