"""Exact coordinate diagrams for matrix parity; CC0-1.0, no external artwork."""
from pathlib import Path
import hashlib,json,html
root=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="500" viewBox="0 0 1040 500">',
'<rect width="1040" height="500" fill="#f6f9fc"/>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10" fill="#285670"/></marker></defs>',
'<style>text{font-family:Arial,sans-serif;fill:#19364b;font-size:16px}.title{font-size:20px;font-weight:bold}.small{font-size:14px}.axis{stroke:#8093a4;stroke-width:1.4}.line{stroke:#285670;stroke-width:2.5;fill:none}.orange{stroke:#bd6b20;stroke-width:3;fill:none}</style>']
def text(x,y,s,cls=''):parts.append(f'<text x="{x}" y="{y}" class="{cls}">{html.escape(s)}</text>')
def line(x1,y1,x2,y2,cls='line',arrow=False):parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def dot(x,y,c='#167784'):parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>')
for x in (12,356,700):parts.append(f'<rect x="{x}" y="14" width="328" height="472" rx="12" fill="white" stroke="#d4e0e8"/>')
text(29,47,'Two distinct exchanges','title');text(373,47,'A finite correction chain','title');text(717,47,'Order changes the result','title')
def xy(t,s):return 58+250*t,235-150*s
line(*xy(-.08,0),*xy(1.03,0),'axis');line(*xy(0,-.9),*xy(0,1),'axis');text(312,258,'t');text(42,81,'s')
p=xy(.2,.6);ii=xy(.2,-.6);jj=xy(.8,-.6)
line(*p,*ii,'orange',True);line(*p,*jj,arrow=True)
for pt in (p,ii,jj):dot(*pt)
text(p[0]-38,p[1]-15,'P = (1/5, 3/5)','small');text(ii[0]-35,ii[1]+25,'I P','small');text(jj[0]-15,jj[1]+25,'J P','small')
text(29,398,'J preserves w = t + s/2 = 1/2.');text(29,426,'I changes w to −1/10.');text(29,455,'Fixed set: s = 0.','small')
text(373,89,'s = 1/5,  t = 2/5');text(373,119,'Sample points: t − j s.','small')
def xp(t):return 383+(t+1.2)*162
line(xp(-1.2),241,xp(.45),241,'axis');parts.append(f'<rect x="{xp(-1)}" y="195" width="{xp(.45)-xp(-1)}" height="92" fill="#e5f2f4"/>')
for j in range(9):
 x=xp(.4-.2*j);dot(x,241,'#bd6b20' if j==8 else '#167784')
 if j<8:line(x-6,241,xp(.2-.2*j)+6,241,arrow=True)
 if j in [0,2,7,8]:text(x-12,319 if j in [7] else 300,str(j),'small')
text(376,342,'j = 8 lies beyond the support.','small');text(373,398,'Factors stay in chain order.');text(373,426,'At most K/s terms contribute.');text(373,455,'Shading: support t ≥ −1 in view.','small')
def vec(x,y):return 742+160*x,333-270*y
line(*vec(0,0),*vec(1.55,0),'axis');text(984,354,'x₁');text(716,127,'x₂')
line(*vec(0,-.05),*vec(0,.72),'axis');text(726,354,'0','small')
A=vec(1,0);B=vec(1,.5);D=vec(1.25,.5)
line(*A,*B,'orange',True);line(*B,*D,arrow=True)
for pnt in (A,B,D):dot(*pnt)
text(A[0]-13,A[1]+25,'e₁');text(B[0]-39,B[1]-30,'(1, 1/2)','small');text(D[0]-9,D[1]+26,'(5/4, 1/2)','small')
text(717,86,'s = 1/4');text(717,113,'Rₙ Rₘ e₁  versus  Rₘ Rₙ e₁','small')
text(717,398,'Rₙ e₁ = e₁: first step is zero.','small');text(717,426,'The two endpoints differ.');text(717,455,'Exact matrices: Exercise 3.','small')
parts.append('</svg>');out=root/'matrix-parity.svg';out.write_text('\n'.join(parts),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/matrix-parity.svg','svg_sha256':sha(out),
 'generator_sha256':sha(Path(__file__)),'coordinate_scope':'MP1, MP10 and MP24, with the exact rational points in F0.',
 'external_artwork':False,'licence':'CC0-1.0','actually_inspected':False},indent=2)+'\n','utf-8')
print('Built exact three-panel SVG.')
