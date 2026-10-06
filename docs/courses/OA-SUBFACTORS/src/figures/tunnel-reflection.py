"""Reproduce the finite-level reflection diagram of Corollary 14.5."""
from pathlib import Path
from html import escape

out = Path(__file__).with_suffix('.svg')
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="670" viewBox="0 0 500 670" role="img" aria-labelledby="title desc">',
         '<title id="title">The two reflected starting levels</title>',
         '<desc id="desc">A downward relative commutant with endpoint M reflects to M prime intersect M a. The endpoint N reflects to M one prime intersect M a. Their tracial closures are R and S, respectively.</desc>',
         '<rect width="500" height="670" fill="#ffffff"/>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315c87"/></marker></defs>']

def label(x, y, text, size=22, color='#15202b', weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(text)}</text>')

def box(y, left, right):
    for x in (20, 280):
        parts.append(f'<rect x="{x}" y="{y}" width="200" height="72" rx="8" fill="#f0f5fa" stroke="#7897b5"/>')
    label(120, y + 45, left)
    label(380, y + 45, right)
    parts.append(f'<path d="M228,{y+36} L272,{y+36}" stroke="#315c87" stroke-width="2.5" marker-end="url(#arrow)"/>')

label(250, 38, 'Reflection keeps the starting level', 22, weight='bold')
label(250, 73, 'Θ(x) = Jx*J   ·   a ≥ 1', 22, '#315c87')
label(120, 120, 'Inside M', 20, weight='bold')
label(380, 120, 'Finite tower level', 20, weight='bold')
box(145, 'M₋ₐ′ ∩ M', 'M′ ∩ Mₐ')
box(290, 'M₋ₐ′ ∩ N', 'M₁′ ∩ Mₐ')
for x in (120, 380):
    parts.append(f'<path d="M{x},282 L{x},225" stroke="#315c87" stroke-width="2.5" marker-end="url(#arrow)"/>')
    label(x + 27, 261, '⊂', 24)
label(250, 407, 'Take the increasing tracial closures', 21)
box(435, 'R', 'M′ ∩ M∞')
box(558, 'S', 'M₁′ ∩ M∞')
for x in (120, 380):
    parts.append(f'<path d="M{x},550 L{x},515" stroke="#315c87" stroke-width="2.5" marker-end="url(#arrow)"/>')
    label(x + 27, 539, '⊂', 24)
parts.append('</svg>')
out.write_text('\n'.join(parts) + '\n', encoding='utf-8')
print(out.name)
