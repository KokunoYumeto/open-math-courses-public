"""Original exact-geometry illustration for public Proposition 6.8e.

Adapted from the original course workflow's connected-chart diagram. This
script only writes its own two figure outputs and does not rewrite a report.
Five branches are numerical samples; all-N estimates are proved in the text.
Authored mathematical expression and scene source: CC0.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "plaque-connected-chart-v1"
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent

def a(r):
    return np.exp(-r)

def delta(r):
    return a(r) / 16

fig = plt.figure(figsize=(12, 7.6), layout="constrained")
fig.suptitle("Figure 6.8b · Ambient spaces: Lemma 6.8d; packing: Proposition 6.8e",
             fontsize=12)
gs = fig.add_gridspec(2, 2, height_ratios=[5, 1.7])
ax = fig.add_subplot(gs[0, 0])
right = fig.add_subplot(gs[0, 1])
caption = fig.add_subplot(gs[1, :])
caption.axis("off")
y = np.linspace(.001, 3.999, 900)
colors = ["#b5d8e9", "#73a6d0", "#559a88", "#dda459", "#a880bc"]

for k, color in zip(range(5), colors):
    r = y + 4*k
    ax.fill_betweenx(y, a(r), a(r)+delta(r), color=color, alpha=.9)
    ax.plot(a(r), y, color="#304451", lw=.7)
    ax.plot(a(r)+delta(r), y, color="#304451", lw=.7)
    left = float(a(2+4*k))
    end = left+float(delta(2+4*k))
    ax.plot([left, end], [2, 2], color="#b53232", lw=4)
ax.axhline(2, color="#963f3f", lw=1, ls="--", alpha=.5)
ax.set(xlim=(-.03, 1.09), ylim=(0, 4),
       xlabel="Physical leaf coordinate x",
       ylabel="Physical transverse coordinate y",
       title="Connected chart: five sampled branches")
ax.set_xticks([0, .25, .5, .75, 1])
ax.set_yticks([0, 1, 2, 3, 4])
ax.text(.5, 3.85, "y = 0 and y = 4 are identified", ha="center", fontsize=9,
        bbox={"facecolor":"white", "alpha":.9, "edgecolor":"none"})
ax.text(.5, 1.8, "Selected leaf y = 2", ha="center", color="#963f3f",
        fontsize=10, bbox={"facecolor":"white", "alpha":.9, "edgecolor":"none"})

for j in range(5):
    left = float(a(2+4*j))
    end = left+float(delta(2+4*j))
    right.plot([left, end], [j, j], color="#b53232", lw=9,
               solid_capstyle="butt")
    if j == 0:
        right.annotate(f"-log u = {2+4*j}", (left, j), xytext=(-12, 0),
                       textcoords="offset points", ha="right", va="center",
                       fontsize=10)
    else:
        right.text(end*1.3, j, f"-log u = {2+4*j}", va="center", fontsize=10)
right.set_xscale("log")
right.set(xlim=(1e-9, 2), ylim=(-.7, 4.7),
          xlabel="Physical x on logarithmic scale", ylabel="Plaque index j",
          title="Five positive plaques on the same leaf")
right.set_yticks(range(5))
right.grid(axis="x", alpha=.2)
right.text(.5, .95, "Intervals I\u2c7c = (u\u2c7c, 17u\u2c7c/16); none overlaps",
           ha="center", transform=right.transAxes, fontsize=10)

caption.text(.01, .93,
    r"$\mathcal{F}(t,u)=(u(1+t/16),-\log u\ \mathrm{mod}\ 4),\quad "
    r"T=U=(0,1),\quad u_j=e^{-(2+4j)}$", fontsize=12)
caption.text(.01, .64,
    "Left: numerical samples of branches -log u = y + 4k, k = 0,...,4; "
    "all other branches are omitted.\n"
    "The chart is connected through the identified transverse edges. "
    "Boundaries t = 0, 1 and u = 0, 1 are excluded.", fontsize=10)
caption.text(.01, .32,
    r"Proposition 6.8e: $\|P_{N,u}\|_{Q_M^1(I_u)\to S_M^0(I_u)}"
    r"\leq\sqrt{3}/2,\quad P'_{N,2}1=\sum_{j=0}^{N-1}g_{u_j}$.",
    fontsize=12)
caption.text(.01, .01,
    r"One global test: $\|1\|_{W^1(M)}=2,\quad"
    r"\|P'_{N,2}1\|_2=\sqrt{N},\quad"
    r"\|P'_N\|_{W^1\to W^0}\geq\sqrt{N}/2$.", fontsize=12)
for suffix in ["svg", "png"]:
    fig.savefig(OUT/f"plaque-connected-chart.{suffix}", dpi=160,
                metadata={"Creator": "Original course mathematical illustration", "Date": None,
                          "Description": "Exact connected chart and Proposition6.8e physical plaque packing; CC0."}
                if suffix == "svg" else
                {"Software": "Matplotlib; original course mathematical illustration",
                 "Description": "Exact connected chart and Proposition6.8e physical plaque packing; CC0."})
plt.close(fig)
