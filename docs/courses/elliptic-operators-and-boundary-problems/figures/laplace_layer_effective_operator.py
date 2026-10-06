"""Render the Chapter 20 Laplace layer reduction with its exact normal signs."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
SVG = HERE / "laplace_layer_effective_operator.svg"
PNG = HERE / "laplace_layer_effective_operator.png"


fig, ax = plt.subplots(figsize=(15.5, 8.4))
fig.patch.set_facecolor("#fffdf8")
ax.set_facecolor("#fffdf8")
ax.set_xlim(0, 15.5)
ax.set_ylim(0, 8.4)
ax.axis("off")


def arrow(x0, y0, x1, y1, color="#536b78", width=1.8, label=None, offset=0.18):
    patch = FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=17,
        linewidth=width, color=color,
    )
    ax.add_patch(patch)
    if label:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + offset, label,
                ha="center", va="bottom", fontsize=10.5, color=color)
    return patch


def box(x, y, w, h, text, face="#eef5f7", edge="#608397", size=12.5, weight=None):
    patch = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.13,rounding_size=0.13",
        facecolor=face, edgecolor=edge, linewidth=1.8,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=size, color="#18384b", weight=weight, linespacing=1.35)
    return patch


ax.text(7.75, 8.00, "A harmonic boundary problem becomes one boundary operator",
        ha="center", va="center", fontsize=19, weight="bold", color="#173750")
ax.text(7.75, 7.55,
        "The normal convention fixes the signs; exterior uniqueness makes the single layer invertible when n > 2.",
        ha="center", va="center", fontsize=11.5, color="#405163")

# Geometry and jump mechanism.
domain = Ellipse((3.25, 4.10), 5.25, 3.45,
                 facecolor="#eaf4ed", edgecolor="#4f8165", linewidth=2.4)
ax.add_patch(domain)
ax.text(3.25, 4.10, r"$X$", ha="center", va="center",
        fontsize=21, weight="bold", color="#35644d")
ax.text(3.25, 6.05, r"$Y=\partial X$", ha="center", va="bottom",
        fontsize=12.5, color="#35644d")
ax.text(0.55, 5.65, "exterior", ha="left", va="center",
        fontsize=11.5, color="#6a7880")

px, py = 3.25, 5.825
ax.plot([px], [py], "o", color="#9a543f", markersize=6)
arrow(px - 0.12, py + 0.08, px - 0.12, py + 1.08,
      color="#9a543f", label=r"$\nu$", offset=0.05)
arrow(px + 0.18, py - 0.03, px + 0.18, py - 1.02,
      color="#315f78", label=r"$n=-\nu$", offset=-0.05)

ax.plot([2.15, 4.35], [4.75, 4.55], "o", color="#ac7255", markersize=5)
ax.plot([3.28], [3.45], "o", color="#315f78", markersize=7)
arrow(2.18, 4.72, 3.18, 3.53, color="#81929a", width=1.2)
arrow(4.32, 4.52, 3.38, 3.53, color="#81929a", width=1.2)
ax.text(3.38, 3.22, r"$u=D_+u_0-S_+u_1$", ha="center", va="top",
        fontsize=12.3, color="#18384b")

box(0.55, 0.82, 5.40, 1.50,
    r"$\gamma^-S_-=\gamma^+S_-=V$" + "\n" +
    r"$\gamma_1^+S_- - \gamma_1^-S_-=I$" + "\n" +
    r"$V\sigma=0\;\Longrightarrow\;S_-\sigma=0\;\Longrightarrow\;\sigma=0$",
    face="#f8f1e8", edge="#9b7a55", size=11.8)
ax.text(3.25, 0.43, r"$n>2$: the exterior layer is $O(|x|^{2-n})$.",
        ha="center", va="center", fontsize=10.8, color="#6c5745")

# Exact boundary reduction.
ax.plot([6.55, 6.55], [0.62, 6.92], color="#ccd5d8", linewidth=1.5)
ax.text(10.95, 6.88, r"$(I-k_0)u_0-k_1u_1=0$",
        ha="center", va="center", fontsize=16.0, weight="bold", color="#173750")

box(7.05, 5.00, 1.55, 0.92, r"$u_0$", face="#edf4f8", edge="#5f8298", size=15)
box(9.05, 5.00, 2.10, 0.92, r"$I-k_0$", face="#eff6ec", edge="#6f8b64", size=14)
box(11.62, 5.00, 1.85, 0.92, r"$k_1^{-1}$", face="#fff3e8", edge="#a7784f", size=14)
box(13.88, 5.00, 1.20, 0.92, r"$u_1$", face="#f4eff8", edge="#826d96", size=15)
arrow(8.62, 5.46, 9.02, 5.46)
arrow(11.18, 5.46, 11.59, 5.46)
arrow(13.50, 5.46, 13.85, 5.46)

box(7.50, 3.18, 3.22, 0.98, r"$b_0u_0$", face="#eef5f7", edge="#608397", size=14)
box(11.62, 3.18, 3.22, 0.98, r"$b_1u_1$", face="#f6f0f8", edge="#826d96", size=14)
arrow(7.82, 4.98, 8.72, 4.18, color="#5f8298")
arrow(14.48, 4.98, 13.70, 4.18, color="#826d96")

box(8.45, 1.70, 5.45, 1.00,
    r"$[b_0+b_1k_1^{-1}(I-k_0)]u_0=f$",
    face="#e8f2f7", edge="#315f78", size=14.5, weight="bold")
arrow(9.22, 3.15, 10.25, 2.73, color="#536b78")
arrow(13.25, 3.15, 12.43, 2.73, color="#536b78")

ax.text(10.98, 1.23,
        r"$k_1=V$,  $\sigma_{-1}(k_1)=-1/(2|\eta|)$,  "
        r"$k_1^{-1}(I-k_0)=A_{\rm in}$",
        ha="center", va="center", fontsize=12.0, color="#405163")
ax.text(10.98, 0.70,
        r"$\sigma_1(A_{\rm in})=-|\eta|$: exactly the inward derivative of $e^{-t|\eta|}$ at $t=0$.",
        ha="center", va="center", fontsize=11.2, color="#5a4a40")

fig.tight_layout(pad=0.4)
fig.savefig(SVG, facecolor=fig.get_facecolor())
fig.savefig(PNG, dpi=180, facecolor=fig.get_facecolor())
plt.close(fig)
print(f"{SVG}\n{PNG}")
