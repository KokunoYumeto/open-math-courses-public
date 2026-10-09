"""Exact real-slice examples for PROPER-SUPPORT-ACYCLICITY.md Sections 2 and 7."""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "axes.titlesize": 15, "mathtext.fontset": "dejavusans"})
x = np.linspace(-2.4, 2.4, 801)
r = np.sqrt(1 + x*x) + 1
fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.9), constrained_layout=True)

ax = axes[0]
ax.fill_between(x, -r, r, color="#cfe4f8", alpha=.85)
ax.plot(x, r, color="#28618b", lw=1.7)
ax.plot(x, -r, color="#28618b", lw=1.7)
ax.plot(x, x, color="#b54b20", lw=3)
ax.set_title("A proper closed neighbourhood")
ax.text(-2.2, 3.22, r"$F_r=\{(x,y): |y|\leq\sqrt{1+x^2}+1\}$", fontsize=11)
ax.text(.25, .04, r"$S=\{y=x\}$", color="#8e3517", rotation=35)
ax.text(-1.95, -3.2, r"$p:F_r\longrightarrow\mathbf{R},\quad p(x,y)=x$", fontsize=11)
ax.annotate("compact fibre interval", xy=(1.7, 1.0), xytext=(.3, -1.55),
            arrowprops={"arrowstyle": "->", "color": "#28618b"}, color="#28618b", fontsize=11)
ax.plot([1.7, 1.7], [-np.sqrt(1+1.7**2)-1, np.sqrt(1+1.7**2)+1],
        color="#28618b", linestyle="--", lw=1.3)

ax = axes[1]
ax.axhspan(0, 3.6, color="#edf6e8")
ax.axhline(0, color="#387548", linestyle="--", lw=1.7)
ax.plot(x[x <= 0], x[x <= 0], color="#a7a7a7", linestyle=":", lw=2)
ax.plot(x[x > 0], x[x > 0], color="#b54b20", lw=3)
ax.plot([0], [0], marker="o", markerfacecolor="white", markeredgecolor="#b54b20", markersize=8, zorder=5)
ax.plot([1], [1], marker="o", color="#b54b20", markersize=5)
ax.set_title("Restriction can lose proper support")
ax.text(-2.18, 3.1, r"$W=\{y>0\}$ (open)", color="#387548")
ax.text(.27, .13, r"$S\cap W=\{(x,x):x>0\}$", color="#8e3517", fontsize=11)
ax.text(-2.14, -3.15, r"$(p|_{S\cap W})^{-1}([-1,1])$", fontsize=11)
ax.text(-2.14, -3.55, r"$=\{(x,x):0<x\leq1\}$: not compact", fontsize=11)
ax.annotate("missing limit point", xy=(0, 0), xytext=(-2.1, -1.7),
            arrowprops={"arrowstyle": "->", "color": "#b54b20"}, color="#8e3517", fontsize=11)

for ax in axes:
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(-3.8, 3.6)
    ax.set_xlabel(r"base coordinate $x$")
    ax.set_ylabel(r"fibre coordinate $y$")
    ax.grid(alpha=.2)
    ax.spines[["top", "right"]].set_visible(False)

fig.savefig(out / "proper-support-control.png", dpi=170)
fig.savefig(out / "proper-support-control.svg")
plt.close(fig)

data = {
    "classification": "Exact real-coordinate example; complex-fibre versions obtained by taking a real slice.",
    "projection": "p(x,y)=x",
    "closed_support": "S={(x,y):y=x}",
    "proper_tube_radius": "r(x)=sqrt(1+x^2)+1",
    "open_neighbourhood_cut": "W={(x,y):y>0}",
    "noncompact_compact_base_preimage": "{(x,x):0<x<=1}",
    "plot_window": {"base": [-2.4, 2.4], "fibre": [-3.8, 3.6]},
    "sample_count": len(x),
    "checks": {
        "sample_radius_strictly_contains_graph": bool(np.all(r > np.abs(x))),
        "radius_is_globally_strict": "sqrt(1+x^2)>|x|, hence r(x)>|x| for every real x",
        "noncompactness_witness": "(1/n,1/n) for n>=1 converges in R^2 to (0,0), which is not in W",
    },
}
(out / "proper-support-figure-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
