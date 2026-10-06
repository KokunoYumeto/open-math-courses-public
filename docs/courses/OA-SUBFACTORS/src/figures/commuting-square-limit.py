"""A fixed frame and its actual limit corner. CC0; regenerate with Python."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="640" viewBox="0 0 540 640" role="img" aria-labelledby="title desc">',
         '<title id="title">A finite frame identifies the limit basic construction</title>',
         '<desc id="desc">A nondegenerate commuting square has horizontal index kappa and vertical index c. The vertical frame in Q0 transports to every Qn over Pn. Its fixed Gram projection p gives M1 equals p M_m(N) p, with normalized trace c inverse times the unnormalized matrix trace. Repeating identifies every level of the Jones tower.</desc>',
         '<rect width="540" height="640" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:18px}.small{font-size:16px}</style>']

def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y,title,lines,height=115):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+29,title,'heading','middle')
    for i,line in enumerate(lines):
        text(270,y+61+26*i,line,'label' if i==0 else 'small','middle')

text(24,33,'A finite square produces an inclusion','title')
text(24,64,'Horizontal index κ; vertical index c.','small')
for y,labels in [(112,['Q₀','Q₁','Qₙ','M']), (209,['P₀','P₁','Pₙ','N'])]:
    for x,label in zip([62,176,334,470],labels):
        text(x,y,label,'label','middle')
    text(270,y,'⋯','label','middle')
    for x1,x2 in [(86,148),(360,447)]:
        parts.append(f'<path d="M{x1} {y-6} H{x2}" stroke="#426987" stroke-width="2"/>')
        text((x1+x2)/2,y-18,'⊂','small','middle')
for x in [62,176,334,470]:
    text(x,164,'∪','label','middle')
text(116,149,'κ','small','middle')
text(80,174,'c','small')
text(270,249,'Qₙ = span(Q₀Pₙ); E_Pₙ|Q₀ = E_P₀','small','middle')
box(277,'One vertical frame at every level',[
    'uᵢ ∈ Q₀;  x = Σᵢ uᵢ E_Pₙ(uᵢ* x)',
    'Σᵢ uᵢuᵢ* = c1;  pᵢⱼ = E_P₀(uᵢ* uⱼ).'])
box(413,'The matrix corner is the actual tower level',[
    'M₁ = p Mₘ(N) p;  τ₁ = c⁻¹(τ_N ⊗ Trₘ)',
    'Trₘ is unnormalized; (τ_N ⊗ Trₘ)(p) = c.'])
box(549,'Repeat with the common finite Jones projection',[
    'Theorem 30.4 and Proposition 30.5.'],height=73)
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
