# SEO audit evidence log — thesussexcovegardeningcompany.co.uk
Audited 2026-08-19. Every claim here was verified directly, not taken from a tool's summary.

## Baseline: where he stands today (measured, not estimated)
- `site:thesussexcovegardeningcompany.co.uk` in Google -> "did not match any documents". The site is NOT indexed yet.
- Searching his business name: the DEAD domain sussexcovegardening.com ranks #1 with a stale snippet
  and old image. His real website does not appear at all.
- Google Business Profile: live, correct category (Gardener), correct address/phone, correct website,
  ZERO reviews.

## Verified PASSES (do not "fix" these)
- All 4 host/scheme variants collapse to one canonical URL in a single hop:
  http apex -> 301, http www -> 301, https www -> 301, all to https://thesussexcovegardeningcompany.co.uk/
- Valid Let's Encrypt cert covering apex + www. No mixed content.
- robots.txt allows all crawlers incl. AI bots. sitemap.xml valid, matches canonical exactly.
- No noindex, no X-Robots-Tag. lang="en-GB". Viewport correct.
- 12 requests total, 178KB. First-party 160KB, third-party 17.9KB (Adobe Fonts). Zero failed requests.
- Every outbound link returns 200 (WhatsApp, Facebook, Instagram, Nextdoor, Maps).
- Image alt text correct: decorative images empty alt, hero image descriptive.
- JSON-LD parses cleanly, telephone in correct E.164 format, sameAs all resolve.

## Confirmed ISSUES
1. H1 is "THE SUSSEX COVE" only. No service word, no place name. "GARDENING COMPANY" sits in a <p>.
2. Title 824px wide vs Google's ~600px cut -> truncates to "...The Sussex…", cutting the business name.
3. Meta description 261 chars, cuts mid-word at "Lanci…", losing 3 towns + "fully insured, free quotations".
4. No heading anywhere contains a town name. Service terms only appear in H3s.
5. No sentence pairs a service with a town ("hedge trimming in Worthing" appears nowhere).
6. No price indication anywhere on the page.
7. Street address 6 Kings Rd / BN15 8EA is in the JSON-LD but NEVER visible to a human.
   VERIFIED: string absent from rendered text, present in markup.
8. Insurance + waste-carrier licence are claimed but carry no policy/licence number.
9. Visible prose is ~280-300 words once nav/buttons/map labels are excluded.
10. No reviews anywhere, and nothing on the site links to his Google review form.
