"""Exact moment bounds and complex extension domains, AN01-U150 and U151.

The plots show a proved mass interval and open domains, not sampled density
values or values of an unspecified holomorphic function.
Original figure by GPT-6 Astra (OpenAI), 2026; CC0.
Requires NumPy and Matplotlib; output is written beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
matplotlib.rcParams["svg.hashsalt"]="AN01-escaping-averages-and-analytic-tubes"
root=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout="constrained")
N=np.arange(1,513)
widths=1/np.arange(1,514)
mean=np.cumsum(widths)[1:]/2
ax=axes[0]
ax.fill_between(N,mean-1,mean+1,color="#bcd6e9",alpha=.7,
                label=r"mass at least $5/6$ in $[m_N-1,m_N+1]$")
ax.plot(N,mean,color="#126c8c",lw=2,label=r"$m_N=\frac{1}{2}\sum_{i=0}^N 1/(i+1)$")
ax.axhline(1,color="#b65931",ls="--",lw=1.5,label=r"fixed level $R=1$")
ax.set_xscale("log",base=2)
ax.set(xlabel="number N of the last averaging factor",ylabel="position on the real line",
       title="Concentration can move beyond every fixed interval")
ax.legend(fontsize=9,loc="upper left")
ax.grid(alpha=.2)

def tube(a,b,r):
    right=np.linspace(-np.pi/2,np.pi/2,151)
    left=np.linspace(np.pi/2,3*np.pi/2,151)
    return (np.r_[b+r*np.cos(right),a+r*np.cos(left),b],
            np.r_[r*np.sin(right),r*np.sin(left),-r])
ax=axes[1]
for r,color,label in [(1/4,"#bcd6e9",r"$\Omega_{1/4}([-1,2])$"),
                      (1/8,"#8ec8b0",r"$\Omega_{1/8}([-1,2])$: $|F|\leq8$")]:
    x,y=tube(-1,2,r)
    ax.fill(x,y,color=color,alpha=.7,label=label)
    ax.plot(x,y,color="#126c8c" if r==.25 else "#257754",ls="--",lw=1.2)
theta=np.linspace(0,2*np.pi,241)
for center in [-1,.5,2]:
    ax.plot(center+.25*np.cos(theta),.25*np.sin(theta),color="#126c8c",alpha=.4,lw=.9)
ax.plot([-1,2],[0,0],color="#263a59",lw=3,label=r"real interval $I=[-1,2]$")
ax.scatter([-1,2],[0,0],color="#263a59",s=16)
ax.set(xlim=(-1.5,2.5),ylim=(-.8,.8),xlabel=r"$\operatorname{Re}z$",
       ylabel=r"$\operatorname{Im}z$",title="Factorial bounds extend past both endpoints")
ax.set_aspect("equal")
ax.set_yticks([-.25,0,.25],["−1/4","0","1/4"])
ax.legend(fontsize=9,loc="upper center",bbox_to_anchor=(.5,-.22))
ax.grid(alpha=.2)
fig.suptitle("One-sided averaging and factorial derivative bounds",fontsize=14)
for suffix in ["png","svg"]:
    target=root/f"escaping-averages-and-analytic-tubes.{suffix}"
    fig.savefig(target,dpi=160,metadata={"Date":None} if suffix=="svg" else None)
    if suffix=="svg":
        target.write_text("\n".join(line.rstrip() for line in target.read_text(encoding="utf-8").splitlines())+"\n",
                          encoding="utf-8",newline="\n")
