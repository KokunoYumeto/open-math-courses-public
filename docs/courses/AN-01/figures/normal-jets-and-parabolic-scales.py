"""Normal jets, directional uniqueness and exact parabolic scaling.

Original figure by GPT-6 Astra (OpenAI), October 2026. CC0.
Reproduce with Python, NumPy and Matplotlib; outputs are written beside this file.
The distribution markers are support/degree labels, not values of a function.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.hashsalt": "AN01-normal-jets-parabolic-scales"})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,2,figsize=(14,9.5),layout="constrained")
blue,orange,green="#2166ac","#c75a16","#238b45"

ax=axes[0,0]
ax.axhline(0,color=blue,lw=2)
for z,degree,color in [(-1,0,blue),(0,1,orange),(1,2,green)]:
    ax.scatter([z],[0],s=90,color=color,zorder=4)
    ax.annotate(r"$\partial_t^{%d}\delta_0(t)\otimes\delta_{%d}(z)$"%(degree,z),
                (z,0),xytext=(z,0.48 if degree!=1 else -0.55),
                ha="center",arrowprops={"arrowstyle":"-","color":color})
ax.set(xlim=(-1.65,1.65),ylim=(-.95,.95),xlabel=r"Tangential coordinate $z$",
       ylabel=r"Normal coordinate $t$",title="A. Finite normal degree, arbitrary tangential coefficients")
ax.text(-1.55,.78,r"$t^3u=0$   |   support and normal-degree markers",fontsize=10)
ax.set_xticks([-1,0,1]);ax.set_yticks([0])
ax.grid(alpha=.15)

ax=axes[0,1]
t=np.linspace(-1.15,1.15,501)
ax.axvline(0,color="0.35",ls="--",label=r"$\phi=t=0$")
ax.plot(t,-t,color=blue,label=r"$\psi_1=z+t=0,\quad X\psi_1=1$")
ax.plot(t,-t*t,color=orange,label=r"$\psi_2=z+t^2=0,\quad X\psi_2(0)=0$")
ax.scatter([0],[0],color="black",s=35,zorder=4)
ax.annotate("",xy=(.6,0),xytext=(0,0),arrowprops={"arrowstyle":"->","lw":2,"color":green})
ax.text(.3,.12,r"$X=\partial_t$",color=green,ha="center")
ax.set(xlim=(-1.15,1.15),ylim=(-1.4,1.2),xlabel=r"$t$",ylabel=r"$z$",
       title="B. The specified differentiation direction decides uniqueness")
ax.legend(loc="lower left",fontsize=9)
ax.grid(alpha=.15)

ax=axes[1,0]
v=np.linspace(-1,1,502)
x,y=np.meshgrid(v,v)
logmag=-.5*np.log10(x**4+y*y)
im=ax.pcolormesh(x,y,np.minimum(logmag,2),cmap="magma",vmin=-.16,vmax=2,shading="nearest",rasterized=True)
ax.scatter([0],[0],s=35,facecolors="none",edgecolors="#5de0d8",lw=1.5)
ax.set(xlabel=r"$x$",ylabel=r"$y$",title=r"C. First pole: $\log_{10}|(x^2+iy)^{-1}|$",aspect="equal")
fig.colorbar(im,ax=ax,label=r"$\log_{10}$ magnitude (capped at 2)",shrink=.85)

ax=axes[1,1]
for h,color in [(.8,blue),(.5,orange),(.25,green)]:
    ax.add_patch(Rectangle((.75*h,-.15*h*h),.5*h,.3*h*h,
                          facecolor=color,edgecolor=color,alpha=.25,lw=2))
    ax.text(h,.15*h*h+.018,f"$h={h:g}$",ha="center",color=color)
ax.scatter([0],[0],s=25,color="black")
ax.axhline(0,color="0.6",lw=.7)
ax.set(xlim=(-.05,1.1),ylim=(-.15,.24),xlabel=r"$x=hs$",ylabel=r"$y=h^2t$",
       title=r"D. Bounded test amplitude, unbounded pairing ($q=1,N=2$)")
ax.text(.04,.19,r"$\|\phi_h\|_\infty=\|\eta\|_\infty,\qquad U_{1,2}(\phi_h)=C_\eta/h$",fontsize=11)
ax.text(.04,-.135,r"Every box avoids $(0,0)$; widths scale as $h$ and $h^2$.",fontsize=10)
ax.grid(alpha=.15)
fig.suptitle("Normal constraints and anisotropic singularity scales",fontsize=18)
fig.savefig(out/"normal-jets-and-parabolic-scales.png",dpi=150)
svg=out/"normal-jets-and-parabolic-scales.svg"
fig.savefig(svg,metadata={"Date":None})
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
