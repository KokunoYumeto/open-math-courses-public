"""Reproducible CC0 algebra schematic; no metric geometry is asserted."""
from pathlib import Path
from html import escape

OWN = Path(__file__).resolve().parent
W, H = 1640, 1260
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="#f7f9fc"/>']
def text(x, y, value, size=30, weight=False, color="#152438"):
    svg.append(f'<text x="{x}" y="{y + size}" font-family="Segoe UI, sans-serif" font-size="{size}" font-weight="{700 if weight else 400}" fill="{color}">{escape(value)}</text>')
def box(x, y, w, h, color="#ffffff", border="#b8c8dc"):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{color}" stroke="{border}" stroke-width="3"/>')
def line(x1, y1, x2, y2, color="#637b98", width=4):
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')

text(48, 26, "Interior density: a physical spectral cut is not an admissible return", 40, True)
text(48, 86, "Actual index-18 Jones model • full all-smooth amenability • generating product tunnel", 29)

box(48, 145, 1544, 158, "#eaf1fb")
text(76, 165, "N = N₀ x 1 x F    inside    M = M₀ x Mat₂ x F", 37, True)
text(76, 223, "Weighted-spin index 9/2 × Bell index 4 = 18.  F is the infinite hyperfinite tensor tail.", 29)
text(76, 263, "All-smooth proof: V9.5 + IF.3a (larger matrix leg) + IF.3b (common tail).", 27)

box(48, 330, 1544, 250)
text(76, 348, "Physical commutant C = Mat₂ + Mat₂, central blocks c₊ and c₋", 32, True)
text(76, 402, "Block", 29, True)
text(290, 402, "Inherited τ", 29, True)
text(600, 402, "Normalized dual trace", 29, True)
text(1130, 402, "k_C density", 29, True)
line(76, 451, 1558, 451)
text(100, 463, "c₊", 31, True)
text(330, 463, "1/3", 31)
text(770, 463, "2/3", 31)
text(1200, 463, "2", 31)
text(100, 515, "c₋", 31, True)
text(330, 515, "2/3", 31)
text(770, 515, "1/3", 31)
text(1200, 515, "1/2", 31)

box(48, 610, 748, 247, "#edf7f1", "#95bfa8")
text(76, 629, "Actual original core", 32, True)
text(76, 682, "R = M,  S = N;   A = N,  B = M", 30)
text(76, 734, "Original E = E_N; both centers are scalar.", 29)
text(76, 790, "w = ℓ = 1;  original cost a = 0", 32, True, "#205e41")

box(826, 610, 766, 247, "#f1effb", "#afa0d1")
text(854, 629, "The cup projection still lies outside C", 31, True)
text(854, 681, "Endpoints r = 8 − 3√7, R* = 8 + 3√7", 29)
text(854, 728, "E_C(f):  η₊ = 1/2 − 1/√7", 29)
text(854, 771, "                 η₋ = 1/2 − 5/(4√7)", 29)
text(854, 817, "Both interior;  ||f − E_C(f)||₂² = 3/56", 28, True)

box(48, 887, 748, 193, "#fff4e9", "#d6b291")
text(76, 905, "Condition on c₊, trace t = 1/3", 31, True)
text(76, 958, "Cost unchanged; original E-defect = 4/3", 29)
text(76, 1009, "Actual corner index = 4; M-reducing part = 0", 28)
box(826, 887, 766, 193, "#fff4e9", "#d6b291")
text(854, 905, "Condition on c₋, trace t = 2/3", 31, True)
text(854, 958, "Cost unchanged; original E-defect = 2/3", 29)
text(854, 1009, "Actual corner index = 4; M-reducing part = 0", 28)

text(48, 1110, "IF.6: r commutes with M; projection r ≤ c; 0 < τ(c) < 1 implies r = 0.", 30, True)
text(48, 1160, "Norm averages of ucu* converge to τ(c)1; hence r ≤ τ(c)1. Applies also in the bidual.", 29)
text(48, 1210, "x: spatial tensor product; +: direct sum. IF.1–IF.32; Popa (1994), §§3.1–3.2. CC0 schematic.", 24)

svg.append("</svg>")
(OWN / "interior-physical-faces-v10.svg").write_text("\n".join(svg), encoding="utf-8")
