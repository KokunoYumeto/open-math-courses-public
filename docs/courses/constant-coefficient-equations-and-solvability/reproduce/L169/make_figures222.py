"""Reproduce exact domain translations and boundary-escaping test supports."""
from pathlib import Path
from tempfile import TemporaryDirectory
from fractions import Fraction
import os,json
OWN=Path(__file__).resolve().parent;FIG=OWN/"figures";FIG.mkdir(exist_ok=True)
with TemporaryDirectory(prefix="an02-own222-mpl-")as task_cache:
    os.environ["MPLCONFIGDIR"]=task_cache
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.titlesize":15,
                         "svg.hashsalt":"an02-smooth-forcing222"})
    def save(fig,name):
        for ext in ["png","svg"]:
            fig.savefig(FIG/(name+"."+ext),dpi=160,bbox_inches="tight",
                metadata={"Creator":"Open Mathematics Courses"}if ext=="svg"else{"Software":"Open Mathematics Courses"})
        plt.close(fig)
    def bar(ax,bounds,y,color,closed=False,lw=4):
        ax.plot(bounds,[y,y],color=color,lw=lw,solid_capstyle="butt")
        ax.plot(bounds,[y,y],"o",mfc=color if closed else"white",mec=color,ms=8,mew=1.8)
    fig,ax=plt.subplots(figsize=(11,6))
    for interval in [[-3,-2],[1,2]]:bar(ax,interval,3,"#14727a")
    for interval in [[-3.75,-2.75],[.25,1.25]]:bar(ax,interval,1,"#3862a2")
    bar(ax,[1.25,1.75],2,"#2d8747",True);bar(ax,[.5,1],0,"#8c4e9b",True)
    ax.annotate("",xy=(.75,.18),xytext=(1.5,1.82),
        arrowprops={"arrowstyle":"->","lw":2,"color":"#644c85"})
    ax.text(1.5,1.48,r"$x\mapsto x-a,\ a=3/4$",fontsize=12,ha="left",color="#644c85")
    ax.annotate("",xy=(-3.25,1.16),xytext=(-2.5,2.84),
        arrowprops={"arrowstyle":"->","lw":1.5,"color":"#728d9d"})
    ax.text(-3.3,2.08,r"subtract $a$",fontsize=12,color="#526c7c")
    ax.set_yticks([3,2,1,0],[
        r"equation domain $X_2$",r"closed test support $K$",
        r"solution domain $X_1$",r"transpose support $K-a$"])
    ax.set_xlim(-4,2.65);ax.set_ylim(-.5,3.5);ax.set_xticks([-4,-3,-2,-1,0,1,2])
    ax.grid(axis="x",alpha=.15);ax.set_xlabel("real coordinate x")
    ax.set_title("A reflected transpose translates supports on disconnected domains",pad=18)
    ax.spines[["top","right","left"]].set_visible(False)
    fig.text(.5,.01,"Open circles: excluded domain endpoints. Filled circles: included compact-support endpoints.",
        ha="center",fontsize=11)
    fig.tight_layout(rect=(0,.045,1,1));save(fig,"disconnected-domains-and-transpose-supports")
    fig,axes=plt.subplots(2,1,figsize=(10,7),gridspec_kw={"height_ratios":[1,1.7]})
    ax=axes[0]
    bar(ax,[-2,2],2,"#3862a2");bar(ax,[-1.25,1.25],1,"#8c4e9b",True);bar(ax,[-1,1],0,"#14727a")
    ax.set_yticks([2,1,0],[r"$X_1=(-2,2)$",r"$K_1=[-5/4,5/4]$",r"$X_2=(-1,1)$"])
    ax.set_xlim(-2.2,2.2);ax.set_ylim(-.5,2.5);ax.set_xticks([-2,-1,0,1,2])
    ax.set_title("A fixed compact transpose support does not prevent test supports escaping")
    ax.spines[["top","right","left"]].set_visible(False);ax.grid(axis="x",alpha=.13)
    ax=axes[1];rows=[]
    for y,j in enumerate([16,8,4,2]):
        interval=[float(Fraction(1)-Fraction(5,4*j)),float(Fraction(1)-Fraction(3,4*j))]
        bar(ax,interval,y,"#b56a20",True,lw=5)
        ax.text(interval[0]-.035,y,f"j={j}",ha="right",va="center",fontsize=12,color="#875019")
        rows.append({"j":j,"support":interval,"exact_left":str(Fraction(1)-Fraction(5,4*j)),
                     "exact_right":str(Fraction(1)-Fraction(3,4*j))})
    ax.axvspan(1,1.3,color="#ece7e7");ax.axvline(1,color="#9d3d39",ls=":",lw=1.8)
    ax.text(1.055,2.25,"outside\n"+r"$X_2$",ha="left",color="#8b3633",fontsize=12)
    ax.set_xlim(0,1.3);ax.set_ylim(-.5,3.5);ax.set_yticks([])
    ax.set_xticks([0,.25,.5,.75,1,1.25]);ax.set_xlabel("real coordinate x; lower panel magnifies the right boundary")
    ax.spines[["top","right","left"]].set_visible(False);ax.grid(axis="x",alpha=.13)
    fig.tight_layout(h_pad=2);save(fig,"escaping-tests-and-fixed-transpose-support")
    geometry={"schema":"AN02-original-support-geometry222/v1",
        "translation":{"a":"3/4","X2":[[-3,-2],[1,2]],"X1":[[-3.75,-2.75],[.25,1.25]],
            "K":[1.25,1.75],"K_minus_a":[.5,1],"domain_endpoints_open":True,"compact_endpoints_closed":True,
            "vertical_rows_are_labels_not_a_second_spatial_coordinate":True,
            "proof_locator":"LearnerExample1,equationsL8,L9"},
        "escape":{"X1":[-2,2],"X2":[-1,1],"K1":[-1.25,1.25],"rows":rows,
            "kernel":"delta0,so transpose support equals original support",
            "limit_endpoint":1,"endpoint_excluded_from_X2":True,
            "proof_locator":"LearnerExample4,equationsL17–L19;FormalTheorem5.1"}}
    (FIG/"geometry222.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"FIGURES_WRITTEN","figure_pairs":2,"private_font_cache_removed":True}))
