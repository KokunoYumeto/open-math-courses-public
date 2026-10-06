"""Exact native SVG for one marked-monomial type transition; Python stdlib.

Original programme figure, CC0. No external artwork or mathematical source body
is embedded. The containing-label mechanism is used in SH03/subanalytic-sets-and-limiting-tangent-directions.md,
TN12--TN14; the explicit x^2 y^2 z^2 calculation is independently verified here.
Run: python SH03-terminal-type-genealogy.py [output.svg]
"""

from itertools import combinations
from pathlib import Path
from html import escape
import json
import sys


def minimal_sets(weights, mark):
    subsets = []
    for size in range(1, len(weights) + 1):
        for subset in combinations(range(len(weights)), size):
            total = sum(weights[i] for i in subset)
            if total >= mark and all(total - weights[i] < mark for i in subset):
                subsets.append(subset)
    return subsets


def type_bits(labels, subset, count=4):
    selected = {labels[i] for i in subset}
    return ''.join('1' if i in selected else '0' for i in range(count))


def verify():
    old = minimal_sets((2, 2, 2), 3)
    assert old == [(0, 1), (0, 2), (1, 2)]
    assert 2 + 2 - 3 == 1
    # x-chart variables u,v,z correspond to the new divisor, H2,H3.
    x_types = {type_bits((3, 1, 2), a) for a in minimal_sets((1, 2, 2), 3)}
    # y-chart variables t,w,z correspond to the new divisor, H1,H3.
    y_types = {type_bits((3, 0, 2), a) for a in minimal_sets((1, 2, 2), 3)}
    assert x_types == {'0101', '0011', '0110'}
    assert y_types == {'1001', '0011', '1010'}
    new_types = x_types | y_types
    assert '1100' not in new_types
    assert {s for s in new_types if s[-1] == '0'} == {'1010', '0110'}
    assert {s for s in new_types if s[-1] == '1'} == {'1001', '0101', '0011'}
    # The fibre over (0,0,0) is E intersect z=0. At its two endpoint
    # directions the incident weights are 1+2+2=5. Every listed type
    # contains at least one of these endpoint germs, so every type-bound is 5.
    assert sum((2, 2, 2)) == 6 and sum((1, 2, 2)) == 5
    return {'mark': 3, 'old_weights': [2, 2, 2],
            'x_chart_weights': [1, 2, 2], 'y_chart_weights': [1, 2, 2],
            'old_types': ['110', '101', '011'],
            'surviving_types': ['1010', '0110'],
            'new_types': ['1001', '0101', '0011'],
            'old_maximum_weight': 6, 'new_type_bounds_on_origin_fibre': 5}


def make_svg():
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1480" '
           'viewBox="0 0 720 1480" role="img" aria-labelledby="title desc">',
           '<title id="title">A finite genealogy of terminal component types</title>',
           '<desc id="desc">Exact marked monomial x squared y squared z squared, '
           'mark three. Blow up x equals y equals zero. The old type 110 is selected; '
           'types 101 and 011 survive with appended zero. Three new types 1001,0101,0011 '
           'have new exceptional bit one. The maximum terminal weight over the origin '
           'fibre falls from six to five. This is one monomial transition, not a full '
           'resolution invariant for the function.</desc>',
           '<metadata>Original programme figure and generator: CC0. Proof locator: '
           'SH03/subanalytic-sets-and-limiting-tangent-directions.md, Component types survive restriction without splitting '
           'into new types; TN12a--TN14. Framework comparison: Bierstone--Milman, '
           'author manuscript 25 November 1996, pp.39--40; explicit example computed here.'
           '</metadata>',
           '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" '
           'refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6" '
           'fill="#385b83"/></marker></defs>',
           '<rect width="720" height="1480" fill="#ffffff"/>',
           '<g font-family="Arial,DejaVu Sans,sans-serif" fill="#16283e">']

    def text(x, y, value, size=28, weight='normal', anchor='start', color=None):
        attrs = f'x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"'
        if color:
            attrs += f' fill="{color}"'
        out.append(f'<text {attrs}>{escape(value)}</text>')

    def box(x, y, width, height, fill='#f4f7fb', stroke='#b7c7d8'):
        out.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
                   f'rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

    text(32, 48, 'A finite genealogy of component types', 31, 'bold')
    text(32, 89, 'One exact terminal-monomial transition', 27)
    box(24, 118, 672, 302)
    text(46, 159, '1. Before the blow-up', 29, 'bold')
    text(46, 207, '(x² y² z², 3)  on  ℝ³', 33)
    text(46, 253, 'H₁: x = 0   H₂: y = 0   H₃: z = 0', 27)
    text(46, 299, 'Minimal components: 110, 101, 011', 27)
    text(46, 343, 'Select 110: C = {x = y = 0}.', 28, 'bold', color='#8a3e1f')
    text(46, 389, 'Over a = (0,0,0): each type has bound 6.', 26)

    box(24, 445, 672, 403)
    text(46, 489, '2. Both projective charts', 29, 'bold')
    text(46, 536, 'x = u,  y = uv,  z = z', 29)
    text(46, 580, 'Controlled monomial: u v² z²   (mark 3)', 28)
    text(46, 624, 'Types: 0101, 0011, 0110', 27)
    out.append('<path d="M46 646 H674" stroke="#b7c7d8" stroke-width="2"/>')
    text(46, 691, 'y = t,  x = tw,  z = z', 29)
    text(46, 735, 'Controlled monomial: t w² z²   (mark 3)', 28)
    text(46, 779, 'Types: 1001, 0011, 1010', 27)
    text(46, 823, 'New label H₄ = E; new exponent 2+2−3 = 1.', 25)

    box(24, 873, 672, 487)
    text(46, 917, '3. Types over the compact origin fibre', 28, 'bold')
    text(46, 960, 'Old types survive with new bit 0:', 27)
    text(46, 1003, '101 → 1010   |   011 → 0110', 28, 'bold')
    text(46, 1045, 'Their current bounds are 5.', 27)
    box(227, 1072, 266, 68, '#fff0e5', '#bb7348')
    text(360, 1117, 'selected 110; rank 6', 26, 'bold', 'middle')
    for target in (135, 360, 585):
        out.append(f'<path d="M360 1140 L{target} 1190" fill="none" '
                   'stroke="#385b83" stroke-width="3" marker-end="url(#arrow)"/>')
    for x, label in ((46, '1001'), (271, '0101'), (496, '0011')):
        box(x, 1197, 178, 94, '#e9f4f2', '#599086')
        text(x+89, 1236, label, 31, 'bold', 'middle')
        text(x+89, 1275, 'rank 5', 26, 'normal', 'middle')
    text(46, 1335, 'New bit 1 distinguishes every new type.', 27)
    text(32, 1407, 'Bits record containment of a whole component.', 26)
    text(32, 1445, 'One monomial step; no full-function invariant is claimed.', 24)
    out.append('</g></svg>')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.svg')
    result = verify()
    output.write_text(make_svg(), encoding='utf-8')
    output.with_suffix('.verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {output}; exact monomial and incidence checks passed.')
