"""Render the exact constant-metric example in W43--W44. CC0 1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.fonttype": "path"})
fig, axes = plt.subplots(1, 2, figsize=(11.2, 6.4))
theta = np.linspace(0, 2*np.pi, 1001)
colors = ["#176e9a", "#b85a1d"]
for ax, radii, title, extent, labels in [
    (axes[0], [1/4, 4/5], "Input metric balls on one phase-space plane", 1,
     [r"$g_1=16Q$; radius $1/4$", r"$g_2=(25/16)Q$; radius $4/5$"]),
    (axes[1], [4, 5/4], "Symplectic dual balls on the same plane", 4.7,
     [r"$q_1=Q/16$; radius $4$", r"$q_2=(16/25)Q$; radius $5/4$"])
]:
    for radius, color, label in zip(radii, colors, labels):
        ax.plot(radius*np.cos(theta), radius*np.sin(theta), color=color, lw=2.3, label=label)
    ax.axhline(0, color="#9b9b9b", lw=.6)
    ax.axvline(0, color="#9b9b9b", lw=.6)
    ax.set(xlim=(-extent, extent), ylim=(-extent, extent), xlabel=r"$x$", ylabel=r"$\xi$", title=title)
    ax.set_aspect("equal")
    ax.legend(loc="lower center", bbox_to_anchor=(.5, -.29), frameon=False)
fig.suptitle("A finite cross parameter permits the original metrics", fontsize=17, y=.98)
fig.text(.5, .085, r"$Q=dx^2+d\xi^2$,  $H=5$,  $h_1=16$,  $h_2=25/16$,  $h_g=281/32$,  $h_{G,\mathcal{A}}=5/4$",
         ha="center", fontsize=12)
fig.text(.5, .042, "The product metric G acts in four dimensions; these circles are its two input slices.  Proof: W43–W44 and G24–G26.",
         ha="center", fontsize=10)
fig.subplots_adjust(top=.84, bottom=.29, wspace=.26)
for suffix in ["svg", "png"]:
    fig.savefig(root / (Path(__file__).stem + "." + suffix), dpi=160,
                metadata={"Description": "Exact constant-metric example; phase-space input slices, not the full product metric."}
                if suffix == "svg" else {"Description": "W43--W44 exact metric input slices."})
plt.close(fig)
