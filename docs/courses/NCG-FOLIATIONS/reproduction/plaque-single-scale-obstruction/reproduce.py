"""CC0 original drawing of the single-scale interpolation obstruction."""
from pathlib import Path
import argparse, base64, html, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, default=HERE / 'figures')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
FONT = HERE / 'fonts/DejaVuSans.ttf'
NOTICE = (HERE / 'FONT-NOTICE.txt').read_text(encoding='utf8')
W, H = 2400, 1540
im = Image.new('RGB', (W, H), '#f6f8fc')
draw = ImageDraw.Draw(im)
font_cache = {}
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<title>One interpolating plaque scale cannot serve both roles</title>',
    '<desc>Fixed length-four circle and ordinary chart, exact boundary cutoff at epsilon 1/32, even-reflected smooth extension, duality and interpolation maps, and the proved cross-boundary integral lower bound. No spectrum or unspecified constant is sampled.</desc>',
    '<metadata>' + html.escape('Original diagram and generator: CC0-1.0.\nUnmodified DejaVu Sans full terms:\n' + NOTICE) + '</metadata>',
    '<style>@font-face{font-family:NormSans;src:url(data:font/ttf;base64,' + base64.b64encode(FONT.read_bytes()).decode() + ')}text{font-family:NormSans}</style>',
    f'<rect width="{W}" height="{H}" fill="#f6f8fc"/>',
]

def txt(x, y, value, size=27, color='#14243a'):
    if size not in font_cache:
        font_cache[size] = ImageFont.truetype(str(FONT), size)
    draw.text((x, y), value, fill=color, font=font_cache[size], anchor='lt')
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(value)}</text>')

def rect(x, y, w, h, fill='#ffffff', stroke='#cbd5e1'):
    draw.rectangle((x, y, x+w, y+h), fill=fill, outline=stroke, width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')

def line(x, y, x2, y2, color='#72839b', width=3):
    draw.line((x, y, x2, y2), fill=color, width=width)
    svg.append(f'<path d="M{x},{y} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}"/>')

def poly(points, color='#245fad', width=4):
    draw.line(points, fill=color, width=width)
    svg.append('<polyline points="' + ' '.join(f'{x:.3f},{y:.3f}' for x, y in points) + f'" fill="none" stroke="{color}" stroke-width="{width}"/>')

def arrow(x, y, x2, y2, color='#245fad'):
    line(x, y, x2, y2, color, 4)
    a = math.atan2(y2-y, x2-x)
    points = [(x2, y2)] + [(x2-16*math.cos(a+z), y2-16*math.sin(a+z)) for z in [-0.45, 0.45]]
    draw.polygon(points, fill=color)
    svg.append('<polygon points="' + ' '.join(f'{x:.3f},{y:.3f}' for x, y in points) + f'" fill="{color}"/>')

def ellipse(cx, cy, r, color='#72839b', width=5):
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), outline=color, width=width)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}"/>')

def smooth_step(z):
    if z <= 0: return 0.0
    if z >= 1: return 1.0
    a, b = -1/z, -1/(1-z)
    return 1/(1+math.exp(max(-700, min(700, b-a))))

def eta(t):
    return smooth_step(t-1)

EPS = 1/32
def f(t):
    return eta(t/EPS)*eta((1-t)/EPS) if 0 <= t <= 1 else 0.0

def reflected(t):
    if -1 < t < 0: value = f(-t)
    elif 0 <= t <= 1: value = f(t)
    elif 1 < t < 2: value = f(2-t)
    else: return 0.0
    # Fixed smooth cutoff supported in [-3/4,7/4], equal to one
    # on [-1/2,3/2]. Its flat endpoint extensions are smooth.
    chi = smooth_step(4*(t+3/4))*smooth_step(4*(7/4-t))
    return chi*value

txt(50, 35, 'One interpolating plaque scale cannot serve both roles', 44)
txt(50, 106, 'A fixed ordinary chart suffices: input restriction + interpolation conflicts with half-order zero extension.', 28)
rect(45, 172, 1125, 597)
rect(1210, 172, 1145, 597)
rect(45, 809, 1125, 630)
rect(1210, 809, 1145, 630)

txt(75, 197, 'A. The actual compact leaf and its chart', 32)
cx, cy, r = 330, 445, 178
ellipse(cx, cy, r)
arc = [(cx+r*math.cos(2*math.pi*x/4), cy-r*math.sin(2*math.pi*x/4))
       for x in [i/400 for i in range(401)]]
poly(arc, '#13916b', 10)
for x in range(4):
    a=2*math.pi*x/4
    px, py = cx+r*math.cos(a), cy-r*math.sin(a)
    line(cx+(r-8)*math.cos(a), cy-(r-8)*math.sin(a), cx+(r+9)*math.cos(a), cy-(r+9)*math.sin(a), '#14243a', 3)
    txt(px+16*math.cos(a)-9, py-20*math.sin(a)-14, str(x), 25)
