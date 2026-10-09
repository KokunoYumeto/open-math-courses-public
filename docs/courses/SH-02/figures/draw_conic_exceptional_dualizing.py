"""Exact dualizing-section and return-germ test on the 2-adic suspension.

The diagram samples three exact valuation pairs. The proof uses every
positive index; panel spacing is schematic, not a 2-adic metric.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams["svg.hashsalt"] = "SH02-conic-exceptional-dualizing-v1"

import argparse
_parser=argparse.ArgumentParser()
_parser.add_argument("--output",type=Path,default=Path(__file__).parent)
OUT = _parser.parse_args().output
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#183044"
BLUE = "#28658c"
RED = "#a34840"
GOLD = "#a77d20"
MUTED = "#526879"
LIGHT_BLUE = "#e7f1f7"
LIGHT_RED = "#faecea"
LIGHT_GOLD = "#f7f0db"

fig, (left, right) = plt.subplots(
    1, 2, figsize=(15.6, 7.8), dpi=180, facecolor="white",
    width_ratios=(1.03, .97))
fig.subplots_adjust(left=.055, right=.97, top=.80, bottom=.18, wspace=.14)
fig.text(.055, .94, "Exceptional inverse image on a recurrent orbit",
         fontsize=22, weight="bold", color=NAVY)
fig.text(.055, .88,
         r"$X=(\mathbb{R}\times\mathbb{Z}_2)/((t+1,k)\sim(t,k+1))$"
         r"$\qquad D_X=(X\to\mathrm{pt})^!\mathbb{Q}$",
         fontsize=16, color=MUTED)

for ax in (left, right):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()


def card(ax, x, y, w, h, face, edge, title, detail,
         title_size=15, detail_size=14):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=.014,rounding_size=.022",
        facecolor=face, edgecolor=edge, linewidth=1.5))
    ax.text(x+.025, y+h-.055, title, va="center", color=edge,
            fontsize=title_size, weight="bold")
    ax.text(x+.025, y+.055, detail, va="center", color=NAVY,
            fontsize=detail_size)


left.text(.02, .98, "Adjunction on an open flow box", va="top",
          color=NAVY, fontsize=17, weight="bold")
card(left, .03, .71, .91, .16, LIGHT_BLUE, BLUE,
     r"$W=I\times V$, with $V\subset\mathbb{Z}_2$ clopen",
     r"$R\Gamma_c(W;\mathbb{Q})\simeq\Gamma(V;\mathbb{Q})[-1]$",
     title_size=14.2, detail_size=14.8)
left.annotate("", xy=(.49, .645), xytext=(.49, .70),
              arrowprops={"arrowstyle": "-|>", "color": GOLD, "lw": 2.1})
card(left, .03, .45, .91, .16, LIGHT_GOLD, GOLD,
     "Exceptional adjunction",
     r"$\mathcal{H}^{-1}(D_X)(W)"
     r"\simeq\mathrm{Hom}_{\mathbb{Q}}(\Gamma(V;\mathbb{Q}),\mathbb{Q})$",
     title_size=15, detail_size=13.6)
left.annotate("", xy=(.49, .39), xytext=(.49, .44),
              arrowprops={"arrowstyle": "-|>", "color": GOLD, "lw": 2.1})
card(left, .03, .13, .91, .22, LIGHT_BLUE, BLUE,
     "A genuine local section",
     r"$\lambda(h)=\sum_{n\geq1}"
     r"\left(h(2^{2n})-h(0)\right)$",
     title_size=15, detail_size=15)
left.text(.50, .045, "Each sum is finite because h is constant near 0.",
          ha="center", color=MUTED, fontsize=12.3)

right.text(.02, .98, "Exact stalk tests on the induced orbit", va="top",
           color=NAVY, fontsize=17, weight="bold")
right.text(.50, .875, r"$x=[0,0],\quad z_n=[0,2^{2n+1}]\longrightarrow x$",
           ha="center", color=NAVY, fontsize=15)

for n, y in ((1, .665), (2, .455), (3, .245)):
    card(right, .025, y, .45, .155, LIGHT_BLUE, BLUE,
         rf"$C_{n}:v_2= {2*n}$",
         rf"$\lambda(1_{{C_{n}}})=1$",
         title_size=13.5, detail_size=13.7)
    card(right, .525, y, .45, .155, LIGHT_RED, RED,
         rf"$D_{n}:v_2= {2*n+1}$",
         rf"$\lambda_{{z_{n}}}=0$",
         title_size=13.5, detail_size=13.7)

right.text(.50, .10,
           "Blue tests remain nonzero in every neighborhood of x;",
           ha="center", color=BLUE, fontsize=12)
right.text(.50, .05,
           "red return points have zero germs and converge to x.",
           ha="center", color=RED, fontsize=12)

fig.text(.5, .085,
         "Three rows sample an infinite family. The labels are exact; vertical spacing is schematic.",
         ha="center", color=MUTED, fontsize=12.5)

for ext in ("png", "svg"):
    fig.savefig(OUT / f"conic-exceptional-dualizing.{ext}",
                bbox_inches="tight", pad_inches=.12, facecolor="white",
                metadata={"Date": None} if ext == "svg" else {})
plt.close(fig)
