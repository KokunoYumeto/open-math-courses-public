"""Full coefficient stabilization with its normal complement: original CC0."""
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
W,H=2450,1850
INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<title>Completing the coefficient stabilization with a normal complement</title>',
'<desc>CSB.1 to CSB.21. An actual infinite defect-cell unitary, compact derivatives of each complementary column, and a parallel confining complementary operator give genuine full coefficient resolvents. The green curve is a proved upper bound, not an exact norm or a finite-truncation norm. The B-source inverse and original physical graph sum remain unproved.</desc>',
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
text(45,25,'Completing the coefficient stabilization with a normal complement',40)
text(45,88,'CSB.1–CSB.21. Actual coefficient A=C0(X). The inverse dX has a different left algebra and remains to be identified.',26)
box(45,145,1155,355)
text(78,175,'The Hilbert–Schmidt endpoint supplies the columns',31)
text(78,245,'Trace h ≤ ¼; V=Γ(T), q=V*V, b=√(1−q)',29,BLUE)
text(78,310,'V, δiV and δi√q are actual Hilbert–Schmidt maps',27)
text(78,375,'(δiJN)V* → Ai in compact norm',32,GREEN)
text(78,435,'Triangular coefficient F(μ,ν) ≤ 8/3',29,GREEN)
box(1240,145,1165,355)
text(1273,175,'An exact infinite defect-cell unitary',32)
text(1273,245,'K0 y=(d y, −JV*y); Kn=shiftⁿ K0',29,BLUE)
text(1273,310,'d=√(1−VV*); J*Kn=0; Kn*Km=δnm',29)
text(1273,375,'U=(J,K): E⊕H∞ → H∞; JJ*+KK*=1',28,GREEN)
text(1273,435,'δiKn=shiftⁿ δiK0 is compact; ||δiKn||≤Ci',27)
arrow(620,507,620,543)
arrow(1820,507,1820,543)
box(45,550,1155,345)
text(78,580,'A parallel complementary input operator',32)
text(78,650,'r=Γ(r0), ||r||≤½; C0=QH r⁻²; |C0|≥4',28,BLUE)
text(78,715,'Cc=⊕m 2ᵐ⁺¹ C0; diagonal resolvents are parallel',27)
text(78,780,'Σm ||Rc,m||² ≤ 1/(8λ)',31,GREEN)
text(78,840,'δi(KRc,±K*) compact; norm ≤ Ci/√(2λ)',27,GREEN)
box(1240,550,1165,345)
text(1273,580,'The actual full ambient resolvent',32)
text(1273,650,'Lhat+=U(L⊕Cc)U*; L=W q⁻²',29,BLUE)
text(1273,715,'Rhat±=JR±J*+KRc,±K*',32,GREEN)
text(1273,780,'Closed normal-domain rule on all of H∞',29)
text(1273,840,'Adjoin A vacuum; transport the full affine action',27)
box(45,945,2360,650)
text(78,975,'Scalar family V=t²I, L=Q t⁻⁸, Cc,m=2ᵐ⁺³ Q, λ=256, 0<t≤½',32)
text(78,1038,'The curves use proved infinite-column formulas. Green is the full resolvent derivative upper bound CSB.20.',25)
gx,gy,gw,gh=175,1487,1325,365
ylo,yhi=-4,3
def xy(t,v):return gx+gw*(math.log2(t)+6)/5,gy-gh*(math.log10(v)-ylo)/(yhi-ylo)
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
for v,label in [(1e-4,'10⁻⁴'),(1e-2,'10⁻²'),(1,'1'),(100,'10²')]:
 yy=xy(1/64,v)[1];line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(68,yy-12,label,22,GRAY)
for t,label in [(1/64,'1/64'),(1/16,'1/16'),(1/4,'1/4'),(1/2,'1/2')]:
 xx=xy(t,1e-4)[0];line([(xx,gy-gh),(xx,gy)],'#dbe5ee',1);text(xx-23,gy+12,label,22,GRAY)
curves=[[],[],[]];curve_values=[]
for i in range(201):
 t=2**(-6+5*i/200);den=1+256**2*t**16
 j2=4/(t*t*(1-t**4));k2=8*t*t/(1-t**4)
 r2=t**16/den;dr2=64*t**14/den**2;off2=r2*j2
 source2=(dr2+2*off2+math.sqrt(dr2*dr2+4*dr2*off2))/2
 bound=math.sqrt(source2)+math.sqrt(k2/512)
 values=[math.sqrt(j2),math.sqrt(k2),bound]
 assert all(1e-4<v<1000 for v in values)
 for pts,v in zip(curves,values):pts.append(xy(t,v))
 curve_values.append(dict(t=t,J_derivative=values[0],K0_derivative=values[1],full_derivative_upper_bound=values[2]))
