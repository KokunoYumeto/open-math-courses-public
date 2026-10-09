"""Reproduce the elementary transport figure. Original drawing: CC0-1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def build():
    root=Path(__file__).resolve().parents[1]
    plt.rcParams.update({"font.size":13,"svg.fonttype":"none","font.family":"DejaVu Sans",
                         "svg.hashsalt":"YM-GAUGE-F01-transport-20261009"})
    fig,axes=plt.subplots(1,2,figsize=(12.8,5.5),layout="constrained")
    x=np.linspace(-3,4,700)
    U0=2.0
    ell=1.0
    v=0.5
    for t,color in [(0.0,"#176a87"),(2.0,"#b55a24")]:
        u=U0*np.exp(-((x-v*t)**2)/ell**2)
        axes[0].plot(x,u,color=color,lw=2.7,label=f"t = {t:g} s")
    axes[0].set(xlabel="First coordinate x¹ (m)",ylabel="Scalar value u (concentration units)",
                title="A moving scalar-field slice",xlim=(-3,4),ylim=(0,2.3))
    axes[0].legend(frameon=False)
    axes[0].text(.02,.95,"x² = x³ = 0",transform=axes[0].transAxes,va="top")
    ts=np.linspace(0,3,200)
    for xi in [-2,-1,0,1,2]:
        axes[1].plot(xi+v*ts,ts,color="#176a87" if xi==0 else "#9daeb3",
                     lw=2.8 if xi==0 else 1.5)
        axes[1].text(xi,-.14,f"{xi:g}",ha="center",va="top",fontsize=11)
    axes[1].scatter([0,1],[0,2],color="#b55a24",s=42,zorder=3)
    axes[1].annotate("Same field value u = 2",xy=(1,2),xytext=(-2.3,2.65),
                     arrowprops={"arrowstyle":"->","color":"#303b43"},fontsize=12)
    axes[1].set(xlabel="First coordinate x¹ (m)",ylabel="Time t (s)",
                title="Paths x¹ = ξ¹ + vt",xlim=(-2.7,3.8),ylim=(-.35,3.2))
    for ax in axes:
        ax.grid(alpha=.18)
        ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("U₀ = 2 concentration units, ℓ = 1 m, v = 0.5 m/s",fontsize=16)
    fig.savefig(root/"figures/f01-transport.svg",metadata={"Date":None,"Creator":"YM-GAUGE figure source; CC0-1.0"})
    fig.savefig(root/"figures/f01-transport.png",dpi=150,metadata={"Software":"YM-GAUGE figure source; CC0-1.0"})
    plt.close(fig)

if __name__=="__main__":
    build()
