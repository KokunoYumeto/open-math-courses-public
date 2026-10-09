"""Reproduce the exact reflection-group coordinates in OA-FLOW-L71, P41-P46.

Original code, geometry and diagram: CC0-1.0.
Matplotlib/DejaVu font terms are retained beside this script.
"""
from pathlib import Path
from fractions import Fraction as F
import json, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-measure-models-proper-20261009-v1"

D = Path(__file__).resolve().parent
blue, teal, orange = "#345d9d", "#087f7b", "#ad5b17"
ink, muted, grid = "#192941", "#596a80", "#d3dce7"
plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
    "font.size":12,"axes.labelcolor":ink,"xtick.color":muted,"ytick.color":muted,
    "svg.fonttype":"path"})

def mul(g,h):
    b,e=g; a,d=h
    return b+e*a,e*d

samples=[]
for y in [F(-3,4),F(1,2)]:
    c=y if y<0 else y+1
    p=F(1,2)
    h=(2*c,-1)
    plus=(p-c,1)
    minus=(p+c,-1)
    assert mul(h,h)==(0,1)
    assert mul(plus,h)==minus
    assert plus[0]+plus[1]*c==minus[0]+minus[1]*c==p
    samples.append({"y":str(y),"c":str(c),"p":str(p),
        "nonidentity_stabilizer":[str(h[0]),h[1]],
        "representatives":[[str(plus[0]),plus[1]],[str(minus[0]),minus[1]]]})
for delta in [1,-1]:
    for a in [F(-2),F(-1),F(0),F(1),F(2)]:
        p=-delta*a/2; q=a/2
        assert abs(p)<=1 and abs(q)<=1 and a==q-delta*p
data={"group":"R semidirect {+1,-1}",
    "multiplication":"(b,epsilon)(a,delta)=(b+epsilon*a,epsilon*delta)",
    "base_pieces":[["-1","0"],["0","1"]],"base_endpoints":"open",
    "base_probability_density":"1/2",
    "compact_B":[["-17/20","-13/20"],["2/5","3/5"]],
    "field":"c(y)=y on (-1,0); c(y)=y+1 on (0,1)",
    "stabilizer":"H_y={(0,+1),(2c(y),-1)}",
    "coset_coordinate":"p=b+epsilon*c(y)","samples":samples,
    "transporter":{"R":"1","a_interval":["-2","2"],"signs":[1,-1],
                   "formula":"a=q-delta*p"},
    "probability_density_on_bundle":"(1/4)*exp(-abs(p)) dy dp",
    "proof_locators":"OA-FLOW-L71.md, P19-P26 and P41-P46",
    "terms":"CC0-1.0 original diagram/code/data; accompanying font terms retained"}
(D/"figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")

fig=plt.figure(figsize=(15,11),dpi=200,facecolor="#f6f8fc")
fig.text(.06,.956,"Compact base pieces and varying cosets",fontsize=24,weight="bold",color=ink)
fig.text(.06,.916,
    r"$G=\mathbb{R}\rtimes\{1,-1\}$:  $(b,\epsilon)(a,\delta)=(b+\epsilon a,\epsilon\delta)$",
    fontsize=16,color=ink)
gs=fig.add_gridspec(2,2,left=.07,right=.95,bottom=.165,top=.845,hspace=.59,wspace=.30)
axes=[fig.add_subplot(gs[i,j]) for i in range(2) for j in range(2)]
for ax in axes:
    ax.set_facecolor("white")
    for sp in ax.spines.values():sp.set_color(grid)

# A: two open base components and an explicit compact set in them.
ax=axes[0]
ax.set_title("A. Two locally compact base pieces",loc="left",pad=15,color=ink,fontsize=15,weight="bold")
ax.set_xlim(-1.12,1.12);ax.set_ylim(-.8,1.05);ax.set_yticks([])
ax.set_xticks([-1,0,1]);ax.set_xlabel("base coordinate y")
ax.plot([-1,0],[.25,.25],color=blue,lw=5)
ax.plot([0,1],[.25,.25],color=teal,lw=5)
for x,col in [(-1,blue),(0,blue),(0,teal),(1,teal)]:
    ax.scatter([x],[.25],s=95,facecolor="white",edgecolor=col,lw=1.8,zorder=4)
ax.text(-.5,.76,r"$S_1=(-1,0)$",ha="center",color=blue,fontsize=15)
ax.text(.5,.76,r"$S_2=(0,1)$",ha="center",color=teal,fontsize=15)
ax.text(-.5,-.28,r"$c(y)=y$",ha="center",color=blue,fontsize=14)
ax.text(.5,-.28,r"$c(y)=y+1$",ha="center",color=teal,fontsize=14)
for lo,hi,col in [(-.85,-.65,blue),(.4,.6,teal)]:
    ax.plot([lo,hi],[.25,.25],lw=11,color=col,solid_capstyle="butt",alpha=.55)
ax.scatter([-.75,.5],[.25,.25],s=26,color=ink,zorder=5)
ax.text(.5,-.25,"Thick subintervals form a compact base set B.",transform=ax.transAxes,
    ha="center",fontsize=11,color=muted)

