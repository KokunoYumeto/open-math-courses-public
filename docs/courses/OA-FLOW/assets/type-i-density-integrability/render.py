"""Exact interval model for NEXT_TYPE_I_DENSITY.md, TI49--TI53.
Run Python 3 with NumPy and Matplotlib. No downloads or external artwork.
render() returns SVG bytes, PNG bytes, and exact-data checks.
To export: s,p,c=render(); open("type-i-density.svg","wb").write(s);
open("type-i-density.png","wb").write(p).
"""
import io
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
DATA = {
    "spectral_intervals": [[-1, 1], [0, 2], [0.5, 1.5]],
    "multiplicity_edges": [-1, 0, 0.5, 1, 1.5, 2],
    "multiplicity_values": [1, 2, 3, 2, 1],
    "phase_interval": [0, 1],
    "phase_height_in_pi_units": 1/3,
    "kernel_domain": [-1, 1],
    "kernel_phase_in_pi_units": {"upper_left":1/3,"upper_right":0,"lower_left":0,"lower_right":-1/3},
    "conventions": "horizontal q_prime, vertical q; intervals half-open; endpoint null sets do not change operators",
    "proof_tags": ["TI49", "TI50", "TI52", "TI53"]
}
def render():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "mathtext.fontset": "dejavusans",
        "svg.fonttype": "none",
        "svg.hashsalt": "oa-flow-type-i-density-ti49-ti53-v1",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.labelsize": 13,
        "axes.titlesize": 14,
        "axes.titleweight": "semibold",
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })
    fig,axs=plt.subplots(1,3,figsize=(15.8,6.1),gridspec_kw={"width_ratios":[1.12,1.04,1]})
    fig.subplots_adjust(left=.052,right=.975,bottom=.31,top=.74,wspace=.38)
    blue="#2364a0"; red="#b9434c"; ink="#172839"; gray="#e4eaf0"
    fig.suptitle("Exact type-I density model: multiplicity, transfer function, inner action",x=.51,y=.965,fontsize=19,color=ink,weight="semibold")
    fig.text(.51,.889,r"$h_0=e^A$ on $K=\bigoplus_{j=1}^{3} L^2(S_j)$;  $M=B(K)\,\overline{\otimes}\,B(\ell^2)$;  $h=h_0\otimes1$",ha="center",fontsize=14,color=ink)
    ax=axs[0]
    edges=DATA["multiplicity_edges"];vals=DATA["multiplicity_values"]
    for a,b,v in zip(edges[:-1],edges[1:],vals):
        ax.add_patch(Rectangle((a,0),b-a,v,facecolor=blue,alpha=.16,edgecolor="none"))
        ax.plot([a,b],[v,v],color=blue,lw=3,solid_capstyle="butt")
        ax.plot(a,v,"o",ms=5,color=blue)
        ax.plot(b,v,"o",ms=5,mfc="white",mec=blue)
    ax.axhline(0,color=ink,lw=.8)
    ax.set(xlim=(-1.18,2.18),ylim=(-.1,3.5),xticks=[-1,0,.5,1,1.5,2],yticks=[0,1,2,3],xlabel=r"$q=\log\lambda$",ylabel="multiplicity in B(K)")
    ax.set_xticklabels(["−1","0","½","1","1½","2"])
    ax.set_title("A  Varying spectral multiplicity",loc="left",pad=15)
    ax.text(.5,-.28,r"$m=1_{[-1,1)}+1_{[0,2)}+1_{[1/2,3/2)}$",transform=ax.transAxes,ha="center",fontsize=12)
    ax.text(.5,-.43,"Exact projection p in TI12; model TI49–TI50",transform=ax.transAxes,ha="center",fontsize=10.5,color=ink)
    ax=axs[1]
    for a,b,y in [(-1,0,0),(0,1,1/3),(1,2,0)]:
        ax.plot([a,b],[y,y],color=red,lw=3,solid_capstyle="butt")
    for x,y in [(0,1/3),(1,0)]:ax.plot(x,y,"o",color=red,ms=6)
    for x,y in [(0,0),(1,1/3)]:ax.plot(x,y,"o",mfc="white",mec=red,ms=6)
    ax.set(xlim=(-1.18,2.18),ylim=(-.08,.43),xticks=[-1,0,1,2],yticks=[0,1/3],xlabel=r"$q$",ylabel=r"phase of $b(q)$")
    ax.set_yticklabels(["0",r"$\pi/3$"])
    ax.set_title("B  A discontinuous transfer",loc="left",pad=15)
    ax.text(.5,-.28,r"$b(q)=\exp\!\left(\frac{\pi i}{3}1_{[0,1)}(q)\right)$",transform=ax.transAxes,ha="center",fontsize=12)
    ax.text(.5,-.43,"All-times strong continuity: TI38, TI52",transform=ax.transAxes,ha="center",fontsize=10.5,color=ink)
    ax=axs[2]
    colors={(0,0):gray,(0,1):red,(1,0):blue,(1,1):gray}
    labels={(0,0):"0",(0,1):r"$+\pi/3$",(1,0):r"$-\pi/3$",(1,1):"0"}
    for i in range(2):
        for j in range(2):
            ax.add_patch(Rectangle((-1+i,-1+j),1,1,facecolor=colors[i,j],edgecolor="white",lw=2))
            ax.text(-.5+i,-.5+j,labels[i,j],ha="center",va="center",fontsize=19,color="white" if i!=j else ink)
    ax.set(xlim=(-1,1),ylim=(-1,1),xticks=[-1,0,1],yticks=[-1,0,1],xlabel=r"input coordinate $q'$",ylabel=r"output coordinate $q$")
    ax.set_aspect("equal")
    ax.set_title("C  Exact kernel phase",loc="left",pad=15)
    ax.text(.5,-.28,r"$X(q,q')\mapsto b(q)\overline{b(q')}\,X(q,q')$",transform=ax.transAxes,ha="center",fontsize=12)
    ax.text(.5,-.43,"First summand: (−1,1)²; exact phases, TI53",transform=ax.transAxes,ha="center",fontsize=10.5,color=ink)
    fig.text(.052,.035,"Panel A concerns the specified type-I subfactor. The separate ℓ² factor makes the full centralizer properly infinite.",fontsize=11,color=ink)
    svg=io.BytesIO();png=io.BytesIO()
    fig.savefig(svg,format="svg",metadata={"Date":None,"Creator":"Original exact plotting source; CC0 new expression","Title":"Type-I density: TI49–TI53"})
    fig.savefig(png,format="png",dpi=150,metadata={"Software":"Matplotlib; deterministic type-I density renderer"})
    plt.close(fig)
    mids=[(a+b)/2 for a,b in zip(edges[:-1],edges[1:])]
    actual=[sum(a<=q<b for a,b in DATA["spectral_intervals"]) for q in mids]
    assert actual==vals
    assert DATA["kernel_phase_in_pi_units"]["upper_left"]==DATA["phase_height_in_pi_units"]
    checks={"multiplicity_at_interval_midpoints":actual,"rank_one_weight":math.e-1,"kernel_phase_signs":"upper-left +pi/3; lower-right -pi/3","render_type":"exact rectangles and interval segments; no sampled field"}
    return svg.getvalue(),png.getvalue(),checks
if __name__ == '__main__':
    from pathlib import Path
    directory = Path(__file__).resolve().parent
    svg, png, checks = render()
    (directory / 'tid-models.svg').write_bytes(svg)
    (directory / 'tid-models.png').write_bytes(png)
    print(json.dumps(checks, sort_keys=True))
