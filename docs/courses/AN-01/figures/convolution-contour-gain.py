"""AN01-U092 Lemma 2 and Exercise 8: exact phase gains. CC0-1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"svg.fonttype":"none"})
x=np.linspace(-3,3,1201)
delta=0.25
bound=delta*(np.sqrt(1+x*x)-1)
exact=delta*x*x/np.sqrt(1+x*x)
fig,(a,b)=plt.subplots(1,2,figsize=(12.5,5.8),layout="constrained")
a.fill_between(x,0,0.35,color="#e8f0f9",label=r"original tube: $h>0$")
a.fill_between(x,np.maximum(-bound,-0.35),0,color="#d1e9d8",
               label="continuation supplied by the estimate")
a.plot(x,-bound,color="#26704b",lw=2)
a.axhline(0,color="#617486",lw=0.9)
a.scatter([0],[0],color="#b44627",s=40,zorder=5)
a.annotate("gain vanishes at the origin",xy=(0,0),xytext=(-2.85,0.22),
           fontsize=10,arrowprops={"arrowstyle":"->","color":"#b44627"})
a.text(0,-0.29,r"$h=-\frac{1}{4}(\sqrt{1+x^2}-1)$",ha="center",fontsize=13,
       bbox={"facecolor":"white","edgecolor":"none","alpha":0.85})
a.set(xlim=(-3,3),ylim=(-0.35,0.35),xlabel=r"real base coordinate $x$",
      ylabel=r"height $h=y+1$",title="A sufficient local continuation region")
a.legend(loc="upper center",bbox_to_anchor=(0.5,-0.18),fontsize=10,frameon=False)
b.plot(x,exact,color="#155c8b",lw=2,label=r"exact collinear gain: $\delta x^2/\sqrt{1+x^2}$")
b.plot(x,bound,color="#c26a26",lw=2,ls="--",
       label=r"proved lower gain: $\delta(\sqrt{1+x^2}-1)$")
b.set(xlim=(-3,3),ylim=(0,0.75),xlabel=r"real base coordinate $x$",
      ylabel="damping per unit frequency",
      title="The contour produces a positive gain off zero")
b.grid(alpha=0.18)
b.legend(loc="upper center",bbox_to_anchor=(0.5,-0.18),fontsize=10,frameon=False)
fig.suptitle(r"Positive frequency, $\theta=1$, $\delta=1/4$: Lemma 2 and Exercise 8",
             fontsize=16)
for extension in ["png","svg"]:
 p=out/("convolution-contour-gain."+extension)
 fig.savefig(p,dpi=160,facecolor="white")
 if extension=="svg":
  p.write_text("\n".join(line.rstrip() for line in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
