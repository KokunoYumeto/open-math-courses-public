"""Slow transport and the controlled normal core: CC0."""
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
 '<title>Compact transport defects and the controlled normal core</title>',
 '<desc>SL.1 to SL.15. The actual intrinsic field, compact additive arrow defects, a controlled normal core and the coefficient oscillator phase. The original-unit graph realization remains unproved.</desc>',
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
text(45,25,'Compact transport defects and a controlled normal core',43)
text(45,91,'SL.1–SL.15: actual JD field; fast normal reciprocal; slow transport weight; coefficient algebra retained.',29)
box(45,150,1155,440);text(77,182,'From order comparison to compact defects',34)
for y,s in [(246,'Θf=κ⁻¹, H=log(1+Θf); completed domains retained'),(315,'B=Ha−Hb bounded; ||B||≤½ max(log C,log C′)'),(384,'Ω=1+Σ H/(H+sn), sn≥2ⁿ selected adaptively'),(453,'Ωa−Ωb=Σ sn(Ha+sn)⁻¹B(Hb+sn)⁻¹ compact'),(525,'Actual arrow defect Sg = transported − receiving')]:text(78,y,s,28,GREEN if y>=453 else BLUE)
box(1240,150,1165,440);text(1273,182,'The exact normal-core statement',34)
for y,s in [(246,'Choose the same sn with Ω(δiκ) Hilbert-Schmidt'),(315,'Xi = lim δi qε(κ) κ; ||Xi||₂ ≤ ||Ω δiκ||₂'),(384,'δi(Ωκ)=Xi+Ωδiκ compact'),(453,'∇i(Ωb)=Xi Θf b+Ω∇ib on actual cutoff sections'),(525,'A derivative of Ω⁻¹ is not asserted')]:text(1273,y,s,28,GREEN if y>=384 and y<525 else BLUE)
box(45,630,2360,670);text(78,660,'Actual pair-swap model: fast difference unbounded; first log bounded; slow difference compact',33)
text(78,715,'Θf pair = diag(4ᵐ, 2·4ᵐ), P swaps the two entries; reciprocal-square order constants C=C′=4.',28)
text(78,769,'Explicit constant-field example sn=2ⁿ. Orange: first-log defect Bm. Blue: first 24 terms of slow defect dm.',27)
gx,gy,gw,gh=130,1214,1400,360
line([(gx,gy-gh),(gx,gy),(gx+gw,gy)],GRAY,3)
def xy(m,v):return gx+gw*(m-1)/31,gy-gh*v/.75
for value in [0,.25,.5,.75]:
 yy=gy-gh*value/.75;line([(gx,yy),(gx+gw,yy)],'#dbe5ee',1);text(62,yy-16,str(value),22,GRAY)
N=24;cases=[];slow=[];first=[];bounds=[]
for m in range(1,33):
 fast=4**m;H0=math.log1p(fast);H1=math.log1p(2*fast);B=H1-H0
 value=sum((2**n)*B/((H0+2**n)*(H1+2**n)) for n in range(1,N+1))
 tail=math.log(2)*2**(-N);upper=min(math.log(2),4*math.log(2)/H0)
 assert value>=0 and value+tail<=upper and B<=math.log(2)+1e-14
 first.append(xy(m,B));slow.append(xy(m,value));bounds.append(xy(m,upper))
 if m in [1,2,4,8,16,32]:cases.append(dict(m=m,fast_pair=[fast,2*fast],unbounded_fast_defect=fast,first_log_defect_sample=B,slow_24_term_sample=value,proved_tail_formula='log(2)/2^24',proved_tail_bound=tail,proved_slow_bound=upper))
line(first,RED,5);line(slow,BLUE,5);line(bounds,GREEN,4)
for m in [1,4,8,16,24,32]:text(xy(m,0)[0]-15,1230,str(m),22)
text(1060,1265,'m (pair index)',24)
text(1595,851,'Analytic bounds (SL.8, example)',31)
for y,s in [(922,'0 ≤ Bm ≤ log 2; Bm → log 2'),(996,'0 ≤ dm ≤ min(log 2, 4 log 2/Hm)'),(1070,'Omitted tail ≤ (log 2)·2⁻²⁴'),(1144,'dm → 0 ⇒ diagonal defect compact'),(1240,'Green: proved bound; samples give no limit proof')]:text(1595,y,s,27,GREEN)
box(45,1340,2360,170);text(78,1369,'The coefficient oscillator phase: CΩ=D³+B(1+Ω), with exterior parity and an even vacuum.',29)
text(78,1433,'After the explicit affine/linear homotopies, the coefficient class is 1A, A=C0(Y).',29,GREEN)
box(45,1550,2360,105,'#fff0e7',RED)
text(78,1574,'Still required: balanced realization at C0(T), differentiable inverse-module passage, physical sum and original Bott +1.',28,RED)
text(45,1680,'Original CC0 diagram. Proof SL.1–SL.15. Human context: Connes, A survey of foliations and operator algebras, §8.',23)
assert not overflow,overflow
for m in [1,2,4,8,16,32]:
 qa=Q(1,4**(2*m));qb=qa/4
 assert qa==4*qb and qb<=4*qa
checks=dict(schema='slow-transport-weight-checks/v1',pair_swap_order_constant=4,positive_involution_square=1,
 numerical_pair_samples=cases,sample_count=32,finite_sum_terms=N,
 first_log_limit='log(2)',slow_defect_limit=0,proved_tail='log(2)/2^24',
 plotted_quantities='numerical samples of the exact positive series; analytic tail and limit bounds are proved in the lesson',
 actual_compact_transport_weight_proved=True,actual_weighted_normal_core_proved=True,
 coefficient_identity_algebra='C0(Y)',original_unit_gamma_identity_inferred=False,
 original_graph_Bott_plus_one_proved=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append('</svg>')
im.save(a.output_dir/'slow-transport-weight.png')
(a.output_dir/'slow-transport-weight.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
(a.output_dir/'SLOW-TRANSPORT-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outputs=3,sample_count=32,pair_order_checks=True,overflows=overflow)))
