"""Render the exact generalized collar parametrix and its five retained errors."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
SVG = HERE / "generalized_collar_parametrix.svg"
PNG = HERE / "generalized_collar_parametrix.png"

BG = "#fffdf8"
INK = "#173750"
MUTED = "#52616d"
BLUE = "#e9f3f8"
BLUE_EDGE = "#4d7891"
GREEN = "#edf6ec"
GREEN_EDGE = "#608358"
ORANGE = "#fff1e4"
ORANGE_EDGE = "#a66c3f"
PURPLE = "#f3edf8"
PURPLE_EDGE = "#80669a"
RED = "#fff0ee"
RED_EDGE = "#a85d51"

fig, ax = plt.subplots(figsize=(16.0, 9.3))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9.3)
ax.axis("off")


def box(x, y, w, h, text, face=BLUE, edge=BLUE_EDGE, size=12, weight=None):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.12,rounding_size=0.12",
        facecolor=face, edgecolor=edge, linewidth=1.8,
    )
    ax.add_patch(p)
    ax.text(
        x + w / 2, y + h / 2, text,
        ha="center", va="center", fontsize=size, color=INK,
        weight=weight, linespacing=1.25,
    )
    return p


def arrow(x0, y0, x1, y1, label=None, color=MUTED, curve=0.0, offset=0.16, size=10.5):
    p = FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=16,
        linewidth=1.7, color=color,
        connectionstyle=f"arc3,rad={curve}",
    )
    ax.add_patch(p)
    if label:
        ax.text(
            (x0 + x1) / 2, (y0 + y1) / 2 + offset,
            label, ha="center", va="bottom", fontsize=size, color=color,
        )
    return p


ax.text(
    8, 8.95,
    "A first-order Calderón defect still gives a Fredholm boundary parametrix",
    ha="center", va="center", fontsize=19, weight="bold", color=INK,
)
ax.text(
    8, 8.52,
    r"The order $-1$ terms are kept in the algebra; only $\mathcal{K}_4$ is smoothing.",
    ha="center", va="center", fontsize=11.7, color=MUTED,
)

# Top band: the boundary algebra.
ax.text(0.55, 7.95, "Boundary algebra", fontsize=13.5, weight="bold", color=INK)
box(0.55, 6.40, 2.15, 1.00, r"Cauchy vector" + "\n" + r"$U=\gamma u$", BLUE, BLUE_EDGE, 13)
box(3.35, 6.40, 2.55, 1.00, r"measurement" + "\n" + r"$g=\mathcal{B}U$", GREEN, GREEN_EDGE, 12.5)
box(6.55, 6.40, 2.65, 1.00, r"stable part" + "\n" + r"$Q U$", PURPLE, PURPLE_EDGE, 12.5)
box(9.85, 6.40, 2.85, 1.00, r"projected inverse" + "\n" + r"$S=QT$", ORANGE, ORANGE_EDGE, 12.5)
box(13.25, 6.40, 2.20, 1.00, r"$\mathcal{B}QS-I$" + "\n" + r"smoothing", GREEN, GREEN_EDGE, 12.5)

arrow(2.72, 6.90, 3.32, 6.90, r"$\mathcal{B}$", offset=0.43)
arrow(5.93, 6.90, 6.52, 6.90, r"$q^2=q$", offset=0.43)
arrow(9.23, 6.90, 9.82, 6.90, r"$\mathcal{B}Q^2T\equiv I$", offset=0.43)
arrow(12.73, 6.90, 13.22, 6.90, r"right error", offset=0.43)

box(
    4.25, 5.05, 7.55, 0.78,
    r"$U=Sg+S''(I-Q)U+R_1U,$"
    + "   " + r"$Q^2-Q,\ S''Q,\ R_1\in\Psi^{-1}_{\rm wt}$",
    RED, RED_EDGE, 12.6, "bold",
)
arrow(1.63, 6.38, 4.45, 5.82, r"exact decomposition", RED_EDGE, -0.12, 0.08)
arrow(10.95, 6.38, 11.15, 5.84, r"one order retained", RED_EDGE, 0.10, 0.08)

# Divider.
ax.plot([0.45, 15.55], [4.70, 4.70], color="#cbd3d6", linewidth=1.4)

# Bottom band: the two-sided parametrix identities.
ax.text(0.55, 4.27, "Parametrix and errors", fontsize=13.5, weight="bold", color=INK)
box(0.55, 2.77, 2.15, 1.05, r"data" + "\n" + r"$(f,g)$", BLUE, BLUE_EDGE, 14)
box(
    3.45, 2.65, 4.25, 1.28,
    r"$\mathcal{L}(f,g)$"
    + "\n" + r"$=(I+KS''\gamma)Vf+KSg$",
    ORANGE, ORANGE_EDGE, 13, "bold",
)
box(8.52, 2.77, 2.25, 1.05, r"section" + "\n" + r"$u$", GREEN, GREEN_EDGE, 14)
box(
    11.55, 2.52, 3.90, 1.55,
    r"$u=\mathcal{L}(Pu,Bu)+\mathcal{K}u$"
    + "\n" + r"$\mathcal{K}:H_{(s,t)}\to H_{(s+1,t)}$",
    PURPLE, PURPLE_EDGE, 12.3,
)

arrow(2.73, 3.30, 3.42, 3.30, r"$V,K,S,S''$")
arrow(7.73, 3.30, 8.49, 3.30, r"construct")
arrow(10.80, 3.30, 11.52, 3.30, r"left identity")

box(
    1.00, 0.72, 4.10, 1.18,
    r"$P\mathcal{L}(f,g)=f+\mathcal{K}_1f+\mathcal{K}_2g$"
    + "\n" + r"$\mathcal{K}_1,\mathcal{K}_2$: one-derivative gains",
    BLUE, BLUE_EDGE, 11.7,
)
box(
    6.00, 0.72, 4.10, 1.18,
    r"$B\mathcal{L}(f,g)=g+\mathcal{K}_3f+\mathcal{K}_4g$"
    + "\n" + r"$\mathcal{K}_3$: one derivative; $\mathcal{K}_4$: smoothing",
    GREEN, GREEN_EDGE, 11.7,
)
box(
    11.00, 0.72, 4.45, 1.18,
    r"compact defects at the base level"
    + "\n" + r"$\Longrightarrow$ closed range, finite kernel and cokernel",
    RED, RED_EDGE, 11.7, "bold",
)

arrow(5.25, 2.62, 3.50, 1.93, r"interior row", BLUE_EDGE, 0.08, 0.05)
arrow(6.25, 2.62, 8.05, 1.93, r"boundary row", GREEN_EDGE, -0.08, 0.05)
arrow(10.15, 1.31, 10.97, 1.31, r"compact inclusion", RED_EDGE, 0.0, 0.13)

ax.text(
    8, 0.28,
    r"Exact cancellation: $\mathcal{B}(I+QS'')=\mathcal{B}Q+D_{-1}$, "
    r"with $(D_{-1})_{jk}\in\Psi^{m_j-k-1}$.",
    ha="center", va="center", fontsize=11.5, color=MUTED,
)

fig.tight_layout(pad=0.35)
fig.savefig(SVG, facecolor=fig.get_facecolor())
fig.savefig(PNG, dpi=180, facecolor=fig.get_facecolor())
plt.close(fig)
print(f"{SVG}\n{PNG}")
