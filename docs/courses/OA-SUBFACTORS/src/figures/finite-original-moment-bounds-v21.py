from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html
import math

ROOT = Path(__file__).resolve().parent
W, H = 1560, 1110
bg, ink, blue, pale, green, amber = '#fafbf9', '#172e35', '#245c74', '#e8f0f3', '#e9f0e5', '#f5ead3'
im = Image.new('RGB', (W, H), bg)
d = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="{bg}"/>']

def txt(x, y, value, size=28, bold=False, color=ink):
    font = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf', size)
    d.text((x, y), value, font=font, fill=color)
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{html.escape(value)}</text>')

def box(x, y, width, height, lines, fill=pale, size=28):
    d.rounded_rectangle((x,y,x+width,y+height), radius=18, fill=fill, outline=blue, width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="18" fill="{fill}" stroke="{blue}" stroke-width="2"/>')
    for i, value in enumerate(lines):
        txt(x+25, y+22+44*i, value, size, i==0)

def arrow(x1,y1,x2,y2):
    d.line((x1,y1,x2,y2), fill=blue, width=4)
    a = math.atan2(y2-y1,x2-x1)
    pts=[(x2,y2),(x2-17*math.cos(a-.5),y2-17*math.sin(a-.5)),(x2-17*math.cos(a+.5),y2-17*math.sin(a+.5))]
    d.polygon(pts, fill=blue)
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{blue}" stroke-width="4"/>')
    svg.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="{blue}"/>')

txt(60, 30, 'All five original likelihoods: finite averages and cost bounds', 36, True)
txt(60, 88, 'Fixed λ = 1 + δ,  δ = 2⁻³¹ 25⁻¹⁹⁸¹⁵³;   qi = Ri⁻¹;   Q = Σi qi', 27)
box(60, 155, 1440, 168, [
    'Actual pointwise dimension and tangent identities — FM21.3–FM21.4',
    'Σi βi⁻¹(qi) = d;     H = Q − d + K(w1 − R1) ≥ 0',
    'H = Σi (Ri − wi)² / (wi² Ri);    C = Σi |qi − wi⁻¹|',
], green)
box(60, 405, 682, 205, [
    'Original full-H average AL — every seed',
    'Actual WM.16 sets retain central parity.',
    '‖AL(Q) − d‖ ≤ 4(d − 1)/(2L + 1).',
    'No normality assumption on the seed.',
], size=27)
box(818, 405, 682, 205, [
    'Parity-balanced finite average — FM21.10',
    'Abar_L = ½ A_L(id + β1);',
    'Abar_L β1 = Abar_L, on the full center.',
    '‖Abar_L(Q) − d‖ ≤ 3(d − 1)/(2L + 1).',
], size=26)
arrow(402,323,402,405)
arrow(1158,323,1158,405)
box(60, 700, 682, 205, [
    'Concrete finite original cost — FM21.16',
    'Original L* = 208 δ⁻²; balanced L* = 156 δ⁻².',
    'For every actual seed:  φL*(C) < 19 δ.',
    'All five discrepancy terms are controlled.',
], size=26)
box(818, 700, 682, 205, [
    'Every original compatible state — FM21.14',
    'Invariant ω gives ω(Q) = d exactly.',
    'Cω ≤ 2δ √(d/λ) + 4(λ − λ⁻¹) < 18δ.',
    'Original physical return and cost retained.',
], green, size=26)
arrow(402,610,402,700)
arrow(1158,610,1158,700)
box(60, 975, 1440, 86, [
    'The endpoint ω(R1) = λ/(4+λ) remains unresolved; no positive cost floor is claimed.',
], amber, size=27)
txt(60, 1075, 'Physical τ, EA/P0, both canonical traces, all five Ri and singular states remain original.', 24)
svg.append('</svg>')
(ROOT/'finite-original-moment-bounds-v21.svg').write_text('\n'.join(svg), encoding='utf-8')
im.save(ROOT/'finite-original-moment-bounds-v21.png')
print({'image': str(ROOT/'finite-original-moment-bounds-v21.png'), 'width': W, 'height': H})

svg_path=ROOT/'finite-original-moment-bounds-v21.svg'
svg_path.write_text("\n".join(x.rstrip() for x in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")
