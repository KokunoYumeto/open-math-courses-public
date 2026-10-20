"""Exact polygon support functions and signed boundary cancellation. Original figure: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.spines.top":False,
                    "axes.spines.right":False,"svg.hashsalt":"AN01-finite-support-envelopes"})
N=6;angles=2*np.pi*np.arange(N)/N
verts=np.column_stack((np.cos(angles),np.sin(angles)))
theta=np.linspace(0,2*np.pi,2401)
circle=np.column_stack((np.cos(theta),np.sin(theta)))
deficit=1-np.max(np.cos(theta[:,None]-angles),axis=1)
error=1-np.cos(np.pi/N)
normal=np.array([np.cos(np.pi/N),np.sin(np.pi/N)])
midpoint=np.cos(np.pi/N)*normal
fig=plt.figure(figsize=(12.5,8.6),constrained_layout=True)
gs=fig.add_gridspec(2,2,height_ratios=[1.5,1])
ax=[fig.add_subplot(gs[0,0]),fig.add_subplot(gs[0,1]),fig.add_subplot(gs[1,:])]
ax[0].fill(verts[:,0],verts[:,1],color="#b6dbe0",alpha=.6)
polygon=np.vstack((verts,verts[0]))
ax[0].plot(circle[:,0],circle[:,1],color="#444444",lw=1.6,label="Unit circle")
ax[0].plot(polygon[:,0],polygon[:,1],color="#126f82",lw=2,label=r"Convex envelope $C_6$")
ax[0].scatter(verts[:,0],verts[:,1],color="#126f82",s=22,zorder=4)
ax[0].plot([0,normal[0]],[0,normal[1]],color="#999999",lw=1,ls="--")
ax[0].plot([midpoint[0],normal[0]],[midpoint[1],normal[1]],color="#a34828",lw=5,zorder=5)
ax[0].annotate(r"$1-\sqrt{3}/2$",xy=(midpoint+normal)/2,xytext=(1.08,.83),
               arrowprops={"arrowstyle":"-","color":"#a34828"},color="#a34828",ha="center")
ax[0].set(title="Six points and their convex envelope",xlabel="$x_1$",ylabel="$x_2$",
          xlim=(-1.16,1.42),ylim=(-1.18,1.2),aspect="equal")
ax[0].legend(loc="lower left",fontsize=10,frameon=False)
ax[1].plot(theta,deficit,color="#126f82",lw=2.2,label=r"$1-H_{C_6}(\cos\theta,\sin\theta)$")
ax[1].axhline(error,color="#a34828",ls="--",lw=1.2,label=r"Sharp error $1-\sqrt{3}/2$")
ax[1].set(title="Directional support deficit",xlabel=r"Direction angle $\theta$",
          ylabel="Support deficit",xlim=(0,2*np.pi),ylim=(-.005,.172))
ax[1].set_xticks(np.linspace(0,2*np.pi,5),["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
ax[1].legend(loc="upper center",fontsize=10,frameon=False)
ax[1].grid(alpha=.2)
xx=np.array([-3,-2.5,-1.5,1.5,2.5,3])
yy=np.array([0,1,0,-1,0,0])
ax[2].step(xx,yy,where="post",color="#126f82",lw=2.2)
ax[2].fill_between([-2.5,-1.5],[1,1],color="#126f82",alpha=.22)
ax[2].fill_between([1.5,2.5],[-1,-1],color="#a34828",alpha=.22)
ax[2].plot([-2.5,2.5],[1.42,1.42],color="#777777",lw=3)
ax[2].text(0,1.50,"Full input-support sum",ha="center",fontsize=11)
ax[2].text(-2,.48,"+1",ha="center")
ax[2].text(2,-.58,"−1",ha="center")
ax[2].text(0,.22,"Zero on the interior overlap",ha="center",fontsize=11)
ax[2].set(title=r"Boundary cancellation: $1_{(-2,2)}*(\delta_{-1/2}-\delta_{1/2})$",
          xlabel="$x$",ylabel="Regular density",xlim=(-3,3),ylim=(-1.2,1.85))
ax[2].set_xticks([-2.5,-1.5,0,1.5,2.5])
ax[2].set_yticks([-1,0,1])
ax[2].axhline(0,color="#777777",lw=.6)
ax[2].grid(alpha=.15)
for ext in ["png","svg"]:
 fig.savefig(out/("finite-support-envelopes."+ext),dpi=170,
             metadata={"Date":None} if ext=="svg" else None)
p=out/"finite-support-envelopes.svg"
p.write_text("\n".join(x.rstrip() for x in p.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
