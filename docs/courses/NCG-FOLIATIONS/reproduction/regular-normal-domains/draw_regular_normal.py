"""Actual regular normal domains and scalar localized compactness: CC0."""
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
W,H=2450,1800;INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Normal domains and scalar compactness on the regular graph</title>',
 '<desc>RGN.1 to RGN.13. Actual arrow/copy rows, finite-core maximal-to-minimal regularization, and scalar localized compactness. Normalized phase transfer remains unproved.</desc>',
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
text(45,25,'From regular graph coefficients to scalar localized compacts',42)
text(45,86,'RGN.1–RGN.13: actual arrow/copy rows, the full inverse Spin-c coefficient, and completed normal domains.',30)
box(45,150,1160,505);text(77,180,'The literal range-regular graph',35)
text(80,235,'H = L²(GT,νr;r*Sinv) ⊗ ℓ²(N)',31,BLUE)
for j,y in enumerate([310,392,474],1):
 box(85,y,245,60,'#e9f3f8',BLUE);text(106,y+13,'row (g'+str(j)+',n'+str(j)+')',26,BLUE)
 arrow(347,y+30,656,423,GREEN)
box(680,370,465,106,'#e3f2e9',GREEN);text(705,389,'r(gj)=x;  wη=Ση(g)*u(g)',26,GREEN)
text(80,565,'Amax u in L² ⇒ DT wη in L² ⇒ wη locally H¹',29,GREEN)
text(80,615,'Rows retain their arrow labels and copy indices.',27)
box(1245,150,1160,505);text(1277,180,'The finite-core domain test',35)
text(1280,245,'T=Σ θξ,η; ξ and η have compact arrow support',30,BLUE)
box(1280,310,1090,106,'#e3f2e9',GREEN)
text(1305,331,'T Dom Amax ⊂ Dom Amin',33,GREEN)
text(1305,379,'AminTu = TAmaxu − iΣ cj (∂jT)u',28,GREEN)
text(1280,469,'Tn→T and ∂jTn→∂jT in module norm:',29)
text(1280,523,'closed Amin gives the same completed-domain identity.',28,GREEN)
text(1280,596,'Compact fibre rank alone does not give this test.',28,RED)
box(45,695,2360,240);text(77,722,'Exact finite contraction and derivative sample (near a cutoff equal to one)',33)
text(80,784,'ξ=(⅗,⅘,0), η=(0,⅘,⅗), u=(1,2,3)',30,BLUE)
text(1280,784,'wη=17/5; wη′=1; Tu=(51/25,68/25,0)',29,GREEN)
text(80,852,'ξ′=(−⅘,⅗,0), η′=(0,−⅗,⅘)',30,BLUE)
text(1280,852,'(∂T)u=(−2,3,0); [D,T]u=−i(∂T)u',29,GREEN)
box(45,975,1160,580);text(77,1005,'Unit H¹ control: finite cube averages',34)
text(80,1047,'Cell labels: x; left row labels: 2y',22)
gx,gy,gs,n=140,1078,335,4
for i in range(n):
 for j in range(n):
  cx=Q(2*i+1,2*n);cy=Q(2*j+1,2*n)
  col='#'+''.join(f'{z:02x}' for z in [int(223-75*float(cx)),int(239-90*float(cy)),int(245-30*float(cx))])
  box(gx+i*gs/n,gy+(n-1-j)*gs/n,gs/n,gs/n,col,'#c5d1dc')
  text(gx+i*gs/n+12,gy+(n-1-j)*gs/n+29,str(cx),19,INK)
for j in range(n):
 text(82,gy+(n-1-j)*gs/n+29,str(Q(2*j+1,n)),20)
