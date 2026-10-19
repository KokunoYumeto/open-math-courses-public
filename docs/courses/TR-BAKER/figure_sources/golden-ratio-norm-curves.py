"""Norm-curve picture for Proposition 12.7. Original figure, CC0.
OpenAI Codex — GPT-6 Astra, Ultra.
The curves are numerical renderings; all six points have exact labels.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

phi = (1+math.sqrt(5))/2
fig, ax = plt.subplots(figsize=(7.5, 6.3))
blue, orange = "#176ca3", "#a65013"
lo, hi = -2.15, 3.15
for sign, style in [(1, "-"), (-1, "--")]:
    for j, (left, right) in enumerate([(lo, -.02), (.02, hi)]):
        x = np.linspace(left, right, 1000)
        ax.plot(x, sign/x, color=blue, ls=style, lw=1.8,
                label=rf"$XY={sign}$" if j == 0 else None)
    for j, (left, right) in enumerate([(lo, .98), (1.02, hi)]):
        x = np.linspace(left, right, 1000)
        ax.plot(x, 1-sign/(1-x), color=orange, ls=style, lw=1.8,
                label=rf"$(1-X)(1-Y)={sign}$" if j == 0 else None)
points = [
    (phi, -1/phi, r"$\varphi$", (10, 10)),
    (-1/phi, phi, r"$-\varphi^{-1}$", (-57, 10)),
    (phi**2, phi**-2, r"$\varphi^2$", (10, 10)),
    (phi**-2, phi**2, r"$\varphi^{-2}$", (10, 8)),
    (1/phi, -phi, r"$\varphi^{-1}$", (10, -12)),
    (-phi, 1/phi, r"$-\varphi$", (10, 10)),
]
for x, y, label, offset in points:
    assert min(abs(x*y-1), abs(x*y+1)) < 1e-12
    assert min(abs((1-x)*(1-y)-1), abs((1-x)*(1-y)+1)) < 1e-12
    ax.scatter([x], [y], s=48, color="#162b39", zorder=5)
    ax.annotate(label, (x, y), xytext=offset, textcoords="offset points",
                fontsize=13, color="#162b39",
                bbox={"facecolor":"white", "edgecolor":"none", "alpha":.9, "pad":1.1})
ax.axhline(0, color="#adbac1", lw=.7, zorder=0)
ax.axvline(0, color="#adbac1", lw=.7, zorder=0)
ax.set(xlim=(lo, hi), ylim=(lo, hi),
       xlabel=r"$X=\sigma_1(x)$", ylabel=r"$Y=\sigma_2(x)$",
       title="Six units for which 1 − x is also a unit")
ax.set_aspect("equal")
ax.grid(alpha=.14)
ax.legend(loc="upper left", fontsize=10, framealpha=.95)
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/golden-ratio-norm-curves.png", dpi=160, facecolor="white")
plt.close(fig)
