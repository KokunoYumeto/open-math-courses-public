"""Reproduce Figure 16.1; original drawing, CC0, September 2026.

Exact objects: A4 with even vertices 0,2 and odd vertices 1,3;
B=[[1,1],[1,0]], lambda=phi, pi=(phi**2,1)/(phi**2+1).
The lower panels depict the limiting stochastic matrices, not a geometry.
"""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 660" '
         'role="img" aria-labelledby="title desc">',
         '<title id="title">A4 thermal endpoint sectors</title>',
         '<desc id="desc">Odd vertices 1 and 3 index the two extreme graph KMS states. '
         'The negative transfer tail tends to the identity; the positive tail mixes '
         'to pi. The finite interval has odd endpoints at positions minus 2m minus 1 '
         'and 2m plus 1.</desc>',
         '<rect width="900" height="660" fill="#ffffff"/>']

def text(x, y, label, size=20, anchor='start', color='#182124', weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" '
                 f'font-size="{size}" text-anchor="{anchor}" fill="{color}" '
                 f'font-weight="{weight}">{escape(label)}</text>')

def line(x1, y1, x2, y2, color='#52636c', width=3):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                 f'stroke="{color}" stroke-width="{width}"/>')

text(450, 34, 'A₄: two graph thermal boundary sectors', 27, 'middle', weight='bold')
text(450, 64, 'δ = φ = (1 + √5)/2     index = φ²     V = {1, 3}', 20, 'middle')
xs = [140, 340, 540, 740]
for left, right in zip(xs, xs[1:]):
    line(left, 117, right, 117)
for vertex, x in enumerate(xs):
    odd = vertex in (1, 3)
    parts.append(f'<circle cx="{x}" cy="117" r="19" fill="'
                 f'{"#155d7a" if odd else "#ffffff"}" stroke="#155d7a" stroke-width="3"/>')
    text(x, 124, str(vertex), 20, 'middle', '#ffffff' if odd else '#155d7a', 'bold')
    text(x, 163, 'odd endpoint' if odd else 'even vertex', 18, 'middle')
text(450, 201, 'B = [[1, 1], [1, 0]]     λ = φ     π = (φ², 1)/(φ² + 1)', 21, 'middle')
text(450, 236, 'P = [[1/φ, 1/φ²], [1, 0]]     Pₙ = (λP + e⁻ᵝⁿI)/(λ + e⁻ᵝⁿ)', 20, 'middle')
for x, title, color in [(30, 'Negative indices n = −k', '#eaf3f5'),
                        (480, 'Positive indices n = k', '#f5f2e8')]:
    parts.append(f'<rect x="{x}" y="267" width="390" height="213" rx="12" '
                 f'fill="{color}" stroke="#d2dde0"/>')
    text(x+195, 305, title, 22, 'middle', weight='bold')
text(225, 346, 'P₋ₖ → I; changes are summable', 19, 'middle')
text(225, 380, 'Lₘ = ∏ₖ₌ₘ₊₁∞ P₋ₖ → I', 21, 'middle')
text(225, 415, 'Keeps the limiting vector h', 20, 'middle')
text(225, 451, 'Extreme h: (1/π₁, 0), (0, 1/π₃)', 18, 'middle')
text(675, 346, 'Pₖ → P; P is primitive', 20, 'middle')
text(675, 380, '∏ₖ₌ₘ₊₁ᴺ Pₖ → Π as N → ∞', 20, 'middle')
text(675, 415, 'Π(a, b) = πᵦ', 22, 'middle')
text(675, 451, 'Forgets the right endpoint', 20, 'middle')
text(450, 522, 'Finite path window for Aₘ', 22, 'middle', weight='bold')
line(105, 552, 795, 552)
for x in (105, 795):
    parts.append(f'<circle cx="{x}" cy="552" r="7" fill="#155d7a"/>')
text(105, 584, '−2m−1', 20, 'middle')
text(795, 584, '2m+1', 20, 'middle')
text(450, 584, 'Hₘ = Σₙ₌₋ₘᵐ n e₂ₙ', 23, 'middle')
text(450, 629, 'Canonical mixture: π₁ ω⁽¹⁾ + π₃ ω⁽³⁾', 22, 'middle')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n', encoding='utf-8')
