"""Exact weighted Gaussian heat identity and the caloric gauge anchor."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-caloric-20261009",
      "font.size":11,"axes.labelsize":12,"axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12,6.2))
    fig.subplots_adjust(left=.08,right=.98,bottom=.24,top=.79,wspace=.32)
    L=1.;eps=.5;kappa=2.;s=np.linspace(0,2,1601);v=L*L+2*s
    alpha2=105*np.pi**1.5/8*kappa*eps**2*L**6
    alpha3=945*np.pi**1.5/16*kappa*eps**2*L**6
    endpoint=s*alpha2*v**(-4.5)
    integral=alpha3*((L*L)**(-3.5)/63-v**(-3.5)/14+L*L*v**(-4.5)/18)
    previous=alpha2/7*((L*L)**(-3.5)-v**(-3.5))
    axes[0].plot(s,endpoint,color="#126b75",lw=2,label="s a₂(s)²")
    axes[0].plot(s,2*integral,color="#ad5d23",lw=2,label="2 ∫₀ˢ r a₃(r)² dr")
    axes[0].plot(s,previous,color="#684b91",lw=3,label="∫₀ˢ a₂(r)² dr")
    axes[0].plot(s,endpoint+2*integral,"--",color="#263743",lw=1.4,label="Sum of the first two")
    axes[0].set(xlabel="Heat time s (m²)",ylabel="Full spatial integral (m⁻¹)",
      title="Every term of the weighted heat identity")
    x=np.linspace(-5,5,1601)
    for tau,colour in zip([0.,.25,1.],["#263743","#126b75","#ad5d23"]):
        variance=L*L+2*tau
        u=eps*(L*L/variance)**1.5*np.exp(-x*x/(2*variance))
        axes[1].plot(x,-x/variance*u,color=colour,lw=2,label=f"Anchor τ = {tau:g} m²")
    axes[1].set(xlabel="x¹ (m), with x² = x³ = 0",
      ylabel="Coefficient of T in a₁⁽τ⁾ (m⁻¹)",
      title="The anchor selects the initial representative")
    for ax in axes:ax.grid(alpha=.2);ax.legend(fontsize=9.5)
    fig.suptitle("Weighted smoothing and the data of a caloric gauge",fontsize=18,y=.96)
    fig.text(.5,.035,
      "L = 1 m, ε = 1/2, T = diag(i, −i), κ(T,T) = 2. All curvature components vanish.\n"
      "HG.41–HG.44: exact full-space heat integrals on the left; coordinate sections on the right.",
      ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-weighted-caloric.svg",metadata={"Date":None})
    fig.savefig(out/"f09-weighted-caloric.png",dpi=150,metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)

if __name__=="__main__":build()
