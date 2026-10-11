"""Reproduce the interpolation strip and exact constant recurrence (CC0-1.0).

The strip is a schematic with the illustrated value epsilon=1/4. The lower
graph uses actual values c_n=(81/16)**(2**(-n)), not schematic sample values.
Proof locators: sharp-noncommutative-bilinear-inequality, Lemma3.1 and the
complete constant-improvement argument. Human method comparison: Pisier /
Hasegawa, Kyoto lecture notes (2015), section5, pages9-10. No source image
or expression is copied. This figure and its source are original CC0 work.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import math

out = Path(__file__).resolve().with_name('sharp-interpolation-and-constant-iteration.svg')
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="970" viewBox="0 0 760 970" role="img" aria-labelledby="title desc">',
         '<title id="title">Interpolation and the exact improvement of the four-state constant</title>',
         '<desc id="desc">A vertical strip from real part epsilon to 2, with evaluation at 1. The affine boundary weights tend to one half as epsilon tends to zero. Finite third-root averaging and state selection turn C into the square root of C times the form norm. The lower graph plots the exact normalized constants (81/16) to the power 2 to the minus n, decreasing to one.</desc>',
         '<metadata>Original course figure and reproducible source: CC0-1.0.</metadata>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#2b566c"/></marker></defs>',
         '<rect width="760" height="970" fill="#fbfcfe"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#183846} .small{font-size:15px} .body{font-size:18px} .title{font-size:23px;font-weight:700} .formula{font-size:21px}</style>']

def text(x, y, value, cls='body', anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def line(x1,y1,x2,y2,color='#2b566c',dash='',arrow=False):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"' + (f' stroke-dasharray="{dash}"' if dash else '') + (' marker-end="url(#arrow)"' if arrow else '') + '/>')

text(30, 38, 'A strip turns fourth moments into a better constant', 'title')
text(30, 69, 'h(z) = V(f_x(z), f_y(z));  f_x(1) = x', 'formula')
text(30, 98, 'The drawing uses ε = 1/4; the proof allows every 0 < ε < 1.', 'small')
parts.append('<rect x="145" y="125" width="435" height="214" fill="#e4eef6" stroke="#9eb8cb"/>')
line(145,125,145,339);line(580,125,580,339)
# Coordinates implement the actual affine position (1-epsilon)/(2-epsilon).
epsilon=0.25
evaluation_x=145+435*(1-epsilon)/(2-epsilon)
line(evaluation_x,125,evaluation_x,339,color='#bf6c23',dash='6 5')
parts.append(f'<circle cx="{evaluation_x}" cy="231" r="6" fill="#bf6c23"/>')
text(145,365,'Re z = ε',anchor='middle')
text(evaluation_x,365,'Re z = 1',anchor='middle')
text(580,365,'Re z = 2',anchor='middle')
text(30,400,'Left:  |h(ε+it)| ≤ ||V|| ||x||^ε ||y||^ε')
text(30,430,'Right: |h(2+it)| ≤ C P(x)^(1/2) Q(y)^(1/2)')
text(30,462,'θ_left = 1/(2−ε);  θ_right = (1−ε)/(2−ε)', 'formula')
text(30,493,'As ε ↓ 0, both weights tend to 1/2.', 'body')
text(30,524,'Thus |V(x,y)| ≤ √(C ||V||) P(x)^(1/4) Q(y)^(1/4).')
text(30,553,'If x = 0 or y = 0, h = 0; zero boundary bounds use a tolerance.', 'small')

line(30,580,730,580,color='#c9d5dd')
text(30,616,'Finite phases and common states complete the improvement', 'title')
text(30,647,'C_new = √(C ||V||);  c_n = C_n/||V|| = (81/16)^(2^(−n))', 'formula')
text(30,674,'Exact data below; V ≠ 0. The limiting state quadruple comes from compactness.', 'small')
left,right,top,bottom=92,697,705,891
def xy(n,c):return left+(right-left)*n/6,bottom-(bottom-top)*(c-1)/(81/16-1)
for c in [1,2,3,4,81/16]:
    _,y=xy(0,c);line(left,y,right,y,color='#d4dee5',dash='3 5');text(left-12,y+5, '81/16' if c==81/16 else str(c),'small','end')
line(left,bottom,left,top-10,arrow=True);line(left,bottom,right+12,bottom,arrow=True)
values=[(81/16)**(2**(-n)) for n in range(7)]
coords=[xy(n,c) for n,c in enumerate(values)]
parts.append('<polyline points="'+' '.join(f'{x:.6f},{y:.6f}' for x,y in coords)+'" fill="none" stroke="#bf6c23" stroke-width="3"/>')
for n,(x,y) in enumerate(coords):
    parts.append(f'<circle cx="{x:.6f}" cy="{y:.6f}" r="4" fill="#bf6c23"/>')
    text(x,bottom+23,str(n),'small','middle')
text(left,top-18,'c_n','small');text(right+15,bottom+23,'n','small')
text(30,949,'Proof: polar powers → three lines → finite third-root average → state selection.', 'small')
parts.append('</svg>')
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
assert all(values[i+1]<values[i] for i in range(6))
assert all(abs(values[i+1]**2-values[i]) < 1e-12 for i in range(6))
assert math.isclose((2-1)/(2-epsilon)+(1-epsilon)/(2-epsilon),1)
print(out)
