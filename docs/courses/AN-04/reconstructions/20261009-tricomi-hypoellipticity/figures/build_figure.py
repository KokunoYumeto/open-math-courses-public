"""Exact normal envelopes at four Tricomi scales; no PDE solution is sampled."""
from pathlib import Path
import hashlib,json,math,html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'figures/tricomi-normal-layers.svg'
colors=['#235b8a','#b24628','#28704c','#78529a']
vals=[(1,1),(8,4),(27,9),(64,16)]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="590" viewBox="0 0 1040 590" role="img" aria-labelledby="title desc">',
 '<title id="title">Normal layers at the elliptic Tricomi boundary</title>',
 '<desc id="desc">Four exact smooth envelopes in logarithmic normal distance, followed by their common linear rescaling. These are test functions, not computed Airy solutions.</desc>',
 '<rect width="1040" height="590" fill="#fff"/>']
def text(x,y,t,size=16,color='#183447',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#b7c4ca',dash=''):
 parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" fill="none"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def bump(t):
 return math.exp(4-1/((t-1)*(2-t))) if 1<t<2 else 0.
text(30,35,'The Tricomi layer: normal width λ⁻²ᐟ³',25)
text(30,66,'Exact envelopes of compact test packets; the tangential oscillation is omitted.',17)
text(40,106,'Physical normal distance',20)
text(575,106,'One profile after rescaling',20)
left,right,top,bottom=55,490,155,405
left2,right2=580,1005
xp=lambda x:left+(math.log2(x)+4.4)/5.6*(right-left)
yp=lambda y:bottom-y*(bottom-top)
xq=lambda t:left2+t/2.3*(right2-left2)
for v in [0,.5,1]:
 for lo,hi in [(left,right),(left2,right2)]:line(lo,yp(v),hi,yp(v),dash='3 4')
 text(46,yp(v)+5,str(v),14,anchor='end')
text(45,139,'envelope',14)
for value,label in [(1/16,'1/16'),(1/8,'1/8'),(1/4,'1/4'),(1/2,'1/2'),(1,'1'),(2,'2')]:
 pos=xp(value);line(pos,bottom,pos,bottom+6);text(pos,bottom+25,label,14,anchor='middle')
for value in [0,.5,1,1.5,2]:
 pos=xq(value);line(pos,bottom,pos,bottom+6);text(pos,bottom+25,str(value),14,anchor='middle')
for j,(lam,q) in enumerate(vals):
 points=[(1+k/500, bump(1+k/500)) for k in range(501)]
 path=' '.join(('M' if k==0 else 'L')+f'{xp(t/q):.4f},{yp(v):.4f}' for k,(t,v) in enumerate(points))
 parts.append(f'<path d="{path}" fill="none" stroke="{colors[j]}" stroke-width="2.5"/>')
 for t in [1,2]:
  parts.append(f'<circle cx="{xp(t/q)}" cy="{bottom}" r="3" fill="{colors[j]}"/>')
 legend_x=40+j*250
 line(legend_x,505,legend_x+25,505,colors[j])
 text(legend_x+33,511,f'λ = {lam}; width = 1/{q}',15)
path=' '.join(('M' if k==0 else 'L')+f'{xq(k*2.3/700):.4f},{yp(bump(k*2.3/700)):.4f}' for k in range(701))
parts.append(f'<path d="{path}" fill="none" stroke="#183447" stroke-width="3"/>')
text(795,145,'All four rescaled profiles coincide.',15,anchor='middle')
text((left+right)/2,460,'x > 0  (logarithmic axis)',17,anchor='middle')
text((left2+right2)/2,460,'t = λ²ᐟ³ x  (linear axis)',17,anchor='middle')
text(35,550,'Nonzero where λ⁻²ᐟ³ < x < 2λ⁻²ᐟ³. The boundary x = 0 is outside the logarithmic axis.',16)
text(35,577,'Both −∂ₓ² and the principal term λ²x scale as λ⁴ᐟ³. See TH25 and its complete solution.',16)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':OUT.relative_to(ROOT).as_posix(),'svg_sha256':sha(OUT),'generator_sha256':sha(Path(__file__)),
 'exact_formula':'phi(t)=exp(4-1/((t-1)(2-t))) on 1<t<2, zero otherwise; phi(lambda^(2/3)*x)',
 'parameters':[{'lambda':l,'normal_scale':q,'support_endpoints':[f'1/{q}',f'2/{q}']} for l,q in vals],
 'axes':'First panel log2 normal distance x, second panel linear t=lambda^(2/3)*x; vertical normalized envelope.',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'numerical_PDE_solution_claimed':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg_sha256':record['svg_sha256'],'profiles':len(vals)}))
