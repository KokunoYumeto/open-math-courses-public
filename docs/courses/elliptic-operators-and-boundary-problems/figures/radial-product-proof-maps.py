"""Reproduce the U039 endpoint maps and exact n=1 exponent regions.

Written and dedicated to the public domain by Codex, October 2026 (CC0).
All diagram mathematics is proved in radial-symbol-index-transport.md,
PT15--PT21 and RS1--RS29. No external mathematical source is used.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "mathtext.fontset": "dejavusans",
    "svg.hashsalt": "an03-u039-radial-product-proof-maps-264",
})
PARAMETERS = {
    "configuration_dimension": 1,
    "coefficient_rank_in_marked_example": 1,
    "exponent_axes": {"P": [0, 3.1], "Q": [0, 3.1]},
    "whole_class_trace_conditions": ["P > 1", "Q > 1"],
    "whole_class_hilbert_schmidt_conditions": ["2P > 1", "2Q > 1"],
    "marked_example": {
        "P": 2, "Q": 1,
        "symbol": "(1+x^2)^(-1)*(1+xi^2)^(-1/2)",
        "hilbert_schmidt_norm_squared": "pi/4",
        "trace_class": False,
        "compact": True,
    },
    "equal_exponent_line": "P=Q=N",
    "radial_index_interval": "0 <= epsilon <= epsilon_* <= 1",
    "operator_norm_obstruction": {
        "symbol": "2+arctan(x)",
        "coherent_centres": ["R", "R^2"],
        "lower_bound": "pi/2",
        "parameter_range": "0 < epsilon <= 1",
        "meaning": "proved operator-norm lower bound, not a numerical sample",
    },
    "proof_locators": ["RC7", "PT4", "PT20", "RS11", "RS14", "RS18",
                       "RS19--RS25", "CI5 in the earlier trace lesson"],
    "source": "Complete original programme proofs in this lesson and the linked earlier trace lesson.",
    "license": "CC0-1.0",
}

fig = plt.figure(figsize=(15, 8), layout=None, facecolor="white")
left = fig.add_axes([.035, .12, .46, .76])
right = fig.add_axes([.57, .20, .38, .61])
left.set(xlim=(0, 1), ylim=(0, 1))
left.axis("off")

def box(y, height, lines, colour, size=12):
    patch = FancyBboxPatch((.035, y), .93, height,
                          boxstyle="round,pad=0.012",
                          facecolor=colour, edgecolor="#526477", linewidth=1.2)
    left.add_patch(patch)
    left.text(.5, y+height/2, lines, ha="center", va="center",
              fontsize=size, linespacing=1.35)

def arrow(y1, y2, x=.5):
    left.annotate("", xy=(x, y2), xytext=(x, y1),
                  arrowprops={"arrowstyle": "->", "lw": 1.7, "color": "#365777"})

left.set_title("The actual radial receiving maps", fontsize=17, pad=12)
box(.815, .15,
    r"$a_\varepsilon=a\circ F_\varepsilon,\quad b_\varepsilon=b\circ F_\varepsilon$"
    "\n"
    r"bounded in $S(1,G)$; locally equal to $a,b$ near $\varepsilon=0$"
    "\n" r"$\chi_\varepsilon=\chi$ on $0\leq\varepsilon\leq\varepsilon_*$",
    "#e7edf6", 12)
box(.60, .14,
    r"$A_\varepsilon\to A_0,\quad A_\varepsilon^*\to A_0^*$ strongly on $H_\nu$"
    "\n" r"$H_\nu=L^2(\mathbb{R}^n;\mathbb{C}^\nu)$"
    "\n" "Schwartz receivers and the uniform operator bound",
    "#eef2f5", 12)
arrow(.80, .755, .19)
left.text(.035, .775, "RS11; B26", fontsize=10)

box(.375, .14,
    r"$E_{j,\varepsilon}^{\,n+1}\to E_{j,0}^{\,n+1}$ in trace norm"
    "\n" r"$j=1,2$; both original matrix orders"
    "\n" "Full product weights, factorization and dominated convergence",
    "#e6f3ee", 12)
# This separate arrow starts at the original symbol box. Strong operator
# convergence alone is not asserted to imply the trace-norm result.
left.annotate("", xy=(.97, .455), xytext=(.97, .855),
              arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=-.12",
                          "lw": 1.7, "color": "#2d795e"})
left.text(.73, .552, "PT15; PT20", color="#2d795e", fontsize=10)
box(.195, .10,
    r"$\mathrm{ind}\,A_\varepsilon=\mathrm{ind}\,A_0$"
    "\n" r"$0\leq\varepsilon\leq\varepsilon_*$ (RS14)",
    "#d7eade", 13)
arrow(.36, .312)
left.text(.55, .332, "T28; integer traces", fontsize=10)
box(.018, .115,
    r"$a(x,\xi)=2+\arctan x,\quad n=\nu=1$"
    "\n" r"$\|A_\varepsilon-A_0\|\geq\pi/2,\quad 0<\varepsilon\leq1$"
    "\n" r"Coherent centres $(R,R^2)$ prove the bound (RS16--RS18).",
    "#fcf0e7", 11.5)

right.add_patch(Rectangle((.5, .5), 2.6, 2.6,
                          facecolor="#dbe6f5", edgecolor="none"))
right.add_patch(Rectangle((1, 1), 2.1, 2.1,
                          facecolor="#c5e4d1", edgecolor="none"))
right.plot([0, 3.1], [0, 3.1], color="#586176", lw=1.7,
           linestyle="-.", zorder=3)
for t in [.5, 1]:
    right.axvline(t, color="#536a80", linestyle="--", lw=1.2)
    right.axhline(t, color="#536a80", linestyle="--", lw=1.2)
right.scatter([2], [1], s=70, c="#a74723", edgecolors="white",
              linewidths=1, zorder=5)
right.annotate(r"$(P,Q)=(2,1)$" "\nHilbert–Schmidt and compact\n"
               r"not trace class; $\|u_{2,1}^w\|_2^2=\pi/4$",
               xy=(2, 1), xytext=(1.48, .12),
               fontsize=10.5, ha="left", va="bottom",
               arrowprops={"arrowstyle": "->", "color": "#a74723", "lw": 1.2},
               bbox={"boxstyle": "round,pad=.35", "fc": "white", "ec": "#dfc9bd"})
right.text(2.45, 1.70, "Trace class\n"
           r"$P>1,\ Q>1$", ha="center", va="center", fontsize=12)
right.text(.76, 2.10, "Hilbert–Schmidt guarantee\n"
           r"$2P>1,\ 2Q>1$", fontsize=10,
           ha="center", va="center", rotation=90)
right.text(1.53, 1.98, r"$P=Q=N$", rotation=44,
           fontsize=11, ha="center", color="#414958")
right.set(xlim=(0, 3.1), ylim=(0, 3.1),
          xticks=[0, .5, 1, 2, 3], yticks=[0, .5, 1, 2, 3],
          xlabel=r"Original exponent $P$ in $\langle x\rangle^{-P}$",
          ylabel=r"Original exponent $Q$ in $\langle\xi\rangle^{-Q}$")
right.set_title("Whole-class guarantees, n = 1", fontsize=16, pad=13)
right.set_aspect("equal")
right.spines[["top", "right"]].set_visible(False)
right.text(.5, -.13,
           r"$u_{P,Q}(x,\xi)=\langle x\rangle^{-P}\langle\xi\rangle^{-Q}I_\nu$"
           "\nDashed threshold lines are excluded from the stated guarantees.",
           transform=right.transAxes, ha="center", va="top", fontsize=10.5)

fig.suptitle("Radial index transport and the two separate decay weights",
             fontsize=20, y=.96)
fig.text(.5, .020,
         "Complete programme proofs: PT15–PT21; RS1–RS29. "
         "Exact operators, domains, coordinate groups and factors are retained.",
         ha="center", fontsize=10.5)
fig.canvas.draw()
fig.savefig(ROOT/"radial-product-proof-maps.png", dpi=240)
fig.savefig(ROOT/"radial-product-proof-maps.svg",
            metadata={"Date": None, "Creator": "Codex; reproducible CC0 programme proof diagram"})
(ROOT/"radial-product-proof-maps.parameters.json").write_text(
    json.dumps(PARAMETERS, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
plt.close(fig)
