"""Original illustration for AN01-U131. Identities: C15,C31,C34,C36-C38."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"axes.labelsize":12,"svg.hashsalt":"AN01-U131-curvature"})
fig,axes=plt.subplots(1,3,figsize=(16,5.4),layout="constrained")
a,b=2.,1.;theta=np.deg2rad(35);omega=np.array([np.cos(theta),np.sin(theta)])
H=np.sqrt((a*omega[0])**2+(b*omega[1])**2);xp=np.array([a*a*omega[0],b*b*omega[1]])/H
K=H**3/(a*a*b*b);s=np.linspace(0,2*np.pi,801)
ax=axes[0];ax.plot(a*np.cos(s),b*np.sin(s),color="#21658a",lw=2.3)
ax.fill(a*np.cos(s),b*np.sin(s),color="#21658a",alpha=.07)
tangent=np.array([-omega[1],omega[0]])
for sign in [1,-1]:
 p=sign*xp;v=sign*omega
 ax.scatter(*p,color="#b5521e",s=35,zorder=4)
 ax.plot([p[0]-.9*tangent[0],p[0]+.9*tangent[0]],[p[1]-.9*tangent[1],p[1]+.9*tangent[1]],"--",color="#888888",lw=1.2)
 ax.annotate("",xy=p+.65*v,xytext=p,arrowprops=dict(arrowstyle="->",color="#b5521e",lw=2))
 ax.text(*(p+.75*v+sign*np.array([-.55,.25])),r"$x_+,\ \nu=\omega$" if sign==1 else r"$x_-,\ \nu=-\omega$",ha="center",va="center",fontsize=11)
ax.set(xlim=(-3,3),ylim=(-2,2),xlabel=r"$x_1$",ylabel=r"$x_2$",title="A. Two supporting points")
ax.set_aspect("equal");ax.grid(alpha=.18)
ax.text(.5,.02,r"$a=2,\ b=1,\ \theta=35^\circ$"+"\n"+r"$K(x_\pm)=H^3/(a^2b^2)$",transform=ax.transAxes,ha="center",va="bottom",bbox=dict(facecolor="white",alpha=.9,edgecolor="none"))
t=np.linspace(2,20,1601);leading=-4*np.pi*np.cos(t);exact=leading+4*np.pi*np.sin(t)/t
ax=axes[1];ax.plot(t,exact,label=r"$t^2\widehat{\chi_{B_1}}(t\omega)$",color="#21658a",lw=2)
ax.plot(t,leading,"--",label=r"$-4\pi\cos t$",color="#b5521e",lw=1.7)
ax.set(xlabel=r"$t$",ylabel="Scaled transform",title="B. The unit ball in three dimensions")
ax.grid(alpha=.2);ax.legend(loc="lower left",fontsize=10,framealpha=.92)
ax.text(.5,.98,r"Exact difference: $4\pi\sin(t)/t$",transform=ax.transAxes,ha="center",va="top",fontsize=10,bbox=dict(facecolor="white",alpha=.9,edgecolor="none"))
r=np.geomspace(.04,25,801);ax=axes[2]
ax.loglog(r,r,label=r"Boundary cost: $r$",color="#21658a",lw=2)
ax.loglog(r,r**(-.5),label=r"Frequency cost: $r^{-1/2}$",color="#b5521e",lw=2)
ax.scatter([1],[1],color="black",s=26,zorder=3);ax.axvline(1,color="#777777",ls=":",lw=1)
ax.set(xlabel=r"$r=h/t^{-1/3}$",ylabel=r"Cost divided by $t^{2/3}$",title=r"C. Balancing the bounds, $n=2$")
ax.grid(which="both",alpha=.2);ax.legend(loc="upper left",fontsize=10)
ax.annotate(r"$h=t^{-1/3}$",xy=(1,1),xytext=(1.8,.25),arrowprops=dict(arrowstyle="->",lw=1),fontsize=11)
fig.suptitle("Curvature phases and the smoothing balance",fontsize=18)
fig.savefig(out/"curvature-lattice-balance.png",dpi=150,facecolor="white")
fig.savefig(out/"curvature-lattice-balance.svg",metadata={"Date":None})
svg=out/"curvature-lattice-balance.svg"
svg.write_bytes(("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n").encode())
print({"ellipse_support":H,"normal_point":xp.tolist(),"curvature":K,"curve_samples":801,"transform_samples":1601,"bound_samples":801})
