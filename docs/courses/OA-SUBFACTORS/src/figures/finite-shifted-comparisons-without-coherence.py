"""Reproduce the original finite-comparison proof diagram; no third-party art."""
from pathlib import Path
from html import escape

W, H = 900, 1520
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#37556d"/></marker></defs>',
    '<rect width="900" height="1520" fill="#f7f9fc"/>',
    '<style>text{font-family:Arial,sans-serif;fill:#172b41;font-size:19px}.title{font-size:29px;font-weight:bold}.head{font-size:22px;font-weight:bold}.small{font-size:17px}.label{font-size:19px;font-weight:bold}.formula{font-family:Georgia,serif;font-size:22px}.note{fill:#784418}.arrow{stroke:#37556d;stroke-width:2.5;fill:none;marker-end:url(#arrow)}</style>',
]

def text(x,y,value,cls=""):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(value)}</text>')

def panel(y,h,title):
    parts.append(f'<rect x="26" y="{y}" width="848" height="{h}" rx="14" fill="white" stroke="#b8cad8"/>')
    text(48,y+35,title,"head")

def box(x,y,w,h,lines):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#eaf1f8" stroke="#8aa5bc"/>')
    for j,line in enumerate(lines):
        text(x+16,y+29+28*j,line,"formula" if j==0 else "")

def arrow(x,y,xx,yy):
    parts.append(f'<path d="M{x},{y} L{xx},{yy}" class="arrow"/>')

text(35,42,"Finite comparison errors vanish without a limit map","title")
text(35,75,"Conditional input: actual generation + finite trace-preserving pair maps.","small")
text(35,100,"The finite maps are still unproved in general. No arrows identify different m.","small note")

panel(120,365,"1. A finite pair and its cup — r = 0, m ≥ i + 1  [65.4, 65.7, 65.9]")
box(48,180,355,83,["F = M₋ₘ′ ∩ M₋ᵢ₊₁","contains gᵢ ∈ M₋ᵢ₋₁′"])
box(488,180,355,83,["U = Mᵢ₋₁′ ∩ Mₘ","contains eᵢ ∈ Mᵢ₊₁"])
arrow(411,220,480,220)
text(419,203,"αₘ,ᵢ","small")
box(48,300,355,78,["G = M₋ₘ′ ∩ M₋ᵢ","G ⊂ F"])
box(488,300,355,78,["V = Mᵢ′ ∩ Mₘ","V ⊂ U"])
arrow(411,340,480,340)
text(419,322,"αₘ,ᵢ","small")
arrow(221,294,221,269)
arrow(661,294,661,269)
text(48,416,"K = G′ ∩ F maps onto H = V′ ∩ U; traces are inherited.","formula")
text(48,451,"Lower cup: E_(M₋ᵢ′ ∩ M₋ᵢ₊₁)(gᵢ) = λ1. Cup image error ≤ εₘ,ᵢ.","small")

panel(505,310,"2. The entire limit argument is an error bound  [65.5, 65.8, 65.10]")
text(48,580,"Rₖ,ᵢ = Gₖ,ᵢ′ ∩ M₋ᵢ₊₁ decreases to M₋ᵢ′ ∩ M₋ᵢ₊₁.","formula")
text(48,618,"δₖ,ᵢ = ‖E_Rₖ,ᵢ(gᵢ) − λ1‖₂  →  0.","formula")
box(48,650,785,73,["‖E_Cᵢ(eᵢ) − λ1‖₂ ≤ ‖E_H(eᵢ) − λ1‖₂ ≤ δₖ,ᵢ + εₘ,ᵢ","Cᵢ = (Mᵢ′ ∩ 𝒯)′ ∩ 𝒯;     i + 1 ≤ k ≤ m"])
text(48,757,"Fix k, send admitted m → ∞, then k → ∞: E_Cᵢ(eᵢ) = λ1.","small")
text(48,790,"Kₘ,ᵢ need not be nested; αₘ,ᵢ need not agree on intersections.","small note")

panel(835,350,"3. Actual two-step endpoints — i = 1, m = 3  [65.12–65.14, 65.5]")
box(48,895,355,78,["M₋₆′ ∩ M₀","subalgebra M₋₆′ ∩ M₋₂"])
box(488,895,355,78,["M₀′ ∩ M₆","subalgebra M₂′ ∩ M₆"])
arrow(411,934,480,934)
text(418,916,"α₃,₁","small")
text(48,1010,"g₁ᵇˡᵏ ∈ M₀   →   Q₀ = d e₂ e₁ e₃ e₂ ∈ M₄.","formula")
text(48,1044,"Q₀ implements M₀ ⊂ M₂; blocked parameter Λ = d⁻².","small")
text(48,1080,"C₁ᵇˡᵏ = (M₂′ ∩ 𝒯)′ ∩ 𝒯 = M₂ by stage collapse.","formula")
text(48,1117,"M₀ ⊂ C₀ ⊂ M₂, and dense J(M₋₂ₘ′ ∩ M₀)J forces C₀ = M₀.","small")
text(48,1153,"Use only the normal finite M₂ representation on L²(M₀).","small note")

panel(1205,235,"4. Coherence really is extra — an exact finite check")
text(48,1281,"G = diagonal Mat₂, q = ½[[1,1],[1,1]], V = [[0,1],[1,0]].","small")
text(48,1317,"T(x) = xᵀ and S(x) = VxᵀV* both preserve trace, G and q.","small")
text(48,1353,"T(E₀₀) = E₀₀,   S(E₀₀) = E₁₁: alternating maps have no limit.","small")
text(48,1389,"E_G(q) = ½1. This is a finite example, not a generating II₁ tunnel.","small note")
text(35,1473,"Original proof and example locators: 65.1–65.14; complete argument retained beside this figure.","small")
text(35,1502,"Human source: Popa, Classification of amenable subfactors, §4.5.1, printed223–224.","small")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")
