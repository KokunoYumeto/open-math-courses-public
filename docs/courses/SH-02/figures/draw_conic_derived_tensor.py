"""Exact complex and stalk tests for the induced-orbit tensor counterexample.

Original diagram, additionally offered under CC0. Coordinates below describe
the page layout, not a metric embedding of the 2-adic transversal.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

import argparse
_parser=argparse.ArgumentParser()
_parser.add_argument("--output",type=Path,default=Path(__file__).parent)
ASSETS = _parser.parse_args().output
ASSETS.mkdir(parents=True,exist_ok=True)
matplotlib.rcParams["svg.hashsalt"] = "SH02-conic-derived-tensor-v1"
INK, BLUE, RED, GREEN = "#193246", "#2a6b91", "#ad473e", "#127f70"
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans", "svg.fonttype": "path"})
fig = plt.figure(figsize=(17, 11), facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 17), ylim=(0, 11))
ax.axis("off")

def text(x, y, value, size=17, color=INK, **kwargs):
    return ax.text(x, y, value, fontsize=size, color=color, **kwargs)

def box(x, y, w, h, label, color=BLUE, size=20):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.07", linewidth=2,
                             edgecolor=color, facecolor="#f1f6f8"))
    text(x + w/2, y + h/2, label, size, color, ha="center", va="center")

def arrow(x1, y1, x2, y2, label, color=BLUE, size=15):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=17,
                                linewidth=2, color=color))
    text((x1+x2)/2, (y1+y2)/2 + .17, label, size, color, ha="center", va="bottom")

text(.65, 10.45, "A bounded tensor can lose local constancy on an induced orbit", 25, weight="bold")
text(.65, 9.9, r"$A=\mathbb{Q}[z_1,z_2],\quad\kappa=A/(z_1,z_2),\quad\mathrm{gldim}(A)=2$", 20)
text(.65, 9.4, r"$X=(\mathbb{R}\times\mathbb{Z}_2)/((t+1,k)\sim(t,k+1))$; $L|_U\simeq(\bigoplus_{m\in\mathbb{Z}} A e_m)_U$, $P=\bigoplus_{n\geq1}L$", 18)

text(.65, 8.82, "The seam shifts both basis indices and the transversal", 18, weight="bold")
text(.75, 8.33, r"$(1,k,e_m)\sim(0,k+1,e_{m+1})$", 19)
text(8.4, 8.33, r"$h(e_{n,m})=1_{C_n}(k-m)e_m$", 19)
text(.75, 7.89, r"$C_n=\{v_2=2n\}$ is clopen; $k-m$ is unchanged at the seam.", 16)

text(.65, 7.3, "Before tensoring: a flat complex in degrees −1, 0, 1", 19, weight="bold")
box(.8, 6.23, 2.5, .75, r"$P$")
box(6.0, 6.23, 4.7, .75, r"$L\oplus P\oplus P$")
box(13.55, 6.23, 2.5, .75, r"$P$")
arrow(3.4, 6.61, 5.87, 6.61, r"$(h,-z_2,z_1)$", size=17)
arrow(10.83, 6.61, 13.43, 6.61, r"$(0,z_1,z_2)$", size=17)
text(1.0, 5.8, r"$\mathcal{H}^{-1}(F)=0,\quad\mathcal{H}^0(F)=L,\quad\mathcal{H}^1(F)=P_\kappa$", 19)
text(10.1, 5.8, "All input cohomology is locally constant on X.", 15, GREEN)

text(.65, 5.18, r"After tensoring with $\kappa_X$: the Koszul entries vanish", 19, weight="bold")
box(.8, 4.11, 2.5, .75, r"$P_\kappa$")
box(6.0, 4.11, 4.7, .75, r"$L_\kappa\oplus P_\kappa\oplus P_\kappa$")
box(13.55, 4.11, 2.5, .75, r"$P_\kappa$")
arrow(3.4, 4.49, 5.87, 4.49, r"$(\bar h,0,0)$", RED, 17)
arrow(10.83, 4.49, 13.43, 4.49, r"$0$", RED, 17)
text(1.0, 3.65, r"$\mathcal{H}^0(F\otimes_A^{\mathrm{L}}\kappa_X)=\mathrm{coker}(\bar h)\oplus P_\kappa\oplus P_\kappa$", 20)

text(.65, 3.03, r"The section $q=[e_0]$ has incompatible germs on the induced orbit", 19, weight="bold")
box(.8, 1.63, 6.05, 1.05, r"$x=[0,0]:\quad q_x\ne 0$", RED, 21)
box(9.0, 1.63, 7.05, 1.05, r"$y_n=[0,2^{2n}]:\quad q_{y_n}=0$", BLUE, 21)
text(1.0, 1.13, r"$0\notin C_n$ for every $n$.", 17, RED)
text(9.2, 1.13, r"$\bar h(e_{n,0})=e_0$ on $I\times C_n$.", 17, BLUE)
text(.8, .57, r"$y_n\to x$ in the induced orbit topology; a locally constant sheaf cannot have these section germs.", 17, weight="bold")
text(.8, .16, "Exact algebra and stalk tests; page spacing is schematic. Proof: Operations on orbits with their induced topology, IOR4.", 12)

for extension in ("png", "svg"):
    fig.savefig(ASSETS / ("conic-derived-tensor." + extension), dpi=160, bbox_inches="tight", pad_inches=.08, metadata={"Date":None} if extension=="svg" else {})
plt.close(fig)
print("conic-derived-tensor.png and .svg")
