"""Normally controlled stabilization on probability coefficients: original CC0."""
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
W,H=2450,1810
INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<title>Normally controlled stabilization on probability coefficients</title>',
'<desc>PC.1 to PC.22. The proved FD/PJ field supplies the normal connection. A smooth column, its positive-occupation Fock map and exact resolvent weight produce compact normal derivatives of compressed resolvents. The original inverse module and physical graph sum remain unproved. The curves use exact analytic formulas for an infinite-column scalar family.</desc>',
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
text(45,25,'Normally controlled stabilization on the probability coefficients',40)
text(45,88,'PC.1–PC.22. Actual A=C0(X), X=ProbT(YFD). Real fields, full inverse Spin-c and right Clifford order retained.',27)
box(45,150,1155,390);text(78,180,'Use the field whose normal lift is proved',32)
text(78,252,'FD Haar-pinned field → PJ probability field',30,BLUE)
text(78,318,'Compact lifted measures define the closed connection',28)
text(78,384,'Actual affine action; proper anchor to original T',29)
text(78,450,'Ordinary section/contraction; no equivariant evaluation',27,RED)
box(1240,150,1165,390);text(1273,180,'A genuine smooth column and Fock compact',32)
text(1273,252,'T=S*; h=T*T ≤ ¼; T and δiT compact',30,BLUE)
text(1273,318,'TF=Γ(T) on positive occupation; q=Γ(h)',29)
text(1273,384,'||δiΓn(T)|| ≤ n||T||ⁿ⁻¹||δiT|| → 0',29,GREEN)
text(1273,450,'Cf q½ bounded and compact; vacuum separate',29)
box(45,585,1155,330);text(78,616,'Fit the magnitude to the exact weight',32)
text(78,685,'L=W q⁻²; Dom L=Ran q²',32,BLUE)
text(78,753,'R±=q²B±=B±q²; ||B±||≤1',32,GREEN)
text(78,821,'δiR± compact: λ⁻½ magnitude + λ⁻¾ phase',27)
box(1240,585,1165,330);text(1273,616,'The actual infinite-column transfer',32)
text(1273,685,'Jv=(TF(1−q)ⁿᐟ²v)n≥0; J*J=1',29,BLUE)
text(1273,753,'(δiJN)q² → Qi compact in norm',31,GREEN)
text(1273,821,'δi(JR±J*)=QiB±J*+JδiR±J*+JB±Qi*',26)
box(45,960,2360,605);text(78,990,'Exact scalar family: T(t)=t², n=1, λ=256, 0<t≤½',34)
text(78,1052,'q=t⁴, L=Q t⁻⁸. Curves evaluate PC.20–PC.22; J is the full infinite column, not a truncation.',26)
gx,gy,gw,gh=170,1460,1350,335
ylo,yhi=-13,3
def xy(t,v):return gx+gw*(math.log2(t)+6)/5,gy-gh*(math.log10(v)-ylo)/(yhi-ylo)
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
for v,label in [(1e-12,'10⁻¹²'),(1e-8,'10⁻⁸'),(1e-4,'10⁻⁴'),(1,'1'),(100,'10²')]:
 yy=xy(1/64,v)[1];line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(65,yy-12,label,22,GRAY)
for t,label in [(1/64,'1/64'),(1/16,'1/16'),(1/4,'1/4'),(1/2,'1/2')]:
 xx=xy(t,1e-13)[0];line([(xx,gy-gh),(xx,gy)],'#dbe5ee',1);text(xx-22,gy+12,label,22,GRAY)
curves=[[],[],[]]
for i in range(201):
 t=2**(-6+5*i/200);den=1+256**2*t**16
 j2=4/(t*t*(1-t**4));weighted2=j2*t**16
 r2=t**16/den;dr2=64*t**14/den**2;b2=r2*j2
 compressed2=(dr2+2*b2+math.sqrt(dr2*dr2+4*dr2*b2))/2
 for pts,value in zip(curves,[math.sqrt(j2),math.sqrt(weighted2),math.sqrt(compressed2)]):
  assert 1e-13<value<1000
  pts.append(xy(t,value))
line(curves[0],RED,5);line(curves[1],BLUE,5);line(curves[2],GREEN,5)
text(1630,1130,'Red: ||J′||, unbounded at zero',26,RED)
text(1630,1190,'Blue: ||J′q²||, vanishes at zero',26,BLUE)
text(1630,1250,'Green: ||(JR±J*)′||',28,GREEN)
text(1630,1310,'Both axes logarithmic; 201 samples',24)
text(1630,1370,'At t=½: derivative square exactly',24)
text(1630,1420,'(19+√345)/30720',29,GREEN)
text(560,1510,'t (log scale); vertical axis is the indicated derivative norm (log scale)',24)
box(45,1610,2360,135)
text(78,1635,'Compressed resolvents vanish on the complement of Ran J. That complement, actual B-source inverse passage,',26,RED)
text(78,1690,'equivariant absorption, completed physical graph sum and original Bott +1 still require proofs.',28,RED)
text(45,1778,'Original CC0. PC.1–PC.22. Human context: Connes, A survey of foliations and operator algebras, §8; stabilization.',22)
assert not overflow,overflow

