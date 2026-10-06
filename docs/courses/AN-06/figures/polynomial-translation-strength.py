"""Plot exact derivative-strength geometry. Original source: CC0.

Requires Matplotlib 3.11.2 and NumPy 2.5.3. Reproduce the sibling SVG and PNG.
The reader displays the explicitly bound PNG and links the full-size SVG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "svg.hashsalt": "polynomial-translation-strength",
    "axes.spines.top": False,
    "axes.spines.right": False,
})
target = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(8.8, 5.8), layout="constrained")
b = np.linspace(-1, 1, 1601)
delta = 2 * np.sqrt(np.maximum(0, 1-b*b))
left, right = b*b-delta, b*b+delta
ax.fill_betweenx(b, left, right, color="#b7d8e9",
                 label=r"$\widetilde p(a,b)\leq 3$")
ax.plot(left, b, color="#216184", lw=1.6)
ax.plot(right, b, color="#216184", lw=1.6)
wide_b = np.linspace(-2.65, 2.65, 1601)
ax.plot(wide_b*wide_b, wide_b, color="#ad5025", lw=2,
        label=r"$p(a,b)=0$: $a=b^2$")
ax.add_patch(Rectangle((-2, -1), 4, 2, fill=False, lw=1.2,
                       ls="--", edgecolor="#566675",
                       label=r"proved enclosure $[-2,2]\times[-1,1]$"))
ax.scatter([4], [2], color="#ad5025", s=44, zorder=5)
ax.annotate(r"$(4,2)$"+"\n"+r"$p=0,\quad\widetilde p=\sqrt{21}$",
            xy=(4, 2), xytext=(1.1, 2.25),
            arrowprops={"arrowstyle": "->", "color": "#566675"},
            fontsize=12, ha="left")
ax.axhline(0, color="#aab5be", lw=.7, zorder=0)
ax.axvline(0, color="#aab5be", lw=.7, zorder=0)
ax.set(xlim=(-2.7, 7.3), ylim=(-2.8, 2.9),
       xlabel=r"frequency centre $a$", ylabel=r"frequency centre $b$",
       title=r"$p(\xi)=\xi_1-\xi_2^2$: a value does not measure every coefficient")
ax.set_aspect("equal", adjustable="box")
ax.grid(alpha=.18)
ax.legend(loc="lower right", fontsize=10, framealpha=.97)
fig.savefig(target/"polynomial-translation-strength.svg",
            metadata={"Date": None, "Creator": "Original CC0 mathematical figure"})
fig.savefig(target/"polynomial-translation-strength.png", dpi=180,
            metadata={"Software": "Original CC0 mathematical figure"})
plt.close(fig)
