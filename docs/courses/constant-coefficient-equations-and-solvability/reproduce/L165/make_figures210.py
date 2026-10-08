"""Reproducible original atom locations and singular-support diagrams."""
from pathlib import Path
import json,math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
HERE=Path(__file__).resolve().parent; OUT=HERE/"figures"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"svg.fonttype":"path",
                     "svg.hashsalt":"isolated-atoms210","axes.grid":True,"grid.alpha":.15})
BLUE,GREEN,RED,GRAY="#15618a","#26774f","#b44236","#777777"
colors=[BLUE,GREEN,RED]
def save(fig,name):
    fig.savefig(OUT/(name+".png"),dpi=160,bbox_inches="tight",
                metadata={"Software":"Matplotlib;original mathematical figure"})
    fig.savefig(OUT/(name+".svg"),bbox_inches="tight",
                metadata={"Date":None,"Creator":"Original mathematical figure"})
    plt.close(fig)
blocks=[]
for m in [1,2,3]:
    number=math.ceil(2*math.pi*m);radius=1-2**(-m)
    points=[[radius*math.cos(2*math.pi*k/number),radius*math.sin(2*math.pi*k/number)]
            for k in range(number)]
    blocks.append(dict(m=m,boundary_net_count=number,boundary_angle="2*pi*k/N_m",
                       contracted_radius=radius,coordinates=points,
                       boundary_net_cover_radius=2*math.sin(math.pi/(2*number))))
fig,axes=plt.subplots(1,2,figsize=(12,5.5))
ax=axes[0]; ax.add_patch(Circle((0,0),1,fill=False,color=GRAY,lw=2,label="Boundary of the unit disk"))
for block,color in zip(blocks,colors):
    xs,ys=zip(*block["coordinates"])
    ax.scatter(xs,ys,s=30,color=color,zorder=5,
               label="m="+str(block["m"])+": radius "+str(block["contracted_radius"]))
ax.scatter([0],[0],marker="x",s=45,color=GRAY,zorder=6,label="Interior center o=0")
ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel="First physical coordinate",
       ylabel="Second physical coordinate",title="Contract boundary nets inward")
ax.set_aspect("equal",adjustable="box")
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),fontsize=8.8)
ax=axes[1];ax.plot([-1,1],[0,0],ls="--",color=GREEN,lw=2,label="Closed convex core [-1,1]")
segment=[[-(1-2**(-m)),0,0] for m in range(1,6)]+[[1-2**(-m),0,0] for m in range(1,6)]
ax.scatter([p[0] for p in segment],[0]*len(segment),s=38,color=BLUE,zorder=5,
           edgecolors="white",linewidths=.5,label="Atoms from m=1,...,5")
ax.scatter([-1,1],[0,0],s=65,facecolors="white",edgecolors=GRAY,lw=1.7,zorder=6,
           label="Non-isolated support limits")
ax.annotate("x=1/2",xy=(.5,0),xytext=(.1,.46),
            arrowprops={"arrowstyle":"->","color":BLUE},color=BLUE)
ax.annotate("x=31/32",xy=(31/32,0),xytext=(.47,-.45),
            arrowprops={"arrowstyle":"->","color":BLUE},color=BLUE)
ax.text(0,-.82,"Embedded in R³: x₂=x₃=0",ha="center")
ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel="First physical coordinate x₁",
       title="Relative boundary of an embedded segment",yticks=[])
ax.set_aspect("equal",adjustable="box")
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),fontsize=8.8)
fig.suptitle("Isolated interior atoms pin the entire limiting convex core",fontsize=14)
fig.tight_layout(rect=(0,0,1,.93));save(fig,"isolated-atoms-and-relative-boundaries")

fig,axes=plt.subplots(1,2,figsize=(12,5.1))
ax=axes[0]
for row in [2,1]:
    ax.plot([-2,3],[row,row],color="#cbd2d6",lw=10,solid_capstyle="butt",
            label="Ordinary support [-2,3]" if row==2 else None)
