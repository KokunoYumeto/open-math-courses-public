"""Exact mixed-metric ellipses. Original CC0 figure source; no external assets."""
from pathlib import Path
import html

HERE=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="620" viewBox="0 0 1080 620" role="img" aria-labelledby="title desc">',
       '<title id="title">Tangential and full-frequency gains</title>',
       '<desc id="desc">Exact unit ellipses of the mixed frequency metric, with semiaxes one and nine at frequency zero comma eight, and nine and nine at frequency eight comma zero. Both panels have twenty pixels per increment unit.</desc>',
       '<rect width="1080" height="620" fill="white"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#14283a}.title{font-size:27px;font-weight:bold}.head{font-size:21px;font-weight:bold}.label{font-size:18px}.small{font-size:16px}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(value)}</text>')
text(40,42,'The two frequency gains have different meanings','title')
for cx, eta, kappa, T,R in [(270,0,8,1,9),(800,8,0,9,9)]:
    cy=310; scale=20
    text(cx,85,f'Frequency (η, κ) = ({eta}, {kappa})','head','middle')
    text(cx,112,f'T = {T},  R = {R}','label','middle')
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{T*scale}" ry="{R*scale}" fill="#e4f0fa" stroke="#23649b" stroke-width="2.5"/>')
    parts.append(f'<path d="M {cx-208} {cy} H {cx+208} M {cx} {cy+194} V {cy-194}" stroke="#617080" stroke-width="1.2" fill="none"/>')
    for q in [-9,-1,1,9]:
        parts.append(f'<path d="M {cx+q*scale} {cy-4} v 8 M {cx-4} {cy-q*scale} h 8" stroke="#617080"/>')
    text(cx+204,cy-12,'δη','label','end');text(cx+9,cy-184,'δκ')
    text(cx+T*scale+8,cy+25,f'T = {T}','small')
    text(cx+10,cy-R*scale+26,f'R = {R}','small')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#14283a"/>')
    text(cx,530,f'T⁻¹ = {1 if T==1 else "1/9"}     R⁻¹ = 1/9','head','middle')
text(540,570,'Unit metric ellipse: (δη/T)² + (δκ/R)² = 1','label','middle')
text(540,605,'Equal coordinate scale in both panels. See MB9, MB18–MB19 and Exercise 1.','small','middle')
parts.append('</svg>')
(HERE/'mixed-frequency-scales.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Wrote exact mixed-frequency-scales.svg (1080 × 620).')
