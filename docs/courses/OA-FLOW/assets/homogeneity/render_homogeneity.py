"""Reproduce the local proof illustrations. Original code CC0-1.0."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.hashsalt": "homogeneity-finite-partition-20261004-v1",
    "svg.fonttype": "path",
    "savefig.facecolor": "#fafafa",
})
INK, BLUE, TEAL, RED, GOLD = "#192d40", "#3066be", "#087f8c", "#ba3f38", "#b08018"

def save(fig, stem):
    fig.savefig(OUT / (stem + ".png"), dpi=160)
    fig.savefig(OUT / (stem + ".svg"), metadata={"Date": None})
    p = OUT / (stem + ".svg")
    p.write_text(p.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    plt.close(fig)

fig, axes = plt.subplots(2, 2, figsize=(14, 8), gridspec_kw={"height_ratios": [1, 1]})
fig.suptitle("Finite projections prove the cutoff bound; pinching spends measurable mass",
             fontsize=17, color=INK, y=.98)
fig.text(.5, .925, r"$M=M_2,\quad h=\mathrm{diag}(2,-1),\quad "
         r"\xi_{11}=\xi_{22}=2/\sqrt{10},\quad\xi_{12}=\xi_{21}=1/\sqrt{10},"
         r"\quad\phi(x)=\mathrm{Tr}(x\xi^2)$",
         ha="center", fontsize=14, color=INK)
ax = axes[0, 0]
weights = np.array([[.4, .1], [.1, .4]])
ax.imshow(weights, cmap="Blues", vmin=0, vmax=.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, str(Fraction(float(weights[i, j])).limit_denominator()),
                ha="center", va="center", fontsize=20, color=INK)
ax.set_xticks([0, 1], ["$j=1$\n$t_j=2$", "$j=2$\n$t_j=-1$"])
ax.set_yticks([0, 1], [r"$i=1$", r"$i=2$"])
ax.set_title(r"FP2: $\mu_{ij}=\|L_{e_i}R_{e_j}\xi\|^2$"
             "\nBoth marginal sums are (1/2, 1/2)", pad=11, fontsize=12)
ax.set_xlabel("A finite orthogonal array; no joint measure")
ax = axes[0, 1]
ax.fill_between([0, 1], [.4, .4], color=TEAL, alpha=.24)
ax.fill_between([1, 4], [.1, .1], color=TEAL, alpha=.24)
ax.plot([0, 1], [.4, .4], color=TEAL, lw=3)
ax.plot([1, 4], [.1, .1], color=TEAL, lw=3)
ax.plot([4, 4.5], [0, 0], color=TEAL, lw=3)
ax.scatter([1, 4], [.4, .1], color=TEAL, s=45, zorder=5)
ax.scatter([1, 4], [.1, 0], facecolor="white", edgecolor=TEAL, s=45, zorder=5)
ax.text(.50, .20, "area 2/5", ha="center", color=TEAL)
ax.text(2.5, .045, "area 3/10", ha="center", color=TEAL)
ax.set(xlim=(0, 4.5), ylim=(-.025, .5), xlabel=r"cutoff parameter $a>0$",
       ylabel=r"$I_\phi(g_a(h))$")
ax.set_title(r"FP3–FP4: integral $=7/10$"
             "\nClosed dots retain the spectral threshold", fontsize=12)
ax.set_xticks([0, 1, 4])
ax = axes[1, 0]
ax.axis("off")
ax.set_title("FP7 and FP15: exact sample and proved bound", fontsize=12, color=INK)
lines = [
    r"$I_\phi(h)=9/10,\qquad q_\phi(h)^2=5$",
    r"$\int_0^\infty I_\phi(g_a(h))\,da=7/10$",
    r"$7/10\ \leq\ \sqrt{I_\phi(h)}\,q_\phi(h)=3/\sqrt{2}$",
    r"$\int_0^\infty q_\phi(g_a(h))^2\,da=2\cdot1+1\cdot3=5$",
]
for y, line in zip([.81, .59, .36, .13], lines):
    ax.text(.5, y, line, ha="center", color=INK, fontsize=14, transform=ax.transAxes)
ax = axes[1, 1]
ax.axis("off")
ax.set_title(r"HC4–HC5: pinch by $e=E_{11}$", fontsize=12, color=INK)
for x0, offdiag in [(0.05, True), (.61, False)]:
    for i in range(2):
        for j in range(2):
            color = RED if i != j and offdiag else BLUE if i == j else "#e5e8eb"
            ax.add_patch(Rectangle((x0+j*.12, .65-i*.19), .12, .19,
                                   facecolor=color, alpha=.25, edgecolor="white"))
            ax.text(x0+j*.12+.06, .745-i*.19, "2" if i==j else "1" if offdiag else "0",
                    ha="center", va="center", color=INK, fontsize=17)
ax.text(.045, .36, r"$\xi\quad(\times\sqrt{10})$", color=INK, transform=ax.transAxes)
ax.text(.595, .36, r"$T_e\xi\quad(\times\sqrt{10})$", color=INK, transform=ax.transAxes)
ax.annotate("", xy=(.56, .65), xytext=(.34, .65),
            arrowprops={"arrowstyle": "->", "color": INK, "lw": 2})
ax.text(.5, .03, r"$\phi(e)=1/2,\ I_\phi(e)=1/10,\ \phi'(e)=2/5$"
        "\n" + r"$\|\xi\|^2=1,\quad\|T_e\xi\|^2=4/5$",
        ha="center", color=INK, fontsize=13, transform=ax.transAxes)
fig.subplots_adjust(top=.84, bottom=.09, left=.07, right=.97, hspace=.58, wspace=.35)
save(fig, "finite-partition-and-pinching")

fig = plt.figure(figsize=(14, 7.5))
fig.suptitle("Strong unitary completion and the five controlled errors",
             fontsize=18, color=INK, y=.98)
ax = fig.add_axes([.07, .22, .51, .60])
ax.set(xlim=(-.3, 6.6), ylim=(-.5, 1.6))
ax.axis("off")
ax.set_title(r"HC25–HC26: $U_n\to S$ strongly, illustrated at $n=4$",
             color=INK, fontsize=14, pad=15)
for k in range(7):
    ax.scatter(k, 1, color=BLUE, s=65, zorder=3)
    ax.scatter(k, 0, color=TEAL, s=65, zorder=3)
    ax.text(k, 1.15, rf"$e_{k}$", ha="center", fontsize=14, color=INK)
    ax.text(k, -.26, rf"$e_{k}$", ha="center", fontsize=14, color=INK)
for k in range(4):
    ax.add_patch(FancyArrowPatch((k, .94), (k+1, .06), arrowstyle="-|>",
                                color=BLUE, mutation_scale=14, lw=2))
ax.add_patch(FancyArrowPatch((4, .94), (0, .06), arrowstyle="-|>",
                            connectionstyle="arc3,rad=.13", color=RED,
                            mutation_scale=14, lw=2.2))
for k in [5, 6]:
    ax.add_patch(FancyArrowPatch((k, .94), (k, .06), arrowstyle="-|>",
                                color=GOLD, mutation_scale=14, lw=2))
ax.text(2.0, .52, r"$e_4\mapsto e_0$", color=RED, ha="center",
        bbox={"facecolor": "#fafafa", "edgecolor": "none", "pad": 2})
fig.text(.07, .16, r"$S e_k=e_{k+1};\quad U_n e_k=e_{k+1}\ (k<n),\ "
         r"U_n e_n=e_0,\ U_n e_k=e_k\ (k>n)$", fontsize=12, color=INK)
fig.text(.07, .09, r"$U_n^*e_0=e_n,\quad S^*e_0=0$: no strong convergence of adjoints."
         "\nThis is a shift model of the completion mechanism, not a type III factor.",
         fontsize=12, color=INK)
ax = fig.add_axes([.66, .27, .28, .53])
labels = ["initial state", "unitary limit", "commutator", "discarded mass", "final state"]
coefficients = np.array([4, 1, 4, 8, 4])
colors = [BLUE, GOLD, TEAL, RED, BLUE]
ax.barh(np.arange(5), coefficients, color=colors, alpha=.85)
ax.set_yticks(np.arange(5), labels)
ax.invert_yaxis()
ax.set_xlim(0, 9.1)
ax.set_xticks([0, 4, 8])
for i, c in enumerate(coefficients):
    ax.text(c+.15, i, str(c), va="center", fontsize=13, color=INK)
ax.set_xlabel(r"coefficient of $\sqrt{\delta}$")
ax.set_title("HC27: each error has its own bound", fontsize=13, color=INK)
fig.text(.79, .13, r"$4+1+4+8+4=21$" "\n"
         r"$\|\phi_0^{u_n}-\psi_0\|<21\sqrt{\delta}$",
         ha="center", fontsize=16, color=INK)
save(fig, "strong-unitary-and-error-budget")

checks = {
    "finite_array": [["2/5", "1/10"], ["1/10", "2/5"]],
    "left_and_right_marginals": ["1/2", "1/2"],
    "I_h": "9/10", "q_h_squared": "5",
    "cutoff_I_integral": "7/10",
    "cutoff_q_squared_integral": "5",
    "pinched_e_mass": "2/5",
    "pinching_e_mass_loss": "1/10",
    "pinched_total_vector_norm_squared": "4/5",
    "error_coefficients": coefficients.tolist(),
    "error_sum": int(coefficients.sum()),
    "shift_example_n": 4,
    "proof_locators": ["FP2–FP4", "HC2", "HC6"],
    "sample_scope": "Finite matrix and unilateral shift examples illustrate local mechanisms only.",
}
assert Fraction(2, 5)+Fraction(1, 10)==Fraction(1, 2)
assert Fraction(2, 5)+3*Fraction(1, 10)==Fraction(7, 10)
assert Fraction(1, 2)-Fraction(1, 10)==Fraction(2, 5)
assert coefficients.sum()==21
(OUT / "FIGURE_CHECKS.json").write_text(json.dumps(checks, indent=2)+"\n",
                                       encoding="utf-8", newline="\n")
print(json.dumps({p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(OUT.glob("*.png"))}, indent=2))
