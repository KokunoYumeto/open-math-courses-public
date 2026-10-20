"""A smooth norming test for a finite complex measure.

Exact atom locations, phases and contributions for AN01-U008, Solution 6.
Original figure by GPT-6 Astra (OpenAI), 2026; CC0.
Requires NumPy and Matplotlib. Outputs are written beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
matplotlib.rcParams["svg.hashsalt"]="AN01-complex-mass-and-smooth-tests"
root=Path(__file__).resolve().parent
x=np.linspace(-2,4,1801)
def bump(a):
 z=(x-a)/.45
 b=np.zeros_like(z)
 inside=np.abs(z)<1
 b[inside]=np.exp(1-1/(1-z[inside]**2))
 return b
f=bump(-1)-1j*bump(1)-bump(3)
fig,ax=plt.subplots(1,2,figsize=(11,4.3),layout="constrained")
ax[0].plot(x,f.real,lw=2,color="#1a6b8c",label=r"$\operatorname{Re}f$")
ax[0].plot(x,f.imag,lw=2,color="#b85832",label=r"$\operatorname{Im}f$")
for a,label in [(-1,r"$2\delta_{-1}$"),(1,r"$i\delta_1$"),(3,r"$-3\delta_3$")]:
 ax[0].axvline(a,color="#747d8b",lw=.8,ls=":")
 ax[0].text(a,1.13,label,ha="center",fontsize=12)
ax[0].set(xlabel="x",ylabel="value of the smooth test",ylim=(-1.3,1.5),
          title="Disjoint bumps keep the supremum equal to one")
ax[0].set_xticks([-1,1,3])
ax[0].grid(alpha=.2);ax[0].legend(loc="lower left")
bars=ax[1].bar(["at −1","at 1","at 3"],[2,1,3],color=["#1a6b8c","#b85832","#608c61"],width=.55)
ax[1].bar_label(bars,labels=[r"$2\cdot1=2$",r"$i\cdot(-i)=1$",r"$(-3)\cdot(-1)=3$"],padding=5,fontsize=11)
ax[1].set(ylim=(0,3.8),ylabel="positive contribution to the integral",
          title=r"$\int f\,d\mu=2+1+3=|\mu|(\mathbb{R})=6$")
ax[1].grid(axis="y",alpha=.2);ax[1].set_axisbelow(True)
for suffix in ["png","svg"]:
 target=root/f"complex-mass-and-smooth-tests.{suffix}"
 fig.savefig(target,dpi=160,metadata={"Date":None} if suffix=="svg" else None)
 if suffix=="svg":
  target.write_text("\n".join(l.rstrip() for l in target.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8",newline="\n")
