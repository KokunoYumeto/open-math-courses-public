"""Exact real trace and incidence diagram for Exercise 22.117."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 5.8), dpi=180)
fig.patch.set_facecolor("white")
fig.suptitle("A boundary loop gives a relative degree-two class",
             fontsize=18, fontweight="bold", color="#192b43", y=.97)
left, right = axes
z = np.linspace(-1.65, 1.65, 400)
left.plot(z, z*z, color="#275a94", linewidth=2.6, label=r"$P:\ t=z^2$")
left.axhline(1, color="#ad592a", linewidth=2.6, label=r"$L:\ t=1$")
between = np.linspace(-1, 1, 160)
left.fill_between(between, between*between, 1, alpha=.12, color="#275a94")
left.scatter([-1, 1], [1, 1], s=48, color="#192b43", zorder=5)
point_box = dict(facecolor="white", edgecolor="none", pad=2)
left.annotate(r"$A=(1,-1)$", (-1, 1), xytext=(-1.65, 1.35),
              fontsize=11, bbox=point_box)
left.annotate(r"$B=(1,1)$", (1, 1), xytext=(.7, 1.35),
              fontsize=11, bbox=point_box)
left.set(xlim=(-1.8, 1.8), ylim=(-.15, 3.05),
         xlabel=r"$z$ (real)", ylabel=r"$t$ (real)")
left.set_title("Real trace of the complex pair", fontsize=13, pad=12)
left.legend(loc="upper center", frameon=False, fontsize=11)
left.spines[["top", "right"]].set_visible(False)
left.grid(alpha=.15)

right.set(xlim=(-.2, 3.2), ylim=(-1.5, 1.7))
right.axis("off")
right.set_title("Cohomology incidence diagram", fontsize=13, pad=12)
for y, label in [(.52, r"$A$"), (-.52, r"$B$")]:
    curvature = -.42 if y > 0 else .42
    arc = FancyArrowPatch((.45, .25), (2.55, .25),
                          connectionstyle=f"arc3,rad={curvature}",
                          arrowstyle="-", linewidth=2.5, color="#667b94")
    right.add_patch(arc)
    right.text(1.5, .25+y, label, ha="center", va="center", fontsize=15,
               bbox=dict(facecolor="white", edgecolor="none", pad=2))
right.scatter([.45, 2.55], [.25, .25], s=300,
              c=["#275a94", "#ad592a"], zorder=4)
right.text(.45, -.05, r"$P\simeq\mathbf{C}$", ha="center", fontsize=14)
right.text(2.55, -.05, r"$L\simeq\mathbf{C}$", ha="center", fontsize=14)
right.text(1.5, 1.3, "Two components · two intersections", ha="center",
           fontsize=12, color="#52657c")
right.text(1.5, -.83, r"$H^1(Y;\mathbf{Q})\simeq\mathbf{Q}$",
           ha="center", fontsize=17, color="#192b43")
right.text(1.5, -1.22, r"$H^2(X,Y;\mathbf{Q})\simeq H^1(Y;\mathbf{Q})$",
           ha="center", fontsize=16, color="#192b43")
fig.text(.5, .035, r"$X=\mathbf{A}^2_{t,z}$     "
         r"$Y=V((z^2-t)(t-1))$"
         "     •     Exercise 22.117, equations (22.299)–(22.300)",
         ha="center", fontsize=11, color="#52657c")
fig.subplots_adjust(left=.07, right=.98, bottom=.16, top=.82, wspace=.24)
fig.savefig(Path(__file__).with_suffix(".png"), facecolor="white")
plt.close(fig)
