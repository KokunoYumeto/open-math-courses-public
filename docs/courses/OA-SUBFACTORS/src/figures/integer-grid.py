"""Reproduce the exact integer rectangle of Proposition 14.9 (CC0).

The arrows denote inclusions. Reflection is an algebra anti-isomorphism;
no trace equality or infinite normal extension is asserted.
"""
from pathlib import Path
from html import escape

width, height = 640, 865
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
    '<title>Integer rectangle and its algebraic reflection about zero</title>',
    '<desc>Original corners A minus3 minus1, A minus3 1, A minus2 minus1, A minus2 1. '
    'Reflected corners A 1 3, A minus1 3, A 1 2, A minus1 2. '
    'Horizontal arrows point right and vertical arrows point upward.</desc>',
    '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" '
    'markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#24475e"/></marker></defs>',
    '<rect width="640" height="865" rx="16" fill="#f7fafc"/>',
]

def text(x, y, label, size=23, color="#193b50", anchor="middle"):
    parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
                 f'font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" '
                 f'fill="{color}">{escape(label)}</text>')

def arrow(x1, y1, x2, y2):
    parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#24475e" '
                 'stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')

text(320, 30, "Commuting integer rectangles", 27)
text(320, 61, "Exact coordinate reflection about zero", 23)
for base, heading, labels in (
    (0, "i = −3, j = −1, k = 1, l = 2",
     ("A(−3,−1)", "A(−3,1)", "A(−2,−1)", "A(−2,1)")),
    (390, "Θ₀ : A(r,s) ↦ A(−s,−r)",
     ("A(1,3)", "A(−1,3)", "A(1,2)", "A(−1,2)")),
):
    text(320, base+98, heading, 22)
    for x, y, label in ((180,base+150,labels[0]), (460,base+150,labels[1]),
                         (180,base+292,labels[2]), (460,base+292,labels[3])):
        parts.append(f'<rect x="{x-103}" y="{y-34}" width="206" height="56" rx="9" '
                     'fill="#e0eef4" stroke="#83a9bb"/>')
        text(x, y+3, label, 25)
    arrow(290,base+142,345,base+142)
    arrow(290,base+284,345,base+284)
    arrow(180,base+247,180,base+189)
    arrow(460,base+247,460,base+189)
    text(320,base+220,"E_P E_B = E_B E_P = E_C",19)
    text(320,base+347,"Each lower algebra is included above.",20)
arrow(320,365,320,431)
text(355,405,"Θ₀",25)
text(320,785,"Arrows show inclusions.",21)
text(320,815,"Θ₀ reverses products and preserves inclusions.",20)
text(320,845,"Infinite normal extension needs separate hypotheses.",19)
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n', encoding='utf-8')