# B: exactly the translation projection of the nonidentity stabilizer.
ax=axes[1]
ax.set_title("B. The stabilizer changes continuously on each piece",loc="left",
    pad=15,color=ink,fontsize=13.2,weight="bold")
ax.set_xlim(-1.08,1.08);ax.set_ylim(-2.35,4.4)
ys=np.linspace(-1,0,160);ax.plot(ys,2*ys,color=blue,lw=3)
ys=np.linspace(0,1,160);ax.plot(ys,2*(ys+1),color=teal,lw=3)
for x,b,col in [(-1,-2,blue),(0,0,blue),(0,2,teal),(1,4,teal)]:
    ax.scatter([x],[b],s=55,facecolor="white",edgecolor=col,lw=1.6,zorder=4)
ax.axvline(0,color=grid,lw=1,ls=":");ax.set_xticks([-1,0,1])
ax.set_xlabel("base coordinate y");ax.set_ylabel(r"translation $2c(y)$")
ax.text(.5,-.26,r"Plotted element: $(2c(y),-1)$.  The identity $(0,1)$ is also in every $H_y$.",
    transform=ax.transAxes,ha="center",fontsize=10.5,color=muted)

# C: two representatives on the two disconnected sign sheets.
ax=axes[2]
ax.set_title("C. Two representatives, one coset coordinate p = 1/2",loc="left",
    pad=15,color=ink,fontsize=13.4,weight="bold")
ax.set_xlim(-1.6,2.6);ax.set_ylim(-.35,4.1)
ax.set_yticks([3,2,1,0]);ax.set_yticklabels(["+1","-1","+1","-1"])
ax.set_ylabel(r"sign $\epsilon$");ax.set_xlabel("translation coordinate b")
ax.set_xticks([-1,0,1,2])
for yy in [0,1,2,3]:ax.axhline(yy,color=grid,lw=.9)
for p1,p2,h1,h2,col,label in [
    (1.25,-.25,3,2,blue,r"$y=-3/4,\ c=-3/4$"),
    (-1,2,1,0,teal,r"$y=1/2,\ c=3/2$")]:
    ax.plot([p1,p2],[h1,h2],color=col,lw=1.8,ls="--")
    ax.scatter([p1,p2],[h1,h2],s=65,color=col,zorder=4)
    ax.text(-1.45,h1+.47,label,color=col,fontsize=12)
for b,y,label,col in [(1.25,3,"5/4",blue),(-.25,2,"−1/4",blue),
                       (-1,1,"−1",teal),(2,0,"2",teal)]:
    dx,align=(-.09,"right") if b==-.25 else (.08,"left")
    ax.text(b+dx,y+.15,label,color=col,fontsize=11,ha=align)
ax.text(.5,-.26,r"$p=b+\epsilon c(y)$.  Dashed connectors identify a coset; they are not group paths.",
    transform=ax.transAxes,ha="center",fontsize=10.5,color=muted)

# D: the full compact transporter, with both discrete signs.
ax=axes[3]
ax.set_title("D. A compact window has a compact transporter",loc="left",
    pad=15,color=ink,fontsize=13.6,weight="bold")
ax.set_xlim(-2.7,2.7);ax.set_ylim(-1.45,1.45)
ax.set_yticks([.65,-.65]);ax.set_yticklabels(["+1","-1"])
ax.set_ylabel(r"sign $\delta$");ax.set_xlabel("translation coordinate a")
ax.set_xticks([-2,-1,0,1,2])
for y in [.65,-.65]:
    ax.axhline(y,color=grid,lw=.9)
    ax.plot([-2,2],[y,y],color=orange,lw=7)
    ax.scatter([-2,2],[y,y],s=60,color=orange,zorder=3)
ax.axvline(0,color=grid,lw=1,ls=":")
ax.text(0,0,r"$a=q-\delta p,\quad |p|,|q|\leq1$",ha="center",fontsize=13,color=ink)
ax.text(.5,-.26,r"$T(B\times[-1,1],B\times[-1,1])=[-2,2]\times\{1,-1\}$",
    transform=ax.transAxes,ha="center",fontsize=11,color=muted)

fig.text(.07,.035,
    "Exact example: OA-FLOW-L71, P41–P46. General bundle topology and compact transporter bound: P23–P26.",
    color=muted,fontsize=11)
fig.savefig(D/"proper-coset-model.png",dpi=200)
fig.savefig(D/"proper-coset-model.svg", metadata={'Date': None})
plt.close(fig)

font_license=Path(matplotlib.get_data_path())/"fonts/ttf/LICENSE_DEJAVU"
shutil.copyfile(font_license,D/"FONT-LICENSE-DEJAVU.txt")
(D/"LICENSE.txt").write_text(
    "Original diagram, geometry, coordinate data and reproduction code: CC0-1.0.\n"
    "Self-checked by the writing AI. Human review and formal verification are not asserted.\n"
    "DejaVu glyph designs retain the terms in FONT-LICENSE-DEJAVU.txt.\n"
    "No third-party source page or source illustration is included.\n",encoding="utf-8")
print("Wrote 3000×2200 PNG, editable SVG, exact data, and retained font terms.")
