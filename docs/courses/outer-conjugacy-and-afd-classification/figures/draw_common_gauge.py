"""Common gauge diagram; geometry is a quotient schematic."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

dest=Path(__file__).resolve().parent
dest.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","svg.hashsalt":"OA-CLASSIFY-extended-unitary-gauge-v1"})
fig=plt.figure(figsize=(11,7.6),facecolor="white")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
blue="#164d80";orange="#a64a15";dark="#172535"

def box(x,y,w,h,text,color=blue,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.009,rounding_size=0.012",
                               edgecolor=color,facecolor="#f5f8fb",linewidth=1.6))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=size,color=dark,linespacing=1.5)

def arrow(a,b):
    ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","color":blue,"lw":1.6})

ax.text(.05,.96,"One implementer change acts on both components",fontsize=20,weight="bold",color=dark,va="top")
ax.text(.05,.902,r"$u'=wu:\quad(v,c_t)\mapsto(v\,w^*h(w),\ c_t\,w^*\theta_t(w))$",
        fontsize=17,color=blue,va="top")
ax.text(.05,.831,"Separate quotients",fontsize=15,weight="bold",color=dark)
ax.text(.55,.831,"Common gauge quotient",fontsize=15,weight="bold",color=dark)

box(.06,.664,.17,.09,r"$(1,1)$")
box(.29,.664,.17,.09,r"$(-1,1)$",orange)
box(.15,.479,.22,.094,r"$([1],[1])$")
arrow((.145,.653),(.215,.584));arrow((.375,.653),(.305,.584))
ax.text(.26,.616,r"$[v]\quad$ and $\quad[c]$",ha="center",fontsize=12,color=blue)
ax.text(.26,.412,"Both pairs have the same image.\nDifferent gauges may be used.",ha="center",va="center",
        fontsize=11.5,color=dark,linespacing=1.5)

box(.565,.664,.17,.09,r"$[(1,1)]$")
box(.79,.664,.17,.09,r"$[(-1,1)]$",orange)
ax.text(.76,.616,"Distinct classes",ha="center",fontsize=12,color=orange,weight="bold")
ax.text(.76,.588,"Ergodic centre flow",ha="center",fontsize=10.5,color=dark)
box(.57,.435,.38,.136,
    r"$w^*\theta_t(w)=1\ \ (\mathrm{all}\ t)$"+"\n"+
    r"$\Longrightarrow w\ \mathrm{scalar}$"+"\n"+
    r"$\Longrightarrow w^*h(w)=1$",size=14)

ax.plot([.51,.51],[.399,.815],color="#bac5d0",lw=1)
ax.text(.05,.335,"Exact torus-flow example",fontsize=15,weight="bold",color=dark)
ax.text(.05,.287,r"$T_t(x,y)=(x+t,y+\sqrt{2}\,t),\quad h(x,y)=(x+\frac{1}{2},y),\quad w=e^{2\pi i x}$",
        fontsize=14,color=blue)
ax.text(.05,.238,r"$\theta_t(f)=f\circ T_{-t},\quad w^*h(w)=-1,\quad w^*\theta_t(w)=e^{-2\pi i t}$",
        fontsize=14,color=blue)
ax.text(.05,.182,r"$\alpha_+=\beta\otimes\mathrm{id}:\ \mathrm{Ob}=1$"+"     "+
        r"$\alpha_-=\beta\otimes\rho:\ \mathrm{Ob}=-1$",fontsize=14,color=orange)
ax.text(.05,.126,"The scalar obstruction separates the two outer-conjugacy classes.",fontsize=12,color=dark)
ax.text(.05,.081,"Proof: Common gauge invariants, §§1, 3; equations (1.4), (3.5), (3.6). Quotient arrows are schematic; no metric or embedding is asserted.",
        fontsize=10,color=dark)
ax.text(.05,.045,"Inputs: Connes (1975), ordinary obstruction; Sutherland–Takesaki (1989), extended-unitary framework.",
        fontsize=10,color=dark)
fig.savefig(dest/"common-gauge.png",dpi=170,metadata={"Software":"OA-CLASSIFY reproducible diagram"})
fig.savefig(dest/"common-gauge.svg",metadata={"Date":None,"Creator":"OA-CLASSIFY writing AI"})
plt.close(fig)
print(str(dest/"common-gauge.png"))
