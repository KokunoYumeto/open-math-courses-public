"""CC0 1.0: exact cubic cluster in the retained original unit ball."""
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

HERE=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--output",type=Path,default=HERE)
OUT=parser.parse_args().output
OUT.mkdir(parents=True,exist_ok=True)
alpha=Q(1,16);v=-Q(1,16);eta=Q(1,80);R=Q(3,32);delta=Q(1,5)
a0=Q(1,1024);a1=Q(1,256);a2=R*R
critical=[Q(-1,4),Q(1,4)]
values=[Q(1,96),Q(-1,96)]
levels=sorted((c-v)**2 for c in values)
assert eta<abs(v)/4
assert abs(v)+eta<R and R+abs(v)<delta
assert a0<levels[0]<a1<levels[1]<a2
boundary_min=Q(1,3)-alpha
assert boundary_min>delta
roots0=np.roots([1,0,0,-3*float(v)])
roots1=np.roots([1,0,-3*float(alpha),-3*float(v)])
assert np.max(abs(roots0))<1 and np.max(abs(roots1))<1
assert max(abs(roots0**3/3-float(v)))<1e-12
assert max(abs(roots1**3/3-float(alpha)*roots1-float(v)))<1e-12
plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none","svg.hashsalt":"SH02-IH-cubic-20261008"})
def render(portrait):
    plt.rcParams.update({"font.size":12 if portrait else 10})
    fig=plt.figure(figsize=(6.4,17.4) if portrait else (16.8,6.2),layout="constrained")
    grid=fig.add_gridspec(3,1) if portrait else fig.add_gridspec(1,3,width_ratios=[1,1.12,1.30])
    ax=fig.add_subplot(grid[0]);ay=fig.add_subplot(grid[1]);az=fig.add_subplot(grid[2])
    blue="#2875bb";green="#147c53";orange="#bc6317";purple="#6c4fa0"
    ax.add_patch(Circle((0,0),1,fill=False,color="#34404c",lw=1.6))
    ax.scatter(roots0.real,roots0.imag,color=blue,s=60,label=r"$g_0^{-1}(v)$: three points",zorder=4)
    ax.scatter(roots1.real,roots1.imag,color=green,s=60,marker="s",label=r"$g_1^{-1}(v)$: three points",zorder=4)
    ax.scatter([float(c) for c in critical],[0,0],color=orange,marker="*",s=130,zorder=5)
    ax.annotate(r"$p_-=-1/4$",(-.25,0),xytext=(-.65,.15),arrowprops={"arrowstyle":"-","color":orange},color=orange)
    ax.annotate(r"$p_+=1/4$",(.25,0),xytext=(.18,.22),arrowprops={"arrowstyle":"-","color":orange},color=orange)
    ax.scatter([0],[0],color="#34404c",s=16)
    ax.text(0,-1.22,r"Original $C=\{|z|\leq1\}$, $\rho=|z|^2$",ha="center")
    ax.set(xlim=(-1.3,1.3),ylim=(-1.34,1.35),xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$")
    ax.set_aspect("equal");ax.grid(alpha=.15);ax.legend(loc="upper left",fontsize=10 if portrait else 8)
    ax.set_title("1  Keep the original ball and fibres",loc="left",fontweight="bold")

    for radius,color,style,label in [
        (float(R),"#34404c","-",r"Top radius $R=3/32$"),
        (float(Q(7,96)),purple,"--",r"Higher level $\ell_2=49/9216$"),
        (float(Q(5,96)),orange,"--",r"Lower level $\ell_1=25/9216$"),
        (float(Q(1,32)),green,":",r"Bottom radius $\sqrt{a_0}=1/32$")]:
        ay.add_patch(Circle((float(v),0),radius,fill=False,color=color,linestyle=style,lw=1.4,label=label))
    ay.plot([float(-eta),float(eta)],[0,0],lw=6,color=orange,alpha=.3,zorder=1)
    ay.scatter([float(v),0,float(values[0]),float(values[1])],[0,0,0,0],
               color=["#34404c","#34404c",purple,orange],s=[45,22,55,55],zorder=5)
    ay.annotate(r"$v=-1/16$",(float(v),0),xytext=(-.11,-.019),arrowprops={"arrowstyle":"-","color":"#34404c"})
    ay.annotate(r"$c_-=+1/96$",(float(values[0]),0),xytext=(.010,.040),arrowprops={"arrowstyle":"-","color":purple},color=purple)
    ay.annotate(r"$c_+=-1/96$",(float(values[1]),0),xytext=(-.029,-.055),arrowprops={"arrowstyle":"-","color":orange},color=orange)
    ay.text(-.156,-.122,r"$c_\pm(s)=\mp s^{3/2}/96$: the whole cluster",fontsize=9)
    ay.set(xlim=(-.17,.055),ylim=(-.132,.113),xlabel=r"$\operatorname{Re}g_s$",ylabel=r"$\operatorname{Im}g_s$")
    ay.set_aspect("equal");ay.grid(alpha=.15);ay.legend(loc="upper left",fontsize=9 if portrait else 7.7)
    ay.set_title("2  One value disc contains\nthe whole cluster" if portrait else "2  One value disc contains the whole cluster",loc="left",fontweight="bold")

    az.axis("off")
    az.set(xlim=(0,1.10),ylim=(0,1))
    az.set_title("3  Restriction arrows give\nreverse exit order" if portrait else "3  Restriction arrows give reverse exit order",loc="left",fontweight="bold")
    az.text(.02,.93,r"$g_s(z)=z^3/3-sz/16,\quad 0\leq s\leq1$",fontsize=12)
    az.text(.02,.83,r"$h=|g_1-v|^2,\quad B_j=C\cap\{h\leq a_j\}$",fontsize=11)
    az.text(.02,.73,r"$(a_0,a_1,a_2)=(1/1024,\ 1/256,\ 9/1024)$",fontsize=10)
    xs=[.07,.43,.85]
    for x,t in zip(xs,[r"$F_0=0$",r"$F_1$",r"$F_2=M_{g_0}$"]):
        az.text(x,.56,t,ha="center",fontsize=13,color="#34404c")
    for left,right in zip(xs,xs[1:]):
        az.add_patch(FancyArrowPatch((left+.08,.575),(right-.075,.575),arrowstyle="-|>",mutation_scale=14,color="#34404c"))
    az.text(.41,.47,r"$F_1=R\Gamma(B_2,B_1)$",ha="center",fontsize=10)
    az.text(.65,.37,r"$F_2=R\Gamma(B_2,B_0)$",ha="center",fontsize=10)
    az.text(.12,.28,r"first quotient $Q_2$: higher level",color=purple,fontsize=10)
    az.text(.12,.20,r"second quotient $Q_1$: lower level",color=orange,fontsize=10)
    az.text(.02,.08,"For the perverse constant sheaf K[1]:\n"
            r"$Q_1\simeq Q_2\simeq K$,  $\dim_K M_{g_0}=2$",fontsize=10)
    fig.suptitle("An exact degenerate cubic,\nits perturbation and original pair" if portrait else "An exact degenerate cubic, its linear perturbation and the original pair",fontsize=15,fontweight="bold")
    stem="isolated-cubic-cluster-mobile" if portrait else "isolated-cubic-cluster"
    fig.savefig(OUT/(stem+".svg"),metadata={"Date":"2026-10-08T00:00:00Z"})
    fig.savefig(OUT/(stem+".png"),dpi=170)
    fig.savefig(OUT/(stem+".pdf"),metadata={"CreationDate":None,"ModDate":None})
    plt.close(fig)
render(False)
render(True)
metadata=dict(licence="CC0-1.0",equations="g_s=z^3/3-sz/16; rho=|z|^2",
parameters={k:str(val) for k,val in dict(alpha=alpha,v=v,eta=eta,R=R,delta=delta,a0=a0,a1=a1,a2=a2,boundary_min=boundary_min).items()},
critical_points=list(map(str,critical)),critical_values=list(map(str,values)),
critical_levels=list(map(str,levels)),root_samples={"unperturbed":[[float(z.real),float(z.imag)] for z in roots0],"endpoint":[[float(z.real),float(z.imag)] for z in roots1]},
proved_boundary_bound="On |z|=1, |g_s(z)| >= 1/3-1/16=13/48 > delta=1/5; the controlled value faces miss the original sphere for all s.",
proof_locators=["IH3","IH14","IH15","IH16","IH21","IH22"],
plot_status="Exact mathematical metadata; visual inspection and byte reproduction recorded separately by the course owner")
(OUT/"FIGURE_MATH.json").write_text(json.dumps(metadata,indent=2)+"\n",encoding="utf-8")
