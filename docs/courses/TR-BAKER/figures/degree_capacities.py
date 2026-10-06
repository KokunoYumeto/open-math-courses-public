"""Reproduce the exact degree-capacity example in the many-logarithm lesson."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

base = Path(__file__).resolve().parent
colors = ["#215B8F","#168575","#B86825","#8E4D8A"]
weights = []
fig, ax = plt.subplots(1,2,figsize=(11.5,4.2),layout="constrained")
for h in range(4):
    c = 5*(4-h)
    j = np.arange(c)
    ax[0].scatter(j,np.full(c,h),color=colors[h],s=28)
    ax[0].text(c-1+.7,h,f"{c} rows",va="center",fontsize=9)
    weights.extend(h+int(v) for v in j)
weights.sort()
assert len(weights) == 50 and sum(weights) == 400
trim = np.minimum(weights,10)
assert sum(trim) == 339
ax[0].set(xlim=(-.8,24),ylim=(-.5,3.5),yticks=range(4),
          xlabel="Radial Taylor index j",ylabel="Transverse degree |ρ|",
          title="Each group has 5(4 − |ρ|) rows")
ax[0].grid(axis="x",alpha=.2)
x = np.arange(1,51)
ax[1].step(x,weights,where="mid",color="#215B8F",label="Degree |ρ| + j")
ax[1].step(x,trim,where="mid",color="#8E4D8A",linewidth=2,
           label="Degree capped at 10")
ax[1].axhline(10,color="#8E4D8A",linestyle="--",alpha=.65)
edges = np.arange(.5,51.5)
ax[1].fill_between(edges,0,np.append(trim,trim[-1]),step="post",
                   color="#8E4D8A",alpha=.12)
ax[1].set(xlim=(.5,50.5),ylim=(0,20),xlabel="Position in the sorted degree list",
          ylabel="Degree",title="Capped sum = 339; mean = 339/50")
ax[1].legend(loc="upper left",fontsize=9)
ax[1].grid(alpha=.2)
fig.suptitle("Polynomial degree capacities: d = 2, T₀ = 3, 2T₁ + 1 = 5",
             fontsize=13)
fig.savefig(base/"degree-capacities.png",dpi=170)
fig.savefig(base/"degree-capacities.svg")
plt.close(fig)
print("degree-capacities.png: exact50-entry list, sum400, capped sum339")