# Complex arithmetic as pairs of exact fractions; no floating matrix certificate.
def c(re=0,im=0):return (F(re),F(im))
def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cs(k,a):return (k*a[0],k*a[1])
def conj(a):return (a[0],-a[1])
def mm(a,b):return [[ca(cm(a[i][0],b[0][j]),cm(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def adj(a):return [[conj(a[j][i]) for j in range(2)] for i in range(2)]
I=[[c(1),c()],[c(),c(1)]];Q=[[c(),c(1)],[c(1),c()]]
samples=[]
for n in [1,2,3,4]:
 for t in [F(1,2),F(1,4),F(1,8)]:
  q=t**(4*n);m=q**-2;mp=-8*n*t**(-8*n-1);mi=4*n*t**(4*n-1)
  for lam in [1,16,256]:
   den=m*m+lam*lam
   r=[[c(0,-F(lam,den)),c(F(m,den))],[c(F(m,den)),c(0,-F(lam,den))]]
   rprime=[[c(0,2*lam*m*mp/(den*den)),c(mp*(lam*lam-m*m)/(den*den))],[c(mp*(lam*lam-m*m)/(den*den)),c(0,2*lam*m*mp/(den*den))]]
   inv=mm(r,[[c(0,lam),c(m)],[c(m),c(0,lam)]])
   assert inv==I
   predicted=[[cs(-mp,x) for x in row] for row in mm(mm(r,Q),r)]
   assert predicted==rprime
   dr2=64*n*n*t**(16*n-2)/(1+lam*lam*t**(16*n))**2
   bound2=2*mi*mi/lam
   assert mm(adj(rprime),rprime)==[[cs(dr2,x) for x in row] for row in I]
   assert dr2<=bound2
   bnorm2=m*m/den
   assert bnorm2<=1
   samples.append(dict(occupation=n,t=str(t),lambda_value=lam,derivative_squared=str(dr2),bound_squared=str(bound2),factor_norm_squared=str(bnorm2),exact_inverse_identity=True,exact_inverse_derivative_identity=True,exact_norm_and_bound=True))
assert len(samples)==36
n=1;t=F(1,2);lam=256
j2=F(4)/(t*t*(1-t**4));weighted2=j2*t**16
dr2=F(64)*t**14/(1+lam*lam*t**16)**2
r2=t**16/(1+lam*lam*t**16);b2=r2*j2
assert j2==F(256,15) and weighted2==F(1,3840)
assert dr2==F(1,1024) and b2==F(1,7680)
assert dr2+2*b2==F(19,15360)
assert dr2*dr2+4*dr2*b2==F(345,15360**2)
assert F(19,15360)<F(1,1920)+F(1,1024)==F(23,15360)
for n in range(1,101):
 assert n<=4**(n-1) and n*(1+2*n)**2<=4*4**n
checks=dict(schema='probability-coercive-stabilization-checks/v1',real_clifford_matrix=[[0,1],[1,0]],
exact_scalar_samples=samples,all_complex_matrix_fraction_checks=True,curve_samples=201,
sample_occupation=1,sample_t='1/2',sample_lambda=256,unweighted_column_derivative_squared=str(j2),
weighted_column_derivative_squared=str(weighted2),resolvent_derivative_squared=str(dr2),
resolvent_derivative_bound_squared='1/512',factor_norm_squared='1/2',
compressed_derivative_squared='(19+sqrt(345))/30720',compressed_discriminant_integer=345,
compressed_trace=str(dr2+2*b2),compressed_discriminant=str(dr2*dr2+4*dr2*b2),
compressed_upper_rational='19/15360',transfer_bound_lower_rational='23/15360',
infinite_column_reduction_proved=True,actual_probability_coefficient_algebra='C0(X)',
actual_compact_normal_compressed_resolvents_proved=True,whole_ambient_resolvent=False,
unweighted_stabilization_derivative_asserted=False,actual_B_source_inverse_module_identified=False,
completed_physical_graph_sum_proved=False,original_Bott_plus_one_proved=False,
canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'probability-coercive-stabilization.png')
(a.output_dir/'probability-coercive-stabilization.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
(a.output_dir/'PROBABILITY-STABILIZATION-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outputs=3,exact_matrix_samples=len(samples),infinite_column_reduction=True,overflows=overflow)))
