"""Exact smooth cutoff and boundary carriers for AN01-U106, Lemma1/Theorem2.
GPT-6 Astra (OpenAI), Ultra, October 2026. CC0.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
OUT=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"svg.fonttype":"none",
                     "axes.spines.top":False,"axes.spines.right":False})
fig,axes=plt.subplots(1,2,figsize=(12.5,6.5))
fig.subplots_adjust(left=.085,right=.96,bottom=.22,top=.79,wspace=.38)
fig.suptitle("Which boundary survives fiber integration?",fontsize=20,y=.96)
fig.text(.5,.90,"The contour is fixed at the fiber faces; the remaining carrier lies over the output boundary.",
         ha="center",fontsize=12)
ax=axes[0];ax.set_title("Real product and carrier",fontweight="bold",pad=14)
ax.add_patch(Rectangle((-1,-2.5),2,5,facecolor="#eff5fa",edgecolor="none"))
ax.add_patch(Rectangle((-1,-1),2,2,facecolor="#cfe1f0",edgecolor="none"))
for x in [-1,1]:ax.plot([x,x],[-2.5,2.5],color="#9a3526",lw=3)
for y in [-2.5,2.5]:ax.plot([-1,1],[y,y],color="#18734d",lw=3)
for y in [-2,2]:ax.plot([-1,1],[y,y],color="#63798a",ls="--",lw=1)
ax.text(0,0,r"$\chi=1$",ha="center",va="center",fontsize=15,color="#205c86")
ax.text(0,2.23,r"$\chi=0$",ha="center",fontsize=12,color="#18734d")
ax.text(0,-2.36,r"$\chi=0$",ha="center",fontsize=12,color="#18734d")
ax.annotate(r"$K_0$",xy=(1,1.3),xytext=(1.23,1.3),color="#9a3526",
            arrowprops={"arrowstyle":"-","color":"#9a3526"})
ax.text(0,2.82,"fixed fiber face",ha="center",color="#18734d")
ax.text(0,-3.18,"fixed fiber face",ha="center",color="#18734d")
ax.set(xlim=(-1.65,1.65),ylim=(-3.4,3.4),xlabel=r"output $x$",ylabel=r"fiber $y$")
ax.set_xticks([-1,0,1]);ax.set_yticks([-2.5,-2,-1,0,1,2,2.5])
ax.text(.5,-.27,r"$p(K_0)=\{-1,1\}=\partial V$",transform=ax.transAxes,
        ha="center",fontsize=13)

ax=axes[1];ax.set_title("Exact contour heights",fontweight="bold",pad=14)
y=np.linspace(-2.5,2.5,1401)
def bump(t):
    out=np.zeros_like(t);idx=t>0;out[idx]=np.exp(-1/t[idx]);return out
a=bump(2-np.abs(y));b=bump(np.abs(y)-1);chi=a/(a+b)
ax.axhline(0,color="#a4afb8",lw=1)
ax.fill_between(y,0,.25*chi,color="#d9e8f4",alpha=.8)
ax.plot(y,.25*chi,lw=2.5,color="#246d9a",label=r"fiber: $\epsilon\beta\chi=\chi/4$")
ax.plot(y,.125*chi,lw=2.5,color="#9b4a16",label=r"base: $\epsilon\alpha\chi=\chi/8$")
for v in [-2,2]:ax.axvline(v,color="#a4afb8",ls="--",lw=1)
ax.set(xlim=(-2.6,2.6),ylim=(-.035,.34),xlabel=r"real fiber $y$",ylabel="imaginary displacement")
ax.set_xticks([-2.5,-2,-1,0,1,2,2.5],["−2.5","−2","−1","0","1","2","2.5"])
ax.set_yticks([0,.125,.25],["0","1/8","1/4"])
ax.legend(loc="upper center",frameon=False,fontsize=11)
ax.text(.5,-.27,"Both displacements vanish near the fiber faces.",transform=ax.transAxes,
        ha="center",fontsize=12)
for ext in ["svg","png"]:fig.savefig(OUT/("fixed-fiber-boundary."+ext),dpi=160,facecolor="white")
svg=OUT/"fixed-fiber-boundary.svg"
svg.write_bytes(("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n").encode())
plt.close(fig)
