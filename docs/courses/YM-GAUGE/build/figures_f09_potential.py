"""Exact full Gaussian derivative norms at finite heat endpoints."""
from pathlib import Path
import numpy as np
from scipy.special import gamma,beta,betainc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-potential-20261009",
      "font.size":11,"axes.labelsize":12,"axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12,6))
    fig.subplots_adjust(left=.08,right=.98,bottom=.24,top=.79,wspace=.31)
    L=1.;epsilon=.5;kappa=2.;heat=np.linspace(0,1,1201)
    z=2*heat/(L*L+2*heat)
    for m,colour in zip(range(3),["#263743","#126b75","#ad5d23"]):
        endpoint2=2*np.pi*kappa*epsilon**2*L**6*gamma(m+3.5)*heat**m/(L*L+2*heat)**(m+3.5)
        integral2=2*np.pi*kappa*epsilon**2*gamma(m+4.5)/(2**(m+1)*L)*beta(m+1,3.5)*betainc(m+1,3.5,z)
        axes[0].plot(heat,np.sqrt(endpoint2),lw=2,color=colour,label=f"m = {m}")
        axes[1].plot(heat,np.sqrt(integral2),lw=2,color=colour,label=f"m = {m}")
    axes[0].set(title="Actual weighted endpoint value Uₘ(S)",ylabel="Uₘ(S) (m⁻¹ᐟ²)")
    axes[1].set(title="Accumulated heat dissipation Vₘ(S)",ylabel="Vₘ(S) (m⁻¹ᐟ²)")
    for ax in axes:
        ax.set_xlabel("Original heat endpoint S (m²)")
        ax.grid(alpha=.2);ax.legend(fontsize=10)
    fig.suptitle("Every derivative keeps its finite heat endpoint",fontsize=18,y=.96)
    fig.text(.5,.035,
       "Three-dimensional Aᵢ = ε ∂ᵢhₛ T; L = 1 m; ε = 1/2; −tr(T²) = 2.\n"
       "HP.29–HP.34: exact full-space norms, with the original radial and Fourier factors.",
       ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-ordinary-smoothing.svg",metadata={"Date":None})
    fig.savefig(out/"f09-ordinary-smoothing.png",dpi=150,
       metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)
if __name__=="__main__":build()
