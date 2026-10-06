"""Exact rank/trace diagram for Lemma 16.1 and Exercise 16.2. CC0."""
from pathlib import Path
from html import escape

out = Path(__file__).with_suffix('.svg')
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="430" viewBox="0 0 500 430" role="img" aria-labelledby="title desc">',
         '<title id="title">Removing one row permits a matrix copy</title>',
         '<desc id="desc">For M5 plus M8, each minimal row has trace one thirteenth. Two pairs in M5 and four pairs in M8 give six copies of M2. The identity has trace twelve thirteenths; each minimal projection of the copied M2 has trace six thirteenths.</desc>',
         '<rect width="500" height="430" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:19px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}</style>']

def text(x, y, value, cls='label', anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

text(24, 32, 'A nearly full copy of M₂', 'title')
text(24, 60, 'Every cell represents one minimal row: trace 1/13.', 'small')
for count, y, name, first_pair in [(5, 105, 'M₅', 1), (8, 190, 'M₈', 3)]:
    text(24, y + 31, name)
    for j in range(count):
        kept = j < count - count % 2
        color = ('#2b6fbd' if j % 2 == 0 else '#2b9383') if kept else '#d8dde5'
        x = 78 + 49 * j
        parts.append(f'<rect x="{x}" y="{y}" width="43" height="43" rx="4" fill="{color}"/>')
        label = ('a' if j % 2 == 0 else 'b') + str(first_pair + j // 2) if kept else '×'
        parts.append(f'<text x="{x + 21.5}" y="{y + 27}" text-anchor="middle" font-size="14" font-family="Arial,sans-serif" fill="{"white" if kept else "#172c45"}">{label}</text>')
    text(78, y + 65, '2 copies of M₂; one row removed' if count == 5 else '4 copies of M₂; all rows retained', 'small')

parts.append('<line x1="24" y1="278" x2="476" y2="278" stroke="#a4b4c8"/>')
text(24, 311, 'Identity q: 12 retained cells, τ(q) = 12/13.')
text(24, 340, 'Blue projection: six a-cells, trace 6/13.')
text(24, 369, 'Green projection: six b-cells, trace 6/13.')
text(24, 405, 'Equal traces allow unitary matching with Az.', 'small')
parts.append('</svg>')
out.write_text('\n'.join(parts) + '\n', encoding='utf-8')
