"""Quartic roots, a crossing strip and exact overlap mass. Original, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
out=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(14,4.5),layout="constrained")
theta=np.linspace(0,2*np.pi,501)
axs[0].plot(np.cos(theta),np.sin(theta),color="#aaaaaa",lw=1,ls=":")
roots=np.exp(1j*(np.pi/12+np.pi/4+np.arange(4)*np.pi/2))
for j,z in enumerate(roots):
    color="#075e83" if z.imag>0 else "#a45a29"
    axs[0].plot(z.real,z.imag,"o",color=color)
    axs[0].text(1.16*z.real,1.16*z.imag,rf"$\zeta_{j}$",color=color,ha="center",va="center")
axs[0].axhline(0,lw=.6,color="#777777");axs[0].axvline(0,lw=.6,color="#777777")
axs[0].set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$",title=r"$z^4+e^{i\pi/3}=0$")
axs[0].set_aspect("equal");axs[0].set_xticks([-1,0,1]);axs[0].set_yticks([-1,0,1])
eps=.12;x=np.linspace(-1.8,1.8,801);xx,yy=np.meshgrid(x,x)
axs[1].contourf(xx,yy,np.abs(xx*yy),levels=[0,eps],colors=["#dce8ed"])
axs[1].contour(xx,yy,xx*yy,levels=[-eps,eps],colors=["#075e83"],linewidths=1)
axs[1].axhline(0,color="#a45a29",lw=1.5);axs[1].axvline(0,color="#a45a29",lw=1.5)
axs[1].plot(0,0,"o",color="#a45a29",ms=5)
axs[1].annotate(r"$|xy|\leq\varepsilon$",xy=(.8,.07),xytext=(.8,.62),ha="center",arrowprops={"arrowstyle":"->","color":"#075e83"})
axs[1].set(xlim=(-1.8,1.8),ylim=(-1.8,1.8),xlabel="$x$",ylabel="$y$",title=r"A crossing strip: $\varepsilon=0.12$")
axs[1].set_aspect("equal");axs[1].set_xticks([-1,0,1]);axs[1].set_yticks([-1,0,1])
eps=.04;d=np.linspace(-2,2,1001)
axs[2].plot(d,2/(d*d+4*eps),lw=2,color="#075e83")
axs[2].plot([0],[1/(2*eps)],"o",color="#a45a29")
axs[2].text(1.05,8.8,r"$M_\varepsilon/\pi=\frac{2}{(a-b)^2+4\varepsilon}$",fontsize=10,ha="center")
axs[2].set(xlim=(-2,2),ylim=(0,14),xlabel="$a-b$",ylabel=r"$M_\varepsilon/\pi$",title=r"Overlap mass: $\varepsilon=0.04$")
axs[2].grid(alpha=.15)
for ext in ("png","svg"):
    p=out/f"crossings-roots-and-overlap.{ext}"
    fig.savefig(p,dpi=170,metadata={"Date":None} if ext=="svg" else {})
    if ext=="svg":p.write_text("\n".join(x.rstrip() for x in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
