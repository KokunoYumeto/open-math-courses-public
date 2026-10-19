"""Gaussian scales, radial support terms and a joint pole limit. Original, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
out=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(14,4.5),layout="constrained")
x=np.linspace(-5,5,2001)
for s,color in [(0.25,"#075e83"),(1,"#a45a29"),(4,"#476d47")]:
    axs[0].plot(x,s**(-.5)*np.exp(-x*x/(4*s)),color=color,lw=2,label=f"$s={s:g}$")
axs[0].set(xlabel="$x$",ylabel=r"$G_s(x)$",title="One mass, different widths",ylim=(0,2.2))
axs[0].text(-4.6,1.97,r"$\int_{\mathbb{R}}G_s=2\sqrt{\pi}$")
axs[0].grid(alpha=.15);axs[0].legend()
theta=np.linspace(0,2*np.pi,500)
axs[1].plot(np.cos(theta),np.sin(theta),lw=3,color="#075e83")
axs[1].plot(0,0,"o",color="#a45a29",ms=7)
axs[1].annotate(r"$-\pi\cos t\,\delta_0$",xy=(0,0),xytext=(-1.32,-.63),arrowprops={"arrowstyle":"->","color":"#a45a29"},color="#a45a29")
axs[1].annotate(r"$\sigma_{S^1}$",xy=(.7,.714),xytext=(.82,1.04),arrowprops={"arrowstyle":"->","color":"#075e83"},color="#075e83")
axs[1].axhline(0,color="#999999",lw=.5);axs[1].axvline(0,color="#999999",lw=.5)
axs[1].set(xlim=(-1.55,1.55),ylim=(-1.4,1.4),xlabel="$x_1$",ylabel="$x_2$",title="The circle and its center")
axs[1].set_aspect("equal");axs[1].set_xticks([-1,0,1]);axs[1].set_yticks([-1,0,1])
lam=np.linspace(0,5,501)
axs[2].plot(lam,np.exp(-lam),color="#075e83",lw=2)
axs[2].plot([0,1],[1,np.exp(-1)],"o",color="#a45a29")
axs[2].annotate("$e^{-1}$",xy=(1,np.exp(-1)),xytext=(1.4,.55),arrowprops={"arrowstyle":"->"})
axs[2].set(xlim=(-.08,5),ylim=(-.03,1.08),xlabel=r"$\lambda=\varepsilon t$",ylabel=r"Coefficient divided by $-2\pi i$",title="The joint boundary-pole limit")
axs[2].grid(alpha=.15)
for ext in ("png","svg"):
    p=out/f"concentration-and-limit-parameters.{ext}"
    fig.savefig(p,dpi=170,metadata={"Date":None} if ext=="svg" else {})
    if ext=="svg":p.write_text("\n".join(x.rstrip() for x in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
