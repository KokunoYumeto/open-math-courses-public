"""Exact two-dimensional illustrations for logarithmic lattice proofs.

Original figure: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
Source mechanism: Matveev 1999, section 9; Matveev 2000, section 18.
These are specified convex-body and exponent-support examples, not samples
of particular algebraic logarithms. Every plotted vertex is exact.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

square = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
clipped = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]
contracted = [(F(1, 2), F(1, 2)), (-1, 1),
              (F(-1, 2), F(-1, 2)), (1, -1)]

def area(vertices):
    return abs(sum(F(x1)*F(y2)-F(x2)*F(y1)
                   for (x1,y1),(x2,y2) in zip(vertices,vertices[1:]+vertices[:1])))/2

assert area(square) == 4 and area(clipped) == 3 and area(contracted) == 2
assert all(abs(x+y) <= 1 and abs(x) <= 1 and abs(y) <= 1 for x,y in contracted)

fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.1), constrained_layout=True)
for ax in axes:
    ax.add_patch(Polygon(square, facecolor="#ecf1f8", edgecolor="#8291a8", linewidth=1.6))
    ax.add_patch(Polygon(clipped, facecolor="#99d2c0", edgecolor="#226b58", linewidth=1.8))
    ax.set(xlim=(-1.3,1.3), ylim=(-1.3,1.3), xticks=[-1,0,1], yticks=[-1,0,1],
           xlabel=r"$w_1$", ylabel=r"$w_2$", aspect="equal")
    ax.axhline(0,color="#96a0ad",linewidth=.7)
    ax.axvline(0,color="#96a0ad",linewidth=.7)
    ax.spines[["top","right"]].set_visible(False)
axes[0].set_title(r"Clip the square by $|w_1+w_2|\leq1$", fontsize=13)
axes[0].text(0,0,"clipped area = 3",ha="center",va="center",
             bbox={"facecolor":"white","alpha":.9,"edgecolor":"none"})
axes[0].text(.78,.50,r"$w_1+w_2=1$",rotation=-45,ha="center",va="center",fontsize=10,
             bbox={"facecolor":"white","alpha":.85,"edgecolor":"none","pad":1})
axes[0].text(-.9,-.94,"original area = 4",fontsize=10,ha="left",
             bbox={"facecolor":"white","alpha":.9,"edgecolor":"none"})
axes[1].add_patch(Polygon(contracted,facecolor="#9b87cb",edgecolor="#4f357d",alpha=.85,linewidth=1.8))
axes[1].set_title("Contract the normal direction by 1/2",fontsize=13)
axes[1].annotate("",xy=(.5,.5),xytext=(1,1),
                 arrowprops={"arrowstyle":"->","color":"#4f357d","lw":2})
axes[1].text(0,0,"contracted area = 2",ha="center",va="center",
             bbox={"facecolor":"white","alpha":.9,"edgecolor":"none"})
fig.suptitle("One constraint gives the lower bound 4 × (1/2) = 2",fontsize=15)
dest = ROOT/"figures/clipped-logarithmic-body.png"
fig.savefig(dest,dpi=160)
plt.close(fig)

colors = {(0,0):"#3876b5",(1,0):"#b34732",(0,1):"#398469",(1,1):"#8461ad"}
fig, axes = plt.subplots(1,2,figsize=(11.2,5.1),constrained_layout=True)
for parity,color in colors.items():
    pts=[(i,j) for i in range(6) for j in range(6) if (i%2,j%2)==parity]
    axes[0].scatter([x for x,y in pts],[y for x,y in pts],c=color,s=64,
                    label=f"δ = {parity}",edgecolors="white",linewidths=.5)
selected=[(F(i,2),F(j,2)) for i in range(1,6,2) for j in range(0,6,2)]
assert len(selected)==9
assert all(x-F(1,2)==int(x-F(1,2)) and y==int(y) for x,y in selected)
axes[1].scatter([float(x) for x,y in selected],[float(y) for x,y in selected],
                c=colors[(1,0)],s=80,edgecolors="white",linewidths=.6)
for ax in axes:
    ax.set_aspect("equal")
    ax.grid(color="#d5dbe4",linewidth=.6)
    ax.set_axisbelow(True)
    ax.spines[["top","right"]].set_visible(False)
axes[0].set(xlim=(-.4,5.4),ylim=(-.4,6.25),xticks=range(6),yticks=range(6),
            xlabel=r"$\mu_1$",ylabel=r"$\mu_2$",title="The four parity classes")
axes[0].legend(loc="upper left",bbox_to_anchor=(0,1),ncol=2,fontsize=9,
               framealpha=.97,handletextpad=.2,columnspacing=.5)
axes[1].set(xlim=(-.3,2.9),ylim=(-.3,2.9),xticks=[.5,1.5,2.5],yticks=[0,1,2],
            xlabel=r"$\mu_1/2$",ylabel=r"$\mu_2/2$",
            title=r"Retain $\delta=(1,0)$ and halve")
axes[1].text(1.5,2.7,r"new support in $\mathbb{Z}^2+(1/2,0)$",ha="center",fontsize=11)
fig.suptitle("Independent square-root monomials split each zero into four conditions",fontsize=14)
parity_dest=ROOT/"figures/logarithmic-parity-division.png"
fig.savefig(parity_dest,dpi=160)
plt.close(fig)

RESULT={"clipped_body":{"vertices":clipped,"area":3,"lower_bound":2,
                        "map":[["3/4","-1/4"],["-1/4","3/4"]],
                        "path":str(dest)},
        "parity":{"old_support":"{0,1,2,3,4,5}^2","retained_class":[1,0],
                  "new_points":[[str(x),str(y)] for x,y in selected],
                  "path":str(parity_dest)}}
if __name__=="__main__":
    print(json.dumps(RESULT,indent=2))
