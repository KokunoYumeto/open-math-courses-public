"""Original-coordinate exact half-wave and the Fourier cone of its square."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def build():
    out=Path(__file__).resolve().parents[1]/"figures"
    plt.rcParams.update({"svg.hashsalt":"YM-F09-wave-20261009","font.size":11,
       "axes.labelsize":12,"axes.titlesize":13,"font.family":"DejaVu Sans"})
    fig,axes=plt.subplots(1,2,figsize=(12.8,6.1))
    fig.subplots_adjust(left=.08,right=.93,bottom=.26,top=.8,wspace=.34)
    a=1.;A=1.;c=1.;r=np.linspace(0,5,1801)
    for t,col in [(0.,"#126b75"),(1.,"#ad5d23"),(2.,"#6b4a9b"),(4.,"#344957")]:
        modulus=abs(A)/(2*np.pi**2*np.sqrt((a*a-c*c*t*t+r*r)**2+4*a*a*c*c*t*t))
        axes[0].plot(r,modulus,color=col,lw=2,label=f"t = {t:g} s")
    axes[0].set(title="The exact smooth half-wave (HW.40)",
       xlabel="Original radius r (m)",ylabel="Field modulus |u(t,r)| (m⁻¹)")
    axes[0].legend(frameon=False);axes[0].grid(alpha=.2)
    xi=np.linspace(-4,4,801);tau=np.linspace(0,4,501)
    XI,TAU=np.meshgrid(xi,tau)
    density=A*A/(2*np.pi*c)*np.exp(-a*TAU/c)*(TAU>c*np.abs(XI))
    im=axes[1].pcolormesh(XI,TAU,density,cmap="viridis",shading="auto",rasterized=True,
       vmin=0,vmax=A*A/(2*np.pi*c))
    axes[1].plot([-4,0,4],[4,0,4],color="white",lw=1.4,ls="--")
    axes[1].set(title="Fourier density of u² (HW.42)",
       xlabel="Spatial frequency ξ₁ (m⁻¹)",ylabel="Temporal frequency τ (s⁻¹)")
    axes[1].text(.5,.92,"Slice ξ₂ = ξ₃ = 0",transform=axes[1].transAxes,
       ha="center",va="top",color="white",fontsize=11)
    cb=fig.colorbar(im,ax=axes[1],fraction=.052,pad=.035)
    cb.set_label("Actual Fourier density (m·s)")
    fig.suptitle("An attained wave bound with every physical factor retained",fontsize=18,y=.96)
    fig.text(.5,.04,
       "a = 1 m, A = 1 m, c = 1 m/s. Profiles have noncompact initial data; r ≤ 5 m is a viewing window.\n"
       "The dashed cone τ = c|ξ₁| describes Fourier support, not spatial support. Full proofs: HW.39–HW.44.",
       ha="center",va="bottom",fontsize=10)
    fig.savefig(out/"f09-wave-cone-and-profile.svg",metadata={"Date":None})
    fig.savefig(out/"f09-wave-cone-and-profile.png",dpi=150,
       metadata={"Software":"YM-GAUGE reproducible figure"})
    plt.close(fig)
if __name__=="__main__":build()

