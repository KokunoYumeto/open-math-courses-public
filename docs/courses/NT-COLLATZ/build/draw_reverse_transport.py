"""Reproducible exact interval geometry for Theorem 3; not an actual fibre."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="360" viewBox="0 0 440 360" role="img" aria-labelledby="title desc">',
'<title id="title">Clipping the reverse interval to its source shell</title>',
'<desc id="desc">The shell has integer sources 8 through 15. With reverse scale 15 and defect bound one third, the candidate interval is 10 through 15. Six integers is an interval bound, not a claim about actual Collatz occupancy.</desc>',
'<rect width="440" height="360" fill="white"/>',
'<g font-family="Arial,sans-serif" fill="#172c38">',
'<text x="22" y="32" font-size="19" font-weight="bold">One source shell and one interval</text>',
'<text x="22" y="61" font-size="16">M = 3, A = 15, ε = 1/3</text>',
'<rect x="26" y="96" width="384" height="52" rx="4" fill="#e5edf2"/>',
'<text x="28" y="89" font-size="15">Source shell [8, 16)</text>']
x=lambda n:28+47*(n-8)
for n in range(8,17):
    svg.append(f'<circle cx="{x(n)}" cy="122" r="5" fill="{("#fff" if n==16 else "#526878")}" stroke="#526878" stroke-width="2"/>')
    svg.append(f'<text x="{x(n)}" y="171" text-anchor="middle" font-size="16">{n}</text>')
svg+=['<text x="22" y="204" font-size="15">Reverse interval [(1 − ε)A, A] = [10, 15]</text>',
f'<line x1="{x(10)}" y1="231" x2="{x(15)}" y2="231" stroke="#13796d" stroke-width="5"/>']
for n in range(10,16):
    svg.append(f'<circle cx="{x(n)}" cy="231" r="6" fill="#13796d"/>')
svg+=['<text x="22" y="275" font-size="17">At most 1 + floor((16 − 1)/3) = 6 sources</text>',
'<text x="22" y="310" font-size="15">The dots count interval candidates.</text>',
'<text x="22" y="333" font-size="15">They are not six verified paths with one tag.</text>',
'</g></svg>']
(ROOT/'figures/reverse-fibre.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
print('Wrote exact interval figure.')
