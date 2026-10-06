"""Expected-inclusion composition and reversed commutant duals, Theorem 24.1. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="420" viewBox="0 0 540 420" role="img" aria-labelledby="title desc">',
         '<title id="title">Composing expectations reverses dual order</title>',
         '<desc id="desc">On P contained in N contained in M, the expectations run from M to N by E and then N to P by F. On the reversed commutant inclusion M-prime contained in N-prime contained in P-prime, F-prime goes from P-prime to N-prime and E-prime from N-prime to M-prime. The composite dual is E-prime composed with F-prime and has identity scalar cb.</desc>',
         '<rect width="540" height="420" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.algebra{font-size:23px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}</style>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#426987"/></marker></defs>']

def text(x, y, value, cls='label', anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def arrow(x1, y1, x2, y2):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#426987" stroke-width="2" marker-end="url(#arrow)"/>')

text(24, 34, 'Expectations compose; duals reverse', 'title')
text(24, 64, 'Assume Idx(E) = c < ∞ and Idx(F) = b < ∞.', 'small')
for x, value in [(70, 'P'), (270, 'N'), (470, 'M')]:
    text(x, 112, value, 'algebra', 'middle')
arrow(237, 105, 104, 105); text(170, 95, 'F', 'label', 'middle')
arrow(437, 105, 304, 105); text(370, 95, 'E', 'label', 'middle')
text(270, 154, 'G = F ∘ E', 'label', 'middle')
text(270, 184, 'Underlying inclusion: P ⊂ N ⊂ M', 'small', 'middle')
parts.append('<line x1="24" y1="208" x2="516" y2="208" stroke="#a4b4c8"/>')
for x, value in [(70, 'P′'), (270, 'N′'), (470, 'M′')]:
    text(x, 256, value, 'algebra', 'middle')
arrow(104, 249, 237, 249); text(170, 238, 'F′', 'label', 'middle')
arrow(304, 249, 437, 249); text(370, 238, 'E′', 'label', 'middle')
text(270, 297, 'G′ = E′ ∘ F′;   G′(1) = cb1', 'label', 'middle')
text(270, 329, 'Reversed inclusion: M′ ⊂ N′ ⊂ P′', 'small', 'middle')
text(24, 372, 'Theorem 24.1: all-reference spatial identity (24.4).', 'small')
text(24, 402, 'Idx(G) = cb in every faithful normal representation.', 'small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts) + '\n', encoding='utf-8')
