from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description="Draw the exact normalized-coefficient model.")
parser.add_argument("--font-dir", type=Path, required=True,
                    help="Existing OA-FLOW assets/typeiii-zero-decomposition directory.")
args = parser.parse_args()
font_dir = args.font_dir.resolve()
regular = font_dir / "DejaVuSans.ttf"
bold = font_dir / "DejaVuSans-Bold.ttf"
for font in (regular, bold):
    if not font.is_file():
        raise FileNotFoundError(font)
fp = FontProperties(fname=str(regular))
fb = FontProperties(fname=str(bold))

def weight(j: int) -> Fraction:
    if j % 2 == 0:
        return Fraction(8) ** (j // 2)
    return 4 * Fraction(8) ** ((j - 1) // 2)

def rho(n: int, j: int) -> Fraction:
    return weight(j - n) / weight(j)

def log2_fraction(q: Fraction) -> int:
    a, b = q.numerator, q.denominator
    assert a & (a - 1) == 0 and b & (b - 1) == 0
    return a.bit_length() - b.bit_length()

for j in range(-8, 9):
    assert rho(1, j) == (Fraction(1, 2) if j % 2 == 0 else Fraction(1, 4))
    for n in range(-4, 5):
        for m in range(-4, 5):
            assert rho(n + m, j) == rho(n, j) * rho(m, j - n)
    assert weight(j) / weight(j + 1) == rho(1, j + 1)
assert rho(1, 0) != rho(1, 1)
assert weight(0) * 1 == weight(1) * Fraction(1, 4)

data = {
    "model": "N = ell-infinity(Z) tensor B(ell2(N)); theta(x)(j)=x(j+1)",
    "trace": "tau(x)=sum_j w_j Tr(x(j)), w_(2k)=8^k, w_(2k+1)=4*8^k",
    "rho": "rho_n(j)=w_(j-n)/w_j; rho_1(even)=1/2, rho_1(odd)=1/4",
    "unitary": "U delta_j=delta_(j-1); sigma_t(U)=U rho^(it)",
    "scope": "An exact type-I coefficient/crossed-product model, not a type-III0 model.",
    "panel_a": [{"j": j, "weight": str(weight(j)),
                 "phase_on_arrow_from_j_to_previous": str(rho(1, j))}
                for j in range(-1, 3)],
    "panel_b": [{"parity": label, "j": j,
                 "endpoints": [{"n": n, "rho": str(rho(n, j)),
                                "log2_rho": log2_fraction(rho(n, j))}
                               for n in range(-2, 4)]}
                for label, j in [("even", 0), ("odd", 1)]],
    "panel_c": [{"j": j, "h": str(1 - Fraction(1, j + 2)),
                 "one_minus_h": str(Fraction(1, j + 2))}
                for j in range(13)],
    "panel_d": {"projection": "e=1_{0} tensor e_11", "density": "h e=(1/2)e",
                "before": "N_(tau_h)=N, properly infinite",
                "after": "eNe=C e, finite",
                "drawing": "Only the first four multiplicity coordinates are displayed."},
    "proof_locators": ["../../OA-FLOW-NCOEF.html#nc-density-cocycle",
                       "../../OA-FLOW-NCOEF.html#nc-rigidity",
                       "../../OA-FLOW-NCOEF.html#nc-centralizer",
                       "../../OA-FLOW-NCOEF.html#nc-seed",
                       "../../OA-FLOW-NCOEF.html#nc-models"],
    "source_policy": "Original exact models and drawing; no source-page image or source figure.",
    "font_dependencies": [{"file": f.name,
                           "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                           "public_relative_path": "../typeiii-zero-decomposition/" + f.name}
                          for f in (regular, bold)]
}
(HERE / "data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                               encoding="utf-8", newline="\n")

plt.rcParams.update({"svg.fonttype": "path", "svg.hashsalt": "oa-flow-ncoef-v1",
                     "axes.linewidth": 0.8})
fig, axs = plt.subplots(2, 2, figsize=(13.2, 10.4))
fig.patch.set_facecolor("#f7f9fc")
fig.subplots_adjust(left=0.06, right=0.975, top=0.875, bottom=0.1,
                    hspace=0.40, wspace=0.23)
ink, blue, purple, red, teal = "#183048", "#2166ac", "#7550a1", "#be4b48", "#167d8d"

def label(ax, x, y, text, size=11, color=ink, weight=False, **kw):
    return ax.text(x, y, text, fontproperties=fb if weight else fp,
                   fontsize=size, color=color, **kw)

def title(ax, text):
    ax.set_title(text, loc="left", fontproperties=fb, fontsize=14, color=ink, pad=14)

for ax in axs.flat:
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_color("#ccd5df")

fig.text(0.06, 0.956, "Normalized coefficient weights", fontproperties=fb,
         fontsize=23, color=ink)
fig.text(0.06, 0.923, "An alternating central density: exact phases, bands, strictness and support cuts",
         fontproperties=fp, fontsize=12.4, color=ink)

ax = axs[0, 0]
title(ax, "A   The density is on the right")
ax.set_xlim(-1.5, 2.5); ax.set_ylim(-0.75, 3.1); ax.axis("off")
for j in range(-1, 3):
    ax.plot(j, 1.3, "o", ms=10, color=blue)
    label(ax, j, 0.98, "δ" + str(j), 12, ha="center")
    label(ax, j, 0.52, "w = " + str(weight(j)), 11, ha="center")
for j in range(0, 3):
    ar = FancyArrowPatch((j - 0.09, 1.53), (j - 0.91, 1.53),
                         arrowstyle="-|>", mutation_scale=16,
                         connectionstyle="arc3,rad=0.35", linewidth=2.1, color=purple)
    ax.add_patch(ar)
    label(ax, j - 0.5, 2.12, str(rho(1, j)), 13, color=purple, ha="center", weight=True)
label(ax, 0.5, 2.72, "Uδⱼ = δⱼ₋₁    •    arrow phase = ρ(j)ⁱᵗ", 11.5, ha="center")
label(ax, 0.5, -0.07, "On δ₁ → δ₀:   right ρ(1) = 1/4", 11.5,
      ha="center", color=purple, weight=True)
label(ax, 0.5, -0.46, "The incorrect left order gives ρ(0) = 1/2.", 10.5,
      ha="center", color=red)

ax = axs[0, 1]
title(ax, "B   Central bands have different endpoints")
ax.set_xlim(-5.35, 3.25); ax.set_ylim(-0.6, 2.8)
colors = {-1: "#cadbe9", 0: "#e3d4ee", 1: "#6ebfc3", 2: "#aec7e8", 3: "#d9e5f1"}
for label_text, j, y in [("even j", 0, 1.6), ("odd j", 1, 0.5)]:
    for n in range(3, -2, -1):
        lo = log2_fraction(rho(n, j)); hi = log2_fraction(rho(n - 1, j))
        ax.add_patch(Rectangle((lo, y), hi - lo, .48, facecolor=colors[n],
                               edgecolor="white", linewidth=1.2))
        label(ax, (lo + hi) / 2, y + .24, "c" + str(n), 10.5, ha="center", va="center")
    label(ax, -5.25, y + .66, label_text, 11.2, weight=True)
    lo = log2_fraction(rho(1, j))
    ax.plot([lo, 0], [y - .13, y - .13], color=teal, linewidth=2.5)
    ax.plot(lo, y - .13, "o", color=teal, ms=5)
    ax.plot(0, y - .13, "o", color=teal, markerfacecolor="white", ms=5)
label(ax, -1.0, 2.49, "cₙ(j) = [ρₙ(j), ρₙ₋₁(j))", 11.2, ha="center")
label(ax, -1.0, -0.28, "Highlighted c₁:  [ρ(j), 1)", 11, color=teal, ha="center", weight=True)
ax.set_xticks(range(-5, 4)); ax.set_yticks([])
ax.set_xlabel("log₂ of the positive density", fontproperties=fp, fontsize=11, color=ink)
for t in ax.get_xticklabels(): t.set_fontproperties(fp); t.set_fontsize(10)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax = axs[1, 0]
title(ax, "C   Strict does not mean uniformly below 1")
js = list(range(13)); hs = [float(1 - Fraction(1, j + 2)) for j in js]
ax.set_xlim(-.55, 13.6); ax.set_ylim(.37, 1.17)
ax.axhline(1, color=red, ls=(0, (5, 3)), lw=1.5)
ax.scatter(js, hs, s=37, color=blue, zorder=3)
ax.plot(js, hs, color=blue, lw=.7, alpha=.3)
label(ax, 12.9, 1.015, "1", 11.5, color=red)
label(ax, .0, 1.105, "h(j) = 1 − 1/(|j| + 2)", 12, weight=True)
label(ax, 6.4, .48, "ker(1 − h) = 0     ‖h‖ = 1", 11.5, ha="center")
label(ax, 6.4, .405, "1 is a limit, not an eigenvalue.", 10.5, color=red, ha="center")
ax.set_xticks([0, 2, 4, 6, 8, 10, 12]); ax.set_yticks([.5, .75, 1])
ax.set_xlabel("integer j ≥ 0  (the negative indices are reflected)", fontproperties=fp,
              fontsize=10.5, color=ink)
for t in ax.get_xticklabels() + ax.get_yticklabels():
    t.set_fontproperties(fp); t.set_fontsize(10)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

ax = axs[1, 1]
title(ax, "D   A finite cut loses infinite multiplicity")
ax.set_xlim(-.2, 6.3); ax.set_ylim(-1.0, 4.25); ax.axis("off")
cell = .56; x0, y0 = .25, .55
for i in range(4):
    for j in range(4):
        face = "#a5cee5" if i == j else "#eff4f7"
        ax.add_patch(Rectangle((x0 + j * cell, y0 + (3-i)*cell), cell, cell,
                               facecolor=face, edgecolor="white", linewidth=1.5))
        if i == j:
            label(ax, x0+(j+.5)*cell, y0+(3-i+.5)*cell, "½", 11,
                  ha="center", va="center")
label(ax, 1.37, 3.33, "h(0)I on ℓ²", 12, weight=True, ha="center")
label(ax, 2.7, 1.65, "⋯", 19)
label(ax, 1.37, .06, "centralizer B(ℓ²)", 11.3, ha="center", color=blue)
label(ax, 1.37, -.43, "properly infinite", 11.3, ha="center", color=blue, weight=True)
ax.add_patch(FancyArrowPatch((3.05, 1.68), (4.06, 1.68), arrowstyle="-|>",
                            mutation_scale=16, color=purple, linewidth=1.8))
label(ax, 3.58, 2.12, "cut e₁₁", 10.5, color=purple, ha="center")
ax.add_patch(Rectangle((4.4, 1.4), cell, cell, facecolor="#efd0cb",
                       edgecolor=red, linewidth=1.4))
label(ax, 4.68, 1.68, "½", 12, ha="center", va="center")
label(ax, 4.7, 3.33, "he = ½e", 12, weight=True, ha="center")
label(ax, 4.7, .06, "centralizer ℂe", 11.3, ha="center", color=red)
label(ax, 4.7, -.43, "finite", 11.3, ha="center", color=red, weight=True)
label(ax, 3.0, -.9, "Four multiplicity coordinates shown; the original fiber is infinite.",
      9.4, ha="center")

fig.text(.06, .040,
         "Exact model: NC54–NC58.  Right density: NC9.  Rigidity: NC27.  Centralizers: NC28.  Seed multiplicity: NC50.",
         fontproperties=fp, fontsize=10, color=ink)
fig.text(.06, .018, "OA-FLOW-NCOEF • Original diagram and data • CC0-1.0 • External DejaVu font assets retain their license.",
         fontproperties=fp, fontsize=9.2, color=ink)
for ext in ["png", "svg"]:
    meta = {"Software": "OA-FLOW normalized-coefficients renderer"} if ext == "png" else {
        "Date": None, "Creator": "OA-FLOW normalized-coefficients renderer",
        "Title": "Normalized coefficient weights",
        "Description": "Exact alternating density model and supported centralizer diagnostics."}
    fig.savefig(HERE / ("normalized-coefficients." + ext), dpi=160,
                facecolor=fig.get_facecolor(), metadata=meta)
plt.close(fig)
print(json.dumps({"exact_assertions": "passed", "outputs": ["data.json",
                 "normalized-coefficients.png", "normalized-coefficients.svg"]}))

