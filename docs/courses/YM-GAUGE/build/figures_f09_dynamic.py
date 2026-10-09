"""Exact time components before and after the endpoint gauge."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-dynamic-20261009",
      "font.size":11,"axes.labelsize":12,"axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12,6))
    fig.subplots_adjust(left=.08,right=.98,bottom=.25,top=.79,wspace=.32)
    L=1.;eps=.5;omega=1.;endpoint=1.;x=np.linspace(-5,5,1601)
    def h(s):
        v=L*L+2*s
        return (L*L/v)**1.5*np.exp(-x*x/(2*v))
    g=h(0);hS=h(endpoint)
    for heat,colour in zip([0.,.25,1.],["#263743","#126b75","#ad5d23"]):
        axes[0].plot(x,eps*omega*(g-h(heat)),color=colour,lw=2,
          label=f"Heat s = {heat:g} m²")
        axes[1].plot(x,eps*omega*(hS-h(heat)),color=colour,lw=2,
          label=f"Heat s = {heat:g} m²")
    axes[0].set(title="The original time component Aₜ",
      ylabel="Coefficient of T (1/second)")
    axes[1].set(title="The transformed component aₜ vanishes at S",
      ylabel="Coefficient of T (1/second)")
    for ax in axes:
        ax.set_xlabel("x¹ (m), with x² = x³ = 0")
        ax.grid(alpha=.2);ax.legend(fontsize=9.5)
    fig.suptitle("An exact dynamic heat flow and its endpoint gauge",fontsize=18,y=.96)
    fig.text(.5,.035,
      "Physical t = t* = 0 seconds; ω = 1/second; ε = 1/2; L = 1 m; heat endpoint S = 1 m².\n"
      "HD.31–HD.34: coordinate sections of a regular dynamic heat connection with its computed Gauss defect.",
      ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-dynamic-time-gauge.svg",metadata={"Date":None})
    fig.savefig(out/"f09-dynamic-time-gauge.png",dpi=150,
      metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)

if __name__=="__main__":build()
