"""Exact real slices of the original-stratum example in AC1--AC4/AP3.

All panels suppress imaginary coordinates. They do not alter the stated complex
dimensions. The complete objects and maps are given explicitly in the source.
Output: native SVG plus inspected PNG, both generated without raster AI assets.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "svg.fonttype": "none",
    "svg.hashsalt": "SH02-AC-original-conormal-example-v1",
    "axes.titleweight": "semibold",
    "mathtext.fontset": "dejavusans",
})
BLUE, GOLD, RED, GREEN = "#1f5f99", "#aa7012", "#b22c35", "#18734a"
GREY = "#6c7280"
fig, axs = plt.subplots(1, 3, figsize=(17.8, 7.5), dpi=150)
fig.patch.set_facecolor("white")
fig.subplots_adjust(left=0.035, right=0.985, bottom=0.28, top=0.82, wspace=0.20)
fig.suptitle("Original frontiers become a smaller analytic conormal locus",
             x=0.51, y=0.966, fontsize=20, weight="semibold")
fig.text(0.51, 0.905,
         r"Exact example: $M=\mathbb{C}^2$, $X=\{zw=0\}$; all three panels show real coordinate slices.",
         ha="center", fontsize=14, color="#333b48")

def panel(ax, title, xlabel, ylabel):
    ax.set_aspect("equal")
    ax.set_xlim(-1.60, 1.60)
    ax.set_ylim(-1.60, 1.60)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_facecolor("#f8fafc")
    ax.set_title(title, fontsize=15, pad=15)
    ax.annotate("", xy=(1.49, 0), xytext=(-1.49, 0),
                arrowprops={"arrowstyle": "->", "color": GREY, "lw": 1.3}, zorder=0)
    ax.annotate("", xy=(0, 1.49), xytext=(0, -1.49),
                arrowprops={"arrowstyle": "->", "color": GREY, "lw": 1.3}, zorder=0)
    ax.text(1.50, -0.18, xlabel, ha="right", va="top", fontsize=13)
    ax.text(0.12, 1.50, ylabel, ha="left", va="top", fontsize=13)

panel(axs[0], "1  Original base partition", r"$\mathrm{Re}\,z$", r"$\mathrm{Re}\,w$")
for lo, hi in [(-1.42, -0.08), (0.08, 1.42)]:
    axs[0].plot([lo, hi], [0, 0], color=BLUE, lw=5, solid_capstyle="round")
    axs[0].plot([0, 0], [lo, hi], color=GOLD, lw=5, solid_capstyle="round")
axs[0].scatter([0], [0], s=70, c=RED, zorder=4)
axs[0].text(-1.41, 0.20, r"$S_z:\ w=0,\ z\ne0$", color=BLUE, fontsize=13)
axs[0].text(0.17, 0.92, r"$S_w$", color=GOLD, fontsize=14)
axs[0].annotate(r"$S_0=\{0\}$", xy=(0, 0), xytext=(0.43, -0.67),
                color=RED, fontsize=14,
                arrowprops={"arrowstyle": "->", "color": RED, "lw": 1.1})
axs[0].text(0.5, -0.18,
            r"$H_{S_z}=\{w=0\},\quad H_{S_w}=\{z=0\}$" + "\n" +
            r"$B_{S_z}=B_{S_w}=\{0\}$",
            transform=axs[0].transAxes, ha="center", va="top", fontsize=12.5)

panel(axs[1], "2  Bad locus in the fibre over 0", r"$\mathrm{Re}\,\xi_z$", r"$\mathrm{Re}\,\xi_w$")
axs[1].plot([0, 0], [-1.42, 1.42], color=BLUE, lw=5)
axs[1].plot([-1.42, 1.42], [0, 0], color=GOLD, lw=5)
axs[1].scatter([0], [0], s=42, c=RED, zorder=4)
axs[1].text(0.17, 0.92, r"$\xi_z=0$", color=BLUE, fontsize=13)
axs[1].text(-1.43, 0.20, r"$\xi_w=0$", color=GOLD, fontsize=13)
axs[1].text(0.50, 0.52, r"$C_{S_0}|_0=\mathbb{C}^2$",
            ha="center", va="center", color="#495668", fontsize=13,
            transform=axs[1].transAxes,
            bbox={"facecolor": "white", "alpha": .88, "edgecolor": "none", "pad": 3})
axs[1].text(0.5, -0.18,
            r"$\mathcal{B}=\{z=w=0,\ \xi_z\xi_w=0\}$" + "\n" +
            r"$\dim_{\mathbb{C}}\mathcal{B}=1=n-1$",
            transform=axs[1].transAxes, ha="center", va="top", fontsize=12.5)

panel(axs[2], "3  Excluded affine parameters", r"$\mathrm{Re}\,c_z$", r"$\mathrm{Re}\,c_w$")
axs[2].plot([0, 0], [-1.42, 1.42], color=BLUE, lw=5)
axs[2].plot([-1.42, 1.42], [0, 0], color=GOLD, lw=5)
axs[2].text(0.16, 0.93, r"$c_z=0$", color=BLUE, fontsize=13)
axs[2].text(-1.42, 0.20, r"$c_w=0$", color=GOLD, fontsize=13)
axs[2].plot([0, 0.83], [0, 0.83], ls="--", lw=1.2, c=GREEN)
axs[2].scatter([0.83], [0.83], c=GREEN, s=85, zorder=4)
axs[2].annotate(r"$(\varepsilon,\varepsilon)$" + "\n" + "avoids both planes",
                xy=(0.83, 0.83), xytext=(0.42, -0.72), ha="center", color=GREEN,
                arrowprops={"arrowstyle": "->", "color": GREEN, "lw": 1.1},
                fontsize=12)
axs[2].text(0.5, -0.18,
            r"$F(0,\xi)=J(\xi)$, since $d\psi_0=0$" + "\n" +
            r"$F(\mathcal{B})=\{c_z=0\}\cup\{c_w=0\}$",
            transform=axs[2].transAxes, ha="center", va="top", fontsize=12.5)

fig.text(0.51, 0.105,
         r"$\psi=|z|^2+|w|^2,\qquad\ell_c=\varepsilon\,\mathrm{Re}(z+w),\qquad"
         r"\operatorname{graph}d(\psi+\ell_c)\cap J(\mathcal{B})=\varnothing.$",
         ha="center", fontsize=14)
fig.text(0.51, 0.053,
         "Full dimensions: each conormal closure is complex 2; the bad locus is complex 1; "
         "its parameter image has real dimension 2 inside real dimension 4.",
         ha="center", fontsize=12, color="#495668")
for ext in ("svg", "png"):
    fig.savefig(ROOT / f"analytic-conormal-exclusion.{ext}", facecolor="white", metadata={"Date": None} if ext == "svg" else None)
print("Wrote analytic-conormal-exclusion.svg and analytic-conormal-exclusion.png")
