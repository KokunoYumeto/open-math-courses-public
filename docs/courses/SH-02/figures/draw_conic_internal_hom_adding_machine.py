"""Illustrate the exact adding-machine suspension and 2-adic valuation test.

The tree records clopen ball inclusion and exact valuation levels. It is not
a metric drawing of the 2-adic integers. Three levels sample an infinite
family proved in the lesson.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


matplotlib.rcParams["svg.hashsalt"] = "SH02-conic-internal-hom-adding-machine-v1"
import argparse
_parser=argparse.ArgumentParser()
_parser.add_argument("--output",type=Path,default=Path(__file__).parent)
OUT = _parser.parse_args().output
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#183044"
BLUE = "#236a95"
RED = "#a54842"
GOLD = "#a77b25"
MUTED = "#536878"
LIGHT = "#edf5fa"
FAINT = "#f6f8fa"

fig, (left, right) = plt.subplots(
    1, 2, figsize=(15.2, 8.5), dpi=180, facecolor="white",
    width_ratios=(0.91, 1.09),
)
fig.subplots_adjust(left=.055, right=.975, top=.82, bottom=.19, wspace=.16)
fig.text(.055, .945, "An internal Hom that loses induced-orbit constancy",
         fontsize=22, color=NAVY, weight="bold")
fig.text(.055, .885,
         r"$X=(\mathbb{R}\times\mathbb{Z}_2)/((t+1,k)\sim(t,k+1))$"
         r"$\qquad P=\mathcal{H}om((\bigoplus_n\mathbb{Z})_X,\mathbb{Z}_X)$",
         fontsize=15.5, color=MUTED)

for ax in (left, right):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

# Left panel: mapping-torus seam and local product chart.
left.text(.02, .97, "A compact suspension with recurrent orbits",
          color=NAVY, fontsize=17, weight="bold", va="top")
frame = Rectangle((.14, .29), .69, .46, edgecolor=NAVY,
                  facecolor=FAINT, linewidth=1.8)
left.add_patch(frame)
left.add_patch(Rectangle((.14, .29), .13, .46, facecolor=LIGHT,
                         edgecolor="none"))
left.add_patch(Rectangle((.70, .29), .13, .46, facecolor=LIGHT,
                         edgecolor="none"))
left.text(.15, .715, r"$t=0$", color=NAVY, fontsize=13)
left.text(.75, .715, r"$t=1$", color=NAVY, fontsize=13)
left.text(.33, .51, r"flow in the $t$ direction", color=BLUE,
          fontsize=14, ha="center")
left.add_patch(FancyArrowPatch((.32, .45), (.63, .45),
                               arrowstyle="-|>", mutation_scale=18,
                               color=BLUE, linewidth=2.5))
left.text(.48, .33, r"transverse coordinate $k\in\mathbb{Z}_2$",
          ha="center", color=MUTED, fontsize=12.7)
left.add_patch(FancyArrowPatch((.83, .80), (.14, .80),
                               arrowstyle="-|>", mutation_scale=17,
                               color=GOLD, linewidth=2))
left.text(.50, .845, r"seam: $(1,k)\sim(0,k+1)$",
          color=GOLD, ha="center", fontsize=14)
box = FancyBboxPatch((.08, .06), .83, .145,
                     boxstyle="round,pad=.017,rounding_size=.023",
                     edgecolor=BLUE, facecolor=LIGHT, linewidth=1.4)
left.add_patch(box)
left.text(.50, .158, r"$U\simeq I\times\mathbb{Z}_2$;  "
          r"$b\cap U\simeq I\times\mathbb{Z}$",
          ha="center", va="center", color=NAVY, fontsize=13.5)
left.text(.50, .096, r"integers return densely in the $2$-adic transverse set",
          ha="center", va="center", color=MUTED, fontsize=11.7)

# Right panel: the exact branch levels on the nested zero path in Z_2.
right.text(.02, .97, "Nested clopen balls and the product-sheaf germ",
           color=NAVY, fontsize=17, weight="bold", va="top")
path_x = .205
top_y = .86
step = .092
right.plot([path_x, path_x], [top_y, top_y - 8*step],
           color=NAVY, lw=2.8)
right.text(path_x-.08, top_y+.035, r"$K$", color=NAVY,
           fontsize=13, va="bottom")
right.text(.10, .083, r"$0\in\bigcap_m2^mK$",
           color=NAVY, fontsize=12, va="top")

for m in range(1, 8):
    y = top_y - m*step
    right.plot(path_x, y, "o", ms=5, color=NAVY)
    if m in (2, 3, 4, 5, 6, 7):
        bx = .47
        color = BLUE if m % 2 == 0 else RED
        right.plot([path_x, bx-.025], [y, y], color=color, lw=2.1)
        right.plot(bx, y, "o", ms=8, color=color)
        if m % 2 == 0:
            n = m // 2
            label = rf"$C_{n}:\ v_2= {m}$  ·  $s_{n}=1$"
        else:
            n = (m-1) // 2
            label = rf"$y_{n}=2^{{{m}}}:\ s_{{y_{n}}}=0$"
        right.text(.50, y, label, va="center", color=color, fontsize=12.5)
    else:
        right.text(.27, y, rf"$2^{{{m}}}K$", va="center",
                   color=MUTED, fontsize=11.7)

right.text(.54, .070, r"$s_x\ne0$",
           ha="center", color=GOLD, fontsize=14.5, weight="bold")

fig.text(.5, .105,
         "Blue even-valuation branches occur in every neighborhood of 0; red odd-valuation returns also converge to 0.",
         ha="center", color=NAVY, fontsize=13)
fig.text(.5, .058,
         "Only three pairs are drawn. Branch spacing shows clopen containment, not ordinary distance in the 2-adic integers.",
         ha="center", color=MUTED, fontsize=11.5)

for ext in ("png", "svg"):
    fig.savefig(
        OUT / f"conic-internal-hom-adding-machine.{ext}",
        bbox_inches="tight", pad_inches=.13, facecolor="white",
        metadata={"Date": None} if ext == "svg" else {},
    )
plt.close(fig)
