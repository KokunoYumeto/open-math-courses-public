"""Render the exact multiplier levels and ordinary-scale defect in AH1/AH8."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
SVG = HERE / "adapted_hypoelliptic_family.svg"
PNG = HERE / "adapted_hypoelliptic_family.png"

k = np.linspace(-5, 5, 801)
ell = np.linspace(-3, 3, 801)
K, L = np.meshgrid(k, ell)
P = 1 + K**2 + L**4
levels = [2, 5, 17, 65, 257]

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 6.4))
fig.patch.set_facecolor("#fffdf8")
for ax in (ax0, ax1):
    ax.set_facecolor("#fffdf8")

contours = ax0.contour(K, L, P, levels=levels, colors="#24577a", linewidths=1.7)
ax0.clabel(contours, inline=True, fmt=lambda value: f"p={int(value)}", fontsize=9)
ax0.axhline(0, color="#8c5b37", lw=1.0, alpha=0.8)
ax0.axvline(0, color="#5a725a", lw=1.0, alpha=0.8)
ax0.annotate(
    r"$p(k,0)=1+k^2$", xy=(4.2, 0), xytext=(2.5, 1.7),
    arrowprops={"arrowstyle": "->", "color": "#8c5b37"},
    color="#6e4024", fontsize=12,
)
ax0.annotate(
    r"$p(0,\ell)=1+\ell^4$", xy=(0, 2.4), xytext=(-4.7, 2.45),
    arrowprops={"arrowstyle": "->", "color": "#5a725a"},
    color="#3f6241", fontsize=12,
)
ax0.set_xlabel(r"$k$")
ax0.set_ylabel(r"$\ell$")
ax0.set_title(r"Exact levels of $p(k,\ell)=1+k^2+\ell^4$")
ax0.set_aspect("equal", adjustable="box")

N = np.arange(1, 129, dtype=float)
residual = 1 / (1 + N**2)
ax1.loglog(N, residual, color="#24577a", lw=2.2, label=r"$1/(1+N^2)$")
ax1.loglog(N, N**-2, "--", color="#8c5b37", lw=1.5, label=r"$N^{-2}$")
points = np.array([1, 2, 4, 8, 16, 32, 64, 128], dtype=float)
ax1.scatter(points, 1 / (1 + points**2), s=25, color="#24577a", zorder=3)
ax1.set_xlabel(r"$N$")
ax1.set_ylabel(r"$\|Pu_N\|_{H^\sigma}$")
ax1.set_title("Normalized ordinary-order-four sequence")
ax1.grid(True, which="both", color="#d7d3ca", lw=0.7)
ax1.legend(frameon=False, loc="upper right")
ax1.text(
    0.04, 0.08,
    r"$\|u_N\|_{H^{\sigma+4}}=1$" + "\n" +
    r"$\|Pu_N\|_{H^\sigma}\to0$",
    transform=ax1.transAxes, fontsize=12,
    bbox={"boxstyle": "round,pad=0.4", "facecolor": "#edf4f8", "edgecolor": "#7890a3"},
)

fig.suptitle("One operator, two exact growth orders and two different Fredholm outcomes",
             fontsize=17, color="#173750")
fig.text(
    0.5, 0.015,
    "The adapted multiplier norm retains both axes; the isotropic order-four domain overweights the k-axis.",
    ha="center", fontsize=11, color="#405163",
)
fig.tight_layout(rect=(0, 0.05, 1, 0.93))
fig.savefig(SVG, facecolor=fig.get_facecolor())
fig.savefig(PNG, dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
print(f"{SVG}\n{PNG}")
