from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})

navy = "#17324d"
blue = "#2676ad"
green = "#2e8655"
amber = "#d27a26"
red = "#b33e43"
gray = "#66727d"


def box(ax, x, y, w, h, label, edge=navy, face="#f4f7fa", size=10):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.018,rounding_size=0.025",
        linewidth=1.7,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=size, color=navy)


def arrow(ax, start, end, label="", color=navy, offset=0.055):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.9,
            color=color,
        )
    )
    if label:
        ax.text(
            (start[0] + end[0]) / 2,
            (start[1] + end[1]) / 2 + offset,
            label,
            ha="center",
            va="center",
            fontsize=9.5,
            color=color,
        )


fig, axes = plt.subplots(1, 3, figsize=(16.2, 6.1), constrained_layout=True)

# Panel 1: the two analytic deformations.
ax = axes[0]
ax.set_title("1  Keep the stable projection fixed", loc="left",
             fontweight="bold", color=navy)
box(ax, 0.05, 0.72, 0.90, 0.15,
    r"$\zeta I-a(y,t,\eta)$" + "\noriginal collar symbol",
    blue, "#edf6fc", 11)
box(ax, 0.05, 0.45, 0.90, 0.15,
    r"$\zeta I-a(y,0,\eta)$" + "\nfreeze near the boundary",
    amber, "#fff4e8", 11)
box(ax, 0.05, 0.16, 0.90, 0.17,
    r"$a_r=(1-r)a+ir\lambda(2q-I)$" + "\n"
    r"$q_r=q$ for every $0\leq r\leq1$",
    green, "#edf8f1", 11)
arrow(ax, (0.50, 0.71), (0.50, 0.61),
      r"uniform elliptic neighborhood", blue, 0.02)
arrow(ax, (0.50, 0.44), (0.50, 0.34),
      r"primary blocks stay in their half-planes", green, 0.02)
ax.text(0.50, 0.055,
        r"$b|_{\operatorname{ran}q}$ stays invertible",
        ha="center", color=gray, fontsize=10.5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Panel 2: exact bundle rotation.
ax = axes[1]
ax.set_title("2  Rotate the stable bundle and its inverse", loc="left",
             fontweight="bold", color=navy)
box(ax, 0.04, 0.72, 0.92, 0.15,
    r"$q_\theta$ blocks:  $c^2q,\ cds,\ cdbq,\ d^2I_G$",
    blue, "#edf6fc", 13)
box(ax, 0.07, 0.42, 0.36, 0.16,
    r"$\theta=0$" + "\n" + r"$\operatorname{ran}q\oplus0$",
    amber, "#fff4e8", 11)
box(ax, 0.57, 0.42, 0.36, 0.16,
    r"$\theta=\pi/2$" + "\n" + r"$0\oplus G$",
    green, "#edf8f1", 11)
arrow(ax, (0.44, 0.50), (0.56, 0.50), r"$0\leq\theta\leq\pi/2$", navy, 0.07)
box(ax, 0.09, 0.13, 0.82, 0.16,
    r"$s_\theta g=(\cos\theta\,sg,\ \sin\theta\,g)$" + "\n"
    r"$b_\theta s_\theta=I_G$",
    green, "#edf8f1", 11)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Panel 3: endpoint and index.
ax = axes[2]
ax.set_title("3  Reach the split trace endpoint", loc="left",
             fontweight="bold", color=navy)
box(ax, 0.05, 0.72, 0.90, 0.16,
    "unstable:  $E\\oplus G'$" + "\n"
    r"$D_t+i\Lambda^+$",
    blue, "#edf6fc", 11)
box(ax, 0.05, 0.47, 0.90, 0.16,
    "stable:  $G$" + "\n"
    r"$D_t-i\Lambda_G\ \longrightarrow\ -D_t+i\Lambda_G$"
    + "   by $-I_G$",
    green, "#edf8f1", 11)
box(ax, 0.05, 0.23, 0.90, 0.13,
    r"$B_{\rm sp}=\gamma_0|_G$",
    amber, "#fff4e8", 12)
ax.text(
    0.50,
    0.09,
    r"$\operatorname{ind}(P,B)"
    r"=\operatorname{ind}(P_{\rm sp},B_{\rm sp})"
    r"=\operatorname{ind}\widehat P_{\rm sp}$",
    ha="center",
    va="center",
    fontsize=10.2,
    color=red,
    bbox={"facecolor": "#fceded", "edgecolor": red, "boxstyle": "round,pad=0.35"},
)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

fig.suptitle(
    "Stable reduction of a first-order elliptic boundary problem",
    fontsize=18,
    fontweight="bold",
    color=navy,
)
fig.savefig(OUT / "stable_boundary_reduction.svg", bbox_inches="tight")
fig.savefig(OUT / "stable_boundary_reduction.png", dpi=220, bbox_inches="tight")
