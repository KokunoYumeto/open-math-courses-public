"""Original CC0 diagram for the proved local uniqueness cutoff implication."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(-1.05,1.05,801)
boundary=-x*x/2
delta=15/128
with plt.rc_context({"font.family":"DejaVu Sans","font.size":12}):
    fig=plt.figure(figsize=(14,8),dpi=150,facecolor="#fffdfa")
    fig.text(0.05,0.94,"A fixed cutoff creates a strict exponential weight gap",fontsize=21,weight="bold",color="#17374b")
    fig.text(0.05,0.885,"The full local Carleman estimate (5.7) supplies the analytic premise for the cutoff argument.",fontsize=13,color="#17374b")
    ax=fig.add_axes([0.09,0.255,0.61,0.53])
    ax.fill_between(x,-0.30,np.maximum(boundary,-0.30),color="#d7e4ed",alpha=0.8)
    ax.fill_between(x,np.maximum(boundary,-0.30),0.08,color="#fffdfa")
    ax.plot(x,boundary,color="#2178a5",lw=2.5)
    ax.axhline(-1/8,color="#a45330",lw=2,ls="--",label=r"Every error: $t\leq-1/8$")
    ax.axhline(-15/256,color="#267252",lw=2,ls="-.",label=r"Target strip: $t\geq-15/256$")
    ax.axvline(-0.5,color="#8b6094",lw=1.5,ls=":")
    ax.axvline(0.5,color="#8b6094",lw=1.5,ls=":")
    ax.scatter([-0.5,0.5],[-0.125,-0.125],c="#a45330",zorder=5)
    ax.text(-0.97,0.036,r"Given zero side: $u=0$ for $t>-x^2/2$",fontsize=12,color="#2178a5")
    ax.text(-0.45,-0.262,"Possible support below the parabola",fontsize=12,color="#344756")
    ax.annotate(r"$|x|\geq r_1=1/2$ on a spatial transition",xy=(0.5,-0.125),xytext=(0.1,-0.215),arrowprops={"arrowstyle":"->","color":"#8b6094"},fontsize=11,color="#8b6094")
    ax.set(xlim=(-1.05,1.05),ylim=(-0.3,0.08),xlabel="Transverse coordinate x",ylabel="Time coordinate t")
    ax.grid(alpha=0.12)
    ax.legend(loc="upper right",bbox_to_anchor=(1.0,-0.12),frameon=False,fontsize=11)
    for s in ax.spines.values():s.set_color("#c3cbd0")
    fig.text(0.745,0.740,r"$\phi(t)=t+t^2/2$",fontsize=15,color="#17374b")
    fig.text(0.745,0.650,r"$\phi(-1/8)=-15/128$",fontsize=14,color="#a45330")
    fig.text(0.745,0.575,r"$\delta=15/128$",fontsize=14,color="#a45330")
    fig.text(0.745,0.485,r"Errors: $e^{\tau\phi}\leq e^{-\tau\delta}$",fontsize=13,color="#a45330")
    fig.text(0.745,0.390,r"Target: $e^{\tau\phi}\geq e^{-\tau\delta/2}$",fontsize=13,color="#267252")
    fig.text(0.08,0.135,r"After (5.7) and absorption: $\|u\|_{\mathrm{target}}^2\leq C\tau^{-1}e^{-\tau\delta}\to0$ (7.4).",fontsize=14,color="#267252")
    fig.text(0.05,0.070,"Exact geometry: lesson Section 7; gamma=1/2, r1=1/2, a=1/8. These are illustrative local parameters.",fontsize=10,color="#566779")
    fig.text(0.05,0.035,"Hörmander IV, Theorem 28.1.1, pp. 220–224. Original CC0 diagram and reproducible Python source; author self-check, no independent review.",fontsize=10,color="#566779")
    fig.savefig(Path(__file__).with_name("cutoff-weight-gap.png"),dpi=150)
    plt.close(fig)
