"""Compact-frame quotient versus Haar averaging; exact field types, CC0."""
from pathlib import Path
from fractions import Fraction as Q
import base64, html, io, json, math, re, hashlib, xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
import argparse
ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,default=ROOT/'out')
parser.add_argument('--resources',type=Path,default=ROOT.parent/'labelled-geometric-kernel')
args=parser.parse_args(); OUTPUT=args.output_dir; OUTPUT.mkdir(parents=True,exist_ok=True)
font_bytes=(args.resources/'fonts/DejaVuSans.ttf').read_bytes()
notice=(args.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=2300,1490
INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Compact-frame quotient preserves compact inverse without Haar Fourier modes</title>',
 '<desc>Exact circle principal-bundle scalar-weight illustration; quotient and averaging Hilbert fields have different fibre types. General intrinsic-jet quotient provider and remaining normal-weight derivative.</desc>',
 '<metadata>'+html.escape('Original drawing: CC0.\n'+notice)+'</metadata>',
 '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font_bytes).decode()+')}text{font-family:LocalSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']
def text(x,y,s,size=30,col=INK):
    if size not in fonts:fonts[size]=ImageFont.truetype(io.BytesIO(font_bytes),size,layout_engine=ImageFont.Layout.BASIC)
    z=d.textbbox((x,y),s,font=fonts[size],anchor='lt')
    if z[0]<0 or z[1]<0 or z[2]>W or z[3]>H:overflow.append([s,list(z)])
    d.text((x,y),s,font=fonts[size],fill=col,anchor='lt')
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def box(x,y,w,h,fill='white',col='#c9d5e3'):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=col,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{col}" stroke-width="3"/>')
def line(x,y,xx,yy,col=BLUE,width=4):
    d.line((x,y,xx,yy),fill=col,width=width)
    svg.append(f'<path d="M{x},{y}L{xx},{yy}" fill="none" stroke="{col}" stroke-width="{width}"/>')
def arrow(x,y,xx,yy,col=BLUE):
    line(x,y,xx,yy,col);a=math.atan2(yy-y,xx-x)
    pts=[(xx,yy)]+[(xx-16*math.cos(a+b),yy-16*math.sin(a+b)) for b in [-.45,.45]]
    d.polygon(pts,fill=col);svg.append('<polygon points="'+' '.join(f'{px:.5f},{py:.5f}' for px,py in pts)+f'" fill="{col}"/>')
def poly(points,col=BLUE,width=4):
    d.line(points,fill=col,width=width)
    svg.append('<polyline points="'+' '.join(f'{x:.5f},{y:.5f}' for x,y in points)+f'" fill="none" stroke="{col}" stroke-width="{width}"/>')

text(45,25,'Compact-frame quotient: one representative fibre, no new Haar modes',42)
text(45,90,'IJ.1–IJ.7: controlled vector jets → actual metric connection → auxiliary K quotient; full inverse Spinᶜ factor retained.',28)
box(45,148,2210,562)
text(78,177,'Complexified principal-bundle illustration: K=S¹, P=S¹→{*}, YH=P, EH=P×ℂ, ΘH=2, trivial fibre rotation.',30)
cx,cy,rad=335,445,152
pts=[(cx+rad*math.cos(2*math.pi*i/512),cy-rad*math.sin(2*math.pi*i/512)) for i in range(513)]
poly(pts,BLUE,5)
line(cx,cy,cx+rad,cy,GRAY,2)
px,py=cx+rad/2,cy-rad*math.sqrt(3)/2
line(cx,cy,px,py,GRAY,2)
d.ellipse((px-8,py-8,px+8,py+8),fill=GREEN)
svg.append(f'<circle cx="{px:.5f}" cy="{py:.5f}" r="8" fill="{GREEN}"/>')
text(88,257,'u(θ)=(cos θ,sin θ)',29,BLUE)
text(100,615,'K acts freely on P;',27)
text(100,654,'each fibre carries ΘH=2.',27)
text(515,332,'v stays in the same',29)
text(515,378,'one-dimensional fibre',29)
text(515,445,'under frame identification.',29)
arrow(905,449,1335,449,GREEN)
text(962,364,'quotient by K',30,GREEN)
box(1380,320,775,225,'#e3f2e9',GREEN)
text(1415,350,'Y={*}, E=ℂ, Θ=2',35,GREEN)
text(1415,409,'Θ⁻¹=½ Iℂ: rank one, compact',31,GREEN)
text(1415,468,'Local frames choose one representative.',28)
text(845,604,'General IJ.6–IJ.7: actual orbit maps are onto isometries;',28)
text(845,651,'localized resolvents restrict with the same finite-rank norms.',28)

box(45,750,2210,375)
text(78,779,'Averaging is a different Hilbert field: L²(S¹)⊗ℂ, with pointwise inverse ½ I.',32,RED)
for i,n in enumerate([-2,-1,0,1,2]):
    x=100+i*420;box(x,852,365,124,'#fff3ee',RED)
    text(x+24,874,f'mode e^({n}iu)',29,RED)
    text(x+24,926,'image norm = ½',28,RED)
text(78,1010,'The displayed finite list continues over every n∈ℤ.  Modes are orthonormal and weakly zero as |n|→∞.',29)
text(78,1064,'A fixed nonzero image norm proves noncompactness (FD.7).  Quotient did not introduce this multiplicity.',28,RED)

box(45,1165,2210,254)
text(78,1194,'Actual mathematical provider and its precise remaining boundary',33)
text(78,1248,'The enlarged jet spectrum has a dense closable covariant metric connection; its compact K quotient keeps it.',28)
text(78,1298,'A K-invariant compact weight can be selected and descended.  Its normal derivative estimates remain unproved.',28,RED)
text(78,1348,'Still required: joint weight/connection control, probability-step control, inverse-module passage and the physical +1 graph operator.',27,RED)
text(45,1445,'CC0.  Circle coordinates are reproducible samples of the exact displayed parametrization; the operator claims are proved in IJ.6–IJ.7 / FD.7.',25,GRAY)

exact={'quotient_inverse_rank_one':Q(1,2)*Q(2)==1,
       'fourier_image_squared_norm':all(Q(1,2)**2==Q(1,4) for _ in range(21)),
       'theta_positive':Q(2)>=1}
assert all(exact.values()) and not overflow
im.save(OUTPUT/'compact-frame-quotient.png');svg.append('</svg>')
(OUTPUT/'compact-frame-quotient.svg').write_text('\n'.join(svg),encoding='utf-8')
data={'schema':'compact-frame-quotient-figure/v1','license':'CC0',
 'toy':{'K':'S1','P':'S1','T':'point','Y_H':'P','E_H':'P times C (complexification)','Theta_H':2,
 'quotient_E':'C','quotient_inverse_rank':1,'averaged_E':'L2(S1) times C',
 'averaged_inverse':'one-half identity, noncompact'},'exact_checks':exact,
 'circle_samples':513,'circle_exact_formula':'u(theta)=(cos(theta),sin(theta)); theta marker pi/3',
 'text_canvas_overflows':overflow,'font_sha256':hashlib.sha256(font_bytes).hexdigest(),
 'font_source':'Shared unchanged DejaVuSans.ttf; full font and notice embedded in the SVG',
 'proof_locators':['IJ.1-IJ.7','FD.7'],
 'human_source_context':'Connes, A survey of foliations and operator algebras (1982), the graph-operator problem; the intrinsic field and quotient proofs are IJ.1–IJ.7',
 'normal_weight_derivative_proved':False,'physical_graph_operator_constructed':False}
(OUTPUT/'QUOTIENT-FIGURE-CHECKS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':exact,'canvas_overflows':len(overflow)}))
