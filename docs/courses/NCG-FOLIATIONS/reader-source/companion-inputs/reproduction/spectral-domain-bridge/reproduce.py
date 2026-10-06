"""Original CC0 diagram generator; uses only Pillow and the bundled unmodified font."""
from pathlib import Path
import base64, html, json, sys
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE/'figures'
OUT.mkdir(exist_ok=True)
FONT = HERE/'fonts/DejaVuSans.ttf'
NOTICE = (HERE/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W, H = 1900, 1050
im = Image.new('RGB', (W,H), '#f8fafc')
draw = ImageDraw.Draw(im)
fonts = {}
svg = [
 f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Spectral domains: graph cutoffs, supported inverse, antiunitary transport</title>',
 '<desc>Exact mechanisms of Lemma 1 and Propositions 2, 4 and 5. Arrows are labelled domain inclusions, inverse actions or transports.</desc>',
 '<metadata>'+html.escape('Original diagram/generator: CC0-1.0.\nUnmodified embedded DejaVu Sans font; complete terms:\n'+NOTICE)+'</metadata>',
 '<style>@font-face{font-family:BridgeSans;src:url(data:font/ttf;base64,'+base64.b64encode(FONT.read_bytes()).decode()+')}text{font-family:BridgeSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f8fafc"/>'
]
def text(x,y,s,size=26,color='#15243a'):
    if size not in fonts: fonts[size] = ImageFont.truetype(str(FONT), size)
    # Top anchoring is used in both raster and SVG; all diagram strings are plain text.
    draw.text((x,y),s,font=fonts[size],fill=color,anchor='lt')
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def rect(x,y,w,h,fill='#ffffff',stroke='#c9d4e2'):
    draw.rectangle((x,y,x+w,y+h),fill=fill,outline=stroke,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
def arrow(x,y,x2,y2,color='#245fad'):
    draw.line((x,y,x2,y2),fill=color,width=4)
    if x==x2:
        draw.polygon([(x2,y2),(x2-8,y2-13),(x2+8,y2-13)],fill=color)
        points=f'{x2},{y2} {x2-8},{y2-13} {x2+8},{y2-13}'
    else:
        draw.polygon([(x2,y2),(x2-13,y2-8),(x2-13,y2+8)],fill=color)
        points=f'{x2},{y2} {x2-13},{y2-8} {x2-13},{y2+8}'
    svg.append(f'<path d="M{x},{y} L{x2},{y2}" stroke="{color}" stroke-width="4"/><polygon points="{points}" fill="{color}"/>')

text(52,38,'Spectral domains: what the arrows preserve',42)
text(52,103,'Exact Hilbert-space mechanisms; no joint, field or module calculus is asserted.',25)
xs=[50,670,1290]
for x in xs:rect(x,165,560,765)
text(74,189,'1. Graph cutoffs',31)
text(74,237,'Cₙ = {|f| ≤ n, |g| ≤ n}',27)
text(74,280,'Pₙ = E(Cₙ),   Pₙ → I strongly',25)
rect(76,350,505,104,'#edf4ff')
text(96,373,'D(Tg) ∩ D(Tfg)',30)
text(96,414,'unclosed domain of Tf Tg',22)
arrow(329,463,329,526)
text(349,478,'inclusion',21)
rect(76,536,505,108,'#eef9f1')
text(96,558,'D(Tfg)',30)
text(96,600,'domain after graph closure',22)
text(76,690,'u ∈ D(Tfg)  ⇒  Pₙu ∈ D(Tf Tg)',23)
text(76,739,'Graph error squared:',23)
text(76,782,'∫ outside Cₙ (1 + |fg|²) dμu → 0',24)
text(76,858,'Lemma 1; Proposition 2, SC.4–6',21)

text(694,189,'2. Range and support',31)
text(694,237,'B = g(A),   P = E({g ≠ 0})',25)
text(694,280,'H = ker B ⊕ M,   M = PH',25)
rect(696,350,505,104,'#fff4e5')
text(716,373,'Ran B = D(C) ∩ M',29)
text(716,414,'C = (1/g)(A) on the support',22)
arrow(949,463,949,526)
text(969,478,'dense inclusion',20)
rect(696,536,505,108,'#eef9f1')
text(716,558,'M = closure(Ran B)',29)
text(716,600,'not generally the inverse domain',21)
text(696,690,'B : D(B) ∩ M → Ran B',24)
text(696,738,'C : Ran B → D(B) ∩ M',24)
text(696,787,'These two arrows are inverses.',23)
text(696,858,'Proposition 5, SC.13–14',21)

text(1314,189,'3. Antiunitary transport',31)
text(1314,237,'W : H → K onto, conjugate-linear',24)
text(1314,280,'B = W A W⁻¹ on W D(A)',25)
rect(1316,350,505,104,'#edf4ff')
text(1336,373,'E(C)   and   f(A)',29)
text(1336,414,'real projections; complex coefficients',20)
arrow(1569,463,1569,526)
text(1589,478,'transport by W',20)
rect(1316,536,505,108,'#eef9f1')
text(1336,558,'E_B(C)   and   conjugate(f)(B)',25)
text(1336,600,'on the transported domains',22)
text(1316,690,'Scalar measures at u and Wu agree.',22)
text(1316,738,'The squared-moment domain survives.',22)
text(1316,787,'Example: W(iA)W⁻¹ = −iB.',25)
text(1316,858,'Proposition 4, SC.10–11',21)
text(52,970,'The inverse is defined on the actual range; the unclosed product keeps the inner-factor domain.',26)
text(52,1012,'Proof locators: Lemma 1; Propositions 2, 4 and 5. All symbols refer to the accompanying lesson.',21)
svg.append('</svg>')
im.save(OUT/'spectral-domain-bridge.png')
(OUT/'spectral-domain-bridge.svg').write_bytes(('\n'.join(svg)+'\n').encode('utf-8'))
print(json.dumps({'dimensions':[W,H],'font_file':'fonts/DejaVuSans.ttf','font_calls':len(fonts),'figure':'figures/spectral-domain-bridge.png'}))
