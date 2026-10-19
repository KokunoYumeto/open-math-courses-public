"""Extension order and an exact oscillatory primitive. Original figure, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
out=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout="constrained")
ax=axs[0]
for step,color,offset,label in [(1,"#687b8b",0,r"$x^b$"),(2,"#075e83",0,r"$e^{i/x}x^b$")]:
    for n in range(0,8):
        lo=-1-step*n; hi=-1-step*(n-1)
        if n==0:hi=1
        if hi < -7 or lo>1:continue
        ax.plot([max(lo,-7),min(hi,1)],[n,n],color=color,lw=2,label=label if n==0 else None)
        if -7<=lo<=1:ax.plot(lo,n,marker="o",ms=6,mfc="white",mec=color,zorder=4)
        if n>0 and -7<=hi<=1:ax.plot(hi,n,marker="o",ms=5,color=color,zorder=5)
ax.set(xlim=(-7.15,1.1),ylim=(-.3,7.3),xlabel=r"$\sigma=\mathrm{Re}\,b$",ylabel="Minimum extension order",
       title="Strict thresholds, including equality")
ax.set_xticks(range(-7,2));ax.set_yticks(range(8))
ax.grid(alpha=.15);ax.legend(loc="upper right")
ax=axs[1]
x=np.linspace(.025,.45,7000)
ax.plot(x,-x*np.cos(1/x),color="#075e83",lw=1.8,label=r"$\mathrm{Re}\,V=-x\cos(1/x)$")
ax.plot(x,x,"--",color="#bb6b2c",lw=1.4,label=r"Envelope $\pm x$")
ax.plot(x,-x,"--",color="#bb6b2c",lw=1.4)
ax.axhline(0,color="#687b8b",lw=.6)
ax.text(.045,.31,r"$V''=x^{-3}e^{i/x}$",fontsize=14)
ax.set(xlim=(0,.45),ylim=(-.47,.47),xlabel="$x>0$",ylabel="Real part of the primitive",
       title="An integrable primitive with a singular second derivative")
ax.legend(loc="lower left");ax.grid(alpha=.15)
for ext in ("png","svg"):
    p=out/f"oscillatory-extension-thresholds.{ext}"
    fig.savefig(p,dpi=170,metadata={"Date":None} if ext=="svg" else {})
    if ext=="svg":p.write_text("\n".join(x.rstrip() for x in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
