"""Exact strict-level populations for A=40, Delta=2/5, W=3."""
from pathlib import Path
from fractions import Fraction as F
from math import floor
ROOT=Path(__file__).resolve().parents[1]
pop=[sum(floor(F(40)-F(2,5)*v)+1==z for v in range(96,108)) for z in range(-2,3)]
assert pop==[2,3,2,3,2]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="920" height="590" viewBox="0 0 920 590" role="img" aria-labelledby="title desc">',
'<title id="title">Strict integer levels and their cumulative counting error</title>',
'<desc id="desc">For A=40 and Delta=2/5, levels minus two through two have populations2,3,2,3,2. Their cumulative errors from mean5/2 alternate between minus1/2 and zero.</desc>',
'<rect width="920" height="590" fill="#fbfaf7"/><g font-family="Georgia,serif" fill="#152b39">',
'<text x="35" y="38" font-size="24">Unequal populations, bounded cumulative error</text>',
'<text x="35" y="71" font-size="18">d(ν) = floor(40 − 2ν/5) + 1.  Retain |d| &lt; 3.</text>',
'<text x="35" y="112" font-size="18">Level d</text>']
for i,z in enumerate(range(-2,3)):
 x=255+135*i
 vals=[v for v in range(96,108) if floor(F(40)-F(2,5)*v)+1==z]
 parts.append(f'<text x="{x}" y="112" font-size="21" text-anchor="middle">{z}</text>')
 for j,v in enumerate(vals):
  y=134+j*38
  parts.append(f'<rect x="{x-41}" y="{y}" width="82" height="31" rx="5" fill="#d8ebe8" stroke="#16736b"/>')
  parts.append(f'<text x="{x}" y="{y+23}" font-size="18" text-anchor="middle">ν = {v}</text>')
 parts.append(f'<text x="{x}" y="284" text-anchor="middle" font-size="21">{len(vals)}</text>')
parts+=['<text x="35" y="157" font-size="18">Integer times</text>',
'<text x="35" y="284" font-size="18">Population a(d)</text>',
'<text x="35" y="330" font-size="18">Cumulative sum of a(d) − 5/2, starting at d = −2</text>']
for y,label in [(385,'0'),(445,'−1/2'),(505,'−1')]:
 parts.append(f'<line x1="210" y1="{y}" x2="840" y2="{y}" stroke="#b8c5cb"/>')
 parts.append(f'<text x="173" y="{y+6}" font-size="18" text-anchor="end">{label}</text>')
acc=F(0);pts=[]
for i,c in enumerate(pop):
 acc+=c-F(5,2);x=255+135*i;y=385-float(acc)*120;pts.append(f'{x},{y}')
 parts.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#204d81"/>')
 parts.append(f'<text x="{x}" y="533" text-anchor="middle" font-size="18">{i-2}</text>')
parts.append('<polyline points="'+' '.join(pts)+'" fill="none" stroke="#204d81" stroke-width="2"/>')
parts+=['<text x="35" y="568" font-size="17">Each prefix error has absolute value ≤ 1; no error accumulates with the number of levels.</text>','</g></svg>']
(ROOT/'figures/lattice-multiplicity.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('figures/lattice-multiplicity.svg')
