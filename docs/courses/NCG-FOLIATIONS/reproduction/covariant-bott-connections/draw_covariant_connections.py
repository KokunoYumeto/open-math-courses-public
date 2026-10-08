"""Transported closed normal connections: original CC0."""
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
'<title>Two specified normal connections after actual stabilization</title>',
'<desc>CTN.1 to CTN.16. Transporting a closed connection through an actual unitary gives its completed domain and real linear covariance. Finite columns compare it with the constant connection. Full resolvent derivatives conjugate exactly. A fixed weight parallel for the constant connection need not be parallel for the covariant one.</desc>',
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


text(45,25,'Two normal connections after actual stabilization',43)
text(45,92,'CTN.1–CTN.16. The completed domain is transported; no bounded derivative of the full unitary is assumed.',27)
box(45,150,1155,340)
text(78,180,'Transport the actual completed connection',32)
text(78,250,'U:M→N; Dom ∇hat=U Dom ∇',31,BLUE)
text(78,318,'∇hat(Uv)=U∇v; actual graph core is U C',28,GREEN)
text(78,386,'The metric and scalar product rules are preserved',26)
text(78,442,'Actual linear covariance transfers with its directions',25)
box(1240,150,1165,340)
text(1273,180,'Finite columns compare the two connections',31)
text(1273,250,'J*PN=(bʲT*)j≤N; K*PN has n≤N only',28,BLUE)
text(1273,318,'δi(U*PN)=Di,N is an actual compact map',29)
text(1273,386,'∇hat u=∇0u+Ai,N u; Ai,N=U Di,N',28,GREEN)
text(1273,442,'Skew on the common core; no full bounded Ai claim',25)
arrow(620,497,620,540);arrow(1820,497,1820,540)
box(45,550,1155,340)
text(78,580,'Genuine full resolvents conjugate exactly',31)
text(78,650,'Dhat=UDU*; Rhat±=UR±U*',31,BLUE)
text(78,718,'δhat Rhat±=U(δR±)U* is compact',30,GREEN)
text(78,786,'Same norm and completed normal-domain rule',27)
text(78,842,'Complementary input derivative is zero',27)
box(1240,550,1165,340)
text(1273,580,'Parallel weight requires its own connection',30)
text(1273,650,'∇0Θ=0; ∇hatΘ−Θ∇hat=[Ai,Θ]',28,BLUE)
text(1273,718,'Rotation test: Ai=(0,1; −1,0)',29)
text(1273,786,'Θ=diag(1,2); [Ai,Θ]=(0,1; 1,0)',29,RED)
text(1273,842,'Norm =1; covariant does not mean parallel weight',25)
box(45,945,2360,645)
text(78,975,'Infinite scalar comparison: T=t²I, L=Qt⁻⁸, Cc,m=2ᵐ⁺³Q, λ=256',31)
text(78,1040,'Red is the old constant-column upper bound. Green is the exact transported-connection norm; blue bounds green.',24)
gx,gy,gw,gh=180,1485,1325,350;ylo,yhi=-13,0
def xy(t,v):return gx+gw*(math.log2(t)+6)/5,gy-gh*(math.log10(v)-ylo)/(yhi-ylo)
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
for v,label in [(1e-12,'10⁻¹²'),(1e-9,'10⁻⁹'),(1e-6,'10⁻⁶'),(1e-3,'10⁻³'),(1,'1')]:
 yy=xy(1/64,v)[1];line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(68,yy-12,label,22,GRAY)
for t,label in [(1/64,'1/64'),(1/16,'1/16'),(1/4,'1/4'),(1/2,'1/2')]:
 xx=xy(t,1e-13)[0];line([(xx,gy-gh),(xx,gy)],'#dbe5ee',1);text(xx-23,gy+12,label,22,GRAY)
curves=[[],[],[]];values=[]
for i in range(201):
 t=2**(-6+5*i/200);den=1+256**2*t**16;j2=4/(t*t*(1-t**4));k2=8*t*t/(1-t**4)
 dr2=64*t**14/den**2;off2=t**16/den*j2
 source2=(dr2+2*off2+math.sqrt(dr2*dr2+4*dr2*off2))/2
 norms=[math.sqrt(source2)+math.sqrt(k2/512),8*t**7/den,math.sqrt(2)*t**3/4]
 assert norms[1]<=norms[2] and all(1e-13<v<1 for v in norms)
 for pts,v in zip(curves,norms):pts.append(xy(t,v))
 values.append(dict(t=t,constant_column_upper_bound=norms[0],transported_connection_exact_norm=norms[1],transported_connection_upper_bound=norms[2]))
