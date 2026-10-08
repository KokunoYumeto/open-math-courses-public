"""Genuine regular induction and the proper quotient cutoff: original CC0."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,html,io,json,math
from PIL import Image,ImageDraw,ImageFont
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--output-dir',type=Path,default=HERE/'out')
p.add_argument('--resources',type=Path,default=HERE.parent/'labelled-geometric-kernel')
a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
font=(a.resources/'fonts/DejaVuSans.ttf').read_bytes()
notice=(a.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=2450,1590
INK,BLUE,GREEN,RED='#17283c','#17638d','#286d49','#b64932'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<title>Regular induction retains the source action and the quotient identity submodule</title>',
'<desc>RSM.1 to RSM.16. Exact two-arrow induction of a non-equivariant cpc section. The regular quotient retains the coefficient action, and its proper cutoff gives an equivariant identity submodule. This does not supply the inverse operator or lift the quotient projection.</desc>',
'<metadata>'+html.escape('Original CC0 figure.\n'+notice)+'</metadata>',
'<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font).decode()+')}text{font-family:LocalSans}</style>',
f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']
def text(x,y,s,size=30,col=INK):
 if size not in fonts:fonts[size]=ImageFont.truetype(io.BytesIO(font),size,layout_engine=ImageFont.Layout.BASIC)
 b=d.textbbox((x,y),s,font=fonts[size],anchor='lt')
 if b[0]<0 or b[1]<0 or b[2]>W or b[3]>H:overflow.append([s,list(b)])
 d.text((x,y),s,font=fonts[size],fill=col,anchor='lt')
 svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def box(x,y,w,h):
 d.rectangle((x,y,x+w,y+h),fill='white',outline='#c9d5e3',width=3)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#c9d5e3" stroke-width="3"/>')
def line(points,col=BLUE,width=4):
 d.line(points,fill=col,width=width)
 svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{col}" stroke-width="{width}"/>')
def arrow(x,y,xx,yy,col=BLUE):
 line([(x,y),(xx,yy)],col)
 angle=math.atan2(yy-y,xx-x)
 points=[(xx,yy)]+[(xx-17*math.cos(angle+b),yy-17*math.sin(angle+b)) for b in [-.45,.45]]
 d.polygon(points,fill=col)
 svg.append('<polygon points="'+' '.join(f'{x:.4f},{y:.4f}' for x,y in points)+f'" fill="{col}"/>')
text(45,25,'A genuine regular source action; an identity submodule in the quotient',41)
text(45,92,'RSM.1–RSM.16. Full completion and actual arrow action. The inverse Kasparov operator still requires a construction.',26)
box(45,155,1135,360);box(1240,155,1165,360)
text(78,185,'The ordinary section is not equivariant',31)
text(78,251,'H=Z/2={e,a}; a swaps W={0,1}; B=C²',28,BLUE)
text(78,316,'E=C²⊕M2; a swaps C² and fixes M2',28)
text(78,381,'H0=diag(9/25,16/25); H1=1−H0',28)
text(78,448,'αaE s(e0)−s(αaB e0): diag(−7/25,7/25)',26,RED)
text(1273,185,'Regular induction has exact covariance',31)
text(1273,251,'Row e: π(b)=diag(b0I2,b1I2)',29,BLUE)
text(1273,316,'Row a: π(αab)=diag(b1I2,b0I2)',29,BLUE)
text(1273,381,'Ua swaps the two four-dimensional rows',27)
text(1273,448,'Ua²=1; Ua Π(b) Ua=Π(αab)',30,GREEN)
arrow(1188,330,1233,330)
box(45,575,2360,555)
text(78,605,'The quotient is regular; the cutoff selects the equivariant identity submodule',31)
text(78,673,'Qregular: RE(K)⊗E,q B → LH(B);  (b y)(g)=b y(g)',29,BLUE)
text(78,739,'Ua y(g)=αaB(y(a⁻¹g)): both the arrow coordinate and the coefficient transform',27)
text(78,811,'Cutoff c=(9/25,16/25); c(w)+c(aw)=1',29)
text(78,882,'At w=0:  v=(3/5,4/5)',29,BLUE)
text(1273,882,'At w=1:  v=(4/5,3/5)',29,BLUE)
text(78,944,'p(0)=(1/25)[ 9  12 ; 12  16 ]',28,GREEN)
text(1273,944,'p(1)=(1/25)[ 16  12 ; 12  9 ]',28,GREEN)
arrow(965,951,1235,951,GREEN)
text(995,903,'J p(0) J',24,GREEN)
text(78,1010,'v*v=1; p=vv*=p*=p²; p LH(B)≅B with its genuine coefficient action',29,GREEN)
text(78,1075,'b p is compact after source localization. The quotient projection has not been lifted.',26,RED)
box(45,1190,1135,275);box(1240,1190,1165,275)
text(78,1220,'No equivariant shared centre in this E',28)
text(78,1285,'A central matrix projection is 0 or I2',27)
text(78,1345,'Swap covariance would equate complements',25,RED)
text(78,1410,'The proper cutoff belongs to the quotient',26)
text(1273,1220,'Module covariance does not supply the inverse',28)
text(1273,1285,'s′=(1−t)s retains the zero quotient',27)
text(1273,1345,'At t=1 the positive induced module is zero',26,RED)
text(1273,1410,'An odd lift operator and normal domains remain',25)
text(45,1510,'Exact finite illustration: 16 representation products, 4 covariances, 2 cutoff projections, full quotient action.',25)
text(45,1552,'Original CC0. Proof: Section 11AY, RSM.1–RSM.16. No inverse Kasparov class is claimed by the diagram.',23)
assert not overflow,overflow
def mm(A,B):
 return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def diag(v):return [[x if i==j else F(0) for j in range(len(v))] for i,x in enumerate(v)]
def mat(v):return [[str(x) for x in row] for row in v]
def pi(c):return diag([c[0]]*2+[c[1]]*2+[c[1]]*2+[c[0]]*2)
U=[[F(int((i+4)%8==j)) for j in range(8)] for i in range(8)]
I8=diag([F(1)]*8);assert mm(U,U)==I8 and tr(U)==U
samples=[(F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(2),F(-3))]
products=[];covariances=[]
for c in samples:
 assert mm(mm(U,pi(c)),U)==pi((c[1],c[0]))
 covariances.append(dict(b=list(map(str,c)),covariance=True))
 for e in samples:
  assert mm(pi(c),pi(e))==pi((c[0]*e[0],c[1]*e[1]))
  products.append(dict(b=list(map(str,c)),d=list(map(str,e)),exact_product=True))
J=[[F(0),F(1)],[F(1),F(0)]]
v0=[[F(3,5)],[F(4,5)]];v1=mm(J,v0)
P0=mm(v0,tr(v0));P1=mm(v1,tr(v1))
for v,P in [(v0,P0),(v1,P1)]:
 assert mm(tr(v),v)==[[F(1)]] and tr(P)==P and mm(P,P)==P
assert mm(mm(J,P0),J)==P1
Qproj=[[F(0)]*4 for i in range(4)]
for w,P in enumerate([P0,P1]):
 for r in range(2):
  for s in range(2):Qproj[2*r+w][2*s+w]=P[r][s]
V=[[v0[0][0],F(0)],[F(0),v1[0][0]],[v0[1][0],F(0)],[F(0),v1[1][0]]]
Qa=[[F(int((1-i//2)*2+(1-i%2)==j)) for j in range(4)] for i in range(4)]
assert mm(V,tr(V))==Qproj and mm(tr(V),V)==diag([F(1)]*2)
assert mm(Qa,V)==mm(V,J) and mm(mm(Qa,Qproj),Qa)==Qproj
for c in samples:
 Cb=diag([c[0],c[1]]*2)
 assert mm(Cb,V)==mm(V,diag(list(c)))
 assert mm(Cb,Qproj)==mm(Qproj,Cb)
checks=dict(schema='regular-bott-source-exact-checks/v1',
 exact_representation_products=products,exact_covariances=covariances,
 source_section_discrepancy=['-7/25','7/25'],cutoff_vectors=[mat(v0),mat(v1)],
 cutoff_projections=[mat(P0),mat(P1)],quotient_isometry=mat(V),
 quotient_projection=mat(Qproj),quotient_action=mat(Qa),
 exact_unitary_action=True,exact_quotient_covariance=True,
 genuine_regular_module_action_proved=True,nondegenerate_B_source_action_proved=True,
 identity_quotient_submodule_proved=True,whole_quotient_identified_with_identity=False,
 quotient_projection_lift_proved=False,actual_inverse_operator_proved=False,
 positive_taper_module_may_vanish=True,all_fraction_checks=True,
 canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'regular-bott-source.png',format='PNG',optimize=False,compress_level=9)
(a.output_dir/'regular-bott-source.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'REGULAR-BOTT-SOURCE-CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(exact_products=len(products),exact_covariances=len(covariances),quotient_covariance=True,overflows=overflow)))
