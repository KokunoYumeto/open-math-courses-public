from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from html import escape
import json,hashlib
own=Path(__file__).resolve().parent
W,H=1800,1470
im=Image.new('RGB',(W,H),'#f5f7fa')
dr=ImageDraw.Draw(im)
font_regular='segoeui.ttf'
font_bold='segoeuib.ttf'
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<rect width="1800" height="1470" fill="#f5f7fa"/>']
ink='#17283d';muted='#455c73';blue='#175e91';green='#187166';gold='#8a5e13'
def rect(box,fill,outline='#bccbd8',radius=18,width=2):
    dr.rounded_rectangle(box,radius=radius,fill=fill,outline=outline,width=width)
    x,y,xx,yy=box
    svg.append(f'<rect x="{x}" y="{y}" width="{xx-x}" height="{yy-y}" rx="{radius}" fill="{fill}" stroke="{outline}" stroke-width="{width}"/>')
def text(x,y,s,size=30,color=ink,bold=False,center=False,maxwidth=None,math=False):
    names=('cambria.ttc','DejaVuSerif.ttf') if math else ((font_bold,'DejaVuSans-Bold.ttf') if bold else (font_regular,'DejaVuSans.ttf'))
    for name in names:
        try:
            font=ImageFont.truetype(name,size,index=1 if name=='cambria.ttc' else 0)
            break
        except OSError:
            pass
    else:
        font=ImageFont.load_default(size=size)
    b=dr.textbbox((0,0),s,font=font)
    width=b[2]-b[0]
    if maxwidth is not None:assert width<=maxwidth,(s,width,maxwidth)
    xx=x-width/2 if center else x
    dr.text((xx,y),s,font=font,fill=color)
    anchor='middle' if center else 'start'
    family='Cambria Math, serif' if math else 'Segoe UI, sans-serif'
    svg.append(f'<text x="{x}" y="{y+size}" text-anchor="{anchor}" font-family="{family}" font-size="{size}" font-weight="{700 if bold and not math else 400}" fill="{color}">{escape(s)}</text>')
def arrow(x,y,xx,yy,color=blue,width=4):
    import math
    dr.line((x,y,xx,yy),fill=color,width=width)
    a=math.atan2(yy-y,xx-x);l=14
    pts=[(xx,yy),(xx-l*math.cos(a-.48),yy-l*math.sin(a-.48)),
         (xx-l*math.cos(a+.48),yy-l*math.sin(a+.48))]
    dr.polygon(pts,fill=color)
    svg.append(f'<path d="M{x},{y} L{xx},{yy}" stroke="{color}" stroke-width="{width}"/>')
    svg.append('<polygon points="'+' '.join(f'{p[0]:.2f},{p[1]:.2f}' for p in pts)+f'" fill="{color}"/>')

text(900,32,'The actual weighted lamplighter core',52,bold=True,center=True,maxwidth=1680)
text(900,101,'Physical trace, normal dual trace and original joint cost',32,color=muted,center=True)

rect((55,164,835,355),'#ffffff')
text(85,181,'ACTUAL ORDINARY TUNNEL',25,color=blue,bold=True)
text(445,231,'M = L₀ ⊃ N = L₁ ⊃ L₂ ⊃ ···',40,center=True,maxwidth=725,math=True)
text(445,295,'Each triple has its defining cup and index d.',27,color=muted,center=True)
arrow(849,260,932,260)
rect((947,164,1745,355),'#ffffff')
text(977,181,'COMPATIBLE FINITE WORD COMMUTANTS',25,color=blue,bold=True)
text(1346,231,"R = (⋃ Aⱼ)''      S = (⋃ Bⱼ)''",37,center=True,maxwidth=750,math=True)
text(1346,295,'Common finite corners retain every old cup.',27,color=muted,center=True)

rect((55,390,1745,669),'#eaf3fa',outline='#97b9d3')
text(85,407,'FULL FIRST-LABEL CORNERS AND BOTH CENTER MEASURES  •  WM.25–WM.29',26,color=blue,bold=True)
text(430,455,'V = Z(R)',40,bold=True,center=True)
text(1370,455,'U = Z(S)',40,bold=True,center=True)
arrow(630,488,1170,488)
text(900,449,'ϑᵢ',32,color=blue,center=True)
text(900,522,'v pᵢ = ϑᵢ(v) pᵢ     and     pᵢ R pᵢ = S pᵢ',34,center=True)
text(900,572,'rᵢ = E_V(pᵢ) ≥ 1/d     •     τ(pᵢ) = wᵢ',32,center=True)
text(900,617,'τ_U(ϑᵢ(v)) = τ_V(rᵢ v) / wᵢ',31,color=blue,bold=True,center=True)

rect((55,704,1745,990),'#eaf6f1',outline='#8ebaaa')
text(85,721,'RIGHT MULTIPLICATION IN THE RIGHT-S MODULE  •  WM.30–WM.31',26,color=green,bold=True)
text(430,778,'ξ ↦ ξ pᵢ',36,bold=True,center=True,math=True)
text(430,831,'range = L²(R) pᵢ',33,center=True)
arrow(691,828,1004,828,color=green)
text(1340,776,'S-dimension = ϑᵢ(rᵢ⁻¹)',34,bold=True,center=True)
text(1340,831,'dual mass = 1 / (d wᵢ)',34,center=True)
text(900,895,'k₀ on branch pᵢU  =  ϑᵢ(rᵢ⁻¹) / (d wᵢ)',35,color=green,bold=True,center=True)
text(900,952,'Σ ϑᵢ(rᵢ⁻¹) = d · 1_U',27,color=green,center=True)

rect((55,1008,1745,1292),'#fff7e7',outline='#d0b176')
text(85,1025,'THE ORIGINAL JOINT OPERATOR  •  WM.32–WM.35',26,color=gold,bold=True)
text(900,1082,'w = E_D₀(k₀)     ℓ = E_D₀(k_C)',36,bold=True,center=True)
text(900,1140,'P₀(w − ℓ) = (c₀ − c₁)(r₁ − w₁)',35,center=True)
text(900,1202,'τ(d Q(|w − ℓ|)) ≥ d(c₀ − c₁)w₁(h₊ + h₋) > 0',35,color=gold,bold=True,center=True,maxwidth=1600)
text(900,1254,'Actual center witness:  τ(z) = h₊ > 0,   τ(p₁z) = −w₁h₋ < 0.',27,color=gold,center=True)

text(900,1324,'The strict bound tests the faithful inherited normal trace.',31,bold=True,center=True)
text(900,1371,'An annihilating compatible possibly singular state remains unconstructed here.',28,color=muted,center=True)
text(900,1419,'Human context: Sorin Popa (1994), Definition 3.1.1.  Formulas proved here.  CC0-1.0.',24,color=muted,center=True)
svg.append('</svg>')
(own/'weighted-nonfactor-joint-cost-v13.svg').write_text('\n'.join(svg),encoding='utf-8')
im.save(own/'weighted-nonfactor-joint-cost-v13.png')

print('Rendered the weighted-core SVG and PNG.')
