"""Figure 22.6: maps and dimensions in 22.85--88, with no chosen splitting."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
                     "font.size": 12})
fig, ax = plt.subplots(figsize=(12, 8), facecolor="white")
ax.set(xlim=(0, 12), ylim=(0, 8))
ax.axis("off")


def box(x, y, width, height, text, color="#eff6ff", size=16):
    ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.16",
                                facecolor=color, edgecolor="#94a3b8", linewidth=1.2))
    ax.text(x+width/2, y+height/2, text, ha="center", va="center", fontsize=size)


def arrow(start, end, label, label_position):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "-|>", "lw": 1.8,
                                            "color": "#334155", "mutation_scale": 16})
    ax.text(*label_position, label, ha="center", va="center", fontsize=12,
            color="#334155")


ax.text(6, 7.65, "One period, two descriptions", ha="center", fontsize=21, weight="bold")
ax.text(6, 7.19, "Algebraic de Rham classes and the universal vector extension",
        ha="center", color="#475569")

box(.45, 5.25, 3.6, 1.1, r"$\theta\in\operatorname{Lie}(A^\natural)^\vee$")
box(7.95, 5.25, 3.6, 1.1, r"$\xi=\Theta_A(\theta)\in H^1_{\rm dR}(A/k)$")
arrow((4.3, 5.8), (7.7, 5.8), r"$\Theta_A$ : algebraic isomorphism", (6, 6.15))
ax.text(6, 5.35, r"both spaces have dimension $2g$ over $k$", ha="center", fontsize=11)

box(.45, 3.18, 3.6, 1.1, r"$\lambda^\natural\in\Lambda_{A^\natural}$", "#f0fdf4")
box(7.95, 3.18, 3.6, 1.1, r"$\lambda\in\Lambda_A$", "#f0fdf4")
arrow((4.3, 3.73), (7.7, 3.73), r"$d\pi_A$ : lattice isomorphism", (6, 4.12))
ax.text(6, 3.29, r"both lattices have rank $2g$ over $\mathbf{Z}$", ha="center", fontsize=11)
ax.text(2.25, 4.75, "evaluate on", ha="center", color="#334155")
ax.text(9.75, 4.75, "integrate along the loop of", ha="center", color="#334155")
box(2.2, 1.87, 7.6, .7,
    r"$\theta(\lambda^\natural)=\int_{\gamma_\lambda}\xi$", "#fff7ed", 18)
ax.text(6, 1.48, r"$\gamma_\lambda(t)=\exp_A(t\lambda)$,  $0\leq t\leq1$",
        ha="center", fontsize=12)

ax.plot([.3, 11.7], [1.1, 1.1], color="#cbd5e1")
ax.text(.5, .78, "Elliptic normalization", weight="bold", fontsize=12)
ax.text(.5, .35, r"$\alpha=dx/y,\quad\beta=x\,dx/y,\quad\zeta'=-\wp$", fontsize=14)
ax.text(7, .78, r"$\int_{\gamma_j}\alpha=\omega_j$", fontsize=15)
ax.text(7, .32, r"$\int_{\gamma_j}\beta=-\eta_j$", fontsize=15)
fig.text(.04, .018, "Theorems 22.85–22.87 and Proposition 22.88. No splitting of the Hodge sequence is chosen.",
         fontsize=10, color="#475569")
fig.subplots_adjust(left=.03, right=.97, top=.98, bottom=.06)
output = Path(__file__).with_suffix(".png")
fig.savefig(output, dpi=170, facecolor="white")
plt.close(fig)
print(output)
