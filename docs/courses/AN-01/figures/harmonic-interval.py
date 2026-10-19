"""Exact interval Poisson field for AN01-U096, Theorems 4–6 and Exercise 4.
Original figure: GPT-6 Astra (OpenAI), Ultra, October 2026. CC0.
Run with numpy and matplotlib in this directory; writes PNG and SVG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
matplotlib.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","svg.hashsalt":"AN01-U096-harmonic-interval"})
out=Path(__file__).resolve().parent
def field(x,t):
 return (np.arctan((1-x)/t)+np.arctan((1+x)/t))/(2*np.pi)
x=np.linspace(-2.2,2.2,701);t=np.linspace(-1.1,1.1,500)
X,T=np.meshgrid(x,t);U=field(X,T)
assert np.max(abs(U+field(X,-T)))<1e-14
for h in [.15,.45]:
 assert abs(field(0,h)-np.arctan(1/h)/np.pi)<1e-14
assert abs(field(1,1e-7)-.25)<1e-6
fig,axs=plt.subplots(1,2,figsize=(12.6,4.9),layout="constrained")
ax=axs[0]
im=ax.pcolormesh(X,T,U,cmap="RdBu_r",vmin=-.5,vmax=.5,shading="auto",rasterized=True)
for sign in [-1,1]:
 rows=sign*t>0
 levels=[-.4,-.25,-.1] if sign<0 else [.1,.25,.4]
 cont=ax.contour(X[rows],T[rows],U[rows],levels=levels,colors="#424b58",linewidths=.65)
 positions=[(1.5,sign*.57),((-.45 if sign>0 else .65),sign*(.89 if sign>0 else .76)),(.2,sign*.31)]
 ax.clabel(cont,fmt="%g",fontsize=9,manual=positions)
ax.plot([-1,1],[0,0],color="#141b22",lw=4)
ax.annotate(r"Carrier $[-1,1]\times\{0\}$",xy=(.2,0),xytext=(-.1,-.93),ha="center",bbox={"facecolor":"white","alpha":.9,"edgecolor":"none"},arrowprops={"arrowstyle":"->","color":"#172334"},fontsize=10)
ax.set(xlim=(-2.2,2.2),ylim=(-1.1,1.1),xlabel=r"$x$",ylabel=r"$t$",title="Harmonic off the interval")
fig.colorbar(im,ax=ax,label=r"Exact field $U_u(x,t)$",shrink=.85)
ax=axs[1]
colors={.15:"#a12f32",.45:"#e5875c",-.15:"#235788",-.45:"#66a4d0"}
for h in [.15,.45,-.15,-.45]:ax.plot(x,field(x,h),color=colors[h],lw=2,label=f"t = {h:+.2f}")
ax.plot([-2.2,-1,-1,1,1,2.2],[0,0,.5,.5,0,0],"--",color="#7c8490",lw=1.2,label=r"Upper limit $\frac{1}{2}\mathbf{1}_{(-1,1)}$")
ax.plot([-2.2,-1,-1,1,1,2.2],[0,0,-.5,-.5,0,0],"--",color="#7c8490",lw=1.2)
ax.scatter([-1,1,-1,1],[.25,.25,-.25,-.25],color="#414b58",s=18,zorder=4,label=r"Endpoint limits $\pm1/4$")
ax.axhline(0,color="#9ca4ad",lw=.7);ax.grid(alpha=.17)
ax.set(xlim=(-2.2,2.2),ylim=(-.56,.56),xlabel=r"$x$",ylabel=r"$U_u(x,t)$",title="The interior limits differ by one")
ax.legend(fontsize=9,loc="upper center",bbox_to_anchor=(.5,-.15),ncol=2,frameon=False)
fig.savefig(out/"harmonic-interval.png",dpi=160,metadata={"Software":"Matplotlib; original CC0 figure"})
fig.savefig(out/"harmonic-interval.svg",metadata={"Date":None,"Creator":"GPT-6 Astra (OpenAI), Ultra; CC0"})
p=out/"harmonic-interval.svg";p.write_text("\n".join(line.rstrip() for line in p.read_text().splitlines())+"\n")
plt.close(fig)
