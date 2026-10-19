from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
fig,axs=plt.subplots(1,3,figsize=(13.4,4.8),layout="constrained")
ax=axs[0]
ax.axhline(0,color="#536779",lw=1)
ax.axvline(0,color="#536779",lw=1,alpha=.4)
t=-.05; samples=[.05,.15,.45,1.35]
ax.plot(t,0,"o",color="#b34d32",ms=7)
for k,y in enumerate(samples):
 ax.plot(y,0,"o",color="#237c85",ms=6)
 arrow=FancyArrowPatch((t,.03),(y,.03),connectionstyle=f"arc3,rad={-.35-.12*k}",arrowstyle="->",mutation_scale=10,color="#237c85",lw=1.2)
 ax.add_patch(arrow)
 ax.annotate(str(k),(y,0),xytext=(0,-17),textcoords="offset points",ha="center")
ax.axvline(2,color="#a75d35",ls="--",lw=1.3)
ax.text(.95,.67,r"$q^k|t|$ for $k=0,1,2,3$",ha="center")
ax.text(-.22,-.22,r"$t=-0.05$",ha="left",fontsize=10)
ax.text(1.96,-.22,"cutoff",ha="center",fontsize=10)
ax.text(.95,-.45,"Signed weighted samples on the positive side",ha="center",fontsize=9)
ax.set(xlim=(-.28,2.2),ylim=(-.55,.95),title="Reflection through one boundary",xlabel="Normal coordinate")
ax.set_yticks([]);ax.set_xticks([0,.5,1,1.5,2])
ax=axs[1];t=np.linspace(-1.6,1.6,401)
ax.plot(t,t*t,color="#237c85",lw=2);ax.axhline(1,color="#b34d32",ls="--")
ax.plot([-1,1],[1,1],"o",color="#b34d32")
ax.text(0,1.1,"same square value",ha="center",fontsize=10)
ax.set(xlabel=r"$t$",ylabel=r"$r=t^2$",title="The square coordinate",ylim=(-.1,2.7))
ax.grid(alpha=.18)
ax=axs[2];s=np.linspace(-2.7,2.7,401);p=s*s/4
ax.fill_between(s,-1.5,p,color="#cce5e4");ax.plot(s,p,color="#237c85",lw=2)
ax.text(0,-.7,r"$p\leq s^2/4$",ha="center",fontsize=14)
ax.text(0,1.75,"unattained region",ha="center",fontsize=10)
ax.text(1.5,1.15,r"$x=y$",fontsize=11)
ax.set(xlim=(-2.7,2.7),ylim=(-1.5,2.2),xlabel=r"$s=x+y$",ylabel=r"$p=xy$",title="The exchange-invariant image")
ax.grid(alpha=.15)
root=Path(__file__).parent
fig.savefig(root/"smooth-extension-and-folds.png",dpi=180)
fig.savefig(root/"smooth-extension-and-folds.svg")
svg=root/"smooth-extension-and-folds.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
