"""Original groupoid regular interface illustration. Expression CC0-1.0."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import tempfile

HERE = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "ncg-groupoid-figure-cache"))
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle

ap = argparse.ArgumentParser()
ap.add_argument("--output-dir", type=Path, default=HERE)
out = ap.parse_args().output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
REG = FontProperties(fname=str(HERE / "fonts/DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts/DejaVuSans-Bold.ttf"))
plt.rcParams.update({"svg.fonttype": "path",
                     "svg.hashsalt": "groupoid-regular-interface-20261006"})
INK, BLUE, RED, GREEN = "#243b53", "#2467a4", "#b4394a", "#217459"
fig, axs = plt.subplots(2, 2, figsize=(17, 11))
fig.patch.set_facecolor("white")
for a in axs.flat:
    a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")

def text(a, x, y, s, size=11, bold=False, color=INK, ha="center"):
    a.text(x, y, s, fontsize=size, fontproperties=BOLD if bold else REG,
           color=color, ha=ha, va="center", transform=a.transAxes,
           linespacing=1.35, zorder=10)

def arrow(a, p, q, color=BLUE, curve=0, width=2):
    a.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=16,
                               linewidth=width, color=color,
                               transform=a.transAxes,
                               connectionstyle="arc3,rad=" + str(curve)))

a = axs[0, 0]
text(a, .5, .96, "A. A nonzero corner is not the balanced quotient", 13, True)
labels = ["11", "12", "21", "22"]
for j, label in enumerate(labels):
    text(a, .31 + .13*j, .82, label, 12, True)
    text(a, .165, .69 - .115*j, label, 12, True)
for i in range(4):
    for j in range(4):
        x, y = .26 + .13*j, .638 - .115*i
        inside = i in (0, 3) and j in (0, 3)
        a.add_patch(Rectangle((x, y), .12, .105,
                             facecolor="#e4f4eb" if inside else "#eef1f5",
                             edgecolor=GREEN if inside else "#cad3dc",
                             transform=a.transAxes))
        matrix_labels = {(0, 0): "Δ(e₁₁)", (0, 3): "Δ(e₁₂)",
                         (3, 0): "Δ(e₂₁)", (3, 3): "Δ(e₂₂)"}
        text(a, x + .06, y + .052, matrix_labels.get((i, j), "·"), 9,
             color=GREEN if inside else "#9aabb9")
text(a, .54, .22, "Green 2 × 2 corner on span{11,22}:  P M₄ P ≅ M₂", 11,
     True, GREEN)
text(a, .5, .125, "Balancing generator in all M₄:  diag(0,1,−1,0)", 11, True, RED)
text(a, .5, .058, "Eₐ,₁₂  generator  E₁₂,ᵦ = Eₐ,ᵦ    ⇒    quotient = 0", 10, color=RED)

a = axs[0, 1]
text(a, .5, .96, "B. Transport changes the coefficient's unit fibre", 13, True)
nodes = {"z": (.17, .38), "y": (.81, .38), "x": (.49, .76)}
for label, pos in nodes.items():
    a.add_patch(Circle(pos, .035, facecolor="#eaf2fb", edgecolor=BLUE,
                      linewidth=2, transform=a.transAxes))
    text(a, *pos, label, 13, True)
arrow(a, (.20, .41), (.46, .724))
arrow(a, (.78, .41), (.52, .724))
arrow(a, (.21, .38), (.765, .38))
text(a, .245, .625, "g : z → x", 11, color=BLUE)
text(a, .72, .625, "γ : y → x", 11, color=BLUE)
text(a, .49, .32, "γ⁻¹g : z → y", 11, True, BLUE)
text(a, .49, .23, "V_z  →  V_y  →  V_x  →  V_z", 13, True)
text(a, .49, .15, "U_(γ⁻¹g)       U_γ       U_g⁻¹     =     identity on V_z", 10)
text(a, .49, .058, "Jξ(g) = U_g⁻¹ξ(g)  ·  one unit measure  ·  reduced regular norm", 10,
     True, GREEN)

a = axs[1, 0]
text(a, .5, .96, "C. The actual smooth graph leaves a whole source line", 13, True)
text(a, .5, .865, "G = (ℝ_t × ℝ_r × S¹_n) / ℤ   ·   n-circle and C₁ suppressed", 11)
left, right, bottom, top = .11, .94, .25, .72
def rmap(r):
    return left + (right - left)*(r + 1.5)/5
def tmap(t):
    return bottom + (top - bottom)*t
arrow(a, (left-.015, bottom), (right+.025, bottom), INK, width=1.3)
arrow(a, (left, bottom-.015), (left, top+.04), INK, width=1.3)
text(a, .965, .245, "r", 12, True)
text(a, .08, .77, "t", 12, True)
for t, label in [(0, "0"), (.25, "1/4"), (.75, "3/4"), (1, "1")]:
    a.plot([left, right], [tmap(t), tmap(t)], color="#c6d1dd",
           linestyle=":" if t not in (0, 1) else "-", linewidth=1,
           transform=a.transAxes)
    text(a, .07, tmap(t), label, 9)
for j in [-1, 0, 1, 2, 3]:
    a.add_patch(Rectangle((rmap(j-1/8), tmap(.25)),
                         (right-left)*(.25)/5, (top-bottom)*.5,
                         facecolor="#c8e5d5", edgecolor=GREEN,
                         linewidth=1.4, transform=a.transAxes))
    text(a, rmap(j), .195, str(j), 10)
text(a, .53, .64, "Support boxes:  t ∈ (1/4,3/4),  r ∈ (j−1/8,j+1/8)", 9,
     color=GREEN)
text(a, .53, .115, "Fixed k averages t only:  |ξ⟩⟨ξ|_t ⊗ identity on r,n,C₁", 10, True)
text(a, .53, .037, "Source r is unbounded.  Deck phase e^(−ijπ/5) is retained.", 10)

a = axs[1, 1]
text(a, .5, .96, "D. One fixed localized resolvent preserves every ψⱼ", 13, True)
text(a, .5, .86, "D = A(−i∂_n),   A² = 1   ·   ψⱼ = ξ(t) ζ(r−j) u(n)", 11)
xs = [.2, .34, .48, .62, .76]
for i, x in enumerate(xs):
    a.plot([x, x], [.43, .72], color=BLUE, linewidth=4,
           transform=a.transAxes)
    a.plot([x], [.72], "o", color=BLUE, markersize=6, transform=a.transAxes)
    text(a, x, .385, "j=" + str(i-1), 9)
text(a, .08, .72, "1", 11, True)
text(a, .08, .43, "0", 10)
text(a, .5, .79, "Input norm = image norm = 1", 12, True, BLUE)
text(a, .885, .55, "…", 22, True, BLUE)
text(a, .5, .30, "Π(k)(1+D²)⁻¹ ψⱼ = ψⱼ", 14, True)
a.add_patch(Rectangle((.1, .105), .8, .12, facecolor="#fff0f1",
                      edgecolor=RED, transform=a.transAxes))
text(a, .5, .165, "Distinct images are orthogonal:  distance √2", 12, True, RED)
text(a, .5, .047, "Finite sample of a proved infinite sequence; no compact subsequence.", 10)

fig.subplots_adjust(left=.02, right=.985, bottom=.09, top=.92,
                    wspace=.14, hspace=.12)
fig.text(.5, .985, "Regular groupoid absorption: exact norm, distinct index and compactness tests",
         ha="center", va="top", fontproperties=BOLD, fontsize=18, color=INK)
fig.text(.5, .045, "Figure 11M.1. Proposition 11M.1; Theorems 11M.2–11M.3.  "
         "Full proofs: (GR.1)–(GR.18).  Canonical doubled unit-line index is zero: (GR.19)–(GR.21).",
         ha="center", fontproperties=REG, fontsize=10, color=INK)
notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
description = ("Original mathematical illustration CC0-1.0. "
               "Complete font notice:\n" + notice)
png, svg = out / "groupoid-regular-interface.png", out / "groupoid-regular-interface.svg"
fig.savefig(png, dpi=160, metadata={"Description": description,
                                  "Software": "Matplotlib " + matplotlib.__version__})
fig.savefig(svg, metadata={"Date": None, "Description": description})
svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
plt.close(fig)
data = {
    "proof_locators": ["GR.1", "GR.2", "GR.3", "GR.4", "GR.1–GR.21"],
    "A": {"tensor_basis": ["11", "12", "21", "22"],
          "balance_diagonal": [0, 1, -1, 0], "corner_basis": ["11", "22"],
          "balanced_quotient": "zero algebra", "corner": "M2"},
    "B": {"gamma": "y->x", "g": "z->x", "gamma_inverse_g": "z->y",
          "transport_chain": ["Vz->Vy", "Vy->Vx", "Vx->Vz"],
          "one_unit_measure": True, "isotropy_labels_retained": True},
    "C": {"range_strip": [0, 1], "source_line": "R", "normal_circle": "R/2piZ",
          "alpha": "2pi(sqrt(2)-1)", "beta": "pi/5",
          "full_inverse_phase": "exp(-ij*pi/5)", "inverse_determinant": "exp(-2ij*pi/5)",
          "t_support_box": ["1/4", "3/4"], "r_radius": "1/8",
          "displayed_source_centres": [-1, 0, 1, 2, 3],
          "boxes_are_support_bounds_not_function_profiles": True,
          "normal_and_clifford_factors_suppressed": True},
    "D": {"sample_centres": [-1, 0, 1, 2, 3], "input_norms": [1]*5,
          "output_norms": [1]*5, "pairwise_image_distance": "sqrt(2)",
          "infinite_statement_requires_written_proof": True},
    "matplotlib": matplotlib.__version__, "font_notice_embedded": True,
    "outputs": [{"path": p.name, "bytes": p.stat().st_size,
                 "sha256": hashlib.sha256(p.read_bytes()).hexdigest().upper()}
                for p in [png, svg]]
}
(out / "FIGURE-DATA.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
