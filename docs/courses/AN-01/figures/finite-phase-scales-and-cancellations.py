"""Original AN01-U133 illustration of proved scales, cancellations and Airy data."""
from pathlib import Path
import math
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"axes.labelsize":12,"svg.hashsalt":"AN01-U133-finite-phases"})
fig,axes=plt.subplots(1,3,figsize=(16,5.4),layout="constrained")
lam=np.geomspace(1,10000,601)
for k,c in [(2,"#4f5964"),(3,"#21658a"),(4,"#b5521e"),(5,"#276744")]:
 axes[0].loglog(lam,lam**(-1/k),label=f"k = {k}",color=c,lw=2)
axes[0].set(xlabel=r"$\lambda$",ylabel=r"Width $\lambda^{-1/k}$",title="A. Finite order sets the spatial scale")
axes[0].legend(fontsize=10);axes[0].grid(alpha=.18,which="both")
for row,k,c in [(0,3,"#21658a"),(1,4,"#b5521e"),(2,5,"#276744")]:
 for j in range(15):
  zero=(j%2==1) if k%2==0 else ((j+1)%k==0)
  axes[1].scatter(j,row,marker="x" if zero else "o",s=70 if zero else 60,color="#959ca3" if zero else c,lw=1.8)
axes[1].set(xticks=range(0,15,2),yticks=range(3),yticklabels=["k = 3","k = 4","k = 5"],ylim=(-.55,2.55),xlabel=r"Amplitude jet degree $j$",title="B. Which coefficients vanish?")
axes[1].grid(axis="x",alpha=.13)
axes[1].text(.5,-.19,"Filled: nonzero moment    ×: zero moment",ha="center",transform=axes[1].transAxes,fontsize=10)
rho=np.linspace(-4,4,801);z=-rho
# Ai''=z Ai, so c[n+3]=c[n]/((n+3)(n+2)); c[2]=0.
co=np.zeros(100)
co[0]=3**(-1/6)*math.gamma(1/3)/(2*math.pi)
co[1]=-3**(1/6)*math.gamma(2/3)/(2*math.pi)
for n in range(97):co[n+3]=co[n]/((n+3)*(n+2))
profile=2*math.pi*np.polynomial.polynomial.polyval(z,co)
axes[2].plot(rho,profile,color="#21658a",lw=2)
axes[2].axvline(0,color="#777777",ls=":",lw=1)
axes[2].axhline(0,color="#777777",lw=.7)
axes[2].scatter([0],[2*math.pi*co[0]],color="black",s=24,zorder=4)
axes[2].set(xlabel=r"$\rho=y\lambda^{2/3}$",ylabel=r"$2\pi\,\operatorname{Ai}(-\rho)$",title="C. The cubic collision profile")
axes[2].text(.03,.96,"No real critical points",transform=axes[2].transAxes,va="top",fontsize=9)
axes[2].text(.99,.96,"Two real points",transform=axes[2].transAxes,ha="right",va="top",fontsize=9)
axes[2].grid(alpha=.16)
fig.suptitle("Finite-order phases: scales, missing powers and the cubic transition",fontsize=17)
fig.savefig(out/"finite-phase-scales-and-cancellations.png",dpi=150,facecolor="white")
fig.savefig(out/"finite-phase-scales-and-cancellations.svg",metadata={"Date":None})
p=out/"finite-phase-scales-and-cancellations.svg"
p.write_bytes(("\n".join(l.rstrip() for l in p.read_text(encoding="utf-8").splitlines())+"\n").encode())
# Rigorous analytic truncation majorant on |z|<=4, using |c0|,|c1|<1.
# Each of the two nonzero residue classes has a geometric tail after degree99.
first=[]
for residue in [0,1]:
 n=residue;term=Fraction(4**residue)
 while n<100:
  term*=Fraction(64,(n+3)*(n+2));n+=3
 first.append(term)
bound=sum(first)/(1-Fraction(64,100*99))
print({"width_samples":601,"moment_degrees":15,"airy_samples":801,"airy_coefficients":100,"airy_profile_analytic_tail_bound":float(2*math.pi*bound),"Ai0":co[0],"Ai_prime0":co[1]})
