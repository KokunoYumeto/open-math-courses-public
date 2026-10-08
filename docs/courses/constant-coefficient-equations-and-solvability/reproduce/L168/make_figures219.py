"""Reproduce the exact averaging and convex-exhaustion illustrations."""
from pathlib import Path
from tempfile import TemporaryDirectory
import os,json
OWN=Path(__file__).resolve().parent
FIG=OWN/"figures";FIG.mkdir(exist_ok=True)
with TemporaryDirectory(prefix="an02-own219-mpl-")as task_cache:
    os.environ["MPLCONFIGDIR"]=task_cache
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.titlesize":15,
                         "axes.labelsize":12,"svg.hashsalt":"an02-analytic-forcing219"})
    def save(fig,name):
        for ext in ["png","svg"]:
            fig.savefig(FIG/(name+"."+ext),dpi=160,bbox_inches="tight",
                        metadata={"Creator":"Open Mathematics Courses"}if ext=="svg"else{"Software":"Open Mathematics Courses"})
        plt.close(fig)
    fig,axes=plt.subplots(2,1,figsize=(10,7),sharex=True,gridspec_kw={"height_ratios":[1.4,1]})
    x=np.linspace(-3,3,1401);xx=np.linspace(-2,2,1001)
    ax=axes[0];ax.axvspan(-2,2,color="#e2f1ee")
    ax.plot(x,np.pi*x*np.sin(np.pi*x),color="#146b75",lw=2.6,label=r"$u(x)=\pi x\sin(\pi x)$")
    ax.plot([-3,3],[0,0],"o",mfc="white",mec="#146b75",ms=8,mew=1.8)
    ax.set_title("A resonant average has a smooth polynomial–oscillatory solution")
    ax.text(.5,.94,r"Solution domain $X=(-3,3)$",transform=ax.transAxes,va="top",ha="center",
            bbox={"facecolor":"white","edgecolor":"none","alpha":.92})
    ax.set_ylabel("solution");ax.legend(loc="lower center");ax.set_ylim(-9,9)
    ax=axes[1];ax.plot(xx,np.cos(np.pi*xx),color="#b65d18",lw=2.6,
        label=r"$\frac{1}{2}\int_{-1}^{1}u(x-y)\,dy=\cos(\pi x)$")
    ax.plot([-2,2],[1,1],"o",mfc="white",mec="#b65d18",ms=8,mew=1.8)
    ax.text(.5,.98,r"Equation domain $X_\mu=(-2,2)$",transform=ax.transAxes,va="top",ha="center",
            bbox={"facecolor":"white","edgecolor":"none","alpha":.92})
    ax.set_ylabel("average");ax.set_ylim(-1.6,1.6);ax.legend(loc="lower center");ax.set_xlabel("real coordinate x")
    for ax in axes:
        ax.axhline(0,color="#8a9498",lw=.8)
        for endpoint in [-2,2]:ax.axvline(endpoint,color="#6f8583",lw=1,ls=":")
        ax.set_xlim(-3.15,3.15);ax.set_xticks(np.arange(-3,4));ax.grid(axis="x",alpha=.13)
        ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout(h_pad=1.8);save(fig,"resonant-averaging-solution")
    fig,axes=plt.subplots(1,2,figsize=(11,6),sharey=True)
    rows=[]
    for j in range(1,5):
        gap=1/(j+1);source=[-4+gap,4-gap];equation=[-2+gap,4-gap]
        rows.append({"j":j,"gap":f"1/{j+1}","Y_j":source,"Z_j":equation,
                     "closure_margin_into_next":gap-1/(j+2),"open_endpoints":True})
        y=5-j
        for ax,endpoints,color in zip(axes,[source,equation],["#146b75","#a34b20"],strict=True):
            ax.plot(endpoints,[y,y],color=color,lw=4,solid_capstyle="butt")
            ax.plot(endpoints,[y,y],"o",mfc="white",mec=color,ms=8,mew=1.8)
            ax.text(np.mean(endpoints),y+.18,rf"$j={j},\ \delta_j=1/{j+1}$",
                    ha="center",fontsize=11,color=color)
    for ax,bounds,title,color in zip(axes,[[-4,4],[-2,4]],
            [r"Source intervals $Y_j=(-4+\delta_j,\,4-\delta_j)$",
             r"Equation intervals $Z_j=(-2+\delta_j,\,4-\delta_j)$"],
            ["#146b75","#a34b20"],strict=True):
        for endpoint in bounds:ax.axvline(endpoint,color=color,ls=":",lw=1.2)
        ax.set_title(title,fontsize=13);ax.set_xlim(-4.35,4.35);ax.set_ylim(.4,4.8)
        ax.set_xticks([-4,-2,0,2,4]);ax.set_xlabel("real coordinate x")
        ax.grid(axis="x",alpha=.12);ax.spines[["top","right","left"]].set_visible(False)
        ax.set_yticks([])
    fig.suptitle(r"Strict compact margins for a kernel with support $\{0,2\}$",fontsize=16,y=.98)
    fig.text(.5,.025,r"$\overline{Y_j}\subset Y_{j+1}$ and $\overline{Z_j}\subset Z_{j+1}$; open circles exclude every endpoint.",
             ha="center",fontsize=12)
    fig.tight_layout(rect=(0,.065,1,.94));save(fig,"convex-exhaustion-and-eroded-domains")
    geometry={"schema":"AN02-original-figure-coordinates219/v1",
        "resonant_average":{"X":[-3,3],"X_mu":[-2,2],"kernel":"uniform probability on [-1,1]",
            "u":"pi*x*sin(pi*x)","f":"cos(pi*x)","proof_locator":"Learner Example2,equationsL9–L11",
            "analytic_identity_not_inferred_from_samples":True},
        "convex_exhaustion":{"X":[-4,4],"support_mu":[0,2],"rows":rows,
            "union_Y_j":[-4,4],"union_Z_j":[-2,4],"endpoints_open":True,
            "proof_locator":"FormalSection5,equations5.1–5.6;LearnerSection4"}}
    (FIG/"geometry219.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"FIGURES_WRITTEN","figure_pairs":2,"private_font_cache_removed":True}))
