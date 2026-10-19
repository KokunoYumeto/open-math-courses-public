"""Laplace contours and convex carriers, exact examples from U113.

Original figure: GPT-6 Astra (OpenAI), 2026. CC0.
Lemma 2, Theorem 4 and Exercise 5 give the mathematical arguments.
Requires NumPy and Matplotlib. Outputs are written beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"svg.fonttype":"none"})
blue,red,green="#1768a5","#b33a3a","#27835d"
fig,axs=plt.subplots(3,1,figsize=(8,12),constrained_layout=True)
ax=axs[0]
ax.plot([-1,1],[0,0],color=blue,lw=4,label=r"$I=[-1,1]$")
rect=np.array([[-1.25,-.25],[1.25,-.25],[1.25,.25],[-1.25,.25],[-1.25,-.25]])
ax.plot(rect[:,0],rect[:,1],color=green,lw=2,label=r"$\gamma$: margin $1/4$")
ax.annotate("",xy=(.4,-.25),xytext=(-.2,-.25),arrowprops={"arrowstyle":"->","color":green,"lw":2})
ax.scatter([.4],[.8],color=red,zorder=4)
ax.text(.48,.8,r"$z=2/5+4i/5$",va="center",color=red)
ax.set(xlim=(-1.5,1.7),ylim=(-.55,1.08),xlabel=r"$\mathrm{Re}\ z$",ylabel=r"$\mathrm{Im}\ z$",title="Test-variable plane — a small contour around the real carrier")
ax.legend(loc="upper left")
ax=axs[1]
angles=np.deg2rad([-105,-75])
for theta,label in zip(angles,["-105","-75"]):
 endpoint=2*np.array([np.cos(theta),np.sin(theta)])
 ax.annotate("",xy=endpoint,xytext=(0,0),arrowprops={"arrowstyle":"->","color":blue,"lw":2.5})
 ax.text(endpoint[0]*1.4,endpoint[1]*.9,r"$"+label+r"^\circ$",ha="center",color=blue)
t=np.linspace(angles[0],angles[1],101)
ax.plot(np.cos(t),np.sin(t),color=green,lw=3)
ax.text(.05,-.7,"admissible arc",color=green)
ax.scatter([0],[0],color="black",s=20)
ax.set(xlim=(-1.45,1.45),ylim=(-2.15,.25),xlabel=r"$\mathrm{Re}\ t$",ylabel=r"$\mathrm{Im}\ t$",title="Laplace-variable plane — rotation retains a positive gap")
ax.set_aspect("equal",adjustable="box")
ax=axs[2]
ax.add_patch(Polygon([[0,0],[1,0],[1,1],[0,1]],closed=True,fill=False,edgecolor=blue,lw=2,label=r"$B_0$"))
ax.add_patch(Polygon([[-.5,.5],[.5,-.5],[1,0],[0,1]],closed=True,fill=False,edgecolor=green,lw=2,label=r"$B_1$"))
ax.add_patch(Polygon([[0,0],[1,0],[0,1]],closed=True,facecolor=blue,alpha=.18))
ax.text(.2,.22,r"$K=B_0\cap B_1$",color=blue)
ax.scatter([.75],[.75],color=red,zorder=5)
ax.text(.81,.8,r"$q=(3/4,3/4)$",color=red)
ax.scatter([.5],[.5],color="black",s=18,zorder=4)
ax.plot([.5,.75],[.5,.75],color=red,ls="--")
ax.set(xlim=(-.62,1.58),ylim=(-.62,1.16),xlabel=r"$x$",ylabel=r"$y$",title="Real carrier plane — rotated boxes remove extra corners")
ax.set_aspect("equal",adjustable="box")
ax.legend(loc="upper left")
for ax in axs:
 ax.spines[["top","right"]].set_visible(False)
 ax.grid(alpha=.15)
fig.savefig(out/"laplace-rays-and-convex-carriers.svg")
svg=out/"laplace-rays-and-convex-carriers.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
fig.savefig(out/"laplace-rays-and-convex-carriers.png",dpi=170)
plt.close(fig)
