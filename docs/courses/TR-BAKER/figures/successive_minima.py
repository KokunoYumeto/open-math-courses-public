"""Exact affine geometry for the successive-minimum volume argument."""
from pathlib import Path
from fractions import Fraction as F
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

BASE=Path(__file__).resolve().parent
N=2
# Q_1=K/2. Vertices are exact rational coordinates.
q1=[(-F(7,12),-F(1,4)),(F(5,12),-F(1,4)),
    (F(7,12),F(1,4)),(-F(5,12),F(1,4))]
shapes=[q1,[(2*x,y) for x,y in q1],[(2*x,2*y) for x,y in q1]]
titles=[r"$P_2+Q_1$",r"$P_2+S_2Q_1$",r"$P_2+Q_2$"]
areas=[F(25,2),F(15),F(30)]
colors=["#b9d7e8","#88afcb","#4e7eac","#315a80","#1e3d5c"]

def polygon_area(vertices):
    return abs(sum(vertices[i][0]*vertices[(i+1)%4][1]-
                   vertices[(i+1)%4][0]*vertices[i][1]
                   for i in range(4)))/2

assert [polygon_area(p) for p in shapes]==[F(1,2),F(1),F(2)]
for n in range(1,11):
    count=2*n+1
    union=[count*F(1,2)*count,
           count*F(1,2)*(2*n+2),
           count*(2*n+2)]
    assert union[1]>=union[0] and union[2]==2*union[1]
    assert union[2]>=2*union[0]
    if n==N: assert union==areas

fig,axs=plt.subplots(1,3,figsize=(12.6,4.9),constrained_layout=True)
for ax,p,title,area in zip(axs,shapes,titles,areas):
    # Overlapping polygons in one horizontal row have the same fill.
    # Rows have disjoint interiors in all three panels.
    for row in range(-N,N+1):
        for col in range(-N,N+1):
            verts=np.array([(float(x)+col,float(y)+row) for x,y in p])
            ax.add_patch(Polygon(verts,closed=True,facecolor=colors[row+N],
                                 edgecolor="white",linewidth=.55))
            ax.plot(col,row,"o",markersize=2.8,color="#172934")
    ax.axhline(0,color="#263844",linestyle="--",linewidth=.85)
    ax.set_aspect("equal");ax.set_xlim(-3.45,3.45);ax.set_ylim(-2.85,2.85)
    ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2])
    ax.set_xlabel(r"$x$");ax.set_ylabel(r"$y$")
    ax.set_title(title,fontsize=15,pad=10)
    ax.text(.5,-.22,f"Area = {area}",transform=ax.transAxes,
            ha="center",fontsize=13,fontweight="bold")
    for spine in ax.spines.values(): spine.set_color("#a4afb5")
    ax.tick_params(labelsize=10)
fig.suptitle(r"Stretch $x$ first; then stretch $y$: $25/2\ \leq\ 15\ \mapsto\ 30$",
             fontsize=16)
fig.savefig(BASE/"successive_minima.png",dpi=160)
fig.savefig(BASE/"successive_minima.svg")
print({"vertices":"exact rationals","areas":[str(a) for a in areas],
       "finite_union_checks":10,"outputs":["successive_minima.png","successive_minima.svg"]})
