"""Reproduce the exact square and n=3 rectangular cut geometry in M2–M4."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).with_name("marked-surface-cut-models.png")
fig, axes = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"width_ratios": [1, 2.15]})
ink, cut, fill = "#16304d", "#b03834", "#eaf1f7"

def arrow(ax, start, end, color=ink, width=1.8, scale=16):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=scale,
                                color=color, linewidth=width))

ax = axes[0]
ax.add_patch(Rectangle((0, 0), 1, 1, facecolor=fill, edgecolor=ink, linewidth=2))
arrow(ax, (.14, 0), (.78, 0))
arrow(ax, (1, .14), (1, .78))
arrow(ax, (.86, 1), (.22, 1))
arrow(ax, (0, .86), (0, .22))
ax.text(.5, -.14, r"$A$", ha="center", fontsize=17)
ax.text(1.13, .5, r"$B$", va="center", fontsize=17)
ax.text(.5, 1.13, r"$A^{-1}$", ha="center", fontsize=17)
ax.text(-.18, .5, r"$B^{-1}$", va="center", ha="center", fontsize=17)
ax.plot(0, 0, "o", color=ink)
ax.text(.5, .57, "opposite sides\nidentified by translations", ha="center", va="center", fontsize=12)
ax.text(.5, .30, r"$ABA^{-1}B^{-1}$", ha="center", fontsize=17)
ax.set_title("M2: positive square boundary", fontsize=16, pad=16)
ax.set_xlim(-.32, 1.34); ax.set_ylim(-.34, 1.34)
ax.set_aspect("equal"); ax.axis("off")

ax = axes[1]
ax.add_patch(Rectangle((0, 0), 7, 4, facecolor=fill, edgecolor=ink, linewidth=2))
for s in range(1, 4):
    left, mid = 2*s-1, 2*s-.5
    ax.add_patch(Rectangle((left, 2), 1, 1, facecolor="white", edgecolor=ink, linewidth=2))
    ax.plot([mid, mid], [0, 2], "--", color=cut, linewidth=2)
    ax.text(mid+.12, 1.12, rf"$v_{s}$", color=cut, fontsize=15)
    ax.text(mid, 2.45, rf"$D_{s}$", ha="center", fontsize=16)
    arrow(ax, (left+.68, 2), (left+.14, 2))
    arrow(ax, (left, 2.2), (left, 2.8))
    arrow(ax, (left+.2, 3), (left+.8, 3))
    arrow(ax, (left+1, 2.8), (left+1, 2.2))
    ax.text(mid, 3.18, rf"clockwise $C_{s}$", ha="center", fontsize=12)
    ax.text(mid, -.22, f"{mid:g}", ha="center", fontsize=11)
ax.plot(0, 0, "o", color=ink)
ax.text(-.16, -.25, "root", ha="right", fontsize=12)
arrow(ax, (.2, 0), (1.15, 0))
arrow(ax, (7, .35), (7, 1.35))
arrow(ax, (6.5, 4), (5.4, 4))
arrow(ax, (0, 3.5), (0, 2.6))
ax.text(3.5, 4.18, r"positive outer word $W_g$", ha="center", fontsize=15)
ax.text(3.5, -.64, r"$C_1 C_2 C_3 W_g = 1$  (cut disk boundary)", ha="center", fontsize=17)
ax.text(7.12, 4, "4", va="center", fontsize=11)
ax.text(7.12, 3, "3", va="center", fontsize=11)
ax.text(7.12, 2, "2", va="center", fontsize=11)
ax.text(7.12, 0, "0", va="center", fontsize=11)
ax.set_title("M5–M8: exact puncture cuts, n = 3", fontsize=16, pad=16)
ax.set_xlim(-.6, 7.7); ax.set_ylim(-.85, 4.8)
ax.set_aspect("equal"); ax.axis("off")

fig.text(.5, .02, "Dashed cuts are opened into separate banks. Connectors follow the lower outer side, then the cut upwards.",
         ha="center", fontsize=12, color=ink)
fig.tight_layout(rect=[0, .06, 1, 1])
fig.savefig(OUT, dpi=160, facecolor="white", bbox_inches="tight", metadata={"Software": None})
plt.close(fig)
print(OUT)
