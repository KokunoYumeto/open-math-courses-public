"""Original CC0 mathematical diagrams; all arrows and signs are proof-bound."""
from pathlib import Path
import argparse, base64, html, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, default=HERE/'figures')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
FONT = HERE/'fonts/DejaVuSans.ttf'
NOTICE = (HERE/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=2600,1500
im=Image.new('RGB',(W,H),'#f8fafc')
draw=ImageDraw.Draw(im)
fonts={}
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Proper factorization, ordinary calibration and the shifted simplex kernel</title>',
 '<desc>Exact typed even KK arrows through a proper algebra. Below: two ordinary contractions, and the exact compressed Clifford matrix for a two-vertex probability with its even kernel.</desc>',
 '<metadata>'+html.escape('Original diagram and generator: CC0-1.0.\n'+NOTICE)+'</metadata>',
 '<style>@font-face{font-family:FactorSans;src:url(data:font/ttf;base64,'+base64.b64encode(FONT.read_bytes()).decode()+')}text{font-family:FactorSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']

def text(x,y,s,size=30,color='#17283c'):
    if size not in fonts: fonts[size]=ImageFont.truetype(str(FONT),size,layout_engine=ImageFont.Layout.BASIC)
    draw.text((x,y),s,font=fonts[size],fill=color,anchor='lt')
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')

def line(x,y,xx,yy,color='#62758d',width=3):
    draw.line((x,y,xx,yy),fill=color,width=width)
    svg.append(f'<path d="M{x},{y}L{xx},{yy}" stroke="{color}" stroke-width="{width}" fill="none"/>')

def box(x,y,w,h,fill='#fff',border='#c9d5e3'):
    draw.rectangle((x,y,x+w,y+h),fill=fill,outline=border,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{border}" stroke-width="3"/>')

def arrow(x,y,xx,yy,color='#245fad'):
    line(x,y,xx,yy,color,4)
    a=math.atan2(yy-y,xx-x)
    pts=[(xx,yy)]+[(xx-18*math.cos(a+b),yy-18*math.sin(a+b)) for b in [-.45,.45]]
    draw.polygon(pts,fill=color)
    svg.append('<polygon points="'+' '.join(f'{a:.3f},{b:.3f}' for a,b in pts)+f'" fill="{color}"/>')

text(55,35,'Proper Bott–Dirac factorization with ordinary index +1',47)
text(55,111,'Discrete Γ; X = Prob(Y); B is the proper phase-space Bott algebra; A is the universal proper algebra.',31)
box(55,178,2490,510)
text(85,203,'All upper arrows are even Γ-equivariant KK morphisms (ST.4–5).',32)

nodes=[(95,292,220,'C'),(435,292,340,'C(X)'),(895,292,300,'B'),(1315,292,435,'B ⊗ A'),(1870,292,595,'C(X) ⊗ A')]
for x,y,w,label in nodes:
    box(x,y,w,105,'#edf4ff')
    text(x+28,y+31,label,36)
for x,xx,label in [(315,435,'u'),(775,895,'η_X'),(1195,1315,'T_B'),(1750,1870,'d_X ⊗ 1')]:
    arrow(x+7,345,xx-7,345)
    text(x+12,255,label,28)
arrow(2300,410,2300,522)
text(2327,435,'e_A',29)
box(1870,536,595,100,'#eef9f1')
text(1900,565,'A   — D →   C',36)
text(90,449,'η is the composite to A.',32)
text(90,504,'C₀(M) → ZM(A) is nondegenerate;',31)
text(90,550,'the half-mass action on M is proper.',31)
text(900,463,'ForΓ(ηD) = +1',39,'#16764b')
text(900,530,'No equivariant γ = 1 is required.',29)
text(900,586,'The reduced scalar class is κ (ST.9).',29)

box(55,725,1210,700)
box(1305,725,1240,700)
text(83,750,'Ordinary contractions keep the coefficient types',32)
text(87,823,'ψ: W → M   contracts to m₀',32)
text(87,886,'Φ: M → X   contracts to x₀',32)
text(87,950,'T_B  →  1_B ⊗ θ_m₀',32)
text(87,1013,'e_A  →  ev_x₀ ⊗ 1_A',32)
box(84,1080,1150,118,'#eef9f1')
text(109,1100,'u · ForΓ(η_X d_X) · ev_x₀ · (θ_m₀ D)',30)
text(109,1153,'= u · 1_C(X) · ev_x₀ · 1_C = +1',30)
text(88,1246,'ST.1, ST.6–8; all contractions occur after forgetting Γ.',24)
text(88,1297,'Compact source supports have compact homotopy images.',24)
text(88,1348,'No Γ-fixed probability or scalar equivariant evaluation is used.',23)

text(1334,750,'Exact shifted simplex kernel (UD.4, UD.9)',32)
text(1335,820,'μ = (1/4, 3/4),   ξ = (1/2, √3/2, 0)',30)
text(1335,876,'Basis: e₁, e₂, e₁∧e₂; parity: even, even, odd',28)
text(1350,949,'F_μ =',34)
matrix_x,matrix_y=1520,938
line(matrix_x-15,matrix_y,matrix_x-15,matrix_y+183,'#17283c',3)
line(matrix_x+525,matrix_y,matrix_x+525,matrix_y+183,'#17283c',3)
for i,row in enumerate([['0','0','−√3/2'],['0','0','1/2'],['−√3/2','1/2','0']]):
    for j,s in enumerate(row): text(matrix_x+175*j+12,matrix_y+61*i+9,s,31)
text(2112,948,'F_μ ξ = 0',31,'#16764b')
text(2112,1007,'ξ is even.',30,'#16764b')
text(1338,1154,'ζ = (−√3/2, 1/2, 0)  ⇄  e₁∧e₂',31)
text(1338,1211,'F_μ ζ = e₁∧e₂,   F_μ(e₁∧e₂) = ζ',30)
text(1338,1270,'F_μ² = 1 − P_ξ; the complement is invertible.',28)
text(1338,1325,'The single even kernel gives +1, not −1.',30,'#16764b')
svg.append('</svg>')
im.save(args.output/'proper-factorization.png')
(args.output/'proper-factorization.svg').write_text('\n'.join(svg),encoding='utf-8',newline='\n')
(args.output/'render-data.json').write_text(json.dumps({'schema':'proper-factorization-exact-figure/v1','canvas':[W,H],'scope':'typed even Γ-KK diagram; ordinary contractions; exact two-vertex Clifford sample','proof_locators':['ST.4','ST.5','ST.6','ST.7','ST.8','ST.9','UD.4','UD.9'],'sample':{'mu':['1/4','3/4'],'xi':['1/2','sqrt(3)/2','0'],'F':[['0','0','-sqrt(3)/2'],['0','0','1/2'],['-sqrt(3)/2','1/2','0']],'parity':['even','even','odd'],'kernel_index':1}},indent=2)+'\n',encoding='utf-8',newline='\n')
print('Rendered proper-factorization.png and paired SVG.')
