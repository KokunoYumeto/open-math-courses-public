"""Reproducible local rank and actual-restriction diagram for HNC3-HNC4."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root = Path(__file__).parent
fig = plt.figure(figsize=(15, 6.8), facecolor="#fbfcff")
ax = fig.add_axes([.035, .21, .35, .69], projection="3d")
xx, yy = np.meshgrid(np.linspace(-1, 1, 2), np.linspace(-1, 1, 2))
ax.plot_surface(xx, yy, np.zeros_like(xx), color="#90aeca",
                alpha=.38, edgecolor="#7797b4", linewidth=.8)
ax.plot([0, 0], [0, 0], [0, 1.3], color="#b84538", lw=4)
ax.plot([0, 0], [0, 0], [-.35, 0], color="#b84538", lw=2, ls="--")
ax.scatter([0], [0], [0], s=50, color="#b84538", depthshade=False)
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.05, 1.05)
ax.set_zlim(-.35, 1.4)
ax.set_xlabel(r"$x=\operatorname{Re}(g-w)$", labelpad=7)
ax.set_ylabel(r"$y=\operatorname{Im}(g-w)$", labelpad=8)
ax.set_zlabel(r"$h=R^2-\rho$", labelpad=6)
ax.set_xticks([0]); ax.set_yticks([0]); ax.set_zticks([0])
ax.view_init(elev=22, azim=-50)
ax.set_title("Local fibre / radial corner chart", fontsize=14, pad=12)
ax.text(.03, .03, 1.20, r"$L:\ x=y=0$", color="#a1332c", fontsize=12)
ax.text(-.9, -.1, .055, r"$\partial K:\ h=0$", color="#375d7d", fontsize=12)
fig.text(.207, .16,
         r"$K:\ h\geq0$; independent rows $(d\pi,dx,dy,dh)$",
         ha="center", fontsize=12, color="#17334c")
fig.text(.207, .105,
         "A local coordinate chart, with other coordinates suppressed.\n"
         "The nonzero fibre value excludes the vertex from this corner.",
         ha="center", fontsize=10, color="#526174", linespacing=1.6)

bx = fig.add_axes([.43, .14, .55, .76])
bx.set_xlim(0, 12); bx.set_ylim(-.5, 5.8); bx.axis("off")
bx.text(6, 5.5, "Actual endpoint restriction diagram", ha="center",
        fontsize=15, color="#17334c")
positions = [(1.6, 3.7), (6.0, 3.7), (10.4, 3.7),
             (1.6, 1.7), (6.0, 1.7), (10.4, 1.7)]
labels = [r"$R\Gamma(K_0,A)$", r"$R\Gamma(K_0\times I,G)$",
          r"$R\Gamma(K_1,A)$", r"$R\Gamma(L_0,A)$",
          r"$R\Gamma(L_0\times I,G|)$", r"$R\Gamma(L_1,A)$"]
for (x,y), lab in zip(positions, labels):
    bx.text(x, y, lab, ha="center", va="center", fontsize=13,
            color="#17334c", bbox=dict(boxstyle="round,pad=.45",
                                     fc="#eaf0f8", ec="#7797b4"))
for yy in [3.7, 1.7]:
    for endpoint in [2.9, 9.05]:
        start = 4.6 if endpoint < 6 else 7.4
        bx.annotate("", xy=(endpoint, yy), xytext=(start, yy),
                    arrowprops=dict(arrowstyle="->", color="#526c88", lw=1.5))
        bx.text((endpoint+start)/2, yy+.32, r"$\sim$",
                ha="center", fontsize=14, color="#526c88")
for x in [1.6, 6, 10.4]:
    bx.annotate("", xy=(x, 2.12), xytext=(x, 3.28),
                arrowprops=dict(arrowstyle="->", color="#b84538", lw=1.6))
    bx.text(x+.2, 2.70, "res", fontsize=11, color="#a1332c")
bx.text(6, .7, r"$G=H^{-1}A$; $H$ follows original-stratum controlled paths.",
        ha="center", fontsize=12, color="#526174")
bx.text(6, .15,
        "Compact interval transport gives every horizontal isomorphism.\n"
        "Taking the fibres of the actual restrictions gives pair transport.",
        ha="center", fontsize=11, color="#526174", linespacing=1.7)
fig.text(.5, .97, "Holomorphic normal pair: joint corner rank and coefficient transport",
         ha="center", fontsize=17, color="#17334c")
fig.savefig(root/"holomorphic-normal-pair-choice.png", dpi=180)
fig.savefig(root/"holomorphic-normal-pair-choice.svg")
