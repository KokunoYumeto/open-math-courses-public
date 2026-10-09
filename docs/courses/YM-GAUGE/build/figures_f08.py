"""Reproduce the exact cone section and wave energy in YM-F08. CC0-1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def build():
    plt.rcParams.update({"svg.fonttype":"path","svg.hashsalt":"YM-F08-20261009",
                         "font.size":11,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(13.6,5.8))
    ax=axes[0]
    R=2.0
    s=np.linspace(0,R,201)
    ax.fill_betweenx(s,-R+s,R-s,color="#d6eaf4")
    ax.plot(-R+s,s,color="#176087",lw=2)
    ax.plot(R-s,s,color="#176087",lw=2)
    ax.plot([-R,R],[0,0],color="#176087",lw=2)
    ax.plot([-1.2,1.2],[.8,.8],color="#a74e14",lw=2.5)
    ax.annotate("",xy=(1.2,.8),xytext=(1.75,.8),
                arrowprops=dict(arrowstyle="->",color="#a74e14",lw=1.7))
    ax.annotate("",xy=(-1.2,.8),xytext=(-1.75,.8),
                arrowprops=dict(arrowstyle="->",color="#a74e14",lw=1.7))
    ax.text(0,.9,r"$r=R-s=1.2\ {\rm m}$",ha="center",color="#70380e")
    ax.text(0,.34,r"$\frac{d}{dt}\int_{B_{R-c(t-t_0)}}e"
            r"=-\int_{\partial B}(S\cdot n+ce)\leq0$",ha="center",fontsize=12)
    ax.set(xlim=(-2.25,2.25),ylim=(-.12,2.2),
           xlabel=r"$x^1-x_*^1$ (m), with $x^2=x_*^2,\ x^3=x_*^3$",
           ylabel=r"$s=c(t-t_0)$ (m)")
    ax.set_title("A section of the shrinking balls\nExample radius R = 2 m",pad=14)
    ax.grid(alpha=.2)
    ax=axes[1]
    z=np.linspace(-2*np.pi,2*np.pi,801)
    y=np.cos(z)**2
    ax.plot(z,y,color="#176087",lw=3,label=r"$g_{\rm YM}^2e/(2\hbar c K_T A^2k^2)$")
    ax.plot(z,y,color="#b85b16",lw=1.8,ls="--",
            label=r"$g_{\rm YM}^2S_1/(2\hbar c^2K_T A^2k^2)$")
    ax.set(xlim=(-2*np.pi,2*np.pi),ylim=(-.05,1.34),
           xlabel=r"$z=k(x^1-ct)$ (dimensionless)",
           ylabel="Displayed energy and flux")
    ax.set_xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],
                  [r"$-2\pi$",r"$-\pi$","0",r"$\pi$",r"$2\pi$"])
    ax.set_yticks([0,.5,1])
    ax.legend(loc="upper center",frameon=False,fontsize=10)
    ax.set_title(r"Exact wave: $\Gamma_2=A\sin(k(x^1-ct))T$"
                 "\n"+r"$K_T=-\mathrm{tr}(T^2)>0,\quad Ak\ne0,\quad S_1=ce$",pad=14)
    ax.grid(alpha=.2)
    fig.subplots_adjust(left=.065,right=.985,bottom=.20,top=.79,wspace=.31)
    fig.text(.5,.035,"YM-F08: F8.34–F8.35 and F8.37–F8.38. "
             "The left panel is a section; the right uses the exact displayed coordinate and value maps.",
             ha="center",fontsize=10)
    out=Path(__file__).resolve().parents[1]/"figures"
    out.mkdir(exist_ok=True)
    fig.savefig(out/"f08-energy-flux.svg",metadata={"Date":None,"Creator":"YM-GAUGE course"})
    fig.savefig(out/"f08-energy-flux.png",dpi=160,metadata={"Software":"YM-GAUGE course"})
    plt.close(fig)

if __name__=="__main__":build()
