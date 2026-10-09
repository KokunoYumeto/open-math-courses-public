from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html

ROOT = Path(__file__).resolve().parent
W, H = 1460, 940
bg, ink, blue, pale, amber = '#fafbf9', '#172e35', '#245c74', '#e8f0f3', '#f5ead3'
FONT = Path('C:/Windows/Fonts/segoeui.ttf')
FONT_B = Path('C:/Windows/Fonts/segoeuib.ttf')
im = Image.new('RGB', (W, H), bg)
d = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       f'<rect width="{W}" height="{H}" fill="{bg}"/>']

def txt(x, y, s, size=28, bold=False, color=ink):
    f = ImageFont.truetype(str(FONT_B if bold else FONT), size)
    d.text((x, y), s, font=f, fill=color)
    weight = '700' if bold else '400'
    svg.append(f'<text x="{x}" y="{y+size}" fill="{color}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{weight}">{html.escape(s)}</text>')

def box(x, y, w, h, lines, fill=pale):
    d.rounded_rectangle((x, y, x+w, y+h), radius=18, fill=fill, outline=blue, width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{blue}" stroke-width="2"/>')
    for k, line in enumerate(lines):
        txt(x+25, y+23+k*43, line, 27, k==0)

def arrow(x1, y1, x2, y2):
    import math
    d.line((x1, y1, x2, y2), fill=blue, width=4)
    angle = math.atan2(y2-y1, x2-x1)
    pts = [(x2, y2), (x2-18*math.cos(angle-.5), y2-18*math.sin(angle-.5)), (x2-18*math.cos(angle+.5), y2-18*math.sin(angle+.5))]
    d.polygon(pts, fill=blue)
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{blue}" stroke-width="4"/>')
    svg.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="{blue}"/>')

txt(60, 30, 'Fixed WM.22: what finite height-state repair proves', 38, True)
txt(60, 90, 'Original full center, two starting phases, all five likelihoods retained', 26)
box(60, 155, 590, 205, ['Actual height-conditioned states', 'ηK from μU; ρK from μV', 'First-hit prefix has the tilted weights.', 'Post-hit finite-lamp error → 0.'])
box(815, 155, 590, 205, ['Entire cylinder law — HC19.2', 'Height-state clusters restrict to', 'the positive-drift lamp probabilities.', 'Their remote lamp expectations → 1.'])
arrow(650, 257, 815, 257)
txt(665, 188, 'finite', 22)
txt(665, 216, 'lamp tests', 22)
box(60, 455, 590, 205, ['Every finite group average — HC19.7', 'The origin defect may cancel.', 'At a sufficiently remote lamp x:', 'supx ‖σ − σ βax‖ = 2.'], amber)
box(815, 455, 590, 205, ['A full Følner cluster — HC19.8', 'For every fixed group element:', 'the invariance defect tends to 0.', 'All finite lamp marginals are fair.'])
arrow(355, 360, 355, 455)
arrow(1108, 360, 1108, 455)
arrow(650, 559, 815, 559)
txt(663, 482, 'weak-star', 22)
txt(663, 511, 'cluster', 22)
box(60, 755, 1345, 110, ['Endpoint still unresolved: ω(R1) = λ/(4+λ)?', 'Cylinder convergence does not evaluate the bounded measurable full-center Ri.'], '#f0f1ee')
txt(60, 892, 'The remote test varies with the finite average. It gives no floor for all invariant states.', 23)
svg.append('</svg>')
(ROOT / 'height-cylinders-and-finite-averages-v21.svg').write_text('\n'.join(svg), encoding='utf-8')
im.save(ROOT / 'height-cylinders-and-finite-averages-v21.png')
print({'image': str(ROOT / 'height-cylinders-and-finite-averages-v21.png'), 'width': W, 'height': H})

svg_path=ROOT/"height-cylinders-and-finite-averages-v21.svg"
svg_path.write_text("\n".join(x.rstrip() for x in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")
