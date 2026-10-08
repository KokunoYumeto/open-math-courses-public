"""Weighted normal derivatives of the coefficient oscillator phase: CC0."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,base64,hashlib,html,io,json,math
from PIL import Image,ImageDraw,ImageFont
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--output-dir',type=Path,default=HERE/'out')
p.add_argument('--resources',type=Path,default=HERE.parent/'labelled-geometric-kernel')
a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
font=(a.resources/'fonts/DejaVuSans.ttf').read_bytes();notice=(a.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=2450,1710;INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Weighted normal derivatives of the coefficient phase</title>',
 '<desc>PW.1 to PW.12. A compact weighted normal derivative of the actual coefficient oscillator phase, its completed normal graph identity and an exact two-mode Clifford example. The original-unit graph realization remains unproved.</desc>',
 '<metadata>'+html.escape('Original CC0 drawing.\n'+notice)+'</metadata>',
 '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font).decode()+')}text{font-family:LocalSans}</style>',f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']
def text(x,y,s,size=31,col=INK):
 if size not in fonts:fonts[size]=ImageFont.truetype(io.BytesIO(font),size,layout_engine=ImageFont.Layout.BASIC)
 b=d.textbbox((x,y),s,font=fonts[size],anchor='lt')
 if b[0]<0 or b[1]<0 or b[2]>W or b[3]>H:overflow.append([s,list(b)])
 d.text((x,y),s,font=fonts[size],fill=col,anchor='lt');svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def box(x,y,w,h,fill='white',col='#c9d5e3'):
 d.rectangle((x,y,x+w,y+h),fill=fill,outline=col,width=3);svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{col}" stroke-width="3"/>')
def line(points,col=BLUE,width=4,dashed=False):
 d.line(points,fill=col,width=width)
 svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{col}" stroke-width="{width}"'+(' stroke-dasharray="10 9"' if dashed else '')+'/>')
def arrow(x,y,xx,yy,col=BLUE):
 line([(x,y),(xx,yy)],col);ang=math.atan2(yy-y,xx-x);pts=[(xx,yy)]+[(xx-17*math.cos(ang+b),yy-17*math.sin(ang+b)) for b in [-.45,.45]]
 d.polygon(pts,fill=col);svg.append('<polygon points="'+' '.join(f'{x:.4f},{y:.4f}' for x,y in pts)+f'" fill="{col}"/>')

text(45,25,'Weighted normal derivatives of the coefficient phase',43)
text(45,91,'PW.1–PW.12. The slow phase W, fast oscillator Cf and actual coefficient algebra A=C0(Y).',29)
box(45,150,1155,410);text(78,184,'One-particle control → Fock control',34)
for y,label in [(254,'Ai,ε=δi qε(κ); Xi,ε=Ai,ε κ → Xi in HS norm'),(327,'Ai,ε = Xi,ε Θf on the completed fast domain'),(400,'Yi,ε = B(Ai,ε) Rf → Yi compact in norm'),(473,'||Yi|| ≤ ||Xi|| ≤ ||Ω δiκ||₂')]:text(78,y,label,29,BLUE if y<400 else GREEN)
box(1240,150,1165,410);text(1273,184,'Compact sign-resolvent sandwich',34)
for y,label in [(254,'Rf=|Cf|⁻¹ off the even vacuum; zero on it'),(327,'Zi,ε = −(1/π) ∫ (Rε,− Yi,ε Rε,− + Rε,+ Yi,ε Rε,+) da'),(400,'Gap √2: integrand norm ≤ 2||Yi,ε||/(2+a²)'),(473,'Zi,ε → Zi compact; ||Zi|| ≤ ||Xi||/√2')]:text(1273,y,label,27,GREEN if y>=400 else BLUE)
box(45,600,2360,180);text(78,631,'The completed normal graph identity — no derivative of Rf is used',34)
text(78,696,'∇i(Wv) = Zi |Cf| v + W ∇iv,  v in the actual joint fast/normal core.  (PW.9)',32,GREEN)
box(45,825,2360,660);text(78,856,'Exact two-mode example: a moving normalized Clifford coefficient vector',34)
text(78,912,'N1=N2=1, total n=2; shift 1+2n=5.  κ(t)=diag((4+sin t)⁻², 1/25), Ω(t)=diag(5+sin t,6).',27)
text(78,965,'Q1=σx⊗I, Q2=σz⊗σx; Qj²=I and Q1Q2+Q2Q1=0.  W(t)=((10+sin t)Q1+11Q2)/√((10+sin t)²+121).',25)
gx,gy,gw,gh=140,1390,880,325
xmin,xmax,ymin,ymax=.61,.73,.68,.8
def xy(x,y):return gx+gw*(x-xmin)/(xmax-xmin),gy-gh*(y-ymin)/(ymax-ymin)
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
for value in [.62,.66,.70]:
 xx=xy(value,ymin)[0];line([(xx,gy-gh),(xx,gy)],'#dbe5ee',1);text(xx-20,gy+12,str(value),21,GRAY)
for value in [.70,.74,.78]:
 yy=xy(xmin,value)[1];line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(70,yy-14,str(value),21,GRAY)
points=[]
for index in range(101):
 t=-1+2*index/100;c1=10+math.sin(t);scale=math.sqrt(c1*c1+121)
 points.append(xy(c1/scale,11/scale))
line(points,BLUE,5)
x0,y0=10/math.sqrt(221),11/math.sqrt(221)
xx,yy=xy(x0,y0);d.ellipse((xx-7,yy-7,xx+7,yy+7),fill=GREEN)
svg.append(f'<circle cx="{xx}" cy="{yy}" r="7" fill="{GREEN}"/>')
dx,dy=121/(221*math.sqrt(221)),-110/(221*math.sqrt(221))
end=xy(x0+dx,y0+dy);arrow(xx,yy,*end,GREEN)
text(xx-105,yy-44,'t=0; tangent Ẇ',23,GREEN)
text(345,1440,'Q1 coefficient (horizontal); Q2 coefficient (vertical)',24)
text(1180,1058,'At t=0 (PW.12):',31)
for y,label in [(1120,'Cs=√2(10Q1+11Q2); Cf=√2(21Q1+30Q2)'),(1186,'Cf²=2682 I; Ẇ=(121Q1−110Q2)/(221√221)'),(1252,'||B(A)Rf||² = 1/1341 ≤ 1/256 = ||X||²'),(1318,'||Ẇ Rf||² = 121/(221²·2682) ≤ 1/2682'),(1384,'Curve: numerical samples. Matrix/norm checks: exact rationals.')]:text(1180,y,label,27,GREEN if y>=1252 else BLUE)
box(45,1500,2360,140);text(78,1530,'The coefficient phase remains 1A. Its balanced realization at C0(T), inverse-module passage,',28,GREEN)
text(78,1588,'completed physical graph sum and original Bott +1 remain to be constructed.',28,RED)
text(45,1680,'Original CC0 diagram. Proof PW.1–PW.12. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow
def mul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]
def kron(x,y):return [[x[i//len(y)][j//len(y[0])]*y[i%len(y)][j%len(y[0])] for j in range(len(x[0])*len(y[0]))] for i in range(len(x)*len(y))]
def add(x,y):return [[u+v for u,v in zip(a,b)] for a,b in zip(x,y)]
def scale(c,x):return [[c*u for u in row] for row in x]
i2=[[1,0],[0,1]];sx=[[0,1],[1,0]];sz=[[1,0],[0,-1]]
q1=kron(sx,i2);q2=kron(sz,sx);i4=kron(i2,i2);zero=scale(0,i4)
assert mul(q1,q1)==i4 and mul(q2,q2)==i4 and add(mul(q1,q2),mul(q2,q1))==zero
fast=add(scale(21,q1),scale(30,q2));tangent=add(scale(121,q1),scale(-110,q2))
assert scale(2,mul(fast,fast))==scale(2682,i4)
assert mul(tangent,tangent)==scale(121*221,i4)
y2=Q(1,1341);x2=Q(1,256);z2=Q(121,221**2*2682);gap_bound=Q(1,2682)
assert y2<=x2 and z2<=gap_bound and gap_bound==y2/2
checks=dict(schema='weighted-normal-phase-checks/v1',mode_matrices=[q1,q2],clifford_squares_identity=True,clifford_anticommutator_zero=True,
 total_occupation=2,retained_shift=5,slow_coefficients=[10,11],fast_coefficients=[21,30],fast_square=2682,
 tangent_numerator=[121,-110],tangent_denominator='221*sqrt(221)',tangent_norm='11/221',
 weighted_fock_derivative_squared=str(y2),weighted_one_particle_derivative_squared=str(x2),weighted_phase_derivative_squared=str(z2),
 sign_integral_gap_bound_squared=str(gap_bound),all_finite_matrix_and_rational_checks=True,
 curve_samples=101,curve_samples_are_numerical=True,actual_completed_weighted_normal_phase_proved=True,
 derivative_of_fast_inverse_asserted=False,coefficient_identity_algebra='C0(Y)',original_graph_realization_proved=False,
 original_Bott_plus_one_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'weighted-normal-phase.png')
(a.output_dir/'weighted-normal-phase.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
(a.output_dir/'WEIGHTED-PHASE-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outputs=3,exact_clifford_and_rational_checks=True,curve_samples=101,overflows=overflow)))
