"""CC0-1.0: original exact mathematical figure; no source figure is adapted."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-positive-parameter-state-profiles-20261009-v1"
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 13, "axes.titlesize": 16, "axes.labelsize": 14})
fig, (left, right) = plt.subplots(1, 2, figsize=(14, 5.7))
lam = 1/4
left.step([.25,.5,1], [4/3,4/3,4/3], where="post", color="#1f5a85",
          linewidth=3, label=r"$F_{\lambda}=4/3$")
left.step([.25,.5,1], [8/3,2/3,2/3], where="post", color="#b94723",
          linewidth=3, label=r"$F_{\sqrt{\lambda}}$")
left.scatter([.5],[8/3],s=45,facecolors="white",edgecolors="#b94723",zorder=6)
left.scatter([.5],[2/3],s=45,color="#b94723",zorder=6)
left.scatter([1],[4/3],s=45,facecolors="white",edgecolors="#1f5a85",zorder=6)
left.scatter([1],[2/3],s=45,facecolors="white",edgecolors="#b94723",zorder=6)
left.fill_between([.25,.5],4/3,8/3,color="#b94723",alpha=.18)
left.fill_between([.5,1],2/3,4/3,color="#1f5a85",alpha=.18)
left.text(.365,1.94,r"area $1/3$",ha="center")
left.text(.75,1.00,r"area $1/3$",ha="center")
left.text(.37,2.80,r"$8/3$",ha="center",color="#b94723")
left.text(.75,.45,r"$2/3$",ha="center",color="#b94723")
left.set(xlim=(.23,1.02),ylim=(0,3.13),
         xticks=[.25,.5,1],xticklabels=[r"$\lambda=1/4$",r"$\sqrt{\lambda}=1/2$","1"],
         yticks=[0,2/3,4/3,8/3],yticklabels=["0",r"$2/3$",r"$4/3$",r"$8/3$"],
         xlabel=r"threshold $t$",ylabel=r"spectral-tail trace $F(t)$",
         title=r"Two unit-mass profiles on $[\lambda,1)$")
left.legend(loc="upper right",frameon=False,fontsize=12)
left.grid(axis="y",alpha=.15)
ratio = np.linspace(1,4,600)
dist = 2/(1-lam)*(1+lam-1/ratio-lam*ratio)
right.plot(ratio,dist,color="#573d89",lw=3)
right.scatter([2],[2/3],s=65,color="#b94723",zorder=5)
right.axvline(2,color="#b94723",ls="--",alpha=.5)
right.axhline(2/3,color="#b94723",ls="--",alpha=.5)
right.annotate(r"$R=\lambda^{-1/2}=2$"+"\n"+r"$D=2/3$",
               (2,2/3),xytext=(2.42,.48),
               arrowprops={"arrowstyle":"->","color":"#b94723"},color="#b94723")
right.text(2.50,.16,r"$D(R)=\frac{2}{1-\lambda}(1+\lambda-R^{-1}-\lambda R)$",
           ha="center",fontsize=14)
right.set(xlim=(.95,4.05),ylim=(-.035,.78),xticks=[1,2,4],
          yticks=[0,1/3,2/3],yticklabels=["0",r"$1/3$",r"$2/3$"],
          xlabel=r"phase ratio $R=b/a$",ylabel=r"$\|F_a-F_b\|_{L^1[\lambda,1]}$",
          title="The sharp pairwise bound")
right.grid(alpha=.15)
right.text(2.5,-.025,"Endpoint R=4 shown by continuous extension.",ha="center",fontsize=10)
fig.suptitle(r"Normal-state orbit diameter via spectral profiles: $\lambda=1/4$",fontsize=19,y=.99)
fig.text(.5,.035,
         r"At the compact-core hypotheses: $d(\phi,\psi)=\|f_\phi-f_\psi\|_1$; "
         r"every profile is a probability mixture of the $F_a$.",
         ha="center",fontsize=13)
fig.subplots_adjust(bottom=.19,top=.84,wspace=.25)
fig.savefig(OUT/"positive-lambda-state-profiles.png",dpi=180,facecolor="white")
fig.savefig(OUT/"positive-lambda-state-profiles.svg",facecolor="white",metadata={"Date": None})
print({"png":str(OUT/"positive-lambda-state-profiles.png"),
       "svg":str(OUT/"positive-lambda-state-profiles.svg")})
