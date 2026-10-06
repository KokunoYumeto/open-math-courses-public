"""Intrinsic exceptional branch projections and their exact ordered trace. CC0."""
from pathlib import Path
from html import escape

out = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="540" height="1050" viewBox="0 0 540 1050" role="img" aria-labelledby="title desc">',
    '<title id="title">An ordered Jones trace distinguishes opposite exceptional inclusions</title>',
    '<desc id="desc">The original short-tip projection p lies in A k minus1; its image and the dual short-tip projection sigma lie in A k. Sigma lies in B k and annihilates U2 through Uk, with Ui=delta e i minus1. The ordered bridge p sigma U1 through Uk has a non-real trace. E6 uses k3 and a four-dimensional branch block; E8 uses k5 and a six-dimensional block. Exact reduced difference polynomials have degrees14 and30 below minimal cyclotomic degrees16 and32, so neither difference vanishes. Conjugation reverses the sign of the imaginary part. At-most-two plus two distinct constructed classes yields exactly two anti-isomorphic classes for each graph. Lemmas39.1–39.2 and Propositions39.3–39.4.</desc>',
    '<rect width="540" height="1050" fill="#fbfcff"/>',
    '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:21px;font-weight:bold}.head{font-size:18px;font-weight:bold}.body{font-size:17px}.small{font-size:16px}</style>'
]

def text(x,y,value,kind="body"):
    out.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="{kind}">{escape(value)}</text>')

def panel(y,height,heading,lines):
    out.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+28,heading,"head")
    for j,line in enumerate(lines):
        text(270,y+57+27*j,line)

def arrow(x,y1,y2):
    out.append(f'<path d="M{x} {y1} L{x} {y2}" stroke="#287c99" stroke-width="3"/>')
    out.append(f'<path d="M{x-5} {y2-7} L{x} {y2} L{x+5} {y2-7}" fill="none" stroke="#287c99" stroke-width="3"/>')

text(270,35,"The order detects exceptional chirality","title")
panel(63,112,"The inclusion chooses both short-tip projections",[
    "p ∈ Aₖ₋₁: smaller new original scalar block.",
    "σ ∈ Bₖ: smaller new dual scalar block."
])
arrow(270,184,211)
panel(222,139,"Both projections live in Aₖ = Pₖ₊₁",[
    "σ has rank 1, supported at branch endpoint b.",
    "σ Uᵢ = Uᵢ σ = 0 for 2 ≤ i ≤ k.",
    "Uᵢ = δ eᵢ₋₁; the initial U₁ is δ e₀."
])
arrow(270,370,397)
panel(409,111,"The marked ordered bridge gives an invariant",[
    "IΓ = τ(p σ U₁ U₂ … Uₖ).",
    "One diagonal entry × μ(b) / δᵏ⁺¹."
])
panel(541,140,"Exact finite commutation finds the actual σ",[
    "E₆: branch block 4, k = 3; 120 equations.",
    "E₈: branch block 6, k = 5; 6,880 equations.",
    "Four unknowns, rank 3; normalize matrix trace 1."
])
panel(701,167,"IΓ differs from its complex conjugate",[
    "E₆: −11z² + 11z⁶ + 3z¹⁰ − 8z¹⁴ ≠ 0.",
    "E₈: −76z² − 15z⁶ + 27z¹⁰ + 42z¹⁴",
    "+ 49z¹⁸ + 22z²² − 12z²⁶ − 77z³⁰ ≠ 0.",
    "Degrees 14 < 16 and 30 < 32; z = ζ₄₈, ζ₁₂₀."
])
arrow(270,877,904)
panel(916,109,"Exactly two classes for each exceptional graph",[
    "Conjugation gives unequal conjugate values.",
    "The pairs are anti-isomorphic and inequivalent."
])
out.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(out)+"\n",encoding="utf-8")
