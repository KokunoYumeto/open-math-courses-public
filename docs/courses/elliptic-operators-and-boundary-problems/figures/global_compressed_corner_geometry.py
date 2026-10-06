"""Render the exact normal coordinates in GL4, GL7 and GL8."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 13, "mathtext.fontset": "stix", "font.family": "DejaVu Sans"})
fig, axes = plt.subplots(1, 2, figsize=(14.4, 6.4), constrained_layout=True)
ax, bx = axes
colors = { -1: "#a04716", 0: "#195b9a", 1: "#38864c" }
ax.set(xlim=(-.09, 2.08), ylim=(-.09, 2.08), xlabel=r"$x_n$", ylabel=r"$y_n$")
ax.set_aspect("equal")
for t in (.25, .5, .75, 1.0):
    x = np.linspace(0, 2*t, 160)
    ax.plot(x, 2*t-x, color="#adb6c1", lw=1.2)
ax.text(.17, 1.88, r"$x_n+y_n=2t$", color="#465362")
for r in (-1, 0, 1):
    t = np.linspace(0, 2/max(1+r/2, 1-r/2), 180)
    ax.plot(t*(1+r/2), t*(1-r/2), color=colors[r], lw=2.8)
ax.text(.05, 1.81, r"$r=-1:\ y_n=3x_n$", color=colors[-1])
ax.text(1.06, 1.26, r"$r=0:\ y_n=x_n$", color=colors[0], rotation=45)
ax.text(1.05, .28, r"$r=1:\ y_n=x_n/3$", color=colors[1], rotation=18)
ax.plot(0, 0, "o", color="#8a277a", markersize=7)
ax.set_title("Original positive normal quadrant", pad=12)
ax.grid(alpha=.16)

bx.set(xlim=(-2.25, 2.25), ylim=(-.1, 1.08), xlabel=r"$r=2(x_n-y_n)/(x_n+y_n)$", ylabel=r"$t=(x_n+y_n)/2$")
bx.set_xticks([-2, -1, 0, 1, 2])
bx.set_yticks([0, .25, .5, .75, 1])
bx.fill_between([-2, 2], 0, 1, color="#f5f7fa")
for t in (.25, .5, .75, 1):
    bx.plot([-2, 2], [t, t], color="#adb6c1", lw=1.2)
for r in (-1, 0, 1):
    bx.plot([r, r], [0, 1], color=colors[r], lw=2.8)
bx.plot([-2, 2], [0, 0], color="#8a277a", lw=3.2)
for r in (-2, 2):
    bx.plot([r, r], [0, 1], color="#47505d", lw=2)
bx.text(-2.05, .58, r"$x_n=0$", rotation=90, ha="right", color="#47505d")
bx.text(2.05, .58, r"$y_n=0$", rotation=90, ha="left", color="#47505d")
bx.annotate(r"Lifted diagonal: $r=0$", xy=(0, .77), xytext=(.35, .87),
            arrowprops={"arrowstyle": "->", "color": colors[0]}, color=colors[0], fontsize=12)
bx.text(.0, -.065, r"New face $t=0$: each point retains a normal ray", ha="center", color="#8a277a", fontsize=11)
bx.set_title("Stretched normal rectangle", pad=12)
fig.suptitle(r"$x_n=t(1+r/2),\qquad y_n=t(1-r/2)$", fontsize=21)
fig.text(.5, -.045, r"Along the lifted diagonal: $\delta(x_n-y_n)=t\,\delta r$;  ordinary covectors map by $(\tau',\tau_n)\mapsto(\xi'=\tau',\rho=t\tau_n)$.", ha="center", fontsize=13)
for ext in ("png", "svg"):
    fig.savefig(out / f"compressed_corner_geometry.{ext}", dpi=170, bbox_inches="tight")
plt.close(fig)
