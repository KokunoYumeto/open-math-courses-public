"""Exact normalized bending, cell rotation and both invariant rows. CC0."""
from pathlib import Path
from html import escape

parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="540" height="930" viewBox="0 0 540 930" role="img" aria-labelledby="title desc">',
    '<title id="title">Module traces fix the connection rotation</title>',
    '<desc id="desc">An isometric edge map from b to a tensor T bends to a map of squared norm mu(b)/mu(a); multiplying by sqrt(mu(a)/mu(b)) gives its normalized reverse. Two reverse edges contribute sqrt(mu(a)mu(c)/(mu(b)mu(d))). Closing the rotated cell contributes mu(d)/mu(c) times the conjugated coefficient. Their product is sqrt(mu(a)mu(d)/(mu(b)mu(c))) times conjugate w. The exact first rows are G0m=Bm and G1m=Am with vertical tensoring by X equal to the actual inclusion. The projection e0 is the marked rank-one projection in the unit N block of A1, with trace delta^-2. It equals the block identity when X is irreducible; later projections are horizontal cups. Lemmas37.1–37.3, Proposition37.4, Theorem37.5.</desc>',
    '<rect width="540" height="930" fill="#fbfcff"/>',
    '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>',
    '<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#527397"/></marker></defs>'
]

def text(x, y, value, cls="label", anchor="middle"):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y, title, lines, height=118):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270, y+29, title, "heading")
    for i, line in enumerate(lines):
        text(270, y+59+26*i, line)

def arrow(x1, y1, x2, y2):
    parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#527397" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')

text(24, 33, "A trace calculation fixes the rotated cell", "title", "start")
box(55, "Bend an isometric edge f: b → a ⊗ T", [
    "Unnormalized reverse: squared norm μ(b)/μ(a).",
    "Normalize by √(μ(a)/μ(b)); reverse twice gives f."
])
box(191, "Two bends and one closure", [
    "Mate factors: √(μ(a)μ(c)/(μ(b)μ(d)))",
    "Closing trace: μ(d)/μ(c) × conjugate(w)"
])
box(327, "The exact rotated coefficient", [
    "R = √(μ(a)μ(d)/(μ(b)μ(c))) × conjugate(w)",
    "Both matrices are changes of orthonormal bases."
])
box(463, "Unequal-weight example: S₃ representations", [
    "Weights (a,b,c,d) = (1,2,2,1),  w = 1.",
    "Rotating gives R = 1/2, with full unitarity."
])
text(270, 620, "Recover both actual invariant rows", "heading")
for y, row in [(667, ["B₀", "B₁", "B₂"]), (753, ["A₀", "A₁", "A₂"])]:
    for x, label in zip([92, 270, 448], row):
        text(x, y, label, "heading")
    arrow(119, y-6, 236, y-6)
    arrow(298, y-6, 414, y-6)
for x in [92, 270, 448]:
    arrow(x, 682, x, 725)
text(350, 710, "1ₓ ⊗ b = b", "small")
text(270, 800, "G₀,ₘ = M′ ∩ Mₘ;  G₁,ₘ = N′ ∩ Mₘ", "label")
text(270, 830, "e₀: marked rank-one in the unit-N block of A₁.", "label")
text(270, 855, "Block identity if X is irreducible; trace δ⁻².", "label")
text(270, 885, "For j ≥ 1: eⱼ is a horizontal cup.", "label")
text(270, 905, "Keep both unit roots and every marked projection.", "small")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n", encoding="utf-8")
