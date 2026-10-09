"""Exact finite backward-heat and logarithmic factors in HT."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-fixedtime-20261009","font.size":11,
       "axes.labelsize":12,"axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12,6))
    fig.subplots_adjust(left=.09,right=.98,bottom=.25,top=.79,wspace=.33)
    S=1.;left=np.linspace(.01,S,1201);right=np.linspace(0,S,1201)
    backward=4*(left**(-.25)-S**(-.25))
    logarithm=np.zeros_like(right);logarithm[1:]=np.sqrt(right[1:])*np.log(S/right[1:])
    axes[0].plot(left,backward,color="#126b75",lw=2)
    axes[0].set(title="The finite backward power integral",
       ylabel=r"$4(s^{-1/4}-S^{-1/4})$ ($\mathrm{m}^{-1/2}$)")
    axes[0].text(.98,.94,"Diverges as s → 0;\nshown only for s ≥ 0.01 m².",
       transform=axes[0].transAxes,ha="right",va="top",fontsize=10)
    axes[1].plot(right,logarithm,color="#ad5d23",lw=2)
    max_s=S*np.exp(-2);max_y=2*np.sqrt(S)/np.e
    axes[1].scatter([max_s],[max_y],color="#263743",zorder=5)
    axes[1].axhline(max_y,color="#263743",ls="--",lw=1)
    axes[1].annotate("Exact maximum 2√S/e\nat s = S exp(−2)",xy=(max_s,max_y),
       xytext=(.44,.58),arrowprops={"arrowstyle":"->","color":"#263743"},fontsize=10)
    axes[1].set(title="The bounded logarithmic product",
       ylabel=r"$\sqrt{s}\log(S/s)$ (m)")
    for ax in axes:
        ax.set_xlabel("Original heat parameter s (m²)");ax.grid(alpha=.2)
    fig.suptitle("The finite heat endpoint controls both factors",fontsize=18,y=.96)
    fig.text(.5,.035,
       "Original endpoint S = 1 m². Exact scalar proof weights, not Yang–Mills field samples.\n"
       "HT.28 retains the finite power difference; HT.43 proves the logarithmic maximum.",
       ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-backward-heat-weights.svg",metadata={"Date":None})
    fig.savefig(out/"f09-backward-heat-weights.png",dpi=150,
       metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)
if __name__=="__main__":build()
