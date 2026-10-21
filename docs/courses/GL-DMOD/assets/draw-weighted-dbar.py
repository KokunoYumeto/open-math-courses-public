"""Reproducible mathematical schematic of the exact WD.I radii."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "svg.hashsalt":"GL-DMOD-weighted-dbar-WD31"})
fig,axs=plt.subplots(1,2,figsize=(13,6),gridspec_kw={"width_ratios":[1,1.15]})
fig.patch.set_facecolor("#f7f9fc")
a,b=axs
for ax in axs:ax.set_facecolor("#f7f9fc")
a.set_aspect("equal");a.set_xlim(-2.85,2.85);a.set_ylim(-2.85,2.85);a.axis("off")
for rad,color,ls,lw in [(2.5,"#64748b","--",1.6),(2,"#b45309","-",1.5),
                        (1.75,"#b45309","-",1.5),(1.5,"#007e87","-",2),
                        (1,"#3554aa","-",2)]:
 a.add_patch(Circle((0,0),rad,fill=False,edgecolor=color,linestyle=ls,linewidth=lw))
a.add_patch(Wedge((0,0),2,0,360,width=.25,color="#f5bf68",alpha=.55))
a.add_patch(Circle((0,0),.5,facecolor="#9bb3ee",edgecolor="#3554aa",linewidth=1.8))
a.text(0,0,r"$K$",ha="center",va="center",fontsize=16)
labels=[((.70,.70),(1.4,.15),r"$\psi<b_0=1$"),
        ((-1.06,1.06),(-2.7,2.65),r"$\psi<b=9/4$"),
        ((1.33,1.33),(1.0,2.28),r"$7/4<|z|<2$"),
        ((-1.77,-1.77),(-2.7,-2.7),r"$U:\ |z|<5/2$")]
for xy,tx,s in labels:
 a.annotate(s,xy=xy,xytext=tx,fontsize=12,color="#17233a",
            arrowprops={"arrowstyle":"-","color":"#64748b","lw":1})
a.set_title(r"Exact sublevels for $\psi(z)=|z|^2$",pad=18)
b.axis("off");b.set_xlim(0,1);b.set_ylim(0,1)
rows=[(.78,"Cutoff derivative beyond the gap",
       r"$g=\bar\partial(\eta h\,dz)$",r"$\|g\|_{\varphi_\nu}^{\,2}\leq C e^{-\nu}$"),
      (.45,"Weak solution in the complete metric",
       r"$\bar\partial u_\nu=g$",r"$\|u_\nu\|_{\varphi_\nu}^{\,2}\leq C e^{-\nu}$"),
      (.12,"Holomorphic error on the inner sublevel",
       r"$(H_\nu-h)\,dz=-u_\nu$",r"$\sup_K|\partial^\alpha(H_\nu-h)|\leq C_\alpha e^{-\nu/2}$")]
for y,title,eq1,eq2 in rows:
 b.add_patch(FancyBboxPatch((.02,y-.09),.96,.23,boxstyle="round,pad=.018",
                           facecolor="white",edgecolor="#b8c7de",linewidth=1.3))
 b.text(.5,y+.095,title,ha="center",fontsize=11.6,color="#17233a")
 b.text(.5,y+.015,eq1,ha="center",fontsize=14,color="#183f8a")
 b.text(.5,y-.055,eq2,ha="center",fontsize=13,color="#183f8a")
for y in [.67,.34]:
 b.annotate("",xy=(.5,y-.08),xytext=(.5,y+.02),
            arrowprops={"arrowstyle":"->","lw":1.8,"color":"#007e87"})
b.set_title("WD.D and WD.H: the estimate mechanism",pad=18)
fig.subplots_adjust(left=.035,right=.98,top=.86,bottom=.07,wspace=.14)
fig.savefig(r/"weighted-dbar.png",dpi=160,metadata={"Software":"Matplotlib"})
fig.savefig(r/"weighted-dbar.svg",metadata={"Date":None})
plt.close(fig)
data={"example":"WD.I, Omega=C, psi=|z|^2",
 "metric":"omega=i(1+4|z|^2) dz wedge dbar z",
 "radii":{"K":"1/2","inner_sublevel":"1","outer_sublevel":"3/2",
          "cutoff_one_through":"7/4","cutoff_zero_from":"2","U":"5/2"},
 "levels":{"b0":"1","b":"9/4"},
 "theta":"kappa(t-1)/kappa(5/4)",
 "kappa":"integral_0^t (t-s) exp(-1/s) ds for t>0, 0 otherwise",
 "estimates":{"data_squared_norm":"C exp(-nu)",
              "solution_squared_norm":"C exp(-nu)",
              "holomorphic_jet_error":"C_alpha exp(-nu/2)"},
 "geometry":"exact radii; the diagram is explanatory, not a finite verification of the general theorem",
 "proof_locators":["WD.D","WD.H","WD.I"],
 "free_primary":"https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf"}
(r/"weighted-dbar-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
