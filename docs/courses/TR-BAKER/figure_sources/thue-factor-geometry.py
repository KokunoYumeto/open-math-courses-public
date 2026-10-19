"""Original Figure 13.1. Real locus samples are not an integer-solution search."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main(output=None):
    rho=2**(1/3); omega=complex(-.5,3**.5/2)
    y=np.linspace(-3,3,2401); x=np.cbrt(1+2*y**3)
    # Evaluate the positive factor by its norm identity to avoid cancellation.
    q=x*x+rho*x*y+rho*rho*y*y
    u=-np.log(q); v=np.log(q)
    assert np.max(np.abs(x**3-2*y**3-1))<1e-12
    assert np.max(np.abs(np.abs(x-rho*omega*y)**2-q))<1e-12
    plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
    fig,axs=plt.subplots(1,2,figsize=(11.4,4.7),layout="constrained")
    a=axs[0]
    a.plot(x,y,color="#145a78",lw=2,label=r"$x^3-2y^3=1$")
    a.plot(rho*y,y,"--",color="#b15a20",lw=1.5,label=r"$x=\rho y$")
    a.scatter([1,-1],[0,-1],c=["#1d8052","#963f74"],s=52,zorder=5)
    a.annotate("$(1,0)$",(1,0),xytext=(12,-20),textcoords="offset points")
    a.annotate("$(-1,-1)$",(-1,-1),xytext=(-55,15),textcoords="offset points")
    a.set(xlabel="$x$",ylabel="$y$",title="Real curve and two integer solutions")
    a.set_aspect("equal",adjustable="box");a.grid(alpha=.2);a.legend(loc="upper left",fontsize=10)
    a=axs[1]
    a.plot(u,v,color="#145a78",lw=2,label="Logarithms of real-curve factors")
    lu=np.log(rho-1)
    a.scatter([0,lu],[0,-lu],c=["#1d8052","#963f74"],s=52,zorder=5)
    a.annotate("$(1,0)$",(0,0),xytext=(8,10),textcoords="offset points")
    a.annotate("$(-1,-1)$",(lu,-lu),xytext=(12,7),textcoords="offset points")
    a.annotate("",xy=(lu,-lu),xytext=(0,0),arrowprops={"arrowstyle":"->","color":"#963f74","lw":2})
    a.text(.04,.09,"Unit displacement:\n"+r"$(\log(\rho-1),-\log(\rho-1))$",transform=a.transAxes,fontsize=10)
    a.set(xlabel=r"$u=\log|x-\rho y|$",ylabel=r"$v=2\log|x-\rho\omega y|$",
          title="Norm one gives $u+v=0$")
    a.set_aspect("equal",adjustable="box");a.grid(alpha=.2)
    a.set_xlim(-4.1,.65);a.set_ylim(-.65,4.1)
    fig.suptitle(r"$\rho=\sqrt[3]{2}$, $\omega^2+\omega+1=0$    |    Real loci, not an exhaustive integer search",fontsize=12)
    dest=Path(output) if output else Path(__file__).resolve().parents[1] / "figures/thue-factor-geometry.png"
    fig.savefig(dest,dpi=180);plt.close(fig)
    return dest

if __name__=="__main__":
    print(main())
