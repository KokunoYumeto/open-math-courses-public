"""CC0: exact finite projection and an exact countable L2 example."""
from pathlib import Path
import hashlib
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OWN=Path(__file__).resolve().parent
OUT=OWN/"figures"
OUT.mkdir(exist_ok=True)
matplotlib.rcParams.update({
    "font.family":"DejaVu Sans","font.size":15,"svg.hashsalt":"haar-radon-original-20261004",
    "savefig.facecolor":"#ffffff","axes.spines.top":False,"axes.spines.right":False})
fig,(left,right)=plt.subplots(1,2,figsize=(16,10),gridspec_kw={"width_ratios":[1.2,1]})
fig.subplots_adjust(left=.075,right=.965,top=.80,bottom=.35,wspace=.30)
fig.suptitle("Two Haar conventions, one finite-exponent class",fontsize=26,y=.965)
fig.text(.5,.895,r"$G=\mathbb{R}\times D$, $D$ uncountable and discrete",ha="center",fontsize=20)
left.set_title("A finite projection of the open cosets",pad=21,fontsize=18)
lengths=[1,.5,1.5,.75]
for j,length in enumerate(lengths):
    y=4-j
    left.plot([-2,2],[y,y],color="#c6cdd2",lw=2,zorder=1)
    left.plot([-length/2,length/2],[y,y],color="#007d76",lw=10,zorder=2,solid_capstyle="butt")
    left.plot(0,y,"o",color="#b74732",markersize=9,zorder=3)
    left.text(1.08,y+.10,f"length {length:g}",fontsize=14,color="#007d76")
left.set_yticks([4,3,2,1],[r"$d_1$",r"$d_2$",r"$d_3$",r"$d_4$"])
left.set_ylim(.55,4.65)
left.set_xlim(-2,2)
left.set_xticks([-2,-1,0,1,2])
left.set_xlabel(r"real coordinate $x$",labelpad=12)
left.set_ylabel(r"four displayed members of $D$",labelpad=11)
left.spines["left"].set_visible(False)
left.tick_params(axis="y",length=0)
left.text(.5,-.235,r"$S=\{0\}\times D$: red points mark its sections.",transform=left.transAxes,
          ha="center",fontsize=15,color="#b74732")
left.text(.5,-.35,r"$\mu_\ell(S)=0,\qquad \mu_o(S)=\infty$",transform=left.transAxes,
          ha="center",fontsize=22)
right.set_title(r"An exact countable $L^2$ example",pad=21,fontsize=18)
values=[.5,.25,.125,.0625,.0625]
right.bar(range(5),values,color=["#7452a5"]*4+["#bca7d6"],width=.64)
right.set_xticks(range(5),[r"$d_1$",r"$d_2$",r"$d_3$",r"$d_4$","tail"])
right.set_ylim(0,.59)
right.set_ylabel(r"$b_{d_j}=\int_{\mathbb{R}\times\{d_j\}}|f|^2$")
for j,v in enumerate(values):
    right.text(j,v+.015,[r"$1/2$",r"$1/4$",r"$1/8$",r"$1/16$",r"$1/16$"][j],
               ha="center",fontsize=15)
right.text(.5,-.235,r"$f(x,d_j)=2^{-j/2}\,1_{[0,1]}(x),\quad j\geq1$",transform=right.transAxes,
           ha="center",fontsize=17)
right.text(.5,-.35,r"$\|f\|_{2,\mu_o}^2=\|f\|_{2,\mu_\ell}^2=\sum_{j\geq1}2^{-j}=1$",
           transform=right.transAxes,ha="center",fontsize=17)
fig.text(.5,.09,
         "Left: any compact set meets finitely many cosets; its red-point intersection is null.\n"
         "Every open neighbourhood of all of S meets uncountably many cosets in positive intervals.\n"
         "Right: set f = 0 on every other coset. The tail bar sums all j ≥ 5; it is not one extra coset.",
         ha="center",va="center",fontsize=14,linespacing=1.6)
fig.text(.5,.025,"HR-08–HR-10. The left panel is a finite projection; uncountability is established in the proof.",
         ha="center",fontsize=13,color="#3c4f5d")
paths=[OUT/"haar-conventions.svg",OUT/"haar-conventions.png"]
fig.savefig(paths[0],metadata={"Date":None},bbox_inches=None)
fig.savefig(paths[1],dpi=125,metadata={"Software":"Original CC0 Haar/Radon illustration"},bbox_inches=None)
plt.close(fig)
(OWN/"FIGURE_RECEIPT.json").write_text(json.dumps({
    "equation_locators":["HR-08a","HR-09a","HR-09b","HR-09c"],"proof_section":"HR-10",
    "licence":"CC0-1.0","dimensions":[2000,1250],
    "left":"Finite projection of R times uncountable discrete D; displayed sample interval lengths are 1, 1/2, 3/2, 3/4.",
    "right":"Exact countable L2 example with masses 2^-j and total 1; tail aggregates j>=5.",
    "assets":[{"path":p.as_posix(),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
    "source":{"path":Path(__file__).resolve().as_posix(),"sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"assets":[str(p) for p in paths]}))
