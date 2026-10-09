"""Exact commuting heat solution and its caloric-gauge exponential."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-construction-20261009",
      "font.size":11,"axes.labelsize":12,"axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12,6))
    fig.subplots_adjust(left=.08,right=.98,bottom=.24,top=.80,wspace=.30)
    length=1.0;x=np.linspace(-5,5,1601)
    f=np.exp(-x*x/(2*length*length));caloric=-x/(length*length)*f
    axes[0].plot(x,caloric,"--",color="#263743",lw=2,label="Caloric field: every s")
    axes[1].axhline(0,ls="--",color="#263743",lw=1,label="s = 0")
    for s,colour in zip([.25,1.,4.],["#126b75","#ad5d23","#684b91"]):
        variance=length*length+2*s
        u=(length*length/variance)**1.5*np.exp(-x*x/(2*variance))
        axes[0].plot(x,-x/variance*u,color=colour,lw=2,label=f"DeTurck: s = {s:g} m²")
        axes[1].plot(x,u-f,color=colour,lw=2,label=f"s = {s:g} m²")
    axes[0].set(xlabel="x¹ (m), with x² = x³ = 0",
      ylabel="Coefficient of T in A₁ (m⁻¹)",title="The potential smooths in DeTurck gauge")
    axes[1].set(xlabel="x¹ (m), with x² = x³ = 0",
      ylabel="u(s,x) − f(x) (dimensionless)",title="V = exp((u − f)T) restores the initial field")
    for ax in axes:ax.grid(alpha=.2);ax.legend(fontsize=9.5)
    fig.suptitle("An exact heat flow and its caloric gauge",fontsize=18,y=.96)
    fig.text(.5,.035,
      "L = 1 m. The dashed field is a′₁ = (∂₁f)T at every heat time; all curvature components vanish.\n"
      "HC.35–HC.36 retain the full three-dimensional Gaussian factor. Curves are coordinate sections.",
      ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-heat-gauge.svg",metadata={"Date":None})
    fig.savefig(out/"f09-heat-gauge.png",dpi=150,metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)

if __name__=="__main__":build()
