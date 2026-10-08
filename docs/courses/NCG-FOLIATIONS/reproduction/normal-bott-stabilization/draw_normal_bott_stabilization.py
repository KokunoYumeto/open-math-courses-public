"""Normal finite columns and the fixed Bott weight: original CC0."""
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
W,H=2450,1900
INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<title>Normal finite columns of an actual stabilized affine action</title>',
'<desc>NBJ.1 to NBJ.23. Dominated source columns give actual finite normal jets after real stabilization. A fixed parallel diagonal weight accommodates these jets. The scalar reflection example compares exact infinite-column derivative norms; it is not a proper holonomy model or a B-source inverse.</desc>',
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

text(45,25,'Normal finite columns of the stabilized Bott action',43)
text(45,90,'NBJ.1–NBJ.23. Actual real affine field E over A=C0(X); target displacement bg is retained.',29)
box(45,150,1155,365)
text(78,180,'Endpoint domination gives an actual normal jet',32)
text(78,248,'T:E→L; h=T*T≤¼, dense hE; (δiJN)T*→Ai',28,BLUE)
text(78,316,'Z=δiJN−δiJM; VV*≤C h ⇒ ||ZV||≤√C ||ZT*||',25)
text(78,384,'δi(JV)=Qi,V+JδiV is compact',31,GREEN)
text(78,451,'Apply to LgTs* and the original displacement bg',27)
box(1240,150,1165,365)
text(1273,180,'Real stabilization keeps the actual affine action',31)
text(1273,248,'U=(J,K): E⊕L∞ → L∞ is an onto unitary',28,BLUE)
text(1273,316,'Vg=Ur(Lg⊕Wg0)Us*; b̃g=Jrbg',31)
text(1273,384,'b̃gh=b̃g+Vg b̃h; ||b̃g||=||bg||',28,GREEN)
text(1273,451,'bʲT*=T*dʲ controls the finite input columns',27)
arrow(620,522,620,558);arrow(1820,522,1820,558)
box(45,565,1155,365)
text(78,595,'Fixed basis vectors and their normal jets',31)
text(78,663,'Vg ej, δi(Vg ej), b̃g and δib̃g are actual vectors',27,BLUE)
text(78,731,'Choose monotone finite diagonal contractions vn',27)
text(78,799,'||[vn,Vg]||≤2⁻ⁿ; ||(1−vn)ξ||≤2⁻ⁿ',29,GREEN)
text(78,867,'Bounds hold uniformly on each compact arrow test',26)
box(1240,565,1165,365)
text(1273,595,'One parallel weight supplies graph membership',30)
text(1273,663,'Θ=1+Σn(1−vn); Θej=λj ej; λj→∞',29,BLUE)
text(1273,731,'δi(Θξ)=Θδiξ; Vg DomΘ=DomΘ',28,GREEN)
text(1273,799,'Sg=VgΘVg*−Θ is a continuous compact defect',27)
text(1273,867,'No bounded derivative of all of U or Vg is used',26)
box(45,985,2360,620)
text(78,1015,'Exact scalar test: T=t², Jn=t²(1−t⁴)ⁿᐟ², V=1−2JJ*, V²=1',31)
text(78,1080,'Scalar reflection with zero displacement; an analytic test, not a proper holonomy-groupoid model.',25)
gx,gy,gw,gh=180,1480,1300,325
ylo,yhi=-2,3
def xy(t,v):return gx+gw*(math.log2(t)+6)/5,gy-gh*(math.log10(v)-ylo)/(yhi-ylo)
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
for v,label in [(1e-2,'10⁻²'),(1e-1,'10⁻¹'),(1,'1'),(10,'10'),(100,'10²')]:
 yy=xy(1/64,v)[1];line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(70,yy-12,label,22,GRAY)
for t,label in [(1/64,'1/64'),(1/16,'1/16'),(1/4,'1/4'),(1/2,'1/2')]:
 xx=xy(t,.01)[0];line([(xx,gy-gh),(xx,gy)],'#dbe5ee',1);text(xx-23,gy+14,label,22,GRAY)
curves=[[],[],[]];values=[]
for i in range(201):
 t=2**(-6+5*i/200);q=t**4
 norms=[math.sqrt(16/(t*t*(1-q))),math.sqrt(16*t*t*(2-q)/(1-q)),math.sqrt(4*t*t/(1-q))]
 assert all(.01<v<1000 for v in norms)
 for pts,v in zip(curves,norms):pts.append(xy(t,v))
 values.append(dict(t=t,whole_action_derivative=norms[0],first_column_derivative=norms[1],endpoint_derivative=norms[2]))
