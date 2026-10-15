"""A contour proof of spectral addition (AL4).
CC0-1.0 to the extent of rights held.
The plotted bounds have their positive constant divided out; no orbit is sampled.
"""
from pathlib import Path
import json
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
    "svg.hashsalt":"oa-flow-arveson-contour-v1",
    "axes.spines.top":False,"axes.spines.right":False})
out=Path(__file__).resolve().parent
navy,teal,orange,purple="#17324d","#087f8c","#c26722","#8b5d9b"
fig=plt.figure(figsize=(13,9),facecolor="white")
gs=fig.add_gridspec(2,2,height_ratios=[1,1.5],hspace=.5,wspace=.32)
ax=fig.add_subplot(gs[0,:])
ax.set_title("A. Interval pieces retain the gap in the spectral sum",loc="left",
             fontsize=16,weight="bold",color=navy,pad=34)
rows=[(3,[(-4,-3),(3,4)],teal,r"$E$"),
      (2,[(0,.5)],purple,r"$F$"),
      (1,[(-4,-2.5),(3,4.5)],navy,r"$E+F$"),
      (0,[(-1,1)],orange,r"$\mathrm{supp}\,\rho$")]
for y,intervals,color,label in rows:
    for a,b in intervals:
        ax.plot([a,b],[y,y],color=color,lw=8,solid_capstyle="butt")
        ax.scatter([a,b],[y,y],s=22,color=color,zorder=3)
    ax.text(-4.65,y,label,ha="right",va="center",color=color,fontsize=12)
ax.axvspan(-1,1,color=orange,alpha=.07)
ax.set(xlim=(-5,5),ylim=(-.5,3.6),yticks=[],xlabel="Frequency r")
ax.set_xticks([-4,-3,-2.5,-1,0,.5,1,3,4,4.5])
ax.grid(axis="x",alpha=.15)
ax.spines["left"].set_visible(False)
ax.text(.5,1.025,r"$E=[-4,-3]\cup[3,4],\quad F=[0,1/2],\quad \mathrm{supp}\,\rho=[-1,1]$",
        transform=ax.transAxes,ha="center",color=navy)

ax=fig.add_subplot(gs[1,0])
ax.set_title("B. Shift toward exponential decay",loc="left",
             fontsize=15,weight="bold",color=navy,pad=14)
ax.set(xlim=(-3.8,3.8),ylim=(-2.4,2.4),xticks=[-3,0,3],xticklabels=[r"$-R$","0",r"$R$"],
       yticks=[-1.5,0,1.5],yticklabels=[r"$-iv$","0",r"$iv$"],
       xlabel="Real coordinate t (schematic)")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_bounds(-1.75,1.75)
ax.xaxis.set_label_coords(.5,-.04)
for y,col in [(1.5,teal),(0,navy),(-1.5,orange)]:
    ax.plot([-3,3],[y,y],color=col,lw=1.5)
    ax.annotate("",xy=(1.3,y),xytext=(.5,y),arrowprops={"arrowstyle":"->","color":col,"lw":2})
for x in [-3,3]:
    ax.plot([x,x],[-1.5,1.5],"--",color="#95a6ae",lw=1)
ax.annotate("",xy=(-2,1.5),xytext=(-2,.15),arrowprops={"arrowstyle":"->","color":teal,"lw":2})
ax.annotate("",xy=(2,-1.5),xytext=(2,-.15),arrowprops={"arrowstyle":"->","color":orange,"lw":2})
ax.text(0,2.06,"Test below the interval sum: shift up",ha="center",color=teal,fontsize=10)
ax.text(0,-2.06,"Test above the interval sum: shift down",ha="center",color=orange,fontsize=10)
ax.text(.5,-.30,"Horizontal integrals run left to right.\nVertical sides vanish as R tends to infinity.",
        transform=ax.transAxes,ha="center",fontsize=10,color=navy)

ax=fig.add_subplot(gs[1,1])
ax.set_title("C. Exponential decay controls the bound",loc="left",
             fontsize=14,weight="bold",color=navy,pad=14)
v=np.linspace(0,30,601)
gamma_up=Fraction(3)-2*Fraction(1,10)-1
gamma_down=Fraction(-1)-(Fraction(-5,2)+2*Fraction(1,10))
bounds={}
for name,gamma,color in [("up",gamma_up,teal),("down",gamma_down,orange)]:
    b=(1+v)**6*np.exp(-float(gamma)*v);bounds[name]=b
    ax.semilogy(v,b,color=color,lw=2.2,
        label=r"$\gamma=%s$"%("9/5" if name=="up" else "13/10"))
ax.set(xlim=(0,30),ylim=(1e-16,200),xlabel=r"Shift size $v\geq0$",ylabel="Bound with constant C divided out")
ax.grid(alpha=.17,which="major")
ax.legend(frameon=False,loc="upper right")
ax.text(.5,-.30,r"$(1+v)^6 e^{-\gamma v}\longrightarrow0$ for each $\gamma>0$."+"\n"+
        r"Reproducing-window enlargement: $\varepsilon=1/10$.",
        transform=ax.transAxes,ha="center",fontsize=10,color=navy)
fig.subplots_adjust(top=.91,bottom=.23,left=.08,right=.97)
fig.text(.08,.018,"AL4 proves both contour estimates and uses finite interval partitions for arbitrary compact spectra, then a bounded limit for closed spectra.",
         fontsize=10,color=navy)
fig.savefig(out/"arveson-contour.png",dpi=180,bbox_inches="tight")
fig.savefig(out/"arveson-contour.svg",bbox_inches="tight",metadata={"Date":None})
plt.close(fig)
assert gamma_up==Fraction(9,5) and gamma_down==Fraction(13,10)
samples=[{"v":float(v[k]),"up":float(bounds["up"][k]),"down":float(bounds["down"][k])}
         for k in (0,40,100,200,400,600)]
(out/"contour-bounds.json").write_text(json.dumps({
    "proof_locator":"OA-FLOW.AL.4","licence":"CC0-1.0 to the extent of rights held",
    "E":[["-4","-3"],["3","4"]],"F":[["0","1/2"]],
    "E_plus_F":[["-4","-5/2"],["3","9/2"]],"test_support":["-1","1"],
    "epsilon":"1/10","upward_gap":"9/5","downward_gap":"13/10",
    "bound":"C*(1+v)^6*exp(-gamma*v)","plot_normalization":"C=1 for comparison",
    "contours":"schematic horizontal comparison paths; vertical edges disappear in the proved R-to-infinity limit",
    "samples":samples,"samples_are_not_the_proof":True
},indent=2)+"\n",encoding="utf-8")