for pts,col in zip(curves,[RED,GREEN,BLUE]):line(pts,col,5)
text(1580,1140,'Different specified connections',29)
text(1580,1205,'Green: 8t⁷/(1+256²t¹⁶)',30,GREEN)
text(1580,1270,'Blue: √2 t³/4',31,BLUE)
text(1580,1335,'At t=½: green norm =1/32',29,GREEN)
text(1580,1400,'Both axes logarithmic; 201 samples',25)
text(1580,1465,'No finite-truncation norm is used',26)
text(410,1537,'t (log scale); vertical axis is a proved derivative norm or specified upper bound (log scale)',23)
box(45,1640,2360,140)
text(78,1670,'The real linear action has a covariant transported connection; the fixed Bott weight is parallel for ∇0.',27,GREEN)
text(78,1727,'The B-source inverse operator, genuine inverse-module action and original balanced physical sum remain unproved.',25,RED)
text(45,1814,'Original CC0. CTN.1–CTN.16. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def sub(A,B):return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
J=[[F(0),F(-1)],[F(1),F(0)]];A=[[F(0),F(1)],[F(-1),F(0)]];L=[[F(1),F(0)],[F(0),F(-1)]];Theta=[[F(1),F(0)],[F(0),F(2)]]
comm=sub(mm(A,Theta),mm(Theta,A));I=[[F(1),F(0)],[F(0),F(1)]]
assert comm==[[F(0),F(1)],[F(1),F(0)]] and mm(comm,comm)==I
rotations=[]
for c,s in [(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(7,25),F(24,25))]:
 U=[[c,-s],[s,c]];V=mm(mm(U,L),tr(U));Vp=sub(mm(J,V),mm(V,J))
 assert mm(U,tr(U))==I and mm(tr(U),U)==I
 assert add(Vp,sub(mm(A,V),mm(V,A)))==[[F(0)]*2 for _ in range(2)]
 rotations.append(dict(c=str(c),s=str(s),exact_unitary=True,exact_covariant_action_derivative_zero=True,exact_weight_commutator_norm_one=True))
norms=[]
for t in [F(1,2),F(1,4),F(1,8),F(1,16),F(1,32),F(1,64)]:
 den=1+256**2*t**16;n=8*t**7/den;bound2=t**6/8;u=256*t**8
 assert n*n<=bound2 and n*n/bound2==2*u/(1+u*u)**2
 assert (1+u*u)**2-2*u==(u-1)**2+u*u+u**4
 norms.append(dict(t=str(t),exact_transported_resolvent_derivative_norm=str(n),upper_bound_squared=str(bound2),exact_scalar_norm_identity=True,exact_positive_polynomial_bound=True))
assert norms[0]['exact_transported_resolvent_derivative_norm']=='1/32' and norms[0]['upper_bound_squared']=='1/512'
checks=dict(schema='covariant-bott-connection-checks/v1',all_fraction_checks=True,exact_rotation_tests=rotations,exact_infinite_resolvent_norms=norms,curve_samples=201,curve_values=values,transported_connection_completed_domain_proved=True,real_linear_action_covariance_proved=True,finite_connection_difference_columns_compact=True,transported_full_resolvent_derivative_proved=True,fixed_weight_parallel_for_covariant_connection_asserted=False,full_connection_difference_bounded_asserted=False,affine_Fock_connection_covariance_asserted=False,actual_B_source_inverse_module_identified=False,completed_physical_graph_sum_proved=False,original_Bott_plus_one_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>');im.save(a.output_dir/'covariant-bott-connections.png',format='PNG',optimize=False,compress_level=9)
(a.output_dir/'covariant-bott-connections.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'COVARIANT-BOTT-CONNECTIONS-CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(all_fraction_checks=True,exact_rotation_tests=4,exact_infinite_resolvent_norms=6,text_canvas_overflows=overflow)))
