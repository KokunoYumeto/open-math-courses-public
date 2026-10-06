"""Reproduce Figure 1 in 'Paths control supported distributions'.

Original plot: GPT-6.1 Sol (OpenAI), Ultra reasoning effort, 2026.
CC0-1.0. Requires Python, numpy and matplotlib. No TeX installation.
The curve is c(t)=(t**2,t**3), -1<=t<=1.
Marked points correspond exactly to t=+/-1/2.
Proof: Proposition 5.1 and Theorem 4.1 in the accompanying lesson.
Metric terminology: Juha Heinonen, Lectures on Lipschitz Analysis (2005).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "text.usetex": False, "axes.spines.top": False,
    "axes.spines.right": False, "savefig.facecolor": "#faf9f5",
})
fig, ax = plt.subplots(figsize=(6.5, 5.7), facecolor="#faf9f5")
ax.set_facecolor("#faf9f5")
t = np.linspace(-1, 1, 1601)
ax.plot(t**2, t**3, color="#bac8c7", linewidth=3, zorder=1)
t_short = np.linspace(-0.5, 0.5, 801)
ax.plot(t_short**2, t_short**3, color="#12606b", linewidth=4, zorder=3)
ax.plot([0.25, 0.25], [-0.125, 0.125],
        color="#b15b30", linewidth=2.3, linestyle="--", zorder=2)
ax.scatter([0, 0.25, 0.25], [0, -0.125, 0.125],
           color="#153f43", s=52, zorder=4)
ax.annotate(r"$P_+=(1/4,\,1/8)$", xy=(0.25, 0.125),
            xytext=(0.29, 0.24), arrowprops={"arrowstyle": "-", "color": "#59646a"})
ax.annotate(r"$P_-=(1/4,\,-1/8)$", xy=(0.25, -0.125),
            xytext=(0.29, -0.27), arrowprops={"arrowstyle": "-", "color": "#59646a"})
ax.annotate("Every joining path\npasses through zero", xy=(0, 0),
            xytext=(0.34, -0.13), fontsize=12,
            arrowprops={"arrowstyle": "->", "color": "#153f43"})
ax.annotate("Chord\nlength = 1/4", xy=(0.25, 0.015),
            xytext=(0.35, 0.03), fontsize=12, color="#9b4b24",
            arrowprops={"arrowstyle": "-", "color": "#b15b30"})
ax.annotate("Subarc in the cusp", xy=(0.075, 0.075**1.5),
            xytext=(0.015, 0.19), fontsize=12, color="#12606b",
            arrowprops={"arrowstyle": "->", "color": "#12606b"})
ax.set(xlim=(-0.04, 0.69), ylim=(-0.32, 0.32),
       xlabel=r"$x=t^2$", ylabel=r"$y=t^3$")
ax.set_aspect("equal", adjustable="box")
ax.grid(alpha=0.18, color="#59646a")
ax.set_title("A cusp forces a detour", fontsize=20, color="#153f43", pad=16)
fig.text(0.5, 0.04,
         "Every joining path has length at least 1/2.\n"
         "Length / chord is at least 1/t as t tends to zero.",
         ha="center", fontsize=12, color="#173b3e")
fig.subplots_adjust(bottom=0.23, top=0.85, left=0.15, right=0.97)
fig.savefig(Path(__file__).with_suffix(".png"), dpi=160,
            metadata={"Title": "Cusp detour", "Description":
                      "Exact curve (t^2,t^3); Proposition 5.1. Original CC0 plot."})
plt.close(fig)
