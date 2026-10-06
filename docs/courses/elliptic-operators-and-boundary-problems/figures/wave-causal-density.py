"""Reproduce the exact constant-metric wave section in WX3 and WT11.

The original coordinates are retained: G=diag(9,4), y=0, t=1,
H=diag(1/9,1/4), and w=H**(1/2)v=(v1/3,v2/2).
This draws the proved causal cross-section and its coordinate-volume map.
It does not depict a global variable-metric wave evolution.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,2,figsize=(11.8,5.4))
fig.subplots_adjust(left=.065,right=.965,bottom=.25,top=.79,wspace=.35)
color="#145b91"; fill="#d5eafa"; ray="#a54826"
for ax,rx,ry,names in [
    (axes[0],1,1,("$w_1$","$w_2$")),
    (axes[1],3,2,("$v_1=x_1$","$v_2=x_2$"))]:
    ax.add_patch(Ellipse((0,0),2*rx,2*ry,facecolor=fill,edgecolor=color,lw=2))
    ax.axhline(0,color="#777777",lw=.7);ax.axvline(0,color="#777777",lw=.7)
    ax.set_aspect("equal",adjustable="box")
    ax.set_xlim(-1.2*rx,1.2*rx);ax.set_ylim(-1.2*ry,1.2*ry)
    ax.set_xlabel(names[0]);ax.set_ylabel(names[1])
    ax.set_xticks([-rx,0,rx]);ax.set_yticks([-ry,0,ry])
    ax.spines[["top","right"]].set_visible(False)
    ax.plot([0,.6*rx],[0,.8*ry],color=ray,lw=2)
    ax.scatter([0,.6*rx],[0,.8*ry],s=28,color=ray,zorder=4)
axes[0].set_title(r"$|w|\leq1$",pad=10)
axes[1].set_title(r"$v_1^2/9+v_2^2/4\leq1$",pad=10)
axes[0].annotate(r"$w=(3/5,\,4/5)$",(.6,.8),xytext=(-1.06,.39),
                 arrowprops={"arrowstyle":"-","color":ray},color=ray,fontsize=10)
axes[1].annotate(r"$v=(9/5,\,8/5)$",(1.8,1.6),xytext=(-3.16,.8),
                 arrowprops={"arrowstyle":"-","color":ray},color=ray,fontsize=10)
fig.suptitle("Exact causal cross-section at t = 1, with source y = 0",
             fontsize=16,y=.98)
fig.text(.5,.88,r"$G=\mathrm{diag}(9,4),\quad H=\mathrm{diag}(1/9,1/4),"
                    r"\quad w=T v=(v_1/3,v_2/2)$",ha="center",fontsize=12)
fig.add_artist(FancyArrowPatch((.43,.50),(.50,.50),transform=fig.transFigure,
                             arrowstyle="<-",mutation_scale=17,color=color,lw=1.7))
fig.text(.465,.555,r"$T$",ha="center",color=color,fontsize=12)
fig.text(.5,.14,r"$\det T=1/6,\quad dv=6\,dw,\quad d\mu(v)=dv/6=dw$",
         ha="center",fontsize=13)
fig.text(.5,.073,r"$\delta(t,Tv)=6\,\delta(t)\delta_0(v),\qquad u_0=I_r,"
                    r"\quad u_\nu=0\ (\nu\geq1)$",ha="center",fontsize=12)
fig.text(.5,.022,"Filled sets: causal support at t = 1. Boundary points: s = 1.  Proof: WX3, WT11.",
         ha="center",fontsize=10,color="#444444")
for suffix in ["svg","png"]:
    fig.savefig(HERE/f"wave-causal-density.{suffix}",dpi=200,facecolor="white")
plt.close(fig)
