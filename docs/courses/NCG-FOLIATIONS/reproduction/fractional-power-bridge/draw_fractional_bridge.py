"""Exact fractional derivative region and its conditional completed-domain bridge: CC0."""
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
W,H=2500,1640;INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>A sufficient compact normal derivative below the half-power</title>',
 '<desc>FB.1 to FB.7. Strict exponent region, exact quarter-power sample and closed derivative limit. The actual column factorization remains a premise.</desc>',
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
text(45,25,'A sufficient subcritical bridge: one inverse power for transport and normal forms',39)
text(45,84,'Actual anchored column S′=hᵝB with B adjointable is the premise; FB.1–FB.7 prove its derivative consequence.',29)
box(45,145,1400,835);text(77,179,'Strict exponent region: 0<α<½,  ½−α<β<½',35)
text(80,239,'The shaded interior makes the small-resolvent integral finite.',29)
left,right,top,bottom=160,1190,325,800
poly=[(left,top),(right,top),(right,bottom)]
d.polygon(poly,fill='#e3f2e9');svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in poly)+'" fill="#e3f2e9"/>')
line([(left,top),(left,bottom),(right,bottom)],GRAY,3)
line([(left,top),(right,top),(right,bottom)],RED,3,True)
line([(left,top),(right,bottom)],RED,4,True)
text(122,281,'β',34);text(1219,781,'α',34)
text(89,319,'½',30);text(1150,834,'½',30);text(139,834,'0',30)
def point(alpha,beta,col):
 x=left+float(2*alpha)*(right-left);y=bottom-float(2*beta)*(bottom-top)
 d.ellipse((x-9,y-9,x+9,y+9),fill=col);svg.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{col}"/>');return x,y
x,y=point(Q(1,4),Q(3,8),GREEN);text(x+24,y-26,'(¼,⅜): exponent −⅞',29,GREEN)
x,y=point(Q(1,4),Q(1,4),RED);text(250,710,'Boundary sample (¼,¼): exponent −1',28,RED)
text(80,887,'Diagonal α+β=½: ∫₀¹ dt/t diverges; boundary is excluded.',29,RED)
text(80,935,'Plot coordinates are exact fractions. Only the open shaded region is admitted.',26)
box(1485,145,970,835);text(1518,179,'Exact quarter-power sample',35)
text(1518,251,'α=¼, β=⅜;   α+β−½=⅛',32,GREEN)
text(1518,328,'Rₜ=(h+t)⁻¹; h=SS*',31,BLUE)
text(1518,393,'‖Rₜ δh Rₜ‖ ≤ ‖B‖ t⁻⁹⁄⁸',32,BLUE)
text(1518,458,'tᵅ factor: t⁻⁹⁄⁸ × t¹⁄⁴ = t⁻⅞',30,GREEN)
text(1518,532,'∫₀¹ t⁻⅞ dt = 8',34,GREEN)
text(1518,606,'∫₁∞ t⁻⁷⁄⁴ dt = 4/3',34,GREEN)
text(1518,687,'‖δh¹⁄⁴‖ ≤ c(¼) (8‖B‖ + ⁴⁄₃‖δh‖)',29,GREEN)
text(1518,763,'c(α) = (∫₀∞ uᵅ⁻¹/(1+u) du)⁻¹',27)
text(1518,847,'This estimate requires the actual factor B.',28,RED)
text(1518,909,'Fibre order alone does not supply it.',28,RED)
box(45,1020,2410,385);text(77,1050,'The closed normal derivative identifies the same reciprocal compact',34)
box(80,1120,625,118,'#e9f3f8',BLUE);text(102,1140,'kτ=(h+τ)ᵅ−τᵅI',33,BLUE);text(102,1190,'kτ→hᵅ; ‖kτ−hᵅ‖≤τᵅ',28,BLUE)
arrow(725,1177,877,1177)
box(902,1120,663,118,'#e3f2e9',GREEN);text(924,1140,'δkτ→X in compact norm',32,GREEN);text(924,1190,'X=c(α) ∫₀∞ tᵅ Rₜ δh Rₜ dt',28,GREEN)
arrow(1585,1177,1733,1177,GREEN)
box(1759,1120,642,118,'#e3f2e9',GREEN);text(1781,1140,'Closed δ: δhᵅ=X compact',31,GREEN);text(1781,1190,'Θ=h⁻ᵅ; Dom Θ=Ran hᵅ',28,GREEN)
text(80,1272,'JD gives actual G transport and displacement domains at this α. FQ gives the oscillator normal cross form when δhᵅ is compact.',28)
text(80,1325,'The conclusion uses S′=hᵝB on the completed module, with ½−α<β<½. It has not been proved for the actual orbit column.',28,RED)
box(45,1445,2410,135);text(77,1470,'The physical realization, phase compatibility, localized compactness and original Bott +1 still require proofs.',31,RED)
text(77,1524,'K-theory of the leaf space, Section 11AL; FB.1–FB.7. Original diagram and generator: CC0.',28)
assert not overflow,overflow
cases=[]
for alpha,beta in [(Q(1,4),Q(3,8)),(Q(1,3),Q(1,4)),(Q(1,8),Q(7,16))]:
 exponent=alpha+beta-Q(3,2);assert Q(0)<alpha<Q(1,2) and Q(1,2)-alpha<beta<Q(1,2) and exponent>-1
 cases.append({'alpha':str(alpha),'beta':str(beta),'zero_integrand_exponent':str(exponent),'small_integral':str(1/(exponent+1)),'large_integral':str(1/(1-alpha))})
assert cases[0]['zero_integrand_exponent']=='-7/8' and cases[0]['small_integral']=='8' and cases[0]['large_integral']=='4/3'
checks={'schema':'fractional-power-bridge-figure-checks/v1','admissible_cases':cases,'boundary_case':{'alpha':'1/4','beta':'1/4','zero_integrand_exponent':'-1','integrable':False},'actual_column_factorization_is_a_premise':True,'actual_JD_factorization_proved':False,'text_canvas_overflows':overflow,'canvas':[W,H]}
im.save(a.output_dir/'fractional-power-bridge.png',compress_level=9)
(a.output_dir/'fractional-power-bridge.svg').write_text('\n'.join(svg+['</svg>'])+'\n',encoding='utf-8',newline='\n')
(a.output_dir/'FRACTIONAL-POWER-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'finite_exponent_cases':3,'quarter_power_small_integral':8,'quarter_power_large_integral':'4/3','actual_JD_factorization_proved':False,'text_overflows':0}))
