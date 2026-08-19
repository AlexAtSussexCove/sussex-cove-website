# The Sussex Cove Gardening Company · website

The website for The Sussex Cove Gardening Company (Alex, gardener, Shoreham-by-Sea / Worthing coast).

Hosted free on **GitHub Pages**, published from the `docs/` folder on `main`. **`docs/index.html` IS the
website.** There is no build step, no server and no database: edit that file, and the live site updates
within a minute or two.

---

## For Alex: changing the words on the website

You can do this yourself on GitHub, in a browser, with no software to install.

1. In this repository, click the **`docs`** folder, then click **`index.html`**.
2. Click the **pencil icon** (top right) to edit it.
3. Press **Ctrl+F** (**Cmd+F** on a Mac) and type a few words of the text you want to change, to jump
   straight to it.
4. Change **only the words**. Everything inside angle brackets, like `<p>` or `</a>`, is machinery that
   makes the page work. Leave those alone.
5. Scroll to the bottom, click **Commit changes**, then **Commit changes** again on the box that appears.
6. Wait a minute or two and refresh the website.

**If something goes wrong, nothing is lost.** Click the **History** tab on the repository, open your
change, and click the **Revert** button. The site goes back to how it was.

Some things appear more than once in the file, so change every one or they will disagree with each other:

| To change | Search for | How many places |
|---|---|---|
| Phone number | `07356` | 4 |
| Email address | `alex@` | 3 |
| The list of towns | `Shoreham-by-Sea` | 7 |
| "Beautiful gardens by the sea" | `Beautiful gardens` | 3 |
| Your "note from Alex" paragraph | `Hello, I'm Alex` | 1 |
| A service and its description | e.g. `Lawn mowing` | 3 |

Two of those places are invisible on the page: the bit at the very top of the file that tells Google
about the business, and the text that shows when someone shares the link. That is why the counts are
higher than what you can see.

**What not to edit here:** the pictures (`mark.webp`, `mark-sm.webp`), the sharing image
(`og-image.png`), and anything in `fonts/`. Also leave the Recent work gallery
script block alone. Ask for those to be redone properly.

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

3. **Add one `CNAME` record**: Name `www`, Value `alexatsussexcove.github.io`
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
  - `mark.webp` · Alex's logo at its native 566x520, used by the hero and the About section
  - `mark-sm.webp` · the same mark at 226x208, used by the header (46px) and footer (66px). Two sizes on
    purpose: the header mark loads immediately and above the fold, so pointing it at the full-size master
    put unnecessary bytes in the critical path and measurably delayed the hero image. Keep them split.
  - `favicon.png`, `apple-touch-icon.png`, `og-image.png` (social share card), `robots.txt`, `sitemap.xml`
  - `.nojekyll` · stops GitHub trying to run Jekyll over the folder
  - `fonts/` · the woff2 files, referenced by `@font-face` rules inside `index.html`. Subsets pulled from
    Google Fonts (Cormorant Garamond 500/600 + italic, Julius Sans One, Jost 300-600 variable).
- `tools/` · optional helpers. **Nothing here is needed to run or edit the site.**
  - `make-og.py` · regenerates `docs/og-image.png`, the image shown when the link is shared.
    Run: `python3 tools/make-og.py <scratch-dir> <out.png>`.
  - `make-preview.py` · emits a single self-contained copy of the site for previewing.
    Run: `python3 tools/make-preview.py > preview.html`.
- `artwork/` · Alex's original artwork exactly as supplied. Masters: never edit these, derive from them.
  - `logo-mark-master.psd` · **current logo** (was `NewLogoOnly14082026.psd`), 566x520, 16-bit CMYK with
    a real alpha channel. Everything on the site derives from this.
  - `logo-badge-master.jpg`, `medallion-master.png` · the previous artwork, superseded 2026-08-17.

## The logo artwork

`artwork/logo-mark-master.psd` arrives already cut out, with genuine transparency, so **nothing about it
is altered** for the web. The only operations applied are:

