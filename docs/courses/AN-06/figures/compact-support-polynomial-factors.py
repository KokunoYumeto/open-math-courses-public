"""CC0. Reproduce the factor argument in Lemma 1.1.

Requires Python 3.12 and Matplotlib 3.11.2. No TeX executable is used.
The boxes are operators, not numerical samples or assertions about roots.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "svg.hashsalt": "AN06-compact-support-polynomial-factors-v1",
    "text.usetex": False,
})
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

folder = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(12, 5.2), dpi=140)
fig.patch.set_facecolor("white")
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.axis("off")
ax.text(.5, .94, "Insert a polynomial factor; preserve the support",
        ha="center", fontsize=17, fontweight="bold", color="#173447")
for x in [.055, .57]:
    ax.add_patch(FancyBboxPatch((x, .57), .37, .19,
        boxstyle="round,pad=0.018", facecolor="#eaf4f7",
        edgecolor="#23738b", linewidth=1.4))
ax.text(.24, .68, r"$w_1=a(D_t-r_2)(D_t-r_3)w$",
        ha="center", va="center", fontsize=14)
ax.text(.24, .61, "supported in (-1, 1)", ha="center", fontsize=12)
ax.text(.755, .68, r"$(D_t-r_1)w_1=p_\eta(D_t)w$",
        ha="center", va="center", fontsize=14)
ax.text(.755, .61, "supported in (-1, 1)", ha="center", fontsize=12)
ax.annotate("", xy=(.55, .665), xytext=(.445, .665),
            arrowprops={"arrowstyle": "->", "color": "#23738b", "lw": 2})
ax.text(.5, .78, r"$D_t-r_1$", ha="center", fontsize=14)
ax.text(.5, .44, r"$\|w_1\|_{L^2_t}\leq2\|p_\eta(D_t)w\|_{L^2_t}$",
        ha="center", fontsize=16, color="#173447")
ax.text(.5, .32, "The same bound holds for either of the other omitted factors.",
        ha="center", fontsize=13)
ax.text(.5, .21,
        r"$p_\eta'(D_t)w=w_1+w_2+w_3"
        r"\quad\Longrightarrow\quad"
        r"\|p_\eta'(D_t)w\|_{L^2_t}\leq6\|p_\eta(D_t)w\|_{L^2_t}$",
        ha="center", fontsize=15, color="#173447")
ax.text(.5, .085,
        "Fixed tangential frequency eta; degree 3; arbitrary complex roots, including repeats.",
        ha="center", fontsize=11, color="#465d69")
ax.text(.5, .035,
        "Lemma 1.1, equations (3)-(4). All norms use Lebesgue measure in t.",
        ha="center", fontsize=11, color="#465d69")
fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
fig.savefig(folder / "compact-support-polynomial-factors.svg",
            metadata={"Date": None, "Creator": "CC0 original plotting source"})
fig.savefig(folder / "compact-support-polynomial-factors.png",
            metadata={"Software": "CC0 original plotting source"})
plt.close(fig)
