"""Reproduce an exact circle model of a frozen holomorphic denominator."""
from pathlib import Path
import json
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "svg.fonttype": "none", "svg.hashsalt": "frozen-holomorphic-denominator"})
fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), constrained_layout=True)
theta = np.linspace(0, 2*np.pi, 721)
ax = axes[0]
ax.plot(np.cos(theta), np.sin(theta), color="#185a80", lw=2.4)
ax.add_patch(Circle((.25, 0), .25, facecolor="#e8b061", edgecolor="#975500", alpha=.55))
ax.plot([.25], [0], "o", color="#6b3500", ms=5)
ax.axhline(0, color="#aaa", lw=.7)
ax.axvline(0, color="#aaa", lw=.7)
ax.annotate(r"every root $1/4-\lambda$", xy=(.37, .13), xytext=(.14, .64),
            arrowprops={"arrowstyle": "->", "color": "#714100"}, ha="center")
ax.annotate(r"fixed circle $|z|=1$", xy=(-.72, .69), xytext=(-.95, 1.18),
            arrowprops={"arrowstyle": "->", "color": "#185a80"})
ax.plot([.5, 1], [0, 0], color="#136c50", lw=3)
ax.text(.75, -.16, r"gap $\geq 1/2$", ha="center", color="#136c50")
ax.set(xlim=(-1.4, 1.4), ylim=(-1.35, 1.45), aspect="equal", xlabel=r"$\operatorname{Re}z$", ylabel=r"$\operatorname{Im}z$")
ax.set_title("One fixed averaging circle")
ax = axes[1]
N = np.arange(0, 9)
tail = 2.0 * 3.0**(-N-1)
ax.semilogy(N, tail, "o-", color="#185a80", lw=2)
ax.set_xticks(N)
ax.grid(axis="y", alpha=.3)
ax.set(xlabel="degree N of the inverse series", ylabel="uniform upper bound for the remainder")
ax.set_title(r"$|\lambda|\leq 1/4$: ratio $\leq 1/3$")
ax.text(.5, .83, r"$\left|\frac{1}{z-1/4+\lambda}-"
        r"\sum_{k=0}^{N}\frac{(-\lambda)^k}{(z-1/4)^{k+1}}\right|$"
        "\n" r"$\leq\,2\cdot 3^{-(N+1)}$", transform=ax.transAxes,
        ha="center", va="center", bbox={"facecolor": "white", "edgecolor": "#ccc", "pad": 9})
fig.savefig(OUT / "frozen-averaging-circle.png", dpi=180)
fig.savefig(OUT / "frozen-averaging-circle.svg", metadata={"Date": None})
svg = OUT / "frozen-averaging-circle.svg"
svg.write_bytes(b"\n".join(line.rstrip(b" \t\r") for line in svg.read_bytes().split(b"\n")))
plt.close(fig)
print(json.dumps({"status": "RENDERED", "outputs": [str(OUT / ("frozen-averaging-circle." + ext)) for ext in ["png", "svg"]]}))
