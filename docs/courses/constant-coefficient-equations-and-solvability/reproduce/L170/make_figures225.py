"""Reproduce exact reflected support margins and cancellation geometry."""
from pathlib import Path
from tempfile import TemporaryDirectory
import os,json
OWN=Path(__file__).resolve().parent;FIG=OWN/"figures";FIG.mkdir(exist_ok=True)
with TemporaryDirectory(prefix="an02-own225-mpl-")as task_cache:
    os.environ["MPLCONFIGDIR"]=task_cache
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.titlesize":15,
                         "svg.hashsalt":"an02-support-distance225"})
    def save(fig,name):
        for ext in ["png","svg"]:
            fig.savefig(FIG/(name+"."+ext),dpi=160,bbox_inches="tight",
                metadata={"Creator":"Open Mathematics Courses"}if ext=="svg"else{"Software":"Open Mathematics Courses"})
        plt.close(fig)
    def bar(ax,bounds,y,color,closed=False):
        ax.plot(bounds,[y,y],color=color,lw=4,solid_capstyle="butt")
        ax.plot(bounds,[y,y],"o",mfc=color if closed else"white",mec=color,ms=8,mew=1.7)
    fig,ax=plt.subplots(figsize=(11,7.3))
    bar(ax,[-3,4],5,"#3862a2");bar(ax,[-1.75,3.5],4,"#14727a")
    bar(ax,[-.5,.75],3,"#8c4e9b",True)
    for interval in [[-1.75,-.5],[0,1.25]]:bar(ax,interval,2,"#8c4e9b",True)
    bar(ax,[-2,1.5],1,"#687777",True);bar(ax,[-.75,1],0,"#2b804a",True)
    for left,right,y,label in [(-1.75,-.5,3.35,r"$5/4$"),(-3,-1.75,2.35,r"$5/4$")]:
        ax.annotate("",xy=(right,y),xytext=(left,y),
            arrowprops={"arrowstyle":"<->","color":"#bb6723","lw":1.8})
        ax.text((left+right)/2,y+.13,label,ha="center",color="#9b531c",fontsize=13)
    for x,y0,y1 in [(-1.75,3.35,4),(-.5,3,3.35),(-3,2.35,5),(-1.75,2,2.35)]:
        ax.plot([x,x],[y0,y1],color="#c89169",lw=1,ls=":")
    ax.set_yticks([5,4,3,2,1,0],[
        r"$X_1=(-3,4)$",r"$Y=(-7/4,7/2)$",r"$T=[-1/2,3/4]$",
        r"$W=[-7/4,-1/2]\cup[0,5/4]$",r"$K_1=[-2,3/2]$",r"$K_2=[-3/4,1]$"])
    ax.set_xlim(-3.3,4.3);ax.set_ylim(-.45,5.55);ax.set_xticks([-3,-2,-1,0,1,2,3,4])
    ax.set_xlabel("real coordinate x");ax.grid(axis="x",alpha=.13)
    ax.set_title("An asymmetric kernel preserves the exact boundary margin",pad=16)
    ax.spines[["top","right","left"]].set_visible(False)
    fig.text(.5,.015,"Open circles: domain endpoints. Filled circles: compact endpoints. Orange arrows: equal left margins.",
        ha="center",fontsize=11)
    fig.tight_layout(rect=(0,.045,1,1));save(fig,"asymmetric-kernel-support-margins")
    fig,axes=plt.subplots(2,2,figsize=(12,7),gridspec_kw={"width_ratios":[1,1.45]})
    for row in [0,1]:
        ax=axes[row,0];ax.axhline(0,color="#8c9296",lw=.8)
        atoms=[(0,1),(1,1)]if row==0 else[(-1,-1),(1,1)]
        for x,c in atoms:
            color="#2b804a"if c>0 else"#a65078"
            ax.plot([x,x],[0,c],color=color,lw=2);ax.plot(x,c,"o",color=color,ms=7)
            ax.text(x,c+(.12 if c>0 else-.16),f"{c:+d}",ha="center",va="bottom"if c>0 else"top",color=color)
        if row==1:
            ax.plot(0,0,"x",color="#858585",ms=8,mew=1.5)
            ax.text(0,.28,"zero coefficient\ncancels",ha="center",color="#686868",fontsize=11)
        ax.set_xlim(-1.5,1.5);ax.set_ylim(-1.55,1.7);ax.set_xticks([-1,0,1])
        ax.set_yticks([-1,0,1]);ax.set_ylabel("atom coefficient")
        ax.set_title(r"$v=\delta_0+\delta_1$"if row==0 else r"$\check\mu*v=\delta_1-\delta_{-1}$",fontsize=14)
        ax.spines[["top","right"]].set_visible(False)
    eps=.125
    for row in [0,1]:
        ax=axes[row,1]
        intervals=[[-eps,eps],[1-eps,1+eps]]if row==0 else[[-1-eps,-1+eps],[1-eps,1+eps]]
        ax.plot([intervals[0][0],intervals[-1][1]],[0,0],color="#a5acaf",lw=1.2,ls="--")
        for interval in intervals:bar(ax,interval,0,"#8c4e9b",True)
        domain_left=-1 if row==0 else-2
        for edge in [domain_left,3]:ax.axvline(edge,color="#426b76",lw=1.1,ls=":")
        left=intervals[0][0]
        ax.annotate("",xy=(left,.5),xytext=(domain_left,.5),
            arrowprops={"arrowstyle":"<->","color":"#bb6723","lw":1.8})
        ax.text((domain_left+left)/2,.64,r"$7/8$",ha="center",color="#9b531c",fontsize=13)
        ax.set_xlim(-2.25,3.25);ax.set_ylim(-.55,1.1);ax.set_yticks([])
        ax.set_xticks([-2,-1,0,1,2,3]);ax.grid(axis="x",alpha=.12)
        ax.set_title(r"Support of $v_\varepsilon$ in $Y=(-1,3)$"if row==0
            else r"Support of $\check\mu*v_\varepsilon$ in $X_1=(-2,3)$",fontsize=13)
        ax.spines[["top","right","left"]].set_visible(False)
    for ax in axes[1]:ax.set_xlabel("real coordinate x")
    fig.suptitle(r"Cancellation survives mollification; $\varepsilon=1/8$",fontsize=16)
    fig.text(.5,.015,"Right panels show supports, not amplitudes. Dashed joins show hulls; the gaps remain outside the supports.",
        ha="center",fontsize=11)
    fig.tight_layout(rect=(0,.05,1,.95),h_pad=2,w_pad=2)
    save(fig,"cancellation-and-mollified-support-distances")
    geometry={"schema":"AN02-original-support-distance-geometry225/v1",
        "asymmetric_interval":{"kernel_support":["-1/2","5/4"],"kernel_coefficients":[1,-2],
            "X1":[-3,4],"Y":[-1.75,3.5],"T":[-.5,.75],"W":[[-1.75,-.5],[0,1.25]],
            "K1":[-2,1.5],"K2":[-.75,1],"exact_margin":"5/4",
            "domain_endpoints_open":True,"compact_endpoints_closed":True,
            "vertical_rows_are_labels":True,"proof_locator":"LearnerExample1,equationsL7–L11"},
        "cancellation":{"mu_atoms":[[0,1],[1,-1]],"v_atoms":[[0,1],[1,1]],
            "transpose_image_atoms":[[-1,-1],[1,1]],"cancelled_zero_coefficient":True,
            "X1":[-2,3],"Y":[-1,3],"epsilon":"1/8",
            "T_epsilon":[[-.125,.125],[.875,1.125]],"W_epsilon":[[-1.125,-.875],[.875,1.125]],
            "exact_margin":"7/8","dashed_joins_are_hulls_not_supports":True,
            "proof_locator":"LearnerExample2,equationsL12,L13"}}
    (FIG/"geometry225.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"FIGURES_WRITTEN","figure_pairs":2,"private_font_cache_removed":True}))
