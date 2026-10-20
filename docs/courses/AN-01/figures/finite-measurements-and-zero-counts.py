"""Finite test interpolation and exact cumulative zero counts. Original figure: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.spines.top":False,
                    "axes.spines.right":False,"svg.hashsalt":"AN01-finite-measurements-zero-counts"})
def bump(x):
    y=np.zeros_like(x);keep=np.abs(x)<1
    y[keep]=np.exp(1-1/(1-x[keep]**2))
    return y
grid=np.linspace(-1,1,200001)
A2=np.trapezoid(grid**2*bump(grid)**2,grid)
x=np.linspace(-1.15,1.15,1801);b=bump(x);f=-x*b/A2
fig,axes=plt.subplots(1,2,figsize=(12.4,4.9),constrained_layout=True)
axes[0].plot(x,b,lw=1.8,label=r"Test $b$")
axes[0].plot(x,x*b,lw=1.8,label=r"Test $xb$")
axes[0].plot(x,f,lw=2.3,color="#a34828",label=r"Interpolant $-xb/A_2$")
axes[0].axhline(0,color="#888888",lw=.7)
axes[0].set(xlabel="$x$",ylabel="Function value",title="Two exact derivative measurements",xlim=(-1.15,1.15))
axes[0].text(.03,.10,r"$\int fb=0,\quad\int fxb=-1$"+"\n"+
             r"$A_2=\int x^2b^2>0$",transform=axes[0].transAxes,fontsize=12)
axes[0].legend(loc="upper right",frameon=False,fontsize=10)
axes[0].grid(alpha=.18)
N=8;a=(np.arange(1,N+1)-.5)/N
s=np.linspace(-.08,1.08,1001)
axes[1].plot(s,np.clip(s,0,1),color="#888888",lw=2,label="Uniform length measure")
axes[1].step(np.r_[-.08,a,1.08],np.r_[0,np.arange(1,N+1)/N,1],
             where="post",color="#126f82",lw=2.2,label="Eight zeros, each weight 1/8")
axes[1].scatter(a,np.arange(1,N+1)/N,s=20,color="#126f82",zorder=4)
axes[1].set(xlabel="Real coordinate $s$",ylabel=r"Mass of $(-\infty,s]$",
            title="Normalized polynomial-zero measures",xlim=(-.08,1.08),ylim=(-.03,1.05))
axes[1].text(.05,.74,r"$a_{\ell,N}=(\ell-\frac{1}{2})/N$"+"\n"+
             r"$\sup_s|C_N(s)-C(s)|=1/(2N)$",
             transform=axes[1].transAxes,fontsize=12)
axes[1].legend(loc="lower right",frameon=False,fontsize=10)
axes[1].grid(alpha=.18)
for ext in ["png","svg"]:
    fig.savefig(out/("finite-measurements-and-zero-counts."+ext),dpi=170,
                metadata={"Date":None} if ext=="svg" else None)
p=out/"finite-measurements-and-zero-counts.svg"
p.write_text("\n".join(line.rstrip() for line in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
