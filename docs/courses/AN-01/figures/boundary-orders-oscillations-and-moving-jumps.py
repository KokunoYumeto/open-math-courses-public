"""Exact curves accompanying Boundary derivatives, division and moving jumps.

Original figure and plotting source: GPT-6 Astra (OpenAI), CC0-1.0.
The finite plotted oscillation interval illustrates the formula; convergence
and derivative orders follow from the proofs in the lesson.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                     "svg.hashsalt":"AN01-U125-boundaries",
                     "axes.spines.top":False,"axes.spines.right":False})
fig,axs=plt.subplots(2,2,figsize=(12.8,10.0),constrained_layout=True)
blue="#1765a0"; red="#b44238"; green="#267550"
ax=axs[0,0]
theta=np.linspace(0,2*np.pi,801)
ax.fill(np.cos(theta),np.sin(theta),color=blue,alpha=.08)
ax.plot(np.cos(theta),np.sin(theta),color=blue,lw=2)
arc=np.linspace(.32,.90,101)
ax.plot(np.cos(arc),np.sin(arc),color=red,lw=6)
v=np.array([np.cos(.62),np.sin(.62)])
ax.annotate("",xy=1.38*v,xytext=v,arrowprops={"arrowstyle":"->","color":red,"lw":2})
ax.text(1.09,.89,r"$n=(x,y)$",color=red)
ax.text(-1.12,-1.48,r"$\partial_{xy}\chi$: exact order 1",fontsize=12)
ax.text(-1.12,-1.70,r"$S\chi=-\sigma$: exact order 0",fontsize=12)
ax.set(xlim=(-1.5,1.7),ylim=(-1.85,1.48),aspect="equal",
       xlabel="$x$",ylabel="$y$",title="A. A normal test on a circle arc")
ax.axhline(0,c="0.85",lw=.7);ax.axvline(0,c="0.85",lw=.7)

ax=axs[0,1]
x=np.linspace(.025,.5,6500)
ax.plot(x,x*np.sin(1/x),color=red,label=r"$a=b=1$: order 1",lw=1.4)
ax.plot(x,x*x*np.sin(1/x),color=blue,label=r"$a=2,\ b=1$: order 0",lw=1.7)
ax.plot([0,0],[-.4,0],color=green,lw=2,label="vertical endpoint boundary")
ax.set(xlim=(-.015,.51),ylim=(-.42,.5),xlabel="$x$",ylabel="$h(x)$",
       title=r"B. $\partial_xu$, $h(x)=x^a\sin(x^{-b})$")
ax.legend(loc="upper left",fontsize=10)
ax.text(.02,-.37,r"Graph shown for $0.025\leq x\leq0.5$",fontsize=10)
ax.grid(alpha=.15)

ax=axs[1,0]
y=np.linspace(-.8,.8,2001)
flat=np.zeros_like(y); nz=y!=0;flat[nz]=np.exp(-1/y[nz]**2)
ax.plot(y,y**4,color=blue,lw=2,label=r"$f(y)=y^4$: division exists")
ax.plot(y,flat,color=red,lw=2,label=r"$f(y)=e^{-1/y^2}$, $f(0)=0$: no division")
ax.scatter([0],[0],color="black",s=18,zorder=5)
ax.set(xlabel="$y$",ylabel="$f(y)$",ylim=(-.025,.44),
       title=r"C. Solving $(x^2+f(y))u=1$")
ax.legend(loc="upper center",fontsize=10)
ax.text(-.69,.235,"Both functions vanish only at 0.\nTheir orders of vanishing differ.",fontsize=10)
ax.grid(alpha=.15)

ax=axs[1,1]
t=np.linspace(.05,4,700)
for C,color in [(-1,red),(0,"#606060"),(1,blue),(2,green)]:
    ax.plot(t,-t+C*np.sqrt(t),label=f"$C={C}$",color=color,lw=2)
ax.set(xlabel="$t>0$",ylabel=r"$x=\varphi(t)$",
       title=r"D. Exact interfaces $\varphi(t)=-t+C\sqrt{t}$")
ax.legend(ncol=2,fontsize=10)
ax.grid(alpha=.15)
fig.suptitle("Boundary derivatives and singular interfaces",fontsize=19)
dest=Path(__file__).resolve().with_suffix("")
fig.savefig(dest.with_suffix(".png"),dpi=155)
fig.savefig(dest.with_suffix(".svg"),metadata={"Date":None})
p=dest.with_suffix(".svg")
p.write_text("\n".join(line.rstrip() for line in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
print(dest)
