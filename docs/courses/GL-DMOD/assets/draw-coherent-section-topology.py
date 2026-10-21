"""Exact planar scale illustration and the coherent section mechanisms."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "svg.hashsalt":"GL-DMOD-SC-cover-quotients"})
fig,axs=plt.subplots(1,2,figsize=(13,6.5),gridspec_kw={"width_ratios":[1,1.2]})
fig.patch.set_facecolor("#f7f9fc")
a,b=axs
for ax in axs:ax.set_facecolor("#f7f9fc")
a.set_aspect("equal");a.set_xlim(-4.5,4.8);a.set_ylim(-4.5,4.5);a.axis("off")
a.add_patch(Circle((0,0),4,fill=False,edgecolor="#a4adbc",linestyle="--",linewidth=1.6))
for centre,rad,col in[((0,0),1,"#345db1"),((1.5,0),1.01,"#00838e")]:
 a.add_patch(Circle(centre,rad,facecolor=col,alpha=.1))
 a.add_patch(Circle(centre,rad,fill=False,edgecolor=col,linewidth=2))
 a.add_patch(Circle(centre,rad/10,facecolor=col,edgecolor=col))
a.text(-.15,-.35,r"$x_j$",ha="right",fontsize=13)
a.text(1.65,-.35,r"$x_k$",ha="left",fontsize=13)
a.annotate("Radius 1",xy=(-.75,.65),xytext=(-3.55,1.65),
           arrowprops={"arrowstyle":"-","color":"#345db1"},color="#345db1")
a.annotate("Radius 101/100",xy=(2.15,.7),xytext=(1.1,2.6),
           arrowprops={"arrowstyle":"-","color":"#00838e"},color="#00838e")
a.text(0,-2.0,"Small radii: one tenth\nCentre distance: 3/2",ha="center",color="#17233a")
a.text(0,-3.35,r"$\mathrm{star}(V_j)\subset B(x_j,4\delta_j)$",ha="center",fontsize=13)
a.set_title(r"SC.A: lengths in units of $\delta_j$",pad=18)
b.axis("off");b.set_xlim(0,1);b.set_ylim(0,1)
rows=[(.78,"Local coherent sections (SC.24–SC.27)",
       r"$S(A\cap V)=\mathcal{O}(V)^p/Z_0(V)$","Closed relations; nuclear Frechet quotient"),
      (.45,"Sections on an arbitrary open set (SC.29)",
       r"$S(U)\ \subset\ \prod_i S(U_i)$","Closed space of compatible finite jets"),
      (.12,"Support-proper upper bound (SC.35–SC.39)",
       r"$M=r+\max_i 12^{\,2N_i}-1$",r"$H^k(f^{-1}W,F)=0\quad(k\geq M)$")]
for y,title,eq,note in rows:
 b.add_patch(FancyBboxPatch((.02,y-.105),.96,.25,boxstyle="round,pad=.014",
                           facecolor="white",edgecolor="#b8c7de",linewidth=1.4))
 b.text(.5,y+.095,title,ha="center",fontsize=12,color="#17233a")
 b.text(.5,y+.01,eq,ha="center",fontsize=14,color="#244c95")
 b.text(.5,y-.075,note,ha="center",fontsize=11.5,color="#17233a")
for y in[.66,.33]:
 b.annotate("",xy=(.5,y-.08),xytext=(.5,y+.015),
            arrowprops={"arrowstyle":"->","lw":1.7,"color":"#00838e"})
b.set_title("Actual quotients and uniform section bounds",pad=18)
fig.subplots_adjust(left=.025,right=.975,top=.86,bottom=.06,wspace=.1)
fig.savefig(r/"coherent-section-topology.png",dpi=160,metadata={"Software":"Matplotlib"})
fig.savefig(r/"coherent-section-topology.svg",metadata={"Date":None})
plt.close(fig)
data={"planar_example":{"length_unit":"delta_j; all drawn lengths are normalized",
                        "centres":[["0","0"],["3/2","0"]],"radii":["1","101/100"],
                        "small_radii":["1/10","101/1000"],"star_margin":"4","subordination_margin":"50"},
 "exact_bounds":{"delta_lipschitz":"1/100","packing_ratio":"1111/99 < 12",
                 "multiplicity":"D_m=12^m","cohomology_vanishes":"k>=D_m",
                 "proper_support":"M=r+max_i(12^(2N_i))-1"},
 "illustration_only":"The planar pair does not certify a maximal cover or the general theorem.",
 "proof_locators":["SC.A","SC.E","SC.F","SC.G","SC.J"],
 "free_primary":"https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf"}
(r/"coherent-section-topology-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
