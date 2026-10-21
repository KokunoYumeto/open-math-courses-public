"""Exact unit-circle double-cover illustration for Example 22.46."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
blue, orange, ink = "#1768ac", "#d26927", "#243447"
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8), constrained_layout=True)
theta = np.linspace(0, 2*np.pi, 801)
for ax in axes:
    ax.axhline(0, color="#cdd5df", lw=.7)
    ax.axvline(0, color="#cdd5df", lw=.7)
    ax.set(xlim=(-1.5, 1.65), ylim=(-1.45, 1.45), aspect="equal")
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("Real part"); ax.set_ylabel("Imaginary part")
axes[0].plot(np.cos(theta), np.sin(theta), color=ink, lw=2)
axes[0].scatter([1], [0], color=ink, s=34, zorder=4)
axes[0].annotate(r"$t=1$", (1, 0), (1.08, -.24), fontsize=12)
axes[0].annotate("", xy=(0, 1), xytext=(.23, .973),
                 arrowprops=dict(arrowstyle="->", color=ink, lw=1.8))
axes[0].set_title(r"Base: $t(s)=e^{is}$", fontsize=14)
axes[0].text(0, -.36, "Each circuit follows\nthis same unit circle.",
             ha="center", va="center", color=ink, fontsize=10)

first = np.linspace(0, np.pi, 401)
second = np.linspace(np.pi, 2*np.pi, 401)
axes[1].plot(np.cos(first), np.sin(first), color=blue, lw=3,
             label=r"First base circuit: $0\leq s\leq2\pi$")
axes[1].plot(np.cos(second), np.sin(second), color=orange, lw=3,
             label=r"Second circuit: $2\pi\leq s\leq4\pi$")
axes[1].scatter([1, -1], [0, 0], c=[ink, blue], s=34, zorder=4)
axes[1].annotate(r"$z=1$", (1, 0), (1.08, -.24), fontsize=12)
axes[1].annotate(r"$z=-1$", (-1, 0), (-1.46, -.26), fontsize=12)
axes[1].annotate("", xy=(0, 1), xytext=(.23, .973),
                 arrowprops=dict(arrowstyle="->", color=blue, lw=2))
axes[1].annotate("", xy=(0, -1), xytext=(-.23, -.973),
                 arrowprops=dict(arrowstyle="->", color=orange, lw=2))
axes[1].text(0, .12, r"Projection: $t=z^2$", ha="center", fontsize=12, color=ink)
axes[1].text(0, -.18, "One circuit exchanges the roots.", ha="center", fontsize=9, color=ink)
axes[1].set_title(r"Lift: $z(s)=e^{is/2}$", fontsize=14)
fig.legend(*axes[1].get_legend_handles_labels(), loc="outside lower center",
           ncol=2, frameon=False, fontsize=10)
fig.suptitle("Two roots, one connected covering space", fontsize=16)
fig.savefig(root/"algebraic-cover-connectedness.png", dpi=175)
plt.close(fig)
