"""Reproduce the exact TR12 support/centralizer/return diagram (CC0 1.0)."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont

HERE=Path(__file__).resolve().parent
W,H=1800,1210
im=Image.new('RGB',(W,H),'#f7f8fc')
d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<title>Finite smooth representation selected by a compatible state</title>',
     '<desc>Exact support-corner and centralizer maps, arbitrary finite tower smoothness, original expectation mismatch and preserved cost minimum. CC0 1.0.</desc>',
     '<rect width="1800" height="1210" fill="#f7f8fc"/>']
fonts={}
def font(size,bold=False):
    key=(size,bold)
    if key not in fonts:
        for name in (('seguisb.ttf','DejaVuSans-Bold.ttf') if bold else ('segoeui.ttf','DejaVuSans.ttf')):
            try:
                fonts[key]=ImageFont.truetype(name,size)
                break
            except OSError:
                pass
        else:
            fonts[key]=ImageFont.load_default(size=size)
    return fonts[key]
def text(x,y,value,size=24,bold=False,color='#172033'):
    value=value.replace('⊂','subset').replace('⟨','<').replace('⟩','>').replace('𝔄','A^q').replace('𝔅','B^q')
    d.text((x,y),value,font=font(size,bold),fill=color)
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Segoe UI, sans-serif" font-size="{size}" font-weight="{600 if bold else 400}" fill="{color}">{escape(value)}</text>')
def rect(x,y,w,h,fill='#ffffff',stroke='#c9d2e3'):
    d.rounded_rectangle((x,y,x+w,y+h),radius=15,fill=fill,outline=stroke,width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def arrow(x1,y1,x2,y2,color='#526481'):
    d.line((x1,y1,x2,y2),fill=color,width=4)
    if y1==y2:
        points=[(x2,y2),(x2-12,y2-8),(x2-12,y2+8)]
    else:
        points=[(x2,y2),(x2-8,y2-12),(x2+8,y2-12)]
    d.polygon(points,fill=color)
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="4"/>')
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in points)}" fill="{color}"/>')

text(60,25,'A finite smooth representation selected by one compatible state',36,True)
text(60,80,'TR12.1–TR12.20  |  physical N ⊂ M and original E, P₀, τ, TrA, TrB retained',25,color='#415274')
xs=[60,660,1260]
for x in xs:
    rect(x,160,480,145)
    rect(x,395,480,125)
text(84,176,'Original B = ⟨M, eR⟩',30,True)
text(84,226,'Compatible M-central ψ, ψ|M = τ',22)
text(84,262,'Original center restriction may be singular',21,color='#526481')
text(684,176,'𝔅 = qB**q',30,True)
text(684,226,'q = supp ψ = supp(ψ|A**)',23)
text(684,262,'φ is normal and faithful on 𝔅',22,color='#526481')
text(1284,176,'Vψ = centralizer of φ in 𝔅',27,True)
text(1284,226,'τψ = φ|Vψ is finite, normal, faithful',21)
text(1284,262,'Γψ comes from bounded right actions',21,color='#526481')
arrow(548,225,648,225)
text(558,163,'qTq',23,True)
text(555,251,'UCP',21)
arrow(1148,225,1248,225)
text(1171,163,'Γψ',23,True)
text(1155,251,'normal UCP',20)
for x,label in [(300,'E'),(900,'Eᵠ'),(1500,'Eψ')]:
    arrow(x,317,x,384)
    text(x+15,336,label,24,True)
text(84,409,'Original A = ⟨N, eR⟩',28,True)
text(84,459,'Canonical normal faithful expectation E',21)
text(684,409,'𝔄 = qA**q',28,True)
text(684,459,'Eᵠ = E**|𝔅, original restriction EΝ',21)
text(1284,409,'Uψ = 𝔄 ∩ Vψ',28,True)
text(1284,459,'Eψ preserves the finite trace τψ',22)
arrow(548,455,648,455)
text(558,410,'qTq',23)
arrow(1148,455,1248,455)
text(1171,410,'Γψ',23)

rect(60,555,790,275,fill='#eef4ff')
text(85,575,'Physical embeddings at every finite stage',28,True)
text(85,625,'j(m) = qm is a faithful normal *-homomorphism.',24)
text(85,663,'L**(q)ij = δij qfi; repeat with each physical basis.',24)
text(85,701,'The same Jones cups and expectations remain.',24)
text(85,739,'N′ ∩ Mj commutes with Uψ for every finite j.',24)
text(85,778,'Both original physical relative-commutant traces remain.',22)

rect(885,555,855,275,fill='#f3f0ff')
text(910,575,'The original center expectation is different',28,True)
text(910,625,'αP₀ = θα,   θ = ℓ/w;   α = τψ|jψ(D₀)″.',24)
text(910,663,'The α-preserving map is Pα(t) = P₀(θ⁻¹t).',24)
text(910,701,'Λψ fixes the image jψ(t) = qι(t)q.',24)
text(910,739,'α(P₀ log θ − log θ) = α((θ − 1) log θ) ≥ 0.',24)
text(910,778,'The constructed finite trace keeps this original test.',22)

rect(60,865,1680,225,fill='#ffffff',stroke='#3c577f')
text(85,883,'Exact original-state return and preserved minimum',29,True)
text(85,929,'Λψ(T) = Γψ(qTq),   EψΛψ = ΛψE,   τψΛψ = ψ.',27)
text(85,973,'Every compatible η returns to ηΛψ on original B. If ψ(J_e) = 0, then Λψ(J_e) = 0.',24)
text(85,1013,'At an original minimizer m:  minη η(Λψ(a)) = m, attained by τψ. Here a is the original cost.',25,True)
text(85,1052,'The unrestricted existence of an original joint-balanced state remains unproved.',23,color='#8a2a2a')
text(60,1133,'Proof: TR12.1–TR12.20. Human context: Popa (1994), §§2.3–2.4, Definition 3.1.1 and Proposition 3.2.2.',22)
text(60,1170,'Schematic boxes and arrows; areas do not encode trace masses. CC0 1.0.',20,color='#526481')
svg.append('</svg>')
(HERE/'finite-smooth-return-v13.svg').write_text('\n'.join(svg)+'\n',encoding='utf8')
im.save(HERE/'finite-smooth-return-v13.png')
print('Rendered SVG and PNG.')
