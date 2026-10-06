"""Original figure by GPT-6 Astra (OpenAI), Ultra, 2026-10-06. CC0-1.0.
Reproduce the exact analytic rank-one normal form from the course proof.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[2]/"figures"
root.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.hashsalt":"SH03-analytic-normal-form-v1"})
fig,axs=plt.subplots(1,3,figsize=(13,4.5))
fig.subplots_adjust(left=.07,right=.98,bottom=.24,top=.78,wspace=.35)
colors=["#bb6519","#216394","#703b88"]
ys=np.linspace(-1.15,1.15,500)
for u,c in zip([-1,0,1],colors):
    axs[0].plot(u-ys**2-.5*ys,ys,color=c,lw=2,label=f"$u={u}$")
    axs[1].plot(u,u*u,"o",color=c,ms=8)
    axs[2].plot(u,0,"o",color=c,ms=8)
a=np.linspace(-1.25,1.25,400)
axs[1].plot(a,a*a,color="#aaa",lw=1.5,zorder=-1)
axs[2].plot([-1.25,1.25],[0,0],color="#aaa",lw=1.5,zorder=-1)
axs[0].set(xlabel="$x$",ylabel="$y$",xlim=(-2.9,1.4),ylim=(-1.2,1.2),title="Source fibres")
axs[0].legend(loc="lower left",fontsize=9)
axs[1].set(xlabel="$a$",ylabel="$b$",xlim=(-1.4,1.4),ylim=(-.2,1.8),title="Analytic image $b=a^2$")
axs[2].set(xlabel="$u$",ylabel="$w=b-a^2$",xlim=(-1.4,1.4),ylim=(-.65,.65),title="Straightened image $w=0$")
for ax in axs:
    ax.axhline(0,color="#ddd",lw=.7,zorder=-2)
    ax.axvline(0,color="#ddd",lw=.7,zorder=-2)
    ax.spines[["top","right"]].set_visible(False)
fig.suptitle("Constant rank with a fixed parameter: $\\lambda=1/2$",fontsize=17,y=.97)
fig.text(.5,.86,r"$u=x+y^2+\lambda y,\quad F_\lambda(x,y)=(u,u^2),\quad (a,b)\mapsto(a,b-a^2)$",ha="center",fontsize=13)
fig.text(.5,.09,r"Each coloured fibre maps to one point.  Source inverse: $(x,y)=(u-z^2-\lambda z,z)$.",ha="center",fontsize=12)
fig.savefig(root/"SH03-analytic-normal-form.svg",bbox_inches="tight",metadata={
    "Date":None,
    "Title":"Analytic constant rank with a fixed parameter",
    "Creator":"GPT-6 Astra (OpenAI), Ultra",
    "Description":"Exact fibres of u=x+y^2+lambda*y, their image (u,u^2), and the analytic target change w=b-a^2; lambda=1/2.",
    "Rights":"CC0 1.0 Universal; original mathematical illustration."
})

