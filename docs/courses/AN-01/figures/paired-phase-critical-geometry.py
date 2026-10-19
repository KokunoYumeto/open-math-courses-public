"""Exact polynomial phase and integer jet region in P10 and P24-P25.
Original figure by GPT-6 Astra (OpenAI), CC0.
Requires NumPy and Matplotlib; writes PNG and SVG beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,2,figsize=(12.8,5.8),constrained_layout=True)
x=np.linspace(-1.5,1.5,451);xi=np.linspace(-1.0,3.5,451)
X,Z=np.meshgrid(x,xi);phase=X**3/3-X*(Z-1)
contours=axes[0].contour(X,Z,phase,levels=[-1.5,-1,-.5,0,.5,1,1.5],
                        cmap="coolwarm",linewidths=1.1)
axes[0].clabel(contours,inline=True,fontsize=9,fmt="%g")
axes[0].plot(x,1+x*x,"--",color="#70419b",linewidth=2)
axes[0].axvline(0,color="#12736b",linewidth=1.7)
axes[0].scatter([0],[1],color="#172334",s=65,zorder=5)
axes[0].annotate("critical point (0, 1)",xy=(0,1),xytext=(-1.35,2.65),
                 arrowprops={"arrowstyle":"->","color":"#172334"},fontsize=11)
axes[0].set(title=r"Paired phase: $x^3/3-x(\xi-1)$",
            xlabel=r"$x$",ylabel=r"$\xi$",xlim=(-1.5,1.5),ylim=(-1,3.5))
axes[0].legend(handles=[
 Line2D([],[],color="#12736b",label=r"$\partial_\xi\Phi=-x=0$"),
 Line2D([],[],color="#70419b",linestyle="--",
        label=r"$\partial_x\Phi=x^2-(\xi-1)=0$")],loc="lower left",fontsize=10)
pairs=[(nu,mu) for nu in range(9) for mu in range(nu//2+1)]
assert len(pairs)==25
assert all(nu-mu >= (nu+1)//2 for nu,mu in pairs)
points=axes[1].scatter([nu for nu,mu in pairs],[mu for nu,mu in pairs],
                       c=[nu-mu for nu,mu in pairs],cmap="viridis",s=70,
                       vmin=0,vmax=8,zorder=3)
axes[1].plot([0,8],[0,4],"--",color="#505050",linewidth=1.3)
axes[1].set(title="Finite mixed-derivative indices",
            xlabel=r"mixed derivative order $\nu$",ylabel=r"phase power $\mu$",
            xlim=(-.45,8.5),ylim=(-.35,5.0),xticks=range(9),yticks=range(5))
axes[1].text(.15,4.55,r"$2\mu\leq\nu,\quad j=\nu-\mu\geq\lceil\nu/2\rceil$",fontsize=13)
bar=fig.colorbar(points,ax=axes[1],ticks=[0,2,4,6,8],shrink=.75,pad=.02)
bar.set_label(r"inverse-frequency order $j$")
for ax in axes:
 ax.grid(alpha=.17);ax.spines[["top","right"]].set_visible(False)
fig.suptitle("An explicit critical point and an exact derivative count",fontsize=17)
for ext in ["png","svg"]:fig.savefig(out/f"paired-phase-critical-geometry.{ext}",dpi=160)
plt.close(fig)
p=out/"paired-phase-critical-geometry.svg"
p.write_text("\n".join(s.rstrip() for s in p.read_text(encoding="utf-8").splitlines())+"\n",
             encoding="utf-8",newline="\n")
