"""An exact arithmetic lattice example; outline coordinates use logarithms."""
from pathlib import Path
from math import log
from fractions import Fraction
from check_phase import phase, triangle

root=Path(__file__).resolve().parents[1]
eps=Fraction(1,32768)
pts=triangle(14,1,(1,1),eps)
assert len(pts)==14
def xy(j,l):
    return 100+(j-1)*95, 140+(2-l)*35
def line(x1,y1,x2,y2,extra=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {extra}/>'
def text(x,y,t,extra=''):
    return f'<text x="{x}" y="{y}" {extra}>{t}</text>'
s=log(4782969/32768)
corner=xy(1,1); right=xy(1+s/log(9),1); bottom=xy(1,1-s/log(2))
out=['<svg xmlns="http://www.w3.org/2000/svg" width="800" height="580" viewBox="0 0 800 580" role="img" aria-labelledby="title desc">',
     '<title id="title">An exact low-phase triangle and a marked path</title>',
     '<desc id="desc">Fourteen low-phase lattice points in columns one to three. A path from (1,-6) through (2,-3) to (4,2) leaves the triangle on its second jump. The outline is a continuous schematic boundary; only marked lattice points are states.</desc>',
     '<rect width="800" height="580" fill="#fff"/>',
     '<g font-family="Georgia,serif" font-size="17" fill="#172d3d">',
     text(40,36,'Low-phase positions in one arithmetic triangle','font-size="23"'),
     text(40,65,'n = 14, ξ = 1, ε = 1/32768; corner (1, 1)'),
     text(40,92,'32768 · 9^(j−1) · 2^(1−l) ≤ 4782969, j ≥ 1, l ≤ 1'),
     '<g stroke="#e4e9ec" stroke-width="1">']
for j in range(1,7):
    x,_=xy(j,0);out.append(line(x,125,x,495))
for l in range(-7,4):
    _,y=xy(1,l);out.append(line(85,y,610,y))
out+=['</g>',f'<polygon points="{corner[0]},{corner[1]} {right[0]},{right[1]} {bottom[0]},{bottom[1]}" fill="none" stroke="#526b80" stroke-width="2" stroke-dasharray="7 5"/>']
for j in range(1,7):
    for l in range(-7,4):
        x,y=xy(j,l)
        low=abs(phase(14,1,j,l))<=eps
        assert low == ((j,l) in pts)
        out.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{"#172d3d" if low else "#fff"}" stroke="#718595" stroke-width="1.2"/>')
path=[(1,-6),(2,-3),(4,2)]
coords=' '.join(f'{xy(j,l)[0]},{xy(j,l)[1]}' for j,l in path)
out.append(f'<polyline points="{coords}" fill="none" stroke="#a34416" stroke-width="3"/>')
for j,l in path:
    x,y=xy(j,l);out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#a34416"/>')
out += [text(115,454,'(1, −6)'),text(210,356,'(2, −3)'),text(395,132,'(4, 2): cancelling'),
        text(153,397,'(1, 3)','fill="#a34416"'),text(275,255,'(2, 5)','fill="#a34416"')]
for j in range(1,7):
    x,y=xy(j,-8);out.append(text(x-5,515,str(j)))
for l in (-6,-3,0,1,3):
    x,y=xy(1,l);out.append(text(57,y+6,str(l)))
out += [text(610,515,'pair coordinate j'),text(25,315,'height l','transform="rotate(-90 25 315)"'),
        text(40,552,'Filled lattice points: low-phase. Brown line: one admissible path, not a frequency estimate.'),'</g></svg>']
(root/'figures/phase-triangle.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('Wrote exact example with fourteen low-phase lattice points.')