for px,py in [(cx+r,cy),(cx,cy-r)]:
    draw.ellipse((px-7,py-7,px+7,py+7),fill='#ffffff',outline='#13916b',width=3)
    svg.append(f'<circle cx="{px}" cy="{py}" r="7" fill="#ffffff" stroke="#13916b" stroke-width="3"/>')
txt(245, 421, 'M = ℝ / 4ℤ', 29)
txt(218, 470, 'circumference 4', 24)
txt(584, 311, 'Ordinary physical chart I = (0,1)', 27)
txt(584, 368, 'Metric dx²; density dx', 27)
txt(584, 425, 'Full rank-one foliation', 27)
txt(584, 482, 'Holonomy is trivial', 27)
txt(584, 539, 'Actual groupoid M × M', 27)
txt(76, 653, 'Each kernel is smooth and compact in I × I.', 27)
txt(76, 709, 'The chart and global spectral operator stay fixed.  NI.1, NI.3', 24)

txt(1240, 197, 'B. Two different extensions of one profile', 32)
left, top, width, height = 1294, 325, 945, 242
line(left, top+height, left+width, top+height)
line(left, top+height, left, top-24)
points_zero, points_reflected = [], []
for i in range(1201):
    x=-1+3*i/1200
    px=left+width*(x+1)/3
    points_zero.append((px,top+height-height*f(x)))
    points_reflected.append((px,top+height-height*reflected(x)))
poly(points_reflected, '#13916b', 6)
poly(points_zero, '#c8534b', 4)
for x in [-1,0,1,2]:
    px=left+width*(x+1)/3
    line(px, top+height-5, px, top+height+9)
    txt(px-12, top+height+18, str(x), 22)
txt(left-30, top-15, '1', 23)
txt(1244, 255, 'ε = 1/32; sampled smooth function values', 26)
txt(1244, 641, 'Red: zero extension.  Green: even reflection + fixed cutoff.', 25)
txt(1244, 702, 'Reflection has a uniform H¹ᐟ² extension bound.  NI.8–9', 25)

txt(75, 834, 'C. What the input estimate forces', 32)
rect(81, 923, 1049, 89, '#edf4ff')
txt(104, 946, 'K : X₁ anti-dual  →  W⁻¹(M),     ‖K‖ ≤ C₁₀', 30)
arrow(606, 1020, 606, 1063)
txt(694, 1026, 'Hilbert anti-duality', 25)
rect(81, 1074, 1049, 89, '#edf4ff')
txt(104, 1096, 'R₁ : W¹(M)  →  X₁,     j R₁ u = u|I', 30)
arrow(606, 1172, 606, 1214)
txt(694, 1178, 'Interpolation with L² restriction', 23)
rect(81, 1225, 1049, 89, '#eaf7f0')
txt(103, 1247, 'R½ : W¹ᐟ²(M) → [L²(I),X₁]½,    ‖R½‖ ≤ √C₁₀', 28)
txt(78, 1366, 'Compact-test density in X₁ is not assumed.  NI.4–7', 26)

txt(1240, 834, 'D. The cross-boundary lower integral', 32)
left, top, width, height = 1300, 967, 925, 294
line(left, top+height, left+width, top+height)
line(left, top+height, left, top-15)
points=[]
for i in range(401):
    a=1+4*i/400
    inv=10**a
    value=2*math.log((1+2/inv)/(6/inv))
    points.append((left+width*(a-1)/4,top+height-height*value/20))
poly(points, '#c8534b', 6)
for a in range(1,6):
    px=left+width*(a-1)/4
    line(px, top+height-5, px, top+height+9)
    txt(px-19, top+height+19, '10'+{1:'¹',2:'²',3:'³',4:'⁴',5:'⁵'}[a], 23)
for y in [0,5,10,15,20]:
    py=top+height-height*y/20
    line(left-8,py,left+3,py)
    txt(left-45,py-13,str(y),22)
txt(1503, 908, '2 log((1 + 2ε)/(6ε))  →  ∞', 30, '#a63b33')
txt(2124, 1322, '1/ε', 25)
txt(1245, 1322, 'Logarithmic horizontal axis.', 25)
txt(1245, 1372, 'A proved seminorm lower bound; no spectrum is sampled.  NI.11–12', 23)

txt(48, 1476, 'Theorem: the two estimates cannot both hold for a common interpolating scale. Distinct input/output realizations remain valid.', 27)
svg.append('</svg>')
im.save(args.output/'plaque-single-scale-obstruction.png')
(args.output/'plaque-single-scale-obstruction.svg').write_bytes(('\n'.join(svg)+'\n').encode('utf8'))
print(json.dumps({'dimensions':[W,H], 'epsilon_profile':EPS, 'font':'fonts/DejaVuSans.ttf',
                  'curve':'exact lower integral 2 log((1+2 epsilon)/(6 epsilon))',
                  'font_sizes':sorted(font_cache), 'sampled_spectra':False}))
