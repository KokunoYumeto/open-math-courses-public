"""Endpoint Taylor weights and the exact exponential-phase order. Original, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
out=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(14,4.5),layout="constrained")
x=np.linspace(-1,1,1001);w=(1-x*x)**2;d=(1-np.abs(x))**2
axs[0].fill_between(x,d,w,color="#dce8ed")
axs[0].plot(x,w,lw=2,color="#075e83",label=r"$(1-x^2)^2$")
axs[0].plot(x,d,lw=2,ls="--",color="#a45a29",label=r"$(1-|x|)^2$")
axs[0].set(xlim=(-1.05,1.05),ylim=(-.03,1.08),xlabel="$x$",title="Endpoint envelope: $m=2$")
axs[0].legend();axs[0].grid(alpha=.15)
for k in range(1,6):
    lo=1/k;hi=2 if k==1 else 1/(k-1)
    axs[1].plot([lo,hi],[k,k],color="#075e83",lw=2)
    axs[1].plot(lo,k,"o",ms=6,color="#075e83")
    if k>1:axs[1].plot(hi,k,"o",ms=6,mfc="white",mec="#075e83")
axs[1].set_xscale("log");axs[1].set_xlim(.19,2.04);axs[1].set_ylim(.7,5.4)
axs[1].set_xticks([.2,1/3,.5,1,2],["$1/5$","$1/3$","$1/2$","$1$","$2$"]);axs[1].minorticks_off()
axs[1].set_yticks([1,2,3,4,5])
axs[1].set(xlabel="$a$ (logarithmic scale)",ylabel="Minimum extension order",title=r"$k_{\min}=\lceil 1/a\rceil$")
axs[1].grid(alpha=.15)
x=np.linspace(.001,.5,1001);q=4*np.sqrt(1+(12*x-1)**2*np.exp(-1/x))
axs[2].plot(np.r_[0,x],np.r_[4,q],color="#075e83",lw=2)
axs[2].plot(0,4,"o",color="#a45a29")
axs[2].axhline(4,color="#999999",ls=":",lw=1)
axs[2].set(xlim=(-.015,.51),ylim=(3.5,9),xlabel="$x$",ylabel=r"$|W(x)|/x^4$",title="A primitive at $a=1/2$, $k=2$")
axs[2].grid(alpha=.15)
for ext in ("png","svg"):
    p=out/f"endpoint-weights-and-order-thresholds.{ext}"
    fig.savefig(p,dpi=170,metadata={"Date":None} if ext=="svg" else {})
    if ext=="svg":p.write_text("\n".join(x.rstrip() for x in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
