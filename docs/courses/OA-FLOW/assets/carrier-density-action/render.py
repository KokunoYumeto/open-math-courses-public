"""Exact carrier/density bridge, CBD20, CBD25, CBD40--CBD41.
Python 3 + Matplotlib. render() returns SVG bytes, PNG bytes, checks.
No external artwork, files, downloads or sampled numerical approximations.
"""
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
DATA={"maps":{"top":"J_tau","bottom":"K_psi","right":"a -> a q_psi","left":"g -> g(log h_psi)"},"units":{"top_left":"1","top_right":"d","bottom_left":"s(psi)","bottom_right":"q_psi"},"s":0.25,"original_interval":[0,1],"flow_interval":[-0.25,0.75],"evaluation_intersection":[0,0.75],"proof_tags":["CBD20","CBD25","CBD40","CBD41"]}
def render():
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"mathtext.fontset":"dejavusans","svg.fonttype":"none","svg.hashsalt":"oa-flow-carrier-density-cbd20-v1","figure.facecolor":"white","savefig.facecolor":"white"})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(13.7,6.5),gridspec_kw={"width_ratios":[1.15,1]})
    fig.subplots_adjust(left=.04,right=.965,top=.77,bottom=.22,wspace=.30)
    ink="#193044";blue="#1f6795";red="#b44048";purple="#7553a3"
    fig.suptitle("The actual carrier evaluates to the fixed-trace density",y=.955,fontsize=21,weight="semibold",color=ink)
    fig.text(.5,.87,r"$\Theta_s q_\psi=q_{e^{-s}\psi}$  and  $\theta_sg(q)=g(q+s)$",ha="center",fontsize=15,color=ink)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
    ax.set_title("A  A commuting square of normal maps",loc="left",pad=21,fontsize=14,weight="semibold")
    def box(x,y,w,h,line1,line2):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.012,rounding_size=.018",facecolor="#edf4fa",edgecolor=blue,lw=1.3))
        ax.text(x+w/2,y+h*.65,line1,ha="center",va="center",fontsize=17,color=ink)
        ax.text(x+w/2,y+h*.24,line2,ha="center",va="center",fontsize=11,color=ink)
    box(.04,.72,.34,.22,r"$L^\infty(\mathbb{R},dq)$","unit 1")
    box(.63,.72,.32,.22,r"$\mathcal{A} d$","unit d")
    box(.04,.10,.34,.22,r"$Z(M_\psi)$",r"unit $s(\psi)$")
    box(.63,.10,.32,.22,r"$\mathcal{A} q_\psi$",r"unit $q_\psi$")
    def arrow(a,b):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=16,lw=1.65,color=ink))
    arrow((.405,.83),(.603,.83));ax.text(.50,.91,r"$J_\tau$",ha="center",fontsize=15,color=ink)
    arrow((.405,.21),(.603,.21));ax.text(.50,.29,r"$\mathcal{K}_\psi$",ha="center",fontsize=15,color=ink)
    arrow((.21,.68),(.21,.36));ax.text(.115,.515,"spectral calculus",rotation=90,ha="center",va="center",fontsize=11,color=ink)
    ax.text(.25,.515,r"$g(\log h_\psi)$",ha="left",va="center",fontsize=12,color=blue)
    arrow((.79,.68),(.79,.36));ax.text(.86,.515,r"$a\mapsto a q_\psi$",rotation=90,ha="center",va="center",fontsize=12,color=ink)
    ax.text(.50,-.105,r"$\mathcal{E}_\psi(J_\tau g)=\mathcal{K}_\psi^{-1}(J_\tau(g)q_\psi)=g(\log h_\psi)$",ha="center",fontsize=13,color=ink)
    bx.set_title("B  Positive flow time moves the interval left",loc="left",pad=21,fontsize=14,weight="semibold")
    bx.set_xlim(-.48,1.2);bx.set_ylim(-.60,2.65)
    for spine in ("top","left","right"):bx.spines[spine].set_visible(False)
    bx.spines["bottom"].set_position(("data",-.48))
    bx.set_yticks([]);bx.set_xticks([-.25,0,.25,.5,.75,1]);bx.set_xticklabels(["−¼","0","¼","½","¾","1"])
    bx.tick_params(axis="x",labelsize=12);bx.set_xlabel(r"logarithmic coordinate $q$",labelpad=10)
    rows=[(2,[0,1],blue,r"$q_\phi=J_\tau 1_{[0,1]}$"),(1,[-.25,.75],red,r"$\Theta_{1/4}(q_\phi)=J_\tau 1_{[-1/4,3/4]}$"),(0,[0,.75],purple,r"$\mathcal{E}_\phi(\Theta_{1/4}q_\phi)=E_{\log h}([0,3/4])$")]
    for y,(a,b),color,label in rows:
        bx.plot([a,b],[y,y],lw=11,color=color,solid_capstyle="butt")
        bx.plot([a,b],[y,y],"o",color=color,ms=6)
        bx.text(-.46,y+.22,label,fontsize=12,color=ink,va="bottom")
    for q in [-.25,0,.75,1]:
        bx.plot([q,q],[-.36,2.03],color="#d6dce2",ls=":",lw=.8,zorder=0)
    bx.add_patch(FancyArrowPatch((.60,1.63),(.35,1.63),arrowstyle="-|>",mutation_scale=15,color=red,lw=1.4))
    bx.text(.485,1.72,r"$s=1/4$",color=red,ha="center",fontsize=11)
    fig.text(.04,.079,"Exact maps: CBD20 and CBD25. Supported logarithms and corner units are explicit.",fontsize=11,color=ink)
    fig.text(.04,.036,"Exact interval model: CBD40–CBD41. The weight is faithful on M while its carrier is a proper cut of d.",fontsize=11,color=ink)
    sb=io.BytesIO();pb=io.BytesIO()
    fig.savefig(sb,format="svg",metadata={"Date":None,"Title":"Carrier evaluation and density calculus","Creator":"Original exact mathematical figure, CC0 new expression"})
    fig.savefig(pb,format="png",dpi=150,metadata={"Software":"Matplotlib; exact carrier-density bridge"})
    plt.close(fig)
    assert DATA["flow_interval"]==[x-DATA["s"] for x in DATA["original_interval"]]
    assert DATA["evaluation_intersection"]==[max(DATA["original_interval"][0],DATA["flow_interval"][0]),min(DATA["original_interval"][1],DATA["flow_interval"][1])]
    return sb.getvalue(),pb.getvalue(),{"flow_interval":DATA["flow_interval"],"evaluation_intersection":DATA["evaluation_intersection"],"exact_rational_endpoints":True,"kind":"commuting maps and exact intervals; no numerical approximation"}

if __name__ == '__main__':
    from pathlib import Path
    directory=Path(__file__).resolve().parent
    svg,png,checks=render()
    (directory/'cbd-maps.svg').write_bytes(svg)
    (directory/'cbd-maps.png').write_bytes(png)
    print(checks)
