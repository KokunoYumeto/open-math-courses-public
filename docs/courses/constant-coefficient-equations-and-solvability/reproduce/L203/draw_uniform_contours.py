"""Reproduce the exact linear-family contour and finite-gap derivative-mass models."""
from pathlib import Path
import json,sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

OUT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent/"figures"
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"svg.fonttype":"none","svg.hashsalt":"uniform-compact-polynomial-contours"})
def finish(fig,name):
    fig.savefig(OUT/(name+".png"),dpi=180)
    svg=OUT/(name+".svg");fig.savefig(svg,metadata={"Date":None})
    svg.write_bytes(b"\n".join(line.rstrip(b" \t\r") for line in svg.read_bytes().split(b"\n")))
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(12.6,5.6),constrained_layout=True)
ax=axes[0];theta=np.linspace(0,2*np.pi,901)
ax.add_patch(Circle((0,0),1,facecolor="#efbf7b",edgecolor="#946124",alpha=.65))
ax.plot(2+4*np.cos(theta),4*np.sin(theta),color="#185a80",lw=2.2)
ax.axhline(0,color="#aaa",lw=.7);ax.axvline(0,color="#aaa",lw=.7)
ax.plot([2],[0],"o",color="#222",ms=5)
ax.annotate(r"center $\xi=2$",xy=(2,0),xytext=(2.2,-1),arrowprops={"arrowstyle":"->"},ha="left")
ax.text(0,.35,r"$|b|\leq1$",ha="center",color="#5b350c")
ax.plot([-2,-1],[0,0],color="#168358",lw=3)
ax.text(-1.5,-.65,"gap = 1",ha="center",color="#11603f")
ax.annotate(r"$w=2+4z,\ |z|=1$",xy=(4.8,2.85),xytext=(.8,4.5),arrowprops={"arrowstyle":"->","color":"#185a80"},color="#185a80",ha="center")
ax.set(xlim=(-3,7),ylim=(-5,5),aspect="equal",xlabel=r"$\operatorname{Re}w$",ylabel=r"$\operatorname{Im}w$")
ax.set_title("One circle for the entire root disk")
ax=axes[1]
ax.plot([-5,-2],[0,0],color="#185a80",lw=2.4)
ax.plot([2,5],[0,0],color="#185a80",lw=2.4)
ax.plot([-2,2],[4,4],color="#185a80",lw=2.4)
ax.plot([-2,2],[0,0],"o",mfc="white",mec="#185a80",ms=8,mew=1.6)
ax.plot([-2,2],[4,4],"o",color="#185a80",ms=7)
ax.text(0,4.25,r"$4$ on $[-2,2]$",ha="center")
ax.text(-3.4,.28,"0",ha="center");ax.text(3.4,.28,"0",ha="center")
ax.set(xlim=(-5,5),ylim=(-.6,5),xlabel=r"real frequency $\xi$",ylabel=r"real shift $\eta(\xi)$",xticks=[-5,-2,0,2,5],yticks=[0,4])
ax.grid(axis="y",alpha=.2);ax.set_title(r"The bounded Borel shift at $\rho=0$")
finish(fig,"a-common-circle-and-bounded-shift")

fig,(top,bottom)=plt.subplots(2,1,figsize=(12.6,7.2),gridspec_kw={"height_ratios":[3.2,1.5]},sharex=True,constrained_layout=True)
x=np.linspace(-1.1,9.5,800);q=[9,6,2];H=4
colors=["#6c4b8d","#bc6a17","#185a80"]
for j in range(3):
    top.plot(x,np.log(q[j])/np.log(H)+j*x,color=colors[j],lw=2.2,label=rf"$j={j}: \log_4(q_j)+{j}x$")
for grid in [0,3,6,9]:
    for ax in [top,bottom]:ax.axvline(grid,color="#168358" if grid==3 else "#bbb",lw=1.8 if grid==3 else .9,ls="-" if grid==3 else "--")
selected=np.log(2)/np.log(4)+2*3
top.plot([3],[selected],"*",color="#168358",ms=13)
top.annotate("first good candidate: r = 64",xy=(3,selected),xytext=(4,5),arrowprops={"arrowstyle":"->","color":"#168358"},color="#11603f",bbox={"facecolor":"white","edgecolor":"#ddd","pad":5})
top.set(ylabel=r"$\log_4(q_jr^j)$",ylim=(-1,21),title="One scale avoids every pairwise comparison window")
top.legend(loc="upper left",framealpha=.95)
pairs=[(0,1),(0,2),(1,2)]
for row,(i,j) in enumerate(pairs):
    center=np.log(q[i]/q[j])/np.log(H)
    lo=(center-1)/(j-i);hi=(center+1)/(j-i)
    bottom.fill_between([lo,hi],row-.28,row+.28,color="#e3b06f",alpha=.85)
    bottom.plot([lo,hi],[row,row],color="#895b23",lw=1)
bottom.set(yticks=[0,1,2],yticklabels=["pair 0 / 1","pair 0 / 2","pair 1 / 2"],ylim=(-.65,2.65),xlim=(-1.1,9.5),ylabel="bad intervals",xlabel=r"$x=\log_4 r$; labels also give each candidate radius")
bottom.set_xticks([0,3,6,9],["0\nr = 1","3\nr = 64","6\nr = 4096","9\nr = 262144"])
bottom.set_title(r"Bad means $1/4\leq(q_ir^i)/(q_jr^j)\leq4$; interval length $\leq2$",fontsize=12)
finish(fig,"separating-derivative-masses")
print(json.dumps({"status":"RENDERED","files":[p.name for p in sorted(OUT.glob("*"))]}))
