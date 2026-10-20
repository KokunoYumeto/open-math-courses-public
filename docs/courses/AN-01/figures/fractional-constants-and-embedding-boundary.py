"""Exact fractional-energy constants and the weighted L2 embedding region.

Original illustration by GPT-6 Astra (OpenAI), CC0 1.0.
Theorem 2, Corollary 3 and Theorem 5 of the accompanying lesson prove
the formulas. Samples illustrate those proofs; they are not numerical evidence.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size":12,"svg.hashsalt":"AN01-fractional-constants-v1"})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout="constrained")
s=np.linspace(0,1,601)
colors=["#23618f","#a34d22","#588039"]
for n,color in zip([1,2,3],colors):
    # Stable extension of omega/(s*(1-s)*C_ns) through both endpoints.
    values=np.array([4**float(t)*math.gamma(n/2+float(t))/
                     (math.gamma(n/2)*math.gamma(2-float(t))) for t in s])
    assert abs(values[0]-1)<1e-12 and abs(values[-1]-2*n)<1e-12
    axes[0].plot(s,values,color=color,label=rf"$n={n}$",lw=2.2)
    axes[0].scatter([0,1],[1,2*n],color=color,s=32,zorder=3)
axes[0].set(xlabel=r"Fractional order $s$",ylabel=r"$\omega_{n-1}/[s(1-s)C_{n,s}]$",
            title="Exact normalization and its limits",xlim=(-.025,1.025),ylim=(.6,6.5))
axes[0].text(.04,1.35,"limit 1",fontsize=10)
axes[0].text(.77,6.16,r"limits $2n$",fontsize=10)
axes[0].legend(loc="upper left")
axes[0].grid(alpha=.2)

q=np.linspace(1,2,601)
boundary=2*(1/q-.5)
axes[1].fill_between(q,boundary,1.6,color="#d5e8df")
axes[1].plot(q,boundary,"--",color="#a34d22",lw=2,
             label=r"excluded: $s=2(1/q-1/2),\ q<2$")
axes[1].plot([2,2],[0,1.6],color="#23618f",lw=3,
             label=r"included: $q=2,\ s\geq0$")
axes[1].scatter([1],[1],facecolor="white",edgecolor="#a34d22",s=52,zorder=5)
axes[1].scatter([2],[0],color="#23618f",s=45,zorder=6)
axes[1].text(1.33,1.1,r"$L^2_s\subset L^q$",fontsize=15,color="#245b43")
axes[1].text(1.04,.06,"inclusion fails",fontsize=11,color="#81432a")
axes[1].set(xlabel=r"Target exponent $q$",ylabel=r"Weight order $s$",
            title=r"Sharp inclusion region in dimension $n=2$",
            xlim=(.97,2.04),ylim=(-.12,1.6))
axes[1].legend(loc="upper right",fontsize=9,framealpha=.96)
axes[1].grid(alpha=.2)
fig.savefig(out/"fractional-constants-and-embedding-boundary.png",dpi=160)
svg=out/"fractional-constants-and-embedding-boundary.svg"
fig.savefig(svg,metadata={"Date":None})
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
