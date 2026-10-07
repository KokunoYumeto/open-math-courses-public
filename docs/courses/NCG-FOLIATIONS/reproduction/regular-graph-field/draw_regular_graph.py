"""Exact proper-cutoff graph embedding and preserved coefficient types: CC0."""
from pathlib import Path
from fractions import Fraction as Q
import base64, html, json, math, io, re, hashlib, xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

import argparse
ROOT = Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,default=ROOT/'out')
parser.add_argument('--resources',type=Path,default=ROOT.parent/'labelled-geometric-kernel')
args=parser.parse_args();OUTPUT=args.output_dir;OUTPUT.mkdir(parents=True,exist_ok=True)
FONT_BYTES=(args.resources/'fonts/DejaVuSans.ttf').read_bytes()
NOTICE=(args.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=2400,1550
INK,BLUE,GREEN,RED,GRAY="#17283c","#17638d","#286d49","#b64932","#65737e"
im=Image.new("RGB",(W,H),"#f8fafc"); d=ImageDraw.Draw(im)
fonts={}; overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<title>Actual cutoff embedding and regular graph-field coordinates</title>',
     '<desc>Exact C2 cutoff matrix sample; source-coefficient absorption and preserved normal inverse. The physical graph Dirac domain remains an explicit obligation.</desc>',
     '<metadata>'+html.escape('Original drawing: CC0.\n'+NOTICE)+'</metadata>',
     '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(FONT_BYTES).decode()+')}text{font-family:LocalSans}</style>',
     f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']

def text(x,y,s,size=30,color=INK):
    if size not in fonts: fonts[size]=ImageFont.truetype(io.BytesIO(FONT_BYTES),size,layout_engine=ImageFont.Layout.BASIC)
    b=d.textbbox((x,y),s,font=fonts[size],anchor="lt")
    if b[0]<0 or b[1]<0 or b[2]>W or b[3]>H: overflow.append([s,list(b)])
    d.text((x,y),s,font=fonts[size],fill=color,anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')

def box(x,y,w,h,fill="white",color="#c9d5e3",width=3):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=color,width=width)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{color}" stroke-width="{width}"/>')

def line(x,y,xx,yy,color=BLUE,width=4):
    d.line((x,y,xx,yy),fill=color,width=width)
    svg.append(f'<path d="M{x},{y}L{xx},{yy}" stroke="{color}" stroke-width="{width}" fill="none"/>')

def arrow(x,y,xx,yy,color=BLUE):
    line(x,y,xx,yy,color)
    a=math.atan2(yy-y,xx-x)
    pts=[(xx,yy)]+[(xx-16*math.cos(a+b),yy-16*math.sin(a+b)) for b in [-.45,.45]]
    d.polygon(pts,fill=color)
    svg.append('<polygon points="'+' '.join(f'{px:.5f},{py:.5f}' for px,py in pts)+f'" fill="{color}"/>')

text(45,25,'Proper cutoff → actual regular graph field',48)
text(45,93,'RG.1–RG.13: anchor-preserving module maps, exact equivariance and the full normal coefficient.',31)
box(45,155,2310,765)
text(75,183,'Exact finite illustration: Γ=C₂={e,a}, a²=e; T is one point; M=Γ with left translation.',33)
text(75,235,'E=ℂ² with Uₐ swapping its coordinates; c(e)=1, c(a)=0; Σg c(g⁻¹m)²=1.',30)

box(90,340,590,325,'#edf4f8',BLUE)
text(122,370,'Input coefficient E',34)
text(122,432,'ξ = ξₑ δₑ + ξₐ δₐ',36)
text(122,497,'Uₐ: ξₑ ↔ ξₐ',34,BLUE)
text(122,573,'C = projection onto δₑ',30)
arrow(700,510,980,510)
text(712,405,'Vξ(g)=C U_g⁻¹ξ',29,BLUE)
text(716,552,'V*V = 1E',31,GREEN)

