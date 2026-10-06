"""Exact normalized weights in the diagonal inclusion, lesson 40."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 930" role="img" aria-labelledby="title desc">',
         '<title id="title">Reflection compares two different factor traces</title>',
         '<desc id="desc">A diagonal inclusion has corner traces one quarter and three quarters, local indices one, and total index sixteen thirds. The normalized trace of the opposite factor M prime assigns the reflected projection one quarter, while the tower factor M1 assigns it three quarters.</desc>',
         '<rect width="560" height="930" fill="#ffffff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#15283b} .small{font-size:17px}.body{font-size:20px}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}</style>']

def text(x, y, value, cls="body", anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y, h, color="#edf4fb"):
    parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')

text(280, 40, "One projection, two trace weights", "head", "middle")
box(64, 193)
text(40, 95, "M = M₄ ⊗ R₀", "label")
text(40, 126, "p = E₁₁ ⊗ 1,   q = 1 − p")
text(40, 157, "N = {α(x) + β(x) : x ∈ R₀}")
text(40, 190, "Np = pMp,   Nq = qMq", "label")
text(40, 226, "Local indices: 1 and 1", "small")
box(279, 159, "#f0f7f0")
text(40, 311, "Dimension trace on N′", "label")
text(40, 347, "T_N(p) = 4,     T_N(q) = 4/3")
text(40, 383, "[M : N] = T_N(1) = 16/3", "label")
text(40, 416, "ρ_N′(p) = 3/4,    ρ_N′(q) = 1/4", "small")
box(460, 190)
text(40, 493, "Finite reflection: Θ(p) = JpJ = b ∈ B₁", "label")
text(40, 528, "M′ = JMJ:    ρ_M′(b) = τ_M(p) = 1/4", "small")
parts.append('<rect x="40" y="547" width="480" height="24" fill="#dce6ef"/>')
parts.append('<rect x="40" y="547" width="120" height="24" fill="#246b9b"/>')
text(40, 605, "M₁ = JN′J:    τ_M₁(b) = ρ_N′(p) = 3/4", "small")
parts.append('<rect x="40" y="623" width="480" height="24" fill="#dce6ef"/>')
parts.append('<rect x="40" y="623" width="360" height="24" fill="#9e593b"/>')
box(672, 217, "#fff5e8")
text(40, 709, "Extension criteria", "label")
text(40, 746, "Trace preserving: equality at every finite level.", "small")
text(40, 781, "Normal: the pulled-back tower state extends", "small")
text(40, 809, "faithfully and normally to the downward closure.", "small")
text(40, 849, "For a factor closure, the criteria coincide.", "small")
text(40, 914, "Theorems 40.1 and 40.3; Proposition 40.2", "small")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n", encoding="utf-8")
