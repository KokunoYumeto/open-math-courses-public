"""Exact profiles for Complex phases and oscillatory distributions; CC0 1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def cutoff(r):
    r=np.asarray(r,dtype=float)
    out=np.ones_like(r)
    out[r>=2]=0
    mid=(r>1)&(r<2)
    t=r[mid]-1
    left=np.exp(-1/t)
    right=np.exp(-1/(1-t))
    out[mid]=right/(left+right)
    return out

r=np.geomspace(.35,40,2400)
shells=[cutoff(r)]+[cutoff(r/2**j)-cutoff(r/2**(j-1)) for j in range(1,7)]
assert np.max(np.abs(np.sum(shells,axis=0)-1))<1e-14
plt.rcParams.update({"font.size":12,"axes.spines.top":False,"axes.spines.right":False,
                     "svg.hashsalt":"AN01-U135-oscillatory-shells"})
fig,axes=plt.subplots(2,1,figsize=(11,8.5),layout="constrained")
colors=["#164a68","#177b7c","#328c41","#a47b11","#c25e28","#a83a6f","#694e9a"]
for j,v in enumerate(shells):
    axes[0].plot(r,v,lw=2.2,color=colors[j],label=rf"$\psi_{j}$")
axes[0].plot(r,np.sum(shells,axis=0),"k--",lw=1.2,label="sum = 1")
axes[0].set_xscale("log",base=2)
axes[0].set_xticks([.5,1,2,4,8,16,32],labels=["½","1","2","4","8","16","32"])
axes[0].set(xlabel=r"Frequency radius $|\theta|$",ylabel="Partition weight",
            title="Frequency localization: finitely overlapping dyadic annuli",
            xlim=(.35,40),ylim=(-.04,1.1))
axes[0].legend(ncol=8,fontsize=10,loc="lower left",bbox_to_anchor=(0,1.01),frameon=False)
axes[0].set_title("Frequency localization: finitely overlapping dyadic annuli",pad=45)
x=np.linspace(-3,3,2401)
for eps,color in zip([1,.5,.2],["#164a68","#177b7c","#c25e28"]):
    y=2*eps/(x*x+eps*eps)
    axes[1].plot(x,y,lw=2.3,color=color,label=rf"$\varepsilon={eps:g}$")
axes[1].set(xlabel=r"Observed coordinate $x$",ylabel=r"$2\varepsilon/(x^2+\varepsilon^2)$",
            title=r"Damping tends to zero: the total mass stays $2\pi$",
            xlim=(-3,3),ylim=(0,10.6))
axes[1].legend(frameon=False)
axes[1].text(.03,.91,r"$\int_{\mathbb{R}}2\varepsilon/(x^2+\varepsilon^2)\,dx=2\pi$",
             transform=axes[1].transAxes,fontsize=12)
for ax in axes:ax.grid(alpha=.16)
fig.suptitle("Complex phases: cancellation and concentration",fontsize=17)
dest=Path(__file__).resolve().with_suffix("")
fig.savefig(dest.with_suffix(".png"),dpi=160)
fig.savefig(dest.with_suffix(".svg"),metadata={"Date":None})
svg=dest.with_suffix(".svg")
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",
               encoding="utf-8")
