"""Original AN01-U132 figure: exact damping regions and the Fresnel function."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"axes.labelsize":12,"svg.hashsalt":"AN01-U132-half-space"})
fig,axes=plt.subplots(1,3,figsize=(16,5.4),layout="constrained")
lam=25.;radius=np.sqrt(2/lam);y=np.linspace(-radius,radius,601)
for ax in axes[:2]:
 ax.axhline(0,color="#353b42",lw=1.4)
 ax.set(xlim=(-.36,.36),ylim=(-.33,.12),xlabel=r"$y$",ylabel=r"$s$")
 ax.set_aspect("equal");ax.grid(alpha=.15)
 ax.text(-.34,.09,r"Boundary: $s=0$",fontsize=10)
axes[0].fill_between(y,y*y/2-1/lam,0,color="#21658a",alpha=.28)
axes[0].plot(y,y*y/2-1/lam,color="#21658a",lw=2)
axes[0].set_title(r"A. $f=i(y^2/2-s)$")
axes[0].annotate(r"$1/\lambda$",xy=(0,-1/lam),xytext=(.13,-.16),arrowprops=dict(arrowstyle="->"),fontsize=11)
axes[0].text(-.32,-.29,r"Normal width $\lambda^{-1}$",fontsize=11)
bottom=-np.sqrt(np.maximum(0,2/lam-y*y))
axes[1].fill_between(y,bottom,0,color="#b5521e",alpha=.25)
axes[1].plot(y,bottom,color="#b5521e",lw=2)
axes[1].set_title(r"B. $f=i(y^2+s^2)/2$")
axes[1].annotate(r"$\sqrt{2/\lambda}$",xy=(0,-radius),xytext=(.02,-.13),arrowprops=dict(arrowstyle="->"),fontsize=11)
rho=np.linspace(-4,4,801)
# Entire primitive: sum (i/2)^k rho^(2k+1)/(k!(2k+1)).
# On |rho|<=4 the integrated exponential remainder after 80 terms
# is at most 4*8^80/80!, which is below 1e-45.
term=rho.astype(complex);primitive=term.copy()
for k in range(1,80):
 term*=1j*rho*rho/(2*k)
 primitive+=term/(2*k+1)
F=np.sqrt(np.pi)/2*(1+1j)-primitive
ax=axes[2]
ax.plot(rho,F.real,color="#21658a",label=r"$\operatorname{Re}F(\rho)$",lw=2)
ax.plot(rho,F.imag,color="#b5521e",label=r"$\operatorname{Im}F(\rho)$",lw=2)
ax.axvline(0,color="#777777",ls=":",lw=1)
ax.scatter([0],[np.sqrt(np.pi)/2],color="black",s=24,zorder=4)
ax.set(xlabel=r"$\rho=\sqrt{\lambda}\,a$",ylabel="Fresnel tail",title="C. Crossing the boundary")
ax.grid(alpha=.18);ax.legend(loc="upper right",fontsize=10)
ax.text(.03,.03,r"$F(0)=\frac{\sqrt{\pi}}{2}(1+i)$",transform=ax.transAxes,fontsize=11)
fig.suptitle(r"Boundary scales and the Fresnel transition, $\lambda=25$ in A–B",fontsize=17)
fig.savefig(out/"half-space-scales-and-fresnel.png",dpi=150,facecolor="white")
fig.savefig(out/"half-space-scales-and-fresnel.svg",metadata={"Date":None})
p=out/"half-space-scales-and-fresnel.svg"
p.write_bytes(("\n".join(line.rstrip() for line in p.read_text(encoding="utf-8").splitlines())+"\n").encode())
print({"lambda":lam,"normal_endpoint_width":1/lam,"critical_radius":radius,"fresnel_terms":80,"fresnel_samples":801,"F0_real_imag":float(np.sqrt(np.pi)/2)})
