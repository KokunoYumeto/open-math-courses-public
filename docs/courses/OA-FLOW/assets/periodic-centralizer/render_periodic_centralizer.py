"""Reproducible proof schematic for PF2, PF3 and PF5; no finite-dimensional III model."""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans",
                     "svg.hashsalt": "oa-flow-periodic-centralizer-pf-v1",
                     "svg.fonttype": "path"})
navy, blue, green, orange = "#173654", "#1769aa", "#16806a", "#c95524"
gray, pale = "#697989", "#edf3f8"
fig = plt.figure(figsize=(15.6, 11.2), facecolor="white")
fig.text(.065, .956, "At the specified type IIIλ period, the centralizer is type II",
         fontsize=21, weight="bold", color=navy)
fig.text(.065, .916,
         "Assumptions: separable-predual type IIIλ factor, 0 < λ < 1, "
         "faithful n.s.f. φ, σφ at P = 2π/(−log λ) is the identity.",
         fontsize=12.5, color=gray)
fig.text(.065, .886, "Proof schematic. The spectral row uses λ = 1/2; no rank or finite-dimensional factor model is specified.",
         fontsize=11.5, color=gray)

ax = fig.add_axes([.065, .54, .885, .30])
ax.set_axis_off()
ax.set(xlim=(-3.7, 5.4), ylim=(-1.3, 2.2))
ax.text(-3.7, 2.05, "1. Each nonzero fixed corner contains every degree (PF2)",
        fontsize=15, weight="bold", color=navy)
ax.text(-3.7, 1.55, "Choose 0 ≠ f ≤ q in N with 0 < τ(f) < ∞.  "
        "The finite functional on fMf still has the full S intersection below its spectrum.",
        fontsize=11.8, color=navy)
ax.plot([-3.1, 4.0], [.55, .55], color="#c4d1de", linewidth=2)
for n in range(-3, 4):
    val = Fraction(1, 2)**n
    label = str(val.numerator) if val.denominator == 1 else f"{val.numerator}/{val.denominator}"
    selected = n == 2
    ax.scatter(n, .55, s=95 if selected else 64, color=orange if selected else blue, zorder=3)
    ax.text(n, .95, label, ha="center", fontsize=13, color=orange if selected else navy)
    ax.text(n, .12, str(n), ha="center", fontsize=12, color=gray)
ax.text(-3.65, .97, "λⁿ", color=navy, fontsize=13)
ax.text(-3.65, .12, "n", color=gray, fontsize=12)
ax.annotate("n → +∞\nλⁿ → 0", xy=(4.05, .55), xytext=(4.3, .54),
            fontsize=12, color=gray, va="center",
            arrowprops={"arrowstyle": "<-", "color": gray})
ax.text(2, -.34, r"$Q_2=1_{\{1/4\}}(\Delta_{\phi_f})\ne0$",
        ha="center", color=orange, fontsize=13.3)
ax.text(-3.7, -.86,
        r"$P_n(x)\Omega=Q_nx\Omega\quad\Longrightarrow\quad"
        r"qMq\cap M_n\ne\{0\}\quad(n\in\mathbb{Z})$",
        color=green, fontsize=15)
ax.text(3.1, -1.14, "0 is a spectral limit;\nits spectral projection is 0.",
        color=gray, fontsize=10.7, ha="left")

ax = fig.add_axes([.065, .07, .415, .38])
ax.set_axis_off()
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.text(0, .96, "2. Opposite degrees give a fixed bridge (PF3)",
        fontsize=13.8, color=navy, weight="bold")
ax.text(0, .86, "For nonzero projections e₁, e₂ in N, choose y ∈ e₁Me₂\nof degree n.",
        fontsize=11.5, color=navy, linespacing=1.3)
ax.text(0, .755, r"$q=s(y^*y)\leq e_2,\qquad\ker y=(1-q)K$",
        fontsize=13.3, color=navy)
centers = [.13, .49, .86]
labels = [r"$qK$", r"$qK$", r"$e_1K$"]
for c, label in zip(centers, labels):
    ax.add_patch(Rectangle((c-.10, .53), .20, .13, facecolor=pale, edgecolor="none"))
    ax.text(c, .595, label, ha="center", va="center", fontsize=18, color=navy)
for x1, x2, label in [(.24, .38, "z : degree −n"), (.60, .75, "y : degree n")]:
    ax.add_patch(FancyArrowPatch((x1, .595), (x2, .595), arrowstyle="-|>",
                                 mutation_scale=14, color=green))
    ax.text((x1+x2)/2, .72, label, ha="center", fontsize=10.8, color=green)
