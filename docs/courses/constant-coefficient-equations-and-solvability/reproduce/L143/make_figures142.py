"""Reproduce the exact local PSH compactness illustrations; no TeX or network."""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

ROOT = Path(__file__).resolve().parent
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.labelsize": 11,
    "svg.fonttype": "none", "text.usetex": False,
    "savefig.facecolor": "white",
})
blue, orange, green = "#185a9d", "#c45b16", "#227847"

def save(fig, name):
    fig.savefig(FIG / (name + ".png"), dpi=180)
    fig.savefig(FIG / (name + ".svg"))
    plt.close(fig)

fig, axes = plt.subplots(1, 3, figsize=(16, 6.5))
fig.subplots_adjust(left=.045, right=.985, bottom=.25, top=.82, wspace=.29)
fig.suptitle("How a local upper bound and one finite value control negative mass",
             fontsize=17, y=.95)
ax = axes[0]
for centre, radius, colour, style, label in [
    ((0,0),4.5,"#777777","-",r"$\Omega=B(0,9/2)$"),
    ((0,0),4,"#333333","--",r"$\overline{B(x,4r)}\subset\Omega$"),
    ((0,0),3,"#777777",":",r"$B(x,3r)$"),
    ((.25,0),2,orange,"-",r"mean ball $B(y_j,2r)$"),
    ((0,0),1,blue,"-",r"target $B(x,r)$"),
]:
    ax.add_patch(Circle(centre,radius,fill=False,edgecolor=colour,
                        linestyle=style,linewidth=1.8,label=label))
ax.add_patch(Circle((3/16,0),1/8,facecolor=green,edgecolor=green,alpha=.3))
ax.scatter([0,.25],[0,0],color=[blue,orange],s=25,zorder=6)
ax.set(xlim=(-4.8,4.8),ylim=(-4.8,4.8),xlabel="real coordinate",ylabel="imaginary coordinate")
ax.set_aspect("equal")
ax.set_title("Mean-ball transfer (HC3)\n"+r"$x=0,\ r=1,\ y_j=1/4$")
ax.legend(loc="upper left",bbox_to_anchor=(-.02,-.12),fontsize=8.5,frameon=False,ncol=2)
zoom=ax.inset_axes([.63,.63,.34,.34])
zoom.add_patch(Circle((3/16,0),1/8,facecolor=green,edgecolor=green,alpha=.25))
zoom.scatter([0,3/16,.25],[0,0,0],color=[blue,green,orange],s=18)
zoom.annotate(r"$x$", (0,0),xytext=(-.035,.05),fontsize=9)
zoom.annotate(r"$a$", (3/16,0),xytext=(.13,.05),fontsize=9)
zoom.annotate(r"$y_j$", (.25,0),xytext=(.26,-.055),fontsize=9)
zoom.set(xlim=(-.05,.37),ylim=(-.16,.16),xticks=[],yticks=[])
zoom.set_title(r"$a=3/16,\ s=1/8$",fontsize=9)
zoom.set_aspect("equal")

ax=axes[1]
ax.add_patch(Rectangle((-4.2,-1.2),8.4,2.4,facecolor="#eeeeee",
                       edgecolor="#444444",linewidth=1.8))
ax.add_patch(Rectangle((-3,-.1),6,.2,facecolor=blue,alpha=.18))
centres=np.array([float(Fraction(-3)+i*Fraction(3,8)) for i in range(17)])
for centre in centres:
    ax.add_patch(Circle((centre,0),.25,fill=False,edgecolor=blue,linewidth=1))
ax.scatter(centres,np.zeros_like(centres),s=9,color=blue)
ax.text(0,2.0,r"nonempty, open and closed $G=\Omega$",ha="center",fontsize=12)
ax.text(0,-2.0,"A compact strip has a finite ball cover.\n"
        "Each compact set receives its own bound.",
        ha="center",va="center",fontsize=11)
ax.set(xlim=(-4.5,4.5),ylim=(-3.2,3.2),xlabel="real coordinate",
       ylabel="imaginary coordinate")
ax.set_aspect("equal")
ax.set_title("Connected domain and finite covers\n"
             r"ball radius $1/4$, spacing $3/8$")
ax.text(.5,-.30,r"$\Omega=(-21/5,21/5)\times(-6/5,6/5)$",
        transform=ax.transAxes,ha="center",fontsize=10)

ax=axes[2]
for centre, colour, label in [(-1.4,blue,r"$v_j=0$"),(1.4,orange,r"$v_j=-j$")]:
    ax.add_patch(Circle((centre,0),1,facecolor=colour,edgecolor=colour,alpha=.16))
    ax.add_patch(Circle((centre,0),1,fill=False,edgecolor=colour,linewidth=2))
    ax.text(centre,0,label,color=colour,fontsize=18,ha="center",va="center")
ax.text(-1.4,-1.35,"no collapse",ha="center",fontsize=10)
ax.text(1.4,-1.35,r"$L^1$ norm $=\pi j$",ha="center",fontsize=10)
ax.text(0,2.0,"The local upper bound is 0\non both components.",
        ha="center",fontsize=10)
ax.text(0,-2.35,"Different components can take\ndifferent alternatives.",
        ha="center",fontsize=10)
ax.set(xlim=(-2.7,2.7),ylim=(-3.2,3.2),xlabel="real coordinate",
       ylabel="imaginary coordinate")
ax.set_aspect("equal")
ax.set_title("Disconnected counterexample (HC11)\n"
             r"$B(-7/5,1)\cup B(7/5,1)$")
