from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 12, "svg.hashsalt": "AN01-U031-continuous-primitives"})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12.5,5.1),layout="constrained")
x=np.linspace(-2,3,2501)
s=x-np.floor(x)
p=s*(1-s)/2
axes[0].plot(x,p,color="#11768a",lw=2.5,label=r"$p(j+s)=s(1-s)/2$")
axes[0].scatter(np.arange(-2,4),np.zeros(6),color="#11768a",s=25,zorder=3)
axes[0].set(xlim=(-2.1,3.1),ylim=(-0.015,0.175),xlabel="$x$",ylabel="$p(x)$",
 title="A noncompact source of order one")
axes[0].set_xticks(np.arange(-2,4))
axes[0].set_yticks([0,.0625,.125],[r"$0$",r"$1/16$",r"$1/8$"])
axes[0].text(.5,.158,r"$p'''=\sum_{j\in\mathbb{Z}}\delta'_j$",ha="center")
axes[0].legend(loc="lower center",bbox_to_anchor=(.5,-.29),frameon=False)
x=np.linspace(-.7,1.5,1101)
for r,c in [(0,"#11768a"),(1,"#bc532b"),(2,"#6c59a2")]:
    axes[1].plot(x,np.maximum(x,0)**(r+1)/math.factorial(r+1),color=c,lw=2.5,
                 label=rf"$r={r}$")
axes[1].set(xlim=(-.7,1.5),ylim=(-.06,1.58),xlabel="$x$",ylabel="$a_r(x)$",
 title="A point source with prescribed regularity")
axes[1].text(-.57,1.36,r"$a_r(x)=x_+^{r+1}/(r+1)!$")
axes[1].text(-.57,1.16,r"$a_r^{(r+2)}=\delta_0$")
axes[1].legend(loc="lower center",bbox_to_anchor=(.5,-.29),ncol=3,frameon=False)
for ax in axes:
    ax.grid(alpha=.16)
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(out/"finite-order-continuous-primitives.png",dpi=170)
fig.savefig(out/"finite-order-continuous-primitives.svg",metadata={"Date":None})
svg=out/"finite-order-continuous-primitives.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
