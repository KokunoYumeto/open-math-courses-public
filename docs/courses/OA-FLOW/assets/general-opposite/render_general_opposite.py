"""Two exact M2 examples for finite-domain support and right-bounded vectors."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-general-opposite-20261008-v1"

d=Path(__file__).resolve().parent
fig, axes=plt.subplots(1,3,figsize=(14.8,5.4))
fig.subplots_adjust(left=.055,right=.985,top=.78,bottom=.26,wspace=.31)
fig.suptitle("The support restriction is part of the opposite-weight construction",
             fontsize=18,fontweight="bold",y=.98)
fig.text(.5,.895,"First two panels: real coordinate slices of the complex GNS space H = C².",
         ha="center",fontsize=12)
for ax in axes[:2]:
    ax.set_xlim(-1.35,1.4);ax.set_ylim(-1.25,1.4)
    ax.set_aspect("equal")
    ax.axhline(0,color="#176d80",lw=3)
    ax.axvline(0,color="#aab5bc",lw=.9)
    ax.set_xlabel(r"$\mathrm{Re}\,\eta_1$");ax.set_ylabel(r"$\mathrm{Re}\,\eta_2$")
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(alpha=.15)
ax=axes[0]
ax.set_title(r"A. Vector state: $\varphi(a)=a_{11}$",fontsize=12)
ax.annotate("",xy=(1,0),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",lw=2.5,color="#176d80"))
ax.annotate("",xy=(0,1),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",lw=2.5,color="#b65d1d"))
ax.text(.73,.15,r"$e_1\in\mathcal{B}$",color="#176d80",fontsize=12)
ax.text(.1,1.13,r"$e_2\notin\mathcal{B}$",color="#b65d1d",fontsize=12)
ax.text(.05,-.24,r"$e=I,\quad \mathcal{B}=H_0=\mathbb{C} e_1$"
        "\n" r"$E_{12}e_1=0,\qquad E_{12}e_2=e_1$",
        transform=ax.transAxes,fontsize=12,va="top")

ax=axes[1]
ax.set_title("B. Weight finite only on the p-corner",fontsize=12)
ax.axvline(0,color="#b65d1d",lw=2,ls="--")
ax.scatter([1,1],[0,1],s=60,color=["#176d80","#b65d1d"],zorder=5)
ax.annotate("",xy=(1,.08),xytext=(1,.92),arrowprops=dict(arrowstyle="-|>",lw=2,color="#687a84",ls="--"))
ax.text(.12,1.16,r"$(1,1)\mapsto I$",color="#b65d1d",fontsize=12)
ax.text(.2,-.23,r"$(1,0)\mapsto I$",color="#176d80",fontsize=12)
ax.text(-1.2,.4,"Kernel of the\nunrestricted map",fontsize=10,color="#b65d1d")
ax.text(.05,-.24,r"$e=p,\quad R_\eta=\eta_1 I$"
        "\n" r"Restrict to $EH=\mathbb{C} e_1$ for injectivity.",
        transform=ax.transAxes,fontsize=12,va="top")

ax=axes[2]
ax.set_title(r"B. Take $f(a)=\operatorname{Tr}(a)\leq\varphi(a)$",fontsize=12)
ax.bar([0,1,2],[1,1,2],color=["#176d80","#578e70","#b65d1d"],width=.63)
for k,v in enumerate([1,1,2]):ax.text(k,v+.05,str(v),ha="center",fontsize=15,fontweight="bold")
ax.set_xticks([0,1,2],[r"$\rho(t_f)$",r"$f(e)$",r"$\|f\|=f(I)$"],fontsize=12)
ax.set_ylim(0,2.45);ax.set_yticks([0,1,2]);ax.set_ylabel("Exact value")
ax.grid(axis="y",alpha=.18)
ax.text(.5,-.24,r"$t_f=I,\qquad \rho(I)=1=f(p)$"
        "\n" r"$f(I)=2$ includes the other corner.",
        transform=ax.transAxes,ha="center",fontsize=12,va="top")
fig.savefig(d/"assets"/"general-opposite-support.png",dpi=180,bbox_inches="tight")
fig.savefig(d/"assets"/"general-opposite-support.svg",bbox_inches="tight",metadata={"Date": None})
plt.close(fig)
(d/"general-opposite-figure-numerics.json").write_text(json.dumps({
 "scope":"Exact finite-dimensional examples; first two panels are explicitly real coordinate slices of C2",
 "vector_state":{"finite_domain_projection":[[1,0],[0,1]],"right_bounded_vectors":"C e1","rho_identity":1},
 "finite_corner_weight":{"finite_domain_projection":[[1,0],[0,0]],"right_multiplier_unrestricted":"eta_1 I",
 "unrestricted_kernel":"C e2","supported_vectors":"C e1","t_trace":1,"rho_t_trace":1,"trace_at_e":1,"trace_norm":2}
},indent=2)+"\n",encoding="utf-8")
