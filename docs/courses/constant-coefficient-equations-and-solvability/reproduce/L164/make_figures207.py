"""Original exact carrier-translation and singular-locus illustrations."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
HERE=Path(__file__).resolve().parent;OUT=HERE/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"svg.fonttype":"path",
                     "svg.hashsalt":"singular-hull207","axes.grid":True,"grid.alpha":.18})
BLUE,GREEN,RED,GRAY="#15618a","#26774f","#b44236","#777777"
def save(fig,name):
    fig.savefig(OUT/(name+".png"),dpi=160,bbox_inches="tight",
                metadata={"Software":"Matplotlib;original mathematical figure"})
    fig.savefig(OUT/(name+".svg"),bbox_inches="tight",
                metadata={"Date":None,"Creator":"Original mathematical figure"})
    plt.close(fig)
def rect(ax,lo,hi,color,label,fill=True,alpha=.18,ls="-"):
    ax.add_patch(Rectangle(lo,hi[0]-lo[0],hi[1]-lo[1],edgecolor=color,facecolor=color if fill else "none",
                           alpha=alpha if fill else 1,lw=2,ls=ls,label=label))
K=([-3,-2],[5,4]);C=([1,-1],[2,1]);T=([-4,-1],[3,3]);DIFF=([-5,-3],[4,5])
good=(2,1);bad=(4,4)
fig,axes=plt.subplots(1,2,figsize=(12.4,5.4))
rect(axes[0],*DIFF,BLUE,r"Difference set $K-C$")
rect(axes[0],*T,GREEN,r"All translations with $C+x\subset K$",alpha=.32)
axes[0].scatter(*good,color=GREEN,s=55,zorder=5)
axes[0].scatter(*bad,color=RED,s=55,zorder=5)
axes[0].annotate(r"$x=(2,1)$",xy=good,xytext=(-2.8,1.7),color=GREEN,
                 arrowprops={"arrowstyle":"->","color":GREEN})
axes[0].annotate(r"$x=(4,4)$",xy=bad,xytext=(.2,5.3),color=RED,
                 arrowprops={"arrowstyle":"->","color":RED})
axes[0].set(xlim=(-6,5.5),ylim=(-4,6),xlabel=r"Translation coordinate $x_1$",
            ylabel=r"Translation coordinate $x_2$",title="Two different sets of translations")
axes[0].legend(loc="lower left",fontsize=9)
rect(axes[1],*K,GRAY,r"Output bound $K$",fill=False)
rect(axes[1],[3,0],[4,2],GREEN,r"$C+(2,1)$",alpha=.35)
rect(axes[1],[5,3],[6,5],RED,r"$C+(4,4)$",alpha=.35)
axes[1].set(xlim=(-4,7),ylim=(-3,6),xlabel=r"Physical coordinate $y_1$",
            ylabel=r"Physical coordinate $y_2$",title="The entire carrier must fit inside K")
axes[1].legend(loc="lower left",fontsize=9)
for ax in axes:ax.set_aspect("equal",adjustable="box")
fig.suptitle("Admissible carrier translations and the Minkowski difference",fontsize=14)
fig.tight_layout(rect=(0,0,1,.92));save(fig,"admissible-translations-and-difference-sets")

fig,axes=plt.subplots(1,3,figsize=(12.4,5.35))
for ax in axes:
    ax.set(xlim=(-1.4,1.4),ylim=(-.35,2.4),xlabel=r"First physical coordinate $x$",
           xticks=[-1,0,1],yticks=[0,1,2])
    ax.set_aspect("equal",adjustable="box")
    ax.axhline(0,color="#aaaaaa",lw=.6);ax.axvline(0,color="#aaaaaa",lw=.6)
axes[0].set_ylabel(r"Second physical coordinate $y$")
axes[0].plot([0,0],[0,2],color=GRAY,ls="--",lw=2,label=r"Hull $S_u=\{0\}\times[0,2]$")
axes[0].plot([0,0],[1,2],color=BLUE,lw=6,label="Line singularities")
axes[0].scatter([0],[0],color=BLUE,s=65,zorder=6,label="Isolated point mass")
axes[0].set_title(r"Known invertible input $u$")
axes[1].add_patch(Circle((0,0),.2,facecolor="#dfe6eb",edgecolor=GRAY,lw=1.3,
                        label=r"Allowed support ball $\varepsilon=1/5$"))
axes[1].scatter([0],[0],color=RED,s=65,zorder=6,label=r"$\operatorname{sing\,supp}w=\{0\}$")
axes[1].set_title("Selected compact factor")
axes[1].text(0,1.6,"Zero profile on the\nselected frequencies.",ha="center",va="center",fontsize=10,
             bbox={"facecolor":"white","edgecolor":"none","alpha":.85})
axes[2].plot([0,0],[0,2],color=GRAY,ls="--",lw=2,label=r"Sum $S_u+S_w$")
axes[2].scatter([0],[0],color=GREEN,s=75,zorder=6,label=r"Actual hull $S_{u*w}=\{0\}$")
axes[2].set_title("Exact selected convolution hull")
for ax in axes:ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),fontsize=8.8)
fig.suptitle("Invertibility does not force universal singular-hull addition",fontsize=14)
fig.tight_layout(rect=(0,0,1,.92));save(fig,"invertibility-without-universal-hull-addition")
geometry=dict(authorship="Original mathematics and figures;GPT-6.1 Sol (OpenAI),Ultra;CC0 1.0",
    rectangle_geometry=dict(K=K,C=C,all_admissible_translations=T,Minkowski_difference=DIFF,
        good_translation=good,good_translated_carrier=[[3,0],[4,2]],
        bad_translation=bad,bad_translated_carrier=[[5,3],[6,5]],
        geometric_example_does_not_prescribe_an_actual_profile_family=True,
        proof_locators=["Formal Theorem3.1","Formal Corollary6.1","Learner Exercise3"]),
    invertible_counterexample=dict(distribution="delta_(0,0)+(1/4)*(delta_0 tensor f)",
        f={"support":[1,2],"positive_on_interior":True,"smooth":True,"mass":1},
        real_Fourier_lower_bound=.75,input_singular_locus={"isolated_point":[0,0],"segment":[[0,1],[0,2]]},
        input_singular_hull=[[0,0],[0,2]],selected_profile_indicator="zero",
        selected_factor_singular_support=[[0,0]],selected_factor_support_bound_radius=.2,
        actual_selected_output_hull=[[0,0]],hull_sum=[[0,0],[0,2]],
        diagram_shows_singular_loci_not_distribution_densities=True,physical_axes_have_equal_scale=True,
        selected_factor_has_no_closed_formula_asserted=True,
        proof_locators=["Learner Example3","Formal Theorem2.1","Formal Theorem5.1"]),
    references=["Terence Tao,246B Notes2 and245B Notes9",
                "Lars Hörmander,Analysis of Linear Partial Differential Operators I and II"])
(OUT/"geometry207.json").write_text(json.dumps(geometry,indent=2,allow_nan=False)+"\n",encoding="utf-8")
print(json.dumps(dict(figures=2,formats=["PNG","SVG"],exact_geometry=True)))
