"""Nearest-face Gram comparison: exact coordinates, inspected render."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import numpy as np

BASE=Path(__file__).resolve().parent
P=np.array([[1,2],[1.1,2],[3,-3],[-3,-3],[-3,1]])
A=np.array([[0,0],[1,2],[1.1,2]])
C=np.array([[0,0],[1,0],[1,1]])
fig,axs=plt.subplots(1,3,figsize=(12.8,5.3),constrained_layout=True)
ax=axs[0]
ax.add_patch(Polygon(P,facecolor="#e4edf3",edgecolor="#315a80",linewidth=1.8))
ax.add_patch(Polygon(A,facecolor="#e8aa4b",edgecolor="#b56a12",linewidth=1.4))
ax.add_patch(Circle((0,0),1,fill=False,edgecolor="#577f66",linestyle="--"))
ax.plot(0,0,"o",color="#172934",markersize=4)
ax.set_xlim(-3.45,3.45);ax.set_ylim(-3.5,2.55)
ax.set_title(r"$P$, its unit ball, and $A$",fontsize=14)
ax.text(-2.7,1.5,r"$\mathrm{area}(P)=93/4$",fontsize=11)

ax=axs[1]
ax.add_patch(Polygon(A,facecolor="#f1c47e",edgecolor="#b56a12",linewidth=2))
ax.add_patch(Circle((0,0),1,fill=False,edgecolor="#577f66",linestyle="--"))
ax.scatter(A[:,0],A[:,1],color="#172934",s=18,zorder=4)
ax.annotate(r"$a_1=(1,2)$",xy=(1,2),xytext=(-.23,2.35),
            fontsize=11,arrowprops={"arrowstyle":"-","color":"#273844"})
ax.annotate(r"$a_2=(11/10,2)$",xy=(1.1,2),xytext=(.32,1.6),
            fontsize=11,arrowprops={"arrowstyle":"-","color":"#273844"})
ax.text(-.15,-.17,r"$a_0=0$",fontsize=11)
ax.set_xlim(-.4,1.75);ax.set_ylim(-.4,2.7)
ax.set_title("Nearest-face simplex",fontsize=14)

ax=axs[2]
ax.add_patch(Polygon(C,facecolor="#b9d7e8",edgecolor="#315a80",linewidth=2))
ax.add_patch(Circle((0,0),1,fill=False,edgecolor="#577f66",linestyle="--"))
ax.scatter(C[:,0],C[:,1],color="#172934",s=18,zorder=4)
ax.annotate(r"$c_1=(1,0)$",xy=(1,0),xytext=(.5,-.24),fontsize=11)
ax.annotate(r"$c_2=(1,1)$",xy=(1,1),xytext=(.22,1.16),fontsize=11)
ax.text(-.18,-.18,r"$c_0=0$",fontsize=11)
ax.set_xlim(-.4,1.45);ax.set_ylim(-.4,1.45)
ax.set_title(r"$f(A)=C$, with $|f(x)|\leq |x|$ on $A$",fontsize=14)

for ax in axs:
    ax.set_aspect("equal")
    ax.axhline(0,color="#b8c2c8",linewidth=.7,zorder=0)
    ax.axvline(0,color="#b8c2c8",linewidth=.7,zorder=0)
    ax.set_xlabel(r"$x$");ax.set_ylabel(r"$y$")
    for spine in ax.spines.values(): spine.set_color("#a4afb5")
fig.suptitle(r"$f(x,y)=(y/2,\ 10x-5y)$: compare Gram entries on positive combinations",
             fontsize=15)
fig.savefig(BASE/"face_gram.png",dpi=160)
fig.savefig(BASE/"face_gram.svg")
print({"coordinates":"exact decimal rational coordinates",
       "outputs":["face_gram.png","face_gram.svg"]})
