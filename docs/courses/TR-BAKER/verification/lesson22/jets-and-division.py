"""Exact monomial and division-point diagrams for Lesson22, no numerical fitting."""
from pathlib import Path
from math import comb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

root = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, (left, right) = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw={"width_ratios": [1.08, 1]})
colors = ["#283b66", "#315f8c", "#257f8e", "#309b83", "#77ab57"]
T = 4
points = [(a, b) for a in range(T+1) for b in range(T+1-a)]
assert len(points) == comb(T+2, 2) == 15
for a, b in points:
    left.scatter([a], [b], s=175, color=colors[a+b], edgecolor="white", linewidth=1.2, zorder=3)
left.plot([0, T], [T, 0], color="#748196", linestyle="--", linewidth=1)
left.set(xlim=(-.4, 4.5), ylim=(-.4, 4.6), xlabel=r"Exponent $a$ of $z_1$",
         ylabel=r"Exponent $b$ of $z_2$", title="Normal jets through order 4")
left.xaxis.set_major_locator(MultipleLocator(1)); left.yaxis.set_major_locator(MultipleLocator(1))
left.grid(alpha=.15); left.set_aspect("equal")
left.text(2.4, 3.65, r"$a+b\leq 4$"+"\n15 independent classes", ha="center", va="center", fontsize=11)

old = [0, 1, 2]; new = [s/3 for s in range(7)]
right.hlines([1, 0], -.08, 2.08, color="#b6bfcc", linewidth=1)
right.scatter(old, [1]*3, s=95, color="#283b66", zorder=3)
right.scatter(new, [0]*7, s=75, color="#309b83", zorder=3)
for value in old:
    right.plot([value, value], [.08, .92], color="#d5dbe3", linestyle=":")
right.set(xlim=(-.17, 2.17), ylim=(-.42, 1.6), yticks=[0, 1],
          yticklabels=["Division points", "Initial points"], xlabel=r"Additive coordinate in $G=\mathbf{G}_a$")
right.set_xticks(new, ["0", "$1/3$", "$2/3$", "1", "$4/3$", "$5/3$", "2"])
right.set_title(r"Distinct points: $S=2$, $\ell=3$")
right.text(1, 1.36, r"$|\Gamma(2)|=3$", ha="center", color="#283b66")
right.text(1, .34, r"$|\Gamma_3(6)|=7$", ha="center", color="#24755e")
for ax in (left, right):
    ax.spines[["top", "right"]].set_visible(False)
right.spines["left"].set_visible(False); right.tick_params(axis="y", length=0)
fig.subplots_adjust(left=.07, right=.98, top=.87, bottom=.21, wspace=.46)
fig.text(.5, .045, "Left: monomials $z_1^a z_2^b$ counted in Theorem 22.25.  "
         "Right: inclusive endpoints counted in Lemma 22.22.", ha="center", fontsize=10)
fig.savefig(root/"jets-and-division.png", dpi=175, facecolor="white")
plt.close(fig)
print("Saved jets-and-division.png; exact counts 15 and 7.")
