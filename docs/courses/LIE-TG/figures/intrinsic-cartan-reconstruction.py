from pathlib import Path
from html import escape

OUT=Path(__file__).resolve().parent
def text(x,y,value,size=23,weight='normal',fill='#18354a'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(value)}</text>'
def rect(x,y,w,h,fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#c4d3dd"/>'
def arrow(x1,y1,x2,y2):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="#315c95" stroke-width="2.5" marker-end="url(#arrow)"/>'

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="895" viewBox="0 0 1100 820" role="img" aria-labelledby="title desc">',
    '<title id="title">Cartan reconstruction and an intrinsic symmetry</title>',
    '<desc id="desc">A Cartan-preserving action covering a point map is forced by the transformed-graph recurrence. Holonomic planes recover the next jet. The intrinsic action x prime equals x plus s, u prime equals u plus s p, p prime equals p preserves the equation u xx equals zero but fails to descend to the original point space.</desc>',
    '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#315c95" stroke-width="1.5"/></marker></defs>',
    '<rect width="1200" height="895" fill="#fbfcfe"/>',
    '<g font-family="DejaVu Sans,Arial,sans-serif">',
    text(30,42,'Cartan reconstruction: the point-covering hypothesis matters',26,'bold'),
    rect(25,65,1050,290,'#edf3fb'),
    text(45,102,'Theorem 4.40 · holonomic planes determine every next jet',23,'bold'),
    text(90,160,'Eʲ⁺¹'),text(730,160,'Eʲ⁺¹'),
    arrow(185,153,690,153),text(325,138,'Aʲ⁺¹ = g⁽ʲ⁺¹⁾ | Eʲ⁺¹',21),
    text(90,270,'Eʲ'),text(730,270,'Eʲ'),
    arrow(175,263,690,263),text(340,248,'Aʲ = g⁽ʲ⁾ | Eʲ',21),
    arrow(120,177,120,232),arrow(760,177,760,232),
    text(145,212,'π',20),text(784,212,'π',20),
    text(45,315,'eʲ⁺¹ ↦ (eʲ, L(eʲ⁺¹)) is injective: du[α](Dᵢ) recovers u[α+eᵢ].',21),
    rect(25,375,1050,140,'#f1f8f5'),
    text(45,411,'The forced recurrence · det C ≠ 0 on the graph chart',23,'bold'),
    text(45,453,'Cⁱⱼ = DⱼXⁱ,     U′[α+eᵢ] = Σⱼ (C⁻¹)ʲᵢ DⱼU′[α]',25),
    text(45,490,'Initial values (X,U)=g(x,u) force the whole prolongation.  Theorem 4.40, (4.101).',20),
    rect(25,535,1050,210,'#fff6eb'),
    text(45,573,'Intrinsic example · uₓₓ = 0,   p = uₓ,   D = ∂ₓ + p∂ᵤ',23,'bold'),
    text(45,616,'x′ = x+s,     u′ = u+sp,     p′ = p',25),
    text(45,653,'D(x′)=1, D(u′)=p′, D(p′)=0: the Cartan line is preserved.',21),
    text(45,690,'θ′ pulls back to θ+s dp,  θ=du−p dx.  For s≠0 there is no map on (x,u).',20),
    text(45,725,'In (x,b=u−px,p) these are translations of x.  Example 4.41; set a=h=c=d=0.',20),
    text(30,778,'Theorem 4.40; Example 4.41.  The bottom panel is the scalar u projection.',17),
    text(30,803,'Scope context: Kruglikov–Lychagin, arXiv:1111.5480v3 §0.1.  GPT-6.1 Sol (OpenAI). CC0 1.0.',15),
    '</g></svg>']
svg='\n'.join(parts)+'\n'
if __name__=='__main__':
    (OUT/'intrinsic-cartan-reconstruction.svg').write_bytes(svg.encode('utf-8'))
    print(str(OUT/'intrinsic-cartan-reconstruction.svg'))
