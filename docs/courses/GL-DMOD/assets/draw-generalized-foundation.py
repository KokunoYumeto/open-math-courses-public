"""Exact algebra diagrams for NF.1/NF.5; not embeddings of a flag variety."""
from pathlib import Path
import json,argparse
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "gl-dmod-generalized-center-exact-calibration"
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
OUT = Path(args.output) if args.output else ROOT
OUT.mkdir(exist_ok=True)
data = {"type":"A1","geometric_parameter":"Lambda","HC_parameter":"-Lambda-1","Casimir":"Lambda*(Lambda+2)","regular_point":0,"regular_N":2,"regular_branch":"c=2*epsilon mod epsilon^2","inverse":"epsilon=c/2 mod c^2","singular_point":-1,"singular_relation":"c+1=delta^2","same_exponent_N2_image":"c+1 maps to 0 mod delta^2","weight_space_basis":["w_1","z_0"],"h_matrix":[[-2,0],[0,-2]],"C_matrix":[[0,4],[0,0]],"epsilon_matrix":[[0,2],[0,0]],"diagram_status":"Exact ring maps and one weight-space central action; not a full U-submodule diagram","proof_locators":["beilinson-bernstein-localization.html#nf-proof-1","beilinson-bernstein-localization.html#nf-proof-5","beilinson-bernstein-localization.html#5-two-orbits-and-two-highest-weight-simples"],"free_human_comparison":"https://arxiv.org/html/1209.0188v2 Remark1.2(4)","licence":"CC0-1.0"}
(OUT / "generalized-foundation-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")

def box(ax,x,y,w,h,text,edge="#2b607f"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.015",facecolor="#f4f8fa",edgecolor=edge,linewidth=1.6))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=13,linespacing=1.5)
def arrow(ax,start,end,label,yoff=.02):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":"#21647b","lw":1.8})
    ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+yoff,label,ha="center",va="bottom",fontsize=12,color="#164e66")

fig,ax=plt.subplots(figsize=(13,7.5));ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ax.text(.5,.96,"Regular finite branch retains the nilpotent center",ha="center",fontsize=19,weight="bold")
ax.text(.5,.905,r"Type $A_1$: $c=\Lambda(\Lambda+2)$, $\tau=-\Lambda-1$; regular point $\lambda=0$, $N=2$",ha="center",fontsize=13)
box(ax,.06,.64,.32,.18,r"$Z/(c^2)=\mathbf{C}[c]/(c^2)$"+"\ncentral thickening")
box(ax,.62,.64,.32,.18,r"$A/(\Lambda^2)=\mathbf{C}[\varepsilon]/(\varepsilon^2)$"+"\nselected parameter branch")
arrow(ax,(.39,.74),(.61,.74),r"$c\mapsto2\varepsilon$",.025)
arrow(ax,(.61,.67),(.39,.67),r"$\varepsilon\mapsto c/2$",-.055)
ax.text(.5,.50,r"The other residue point $\Lambda=-2$ is a separate formal branch, not an extra object in this selected category.",ha="center",fontsize=12)
ax.plot([.06,.94],[.45,.45],color="#abbec8",lw=1)
ax.text(.5,.40,"Singular boundary: the same-exponent identification fails",ha="center",fontsize=16,weight="bold")
box(ax,.06,.13,.32,.18,r"$Z/((c+1)^2)$"+"\n$\\lambda=-1$",edge="#966148")
box(ax,.62,.13,.32,.18,r"$A/((\Lambda+1)^2)$"+"\n$\\delta=\\Lambda+1$, $\\delta^2=0$",edge="#966148")
arrow(ax,(.39,.22),(.61,.22),r"$c+1\mapsto\delta^2=0$",.02)
ax.text(.5,.07,"The map kills a nonzero source nilpotent. Singular generalized localization needs its own ramified construction.",ha="center",fontsize=12)
fig.text(.5,.015,"Exact algebra maps; proof NF.1. Free formal-neighborhood comparison: Ben-Zvi–Nadler, Remark 1.2(4).",ha="center",fontsize=10)
fig.savefig(OUT/"generalized-foundation-regular-branch.png",dpi=180,bbox_inches="tight")
fig.savefig(OUT/"generalized-foundation-regular-branch.svg",bbox_inches="tight",metadata={"Date":None})
plt.close(fig)

fig,ax=plt.subplots(figsize=(12,6));ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ax.text(.5,.95,"Semisimple Cartan, nonzero nilpotent center",ha="center",fontsize=19,weight="bold")
ax.text(.5,.87,r"One weight space in the generalized principal module of BB §5: $V_{-2}=\mathbf{C}w_1\oplus\mathbf{C}z_0$",ha="center",fontsize=13)
box(ax,.05,.59,.28,.19,r"$h=-2\,\mathrm{id}$"+"\nCartan is semisimple")
box(ax,.36,.59,.28,.19,r"$Cw_1=0$, $Cz_0=4w_1$"+"\n$C^2=0$, $C\\neq0$")
box(ax,.67,.59,.28,.19,r"$\varepsilon=C/2$"+"\n$\\varepsilon z_0=2w_1\\neq0$")
box(ax,.12,.23,.27,.17,r"$z_0$",edge="#5a8a62")
box(ax,.61,.23,.27,.17,r"$w_1$",edge="#5a8a62")
arrow(ax,(.40,.335),(.60,.335),r"$C: z_0\mapsto4w_1$",.025)
arrow(ax,(.40,.26),(.60,.26),r"$\varepsilon: z_0\mapsto2w_1$",-.06)
ax.text(.5,.14,r"A single exact $\mathcal{D}_0$ would force $C=0$ and lose this action. $\mathcal{D}_{0,2}$ retains it.",ha="center",fontsize=13)
fig.text(.5,.04,"This panel displays only h and the central action on one weight space; that space is not a U-submodule.\nComplete arbitrary-rank argument: NF.5. Full rank-one module formulas: BB §5.",ha="center",fontsize=10)
fig.savefig(OUT/"generalized-foundation-nilpotent-module.png",dpi=180,bbox_inches="tight")
fig.savefig(OUT/"generalized-foundation-nilpotent-module.svg",bbox_inches="tight",metadata={"Date":None})
plt.close(fig)
print("Rendered two exact algebra/calibration diagrams and source data.")
