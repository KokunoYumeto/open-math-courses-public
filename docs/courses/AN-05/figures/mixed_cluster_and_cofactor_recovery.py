"""CC0 exact mixed-cubic cluster and cofactor figure; no chosen quadratic branch."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch

parser=argparse.ArgumentParser()
parser.add_argument("--output",type=Path)
args=parser.parse_args()
destination=args.output or Path(__file__).with_suffix(".png")
destination.parent.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "mathtext.fontset":"dejavusans","axes.spines.top":False,
                     "axes.spines.right":False})
fig=plt.figure(figsize=(12,7),dpi=200,facecolor="#f8fafb")
grid=fig.add_gridspec(2,3,height_ratios=[3.9,1.65],width_ratios=[1,1.34,1.05],
                     left=.05,right=.975,top=.86,bottom=.07,wspace=.18,hspace=.19)
fig.text(.05,.955,"A double cluster supplies exactly one cofactor derivative",
         fontsize=18,fontweight="bold",color="#163d51")
fig.text(.05,.9,r"$p(t,\sigma,\eta)=\sigma\left((\sigma-i\eta)^2-t^2\eta^2\right)$",
         fontsize=17,color="#163d51")
blue="#087a9f"; orange="#bc5b14"; dark="#193844"

ax=fig.add_subplot(grid[0,0])
ax.set_facecolor("white")
ax.add_patch(Circle((0,0),3/16,facecolor="#cce7f0",edgecolor=blue,alpha=.65,lw=1.5))
ax.add_patch(Circle((0,1),3/8,facecolor="#ffdfc6",edgecolor=orange,alpha=.55,lw=1.5))
ax.axhline(0,color="#c4cdd1",lw=.8);ax.axvline(0,color="#c4cdd1",lw=.8)
ax.scatter([0],[0],s=65,color=blue,zorder=5)
ax.scatter([0],[1],s=90,facecolors="white",edgecolors=orange,lw=2,zorder=6)
ax.scatter([-1/8,1/8],[1,1],s=48,color=orange,zorder=7)
ax.annotate("simple root 0",xy=(0,0),xytext=(-.49,-.3),
            fontsize=11,color=blue,arrowprops={"arrowstyle":"-","color":blue})
ax.annotate(r"$t=0$: double root $i$",xy=(0,1),xytext=(-.53,1.5),
            fontsize=10.5,color=orange,arrowprops={"arrowstyle":"-","color":orange})
ax.annotate(r"$t=\frac{1}{8}$: $i\pm\frac{1}{8}$",xy=(.125,1),xytext=(-.53,.47),
            fontsize=11,color=orange,arrowprops={"arrowstyle":"-","color":orange})
ax.set_xlim(-.6,.6);ax.set_ylim(-.38,1.65);ax.set_aspect("equal")
ax.set_xticks([-.5,0,.5]);ax.set_yticks([0,.5,1,1.5])
ax.set_xlabel(r"$\operatorname{Re}\sigma$");ax.set_ylabel(r"$\operatorname{Im}\sigma$")
ax.set_title(r"Exact roots at $\eta=1$",fontsize=12,fontweight="bold",pad=8)

middle=fig.add_subplot(grid[0,1]);middle.axis("off")
middle.text(0,.98,"Polynomial reconstruction stays smooth",fontsize=12.5,
            fontweight="bold",color=dark,va="top")
middle.text(0,.87,r"$Q_1=(\sigma-i\eta)^2-t^2\eta^2,\quad Q_2=\sigma$",
            fontsize=12.5,color=dark)
middle.text(0,.68,r"$\sigma^2=\sigma Q_2$",fontsize=17,color=dark)
middle.text(0,.51,r"$\sigma\eta=\eta Q_2$",fontsize=17,color=dark)
middle.text(0,.33,r"$\eta^2=-\frac{Q_1}{1+t^2}+\frac{\sigma-2i\eta}{1+t^2}Q_2$",
            fontsize=16,color=dark)
middle.text(0,.1,"The quadratic numerator is affine in σ.\n"
                       "The coefficient 1 / (1 + t²) stays finite at t = 0.",
            fontsize=11.5,color=dark,linespacing=1.6)

right=fig.add_subplot(grid[0,2]);right.axis("off")
right.text(0,.98,"The factor estimates match the numerators",
           fontsize=12.2,fontweight="bold",color=dark,va="top",wrap=True)
def box(y,height,color,title,formula,body):
    right.add_patch(FancyBboxPatch((0,y),.99,height,boxstyle="round,pad=.018",
                    transform=right.transAxes,facecolor=color,edgecolor="#99aeb8",lw=1))
    right.text(.045,y+height-.025,title,fontsize=12,fontweight="bold",color=dark,va="top")
    right.text(.045,y+height-.1,formula,fontsize=12.5,color=dark,va="top")
    right.text(.045,y+.025,body,fontsize=10.7,color=dark,va="bottom",linespacing=1.4)
box(.54,.3,"#e4f3f8","First-order factor",r"$\|Ww_1\|^2$",
    "Cofactor order 2.\nConstant numerator.")
box(.12,.34,"#fff0e3","Intact quadratic factor",
    r"$\tau^2\|Ww_2\|^2+\|WDw_2\|^2$",
    "Cofactor order 1.\nAffine numerator.")

bottom=fig.add_subplot(grid[1,:]);bottom.axis("off")
bottom.text(.0,.95,"Recover every order-two derivative, then absorb the complete error",
            fontsize=13.5,fontweight="bold",color=dark,va="top")
bottom.text(.01,.56,r"$N_2=\tau^4\|Wu\|^2+\tau^2\sum_{|\alpha|=1}\|WD^\alpha u\|^2"
                          r"+\sum_{|\alpha|=2}\|WD^\alpha u\|^2$",
            fontsize=15,color=dark,va="center")
bottom.text(.01,.1,r"$N_2\leq C_1\|WP_\epsilon u\|^2+C_2\epsilon^2N_2$",
            fontsize=16,color=dark,va="center")
bottom.add_patch(FancyArrowPatch((.53,.1),(.63,.1),transform=bottom.transAxes,
                                 arrowstyle="-|>",mutation_scale=16,color=dark,lw=1.6))
bottom.text(.65,.1,r"$C_2\epsilon^2\leq\frac{1}{2}"
                       r"\ \Longrightarrow\ N_2\leq2C_1\|WP_\epsilon u\|^2$",
            fontsize=15.5,color=dark,va="center")
fig.savefig(destination,dpi=200,facecolor=fig.get_facecolor(),
            metadata={"Software":"Matplotlib; original CC0 AN-05 mathematical source"})
plt.close(fig)
print(str(destination))
