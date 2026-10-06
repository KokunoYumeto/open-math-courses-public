"""Exact operator-action diagram for the finite tracial commutation proof."""
from pathlib import Path
from xml.sax.saxutils import escape
out=Path(__file__).with_suffix('.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="650" viewBox="0 0 960 650" role="img" aria-labelledby="title desc">',
'<title id="title">Finite tracial commutation: bounded vector and commuting actions</title>',
'<desc id="desc">For a faithful normal tracial state and T commuting with every left action, the vector xi equals the vector of c with norm at most C. Both paths from Omega to the vector of xc agree, proving T equals right multiplication by c.</desc>',
'<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8" fill="#145778"/></marker></defs>',
'<rect width="960" height="650" fill="#fbfcff"/>']
def text(x,y,s,size=22,color='#172635',weight='normal',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(s)}</text>')
def arrow(x1,y1,x2,y2):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#145778" stroke-width="3" marker-end="url(#arrow)"/>')
text(40,47,'Finite tracial commutation',29,weight='bold')
text(40,83,'H = L²(B, τ),  τ faithful and normal,  T ∈ L(B)′,  C = ‖T‖',22)
parts.append('<rect x="30" y="112" width="900" height="166" rx="12" fill="#e8f1f6"/>')
text(50,146,'The bounded-vector step (FC2–FC7)',23,weight='bold')
text(50,182,'ξ = TΩ;   ‖Lₐξ‖₂ ≤ C‖a‖₂;   |⟨ξ, ŷ⟩| ≤ Cτ(|y|)',23)
text(50,220,'The weakly compact set K_C = {ĉ : ‖c‖ ≤ C} has the same support bound.',20)
text(50,254,'Therefore ξ = ĉ for a unique c ∈ B, with ‖c‖ ≤ C.',23,weight='bold')
text(120,341,'Ω = vector of 1',25)
text(635,341,'ξ = vector of c',25)
text(120,498,'vector of x',25)
text(635,498,'vector of xc',25)
arrow(330,333,610,333);text(470,321,'T',23,anchor='middle')
arrow(250,362,250,466);text(208,421,'Lₓ',24,anchor='end')
arrow(760,362,760,466);text(799,421,'Lₓ',24)
arrow(330,489,610,489);text(470,478,'T',23,anchor='middle')
text(480,554,'TLₓΩ = LₓTΩ = vector of xc = R_c(vector of x)',23,anchor='middle')
text(480,595,'Density gives T = R_c and L(B)′ = R(B).  Conjugation by J gives R(B)′ = L(B).',20,anchor='middle')
text(480,626,'The arrows act on the actual tracial Hilbert space; no dimension restriction is assumed.',17,anchor='middle')
parts.append('</svg>')
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(str(out))
