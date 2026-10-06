from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13.5,7.5),dpi=180)
fig.patch.set_facecolor("white")
ax.set_xlim(0,13.5);ax.set_ylim(0,7.5);ax.axis("off")
blue="#d7e9fa"; coral="#fae2dc"; ink="#1c3143"; accent="#145d8d"

def box(x,y,w,h,label,color,fs=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.08,rounding_size=0.12",
                                linewidth=1.5,edgecolor=ink,facecolor=color))
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=fs,color=ink)

def arrow(x1,y1,x2,y2,label="",dy=0.22):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=18,
                                 linewidth=1.7,color=accent))
    if label:
        ax.text((x1+x2)/2,(y1+y2)/2+dy,label,ha="center",va="bottom",fontsize=13,color=ink)

ax.text(6.75,7.05,"Actual finite normal Laurent correction",ha="center",fontsize=20,weight="bold",color=ink)
ax.text(6.75,6.65,"Complete tangential products; both signed normal tails and separated kernels are retained",
        ha="center",fontsize=11.5,color=ink)

box(0.55,5.1,2.25,0.78,r"$E_Y$",blue,17)
box(5.63,5.1,2.25,0.78,r"$F_Y$",coral,17)
arrow(2.93,5.49,5.50,5.49,r"$P_c=\sum_{j=0}^{m}A_j(r)D_r^j$")
arrow(5.52,4.94,2.94,4.94,r"$Q\in\mathcal{L}^{-m},\quad C_0=M^{-1}$",dy=-0.36)

box(0.55,3.43,5.55,0.9,r"$\mathcal{R}_E=QP_c-I_E\quad(E_Y\to E_Y)$",blue,13)
box(7.36,3.43,5.55,0.9,r"$\mathcal{R}_F=P_cQ-I_F\quad(F_Y\to F_Y)$",coral,13)
ax.text(6.75,3.13,r"$\mathcal{R}_EQ=Q\mathcal{R}_F$",ha="center",fontsize=12,color=ink)

box(2.00,1.80,9.50,0.96,
    r"$Q_N=\sum_{j=0}^{N-1}(-\mathcal{R}_E)^jQ"
    r"=Q\sum_{j=0}^{N-1}(-\mathcal{R}_F)^j$",
    "#edf2e1",13)
arrow(3.32,3.30,4.18,2.88)
arrow(10.04,3.30,9.28,2.88)
ax.text(6.75,1.13,
        r"$Q_N:F_Y\to E_Y$ has coefficients $C_0,\ldots,C_{N-1}$;"
        r" errors $-(-\mathcal{R}_F)^N$ and $-(-\mathcal{R}_E)^N$",
        ha="center",fontsize=11.8,color=ink)
ax.text(6.75,0.46,
        "Actual composition and full remainders: NC1–NC9. Half-space and all measured layer maps: MH1–MH20.",
        ha="center",fontsize=10.8,color=ink)
fig.savefig(out/"normal_composition_actual_166.png",bbox_inches="tight",facecolor="white")
fig.savefig(out/"normal_composition_actual_166.svg",bbox_inches="tight",facecolor="white")
plt.close(fig)
