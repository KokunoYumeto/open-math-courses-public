"""Exact anchored scalar-transfer samples and proof diagram: original, CC0.

The toy groupoid is the two-unit groupoid T={0,1}.  The actual theorem
uses its stated groupoid and full parameter families, not these samples.
PNG and SVG share the same exact-coordinate drawing instructions.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, base64, html, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, default=HERE)
ROOT = parser.parse_args().output
ROOT.mkdir(parents=True, exist_ok=True)
FONT_ROOT = HERE
FONT = FONT_ROOT / "fonts" / "DejaVuSans.ttf"
NOTICE = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
W, H = 2400, 1530
INK, BLUE, RED, GREEN, GRAY = "#17283c", "#17638d", "#bc4d32", "#286d49", "#65737e"
im = Image.new("RGB", (W, H), "#f8fafc")
draw = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<title>Ordinary anchored transfer: section contractions and exact class comparison</title>',
       '<desc>Exact two-unit groupoid samples, original anchor types and the epsilon comparison. Numerical panels do not replace the analytic proof.</desc>',
       '<metadata>' + html.escape('Original drawing and generator: CC0.\n' + NOTICE) + '</metadata>',
       '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,' + base64.b64encode(FONT.read_bytes()).decode() + ')}text{font-family:LocalSans}</style>',
       f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']

def text(x, y, value, size=30, color=INK):
    if size not in fonts:
        fonts[size] = ImageFont.truetype(str(FONT), size, layout_engine=ImageFont.Layout.BASIC)
    bbox = draw.textbbox((x, y), value, font=fonts[size], anchor="lt")
    if bbox[0] < 0 or bbox[1] < 0 or bbox[2] > W or bbox[3] > H:
        overflow.append([value, list(bbox)])
    draw.text((x, y), value, font=fonts[size], fill=color, anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(value)}</text>')

def line(x, y, xx, yy, color=GRAY, width=3):
    draw.line((x, y, xx, yy), fill=color, width=width)
    svg.append(f'<path d="M{x:.5f},{y:.5f}L{xx:.5f},{yy:.5f}" stroke="{color}" stroke-width="{width}" fill="none"/>')

def box(x, y, w, h, fill="white", border="#c9d5e3"):
    draw.rectangle((x, y, x+w, y+h), fill=fill, outline=border, width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{border}" stroke-width="3"/>')

def arrow(x, y, xx, yy):
    line(x, y, xx, yy, BLUE, 4)
    angle = math.atan2(yy-y, xx-x)
    pts = [(xx, yy)] + [(xx-15*math.cos(angle+a), yy-15*math.sin(angle+a)) for a in [-.45, .45]]
    draw.polygon(pts, fill=BLUE)
    svg.append('<polygon points="' + ' '.join(f'{px:.5f},{py:.5f}' for px, py in pts) + f'" fill="{BLUE}"/>')

def graph(x, y, w, h, ymin=Q(0), ymax=Q(1)):
    def point(s, value):
        return x+float(s)*w, y+h-float((value-ymin)/(ymax-ymin))*h
    for i in range(5):
        s = Q(i, 4)
        xx, _ = point(s, ymin)
        line(xx, y, xx, y+h, "#dae3ec", 2)
        text(xx-16, y+h+15, f'{float(s):g}', 25)
        v = ymin+(ymax-ymin)*s
        _, yy = point(0, v)
        line(x, yy, x+w, yy, "#dae3ec", 2)
        text(x-78, yy-15, f'{float(v):g}', 25)
    line(x, y, x, y+h, GRAY, 3)
    line(x, y+h, x+w, y+h, GRAY, 3)
    text(x+w/2-90, y+h+58, 'homotopy s', 30)
    return point

text(50, 28, 'Original-unit scalar transfer: contractions preserve each unit fibre', 46)
text(50, 90, 'Actual theorem: R = C₀(T), proper P and continuous θM.  Numerical panels: exact toy G = T = {0,1}, only units.', 29)

box(50, 145, 1115, 745)
box(1210, 145, 1140, 745)
text(78, 170, '1  Half-mass family → ordinary unit section  ·  AS.11–AS.14', 30)
text(78, 222, 'μy(s) = (1−s)μy + s δ₁y ;  each endpoint retains its unit y.', 29)
p = graph(170, 340, 900, 350, Q(1, 2), Q(1))
line(*p(Q(0), Q(3, 5)), *p(Q(1), Q(1)), BLUE, 5)
line(*p(Q(0), Q(9, 10)), *p(Q(1), Q(1)), RED, 5)
text(205, 300, 'mass in the exact two-unit toy (not a global mass-continuity claim)', 25)
text(86, 798, 'blue y=0:  (3/5 + 2s/5) δ₁₀', 30, BLUE)
text(86, 844, 'red   y=1:  (9/10 + s/10) δ₁₁   ·   δ₁₀ and δ₁₁ are different points.', 27, RED)

text(1238, 170, '2  Probability family → ordinary section  ·  AS.15–AS.16', 30)
text(1238, 222, 'Xy = Prob({ay,by}); qy = ν(by).  x₀(0)=δa₀; x₀(1)=δb₁.', 29)
pp = graph(1330, 340, 915, 350)
line(*pp(Q(0), Q(2, 5)), *pp(Q(1), Q(0)), BLUE, 5)
line(*pp(Q(0), Q(7, 10)), *pp(Q(1), Q(1)), RED, 5)
text(1364, 300, 'probability coordinate qy', 25)
text(1246, 798, 'blue y=0: q₀(s)=(1−s)2/5  →  0', 30, BLUE)
text(1246, 844, 'red   y=1: q₁(s)=(1−s)7/10+s  →  1  ·  section, not one scalar point.', 27, RED)

box(50, 930, 2300, 550)
text(78, 956, '3  Actual equivariant coefficient types before ordinary contraction  ·  AS.17–AS.19', 34)
labels = ['R', 'A = C₀(X)', 'B', 'B ⊗R P', 'A ⊗R P', 'P', 'R']
factors = ['[u]', 'ηX', 'TB', 'dX ⊠R 1P', '[eP]', 'D']
starts = [90+i*320 for i in range(7)]
for i, label in enumerate(labels):
    box(starts[i], 1070, 245, 80, '#edf4f8', BLUE)
    text(starts[i]+20, 1090, label, 34)
for i, factor in enumerate(factors):
    arrow(starts[i]+245, 1110, starts[i+1], 1110)
    text(starts[i]+245, 1031, factor, 23)
text(86, 1191, 'pX proper ⇒ u:R→C₀(X) is an actual homomorphism.  eP is the equivariant central collapse, not evaluation.', 29)
text(86, 1252, 'ε = [u] ForG(ηX dX) [e₀] ∈ KK_T(R,R) ;  e₀ evaluates along the ordinary section x₀.', 32)
text(86, 1310, 'ForG(η) = ε θ₀ ;   θ₀ D₀ = 1R    ⇒    ForG(ηD) = ε.     Whole-base vacuum identity ⇒ ε = 1R.', 32, GREEN)
text(86, 1370, 'Exact weaker local input: bU ε = bU  ⇒  bU ForG(ηD) = bU.  These bU products forget the anchor only, retaining R.', 28)
text(86, 1423, 'No equivariant section contraction, equivariant scalar evaluation, or equivariant γ=1 is used.', 29)

svg.append('</svg>')
im.save(ROOT / 'anchored-transfer.png')
(ROOT / 'anchored-transfer.svg').write_text('\n'.join(svg), encoding='utf-8')
data = {
    'schema': 'anchored-transfer-figure/v1',
    'original_drawing_license': 'CC0',
    'toy_groupoid': 'G=T={0,1}, only units',
    'half_mass_paths': {'y0': '(3/5+2s/5) delta_1_0', 'y1': '(9/10+s/10) delta_1_1'},
    'probability_paths': {'y0': '(1-s)*2/5', 'y1': '(1-s)*7/10+s'},
    'exact_endpoint_checks': [Q(3, 5)+Q(2, 5)==1, Q(9, 10)+Q(1, 10)==1, (1-Q(1))*Q(2, 5)==0, (1-Q(1))*Q(7, 10)+Q(1)==1],
    'canvas': [W, H], 'text_canvas_overflows': overflow,
    'proof_locators': ['AS.11-AS.14', 'AS.15-AS.16', 'AS.17-AS.21'],
    'human_provenance': 'Jean-Louis Tu, original 2004 printed pp.282-284, Proposition 3.2; the anchored argument is proved in K-theory of the leaf space, Section 11AD.3',
    'font_source': 'fonts/DejaVuSans.ttf',
    'font_notice_source': 'FONT-NOTICE.txt'
}
(ROOT / 'figure-data.json').write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8', newline='\n')
if overflow:
    raise RuntimeError('Text overflows the drawing canvas: '+repr(overflow))
print(json.dumps({'png': 'anchored-transfer.png', 'svg': 'anchored-transfer.svg', 'checks': 'figure-data.json', 'exact_checks': all(data['exact_endpoint_checks']), 'overflows': len(overflow)}))
