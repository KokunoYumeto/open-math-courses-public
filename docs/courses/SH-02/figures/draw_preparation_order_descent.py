"""Native mathematical mechanism figure for FI3, with exact source locators.

This is an equation diagram, not a numerical plot or an empirical proof.
Outputs SVG and PNG next to this reproducible source.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "svg.fonttype": "none", "svg.hashsalt": "SH02-TC-preparation-v1", "mathtext.fontset": "dejavusans"})
fig, ax = plt.subplots(figsize=(13.4, 8.8), dpi=160)
fig.patch.set_facecolor("#f8fafc")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

def box(x, y, width, height, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                               boxstyle="round,pad=0.012,rounding_size=0.012",
                               facecolor=color, edgecolor="#94a3b8", linewidth=1.2))

def label(x, y, text, size=14, weight="normal", color="#0f172a"):
    ax.text(x, y, text, ha="left", va="center", fontsize=size,
            fontweight=weight, color=color)

def arrow(start, stop):
    ax.add_patch(FancyArrowPatch(start, stop, arrowstyle="-|>",
                                mutation_scale=18, linewidth=1.5,
                                color="#334155"))

label(.025, .96, "Why the preparation induction terminates", 21, "bold")
label(.025, .91, "After the affine change removes the coefficient of the next highest power", 13)

box(.04, .715, .92, .15, "#e0f2fe")
label(.07, .824, r"$\widehat{P}(x,w)=w^e+\sum_{i=2}^{e}b_i(x)w^{\,e-i}$", 18)
label(.07, .761, r"$q(x)=\max_{2\leq i\leq e}|b_i(x)|^{1/i}>0$; fix a maximizing index $j$ and its sign", 14)

arrow((.29, .705), (.29, .652))
arrow((.73, .705), (.73, .652))
box(.04, .395, .43, .24, "#ecfdf5")
box(.53, .395, .43, .24, "#eff6ff")
label(.07, .594, r"Outside: $|w|\geq 2q$", 17, "bold")
label(.07, .512, r"$\left|\sum_{i=2}^{e} b_i w^{-i}\right|\leq \frac{1}{2}-2^{-e}<\frac{1}{2}$", 16)
label(.07, .427, "An explicit analytic unit; exponent e", 12)
label(.56, .594, r"Inside: $0<|w|\leq 2q$", 17, "bold")
label(.56, .537, r"$v=w/q,\quad\beta_i=b_i/q^i$", 17)
label(.56, .485, r"$R(\beta,v)=v^e+\beta_2v^{e-2}+\cdots+\beta_e$", 15)
label(.56, .431, r"$|\beta_i|\leq 1,\quad \beta_j=\pm1,\quad |v|\leq 2$", 15)

arrow((.73, .383), (.73, .326))
box(.04, .14, .92, .17, "#fff7ed")
label(.07, .269, r"If derivatives of every order $0,\ldots,e-1$ vanished at a compact-image point:", 14)
label(.07, .216, r"$\partial_v^{e-1}R=e!v=0\ \Longrightarrow\ v=0$", 18)
label(.07, .164, r"$\partial_v^{e-i}R(\beta,0)=(e-i)!\beta_i=0\ \Longrightarrow\ \beta_j=0\ne\pm1$", 17)

label(.04, .099, r"Therefore $\operatorname{ord}_v R\leq e-1$ everywhere on the actual compact normalized image.", 15, "bold")
label(.04, .05, "Exact proof: FI3c–FI3d. Immutable FCT, lines 959–1008, revision cecb8f47005cccf0fa742714d07d259304661666.", 9)
label(.04, .02, "Zero coefficients and w = 0, ±2q are separate base/graph pieces. The diagram supplies no cross-cell analyticity claim.", 9)

fig.savefig(OUT/"preparation-order-descent.svg", bbox_inches="tight", facecolor=fig.get_facecolor(), metadata={"Date": None})
fig.savefig(OUT/"preparation-order-descent.png", bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close(fig)
print("Rendered preparation-order-descent.svg and preparation-order-descent.png")