save(fig,"mean-propagation-and-components")

fig,axes=plt.subplots(1,3,figsize=(16,5.9))
fig.subplots_adjust(left=.055,right=.985,bottom=.23,top=.80,wspace=.32)
fig.suptitle("Truncated logarithms: a singular limit, small integral error and compact maxima",
             fontsize=17,y=.95)
radii=np.geomspace(1e-4,1,1000)
j_values=np.arange(1,9)
ax=axes[0]
ax.plot(radii,np.log(radii),color="#222222",linewidth=2,label=r"limit $\log r$")
for j in [1,2,4,8]:
    ax.plot(radii,np.maximum(np.log(radii),-j),linewidth=1.8,
            label=rf"$j={j}$")
ax.axvspan(1e-4,np.exp(-2),facecolor=blue,alpha=.09)
ax.axvline(np.exp(-2),color=blue,linestyle=":",linewidth=1)
ax.set(xscale="log",xlim=(1e-4,1),ylim=(-10,.3),xlabel=r"positive radius $r$",
       ylabel="function value",title=r"$v_j(r)=\max(\log r,-j)$")
ax.legend(loc="lower right",fontsize=9,frameon=False)
ax.text(.04,-.25,r"$r=e^{-2}$",color=blue,fontsize=9)
ax.text(.5,-.31,r"At zero: $v_j(0)=-j$, $v(0)=-\infty$.",
        transform=ax.transAxes,ha="center",fontsize=10)

ax=axes[1]
errors=(np.pi/2)*np.exp(-2*j_values)
ax.semilogy(j_values,errors,"o-",color=green,linewidth=2)
ax.set(xticks=j_values,xlabel=r"index $j$",ylabel=r"exact $L^1$ error on $|z|\leq1$",
       title=r"$\int |v_j-v|\,dA=(\pi/2)e^{-2j}$")
ax.grid(alpha=.25)
ax.text(.5,-.31,"The displayed values are the proved formula,\n"
        "not a numerical integration estimate.",
        transform=ax.transAxes,ha="center",fontsize=10)

ax=axes[2]
ax.plot(j_values,np.maximum(-2,-j_values),"o-",color=blue,
        label=r"$K=\{|z|\leq e^{-2}\}$")
ax.plot(j_values,-j_values,"s-",color=orange,label=r"$K=\{0\}$")
ax.axhline(-2,color=blue,linestyle=":",label=r"disc limit $-2$")
ax.set(xticks=j_values,ylim=(-8.7,-.5),xlabel=r"index $j$",ylabel=r"$\sup_K v_j$",
       title="Hartogs comparison\non two compact sets")
ax.legend(loc="lower left",fontsize=9,frameon=False)
ax.grid(alpha=.2)
ax.text(.5,-.31,"The singleton limit is minus infinity.\n"
        "Both compact sets are inside the same domain.",
        transform=ax.transAxes,ha="center",fontsize=10)
save(fig,"truncated-logs-and-hartogs")

geometry={
    "lesson_id":"AN02-L143",
    "mean_transfer":{
        "real_dimension_of_picture":2,"proof_locator":"HC3.1–HC3.2",
        "domain":"B(0,9/2)","x":[0,0],"r":"1",
        "a":["3/16","0"],"s":"1/8","y_j":["1/4","0"],
        "exact_inclusions":[
            "B(a,s) subset B(x,r/2)",
            "y_j in B(a,s)",
            "B(x,r) subset B(y_j,2r) subset B(x,3r)",
            "closed B(x,4r) subset Omega"
        ],
        "integral_bound":"|C|*|B_r|+(|C|+D)*|B_2r|",
        "D":"B/|B(a,s)|+1",
        "meaning":"Exact illustrative geometry, not a sample function field"
    },
    "connected_cover":{
        "domain":"(-21/5,21/5) x (-6/5,6/5)",
        "compact_strip":"[-3,3] x [-1/10,1/10]",
        "centres_x_exact":[str(Fraction(-3)+i*Fraction(3,8)) for i in range(17)],
        "ball_radius":"1/4","spacing":"3/8",
        "meaning":"Finite overlapping cover of a compact strip; not one uniform global bound"
    },
    "disconnected":{
        "domain":"B(-7/5,1) union B(7/5,1)",
        "values":["0","-j"],"common_upper_bound":0,
        "right_component_L1_norm":"pi*j","proof_locator":"HC11 Example5"
    },
    "truncated_log":{
        "domain":"|z|<2","sequence":"max(log|z|,-j)",
        "limit":"log|z|","at_zero":["-j","-infinity"],
        "support_of_difference":"|z|<exp(-j)",
        "unit_disc_error_exact":"(pi/2)*exp(-2*j)","proof_locator":"HC10.1–HC10.3",
        "profile_j":[1,2,4,8],"positive_radius_range":[1e-4,1],
        "error_samples":[{"j":int(j),"value":float(e)} for j,e in zip(j_values,errors)],
        "compact_disc":"|z|<=exp(-2)","disc_supremum":"max(-2,-j)",
        "singleton":[0,0],"singleton_supremum":"-j",
        "disc_limit":-2,"singleton_limit":"-infinity"
    },
    "rendering":{"backend":"Agg","TeX":False,"SVG_text":"editable",
                 "PNG_dpi":180,"figure1_pixels":[2880,1170],"figure2_pixels":[2880,1062]}
}
(ROOT/"figure-geometry.json").write_text(
    json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print("Wrote two PNG/SVG pairs and exact figure geometry.")
