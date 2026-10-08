"""Minimal normal domains and a coefficient graph regularizer: CC0."""
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
W,H=2300,1560;INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Confinement regularizes the minimal normal boundary</title>',
 '<desc>NR.1 to NR.12. Exact coefficient cutoffs, minimal/maximal domains and a complete interval Dirac example. General physical realization remains a premise.</desc>',
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
def dot(x,y,col):
 d.ellipse((x-7,y-7,x+7,y+7),fill=col);svg.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{col}"/>')
text(45,25,'Confinement regularizes the minimal normal boundary',42)
text(45,85,'NR.1–NR.12: a self-adjoint sum can exist while the separate normal operator has deficiency spaces.',29)
box(45,145,1080,485);text(77,175,'The actual domain premise',35)
box(80,250,385,95,'#fff0e7',RED);text(100,275,'Dom A* (maximal)',30,RED)
arrow(475,298,690,298,GREEN);text(518,247,'Rλ',32,GREEN)
box(710,250,380,95,'#e3f2e9',GREEN);text(730,275,'Dom A (minimal)',30,GREEN)
text(80,389,'Rλ=(C+iλ)⁻¹; C self-adjoint; ΓC=−CΓ',29)
text(80,444,'[A,Rλ]=Kλ bounded on both normal domains',29)
text(80,500,'‖Kλ‖<2 for both signs: S=C+ΓA is self-adjoint',28,GREEN)
text(80,557,'Dom S = Dom C ∩ Dom A; no choice of an A extension',26,GREEN)
box(1165,145,1090,485);text(1197,175,'Coefficient cutoff: Jε(b)=b²/(b²+ε)',35)
pl,pr,pt,pb=1275,2180,255,515
line([(pl,pt),(pl,pb),(pr,pb)],GRAY,3)
for eps,col in [(1/260,BLUE),(1/1040,GREEN)]:
 line([(pl+i/200*(pr-pl),pb-(.2*i/200)**2/((.2*i/200)**2+eps)*(pb-pt)) for i in range(201)],col,4)
text(1199,252,'1',25);text(1235,497,'0',25);text(2138,540,'b=0.2',25)
text(1510,549,'ε=1/260',25,BLUE);text(1755,549,'ε=1/1040',25,GREEN)
xx=pl+(1/math.sqrt(260))/.2*(pr-pl);yy=pb-.5*(pb-pt);dot(xx,yy,RED)
text(1650,440,'b²=ε=1/260 → Jε=½',25,RED)
text(1199,590,'Curves are numerical samples; the formula and point are exact.',24)
box(45,670,2210,278);text(77,700,'Uniform commutator and the completed adjoint graph',35)
text(80,758,'‖[X,Jε]‖ ≤ (½ + ¼ + ½) ‖M‖ = ⁵⁄₄ ‖M‖',32,BLUE)
text(80,815,'B Dom A* ⊂ Dom A ⇒ Jεu ∈ Dom A for u ∈ Dom X*',31,GREEN)
text(80,877,'Jεu→u and XJεu→X*u: the original symmetric product X is essentially self-adjoint.',29,GREEN)
box(45,988,1080,395);text(77,1015,'Interval coefficient and its normal derivative',31)
pl,pr,pt,pb=150,1040,1110,1300
line([(pl,pt),(pl,pb),(pr,pb)],GRAY,3)
line([(pl+i/400*(pr-pl),pb-(i/400)**2*(1-i/400)**2/.2*(pb-pt)) for i in range(401)],BLUE,4)
line([(pl+i/400*(pr-pl),pb-abs(2*(i/400)*(1-i/400)*(1-2*i/400))/.2*(pb-pt)) for i in range(401)],RED,4)
text(83,1101,'0.2',24);text(112,1290,'0',24);text(1005,1307,'x=1',23)
x=.5;dot(pl+x*(pr-pl),pb-(1/16)/.2*(pb-pt),BLUE)
text(389,1273,'h(½)=1/16',24,BLUE)
x=(3-math.sqrt(3))/6;dot(pl+x*(pr-pl),pb-(math.sqrt(3)/9)/.2*(pb-pt),RED)
text(405,1116,'max |h′|=√3/9',26,RED)
text(80,1340,'h=x²(1−x)² (blue); |h′| (red); θ=1/h',27)
box(1165,988,1090,395);text(1197,1015,'The completed first-order operator',32)
text(1200,1080,'A=−i d/dx; Dom A=H¹₀ ⊊ H¹=Dom A*',28,RED)
text(1200,1144,'S=σ₁/h−iσ₃ d/dx; Dom S=H¹₀ ∩ {θu∈L²}',28,GREEN)
text(1200,1206,'Rλ and Rλ′ vanish at both endpoints.',28,GREEN)
text(1200,1266,'‖Rλ′‖ ≤ √3/9 < 2;  ‖Rλ′‖ ≤ 2|λ|⁻½',28)
text(1200,1325,'Compact resolvent: rank(Pn)=2n; error≤‖u′‖/n',26,GREEN)
box(45,1423,2210,97,'#fff0e7',RED)
text(77,1442,'The general differentiable physical realization, phase compatibility and original Bott +1 remain unproved.',28,RED)
text(77,1484,'K-theory of the leaf space, Section 11AN; NR.1–NR.12. Original diagram and generator: CC0.',25)
assert not overflow,overflow
cases=[]
for x in [Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)]:
 h=x*x*(1-x)*(1-x);dh=2*x*(1-x)*(1-2*x);b2=h*h/(1+4*h*h);eps=Q(1,260)
 cases.append(dict(x=str(x),h=str(h),h_prime=str(dh),B_square=str(b2),cutoff_epsilon=str(eps),J_epsilon=str(b2/(b2+eps)),resolvent_derivative_norm=str(abs(dh)/(1+4*h*h))))
assert cases[2]['h']=='1/16' and cases[2]['B_square']=='1/260' and cases[2]['J_epsilon']=='1/2'
assert sum([Q(1,2),Q(1,4),Q(1,2)])==Q(5,4)
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
s1=[[0,1],[1,0]];s2=[[0,-1j],[1j,0]];g=[[1,0],[0,-1]]
assert mul(g,s1)==[[1j*z for z in row] for row in s2]
assert mul(s2,s2)==mul(g,g)==[[1,0],[0,1]]
assert [[mul(g,s1)[i][j]+mul(s1,g)[i][j] for j in range(2)] for i in range(2)]==[[0,0],[0,0]]
checks=dict(schema='minimal-normal-boundary-figure-checks/v1',exact_rational_cases=cases,exact_commutator_split=['1/2','1/4','1/2'],commutator_bound='5/4',exact_integer_Pauli_products=True,normal_minimal_domain='H1_0(0,1;C2)',normal_maximal_domain='H1(0,1;C2)',normal_self_adjoint=False,sum_domain='H1_0 intersect {h^-1 u in L2}',sum_self_adjoint_and_compact_resolvent_proved_in_text=True,rank_of_interval_average='2n',error_bound='||u_prime||/n',max_h_prime='sqrt(3)/9',physical_groupoid_realization_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
im.save(a.output_dir/'normal-boundary-regularization.png',compress_level=9)
(a.output_dir/'normal-boundary-regularization.svg').write_text('\n'.join(svg+['</svg>'])+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'NORMAL-BOUNDARY-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'rational_cases':5,'midpoint_B_square':'1/260','midpoint_J':'1/2','commutator_bound':'5/4','overflows':len(overflow)}))
