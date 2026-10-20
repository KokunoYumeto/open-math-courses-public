"""Exact maps in the affine quotient construction of Theorem 4.38.

GPT-6.1 Sol (OpenAI), CC0 1.0.
"""
from pathlib import Path
from html import escape
parts=[]
def text(x,y,value,size=21,**attrs):
    attrs=' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" {attrs}>{escape(value)}</text>')
def box(x,y,w,h,color='white'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#c4cfdd"/>')
def arrow(x1,y1,x2,y2,color='#265ba8'):
    parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="2" marker-end="url(#arrow)"/>')
parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1000" viewBox="0 0 1200 1000" role="img" aria-labelledby="title desc">
<title id="title">One finite domain and the affine geometric quotient tower</title>
<desc id="desc">For j at least L, X_j is the entire inverse image of U_a in the fixed equation fibre. The commuting square has q_(j+1)=(q_j pi,z) from X_(j+1) to Y_j times affine d-space, vertical equation projection pi and target projection pr1, and q_j from X_j to Y_j. In a fixed lower equation fibre, the linear map T on g_(j+1) has right inverse S and kernel the full vertical orbit symbol. Polynomial expansion in z has invariant lower coefficients. The eventual transporter images T'_k are nonempty with surjective transitions and define a compatible formal arrow.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker></defs>
<rect width="1200" height="1000" fill="#f6f8fc"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#17283d">
''')
text(30,40,'One finite domain and the affine geometric quotient tower',26,font_weight=650)
text(30,77,'j ≥ L;  Xⱼ is the full inverse image of Uₐ in the fixed equation fibre.',22)
box(25,104,1150,442)
text(47,143,'The commutative quotient square — equation (4.88)',23,font_weight=600)
box(95,194,280,80,'#edf2fc');text(235,244,'Xⱼ₊₁',31,text_anchor='middle')
box(775,194,325,80,'#eaf4ed');text(937,244,'Yⱼ × Aᵈ',31,text_anchor='middle')
box(95,406,280,80,'#edf2fc');text(235,456,'Xⱼ',31,text_anchor='middle')
box(775,406,325,80,'#eaf4ed');text(937,456,'Yⱼ',31,text_anchor='middle')
arrow(391,234,757,234);text(574,213,'qⱼ₊₁ = (qⱼπ,z)',23,text_anchor='middle')
arrow(391,446,757,446);text(574,426,'qⱼ',24,text_anchor='middle')
arrow(235,289,235,389);text(263,340,'πⱼ₊₁,ⱼ',23)
arrow(937,289,937,389,'#2c6547');text(967,340,'pr₁',23)
text(48,519,'Left fibres: affine equation spaces.  Right fibres: Aᵈ with d=dim(gⱼ₊₁/ϖⱼ₊₁).',21)
box(25,568,1150,222)
text(47,606,'A fixed lower fibre: actual affine functions and full orbit level spaces',23,font_weight=600)
text(48,649,'z=T(v)+c,  TS=id;   ker T=ϖⱼ₊₁.   Each z-level is one full stabilizer orbit.',22)
text(48,691,'v=S(z−c)+w,  w∈ker T.   This is an exact polynomial coordinate split.',22)
text(48,734,'f=Σ_α h_α z^α: unique expansion; each h_α is a full lower invariant.',22,fill='#174880')
text(48,769,'All inverses and highest linear coefficients come from the same order-L ring.',21)
box(25,812,1150,164)
text(47,850,'Formal orbit separation: the eventual transporter images',23,font_weight=600)
text(150,901,"T′_L",28,text_anchor='middle');text(435,901,"T′_(L+1)",28,text_anchor='middle');text(745,901,"T′_(L+2)",28,text_anchor='middle');text(1050,901,'⋯',32,text_anchor='middle')
arrow(335,891,215,891);arrow(655,891,530,891);arrow(1010,891,840,891)
text(275,879,'onto',17,text_anchor='middle');text(590,879,'onto',17,text_anchor='middle');text(925,879,'onto',17,text_anchor='middle')
text(48,948,'Nonempty eventual images + onto transitions ⇒ one compatible admissible formal arrow.',21)
parts.append('</g></svg>')
svg='\n'.join(parts)+'\n'
if __name__=='__main__':
    Path(__file__).with_suffix('.svg').write_text(svg,encoding='utf-8',newline='\n')
