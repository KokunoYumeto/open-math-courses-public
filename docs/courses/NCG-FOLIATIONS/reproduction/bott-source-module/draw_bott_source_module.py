"""A concrete ordinary Bott-source module: original CC0."""
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
W,H=2450,1580
INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<title>An exact Bott-source representation is not yet an inverse cycle</title>',
'<desc>BSM.1 to BSM.12. A constant ordinary cpc section gives a nondegenerate Stinespring representation and completed parallel normal connection. The zero quotient module is the identity. A central parameter taper can make the positive module zero, so an inverse operator and genuine action still require proof.</desc>',
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


text(45,25,'A concrete ordinary Bott-source module',44)
text(45,92,'BSM.1–BSM.12. An exact left representation and normal connection; the even inverse cycle remains to be constructed.',26)
box(45,155,1135,330)
text(78,185,'The actual ordinary anchored section',32)
text(78,251,'A=C0(X); B=A⊗C; EB=A⊗D',30,BLUE)
text(78,316,'q0:D→C; s0:C→D is even cpc; q0s0=1C',27)
text(78,381,'sB=1A⊗s0 is parallel for the scalar normal core',26,GREEN)
text(78,438,'Equivariance of this section has not been proved',25,RED)
box(1240,155,1165,330)
text(1273,185,'Completed Stinespring module and exact action',30)
text(1273,251,'K0=completion of C⊗s0D; K=A⊗K0',30,BLUE)
text(1273,316,'⟨c⊗d,c′⊗d′⟩=d*s0(c*c′)d′',28)
text(1273,381,'π(a)(c⊗d)=ac⊗d is a genuine *-homomorphism',25,GREEN)
text(1273,438,'π(un)ξ→ξ; actual nondegenerate left B-action',27)
arrow(1188,315,1233,315)
arrow(670,492,670,535);arrow(1830,492,1830,535)
box(45,545,1135,340)
text(78,575,'The exact zero quotient is the identity module',30)
text(78,641,'Q:(c⊗d)⊗a ↦ c q0(d) a',32,BLUE)
text(78,708,'K⊗EB,qB B ≅ B, preserving the left B-action',27,GREEN)
text(78,775,'δi(π(b)u)=π(δib)u+π(b)δiu',28)
text(78,837,'This module identity does not supply an operator F',25,RED)
box(1240,545,1165,340)
text(1273,575,'The positive fibre can vanish',32)
text(1273,641,'χ(t)=1−t; s0′=χs0 is still an even cpc section',27,BLUE)
text(1273,708,'q0s0′=1C  but  h1s0′=0',32,RED)
text(1273,775,'The entire positive Stinespring module is zero',27,RED)
text(1273,837,'The actual KK lift must contain additional data',27)
box(45,945,2360,400)
text(78,975,'Exact finite test: C=C², D=C²⊕M2; quotient onto C²',32)
text(78,1043,'H0=diag(9/25,16/25); H1=1−H0; Φ(c)=c0H0+c1H1',28,BLUE)
text(78,1110,'π(c)=diag(c0I2,c1I2); V rows: (3/5,0), (0,4/5), (4/5,0), (0,3/5)',27)
text(78,1177,'V*V=I2; P=VV*=P*=P²; Φ(c)=V*π(c)V',30,GREEN)
text(78,1244,'Φ(e0)−Φ(e0)²=(144/625)I2 ≠0; π is multiplicative, its compression is not',26,RED)
text(78,1304,'Sixteen exact rational representation products and the isometry/projection/effect identities are retained.',24)
box(45,1400,2360,105)
text(78,1430,'Transport goes to the Stinespring module for sg=αE,g sB αB,g⁻¹; it is not yet an action on the fixed module.',26,RED)
text(45,1540,'Original CC0. BSM.1–BSM.12. Input: actual anchored Bott deformation and section, BA.5, Section11AD.2.',24)
assert not overflow,overflow
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def diag(v):return [[x if i==j else F(0) for j in range(len(v))] for i,x in enumerate(v)]
V=[[F(3,5),F(0)],[F(0),F(4,5)],[F(4,5),F(0)],[F(0),F(3,5)]]
I2=diag([F(1),F(1)]);I4=diag([F(1)]*4);P=mm(V,tr(V))
assert mm(tr(V),V)==I2 and tr(P)==P and mm(P,P)==P
H0=diag([F(9,25),F(16,25)]);H1=diag([F(16,25),F(9,25)])
def pi(c):return diag([c[0],c[0],c[1],c[1]])
def phi(c):return diag([c[0]*F(9,25)+c[1]*F(16,25),c[0]*F(16,25)+c[1]*F(9,25)])
samples=[(F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(2),F(-3))];products=[]
for c in samples:
 assert mm(mm(tr(V),pi(c)),V)==phi(c)
 for e in samples:
  assert mm(pi(c),pi(e))==pi((c[0]*e[0],c[1]*e[1]))
  products.append(dict(c=list(map(str,c)),e=list(map(str,e)),exact_representation_product=True))
assert pi((F(1),F(1)))==I4
square=mm(H0,H0);defect=[[H0[i][j]-square[i][j] for j in range(2)] for i in range(2)]
assert defect==diag([F(144,625)]*2)
checks=dict(schema='ordinary-bott-source-module-finite-checks/v1',exact_isometry=True,exact_selfadjoint_projection=True,exact_compression_samples=4,exact_representation_products=products,positive_effect_diagonals=['9/25','16/25','16/25','9/25'],multiplicative_defect='(144/625)I2',all_fraction_checks=True,zero_quotient_module_identity_proved=True,parallel_normal_connection_proved=True,nondegenerate_left_B_representation_proved=True,positive_module_may_vanish=True,actual_inverse_operator_proved=False,genuine_groupoid_action_on_fixed_module_proved=False,actual_B_source_inverse_class_identified=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'bott-source-module.png',format='PNG',optimize=False,compress_level=9)
(a.output_dir/'bott-source-module.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'BOTT-SOURCE-MODULE-CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(all_fraction_checks=True,exact_representation_products=16,text_canvas_overflows=overflow)))
