"""Render the exact reduction chain from ordered Weyl errors to the exterior form."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
SVG = HERE / "ordered_weyl_exterior_reduction.svg"
PNG = HERE / "ordered_weyl_exterior_reduction.png"


fig, ax = plt.subplots(figsize=(16, 8.2))
fig.patch.set_facecolor("#fffdf8")
ax.set_facecolor("#fffdf8")
ax.set_xlim(0, 16)
ax.set_ylim(0, 8.2)
ax.axis("off")


def box(x, y, w, h, title, lines, face, edge):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.16,rounding_size=0.16",
        facecolor=face, edgecolor=edge, linewidth=1.8,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h - 0.35, title, ha="center", va="top",
            fontsize=12.5, weight="bold", color="#173750")
    ax.text(x + w / 2, y + h / 2 - 0.12, lines, ha="center", va="center",
            fontsize=11.2, color="#263746", linespacing=1.45)
    return patch


def arrow(x0, y0, x1, y1, label=""):
    a = FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=17,
        linewidth=1.7, color="#6c7780", connectionstyle="arc3,rad=0",
    )
    ax.add_patch(a)
    if label:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.18, label,
                ha="center", va="bottom", fontsize=9.6, color="#53616d")


colors = [
    ("#edf4f8", "#5f8298"),
    ("#eff6ec", "#6f8b64"),
    ("#fff3e8", "#a7784f"),
    ("#f4eff8", "#826d96"),
    ("#f8f2e8", "#9a8056"),
    ("#eaf5f2", "#5c8a7c"),
]

box(0.35, 4.65, 2.25, 2.25, "1  Finite error power",
    r"$N>n$" + "\n" + r"$\operatorname{ind}a^w=A_n^{(N)}$" + "\n" +
    r"exactly $2n$ derivatives", *colors[0])
box(3.05, 4.65, 2.25, 2.25, "2  Independent scales",
    r"$z_j\mapsto\rho_jz_j$" + "\n" + r"$\rho^{\alpha-\mathbf{1}}$" + "\n" +
    r"only $\alpha=\mathbf{1}$ survives", *colors[1])
box(5.75, 4.65, 2.25, 2.25, "3  Full alternation",
    r"$\sum_{\tau\in S_{2n}}\!\operatorname{sgn}(\tau)$" + "\n" +
    "two derivatives on one factor" + "\n" + "cancel in sign-reversed pairs", *colors[2])
box(8.45, 4.65, 2.25, 2.25, "4  First brackets remain",
    r"$tI+\frac{i}{2}\{b,a\}$" + "\n" +
    r"$\binom{N}{n}t^{N-n}(i/2)^n$" + "\n" +
    r"$\times(\{b,a\}^n-\{a,b\}^n)$", *colors[3])
box(11.15, 4.65, 2.25, 2.25, "5  Exterior count",
    r"$2^n n!$ exact choices" + "\n" +
    r"$\widetilde\Omega=(-1)^n\Omega$" + "\n" +
    r"$\operatorname{Tr}(da\wedge db)^n=-\operatorname{Tr}(db\wedge da)^n$", *colors[4])
box(13.85, 4.65, 1.8, 2.25, "6  Choose $N=2n$",
    r"$\binom{2n}{n}$" + "\n" + r"$t^{N-n}=t^n$" + "\n" + "exact cutoff power", *colors[5])

for x0, x1 in ((2.60, 3.05), (5.30, 5.75), (8.00, 8.45),
               (10.70, 11.15), (13.40, 13.85)):
    arrow(x0, 5.78, x1, 5.78)

final = FancyBboxPatch(
    (3.0, 1.10), 10.0, 2.15,
    boxstyle="round,pad=0.2,rounding_size=0.18",
    facecolor="#e8f2f7", edgecolor="#315f78", linewidth=2.2,
)
ax.add_patch(final)
ax.text(8.0, 2.82, "Direct exterior index formula", ha="center", va="top",
        fontsize=14.5, weight="bold", color="#173750")
ax.text(
    8.0, 2.08,
    r"$\operatorname{ind}a^w=(2\pi)^{-n}\frac{2}{i^n n!}"
    r"\int_{\mathrm{R}^{2n}}(1-\psi)^n\operatorname{Tr}[(db\wedge da)^n]$",
    ha="center", va="center", fontsize=15.2, color="#173750",
)
ax.text(
    8.0, 1.47,
    r"For general $N>n$: $\binom{N}{n}\,n!(N-n)!/N!=1$ after the beta moment.",
    ha="center", va="center", fontsize=11.6, color="#405163",
)

arrow(14.75, 4.58, 11.8, 3.30, "substitute and simplify")
ax.text(
    8.0, 7.75,
    "Every discarded Weyl term has an exact cancellation mechanism",
    ha="center", fontsize=18, weight="bold", color="#173750",
)
ax.text(
    8.0, 7.32,
    "Scaling selects the multi-degree; alternation performs the cancellation; exterior algebra fixes the coefficient.",
    ha="center", fontsize=11.7, color="#405163",
)
ax.text(
    8.0, 0.55,
    "The argument proves equality after trace and integration. It does not identify different cutoff representatives point by point.",
    ha="center", fontsize=11.2, color="#5a4a40",
)
ax.text(
    8.0, 0.19,
    "Proof: equations (1)–(18).",
    ha="center", fontsize=10, color="#5a4a40",
)

fig.tight_layout(pad=0.5)
fig.savefig(SVG, facecolor=fig.get_facecolor())
fig.savefig(PNG, dpi=170, facecolor=fig.get_facecolor())
plt.close(fig)
print(f"{SVG}\n{PNG}")
