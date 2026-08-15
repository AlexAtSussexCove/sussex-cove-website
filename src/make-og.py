#!/usr/bin/env python3
"""Rebuild the 1200x630 social share card from Alex's real badge + the brand fonts.

  python3 make-og.py <workdir> <out.png>

Text is rendered through qlmanage (it honours woff2 fonts embedded as data URIs);
the badge is composited afterwards with PIL. qlmanage always renders a square
thumbnail, so the card is laid out on a 1200x1200 canvas and centre-cropped to 630.
"""
import base64, pathlib, subprocess, sys
from PIL import Image

src = pathlib.Path(__file__).parent
work = pathlib.Path(sys.argv[1]); work.mkdir(parents=True, exist_ok=True)
out = pathlib.Path(sys.argv[2])

def font(name):
    return base64.b64encode((src / 'fonts' / name).read_bytes()).decode()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 1200 1200">
<defs><style>
@font-face{{font-family:'Julius Sans One';src:url(data:font/woff2;base64,{font('JuliusSansOne-normal-400.woff2')}) format('woff2')}}
@font-face{{font-family:'Cormorant Garamond';font-style:italic;src:url(data:font/woff2;base64,{font('CormorantGaramond-italic-500.woff2')}) format('woff2')}}
@font-face{{font-family:'Jost';src:url(data:font/woff2;base64,{font('Jost-normal-300_600.woff2')}) format('woff2')}}
</style></defs>
<rect width="1200" height="1200" fill="#f7f4ec"/>
<g transform="translate(0,285)">
  <text x="560" y="255" font-family="Julius Sans One" font-size="46" letter-spacing="11" fill="#243748">THE SUSSEX COVE</text>
  <line x1="565" y1="292" x2="1090" y2="292" stroke="#31465a" stroke-opacity=".4" stroke-width="1.5"/>
  <text x="560" y="338" font-family="Julius Sans One" font-size="26" letter-spacing="12" fill="#5a6d7f">GARDENING COMPANY</text>
  <text x="560" y="415" font-family="Cormorant Garamond" font-style="italic" font-size="44" fill="#395e5c">Beautiful gardens by the sea</text>
  <text x="560" y="472" font-family="Jost" font-size="20" fill="#5a6d7f">Shoreham-by-Sea · Lancing · Steyning · Worthing · Findon · Ferring</text>
  <text x="560" y="530" font-family="Julius Sans One" font-size="30" letter-spacing="6" fill="#243748">07356 275 577</text>
</g></svg>'''

svg_path = work / 'og-text.svg'
svg_path.write_text(svg)
png_path = work / 'og-text.svg.png'
png_path.unlink(missing_ok=True)
subprocess.run(['qlmanage', '-t', '-s', '1200', '-o', str(work), str(svg_path)],
               check=True, capture_output=True)

card = Image.open(png_path).convert('RGBA')
card = card.crop((0, (card.height - 630) // 2, 1200, (card.height - 630) // 2 + 630))

badge = Image.open(src.parent / 'docs' / 'logo.webp').convert('RGBA').resize((450, 450), Image.LANCZOS)
card.alpha_composite(badge, (66, (630 - 450) // 2))
card.convert('RGB').save(out, optimize=True)
print(f"wrote {out} {out.stat().st_size/1024:.1f} KB")