ax.scatter([-1],[2],color=BLUE,s=65,zorder=5,label="Singular point -1")
ax.scatter([2],[1],color=GREEN,s=65,zorder=5,label="Singular point 2")
ax.plot([-1,2],[0,0],color=GRAY,lw=2,ls="--",label="Sum's singular hull [-1,2]")
ax.scatter([-1,2],[0,0],color=[BLUE,GREEN],s=65,zorder=5)
ax.set(xlim=(-2.4,3.4),ylim=(-.7,2.7),xlabel="Physical coordinate x",
       yticks=[2,1,0],yticklabels=["u₁ = δ₋₁ + f","u₂ = δ₂ − f","u₁ + u₂"],
       title="Same support; separate singularities")
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),fontsize=8.5)
ax=axes[1]
ax.scatter([0,0],[2,1],color=RED,s=65,zorder=5,label="Same singular point 0")
ax.text(.15,2,"coefficient +1",va="center",color=RED)
ax.text(.15,1,"coefficient −1",va="center",color=RED)
ax.text(0,0,"Zero distribution:\nno support or singular points",ha="center",va="center",fontsize=10)
ax.set(xlim=(-1.2,1.2),ylim=(-.7,2.7),xlabel="Physical coordinate x",
       yticks=[2,1,0],yticklabels=["v₁ = δ₀","v₂ = −δ₀","v₁ + v₂ = 0"],
       title="Overlapping singularities can cancel",xticks=[-1,0,1])
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),fontsize=8.8)
fig.suptitle("The maximum law separates singular support from ordinary support",fontsize=14)
fig.tight_layout(rect=(0,0,1,.92));save(fig,"separate-singularities-and-cancellation")
geometry=dict(authorship="Original mathematics and figures;GPT-6.1 Sol (OpenAI),Ultra;CC0 1.0",
    convex_measure_construction=dict(disk={"center":[0,0],"radius":1,"displayed_blocks":blocks,
        "full_construction_uses_all_positive_integers_m":True,"atom_weights":"2^(-j), j enumerates all atoms",
        "marker_sizes_do_not_represent_masses":True},
        embedded_segment={"endpoints":[[-1,0,0],[1,0,0]],"displayed_atom_coordinates":segment,
          "weights_per_atom":"2^(-m-1)","physical_projection":"x_1; x_2=x_3=0",
          "full_construction_uses_all_m":True},
        proof_locators=["Formal Theorems3.1,4.1","Learner Example3","Learner Exercises5–7"],
        physical_axes_have_equal_scale=True),
    separated_sum=dict(f={"smooth":True,"support":[-2,3],"positive_on_interior":True},
        u1="delta_-1+f",u2="delta_2-f",ordinary_supports=[[-2,3],[-2,3]],
        singular_supports=[[-1],[2]],sum="delta_-1+delta_2",sum_singular_support=[-1,2],
        sum_singular_hull=[-1,2],sum_indicator="max(-eta,2*eta)",
        diagram_vertical_positions_are_distribution_rows_not_physical_coordinates=True,
        proof_locators=["Formal Lemma2.2,Theorem6.1","Learner Example2"]),
    cancellation=dict(v1="delta_0",v2="-delta_0",common_singular_support=[0],sum="zero",
        component_indicators=["zero","zero"],sum_indicator="collapsed minus infinity",
        proof_locators=["Learner Example4","Learner Exercise10"]),
    references=["Terence Tao,246B Notes2 and245B Notes9",
                "Lars Hörmander,Analysis of Linear Partial Differential Operators I and II"])
(OUT/"geometry210.json").write_text(json.dumps(geometry,indent=2,allow_nan=False)+"\n",encoding="utf-8")
print(json.dumps(dict(figures=2,formats=["PNG","SVG"],exact_geometry=True)))