1. A colour-managed conversion from 16-bit CMYK to sRGB (`sips --matchTo` the sRGB profile). Unavoidable:
   the web is RGB. PIL cannot read 16-bit CMYK PSDs, hence `sips`.
2. Proportional downscaling (Lanczos) to the two sizes above, then WebP at quality 92.

No cropping, no masking, no recolouring, no background added. If the artwork is ever replaced, repeat
exactly those two steps.

Two things worth knowing:

- **It is not square.** 566x520, because the leaf sprig overhangs the circle at the lower left. Every CSS
  rule that sizes it therefore sets `width` with `height:auto`. Setting both would squash it.
- **566px is the whole of the resolution there is.** That caps how large it can be displayed before
  softening on a retina screen, which is why the hero is capped at 280px and the About instance at 320px.
  If Alex ever supplies a larger export, those caps can rise.

On the dark navy footer the mark's own navy outline disappears into the background, leaving the light
interior reading as a coin. A light disc was trialled behind it to restore the crisp edge and **rejected**:
at the real 66px size the disc peeked past the artwork and read as a misaligned halo. Plain is correct.

## The Instagram gallery ("Recent work")

The grid in the Recent work section feeds itself from Alex's Instagram through his **Behold** account
(behold.so, free tier: 6 posts, refreshed roughly daily). The page fetches Behold's JSON feed directly
(their endpoint is CORS-open and CDN-cached for exactly this) and draws its own grid: multi-photo posts
get faint side arrows, swipe-with-snap on touch, Instagram-style dots and a stack badge, all in the
site's own styling. Clicking a photo opens the post on Instagram. None of Behold's hosts sets cookies
(checked), so the site still needs no cookie banner. If the feed is unreachable, the section quietly
collapses to its heading and the Follow button.

**If the gallery ever goes blank:** Alex signs in at behold.so and reconnects Instagram. Behold emails
the account holder when that is needed. Nothing in this repository has to change; the `feed-id` on the
`<behold-widget>` tag only changes if Alex creates a brand-new feed in their dashboard.

This and Adobe Fonts are the site's only third-party requests.

## Design

Palette comes from the logo: ink `#31465a`, chalk `#f7f4ec`, sage `#93a48d`, sea `#c2d3d8`, plus Alex's
brand teal `#395e5c` for accents.

**Type.** Body text uses **Mendl Sans Dusk**, Alex's own licensed face, served from his Adobe Fonts kit
(`https://use.typekit.net/esq3puh.css`). Notes on that:

- The kit is loaded **without blocking first paint** (`media="print"` then swapped by `onload`, with a
  `<noscript>` fallback), and the embedded Jost stays in the stack behind it. If Adobe is slow, blocked,
  or the kit is ever deleted, the page still renders correctly in Jost rather than breaking.
- Adobe's licence does **not** permit downloading and self-hosting those font files, so unlike the other
  faces this one cannot be embedded, and it is the site's only third-party request.
- The kit contains Mendl Sans Dusk only (weights 300/400/700, no italics). **June Light**, the logo font,
  is not in it, and is not needed: the wordmark is artwork.
- If the fonts ever stop appearing, check the domain list on the Adobe Fonts web project first.

Cormorant Garamond carries the headings and the italic tagline; Julius Sans One carries the tracked caps
of the wordmark and the small labels.

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

The fonts used to be embedded in `index.html` as ~135 KB of base64, which made the published file
179 KB and effectively unreadable to edit by hand. They now sit in `docs/fonts/` and are referenced by
URL: the page dropped to 48 KB, renders pixel-for-pixel identically (verified by diffing screenshots),
paints sooner, and can be edited by a human. Do not re-embed them.

## Still open

- The Facebook button points at a share link; a canonical page URL would be better.
- An Instagram "recent work" feed was discussed but not built. It needs a professional/creator account
  (Alex has one), a one-time authorisation, and a scheduled job to pull recent posts.
- A larger export of the logo would let the hero and About instances be displayed bigger; 566px is the
  current ceiling.
- The old Azure deployment at `sussexcovegardening.com` still serves a superseded build. It is being
  retired, so it is deliberately not being kept in step.
