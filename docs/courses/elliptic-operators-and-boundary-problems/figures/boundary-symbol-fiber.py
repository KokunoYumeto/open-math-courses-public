"""Exact diagrams for BR42a--BR43a, dedicated to CC0 1.0 by Codex."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
base=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":15,"svg.fonttype":"none"})
fig,axs=plt.subplots(1,2,figsize=(12,4.8))
for ax in axs:ax.set(xlim=(0,10),ylim=(0,7));ax.axis("off")
def label(ax,x,y,text):ax.text(x,y,text,ha="center",va="center",bbox={"facecolor":"white","edgecolor":"none","pad":5})
def arrow(ax,p,q,text,pos):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle="->",mutation_scale=19,color="#164b7a",linewidth=2))
 label(ax,*pos,text)
a=axs[0];a.set_title("Every symbol with the same stable restriction",fontsize=15,pad=16)
label(a,2,5,r"$L(P)$");label(a,2,2,r"$K(P)$");label(a,8,3.5,r"$\pi^*G$")
arrow(a,(3,5),(7,3.7),r"$\beta$",(5,5.15));arrow(a,(3,2),(7,3.3),r"$c$",(5,1.9))
label(a,5,.35,r"$b=\beta q+c(I-q)$")
a=axs[1];a.set_title("An arrow between two stable data objects",fontsize=15,pad=16)
label(a,1.5,5.3,r"$L(P)$");label(a,8.4,5.3,r"$\pi^*G$");label(a,1.5,1.8,r"$L(P)$");label(a,8.4,1.8,r"$\pi^*G_1$")
arrow(a,(2.5,5.3),(7.3,5.3),r"$\beta$",(5,6));arrow(a,(2.5,1.8),(7.3,1.8),r"$\beta_1$",(5,1.05))
arrow(a,(1.5,4.7),(1.5,2.4),r"$I_L$",(.65,3.5));arrow(a,(8.4,4.7),(8.4,2.4),r"$\pi^*h$",(9.1,3.5))
fig.text(.5,.015,"Exact proof: editorial BR42a--BR43a.",ha="center",fontsize=11)
fig.tight_layout(rect=(0,.045,1,1))
fig.savefig(base/"boundary-symbol-fiber.svg",bbox_inches="tight")
fig.savefig(base/"boundary-symbol-fiber.png",dpi=170,bbox_inches="tight")
