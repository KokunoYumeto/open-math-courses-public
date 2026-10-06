"""Reproduce the two SH-03 geometry proof schematics beside this script.

Analytic critical values: finite-conormal-closures-and-generic-base-directions.html
    #analytic-critical-values, formulas (A3), (A7), (A8).
Microlocal refinement: microlocal-stratifications-by-removing-bad-loci.html
    #closed-bad-set-induction, formulas (16), (19), (20), (21).

The diagrams are proof schematics. The full mathematical arguments, hypotheses,
and human-source references remain in the corresponding lessons.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12.5,
    "svg.fonttype": "path",
    "svg.hashsalt": "sh03-v138-stratification-mechanisms",
})

def make_panel(title):
    fig = plt.figure(figsize=(7.2, 9.6))
    fig.patch.set_facecolor("#f8fafc")
    ax = fig.add_axes((.035, .025, .93, .885))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.text(.06, .967, title, ha="left", va="top", fontsize=20,
             fontweight="bold", color="#142438")
    return fig, ax

def box(ax, xy, width, height, text, color="#e7eef8", fontsize=12.5):
    x, y = xy
    ax.add_patch(FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.012,rounding_size=0.015",
        linewidth=1.25, edgecolor="#40556f", facecolor=color))
    ax.text(x+width/2, y+height/2, text, ha="center", va="center",
            fontsize=fontsize, linespacing=1.5, color="#142438")

def arrow(ax, p, q):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=15,
                                linewidth=1.4, color="#40556f"))

def save(fig, name):
    fig.savefig(OUT / (name + ".png"), dpi=170,
                metadata={"Software": "SH-03 programme figure source"})
    fig.savefig(OUT / (name + ".svg"),
                metadata={"Date": None, "Creator": "SH-03 programme figure source"})
    plt.close(fig)

fig, ax = make_panel("Analytic critical values")
box(ax, (.05, .82), .90, .14,
    "$f:M^m\\to N^e$,   $e>0$,   $C_f=\\{\\mathrm{rank}\\,df<e\\}$\n"
    "On a connected source chart: maximum rank $r$.\n"
    "For $r>0$, choose a nonzero analytic $r$-minor $h$.",
    fontsize=12)
box(ax, (.03, .57), .43, .17,
    "$V=\\{h\\ne0\\}$\nConstant rank $r$.\n"
    "$r=e$: no critical points.\n$r<e$: image is null.",
    color="#e4f3ed", fontsize=12)
box(ax, (.54, .57), .43, .17,
    "Remaining critical points\n$C_f\\cap\\{h=0\\}$\n"
    "$\\{h=0\\}\\subset\\bigcup_\\beta H_\\beta$\n"
    "Countably many hypersurfaces.", fontsize=11.5)
arrow(ax, (.30, .805), (.25, .757))
arrow(ax, (.70, .805), (.75, .757))
box(ax, (.08, .33), .84, .16,
    "$H_\\beta=\\{\\partial^\\beta h=0,\\ d(\\partial^\\beta h)\\ne0\\}$\n"
    "$C_f\\cap H_\\beta\\subset C_{f|_{H_\\beta}}$\n"
    "Apply induction in source dimension $m-1$.")
arrow(ax, (.75, .555), (.62, .507))
box(ax, (.08, .10), .84, .14,
    "Countably many null critical-value sets\n"
    "$\\Longrightarrow f(C_f)$ has measure zero.\n"
    "Base case: a countable zero-dimensional source.",
    color="#e4f3ed", fontsize=12)
arrow(ax, (.50, .312), (.50, .257))
ax.text(.50, .012,
        "Proof schematic: analytic critical-value theorem, (A3), (A7)–(A8).\n"
        "If $r=0$, the map is constant on the connected source chart.\n"
        "Hypersurfaces may overlap and include extra points.",
        ha="center", va="bottom", fontsize=10, color="#45566b",
        linespacing=1.45)
save(fig, "analytic-critical-values")

fig, ax = make_panel("Microlocal refinement")
box(ax, (.05, .82), .90, .14,
    "Closed subanalytic residual $Y_k$\n"
    "Current stratification is $\\mu$ on $X\\setminus Y_k$.\n"
    "Each stratum lies inside or outside $Y_k$.\n"
    "The union of pair bad sets has $B_k\\subset Y_k$.", fontsize=12)
box(ax, (.08, .59), .84, .14,
    "$\\Omega_k=X\\setminus\\overline{B_k}$\n"
    "Largest good open set; $\\Omega_k\\cap Y_k$ is dense in $Y_k$.\n"
    "Locally, only finitely many ordered pairs occur.", fontsize=12)
arrow(ax, (.50, .805), (.50, .747))
box(ax, (.03, .33), .43, .17,
    "Retain the old open pieces\n"
    "$P_a=S_a\\cap\\Omega_k$\n"
    "Their tangent spaces and\n$\\mu$-conditions are preserved.",
    color="#e4f3ed", fontsize=11.5)
box(ax, (.54, .33), .43, .17,
    "$Y_{k+1}=\\overline{B_k}\\subset Y_k$\n"
    "Closed, nowhere dense in $Y_k$.\n"
    "$Y_{k+1}\\ne\\varnothing$ implies\n"
    "$\\dim Y_{k+1}<\\dim Y_k$.", fontsize=11.5)
arrow(ax, (.32, .572), (.25, .517))
arrow(ax, (.68, .572), (.75, .517))
box(ax, (.08, .10), .84, .14,
    "Refine only $Y_{k+1}$, remembering\n"
    "old memberships and every $Y_{k+1}\\cap\\overline{P_a}$.\n"
    "At most $n+1$ stages, where $n=\\dim X$.")
arrow(ax, (.75, .312), (.62, .257))
ax.text(.50, .012,
        "Induction schematic: closed bad-set proof, (16)–(21).\n"
        "Ambient local finiteness is required at every stage.\n"
        "Relative density is checked on every regular dimension part.",
        ha="center", va="bottom", fontsize=10, color="#45566b",
        linespacing=1.45)
save(fig, "microlocal-refinement")
