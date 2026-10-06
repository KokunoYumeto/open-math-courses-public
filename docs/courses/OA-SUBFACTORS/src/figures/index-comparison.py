"""Direct-sum comparison of the commutant dual, Lemma 22.1/Theorem 22.2. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="570" viewBox="0 0 540 570" role="img" aria-labelledby="title desc">',
         '<title id="title">One scalar index in two representations</title>',
         '<desc id="desc">The direct sum of two faithful normal representations has summand projections p1 and p2 in the common target commutant A. Its dual T from B to A compresses to the two representation duals. A diagonal reference weight splits both closed spatial forms and their domains. All three identity values have the same scalar c, possibly infinite.</desc>',
         '<rect width="540" height="570" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}.box{fill:#edf3fb;stroke:#7c9bbd;stroke-width:1.5}</style>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#426987"/></marker></defs>']

def text(x, y, value, cls='label', anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def line(x1, y1, x2, y2):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#426987" stroke-width="2" marker-end="url(#arrow)"/>')

text(24, 34, 'Compare inside H = H₁ ⊕ H₂', 'title')
text(24, 66, 'A = π(M)′ ⊂ B = π(N)′;   p₁, p₂ ∈ A', 'label')
parts.append('<rect x="24" y="92" width="492" height="115" rx="8" class="box"/>')
text(270, 120, 'The common commutant dual', 'heading', 'middle')
text(112, 156, 'B₊', 'heading', 'middle')
text(428, 156, 'Â₊', 'heading', 'middle')
line(145, 150, 388, 150)
text(270, 142, 'T', 'label', 'middle')
text(270, 189, 'T(1) = c1,   c ∈ [1, ∞]', 'label', 'middle')
line(160, 210, 150, 244)
line(380, 210, 390, 244)
for x, i in [(24, '₁'), (284, '₂')]:
    parts.append(f'<rect x="{x}" y="253" width="232" height="136" rx="8" class="box"/>')
    text(x + 116, 281, f'On H{i}', 'heading', 'middle')
    text(x + 116, 311, f'T{i} = T restricted to p{i}Bp{i}', 'small', 'middle')
    text(x + 116, 340, f'T{i}(p{i}) = c p{i}', 'label', 'middle')
    text(x + 116, 369, 'The dual in that representation', 'small', 'middle')
text(270, 235, 'compress by pᵢ', 'small', 'middle')
parts.append('<line x1="24" y1="417" x2="516" y2="417" stroke="#a4b4c8"/>')
text(24, 447, 'β(a) = β₁(p₁ap₁) + β₂(p₂ap₂)', 'label')
text(24, 477, 'Diagonal references split both spatial derivatives.', 'small')
text(24, 503, 'Their closed-form domains split as well.', 'small')
text(24, 541, 'Lemma 22.1 and Theorem 22.2.', 'small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts) + '\n', encoding='utf-8')
