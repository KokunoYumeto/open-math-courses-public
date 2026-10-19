"""Exact geometric examples for Tangent support and analytic directions.

Original figure: GPT-6 Astra (OpenAI), 2026. CC0.
Exercises 2 and 3 and Proposition 10 give the mathematical arguments.
Run with Python, NumPy and Matplotlib; outputs are saved beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "svg.fonttype": "none"})
fig, axs = plt.subplots(3, 1, figsize=(8, 12), constrained_layout=True)
blue, red, gray = "#1768a5", "#b33a3a", "#536273"

ax = axs[0]
s = np.linspace(-1.2, 1.2, 401)
ax.plot(s, s*s, color=blue, lw=2.5, label=r"$S=\{(s,s^2)\}$")
ax.annotate("", xy=(1.25, 0), xytext=(-1.25, 0),
            arrowprops={"arrowstyle": "<->", "lw": 2, "color": red})
ax.scatter([0], [0], color="black", zorder=4)
ax.text(.32, .13, r"$T_0S=\mathbb{R}(1,0)$", color=red)
ax.set(xlim=(-1.4, 1.4), ylim=(-.3, 1.6), xlabel=r"$x_1$", ylabel=r"$x_2$",
       title="Physical tangent cone — both horizontal directions")
ax.legend(loc="upper center")

ax = axs[1]
ax.axvspan(0, 1.2, color=blue, alpha=.12)
ax.axvline(0, color=gray, ls="--", lw=1.5)
ax.scatter([0], [0], s=55, color=blue, zorder=4)
ax.scatter([0], [1], s=90, facecolors="white", edgecolors=red, lw=2, zorder=5)
j = np.arange(1, 9)
ax.scatter(1/j, np.ones(len(j)), color=blue, s=24, zorder=4)
ax.annotate(r"$(1/j,1)$; lift has $c=j$", xy=(.5, 1), xytext=(.22, 1.48),
            arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
ax.annotate(r"$(0,1)\notin\pi(C)$", xy=(0, 1), xytext=(-.48, .43),
            arrowprops={"arrowstyle": "->", "color": red}, color=red)
ax.text(.4, -.55, r"$a>0$: every $b$ occurs", color=blue)
ax.set(xlim=(-.55, 1.15), ylim=(-.8, 1.8), xlabel=r"$a$", ylabel=r"$b$",
       title="Projection of a closed cone — closure adds the vertical axis")

ax = axs[2]
for j in range(1, 9):
    ax.hlines(1/j, -1, 1, color=blue, lw=1.8)
    if j <= 4:
        ax.text(1.05, 1/j, r"$j="+str(j)+"$", va="center", color=blue)
ax.hlines(0, -1.15, 1.15, color=red, lw=2.5)
ax.text(-1.12, -.15, r"$x_4=0$: smooth traces; ambient singularities", color=red)
ax.text(-.95, .68, r"$L_j:\ x_4=1/j,\ x_2=x_3=0$", color=blue)
ax.set(xlim=(-1.3, 1.5), ylim=(-.23, 1.13), xlabel=r"$x_1$", ylabel=r"$x_4$",
       title="Smooth-data counterexample — first eight positive singular lines")
for ax in axs:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=.15)
fig.savefig(out/"tangent-cones-and-boundary-lines.svg")
svg = out/"tangent-cones-and-boundary-lines.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n", encoding="utf-8")
fig.savefig(out/"tangent-cones-and-boundary-lines.png", dpi=170)
plt.close(fig)
