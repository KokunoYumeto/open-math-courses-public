"""Real-path slice of the degree-two cover in Exercise 22.132."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(11, 7), layout="constrained")
gs = fig.add_gridspec(2, 2, height_ratios=[3, 1.25])
ax = fig.add_subplot(gs[0, 0])
left = np.linspace(1, 2, 200)
right = np.linspace(2, 4, 250)
ax.plot(left, (left - 2)**2 / left, lw=3, color="#195b9a")
ax.plot(right, (right - 2)**2 / right, lw=3, color="#c46819")
for start, end, color in [(1.60, 1.32, "#195b9a"), (2.6, 3.0, "#c46819")]:
    ax.annotate("", xy=(end, (end-2)**2/end),
                xytext=(start, (start-2)**2/start),
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.5})
ax.scatter([1, 2, 4], [1, 0, 1], c="#242e36", zorder=4)
ax.annotate(r"$\rho_1:\ 2\to1$", (1.15, .40), color="#195b9a")
ax.annotate(r"$\rho_4:\ 2\to4$", (2.7, .55), color="#a8530b")
ax.set(xlim=(.8, 4.2), ylim=(-.12, 1.18), xlabel=r"$x$",
       ylabel=r"$t=(x-2)^2/x$", xticks=[1, 2, 4], yticks=[0, 1])
ax.set_title("Positive real paths in the cover", fontsize=13, pad=14)
ax.grid(alpha=.15)

bx = fig.add_subplot(gs[0, 1])
bx.set_xlim(0, 1); bx.set_ylim(0, 1); bx.axis("off")
bx.text(.5, .94, r"$\tau(x)=4/x,\qquad t\circ\tau=t$",
        ha="center", fontsize=15)
for yy, names, xs in [(.72, ["1", "2", "4"], [.16, .50, .84]),
                      (.28, ["1", "0", "1"], [.16, .50, .84])]:
    for xx, name in zip(xs, names):
        bx.scatter([xx], [yy], s=35, c="#242e36")
        offset = .055 if yy > .5 else -.065
        bx.text(xx, yy + offset, rf"${name}$", ha="center", fontsize=14)
for xx in [.16, .50, .84]:
    bx.annotate("", xy=(xx, .32), xytext=(xx, .66),
                arrowprops={"arrowstyle": "->", "color": "#77838c"})
bx.text(.52, .49, r"$t$", fontsize=14)
bx.annotate("", xy=(.17, .72), xytext=(.48, .72),
            arrowprops={"arrowstyle": "->", "color": "#195b9a", "lw": 2.5})
bx.annotate("", xy=(.83, .72), xytext=(.52, .72),
            arrowprops={"arrowstyle": "->", "color": "#c46819", "lw": 2.5})
bx.text(.5, .13, r"$t^{-1}(0)=2[2],\quad t^{-1}(1)=[1]+[4]$",
        ha="center", fontsize=13)
bx.text(.5, .02, "Both paths project from 0 to 1.", ha="center", fontsize=12)

cx = fig.add_subplot(gs[1, :]); cx.axis("off")
cx.text(.5, .83, r"$\xi=\frac{1}{2}(\rho_1+\rho_4),\qquad{}"
        r"b_\ell=-(1+\tau_*)\xi=-\rho_1-\rho_4$",
        ha="center", fontsize=17)
cx.text(.5, .40, r"$\partial b_\ell=2[2]-[1]-[4],\qquad"
        r"\int_{b_\ell}\frac{dx}{x}=\log2-\log2=0$",
        ha="center", fontsize=17)
cx.text(.5, .02, "Real-path slice; the complex cover also branches at x = −2, t = −8.",
        ha="center", color="#47535b", fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png"), dpi=170, facecolor="white")
plt.close(fig)
