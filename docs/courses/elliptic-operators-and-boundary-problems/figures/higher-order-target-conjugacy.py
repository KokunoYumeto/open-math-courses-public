"""Exact operator square for AR37a--AR38; Codex, CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
base=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":17,"svg.fonttype":"none"})
fig,ax=plt.subplots(figsize=(10,5));ax.set(xlim=(0,10),ylim=(0,7));ax.axis("off")
def text(x,y,t):ax.text(x,y,t,ha="center",va="center",bbox={"facecolor":"white","edgecolor":"none","pad":5})
def arrow(p,q,t,pos):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle="->",mutation_scale=22,linewidth=2,color="#164b7a"));text(*pos,t)
text(2,5.5,r"$\mathcal{E}|_C$");text(8,5.5,r"$\mathcal{E}|_C$")
text(2,2.3,r"$\mathcal{F}|_C$");text(8,2.3,r"$\mathcal{F}|_C$")
arrow((3,5.5),(7,5.5),r"$C_\sigma$",(5,6.15));arrow((3,2.3),(7,2.3),r"$M_\sigma$",(5,1.65))
arrow((2,4.9),(2,2.9),r"$J_c$",(1.1,3.9));arrow((8,4.9),(8,2.9),r"$J_c$",(8.9,3.9))
text(5,.55,r"$M_\sigma=J_cC_\sigma J_c^{-1}$; $M_0=I$ outside the collar")
ax.set_title("The exact target map on collar sections",fontsize=19,pad=13)
fig.text(.5,.01,"Proof: editorial AR37a--AR38.",ha="center",fontsize=11)
fig.tight_layout(rect=(0,.035,1,1));fig.savefig(base/"higher-order-target-conjugacy.svg",bbox_inches="tight");fig.savefig(base/"higher-order-target-conjugacy.png",dpi=170,bbox_inches="tight")
