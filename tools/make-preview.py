#!/usr/bin/env python3
"""Emit a single self-contained copy of the site, for Claude Artifacts previews.

  python3 tools/make-preview.py > preview.html

The published site is docs/index.html and needs no build step; this only exists
because an Artifact must be one file, so the images are inlined as data URIs and
the html/head/body shell is stripped (the artifact runtime supplies its own).
"""
import base64, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
docs = root / 'docs'
page = (docs / 'index.html').read_text()

for name in ('mark-sm.webp', 'mark.webp'):
    uri = 'data:image/webp;base64,' + base64.b64encode((docs / name).read_bytes()).decode()
    page = page.replace(f'src="{name}"', f'src="{uri}"')

for face in (docs / 'fonts').glob('*.woff2'):
    uri = 'data:font/woff2;base64,' + base64.b64encode(face.read_bytes()).decode()
    page = page.replace(f'url(fonts/{face.name})', f'url({uri})')

title = re.search(r'<title>(.*?)</title>', page, re.S).group(1)
styles = re.findall(r'<style>(.*?)</style>', page, re.S)
body = re.search(r'<body>(.*)</body>', page, re.S).group(1)
out = f'<title>{title}</title>\n' + ''.join(f'<style>{s}</style>\n' for s in styles) + body
sys.stdout.write(out)
