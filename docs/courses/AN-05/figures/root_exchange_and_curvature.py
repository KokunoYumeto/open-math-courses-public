"""Original CC0 figure: exact root exchange and the double-factor proof."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

rho=0.5
kappa=1/16
theta=np.linspace(0,2*np.pi,401)
z=rho*np.exp(1j*theta)
branch=np.exp(0.5j*theta)

with plt.rc_context({"font.family":"DejaVu Sans","font.size":11}):
    fig=plt.figure(figsize=(14,10),dpi=150,facecolor="#fffdfa")
    fig.text(0.05,0.955,"A smooth polynomial can have exchanging roots",fontsize=21,weight="bold",color="#17374b")
    fig.text(0.05,0.918,r"$q=\kappa F(t+ix)\eta^2,\quad a=i\langle\eta\rangle,\quad \kappa=1/16$; full hypotheses proved in (6.1)–(6.3).",fontsize=12,color="#344756")
    ax=fig.add_axes([0.08,0.51,0.34,0.34])
    ax.plot(z.real,z.imag,color="#87528f",linewidth=3)
    ax.scatter([rho], [0],color="#87528f",s=55,zorder=5)
    ax.annotate("",xy=(z[42].real,z[42].imag),xytext=(z[24].real,z[24].imag),arrowprops={"arrowstyle":"->","color":"#87528f","lw":2})
    ax.text(0.52,-0.045,r"$\theta=0=2\pi$",fontsize=11)
    ax.text(-0.04,0.54,r"$\theta=\pi/2$",ha="center")
    ax.text(-0.53,-0.09,r"$\theta=\pi$",ha="right")
    ax.text(0,-0.59,r"$\theta=3\pi/2$",ha="center")
    ax.set(xlim=(-0.76,0.76),ylim=(-0.68,0.68),xlabel="Time coordinate t",ylabel="Spatial coordinate x")
    ax.set_aspect("equal")
    ax.axhline(0,color="#c3cbd0",lw=0.7)
    ax.axvline(0,color="#c3cbd0",lw=0.7)
    ax.set_title(r"Closed base loop: $t+ix=\frac{1}{2}e^{i\theta}$",fontsize=13,pad=15)
    ax.grid(alpha=0.14)
    for s in ax.spines.values():s.set_color("#c3cbd0")
    ax=fig.add_axes([0.57,0.51,0.34,0.34])
    ax.plot(branch.real,branch.imag,color="#2178a5",linewidth=3,label=r"$w_+(\theta)=e^{i\theta/2}$")
    ax.plot(-branch.real,-branch.imag,color="#c7862c",linewidth=3,label=r"$w_-(\theta)=-e^{i\theta/2}$")
    ax.scatter([1,-1],[0,0],color="#2178a5",s=55,zorder=5)
    ax.annotate("",xy=(branch[250].real,branch[250].imag),xytext=(branch[225].real,branch[225].imag),arrowprops={"arrowstyle":"->","color":"#2178a5","lw":2})
    ax.annotate("",xy=(-branch[250].real,-branch[250].imag),xytext=(-branch[225].real,-branch[225].imag),arrowprops={"arrowstyle":"->","color":"#c7862c","lw":2})
    ax.text(1.04,0.06,r"$w_+(0)=1$",color="#2178a5")
    ax.text(-1.05,0.09,r"$w_+(2\pi)=-1$",ha="right",color="#2178a5")
    ax.set(xlim=(-1.62,1.62),ylim=(-1.35,1.35),xlabel="Real part of w",ylabel="Imaginary part of w")
    ax.set_aspect("equal")
    ax.axhline(0,color="#c3cbd0",lw=0.7)
    ax.axvline(0,color="#c3cbd0",lw=0.7)
    ax.set_title(r"Root deviation: $w=(\zeta-i\sqrt{2})/b$",fontsize=13,pad=15)
    ax.legend(loc="lower center",fontsize=9,frameon=False,ncol=2)
    ax.grid(alpha=0.14)
    for s in ax.spines.values():s.set_color("#c3cbd0")
    fig.text(0.08,0.44,r"At $\eta=1$: $q=b^2e^{i\theta}$, $b=\sqrt{\kappa/2}\,e^{-2}=e^{-2}/(4\sqrt{2})>0$.",fontsize=12)
    fig.text(0.08,0.410,"A selected branch is continuous on [0, 2π] and ends at the other root. The unordered pair closes.",fontsize=11,color="#344756")
    fig.text(0.08,0.381,"These parametrized paths display the root exchange proved in (6.4) and Exercise 5; a selected branch cannot close.",fontsize=10,color="#536172")
    ax=fig.add_axes([0.05,0.075,0.90,0.25]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
    ax.text(0,1.01,"The estimate keeps the polynomial intact",fontsize=15,weight="bold",color="#17374b")
    boxes=[
        (0.00,0.42,0.31,0.40,"Curvature: (2.6)",r"$(Mv,v)\geq2\tau(U^2+V^2)$"+"\n"+r"$-\,C\tau^{-1}E^2$","#e9f4f8"),
        (0.34,0.42,0.31,0.40,"Remainder: (4.2)",r"$(Jv,v)\geq-C\epsilon(E^2+\tau U^2)$","#f4ecf5"),
        (0.68,0.42,0.31,0.40,"Nested error: (5.3)",r"$|([T,[T^*,C_T]]v,v)|$"+"\n"+r"$\leq C\epsilon^3U^2$","#faf1df"),
    ]
    for x,y,width,height,title,formula,color in boxes:
        ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle="round,pad=0.012",fc=color,ec="#ccd7dd"))
        ax.text(x+width/2,y+height*0.73,title,ha="center",fontsize=11,weight="bold")
        ax.text(x+width/2,y+height*0.26,formula,ha="center",fontsize=12)
    ax.text(0.5,0.27,r"$E^2=\|P^*v\|^2+([P^*,P]v,v)$; fixed small $\epsilon$, then allowed large $\tau$: $\tau U^2\leq CE^2$.",ha="center",fontsize=11,color="#246149")
    ax.text(0.5,0.10,r"First factor: $\tau^2X^2+\|v\|_{H^1}^2\leq C\tau U^2$; final estimate: $\tau^2X^2+\|Dv\|^2\leq CE^2$.",ha="center",fontsize=11,color="#246149")
    fig.text(0.05,0.044,r"$X=\|v\|,\ U=\|Tv\|,\ V=\|T^*v\|,\ E=\|Pv\|$; compact time / Schwartz space. Constants and thresholds are proved in Sections 2–5.",fontsize=9,color="#536172")
    fig.text(0.05,0.024,"Hörmander IV, Proposition 28.1.4, pp.224–228. Smooth example and figure original; reproducible Python source; CC0.",fontsize=9,color="#536172")
    fig.savefig(Path(__file__).with_name("root-exchange-and-curvature.png"),dpi=150,facecolor=fig.get_facecolor())
    plt.close(fig)
