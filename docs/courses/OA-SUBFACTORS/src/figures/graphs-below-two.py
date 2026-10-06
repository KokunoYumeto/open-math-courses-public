"""Exact graph shapes and root locations for Theorems 20.3–20.7. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="670" viewBox="0 0 500 670" role="img" aria-labelledby="title desc">',
         '<title id="title">Graphs with adjacency norm below two</title>',
         '<desc id="desc">A5 and D6 illustrate their families. E6, E7, E8 have arm lengths 1,2,2; 1,2,3; 1,2,4. Filled endpoints mark roots of minimum Perron weight. The red E7 endpoint has squared Perron coordinate between one and two and is therefore impossible for a principal graph.</desc>',
         '<rect width="500" height="670" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:19px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}</style>']

def text(x, y, value, cls='label'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(value)}</text>')

def graph(points, edges, root=0, obstruction=None):
    for a, b in edges:
        x1, y1 = points[a]; x2, y2 = points[b]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#55738f" stroke-width="2.5"/>')
    for i, (x, y) in enumerate(points):
        fill = '#1e5c9d' if i == root else ('#d96048' if i == obstruction else '#ffffff')
        parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{fill}" stroke="#172c45" stroke-width="1.5"/>')

text(24, 31, 'The candidates below norm two', 'title')
text(24, 58, 'Filled vertex: an endpoint of minimum Perron weight.', 'small')

text(24, 92, 'A₅: a path; h = 6')
graph([(65+90*j, 121) for j in range(5)], [(j,j+1) for j in range(4)])
text(24, 151, 'Aℓ has ℓ vertices and h = ℓ + 1.', 'small')

text(24, 192, 'D₆: arms (1, 1, 3); h = 10')
graph([(65,242),(145,242),(225,242),(305,242),(385,217),(385,267)],
      [(0,1),(1,2),(2,3),(3,4),(3,5)])
text(24, 297, 'Dℓ has arms (1, 1, ℓ − 3); h = 2(ℓ − 1).', 'small')

text(24, 334, 'E₆: arms (1, 2, 2); h = 12')
graph([(65,389),(145,389),(225,389),(305,389),(385,389),(225,354)],
      [(0,1),(1,2),(2,3),(3,4),(2,5)])

text(24, 435, 'E₇: arms (1, 2, 3); h = 18')
graph([(45,490),(115,490),(185,490),(255,490),(325,490),(395,490),(255,455)],
      [(0,1),(1,2),(2,3),(3,4),(4,5),(3,6)], obstruction=5)
text(24, 521, 'Red endpoint: μ² = 4 sin²(2π/9) lies in (1, 2).', 'small')

text(24, 563, 'E₈: arms (1, 2, 4); h = 30')
graph([(35,617),(100,617),(165,617),(230,617),(295,617),(360,617),(425,617),(295,582)],
      [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(4,7)])
text(24, 652, 'Norm: 2 cos(π/h). Root and realization need extra tests.', 'small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n', encoding='utf-8')
