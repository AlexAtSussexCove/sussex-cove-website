#!/usr/bin/env python3
"""Assemble the site. Run from src/.

  python3 build.py index    > ../docs/index.html    (deployable page, images referenced by path)
  python3 build.py artifact > <path>/preview.html   (body-only, images inlined, for Claude Artifacts)

Fonts come from fonts/fonts.css; images come from ../docs/ (see README for how they were cut).
"""
import re, sys, base64, pathlib

src = pathlib.Path(__file__).parent
docs = src.parent / 'docs'

page = (src / 'page.html').read_text()
page = page.replace('/*__FONTS__*/', (src / 'fonts' / 'fonts.css').read_text())

mode = sys.argv[1] if len(sys.argv) > 1 else 'index'

# placeholder -> file in docs/. The nav and footer use the small mark so the full-size
# master never enters the critical path just to paint a 46px icon.
IMAGES = [
    ('__MARK_SM_SRC__', 'mark-sm.webp'),
    ('__MARK_SRC__', 'mark.webp'),
]

if mode == 'index':
    for token, name in IMAGES:
        page = page.replace(token, name)
    sys.stdout.write(page)
else:
    # Artifacts are a single self-contained file: inline the images, and emit
    # title + styles + body only (the artifact runtime supplies the html/head/body shell).
    def data_uri(name):
        return "data:image/webp;base64," + base64.b64encode((docs / name).read_bytes()).decode()
    for token, name in IMAGES:
        page = page.replace(token, data_uri(name))

    title = re.search(r'<title>(.*?)</title>', page, re.S).group(1)
    styles = re.findall(r'<style>(.*?)</style>', page, re.S)
    body = re.search(r'<body>(.*)</body>', page, re.S).group(1)
    out = f"<title>{title}</title>\n"
    for s in styles:
        out += f"<style>{s}</style>\n"
    sys.stdout.write(out + body)
