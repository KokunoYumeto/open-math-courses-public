"""Exact three-dimensional heat-kernel sections and derivative multipliers."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-heat-20261009",
                         "font.size":11,"axes.labelsize":12,
                         "axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12,6))
    fig.subplots_adjust(left=.08,right=.98,bottom=.24,top=.80,wspace=.30)
    colours=["#126b75","#ad5d23","#684b91"]
    x=np.linspace(-6,6,1601);rho=np.linspace(0,5,1601)
    for s,colour in zip([0.25,1.0,4.0],colours):
        kernel=(4*np.pi*s)**(-1.5)*np.exp(-x*x/(4*s))
        axes[0].plot(x,kernel,color=colour,label=f"s = {s:g} m²",lw=2)
        multiplier=rho*np.exp(-s*rho*rho)
        axes[1].plot(rho,multiplier,color=colour,label=f"s = {s:g} m²",lw=2)
        peak=1/np.sqrt(2*s)
        axes[1].plot(peak,1/np.sqrt(2*np.e*s),"o",color=colour,ms=5)
    axes[0].set(xlabel="x¹ (m), with x² = x³ = 0",
                ylabel="kₛ(x¹, 0, 0) (m⁻³)",
                title="A coordinate section of the 3D kernel")
    axes[1].set(xlabel="|ξ| (m⁻¹)",ylabel="|ξ| exp(−s|ξ|²) (m⁻¹)",
                title="The gain of one spatial derivative")
    for ax in axes:
        ax.grid(alpha=.2);ax.legend();ax.set_ylim(bottom=0)
    fig.suptitle("Heat smoothing retains its length scale",fontsize=18,y=.96)
    fig.text(.5,.035,
       "Left: a section, not a 1D density. Right: dots mark |ξ| = 1/√(2s), value 1/√(2es).\n"
       "Exact formulas: H9.16–H9.17 and Exercise 9. Samples draw the curves; the proofs are analytical.",
       ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-heat-smoothing.svg",metadata={"Date":None})
    fig.savefig(out/"f09-heat-smoothing.png",dpi=150,metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)

if __name__=="__main__":build()
