"""Reproduce the exact schematic of PW.17–PW.18; no group is assumed metrizable."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
BOXES = [
    (0.04, 0.35, 0.20, 0.36, [r"$f \in C(G)$", r"$\delta=\Vert(L_a-I)f\Vert_2>0$"]),
    (0.34, 0.35, 0.26, 0.36, [r"$T_hf,\quad T_h=S_h^2\geq0$", r"$\Vert T_hf-f\Vert_2<\delta/4$",
                             r"$\Vert(L_a-I)T_hf\Vert_2>\delta/2$"]),
    (0.71, 0.35, 0.25, 0.36, [r"$v=P_NT_hf\in\bigoplus_{j\leq N}E_j$", r"$\Vert T_hf-v\Vert_2<\delta/8$",
                             r"$\Vert(L_a-I)v\Vert_2>\delta/4$"]),
]
fig, ax = plt.subplots(figsize=(15, 4.5))
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.axis("off")
ax.text(.5, .92, "Finite spectral detection in an arbitrary compact Hausdorff group",
        ha="center", fontsize=17, weight="bold")
for x,y,w,h,labels in BOXES:
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.012",
                               linewidth=1.4,edgecolor="#315a80",facecolor="#edf5fc"))
    for j,label in enumerate(labels):
        ax.text(x+w/2,y+h-(j+1)*h/(len(labels)+1),label,ha="center",va="center",fontsize=12)
for start,end,label in [((.25,.53),(.32,.53),"smoothing"),((.61,.53),(.69,.53),"finite truncation")]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=16,color="#315a80"))
    ax.text((start[0]+end[0])/2,.75,label,ha="center",fontsize=11)
ax.text(.5,.16,r"Some $E_j$ has $L_a|_{E_j}\ne I$;  $\rho_j(g)=L_g|_{E_j}$ is a continuous unitary matrix representation.",
        ha="center",fontsize=13)
ax.text(.5,.05,"Schematic of PW.17–PW.18.  Each Eⱼ is finite dimensional; L²(G) may be nonseparable.",
        ha="center",fontsize=11,color="#334155")
fig.savefig(OUT/"KT-KK-18-separation-mechanism.png",dpi=160,bbox_inches="tight")
fig.savefig(OUT/"KT-KK-18-separation-mechanism.svg",bbox_inches="tight")
plt.close(fig)
