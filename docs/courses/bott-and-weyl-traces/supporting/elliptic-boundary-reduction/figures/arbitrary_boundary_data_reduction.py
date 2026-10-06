from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
SVG = HERE / "arbitrary_boundary_data_reduction.svg"
PNG = HERE / "arbitrary_boundary_data_reduction.png"

INK = "#132238"
BLUE = "#2468A2"
BLUE_BG = "#EAF4FB"
AMBER = "#A86205"
AMBER_BG = "#FFF3D6"
GREEN = "#2D725B"
GREEN_BG = "#E7F4EE"
RED = "#A43E3E"
RED_BG = "#FBECEC"
GREY = "#657383"


fig, ax = plt.subplots(figsize=(15.2, 6.8), dpi=200)
fig.patch.set_facecolor("white")
ax.set_xlim(0, 15.2)
ax.set_ylim(0, 6.8)
ax.axis("off")


def box(x, y, w, h, title, lines, edge, face):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.05,rounding_size=0.12",
        linewidth=1.8,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h - 0.28, title, ha="center", va="top",
            fontsize=11.5, fontweight="bold", color=INK)
    ax.text(x + w / 2, y + h / 2 - 0.08, lines, ha="center", va="center",
            fontsize=10.5, color=INK, linespacing=1.5)
    return patch


def arrow(x1, y1, x2, y2, color=INK, text=None, bend=0.0, dashed=False):
    style = "arc3" if bend == 0 else f"arc3,rad={bend}"
    patch = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=15,
        linewidth=1.8,
        linestyle="--" if dashed else "-",
        color=color,
        connectionstyle=style,
    )
    ax.add_patch(patch)
    if text:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.18, text,
                ha="center", va="bottom", fontsize=9.5, color=color,
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


ax.text(0.45, 6.42, "Arbitrary boundary data through an elliptic reference problem",
        fontsize=18, fontweight="bold", color=INK, va="top")
ax.text(0.45, 6.02,
        "The same reduced operator controls regularity and solvability modulo smooth errors.",
        fontsize=11.5, color=GREY, va="top")

box(0.45, 3.82, 2.25, 1.45, "Interior forcing",
    r"$f\in\bar H^{s-m}(X^\circ,F)$" + "\n" + r"$L_0f=(I+KS''\gamma)Vf$",
    BLUE, BLUE_BG)
box(0.45, 1.45, 2.25, 1.45, "Reference data",
    r"$g=Bu\in\mathcal{D}_B^s$" + "\n" + r"$KSg$",
    AMBER, AMBER_BG)
box(3.55, 2.65, 2.55, 1.65, "Parametrix ansatz",
    r"$u=L_0\widetilde f+KSg$" + "\n" + r"$u-L(Pu,Bu)=\mathcal{R}u$",
    GREEN, GREEN_BG)
box(7.05, 3.82, 2.65, 1.45, "Interior row",
    r"$Pu=\widetilde f+K_1\widetilde f+K_2g$" + "\n" + r"$K_1,K_2:\ \mathrm{data}\to C^\infty$",
    BLUE, BLUE_BG)
box(7.05, 1.45, 2.65, 1.45, "Comparison row",
    r"$Cu=CL_0\widetilde f+Mg$" + "\n" + r"$M=C^cQS$",
    AMBER, AMBER_BG)
box(10.75, 2.65, 3.95, 1.65, "Boundary reduction",
    r"$M:\mathcal{D}_B^s\longrightarrow\mathcal{D}_C^s$" + "\n" +
    r"$M_{kj}\in\Psi^{\mu_k-m_j}$" + "\n" +
    r"$M-C^cS\in\Psi^{-\infty}$",
    RED, RED_BG)

arrow(2.70, 4.54, 3.55, 3.80, BLUE, r"$L_0$")
arrow(2.70, 2.18, 3.55, 3.13, AMBER, r"$KS$")
arrow(6.10, 3.72, 7.05, 4.54, BLUE, r"$P$")
arrow(6.10, 3.20, 7.05, 2.18, AMBER, r"$C$")
arrow(9.70, 2.18, 10.75, 3.08, AMBER, r"$Mg$")
arrow(9.70, 4.52, 10.75, 3.90, BLUE, r"$\widetilde f-f\in C^\infty$", bend=-0.08)

ax.plot([0.45, 14.70], [0.86, 0.86], color="#D3DAE2", linewidth=1.2)
ax.text(0.52, 0.55, "Exact route:", color=INK, fontsize=10.5, fontweight="bold", va="center")
ax.text(1.68, 0.55,
        r"$(\widetilde f,g)\mapsto u\mapsto(Pu,Cu)$ uses both right errors.",
        color=INK, fontsize=10.5, va="center")
ax.text(7.35, 0.55, "Converse route:", color=INK, fontsize=10.5, fontweight="bold", va="center")
ax.text(8.83, 0.55,
        r"$u=L(Pu,Bu)+\mathcal{R}u$ keeps the smooth left error.",
        color=INK, fontsize=10.5, va="center")

plt.tight_layout(pad=0.45)
fig.savefig(SVG, bbox_inches="tight", facecolor="white")
fig.savefig(PNG, bbox_inches="tight", facecolor="white", dpi=200)
plt.close(fig)
