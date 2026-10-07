"""Exact finite presentation code and the two intrinsic map classes: CC0."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, base64, hashlib, html, io, json, math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=ROOT/'out')
parser.add_argument('--resources', type=Path, default=ROOT.parent/'labelled-geometric-kernel')
args = parser.parse_args()
args.output_dir.mkdir(parents=True, exist_ok=True)
font_bytes = (args.resources/'fonts/DejaVuSans.ttf').read_bytes()
notice = (args.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
assert hashlib.sha256(font_bytes).hexdigest() == '3fdf69cabf06049ea70a00b5919340e2ce1e6d02b0cc3c4b44fb6801bd1e0d22'
W, H = 2500, 1840
INK, BLUE, GREEN, RED, GRAY = '#17283c', '#17638d', '#286d49', '#b64932', '#65737e'
im = Image.new('RGB', (W,H), '#f8fafc')
d = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<title>Countable presentation maps and the target-retaining pullback</title>',
       '<desc>Exact six by three normalized incidence matrix, nine least-index codes, full image mass 30, and a strict inclusion of two intrinsic Borel map classes. The finite example does not parametrize a nonsmooth quotient.</desc>',
       '<metadata>'+html.escape('Original drawing: CC0.\n'+notice)+'</metadata>',
       '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font_bytes).decode()+')}text{font-family:LocalSans}</style>',
       f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']

def text(x,y,s,size=31,col=INK):
    if size not in fonts:
        fonts[size] = ImageFont.truetype(io.BytesIO(font_bytes),size,layout_engine=ImageFont.Layout.BASIC)
    bounds = d.textbbox((x,y),s,font=fonts[size],anchor='lt')
    if bounds[0]<0 or bounds[1]<0 or bounds[2]>W or bounds[3]>H:
        overflow.append([s,list(bounds)])
    d.text((x,y),s,font=fonts[size],fill=col,anchor='lt')
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')

def box(x,y,w,h,fill='white',col='#c9d5e3'):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=col,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{col}" stroke-width="3"/>')

def arrow(x,y,xx,yy,col=BLUE):
    d.line((x,y,xx,yy),fill=col,width=4)
    svg.append(f'<path d="M{x},{y}L{xx},{yy}" fill="none" stroke="{col}" stroke-width="4"/>')
    a=math.atan2(yy-y,xx-x)
    points=[(xx,yy)]+[(xx-16*math.cos(a+b),yy-16*math.sin(a+b)) for b in [-.45,.45]]
    d.polygon(points,fill=col)
    svg.append('<polygon points="'+' '.join(f'{px:.5f},{py:.5f}' for px,py in points)+f'" fill="{col}"/>')

classes = [(0,3),(1,2,5),(4,)]
weights = [Q(2),Q(3),Q(5)]
enumerations = [(0,1,2,3,4,5),(5,4,3,2,1,0),(2,0,4,5,3,1)]
class_of = {a:i for i,cls in enumerate(classes) for a in cls}
codes, indicators, normalized, uniform, raw = [], [], [], [], []
for b,enum in enumerate(enumerations):
    minima = {i:min(j for j,a in enumerate(enum) if a in cls) for i,cls in enumerate(classes)}
    reps = {i:enum[j] for i,j in minima.items()}
    column = [int(a==reps[class_of[a]]) for a in range(6)]
    assert all(sum(column[a] for a in cls)==1 for cls in classes)
    codes.append([{'b':b,'j':j,'a':enum[j],'source_class':class_of[enum[j]]} for j in sorted(minima.values())])
    indicators.append(column)
    normalized.append(sum(weights[class_of[a]]*column[a] for a in range(6)))
    uniform.append(sum(weights[class_of[a]]/len(classes[class_of[a]]) for a in range(6)))
    raw.append(sum(weights[class_of[a]] for a in range(6)))
assert normalized==uniform==[Q(10)]*3 and raw==[Q(18)]*3
assert [[r['j'] for r in col] for col in codes]==[[0,1,4],[0,1,2],[0,1,2]]
assert [[r['a'] for r in col] for col in codes]==[[0,1,4],[5,4,3],[2,0,4]]

text(45,25,'Countable presentation maps: retain the target point in the pullback',43)
text(45,87,'Theorems 5.35–5.36 and Corollary 5.37; exact finite example, CP.4–CP.11.',31)

box(45,150,1400,830)
text(77,183,'Normalized source relation cutoff at each target point',34)
text(77,239,'Source classes C₀={0,3}, C₁={1,2,5}, C₂={4}',31)
text(91,300,'source a',28,GRAY)
text(274,300,'class',28,GRAY)
text(424,300,'unit weight',28,GRAY)
for b,x in enumerate((630,880,1130)):
    text(x+49,300,'b'+str(b),34,BLUE)
for a in range(6):
    y=361+76*a
    i=class_of[a]
    text(105,y+17,str(a),31)
    text(278,y+17,f'C{i}',31)
    text(472,y+17,str(weights[i]),31)
    for b,x in enumerate((630,880,1130)):
        selected=indicators[b][a]
        box(x,y,206,62,'#e3f2e9' if selected else '#f1f4f8',GREEN if selected else '#d6dde5')
        text(x+89,y+15,str(selected),34,GREEN if selected else GRAY)
text(80,841,'For every b and source class: Σ c(a,b)=1',33,GREEN)
text(80,902,'μ(N₁)=18; one point per source leaf has mass 10.',31)

box(1485,150,970,830)
text(1518,183,'Least indices and the full image',34)
text(1518,247,'Row enumerations σ(b):',30,GRAY)
for b,enum in enumerate(enumerations):
    text(1518,303+58*b,f'b{b}: '+','.join(str(a) for a in enum),31,BLUE)
text(1518,506,'Codes (b,j)',29,GRAY)
text(1945,506,'representatives a',29,GRAY)
for b,col in enumerate(codes):
    js=','.join(str(r['j']) for r in col)
    aa=','.join(str(r['a']) for r in col)
    text(1518,560+63*b,f'b{b}: j={js}',31,GREEN)
    text(1945,560+63*b,f'a={aa}',31,GREEN)
text(1518,770,'9 codes; weighted mass 10 per b.',31,GREEN)
text(1518,829,'Full target presentation mass: 30.',34,GREEN)
text(1518,900,'Raw incidence: 54; class sums 2,3,1.',29,RED)

box(45,1020,2410,350)
text(77,1050,'Borel coding at a fixed target point; every target presentation is then pulled back',34)
box(80,1116,612,122,'#e9f3f8',BLUE)
text(103,1139,'Rₕ ⊂ N₁ × N₂',33,BLUE)
text(103,1189,'source E₁ classes at fixed b',28,BLUE)
arrow(714,1174,882,1174)
box(904,1116,610,122,'#e3f2e9',GREEN)
text(927,1139,'C ⊂ N₂ × ℕ₀; β(a,b)=(b,m)',30,GREEN)
text(927,1189,'π(b,j)=b; r(b,j)=q₁σⱼ(b)',28,GREEN)
arrow(1538,1174,1706,1174,GREEN)
box(1728,1116,677,122,'#e3f2e9',GREEN)
text(1751,1139,'Cᵧ={(z,y): π(z)=s(y)}',30,GREEN)
text(1751,1189,'q₂s(y)=p(y); retain that y',28,GREEN)
text(80,1265,'m=min{j: b∈Dⱼ, σⱼ(b) E₁ a}; C contains one code per source leaf and that target point.',30)
text(80,1312,'For id on a nonsmooth leaf quotient, C models the transversal. It is not a global quotient selector.',29,RED)

box(45,1410,2410,345)
text(77,1440,'Two intrinsic map categories: the inclusion is strict',34)
box(80,1510,1288,185,'#edf4fa',BLUE)
text(102,1528,'Presentation Borel (pullback category)',31,BLUE)
text(102,1580,'Ordinary circle → point: allowed; image on Y is #Y.',28,BLUE)
box(1440,1510,965,185,'#e3f2e9',GREEN)
text(1463,1528,'Presentation-object preserving',30,GREEN)
text(1463,1580,'Borel incidence + countable coarse fibres',27,GREEN)
text(1463,1628,'idQ and transversal circle → irrational Q',27,GREEN)
arrow(1418,1653,1390,1653,GREEN)
text(80,1717,'Irrational nonsmooth Q → point: weak graph Borel, but outside both categories.',28,RED)
text(45,1790,'Finite matrix = finite standard Borel model. It does not parametrize the nonsmooth quotient or provide a global leaf selector.',27,GRAY)

assert not overflow, overflow
report={'schema':'countable-presentation-map-finite-checks/v1','classes':[list(c) for c in classes],
        'unit_weights':[str(w) for w in weights],'enumerations':[list(e) for e in enumerations],
        'least_index_codes':codes,'cutoff_columns':indicators,'class_normalization_sums':[[sum(col[a] for a in cls) for cls in classes] for col in indicators],
        'complete_transversal_mass':'18','coarse_source_presentation_mass':'10','normalized_column_integrals':[str(x) for x in normalized],
        'uniform_column_integrals':[str(x) for x in uniform],'normalized_full_image':'30','raw_incidence_mass':'54',
        'raw_class_sums':[len(c) for c in classes],'code_count':sum(len(c) for c in codes),'proof_locators':['CP.4','CP.5','CP.6','CP.7','CP.8','CP.9','CP.10','CP.11'],
        'scope':'Finite exact arithmetic verifies the displayed model; it proves no descriptive-set-theoretic theorem and does not parametrize a nonsmooth quotient.',
        'canvas':[W,H],'text_canvas_overflows':overflow,'font_sha256':hashlib.sha256(font_bytes).hexdigest().upper()}
im.save(args.output_dir/'countable-probe-maps.png',compress_level=9)
(args.output_dir/'countable-probe-maps.svg').write_text('\n'.join(svg+['</svg>'])+'\n',encoding='utf-8',newline='\n')
(args.output_dir/'COUNTABLE-PROBE-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'finite_model_cases':3,'code_count':9,'normalized_image':30,'raw_incidence':54,'text_overflows':0}))
