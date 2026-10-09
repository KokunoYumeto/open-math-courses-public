"""Reproduce exact support geometry and the continuous causal inverse."""
from pathlib import Path
from fractions import Fraction
from tempfile import TemporaryDirectory
import json,math,os

OWN=Path(__file__).resolve().parent
OUT=OWN/"figures"
OUT.mkdir(exist_ok=True)
with TemporaryDirectory(prefix="an02-own246-mpl-")as config:
    os.environ["MPLCONFIGDIR"]=config
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
        "svg.hashsalt":"causal-vertex-stability246","axes.spines.top":False,
        "axes.spines.right":False})

    b,c=Fraction(1,5),Fraction(3,10)
    levels=[]
    for j in range(4):
        levels.append({"j":j,"points":[{"sigma":j,"chi":2*k-j,
            "coefficient":str(math.comb(j,k)*b**k*c**(j-k))}
            for k in range(j+1)]})
    fig,ax=plt.subplots(figsize=(9.3,8.1),layout="constrained")
    ax.fill([-4.8,0,4.8],[4.8,0,4.8],color="#edf2f7")
    ax.plot([-4.8,0,4.8],[4.8,0,4.8],color="#7d8ea1",lw=1.8)
    colors=["#182d45","#1676b8","#bd6c12","#aa3867"]
    for level in reversed(levels):
        j=level["j"];color=colors[j]
        for point in level["points"]:
            x,y=point["chi"],point["sigma"]
            ax.annotate("",xy=(x,4.65),xytext=(x,y),
                arrowprops={"arrowstyle":"->","color":color,"lw":1.7,"alpha":.6})
        xs=[p["chi"]for p in level["points"]]
        ax.scatter(xs,[j]*len(xs),s=82,color=color,zorder=5,
                   label=f"Level j = {j}")
        for point in level["points"]:
            ax.annotate(point["coefficient"],(point["chi"],point["sigma"]),
                        xytext=(7,9),textcoords="offset points",color=color,
                        fontsize=11,zorder=6)
    ax.axhline(12/5,color="#266d68",lw=2,ls="--")
    ax.text(-3.48,2.49,"Compact output cutoff: σ = 12/5",fontsize=12,
            color="#266d68",bbox={"facecolor":"white","alpha":.93,"edgecolor":"none"})
    ax.text(0,4.15,"σ ≥ |χ|",ha="center",fontsize=15,
            bbox={"facecolor":"white","alpha":.93,"edgecolor":"none"})
    ax.text(0,-.31,"Inverse vertex: (t,x) = (−3/5, 3/10)",
            ha="center",fontsize=11)
    ax.set(xlim=(-3.65,3.65),ylim=(-.47,4.8),
           xlabel="Centered transverse coordinate χ = x − 3/10",
           ylabel="Positive clock σ = t + 3/5",
           title="Delayed contributions start at clock j")
    ax.set_xticks(range(-3,4));ax.set_yticks(range(5))
    handles,labels=ax.get_legend_handles_labels()
    order=np.argsort([int(label[-1])for label in labels])
    ax.legend([handles[i]for i in order],[labels[i]for i in order],
              loc="lower right",framealpha=.96,fontsize=11)
    ax.grid(alpha=.14)
    for extension in ["png","svg"]:
        fig.savefig(OUT/f"delayed-powers-and-clock-cutoff.{extension}",
                    dpi=160,metadata={"Date":None}if extension=="svg"else None)
    plt.close(fig)

    t=np.linspace(0,1.5,601)
    exact=np.exp(t)-np.exp(-3*t)
    partial=[];current=np.zeros_like(t)
    for j in range(1,4):
        current=current+np.exp(-t)*(4**j)*t**(2*j-1)/math.factorial(2*j-1)
        partial.append(current.copy())
    fig,ax=plt.subplots(figsize=(9.6,6.2),layout="constrained")
    ax.fill_between(t,partial[-1],exact,color="#83bca3",alpha=.45,
                    label="Positive tail after three terms")
    for j,values in enumerate(partial,1):
        ax.plot(t,values,lw=2,ls=["--",":","-."][j-1],
                label=f"First {j} term"+(""if j==1 else"s"))
    ax.plot(t,exact,color="#173f34",lw=3,label="Exact density: exp(t) − exp(−3t)")
    ax.text(.04,.93,"The δ₀ term is separate from these function densities.",
            transform=ax.transAxes,fontsize=11,
            bbox={"facecolor":"white","alpha":.94,"edgecolor":"none"})
    ax.set(xlim=(0,1.5),ylim=(0,4.85),xlabel="Time t",
           ylabel="Regular inverse density",
           title="Continuous feedback converges on every compact interval")
    ax.legend(loc="upper left",bbox_to_anchor=(.015,.87),fontsize=10.5,framealpha=.96)
    ax.grid(alpha=.2)
    for extension in ["png","svg"]:
        fig.savefig(OUT/f"continuous-feedback-and-local-convergence.{extension}",
                    dpi=160,metadata={"Date":None}if extension=="svg"else None)
    plt.close(fig)

geometry={"schema":"causal-vertex-exact-geometry/v1","coordinates":["sigma=t+3/5","chi=x-3/10"],
    "cone":"sigma>=abs(chi)","a":["3/5","-3/10"],"b":"1/5","c":"3/10",
    "delayed_contribution_levels":levels,"each_ray":"chi=2k-j,sigma>=j",
    "coefficient_multiplies_density":"H(sigma-j)*exp(-(sigma-j))*(sigma-j)^j/j!",
    "clock_cutoff":"12/5","only_levels_below_cutoff":[0,1,2],
    "continuous_error":"4*t*H(t)*exp(-t)",
    "continuous_power_j":"H(t)*exp(-t)*4^j*t^(2j-1)/(2j-1)!",
    "exact_regular_inverse":"H(t)*(exp(t)-exp(-3*t))",
    "delta_term_drawn_as_function":False,"continuous_display_interval":["0","3/2"],
    "strictly_distinct_convergence_mechanisms":["locally finite delayed powers",
                                             "uniformly convergent factorial series"],
    "proof_locators":["Formal Theorems2.1,2.2,3.1","Learner Example2,E2.5–E2.8",
                      "Learner Example4,E4.2–E4.5"]}
(OUT/"geometry246.json").write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figures":2,"png_svg_pairs":2,"temporary_configuration_removed":True}))
