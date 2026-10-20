"""Exact sections for Q(t,x,y)=t^2-x^2-y^2. Original figure: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,3,figsize=(14,4.8),layout="constrained")
blue="#176db0";orange="#c95a12";purple="#703fa0"
t=np.linspace(-1.5,1.5,601)
ax=axes[0]
ax.plot(t,t,color=blue,label=r"$Q=0,\ y=0$")
ax.plot(t,-t,color=blue)
point=np.array([1.,1.]);normal=np.array([2.,-2.])
ax.scatter(*point,color="black",s=25,zorder=4)
for sign,color in [(1,orange),(-1,purple)]:
    end=point+sign*.18*normal
    ax.annotate("",xy=end,xytext=point,arrowprops=dict(arrowstyle="->",color=color,lw=2))
ax.text(.02,.97,r"$dQ(1,1,0)=(2,-2,0)$",transform=ax.transAxes,va="top",fontsize=10)
ax.text(.02,.04,r"Arrows: $\pm0.18(2,-2)$",transform=ax.transAxes,fontsize=10)
ax.set_title("Both conormal signs away from the vertex",fontsize=11)
ax.set(xlabel=r"$t$",ylabel=r"$x$",xlim=(-1.65,1.65),ylim=(-1.65,1.65))
angles=np.linspace(0,2*np.pi,1201)
circle=np.column_stack([np.cos(angles),np.sin(angles)])
for ax in axes[1:]:
    ax.axhline(0,color=".75",lw=.6);ax.axvline(0,color=".75",lw=.6)
    ax.set(xlabel=r"$\tau$",ylabel=r"$\xi_x$",xlim=(-1.28,1.28),ylim=(-1.28,1.28))
axes[1].plot(circle[:,0],circle[:,1],color=blue,lw=2)
axes[1].set_title(r"$U_+,U_-,V_+$: every vertex direction",fontsize=11)
axes[1].text(.5,.5,r"$\xi_y=0$"+"\n"+r"$\tau^2+\xi_x^2=1$",ha="center",va="center",transform=axes[1].transAxes)
axes[2].plot(circle[:,0],circle[:,1],color=".75",lw=.8)
for sign in [1,-1]:axes[2].plot(t,sign*t,color=purple,ls="--",lw=.8)
for a in [-1,1]:
    for b in [-1,1]:axes[2].scatter(a/np.sqrt(2),b/np.sqrt(2),color=purple,s=50,zorder=4)
axes[2].set_title(r"$V_-$: only null vertex directions",fontsize=11)
axes[2].text(.5,.5,r"$\xi_y=0$"+"\n"+r"$\tau^2=\xi_x^2$",ha="center",va="center",transform=axes[2].transAxes,bbox=dict(facecolor="white",edgecolor="none",alpha=.95))
for ax in axes:
    ax.set_aspect("equal",adjustable="box")
    ax.grid(alpha=.13)
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(root/"quadratic-vertex-directions.png",dpi=180)
fig.savefig(root/"quadratic-vertex-directions.svg")
svg=root/"quadratic-vertex-directions.svg"
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