text(510,1100,'v(x,y)=(x,2y) ∈ H¹([0,1]²;C²)',27,BLUE)
text(510,1173,'n×n grid; spinor rank r=2 in this sample',26)
text(510,1246,'rank Pn = 2n²; ‖∇v‖² = 5',30,GREEN)
text(510,1318,'Exact error² = 5/(12n²)',30,GREEN)
text(510,1390,'RGN.12 upper bound² = 5/n²',28)
text(80,1485,'n=4: rank 32; exact error² 5/192; upper bound² 5/16.',28)
box(1245,975,1160,580);text(1277,1005,'Scalar localized compactness',35)
text(1280,1079,'Given the actual self-adjoint completed sum S:',29)
text(1280,1143,'χRC ∈ K(E) ⇒ finite core en approximate χRC',29,BLUE)
text(1280,1208,'Amaxχ(S+iλ)⁻¹ has bounded graph images',29,GREEN)
text(1280,1273,'enχ(S+iλ)⁻¹: finitely many H¹ unit coefficients',28,GREEN)
text(1280,1338,'Rellich averages ⇒ scalar compact finite-row images',28,GREEN)
text(1280,1403,'‖(1−en)χRC‖ ‖Lλ⁻¹‖→0 ⇒ χ(S+iλ)⁻¹ compact',28,GREEN)
text(1280,1474,'π(f)=π(f)χ for χ=1 on the source support of f.',27)
box(45,1595,2360,150,'#fff0e7',RED)
text(77,1620,'The normalized auxiliary generator and its differentiable transfer, phase controls and Bott +1 remain unproved.',30,RED)
text(77,1680,'K-theory of the leaf space, Section 11AO; RGN.1–RGN.13. Finite samples illustrate the proved analytic tests.',28)
assert not overflow,overflow
xi=[Q(3,5),Q(4,5),Q(0)];eta=[Q(0),Q(4,5),Q(3,5)]
dxi=[Q(-4,5),Q(3,5),Q(0)];deta=[Q(0),Q(-3,5),Q(4,5)]
u=[Q(1),Q(2),Q(3)];du=[Q(2),Q(-1),Q(1)]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
assert dot(xi,xi)==dot(eta,eta)==dot(dxi,dxi)==dot(deta,deta)==1
w=dot(eta,u);dw=dot(deta,u)+dot(eta,du);tu=[x*w for x in xi]
dtu=[x*w+y*dot(deta,u) for x,y in zip(dxi,xi)];full=[x*w+y*dw for x,y in zip(dxi,xi)]
assert w==Q(17,5) and dw==1 and tu==[Q(51,25),Q(68,25),Q(0)] and dtu==[Q(-2),Q(3),Q(0)]
assert full==[Q(-53,25),Q(71,25),Q(0)]
assert dot(tu,tu)==Q(289,25) and dot(tu,tu)<=dot(u,u)
grids=[]
for n in [2,4,8]:
 ell=Q(1,n);error=Q(0)
 for i in range(n):
  ax,bx=Q(i,n),Q(i+1,n);mx=(ax+bx)/2
  vx=(bx**3-ax**3)/3-mx*(bx**2-ax**2)+mx*mx*(bx-ax)
  for j in range(n):
   ay,by=Q(j,n),Q(j+1,n);my=(ay+by)/2
   vy=(by**3-ay**3)/3-my*(by**2-ay**2)+my*my*(by-ay)
   error+=ell*vx+4*ell*vy
 assert error==Q(5,12*n*n) and error<=Q(5,n*n)
 grids.append(dict(n=n,rank=2*n*n,gradient_norm_square='5',exact_error_square=str(error),proved_bound_square=str(Q(5,n*n))))
checks=dict(schema='actual-regular-normal-figure-checks/v1',finite_rows=3,xi=[str(x) for x in xi],eta=[str(x) for x in eta],xi_prime=[str(x) for x in dxi],eta_prime=[str(x) for x in deta],u=[str(x) for x in u],u_prime=[str(x) for x in du],contraction=str(w),contraction_prime=str(dw),T_u=[str(x) for x in tu],T_prime_u=[str(x) for x in dtu],full_output_derivative=[str(x) for x in full],T_u_norm_square='289/25',u_norm_square='14',grid_cases=grids,compact_arrow_core_required=True,global_derivative_ideal_preserved_by_ordinary_unitary_inferred=False,normalized_auxiliary_generator_proved=False,original_Bott_plus_one_comparison_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
im.save(a.output_dir/'regular-normal-domains.png',compress_level=9)
(a.output_dir/'regular-normal-domains.svg').write_text('\n'.join(svg+['</svg>'])+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'REGULAR-NORMAL-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'exact_contraction':'17/5','exact_derivative':[-2,3,0],'grid_cases':3,'n4_error_square':'5/192','overflows':len(overflow)}))