text(1030,301,'Source coefficient',30)
text(1195,353,'δₑ',34)
text(1615,353,'δₐ',34)
text(1033,430,'g=e',31)
text(1033,600,'g=a',31)
box(1160,412,365,145,'#e3f2e9',GREEN)
box(1580,412,365,145,'#f1f3f5',GRAY)
box(1160,582,365,145,'#e3f2e9',GREEN)
box(1580,582,365,145,'#f1f3f5',GRAY)
text(1230,456,'ξₑ δₑ',38,GREEN)
text(1728,456,'0',38,GRAY)
text(1230,626,'ξₐ δₑ',38,GREEN)
text(1728,626,'0',38,GRAY)
text(2020,404,'Lₐ swaps',31,BLUE)
text(2020,448,'arrow rows;',31,BLUE)
text(2020,502,'source',31,BLUE)
text(2020,546,'coefficient',31,BLUE)
text(2020,590,'stays fixed.',31,BLUE)
arrow(1972,437,1972,702)
text(85,770,'Actual target: ℓ²(Γ arrow label) ⊗ E(source).  The highlighted column is the invariant range of V.',31)
text(85,824,'LV = VU exactly.  This finite sample illustrates the embedding; it does not establish the general index.',30)
text(85,870,'General proof: compact central support bounds all active arrows; RG.5–RG.7 verify completion and the adjoint.',29)

box(45,955,2310,545)
text(75,982,'General normalized field and physical coefficient types',36)
labels=[('Eγ + regular copies',95,1080,580),('regular arrow field',880,1080,585),('graph correspondence',1665,1080,615)]
for s,x,y,w in labels:
    box(x,y,w,88,'#edf4f8',BLUE); text(x+20,y+25,s,32)
arrow(695,1124,860,1124);text(699,1040,'cutoff + source maps',23)
arrow(1485,1124,1645,1124);text(1490,1040,'counting / plaque',23)
text(86,1214,'ForG γ = 1R follows from the proved ηD product, preserved by exactly degenerate additions.',31,GREEN)
text(86,1271,'Normal factor retained: S⁻ with z_g⁻¹ρ_t(s_g), its grading and physical generators; right Cq stays last.',30)
text(86,1330,'Htrans = L²(G,νr ; r*S⁻) ⊗ ℓ²(ℕ) in each auxiliary grading — verified by elementary-section norms.',30)
text(86,1390,'MODULE AND REDUCED NORM PROVED.  Geometric generator, normal connection and closed graph domain remain.',29,RED)
text(86,1444,'The regular-coordinate phase is not labelled as a Dirac operator by generic unboundedification.',29)

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a): return [list(v) for v in zip(*a)]
V=[[Q(1),Q(0)],[Q(0),Q(0)],[Q(0),Q(1)],[Q(0),Q(0)]]
U=[[Q(0),Q(1)],[Q(1),Q(0)]]
L=[[Q(int(j==((i+2)%4))) for j in range(4)] for i in range(4)]
exact={'V_star_V_identity':matmul(transpose(V),V)==[[Q(1),Q(0)],[Q(0),Q(1)]],
       'L_V_equals_V_U':matmul(L,V)==matmul(V,U),
       'projection_diagonal':[matmul(V,transpose(V))[i][i] for i in range(4)]==[Q(1),Q(0),Q(1),Q(0)],
       'cutoff_square_sum_each_orbit_point':all(sum([Q(1),Q(0)][g^m]**2 for g in range(2))==1 for m in range(2))}
assert all(exact.values()) and not overflow
im.save(OUTPUT/'regular-graph-field.png')
svg.append('</svg>');(OUTPUT/'regular-graph-field.svg').write_text('\n'.join(svg),encoding='utf-8')
data={'schema':'regular-graph-field-figure/v1','license':'CC0','toy':'C2 acting on M=C2; T is a point',
      'target_order':['(g=e,coeff=e)','(g=e,coeff=a)','(g=a,coeff=e)','(g=a,coeff=a)'],
      'V':[[str(x) for x in row] for row in V],'U':[[str(x) for x in row] for row in U],
      'L':[[str(x) for x in row] for row in L],'exact_checks':exact,'text_canvas_overflows':overflow,
      'proof_locators':['RG.1-RG.7','RG.8-RG.12','RG.13'],
      'font_dependency':'Shared unchanged DejaVuSans.ttf; full font and notice embedded in the SVG',
      'font_sha256':hashlib.sha256(FONT_BYTES).hexdigest(),
      'human_source':'Connes, A survey of foliations and operator algebras (1982), the graph-operator problem; the original cutoff/module proofs are RG.1-RG.13',
      'scope':'module and reduced representation established from explicit PK input; geometric graph operator unfinished'}
(OUTPUT/'FIGURE-CHECKS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':exact,'canvas_overflows':len(overflow)}))
