"""Reproducible exact event diagram for the critical shell proof."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"svg.fonttype":"none","font.family":"DejaVu Sans"})
fig,ax=plt.subplots(figsize=(6.2,7.4))
ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
def box(y,h,title,formula,detail):
    ax.add_patch(FancyBboxPatch((.035,y),.93,h,boxstyle="round,pad=0.012",
                 linewidth=1.2,edgecolor="#315b78",facecolor="#f1f6f9"))
    ax.text(.5,y+h-.035,title,ha="center",va="top",fontsize=13.5,weight="bold")
    ax.text(.5,y+h-.095,formula,ha="center",va="top",fontsize=15)
    ax.text(.5,y+.025,detail,ha="center",va="bottom",fontsize=10.5)
box(.765,.19,"Initial and later high failures",
    r"$O((M+2)^{3/2-\alpha}),\quad\alpha=4c_0D^2$",
    "One rank sequence; exact endpoint exchange · (35)")
box(.54,.19,"First low timeout",
    r"$C\sqrt{\frac{(M+2)\log(M+2)}{L+1}}\;2^{-\kappa L}$",
    "Word survival, restricted times and integer fibres · (29)")
box(.315,.19,"Initial multiplier maximum",
    r"$\Pr(\max_{j\leq M}F_j>3R/7)\leq 7/(3R)$",
    "Finite stopped mean and the affine factor 7/6 · (44)")
for y in [.746,.521]:
    ax.text(.5,y,"+",ha="center",va="center",fontsize=18)
ax.annotate("",xy=(.5,.252),xytext=(.5,.30),
            arrowprops={"arrowstyle":"->","lw":1.6,"color":"#315b78"})
ax.text(.5,.268,"remove their union from the original shell",
        ha="center",va="center",fontsize=10.5,
        bbox={"facecolor":"white","edgecolor":"none","pad":1})
box(.02,.22,"One retained trajectory",
    r"$T^k(n)=\mathrm{Col}^{\,\ell}(n)=y<2^L$",
    "Both centered clocks and both maxima at most nR\n"
    "Same endpoint, including any halving tail · (41)–(43)")
fig.tight_layout(pad=.2)
out=Path(__file__).resolve().parents[1]/"figures/critical-shell.svg"
fig.savefig(out,format="svg",bbox_inches="tight")
plt.close(fig)

