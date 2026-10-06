"""Plot the exact sequence values and transporter times in lesson 64."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/"73-lemma-414-counterexample-data.json").read_text(encoding="utf-8-sig"))
ns=np.asarray(DATA["display_sequence_n"],dtype=float)
ts=np.asarray(DATA["display_transporter_n"],dtype=int)
assert ns[0]==12 and ns[-1]==80 and ts[0]==12 and ts[-1]==30
assert np.all(np.diff(ns)==1) and np.all(np.diff(ts)==1)

fig,axes=plt.subplots(1,3,figsize=(12.6,5.3),
                      gridspec_kw={"width_ratios":[1.0,1.0,1.35]},
                      facecolor="#fbfcff")
navy="#18334b";teal="#0c8390";purple="#8060a4";orange="#be6d34";muted="#566c7d"
fig.suptitle("A bounded orbit sum can jump at two limit orbits",
             fontsize=16,weight="bold",color=navy,y=.975)
for ax in axes:
    ax.set_facecolor("#fbfcff")
    ax.spines[["top","right"]].set_visible(False)
    ax.spines[["left","bottom"]].set_color("#a2b3c1")
    ax.tick_params(colors=muted,labelsize=9.5)

ax=axes[0]
ax.scatter(1/ns,np.full_like(ns,2),s=35,color=teal,alpha=.76,
           edgecolors="white",linewidth=.35,zorder=3)
ax.scatter([0],[1],s=155,color=orange,edgecolors="white",linewidth=1.1,zorder=4)
ax.set_xlim(-.007,.095);ax.set_ylim(.65,2.27)
ax.set_xticks([0,1/80,1/40,1/20,1/12])
ax.set_xticklabels(["0","1/80","1/40","1/20","1/12"])
ax.set_yticks([1,2])
ax.set_title(r"Near $a_0=(0,0)$",fontsize=12.5,color=navy,pad=12)
ax.set_xlabel("second spatial coordinate",fontsize=9.5,color=muted)
ax.set_ylabel(r"$E(1_S)$",fontsize=11,color=navy)
ax.annotate(r"$n\to\infty$",xy=(.004,2.08),xytext=(.048,2.08),
            arrowprops={"arrowstyle":"->","color":teal,"lw":1.6},
            color=teal,fontsize=10,ha="center")
ax.text(.009,.91,r"$E(1_S)(a_0)=1$",fontsize=9.5,color=orange)

ax=axes[1]
ax.scatter(1+1/ns,np.full_like(ns,2),s=35,color=purple,alpha=.76,
           edgecolors="white",linewidth=.35,zorder=3)
ax.scatter([1],[1],s=155,color=orange,edgecolors="white",linewidth=1.1,zorder=4)
ax.set_xlim(.993,1.095);ax.set_ylim(.65,2.27)
ax.set_xticks([1,1+1/20,1+1/12])
ax.set_xticklabels(["1","1+1/20","1+1/12"])
ax.set_yticks([1,2])
ax.set_title(r"Near $b_0=(0,1)$",fontsize=12.5,color=navy,pad=12)
ax.set_xlabel("second spatial coordinate",fontsize=9.5,color=muted)
ax.annotate(r"$n\to\infty$",xy=(1.004,2.08),xytext=(1.048,2.08),
            arrowprops={"arrowstyle":"->","color":purple,"lw":1.6},
            color=purple,fontsize=10,ha="center")
ax.text(1.009,.91,r"$E(1_S)(b_0)=1$",fontsize=9.5,color=orange)

ax=axes[2]
ax.scatter(ts,np.ones_like(ts),s=48,color="#3c718f",zorder=3)
ax.plot([12,30],[1,1],color="#9fbdce",lw=1.4,zorder=1)
ax.annotate("",xy=(34.0,1),xytext=(30.2,1),
            arrowprops={"arrowstyle":"-|>","color":"#3c718f","lw":2})
ax.set_xlim(10,35);ax.set_ylim(.65,1.35)
ax.set_xticks([12,18,24,30])
ax.set_yticks([])
ax.set_title(r"Every $n\geq12$ is a transporter time",fontsize=11.8,color=navy,pad=13)
ax.set_xlabel("integer group parameter n",fontsize=9.5,color=muted)
ax.text(11.5,1.20,r"$T^n(c_{n,0})=c_{n,n}\in S$",fontsize=10.5,color=navy)
ax.text(11.5,.76,"Shown 12–30; all later integers also occur.",
        fontsize=9.6,color=muted)

fig.text(.5,.035,
    r"$c_{n,0}=(0,1/n),\ c_{n,n}=(0,1+1/n),\ E(1_S)(c_{n,0})=E(1_S)(c_{n,n})=2$",
    ha="center",fontsize=10.5,color="#37556b")
fig.subplots_adjust(left=.07,right=.985,top=.82,bottom=.18,wspace=.30)
out=HERE/"73-lemma-414-counterexample.png"
fig.savefig(out,dpi=190,facecolor=fig.get_facecolor())
plt.close(fig)
print(out)
