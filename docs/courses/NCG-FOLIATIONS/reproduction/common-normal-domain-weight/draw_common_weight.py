"""One normal and completed-arrow weight: CC0."""
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
W,H=2450,1540;INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>One normally differentiable weight with completed arrow domains</title>',
 '<desc>OP.1 to OP.14. Actual intrinsic JD field; a positive resolvent sum has compact first normal derivatives and completed genuine-arrow domains. Normalized phase transfer remains unproved.</desc>',
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
text(45,25,'One normal weight with completed genuine-arrow domains',43)
text(45,91,'OP.1–OP.14: the same actual JD field, the same arrow labels, and the prescribed inverse Spin-c coefficient.',29)
box(45,150,1155,460);text(77,182,'Compact normal derivative: actual whole-module limits',34)
for y,s in [(251,'k=√h; δi k compact; At=t(k+t)⁻¹ → 0 strongly'),(319,'Choose tn>0 with ||Atn (δi k) Atn|| ≤ η 2⁻ⁿ'),(387,'κ=ψ(k)=Σ tn k/(k+tn)  •  Σtn<∞'),(455,'δiκ=Σ tn²(k+tn)⁻¹(δik)(k+tn)⁻¹ compact'),(535,'ψ(s)/s → ∞ as s→0; g(x)=√x/φ(x) → 0')]:text(78,y,s,29,GREEN if y>=455 else BLUE)
box(1240,150,1165,460);text(1273,182,'Completed transport, with the adjoint proved',34)
for y,s in [(251,'φ(x)=ψ(√x);  b≤Ca ⇒ φ(b)²≤C φ(a)²'),(319,'Positive density: √r(s+t)/[π(r+s²)(r+t²)]'),(387,'Uε=(φ(a)+ε)⁻¹√b → U in operator norm'),(455,'DN=Σn≤N tn U(√b+tn)⁻¹ → D strong-star'),(535,'D=φ(a)⁻¹φ(b); ||D||≤√C; reverse range equality')]:text(1273,y,s,28,GREEN if y>=455 else BLUE)
box(45,650,2360,660);text(78,680,'Two-row transport test: the square-root tail stays at 1; the enlarged weight tail tends to zero',33)
text(78,736,'ε=4⁻ᵐ, a=diag(1,ε²), b=PεaPε, Pε²=1; b≤3a and a≤3b. Explicit sequence tn=4⁻ⁿ.',28)
text(78,794,'Blue: Lm=ε ψ(1)/ψ(ε). Green: proved upper bound 2/(3m). Orange: square-root lower-left coefficient 1.',26)
gx,gy,gw,gh=130,1204,1410,345
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
def xy(m,v):return gx+gw*(m-1)/31,gy-gh*v
for value in [0,.25,.5,.75,1]:
 yy=gy-gh*value;line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(62,yy-16,str(value),21,GRAY)
line([xy(1,1),xy(32,1)],RED,5)
N=24;A=sum(Q(1,4**j+1) for j in range(1,N+1));tail=Q(1,3*4**N)
cases=[];blue=[]
for m in range(1,33):
 B=sum(Q(1,1+4**(j-m)) if j>=m else Q(4**(m-j),1+4**(m-j)) for j in range(1,m+N+1))
 lower=A/(B+tail);upper=(A+tail)/B;bound=Q(2,3*m)
 assert Q(0)<lower<=upper<=bound and float(upper-lower)<1e-12
 blue.append(xy(m,float((lower+upper)/2)))
 if m in [1,2,4,8,16,32]:
  cases.append(dict(m=m,epsilon='1/'+str(4**m),coefficient_lower=float(lower),coefficient_upper=float(upper),proved_bound=str(bound),exact_rational_interval_checked=True))
line(blue,BLUE,5);line([xy(m,2/(3*m)) for m in range(1,33)],GREEN,4)
for m in [1,4,8,16,24,32]:text(xy(m,0)[0]-15,1220,str(m),22)
text(1150,1260,'m (actual scalar sample index)',24)
text(1610,865,'Exact mechanism (OP.14)',31)
for y,s in [(930,'ψ(ε)/ε = m−1/2 + tailm'),(997,'First m terms ≥ 1/2 each'),(1064,'ψ(1) ≤ Σ4⁻ⁿ = 1/3'),(1131,'Lm ≤ 2/(3m) → 0'),(1210,'Rational intervals enclose all 32 samples')]:text(1610,y,s,27,GREEN)
box(45,1350,2360,142,'#fff0e7',RED)
text(77,1372,'Closed: one compact normal reciprocal, completed arrow/displacement domains and infinitesimal normal form.',28,GREEN)
text(77,1429,'Still required: normalized phase controls, differentiable inverse-module passage, completed physical sum and Bott +1.',28,RED)
text(45,1510,'Original CC0 diagram; proof OP.1–OP.14. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow
checks=dict(schema='common-normal-domain-weight-checks/v1',two_row_order_constant=3,
 positive_integral_at_x_s_t_one='1/4',three_denominator_integral_over_pi='1/16',
 explicit_example_sequence='4^(-n)',sample_count=32,rational_tail='1/(3*4^24)',cases=cases,
 generic_sequence_selected_by_compact_derivative_bounds=True,
 complete_normal_and_arrow_weight_bridge=True,actual_normalized_generator_proved=False,
 original_Bott_plus_one_comparison_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'common-normal-domain-weight.png')
(a.output_dir/'common-normal-domain-weight.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
(a.output_dir/'COMMON-WEIGHT-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outputs=3,sample_count=32,exact_rational_bounds_passed=True,overflows=overflow)))
