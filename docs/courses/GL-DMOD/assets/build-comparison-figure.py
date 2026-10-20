"""Reproducible exact-coordinate diagram for the ordinary and microlocal maps."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
root=Path(__file__).resolve().parent
out=root if root.name=="assets" else root/"assets"
out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
 "svg.hashsalt":"incidence-evaluation-comparison-v1","axes.titlesize":15})
fig=plt.figure(figsize=(15,10),layout="constrained")
gs=fig.add_gridspec(2,2,height_ratios=[1,1.05])
ax=fig.add_subplot(gs[0,:]);ax.set(xlim=(0,10),ylim=(0,5));ax.axis("off")
ax.set_title("A. Global closed evaluations and the actual proper trace",loc="left",weight="bold")
boxes=[
(.35,3.65,r"$a_N=D_t^N a,\quad b$"+"\nclosed projective incidences", "#dcebf6"),
(6.0,3.65,r"$h_N\ \mapsto\ D_t^N h$"+"\nactual proper operator convolution","#dcebf6"),
(.35,.65,r"$\alpha(a_N)\circ_\mu\alpha(b)$"+"\nfull relative-support composition","#e9e2f6"),
(6.0,.65,r"$\alpha(\mathrm{ev}_{h_N}\theta_{\rm raw})$"+"\nordinary evaluation, then microlocalization","#e9e2f6")]
for x,y,label,color in boxes:
    ax.text(x,y,label,va="center",ha="left",bbox=dict(boxstyle="round,pad=.6",fc=color,ec="#56718a"))
def arrow(start,end,label,xy):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=15,lw=1.5,color="#344b63"))
    ax.text(*xy,label,ha="center",va="center",fontsize=12)
arrow((3.25,3.65),(5.7,3.65),"ordinary trace: PE.13",(4.45,4.15))
arrow((1.7,2.95),(1.7,1.4),"MC.1–MC.3",(.77,2.15))
arrow((7.7,2.95),(7.7,1.4),r"$\alpha$",(8.05,2.15))
arrow((3.85,.65),(5.7,.65),"MC.4",(4.75,1.1))
ax.text(5,2.25,"Middle diagonal: real shift 2N, positive Thom class.\n"
        "Holomorphic trace: degree lowering N; all complements retained.",
        ha="center",va="center",fontsize=13,color="#253b52")
left=fig.add_subplot(gs[1,0]);left.set(xlim=(-2.4,2.4),ylim=(-2.6,2.1),
 xlabel=r"$x$",ylabel=r"$t$");left.grid(alpha=.2)
left.set_title("B. A fixed-covector shear slice",loc="left",weight="bold")
# Exact slice d=1, H=2, tau=1, xi=1/2, hence x'=x+1, t'=t-1/4.
points=[(-1,1),(0,0),(.5,-1)]
for x,t in points:
    left.plot(x,t,"o",color="#266b98");left.plot(x+1,t-.25,"o",color="#934b9f")
    left.annotate("",xy=(x+1,t-.25),xytext=(x,t),arrowprops=dict(arrowstyle="->",color="#596778"))
left.text(-2.2,-2.1,r"$H=2,\ \tau=1,\ \xi=1/2$"+"\n"+
          r"$x'=x+1,\quad t'=t-1/4$",fontsize=13)
right=fig.add_subplot(gs[1,1]);right.set(xlim=(0,1),ylim=(0,1));right.axis("off")
right.set_title("C. Intrinsic inverse and whole-ring transport",loc="left",weight="bold")
right.text(.04,.88,r"$ab=\lambda\,1_X,\quad ba=\lambda\,1_Y$"+"\n"+
           r"$\lambda\in\mathbb{C}^\times,\quad b_{\rm inv}=\lambda^{-1}b$",
           va="top",fontsize=15)
right.text(.04,.60,r"$\Phi(Q)=aQb_{\rm inv},\quad Q\in C_Y$"+"\n\n"+
           r"$\Phi|_B=\mathcal{L}_0,\quad\mathscr{T}_H=\Phi\Theta_H\Phi^{-1}$",
           va="top",fontsize=15)
right.text(.04,.23,"IN.2–IN.3: finite localized diagonal endomorphisms.\n"
           "WT.1–WT.4: proper graph supports, full cubes,\n"
           "inverse products and balanced module maps.",va="top",fontsize=12)
data={"figure":"incidence-evaluation-and-real-transport",
 "diagram_locators":["GP.4–GP.13","PE.13","MC.1–MC.4","IN.2–IN.3","WT.1–WT.4"],
 "slice":{"d":1,"H":[[2]],"tau":"1","xi":["1/2"],"z":["1/2"],
          "x_translation":["1"],"t_translation":"-1/4",
          "points":[{"x":str(x),"t":str(t),"image_x":str(x+1),"image_t":str(t-.25)}for x,t in points]},
 "slice_scope":"Fixed covector real base slice of the full homogeneous symplectic map, not its whole phase space.",
 "lambda":"Unique nonzero scalar of the actual canonical products; no raw numerical value is claimed."}
(out/"incidence-evaluation-and-real-transport-exact-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
fig.savefig(out/"incidence-evaluation-and-real-transport.png",dpi=170)
fig.savefig(out/"incidence-evaluation-and-real-transport.svg",metadata={"Date":None})
plt.close(fig)
print(json.dumps({"outputs":3,"slice_exact":True}))
