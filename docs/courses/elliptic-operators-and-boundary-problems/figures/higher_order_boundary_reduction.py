from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
PNG = HERE / "higher_order_boundary_reduction.png"
SVG = HERE / "higher_order_boundary_reduction.svg"

navy = "#17324d"
blue = "#1976b9"
blue_light = "#dbeefa"
amber = "#d88913"
amber_light = "#fff0cf"
green = "#198754"
green_light = "#dff3e8"
ink = "#17212b"
muted = "#596773"
edge = "#93a4b1"

fig, ax = plt.subplots(figsize=(19, 7.5), dpi=200)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0, 19)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(
    9.5,
    9.55,
    "Arbitrary order to a closed first-order index",
    ha="center",
    va="center",
    fontsize=24,
    color=navy,
    fontweight="bold",
)
ax.text(
    9.5,
    9.08,
    "The blue stable data are carried unchanged; every amber auxiliary factor has index zero.",
    ha="center",
    va="center",
    fontsize=12.5,
    color=muted,
)

xs = [0.45, 4.18, 7.91, 11.64, 15.37]
width = 3.18
height = 5.5
titles = [
    "Original problem",
    "Zero-index\nstabilization",
    "Cayley block path",
    "Common factor\nand cancellation",
    "First order,\nsplit, double",
]
subtitles = [
    r"$(P,\mathbf{B})_s$" + "\n" + r"order $m$",
    r"$\mathrm{diag}(P,Q^m,\ldots,Q^m)$" + "\n" + r"$\mathrm{ind}\,Q=0$",
    r"$\mathcal{P}_\tau$" + "\n" + r"$\mathcal{M}^+(p_\tau)\cong\mathcal{M}^+(p)$",
    r"$D_*Q^{m-1},\ \beta Q^{m-1}$" + "\n" + "right factor retained",
    r"$(D_{\mathrm{sp}},B_{\mathrm{sp}})$" + "\n" + r"$\widehat D_{\mathrm{sp}}$ on the double",
]
fills = ["#f5f8fb", amber_light, "#eef5fb", amber_light, green_light]

for x, title, subtitle, fill in zip(xs, titles, subtitles, fills):
    box = FancyBboxPatch(
        (x, 2.08),
        width,
        height,
        boxstyle="round,pad=0.025,rounding_size=0.12",
        linewidth=1.5,
        edgecolor=edge,
        facecolor=fill,
    )
    ax.add_patch(box)
    ax.text(
        x + width / 2,
        7.18,
        title,
        ha="center",
        va="center",
        fontsize=12.4,
        color=navy,
        fontweight="bold",
    )
    ax.text(
        x + width / 2,
        6.5,
        subtitle,
        ha="center",
        va="top",
        fontsize=12,
        color=ink,
        linespacing=1.45,
    )

for left in range(4):
    start = xs[left] + width + 0.08
    end = xs[left + 1] - 0.08
    arrow = FancyArrowPatch(
        (start, 4.82),
        (end, 4.82),
        arrowstyle="-|>",
        mutation_scale=16,
        linewidth=1.7,
        color=navy,
    )
    ax.add_patch(arrow)

arrow_labels = [
    "add $m-1$ blocks",
    "(AR33)–(AR45)",
    "(AR50)–(AR57)",
    "stable reduction",
]
for left, label in enumerate(arrow_labels):
    ax.text(
        (xs[left] + width + xs[left + 1]) / 2,
        5.12,
        label,
        ha="center",
        va="bottom",
        fontsize=9.8,
        color=muted,
    )

# Stable Cauchy strand.
stable_y = 3.52
for x in xs:
    ax.plot([x + 0.35, x + width - 0.35], [stable_y, stable_y], color=blue, lw=5.2, solid_capstyle="round")
for left in range(4):
    ax.plot(
        [xs[left] + width - 0.35, xs[left + 1] + 0.35],
        [stable_y, stable_y],
        color=blue,
        lw=2.4,
    )
ax.text(0.78, 3.83, r"stable bundle $\mathcal{M}^+(p)$", fontsize=10.6, color=blue, fontweight="bold")
ax.text(8.28, 3.83, r"$U\mapsto U_0$", fontsize=10.6, color=blue, fontweight="bold")
ax.text(15.75, 3.83, "same index", fontsize=10.6, color=green, fontweight="bold")

# Auxiliary growing modes are added and later cancelled.
aux_ys = [2.75, 2.47, 2.19]
for y in aux_ys:
    ax.plot([xs[1] + 0.42, xs[3] + width - 0.5], [y, y], color=amber, lw=2.8, alpha=0.9)
    ax.plot([xs[3] + width - 0.5, xs[3] + width - 0.14], [y, 3.03], color=amber, lw=2.1, alpha=0.85)
ax.text(4.58, 3.02, r"growing $L^m$ modes", fontsize=9.8, color=amber, fontweight="bold")
ax.text(12.1, 3.02, r"cancel $Q^{m-1}$", fontsize=9.8, color=amber, fontweight="bold")

# Factor diagram inside the cancellation box.
cx = xs[3] + width / 2
ax.text(cx, 4.28, r"$\widehat{\mathcal{P}}_1=D_*L^{m-1}$", ha="center", fontsize=12.2, color=ink)
ax.text(cx, 3.82, r"$\mathcal{B}^1=\beta L^{m-1}$", ha="center", fontsize=12.2, color=ink)

# Final equality banner.
banner = FancyBboxPatch(
    (2.4, 0.46),
    14.2,
    0.95,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    linewidth=1.5,
    edgecolor=green,
    facecolor="#f1fbf5",
)
ax.add_patch(banner)
ax.text(
    9.5,
    0.94,
    r"$\mathrm{ind}(P,\mathbf{B})=\mathrm{ind}(D_*,\beta)="
    r"\mathrm{ind}\,\widehat D_{\mathrm{sp}}=\mathrm{sind}(\widehat d_{\mathrm{sp}})$",
    ha="center",
    va="center",
    fontsize=16.2,
    color=green,
    fontweight="bold",
)

ax.text(
    18.72,
    0.2,
    "Exact maps: (AR20)–(AR61)",
    ha="right",
    va="bottom",
    fontsize=8.8,
    color=muted,
)

fig.savefig(PNG, bbox_inches="tight", facecolor="white")
fig.savefig(SVG, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(PNG)
print(SVG)