line(curves[0],RED,5);line(curves[1],BLUE,5);line(curves[2],GREEN,5)
text(1600,1125,'Red: ||J′|| diverges at zero',28,RED)
text(1600,1188,'Blue: ||K0′|| vanishes at zero',27,BLUE)
text(1600,1251,'Green: proved ||Rhat±′|| upper bound',25,GREEN)
text(1600,1314,'Both axes logarithmic; 201 samples',25)
text(1600,1377,'At t=½: ||K0′||²=32/15',28,BLUE)
text(1600,1440,'Complementary bound square =1/240',25,GREEN)
text(485,1545,'t (log scale); vertical axis is derivative norm or its proved upper bound (log scale)',23)
box(45,1640,2360,140)
text(78,1668,'The full coefficient operator and its normal resolvents are proved. Its genuine affine cycle is 1A.',29,GREEN)
text(78,1726,'The B-source inverse, original C0(T) balancing, physical graph sum and Bott +1 remain to be constructed.',27,RED)
text(45,1816,'Original CC0. CSB.1–CSB.21. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow

# Exact rational infinite-series identities and finite defect cells.
pairs=[(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(7,25),F(24,25)),(F(12,37),F(35,37))]
kernels=[]
for s,a0 in pairs:
 for u,c0 in pairs:
  mu=s*s;nu=u*u
  closed=(1+a0*c0)/((1-a0*a0)*(1-c0*c0)*(1-a0*c0))
  if a0!=c0:
   geometric=(a0*a0/(1-a0*a0)+c0*c0/(1-c0*c0)-2*a0*c0/(1-a0*c0))/(a0-c0)**2
  else:geometric=(1+a0*a0)/(1-a0*a0)**3
  assert geometric==closed
  factor=mu*nu*(s+u)**2/(a0+c0)**2*closed
  assert factor==((1+a0*c0)*(s+u)**2/((1-a0*c0)*(a0+c0)**2))
  assert mu<=F(1,4) and nu<=F(1,4) and factor<=F(8,3)
  kernels.append(dict(mu=str(mu),nu=str(nu),a=str(a0),c=str(c0),series=str(closed),kernel=str(factor),exact_series_identity=True,exact_kernel_bound=True))
def mm(A,B):
 return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return [list(x) for x in zip(*A)]
cells=[]
for s,b0 in pairs:
 assert s*s+b0*b0==1
 for N in range(9):
  size=N+2;columns=[]
  for j in range(size):
   carrier=F(j==0);ys=[F(j==m+1) for m in range(N+1)];zs=[]
   for y in ys:
    zs.append(s*carrier+b0*y);carrier=b0*carrier-s*y
   columns.append(zs+[carrier])
  matrix=transpose(columns)
  identity=[[F(i==j) for j in range(size)] for i in range(size)]
  assert mm(transpose(matrix),matrix)==identity and mm(matrix,transpose(matrix))==identity
  assert [matrix[n][0] for n in range(N+1)]==[s*b0**n for n in range(N+1)]
  for j in range(N+1):
   expected=[F(0) if n<j else b0 if n==j else -s*s*b0**(n-j-1) for n in range(N+1)]
   assert [matrix[n][j+1] for n in range(N+1)]==expected
  cells.append(dict(s=str(s),b=str(b0),last_coordinate=N,dimension=size,exact_both_unitary_products=True,exact_J_and_K_columns=True,scope='Finite defect-cell unitary including terminal carrier; no infinite resolvent norm claim'))
norms=[]
for t in [F(1,2),F(1,4),F(1,8)]:
 q=t**4;x=1-q
 S0=1/q;S1=1/(q*q);S2=(1+x)/(x*q**3)
 J_s2=S0-2*q*S1+q*q*S2
 K_s2=q/x+4*q*S0-4*q*q*S1+q**3*S2
 j2=4*t*t*J_s2;k2=4*t*t*K_s2
 assert j2==4/(t*t*(1-q)) and k2==8*t*t/(1-q)
 norms.append(dict(t=str(t),J_derivative_squared=str(j2),K0_derivative_squared=str(k2),exact_geometric_norm_identities=True))
assert norms[0]['K0_derivative_squared']=='32/15'
assert F(32,15)/512==F(1,240)
checks=dict(schema='full-coefficient-complement-checks/v1',exact_geometric_kernels=kernels,exact_defect_cell_matrices=cells,
 exact_scalar_norms=norms,all_fraction_checks=True,curve_samples=201,curve_values=curve_values,
 scalar_sample=dict(t='1/2',lambda_value=256,K0_derivative_squared='32/15',source_compressed_derivative_squared='(19+sqrt(345))/30720',complementary_derivative_bound_squared='1/240'),
 infinite_full_resolvent_proved=True,normal_full_resolvent_product_rule_proved=True,
 actual_coefficient_algebra='C0(X)',coefficient_cycle_class='1_A',vacuum_affine_mixing_retained=True,
 curve_is_proved_upper_bound=True,unweighted_U_derivative_asserted=False,
 target_connection_covariance_under_transported_action_asserted=False,
 actual_B_source_inverse_module_identified=False,completed_physical_graph_sum_proved=False,original_Bott_plus_one_proved=False,
 canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'full-coefficient-complement.png')
(a.output_dir/'full-coefficient-complement.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
(a.output_dir/'COEFFICIENT-COMPLEMENT-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outputs=3,geometric_kernels=len(kernels),exact_cell_matrices=len(cells),exact_scalar_norms=len(norms),curve_samples=201,overflows=overflow)))
