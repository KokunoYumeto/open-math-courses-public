"""CC0 source for the exact joint-domain schematic; no sampled spectrum is claimed."""
from pathlib import Path
import base64, html, json
from PIL import Image, ImageDraw, ImageFont
HERE=Path(__file__).resolve().parent
OUT=HERE.parents[1]/'figures';OUT.mkdir(exist_ok=True)
FONT=HERE/'fonts/DejaVuSans.ttf'
NOTICE=(HERE/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=1950,1150
im=Image.new('RGB',(W,H),'#f8fafc');draw=ImageDraw.Draw(im);fonts={}
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Independent spectral cutoffs and the exact graded tensor domain</title>',
 '<desc>Coordinate schematic of the square cutoff P2 and q=4 contour; graded square cancellation; exact graph and square moments; odd-kernel parity. The plane is not a specified spectral support.</desc>',
 '<metadata>'+html.escape('Original diagram and generator: CC0-1.0.\nUnmodified DejaVu Sans terms:\n'+NOTICE)+'</metadata>',
 '<style>@font-face{font-family:JointSans;src:url(data:font/ttf;base64,'+base64.b64encode(FONT.read_bytes()).decode()+')}text{font-family:JointSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']
def text(x,y,s,size=26,color='#14243a'):
 if size not in fonts:fonts[size]=ImageFont.truetype(str(FONT),size)
 draw.text((x,y),s,font=fonts[size],fill=color,anchor='lt')
 svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def rect(x,y,w,h,fill='#ffffff',stroke='#c9d4e2'):
 draw.rectangle((x,y,x+w,y+h),fill=fill,outline=stroke,width=3)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
def line(x,y,x2,y2,color='#6c7b90',width=3):
 draw.line((x,y,x2,y2),fill=color,width=width)
 svg.append(f'<path d="M{x},{y} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def arrow(x,y,x2,y2):
 line(x,y,x2,y2,'#245fad',4)
 pts=[(x2,y2),(x2-9,y2-14),(x2+9,y2-14)]
 draw.polygon(pts,fill='#245fad')
 svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="#245fad"/>')
text(48,35,'Independent spectral cuts and the graded sum',42)
text(48,104,'The first-order graph uses q; the square domain uses q². Grading cancels the mixed term.',25)
for x in [45,680,1315]:rect(x,170,590,870)
text(66,193,'1. The joint spectral plane',30)
text(66,245,'P₂ = E₁([−2,2]) ⊗ E₂([−2,2])',24)
# Equal scales: 62 pixels for one joint coordinate unit.
cx,cy,scale=340,525,62
rect(cx-2*scale,cy-2*scale,4*scale,4*scale,'#e6efff','#245fad')
line(cx-3*scale,cy,cx+3*scale,cy)
line(cx,cy+3*scale,cx,cy-3*scale)
draw.ellipse((cx-2*scale,cy-2*scale,cx+2*scale,cy+2*scale),outline='#22956a',width=4)
svg.append(f'<circle cx="{cx}" cy="{cy}" r="{2*scale}" fill="none" stroke="#22956a" stroke-width="4"/>')
for n in [-2,-1,1,2]:
 line(cx+n*scale,cy-5,cx+n*scale,cy+5)
 text(cx+n*scale-12,cy+12,str(n),20)
 line(cx-5,cy-n*scale,cx+5,cy-n*scale)
 text(cx-33,cy-n*scale-12,str(n),20)
text(cx+3*scale+8,cy-17,'x',26)
text(cx+14,cy-3*scale-24,'y',26)
text(72,733,'Blue square: the n = 2 cutoff.',23)
text(72,777,'Green circle: q = x² + y² = 4.',23,'#13734e')
text(72,821,'Each fixed vector has a finite μu.',23)
text(72,871,'No support or point mass is inferred.',23)
text(72,966,'Lemma 2; Lemma 3, JT.3–9',21)

text(702,193,'2. Why the mixed term vanishes',29)
text(703,245,'G = Γ₁ ⊗ 1,     D = X + GY',26)
rect(708,335,535,201,'#edf4ff')
text(728,360,'GX = −XG,     GY = YG',27)
text(728,411,'XY = YX on their common domain',23)
text(728,462,'XGY + GYX = 0',28)
arrow(975,547,975,603)
rect(708,615,535,110,'#eef9f1')
text(728,639,'D² = X² + Y² = q(F)',28)
text(728,685,'‖Du‖² = ‖Xu‖² + ‖Yu‖²',25)
text(706,787,'R± = (D ∓ i)(1 + q(F))⁻¹',25)
text(706,836,'‖R±‖ ≤ 1,    Ran R± = Q',26)
text(706,885,'Both imaginary resolvents are onto Q.',22)
text(706,966,'Proposition 4, JT.10–13',21)

text(1337,193,'3. Domains, cores and parity',30)
text(1337,245,'Q = D(X) ∩ D(Y)',28)
rect(1338,335,535,144,'#edf4ff')
text(1358,359,'D(D₁) ⊙ D(D₂)',28)
text(1358,408,'graph completion in ∫ (1 + q) dμu',23)
arrow(1605,490,1605,548)
rect(1338,560,535,132,'#eef9f1')
text(1358,583,'Q : first-order domain',28)
text(1358,634,'D(D²) : finite ∫ q² dμu',26)
text(1337,755,'Pker D = E₁({0}) ⊗ E₂({0})',25)
text(1337,812,'Circle kernel: one odd constant line.',22)
text(1337,864,'ker D⁺ = ker P* ⊗ that line',24)
text(1337,908,'ker D⁻ = ker P  ⊗ that line',24)
text(1337,966,'Corollary 5, JT.14; product grading',21)
text(48,1071,'Ordinary Hilbert-space statement. Module calculus, field decomposition, polar and trace arguments stay separate.',25)
svg.append('</svg>')
im.save(OUT/'joint-tensor-domain.png')
(OUT/'joint-tensor-domain.svg').write_bytes(('\n'.join(svg)+'\n').encode('utf-8'))
print(json.dumps({'dimensions':[W,H],'font':'fonts/DejaVuSans.ttf','mathematical_object':'square cutoff n=2 and q=4 contour; exact operator/domain/parity identities'}))