ax.text(.13, .43, "z ≠ 0,  z = qzq", fontsize=11.4, color=navy)
ax.text(.58, .43, "y is injective on qK", fontsize=11.4, color=navy)
ax.text(0, .29, r"$0\ne yz\in e_1Ne_2,\qquad (-n)+n=0$",
        fontsize=15, color=green)
ax.text(0, .16, "A proper central projection e in N would give\n"
        "eN(1 − e) = 0, contradicting this bridge.",
        fontsize=12.3, color=navy, linespacing=1.5)
ax.text(0, .025, "The support makes nonvanishing exact; no bounded inverse of y is needed.",
        fontsize=10.9, color=gray)

ax = fig.add_axes([.535, .07, .415, .38])
ax.set_axis_off()
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.text(0, .96, "3. Infinite trace versus finite projections (PF5)",
        fontsize=13.8, color=navy, weight="bold")
ax.text(0, .855, "If comparison never stops, it supplies infinitely many\n"
        "orthogonal copies fⱼ of one nonzero finite-trace f.",
        fontsize=11.8, color=navy, linespacing=1.4)
coords = [.075, .255, .435, .615]
for j, c in enumerate(coords, 1):
    ax.add_patch(Rectangle((c-.065, .61), .13, .12,
                           facecolor=pale, edgecolor="none"))
    ax.text(c, .67, f"f{chr(0x2080+j)}K", ha="center", va="center",
            fontsize=13, color=navy)
for c1, c2 in zip(coords[:-1], coords[1:]):
    ax.add_patch(FancyArrowPatch((c1, .595), (c2, .595),
        connectionstyle="arc3,rad=.4", arrowstyle="-|>",
        mutation_scale=14, color=orange))
ax.text(.77, .67, "⋯", fontsize=25, color=navy, va="center")
ax.text(0, .46, r"$r=\sum_{j\geq1}f_j,\quad w^*w=r,\quad ww^*=r-f_1$",
        fontsize=13.3, color=orange)
ax.text(0, .32, r"$v=w+(1-r),\quad v^*v=1,\quad vv^*=1-f_1<1$",
        fontsize=13.2, color=orange)
ax.text(0, .18, "A finite unit excludes this shift, so comparison stops:\n"
        "τ(1) ≤ (m + 1)τ(f) < ∞.",
        fontsize=12.1, color=navy, linespacing=1.5)
ax.text(0, .025, "The full proof gives: p finite ⇔ τ(p) < ∞ in a semifinite factor.",
        fontsize=10.9, color=gray)

fig.savefig(OUT/"periodic-centralizer-mechanism.png", dpi=160,
            facecolor="white", metadata={"Software": "OA-FLOW original renderer"})
fig.savefig(OUT/"periodic-centralizer-mechanism.svg",
            facecolor="white", metadata={"Date": None, "Creator": "OA-FLOW original renderer"})
plt.close(fig)
svg = OUT/"periodic-centralizer-mechanism.svg"
svg.write_text(svg.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
data = {
    "schematic_not_a_factor_model": True, "spectral_projection_ranks_unspecified": True,
    "illustrated_lambda": "1/2", "exact_a": "log(2)", "exact_P": "2*pi/log(2)",
    "visible_degrees": list(range(-3, 4)),
    "visible_spectral_values": [str(Fraction(1,2)**n) for n in range(-3,4)],
    "selected_degree": 2, "selected_spectral_value": "1/4",
    "all_integer_degrees_proved_not_only_drawn": True,
    "Fourier_sign": "P_n(x) = integral exp(+i*a*n*t) sigma_t(x) dt/P",
    "eigencharacter": "sigma_t(y) = exp(-i*a*n*t)*y",
    "bridge": {"y_degree": "n", "z_degree": "-n", "product_degree": "0",
               "q": "s(y^*y)", "y_kernel": "(1-q)K", "z_support": "qzq",
               "product": "0 != yz in e1 N e2"},
    "shift": {"strong_sum": "w = sum_{j>=1} v_j",
              "v_j_initial": "f_j", "v_j_final": "f_{j+1}",
              "w_initial": "r", "w_final": "r-f_1",
              "full_initial": "1", "full_final": "1-f_1"},
    "proof_locators": ["PERIODIC_CENTRALIZER_PROOF.md#pf-2",
                       "PERIODIC_CENTRALIZER_PROOF.md#pf-3",
                       "PERIODIC_CENTRALIZER_PROOF.md#pf-5",
                       "PERIODIC_CENTRALIZER_PROOF.md#pf-7"],
}
(ROOT/"FIGURE_DATA.json").write_text(json.dumps(data, indent=2)+"\n",
                                     encoding="utf-8", newline="\n")
