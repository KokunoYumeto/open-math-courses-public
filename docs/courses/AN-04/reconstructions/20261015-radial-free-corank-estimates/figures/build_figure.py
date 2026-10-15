"""Reproducible original SVG; all coordinates and scale labels are explicit."""
from pathlib import Path
import hashlib,json,html
ROOT=Path(__file__).resolve().parent.parent
W,H=1100,800
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="1100" height="800" fill="#fff"/>',
'<style>text{font-family:Arial,sans-serif;fill:#193148;font-size:19px}.small{font-size:16px}.head{font-size:24px;font-weight:bold}.axis{stroke:#28495c;stroke-width:2}.grid{stroke:#dbe4e8;stroke-width:1}</style>']
def text(x,y,t,cl=''):
    parts.append(f'<text x="{x}" y="{y}" class="{cl}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#28495c',dash=''):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" stroke-dasharray="{dash}"/>')
text(35,38,'Ordinary coordinates on each band; exact frequency recombination','head')
text(35,80,'1. One illustrative comparison constant: 2','head')
for j in [1,2,3]:
    x=110+j*76;y=320-j*38
    parts.append(f'<rect x="{x-76}" y="{y-95}" width="152" height="190" fill="#23a9a2" opacity=".12" stroke="#16877e" stroke-dasharray="5 4"/>')
    parts.append(f'<rect x="{x-76}" y="{y-76}" width="152" height="152" fill="none" stroke="#16877e"/>')
for j in range(5):
    text(105+j*76,410,str(j),'small')
for j in [-1,0,1,2,3,4,5]:
    text(18,325-j*38,str(j),'small')
line(45,390,465,390);line(45,390,45,115)
text(195,435,'log₂ input radius','small');text(57,110,'log₂ output radius','small')
text(52,460,'Input j ± 1; output plateau j ± 2, support j ± 5/2.','small')
text(52,485,'Finite overlaps; summable tails: RF21–23.','small')
text(560,80,'2. Cubic weights after division by h','head')
rows=[('three nongraph factors','1/3 + 1/3 + 1/3','h⁰ survives'),
      ('one shared factor','1/2 + 1/3 + 1/3','h¹⁄⁶ → 0'),
      ('fourth-order remainder','at least 4/3','h¹⁄³ → 0')]
for i,(a,b,c) in enumerate(rows):
    yy=130+i*99
    text(565,yy,a)
    text(565,yy+29,b,'small')
    text(840,yy+29,c,'small')
text(565,448,'A shared factor is x′ or the frequency increment.','small')
text(565,473,'No shared coordinates are required: n = 0 is allowed.','small')
text(35,520,'3. Sufficient and universal necessary inequalities','head')
px=lambda k:85+k*103
py=lambda m:570-m*78
parts.append(f'<polygon points="{px(0)},{py(0)} {px(8)},{py(-2)} {px(8)},{py(-2.5)} {px(0)},{py(-2.5)}" fill="#d4eee5"/>')
for k in range(0,9,2):
    line(px(k),py(0),px(k),py(-2.5),'#dbe4e8')
    text(px(k)-5,py(0)-12,str(k),'small')
for m in [0,-1,-2]:
    line(px(0),py(m),px(8),py(m),'#dbe4e8')
    text(42,py(m)+5,str(m),'small')
line(px(0),py(0),px(8),py(-2),'#087c5e')
line(px(0),py(0),px(8),py(-8/12),'#a34639','7 5')
text(925,568,'k = corank','small')
text(925,622,'m ≤ −k/12','small')
text(925,646,'necessary','small')
text(600,750,'m ≤ −k/4: sufficient','small')
parts.append(f'<circle cx="{px(2)}" cy="{py(-.5)}" r="5" fill="#087c5e"/>')
text(px(2)+10,py(-.5)+60,'k = 2, n = 0 example','small')
text(35,793,'The gap between the lines is not a proved universal continuity range. RF19, RF34, Exercise X1.','small')
parts.append('</svg>')
svg=ROOT/'figures/radial-free-corank.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
v={'schema':'AN04-radial-free-corank-figure/v1','svg':'figures/radial-free-corank.svg',
 'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),'width':W,'height':H,
 'analytic_claims':'Exact exponent and threshold diagram; first panel explicitly a comparison-constant-two schematic.',
 'coordinates':{'corank_range':[0,8],'order_range':[-2.5,0],'sufficient_slope':-.25,'necessary_slope':-1/12,
                'shared_weight':.5,'nongraph_weight':1/3},
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(v,indent=2)+'\n','utf-8')
print(json.dumps({'svg':svg.name,'bytes':svg.stat().st_size}))
