"""Draw the exact normal support wedge and the ordered scalar factorization."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,html
ROOT=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="660" viewBox="0 0 1200 660" role="img" aria-labelledby="title desc">',
 '<title id="title">Compact logarithmic kernels and one scalar test</title>',
 '<desc id="desc">The exact support wedge y over two at most x at most two y, zero at most y at most one, includes the boundary corner. The other panel gives the input cutoff, logarithmic unitary, positive multiplier and bounded quotient in their actual order.</desc>',
 '<style>text{font-family:Arial,sans-serif;fill:#17314b} .title{font-size:25px;font-weight:bold}.head{font-size:21px;font-weight:bold}.body{font-size:18px}.small{font-size:16px}.axis{stroke:#17314b;stroke-width:2}.grid{stroke:#dce3ea;stroke-width:1}.box{fill:#f3f7fa;stroke:#8fa3b6;stroke-width:1.5}</style>',
 '<rect width="1200" height="660" fill="white"/>',
 '<text x="40" y="43" class="title">Compact logarithmic kernels and one scalar source test</text>',
 '<text x="40" y="84" class="head">Exact allowed normal support</text>',
 '<text x="650" y="84" class="head">The full factorization, in order</text>']
def txt(x,y,text,cls='small',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(text)}</text>')
def line(x1,y1,x2,y2,cls='grid',extra=''):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" {extra}/>')
def coord(y,x):return float(90+F(390)*y),float(530-F(180)*x)
for xv in [F(0),F(1,2),F(1),F(3,2),F(2)]:
 x0,y0=coord(F(0),xv);x1,y1=coord(F(11,10),xv);line(x0,y0,x1,y1);txt(76,y0+5,str(float(xv)).rstrip('0').rstrip('.') if xv else '0',anchor='end')
for yv in [F(0),F(1,2),F(1)]:
 x0,y0=coord(yv,F(0));x1,y1=coord(yv,F(11,5));line(x0,y0,x1,y1);txt(x0,555,str(float(yv)).rstrip('0').rstrip('.') if yv else '0',anchor='middle')
vertices=[(F(0),F(0)),(F(1),F(1,2)),(F(1),F(2))]
points=' '.join(f'{coord(y,x)[0]},{coord(y,x)[1]}' for y,x in vertices)
parts.append(f'<polygon points="{points}" fill="#d0e5f5" stroke="#2878b7" stroke-width="2.5"/>')
line(90,530,537,530,'axis');line(90,530,90,125,'axis')
parts.append('<circle cx="90" cy="530" r="5" fill="#bc4d37"/>')
txt(90,120,'x: output','body');txt(355,584,'y: input','body')
txt(296,260,'x = 2y','body');txt(315,494,'x = y/2','body')
txt(489,151,'y = 1','small')
txt(40,622,'The corner is retained. Shading gives support bounds,','small')
txt(40,645,'not nonzero kernel values or a computed solution.','small')
labels=[('1. Localize the actual input','χf; Tχ = T on the complete kernel'),
 ('2. Apply the L2 unitary','g(v,z) = exp(v/2) χf(exp(v),z)'),
 ('3. Apply one positive multiplier','q(D)g; compact difference kernel'),
 ('4. Apply the bounded quotient','B = Op(a/q); uniform finite-derivative bound')]
for i,(heading,body) in enumerate(labels):
 yy=115+i*112
 parts.append(f'<rect x="650" y="{yy}" width="510" height="81" rx="8" class="box"/>')
 txt(670,yy+29,heading,'body');txt(670,yy+58,body)
 if i<3:
  line(905,yy+82,905,yy+102,'axis');parts.append(f'<path d="M900 {yy+97} L905 {yy+104} L910 {yy+97}" fill="none" stroke="#17314b" stroke-width="2"/>')
txt(660,594,'𝒰Tf = B q(D) 𝒰(χf)','head')
txt(660,629,'‖Tf‖₂ ≤ C ‖𝒰⁻¹q(D)𝒰(χf)‖₂','body')
parts.append('</svg>')
svg=ROOT/'scalar-logarithmic-test.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
record={'svg':'figures/'+svg.name,'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'coordinate_convention':'horizontal y=input normal; vertical x=output normal',
 'exact_vertices':[[str(y),str(x)] for y,x in vertices],
 'ratio_bounds':['1/2','2'],'input_normal_bound':'1','output_normal_bound':'2',
 'map_order':['input cutoff','unitary logarithmic density','positive Fourier multiplier','bounded quotient operator'],
 'kernel_value_plot':False,'schematic_factorization':True,'actually_inspected':False}
(ROOT.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure':svg.name,'support_vertices':record['exact_vertices']}))
