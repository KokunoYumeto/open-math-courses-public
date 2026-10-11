"""Exact rational coordinate example; reproducible SVG, not a trajectory plot."""
from pathlib import Path
from fractions import Fraction as F
from html import escape
root=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="430" viewBox="0 0 900 430" role="img" aria-labelledby="title desc">',
'<title id="title">An exact translation of two level supports</title>',
'<desc id="desc">At slope eight fifths, prefix supports 91 through 112 and 93 through 115 fit inside 85 through 118. Adding seven maps them into combined times 92 through 125.</desc>',
'<rect width="900" height="430" fill="#fff"/>',
'<style>text{font-family:Georgia,serif;fill:#172b40;font-size:17px}.small{font-size:15px}.label{font-weight:bold}</style>']
def x(n):return 170+(n-85)*19
def line(a,b,y,color,width=5):
 parts.append(f'<line x1="{x(a)}" y1="{y}" x2="{x(b)}" y2="{y}" stroke="{color}" stroke-width="{width}"/>')
def txt(xp,yp,s,cls=''):
 parts.append(f'<text x="{xp}" y="{yp}" class="{cls}">{escape(s)}</text>')
txt(30,35,'Exact time translation: n = ν + 7','label')
txt(30,61,'Illustrative affine slope λ = 8/5;  δ = 2/5,  A = 40,  W = 5','small')
for a,b,y,color,name in [(85,118,120,'#c9d3df','Allowed ν'),(91,112,175,'#136c79','First level'),(93,115,230,'#91541c','Successor')]:
 line(a,b,y,color,8)
 txt(28,y+6,name)
 for k in range(a,b+1):
  parts.append(f'<circle cx="{x(k)}" cy="{y}" r="3" fill="{color}"/>')
 txt(x(a)-7,y-17,str(a));txt(x(b)-9,y-17,str(b))
line(85,118,335,'#c9d3df',8)
txt(28,341,'Allowed n')
for k in range(85,119):
 parts.append(f'<circle cx="{x(k)}" cy="335" r="3" fill="#8497ab"/>')
for k in [85,91,93,112,115,118]:
 txt(x(k)-8,365,str(k+7))
for k in [91,115]:
 parts.append(f'<path d="M{x(k)} 249 L{x(k)} 317 l-5 -8 m5 8 l5 -8" fill="none" stroke="#476180" stroke-width="1.5"/>')
txt(395,288,'add 7 ↓     ↑ subtract 7')
txt(30,405,'Both original supports are retained; the prescribed window is J = {92, …, 125}.','small')
parts.append('</svg>')
(root/'figures/physical-windows.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
