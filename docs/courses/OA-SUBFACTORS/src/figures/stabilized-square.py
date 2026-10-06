"""Reproducible vector figure for Lemma48.2 and Theorem48.3; CC0."""
from pathlib import Path
from html import escape
W,H=640,930
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="640" height="930" fill="#f8fafc"/>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#475569"/></marker></defs>']
def text(x,y,s,size=19,color="#172554",anchor="middle"):
 out.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" fill="{color}">{escape(s)}</text>')
def arrow(x,y,u,v):
 out.append(f'<path d="M{x} {y}L{u} {v}" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
def box(y,h):
 out.append(f'<rect x="25" y="{y}" width="590" height="{h}" rx="13" fill="white" stroke="#cbd5e1"/>')
text(320,37,"The stabilized square and the original pair",23)
text(320,65,"Finite index d > 1 · finite depth · hyperfinite pairs",16)
box(85,260)
text(320,117,"One shared next Jones projection",21)
xs=[111,320,529]
for i,x in enumerate(xs):
 text(x,166,["Aₖ","Aₖ₊₁","Aₖ₊₂"][i],23)
 text(x,261,["Bₖ","Bₖ₊₁","Bₖ₊₂"][i],23)
 arrow(x,236,x,179)
 if i<2:
  arrow(x+39,157,xs[i+1]-44,157)
  arrow(x+39,252,xs[i+1]-44,252)
text(530,199,"eₖ₊₁",21,"#0369a1")
text(320,300,"Σᵢ vᵢ eₖ₊₁ vᵢ* = 1,   vᵢ ∈ Bₖ₊₁",21,"#0369a1")
text(320,326,"Full lower construction ⇒ a common upper frame",16)
box(363,110)
text(320,396,"Actual linear product span",21)
text(320,430,"x = Σᵢ vᵢ E_Aₖ(vᵢ* x),   x ∈ Aₖ₊₁",21)
text(320,455,"Aₖ₊₁ = span(Bₖ₊₁ Aₖ) = span(Aₖ Bₖ₊₁)",18)
arrow(320,480,320,514)
box(524,109)
text(320,557,"Repeated traced basic constructions",21)
text(320,591,"B∞ ⊂ A∞  ≅  (M ⊂ M₁)ᵒᵖ",23,"#0369a1")
text(320,614,"Finite-depth generating tunnel · equation (17.18)",16)
arrow(320,640,320,674)
box(686,193)
text(320,721,"Recover the original predecessor",21)
text(320,755,"E_M̃(f) = d⁻¹1 = E_M̃(ẽ₀)",22,"#0369a1")
text(320,788,"f = u ẽ₀ u*,   u ∈ M̃",22)
text(320,821,"β(N) = M̃ ∩ {f}′ = u Ñ u*",22)
text(320,855,"Ad(u*) ∘ β carries N ⊂ M onto Ñ ⊂ M̃",17)
text(320,906,"Proof locators: 48.8–48.16 · downward uniqueness 4.5",16)
out.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(out)+"\n",encoding="utf-8")