for pts,col in zip(curves,[RED,GREEN,BLUE]):line(pts,col,5)
text(1580,1153,'Red: ||V′|| diverges at zero',29,RED)
text(1580,1220,'Green: ||(Ve0)′|| tends to zero',28,GREEN)
text(1580,1287,'Blue: ||J′T*|| tends to zero',28,BLUE)
text(1580,1354,'At t=½: squared norms',28)
text(1580,1421,'1024/15, 124/15 and 16/15',29)
text(430,1538,'t (log scale); vertical axis is the exact infinite-column derivative norm (log scale)',23)
box(45,1655,2360,145)
text(78,1685,'Positive Bott operator: TS+tDt³+Bt(1+tΘ); its normal resolvent derivative is zero.',28,GREEN)
text(78,1743,'Its scalar coefficient action does not identify the B-source inverse. That left representation is still unproved.',26,RED)
text(45,1842,'Original CC0. NBJ.1–NBJ.23. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow

def mm(A,B):
 return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return [list(x) for x in zip(*A)]
reflections=[]
for s,b in [(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(7,25),F(24,25)),(F(12,37),F(35,37))]:
 for N in range(9):
  j=[s*b**n for n in range(N+1)]+[b**(N+1)]
  assert sum(x*x for x in j)==1
  size=len(j);I=[[F(i==k) for k in range(size)] for i in range(size)]
  V=[[I[i][k]-2*j[i]*j[k] for k in range(size)] for i in range(size)]
  assert V==transpose(V) and mm(V,V)==I
  assert [V[i][0] for i in range(size)]==[F(i==0)-2*s*j[i] for i in range(size)]
  reflections.append(dict(s=str(s),b=str(b),last_coordinate=N,dimension=size,exact_unit_vector=True,exact_selfadjoint_involution=True,exact_first_column=True,scope='Finite reflection including terminal carrier; infinite derivative norms verified separately'))
norms=[]
for t in [F(1,2),F(1,4),F(1,8),F(1,16),F(1,32),F(1,64)]:
 q=t**4;x=1-q;s=t*t;sp=2*t
 S0=1/q;S1=1/(q*q);S2=(1+x)/(x*q**3)
 js2=S0-2*q*S1+q*q*S2
 inner=s*(S0-q*S1)
 assert inner==0
 j2=sp*sp*js2
 assert j2==4/(t*t*(1-q))
 col2=4*(sp*sp+q*j2);whole2=4*j2;endpoint2=q*j2
 assert col2==16*t*t*(2-q)/(1-q) and whole2==16/(t*t*(1-q)) and endpoint2==4*t*t/(1-q)
 norms.append(dict(t=str(t),J_derivative_squared=str(j2),whole_action_derivative_squared=str(whole2),first_column_derivative_squared=str(col2),endpoint_derivative_squared=str(endpoint2),exact_geometric_norm_identities=True,exact_orthogonality=True))
assert norms[0]['whole_action_derivative_squared']=='1024/15'
assert norms[0]['first_column_derivative_squared']=='124/15'
assert norms[0]['endpoint_derivative_squared']=='16/15'
checks=dict(schema='normal-bott-stabilization-checks/v1',exact_reflections=reflections,exact_infinite_norms=norms,all_fraction_checks=True,curve_samples=201,curve_values=values,curve_interpretation='Exact infinite-column norm formulas NBJ.22–NBJ.23, numerically evaluated; no finite truncation norm',actual_finite_normal_columns_proved=True,actual_displacement_normal_jet_proved=True,fixed_parallel_weight_graph_jets_proved=True,positive_fibre_parallel_resolvents_proved=True,whole_transported_action_bounded_derivative_asserted=False,normal_derivative_of_entire_transport_defect_asserted=False,actual_B_source_inverse_module_identified=False,completed_physical_graph_sum_proved=False,original_Bott_plus_one_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'normal-bott-stabilization.png',format='PNG',optimize=False,compress_level=9)
(a.output_dir/'normal-bott-stabilization.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'NORMAL-BOTT-STABILIZATION-CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(all_fraction_checks=True,exact_reflections=len(reflections),exact_infinite_norms=len(norms),canvas=[W,H],text_canvas_overflows=overflow)))
