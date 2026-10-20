"""Exact local classification diagram, Theorem7.14. CC0-1.0."""
from pathlib import Path
from html import escape

parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1390" viewBox="0 0 1280 1390" role="img" aria-labelledby="title desc">
<title id="title">The quotient and vertical kernel classify transitive imprimitive plane actions</title>
<desc id="desc">All twelve combinations of quotient dimension and vertical kernel type. Low-dimensional coefficient and zero-index cases are retained and lead to the product and small normal forms. The diagram concerns generic regular complex analytic point actions.</desc>
<rect width="1280" height="1390" fill="#f8fafc"/>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:21px}.title{font-size:31px;font-weight:bold}.sub{font-size:25px;font-weight:bold}.small{font-size:18px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a=''if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(s)}</text>')
def box(x,y,w,h,color):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#94a3b8"/>')
text(42,48,'Every quotient / vertical-kernel case','title')
text(42,84,'Transitive imprimitive holomorphic plane germs; one chosen invariant curve foliation.','')
box(42,107,1196,93,'#e0f2fe')
text(640,145,'0 → k → g → h → 0,    X = a(x)∂x + b(x,y)∂y','sub math','middle')
text(640,178,'h acts on the transverse x-line; k acts along the leaves x = constant.','small','middle')
labels=[('dim h = 1','⟨p⟩'),('dim h = 2','⟨p, xp⟩'),('dim h = 3','⟨p, xp, x²p⟩')]
xs=[235,571,907];width=321
for x,(a,b)in zip(xs,labels):
    box(x,222,width,83,'#e2e8f0');text(x+width/2,254,a,'sub','middle');text(x+width/2,286,b,'math','middle')
rows=[
 ('k = c','projective vertical',[[('sᵧ ⊕ tₓ','sub math'),('product','small')],[('sᵧ ⊕ aₓ','sub math'),('product','small')],[('sᵧ ⊕ sₓ','sub math'),('product','small')]]),
 ('k = b(V)','affine vertical',[[('B₁(Σ)','sub math'),('dim V ≥ 2','small'),('dim V = 1: aᵧ ⊕ tₓ','small')],[('B₂(r), r ≥ 1','sub math'),('V = Pᵣ','math'),('r = 0: aₓ ⊕ aᵧ','small')],[('B₃(r), r ≥ 1','sub math'),('V = Pᵣ','math'),('r = 0: sₓ ⊕ aᵧ','small')]]),
 ('k = a(V)','abelian vertical',[[('A₁(Σ)','sub math'),('dim V ≥ 2','small'),('dim V = 1: small actions','small')],[('A₂(r,κ) or Jᵣ','sub math'),('r ≥ 1 for A₂; r ≥ 0 for J','small'),('r = 0 in A₂: Tκ','small')],[('A₃(r), r ≥ 1','sub math'),('r = 0: sₓ ⊕ tᵧ or Z','small'),('residual coefficient t = 0 or 1','small')]]),
 ('k = 0','faithful quotient',[[('Impossible','sub'),('dim g = 1 cannot be transitive','small')],[('Free affine action','sub'),('⟨q, xp + Y⟩','math'),('regular where x ≠ 0','small')],[('N or Δ','sub math'),('nilpotent / semisimple isotropy','small'),('two distinct local sl₂ actions','small')]])
]
for i,(label,desc,cells)in enumerate(rows):
    y=326+i*200
    text(42,y+45,label,'sub math');text(42,y+78,desc,'small')
    for x,lines in zip(xs,cells):
        box(x,y,width,178,'#ffffff')
        for j,(s,cls)in enumerate(lines):text(x+width/2,y+43+j*42,s,cls,'middle')
box(42,1151,1196,178,'#ecfdf5')
text(65,1189,'Exact coefficient mechanisms','sub')
text(65,1224,'V differentiation-invariant  ⇒  V = ⊕ e^(αᵢx) P_(nᵢ−1).','math')
text(65,1258,'Affine quotient  ⇒  polynomial blocks; projective quotient fixes the highest weight r.','small')
text(65,1293,'The affine extension leaves one coefficient t x^(r+1); it survives exactly at κ = r+1.','small')
text(42,1365,'Proof: Theorem 7.14. Parameter equivalence: Theorem 7.15. Foliation counts and multiplicities: Proposition 7.16.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
