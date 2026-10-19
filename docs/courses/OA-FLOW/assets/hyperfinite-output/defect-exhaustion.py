"""Exact residuals for HADT15-16. Standard-library SVG and JSON generator."""
from pathlib import Path
from fractions import Fraction
import json
import re

ROOT = Path(__file__).resolve().parent
rows = [dict(n=n, residual_trace=str(Fraction(1, 3**n)),
             hilbert_error=f'3^(-{n}/2)', map_norm=1,
             trace_log3=-n, hilbert_error_log3=-n/2)
        for n in range(9)]
data = dict(model='L-infinity((0,1]), Lebesgue trace; a_j=indicator(3^-j,3^-(j-1)]',
            proof='OA-FLOW-HA.md, HADT15-HADT16',
            general_bound='||B_n(x)||_2 <= ||x|| sqrt(||h|| tau(h_n))',
            example_rate_is_not_a_general_rate=True, rows=rows)
(ROOT/'defect-exhaustion.json').write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="600" viewBox="0 0 1160 600" role="img" aria-labelledby="title desc">
<title id="title">Finite residuals: small trace does not force small operator norm</title>
<desc id="desc">For interval projections h_n on (0,3 to the minus n], the trace equals 3 to the minus n, the trace Hilbert norm equals 3 to the minus n over two, and the operator and tail-map norms stay one. Left: residual intervals for n zero through four. Right: exact values at n zero through eight on a base-three logarithmic vertical axis.</desc>
<rect width="1160" height="600" fill="#f5f7fb"/>
<style>text{font-family:Arial,sans-serif;fill:#18253a} .title{font-size:25px;font-weight:bold}.head{font-size:20px;font-weight:bold}.body{font-size:16px}.small{font-size:14px}.grid{stroke:#d4dce7;stroke-width:1}</style>
<text x="34" y="43" class="title">Finite residuals in a diffuse algebra</text>
<text x="34" y="72" class="body">h_n = 1_(0, 3^(-n)]   ·   B_n(x) = h_n x   ·   normalized Lebesgue trace</text>
<rect x="24" y="95" width="510" height="435" rx="12" fill="white"/>
<rect x="550" y="95" width="586" height="435" rx="12" fill="white"/>
<text x="44" y="130" class="head">The remaining interval</text>
<text x="44" y="158" class="small">Each step removes two thirds of the remaining mass.</text>
<text x="574" y="130" class="head">Three different sizes</text>
<text x="574" y="158" class="small">Exact values at integer stages; base-three logarithmic axis.</text>''']

for n in range(5):
    y = 205 + n*56
    length = 270 / (3**n)
    parts.append(f'<text x="44" y="{y+6}" class="body">n = {n}</text>')
    parts.append(f'<line x1="113" y1="{y}" x2="383" y2="{y}" stroke="#dce5f0" stroke-width="18"/>')
    parts.append(f'<line x1="113" y1="{y}" x2="{113+length:.8f}" y2="{y}" stroke="#156d9b" stroke-width="18"/>')
    parts.append(f'<text x="401" y="{y+6}" class="body">{Fraction(1,3**n)}</text>')
parts.append('<text x="112" y="476" class="small">0</text><text x="378" y="476" class="small">1</text>')
parts.append('<text x="44" y="506" class="small">Trace = length. Every nonzero projection still has norm 1.</text>')

x0, x1, y0, y1 = 636, 1100, 194, 454
for k in range(0,9,2):
    y = y0+(y1-y0)*k/8
    label = '1' if k==0 else f'3^(-{k})'
    parts.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" class="grid"/>')
    parts.append(f'<text x="{x0-12}" y="{y+5}" text-anchor="end" class="small">{label}</text>')
for n in range(9):
    x=x0+(x1-x0)*n/8
    parts.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" class="grid"/>')
    parts.append(f'<text x="{x}" y="478" text-anchor="middle" class="small">{n}</text>')
for kind, color in [('trace','#156d9b'),('hilbert','#ba5e15'),('norm','#734b98')]:
    points=[]
    for n in range(9):
        exponent = n if kind=='trace' else n/2 if kind=='hilbert' else 0
        x=x0+(x1-x0)*n/8; y=y0+(y1-y0)*exponent/8
        points.append(f'{x},{y}')
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="3"/>')
    for n in range(9):
        exponent=n if kind=='trace' else n/2 if kind=='hilbert' else 0
        x=x0+(x1-x0)*n/8; y=y0+(y1-y0)*exponent/8
        parts.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{color}"/>')
for x,color,label in [(574,'#156d9b','trace: 3^(-n)'),(754,'#ba5e15','Hilbert: 3^(-n/2)'),(977,'#734b98','map norm: 1')]:
    parts.append(f'<line x1="{x}" y1="507" x2="{x+18}" y2="507" stroke="{color}" stroke-width="3"/>')
    parts.append(f'<text x="{x+25}" y="512" class="small">{label}</text>')
parts.append('''<text x="34" y="563" class="body">HADT6 is attained at x = 1: the Hilbert error tends to zero while the tail-map norm remains one.</text>
<text x="34" y="587" class="small">This geometric rate belongs to the displayed example. General defect matching gives r_n ↓ 0 without a fixed rate.</text>
</svg>''')
svg = '\n'.join(parts)+'\n'
# Explicit presentation attributes keep native SVG renderers faithful as well.
styles = {'title':'font-size="25" font-weight="bold"',
          'head':'font-size="20" font-weight="bold"',
          'body':'font-size="16"', 'small':'font-size="14"',
          'grid':'stroke="#d4dce7" stroke-width="1"'}
for name, attributes in styles.items():
    svg = svg.replace(f'class="{name}"', attributes)
svg = svg.replace('<text ', '<text font-family="Arial,sans-serif" fill="#18253a" ')
svg = re.sub(r'<style>.*?</style>', '', svg)
(ROOT/'defect-exhaustion.svg').write_text(svg,encoding='utf-8')
