"""Exact plotted bracket threshold and the proved variable-coefficient example. CC0."""
from pathlib import Path
import html,math
HERE=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="620" viewBox="0 0 1080 620" role="img" aria-labelledby="title desc">',
 '<title id="title">Two normal tails, two inverse calculations</title>',
 '<desc id="desc">The left frequency plot shades kappa greater than or equal to four square root of one plus eta squared and kappa less than or equal to minus that value. The right panel compares pointwise and operator inverse coefficients for exp(i r) D r.</desc>',
 '<rect width="1080" height="620" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#14283a}.title{font-size:26px;font-weight:bold}.head{font-size:21px;font-weight:bold}.body{font-size:18px}.small{font-size:16px}</style>']
def text(x,y,value,cls='body',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(value)}</text>')
text(35,40,'Two normal tails, two inverse calculations','title')
text(260,85,'The same ordered coefficients','head','middle')
cx,cy,sx,sy=260,300,62,14
for sign in [-1,1]:
 pts=[]
 for i in range(241):
  eta=-3+6*i/240;kappa=sign*4*math.sqrt(1+eta*eta)
  pts.append((cx+sx*eta,cy-sy*kappa))
 boundary=' '.join(f'{x:.6f},{y:.6f}' for x,y in pts)
 outer=cy-sign*14*sy
 polygon=f'{pts[0][0]:.6f},{outer:.6f} '+boundary+f' {pts[-1][0]:.6f},{outer:.6f}'
 parts.append(f'<polygon points="{polygon}" fill="#dfedf8"/>')
 parts.append(f'<polyline points="{boundary}" fill="none" stroke="#246497" stroke-width="2.5"/>')
parts.append(f'<path d="M 58 {cy} H 462 M {cx} 100 V 500" stroke="#627180" stroke-width="1.2" fill="none"/>')
text(461,cy-10,'η','body','end');text(cx+10,115,'κ')
for value in [-12,-8,-4,4,8,12]:
 y=cy-sy*value;parts.append(f'<path d="M {cx-4} {y} h 8" stroke="#627180"/>');text(cx-9,y+5,str(value),'small','end')
text(105,119,'positive tail','small');text(105,489,'negative tail','small')
text(260,537,'|κ| ≥ 4√(1 + η²)','head','middle')
text(260,563,'Illustrative threshold; choose the actual','small','middle')
text(260,585,'constant from NI2. See NI5 and NI9.','small','middle')
parts.append('<path d="M 512 80 V 592" stroke="#d5dee5"/>')
text(555,85,'A variable normal coefficient','head')
text(555,130,'P = eⁱʳ Dᵣ     (Exercise 2)')
text(555,195,'Pointwise matrix inverse','head')
text(555,230,'e⁻ⁱʳ κ⁻¹')
text(555,265,'The next coefficient is zero.','small')
text(555,335,'Formal operator inverse','head')
text(555,370,'e⁻ⁱʳ (κ⁻¹ + κ⁻² + κ⁻³ + ⋯)')
text(555,405,'Normal differentiation produces the correction.','small')
text(555,475,'After N terms: P Q_N = 1 − κ⁻ᴺ','body')
text(555,509,'This identity is checked on exp(i κ r).','small')
text(555,555,'Formal inversion alone does not establish','small')
text(555,578,'the half-space mapping or boundary traces.','small')
parts.append('</svg>')
(HERE/'normal-inverse-tails.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Wrote normal-inverse-tails.svg (1080 x 620).')
