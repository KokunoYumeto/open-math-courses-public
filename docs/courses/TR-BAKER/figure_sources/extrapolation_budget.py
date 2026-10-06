"""Exact parameter-count illustration for Baker extrapolation.

Original figure and source: CC0. Requires numpy and matplotlib.
Run from any directory; writes ../figures/extrapolation-budget.png.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

destination = Path(__file__).resolve().parent.parent / "figures"
destination.mkdir(parents=True, exist_ok=True)
j = np.arange(257)
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6), layout="constrained")
fig.suptitle("Extrapolation: more zero locations, fewer derivatives", fontsize=15)
axes[0].plot(j, 256 + 16*j, color="#166c96", linewidth=2.6, label=r"$\log_2 R_J=256+16J$")
axes[0].plot(j, 512 - j, color="#a64b22", linewidth=2.6, label=r"$\log_2 S_J=512-J$")
axes[1].plot(j, 768 + 15*j, color="#34623f", linewidth=2.6, label=r"$\log_2(R_JS_J)=768+15J$")
for ax in axes:
    ax.set_xlim(0, 256)
    ax.set_xticks([0, 64, 128, 192, 256])
    ax.set_xlabel("Extrapolation step J", fontsize=11)
    ax.set_ylabel("Base-2 logarithm of the count", fontsize=11)
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_title(r"Exact counts for $n=2,\ h=2^{256}$", fontsize=12)
axes[1].set_title("The combined vanishing budget increases", fontsize=12)
fig.savefig(destination / "extrapolation-budget.png", dpi=180, metadata={"Software": "Matplotlib"})
plt.close(fig)
print("Created extrapolation-budget.png")

