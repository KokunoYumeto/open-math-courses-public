"""Exact commutant densities, actual rescaled cups and their fixed index."""
from pathlib import Path
from html import escape

R = Path(__file__).resolve().parent
out = ['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="940" viewBox="0 0 740 940">',
       '<rect width="740" height="940" fill="white"/>',
       '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#355b77"/></marker></defs>']

def text(x,y,s,size=17,bold=False):
    out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="#17324a" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')

def rect(x,y,w,h,fill="#eff5fb"):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9eb3c5"/>')

def arrow(x,y,X,Y):
    out.append(f'<path d="M{x},{y} L{X},{Y}" stroke="#355b77" stroke-width="2" marker-end="url(#arrow)"/>')

text(26,38,"Rescale the actual cup with the commutant density",23,True)
text(26,68,"Finite P ⊂ Q ⊂ R = ⟨Q,e⟩; index d; λ = 1/d. Proof: 63.1–63.5.",17)
rect(18,91,704,166)
for x,label in [(42,"P"),(276,"Q"),(526,"R")]:
    rect(x,121,166,48,"white")
    text(x+74,152,label,23,True)
arrow(208,145,273,145)
arrow(442,145,523,145)
text(39,202,"κ ∈ Z(P′ ∩ Q),  ρ(x) = τ_Q(κx),  τ_Q(κ) = 1.",19)
text(39,237,"η: P′ ∩ Q → Q′ ∩ R is finite reflection; E_A(e) = λη(κ⁻¹).",17)

rect(18,277,704,212,"#eef8f4")
text(36,310,"Canonical g = κ¹ᐟ² e κ¹ᐟ² ∈ P′ ∩ R is an actual projection.",18,True)
text(36,346,"E_(Q′∩R)(g) = λ1;       E_Q(g) = λκ;       τ_R(g) = λ.",19)
text(36,382,"F(x) = E_P(κ¹ᐟ² x κ¹ᐟ²);    g x g = F(x) g;    ⟨Q,g⟩ = R.",17)
text(36,418,"F is faithful normal; its exact scalar / positive index is d.",18)
text(36,458,"F preserves the inherited trace precisely when κ = 1.",18)

rect(18,509,704,214,"#fff7ea")
text(36,542,"Weighted-spin example: p = 1/4; q = 3/4; λ = 3/16.",18,True)
text(39,579,"Lower second-site block",16,True)
for x,label in [(288,"τ_Q"),(378,"ρ"),(469,"κ"),(564,"E_Q(g)")]:
    text(x,579,label,17,True)
for y,vals in [(614,["P₀","1/4","3/4","3","9/16"]),
               (650,["P₁","3/4","1/4","1/3","1/16"])]:
    for x,label in zip([48,288,378,469,564],vals):
        text(x,y,label,19)
text(36,694,"The upper relative expectation is (3/16)1 at both first-site blocks.",17)

rect(18,743,704,110)
text(36,777,"Every actual tunnel has these modified cups and the same index.",18,True)
text(36,811,"gⱼgⱼ₊₁gⱼ = λgⱼ;  gⱼ₊₁gⱼgⱼ₊₁ = λgⱼ₊₁;  [gⱼ,gₖ] = 0 for |j−k| ≥ 2.",16)
text(36,838,"The shifted trace-preserving comparison remains a separate input.",17)
text(26,891,"Positions are schematic; all operators, domains and coefficients are exact.",16)
text(26,918,"Human source: Popa, DOI 10.1007/BF02392646, §4.5.1, p. 224.",15)
out.append("</svg>")
(R/"canonical-cup-rescaling.svg").write_text("\n".join(out),encoding="utf-8")
