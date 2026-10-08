"""A coefficient auxiliary with normally controlled resolvents: CC0."""
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
 '<title>A coefficient auxiliary with normally controlled resolvents</title>',
 '<desc>MR.1 to MR.16. The slow phase and fast squared magnitude give an actual regular coefficient auxiliary with compact normal resolvent derivatives and a completed normal-domain rule. The balanced original-unit realization remains unproved.</desc>',
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


text(45,25,'A coefficient auxiliary with normally controlled resolvents',42)
text(45,91,'MR.1–MR.16: L=W H, H=Cf². Actual completed coefficient field A=C0(Y); even vacuum retained.',29)
box(45,150,1155,390);text(78,183,'Phase control and fast magnitude',34)
for y,label in [(250,'W = slow sign; H = fast oscillator square'),(316,'W H = H W; Dom L = Dom H; |L| = H'),(382,'R±(λ) = (W H ∓ iλ)(H²+λ²)⁻¹'),(448,'rε=Hε⁻¹ᐟ² off vacuum:  ||rε−r|| ≤ ε/√2')]:text(78,y,label,29,BLUE)
box(1240,150,1165,390);text(1273,183,'Completed normal derivative',34)
for y,label in [(250,'Phase term: ≤ ||Ω δiκ||₂/(2√λ)'),(316,'Magnitude rows: ||Pε||≤½, ||Qε||≤1/(2√λ)'),(382,'δiR± compact; bound (||δiκ||+½||Ωδiκ||₂)/√λ'),(448,'∇i(R±v) = Bi,±v + R±∇iv on Dom ∇i')]:text(1273,y,label,28,GREEN)
box(45,585,2360,165);text(78,617,'Why the limits close: rε → r in norm; Q rows → compact in norm; P rows → strongly with adjoints.',29)
text(78,684,'Compact multiplication gives the actual inverse-derivative norm limit; the closed connection gives its domain rule.',28,GREEN)
box(45,795,2360,675);text(78,827,'Two-mode circle example: exact resolvent derivatives and the uniform decay bound',34)
text(78,884,'At t=0: H=2682 I, Ḣ=672 I, ||Ẇ||=11/221; δκ=diag(−1/32,0), Ωδκ=diag(−5/32,0).',28)
text(78,944,'||Ṙ±(λ)||² = [672²+2682²·121/221²]/(2682²+λ²)²  ≤ 49/(4096λ).  Source occupation shift: five.',27)
gx,gy,gw,gh=145,1375,1370,345
ymin,ymax=-5,math.log10(.2)
def xy(lam,value):return gx+gw*math.log2(lam)/16,gy-gh*(math.log10(value)-ymin)/(ymax-ymin)
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
for value in [.00001,.0001,.001,.01,.1]:
 yy=xy(1,value)[1];line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(51,yy-13,format(value,'.5g'),21,GRAY)
for lam in [1,16,256,4096,65536]:
 xx=xy(lam,.00001)[0];line([(xx,gy-gh),(xx,gy)],'#dbe5ee',1);text(xx-22,gy+12,str(lam),21,GRAY)
variance=Q(672**2)+Q(2682**2*121,221**2);constant=Q(7,64)
curve=[]
for index in range(101):
 lam=2**(16*index/100);value=math.sqrt(lam*float(variance))/(2682**2+lam**2)
 assert 0<value<=float(constant)
 curve.append(xy(lam,value))
line(curve,BLUE,5)
line([xy(1,float(constant)),xy(65536,float(constant))],GREEN,4)
text(1620,1050,'Green: theorem bound 7/64',29,GREEN)
text(1620,1120,'Blue: √λ ||Ṙ±(λ)|| in this example',26,BLUE)
text(1620,1190,'Both axes are logarithmic',27)
text(1620,1260,'Compact derivative limit is proved,',27)
text(1620,1309,'rather than inferred from samples',27)
text(500,1440,'Resolvent parameter λ (log scale); vertical quantity √λ ||Ṙ±(λ)|| (log scale)',23)
box(45,1510,2360,135);text(78,1538,'The actual coefficient auxiliary has class 1A. Balanced realization at C0(T), inverse-module passage,',27,GREEN)
text(78,1593,'completed physical graph sum and original Bott +1 remain to be constructed.',28,RED)
text(45,1680,'Original CC0 diagram. Proof MR.1–MR.16. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow
def mul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]
def kron(x,y):return [[x[i//len(y)][j//len(y[0])]*y[i%len(y)][j%len(y[0])] for j in range(len(x[0])*len(y[0]))] for i in range(len(x)*len(y))]
def add(x,y):return [[u+v for u,v in zip(a,b)] for a,b in zip(x,y)]
def scale(c,x):return [[c*u for u in row] for row in x]
i2=[[1,0],[0,1]];sx=[[0,1],[1,0]];sz=[[1,0],[0,-1]]
q1=kron(sx,i2);q2=kron(sz,sx);i4=kron(i2,i2)
wn=add(scale(10,q1),scale(11,q2));vn=add(scale(11,q1),scale(-10,q2))
assert mul(wn,wn)==scale(221,i4) and mul(vn,vn)==scale(221,i4)
assert add(mul(wn,vn),mul(vn,wn))==scale(0,i4)
assert 4*21*8==672 and Q(1,32)+Q(5,64)==constant
samples=[]
for lam in [1,4,16,64,256,1024,2682,4096,16384,65536]:
 derivative2=variance/(2682**2+lam**2)**2;bound2=constant**2/lam
 assert derivative2<=bound2
 alpha=Q(672*(lam**2-2682**2),(2682**2+lam**2)**2)
 beta2=Q(2682**2*121,221**2*(2682**2+lam**2)**2)
 gamma=Q(2*lam*2682*672,(2682**2+lam**2)**2)
 assert alpha**2+beta2+gamma**2==derivative2
 samples.append(dict(lambda_value=lam,derivative_norm_squared=str(derivative2),proved_bound_squared=str(bound2),exact_inverse_derivative_identity_checked=True,exact_rational_bound_checked=True))
checks=dict(schema='fast-magnitude-resolvent-checks/v1',mode_matrices=[q1,q2],normalized_phase_numerator=wn,normalized_tangent_numerator=vn,
 clifford_phase_and_tangent_squares=221,clifford_phase_tangent_anticommutator_zero=True,
 total_occupation=2,retained_shift=5,fast_square=2682,fast_square_derivative=672,
 phase_derivative_norm='11/221',normal_kappa_derivative_norm='1/32',weighted_normal_derivative_hs_norm='5/32',
 normal_resolvent_bound_constant=str(constant),inverse_derivative_numerator=str(variance),exact_integer_samples=samples,
 numerical_curve_samples=101,all_matrix_and_exact_fraction_checks=True,actual_regular_coefficient_auxiliary_proved=True,
 actual_closed_normal_resolvent_domain_rule_proved=True,coefficient_identity_algebra='C0(Y)',
 original_unit_R_realization_proved=False,completed_physical_graph_sum_proved=False,original_Bott_plus_one_proved=False,
 canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'fast-magnitude-resolvents.png')
(a.output_dir/'fast-magnitude-resolvents.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
(a.output_dir/'FAST-MAGNITUDE-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outputs=3,exact_clifford_and_inverse_checks=True,exact_parameter_samples=len(samples),overflows=overflow)))
