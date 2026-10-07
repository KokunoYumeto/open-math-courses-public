"""Reproduce the exact center-flow models and the translation-crossing shear.

Run python render.py with NumPy and Matplotlib. No network or external data.
Original renderer, diagram and data: CC0-1.0 to the extent of rights held.
Font terms are copied alongside the rendered files.
"""
from pathlib import Path
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Arc

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                     "mathtext.fontset":"dejavusans","svg.fonttype":"none"})
INK="#213345"; MUTED="#5c6d7b"; BLUE="#176495"; GREEN="#2c7c50"; ORANGE="#b25725"
fig,axes=plt.subplots(2,2,figsize=(18,13))
fig.patch.set_facecolor("#fbfcfe")
fig.subplots_adjust(left=.035,right=.975,bottom=.073,top=.88,hspace=.19,wspace=.12)
fig.suptitle("Center flows: periods and eigenfrequencies",
             y=.968,fontsize=23,fontweight="bold",color=INK)
fig.text(.5,.925,"Exact commutative models and a semifinite trace-scaling comparison",
         ha="center",fontsize=16,color=MUTED)

def panel(ax,title):
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.add_patch(Rectangle((0,0),1,1,fill=False,edgecolor="#cbd5df",lw=1.2))
    ax.text(.028,.953,title,va="top",fontsize=18,fontweight="bold",color=INK)

def txt(ax,x,y,value,**kw):
    ax.text(x,y,value,color=kw.pop("color",INK),**kw)

def arrow(ax,a,b,color=MUTED):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=16,lw=1.5,color=color))

ax=axes[0,0]
panel(ax,"A  A circle period and its eigenfunction phase")
txt(ax,.5,.815,r"$a=\log4,\qquad a_1(r)=e^{2\pi ir/a}$",ha="center",fontsize=19)
circle=ax.inset_axes([.04,.25,.44,.5])
circle.set(xlim=(-1.55,1.55),ylim=(-1.4,1.4),aspect="equal");circle.axis("off")
circle.add_patch(Circle((0,0),1,fill=False,edgecolor="#94a6b4",lw=1.5))
circle.add_patch(Arc((0,0),1.7,1.7,theta1=0,theta2=90,color=ORANGE,lw=2))
circle.add_patch(FancyArrowPatch((.13,.84),(0,.85),arrowstyle="-|>",color=ORANGE,mutation_scale=14))
for q,(x,y),label in [(0,(1,0),r"$r=0$"),(1,(0,1),r"$r=a/4$"),(2,(-1,0),r"$r=a/2$"),(3,(0,-1),r"$r=3a/4$")]:
    circle.scatter([x],[y],s=60,color=ORANGE if q==1 else BLUE,zorder=4)
    align="right" if x<0 else ("left" if x>0 else "center")
    circle.text(1.20*x,1.22*y,label,ha=align,va="center",fontsize=12,color=INK)
circle.text(0,.15,r"$s=a/4$",ha="center",color=ORANGE,fontsize=14)
circle.text(0,-.17,r"$e^{2\pi is/a}=i$",ha="center",color=ORANGE,fontsize=14)
txt(ax,.73,.66,r"$K=a\mathbb{Z}$",ha="center",fontsize=22,color=BLUE)
txt(ax,.73,.51,r"$\mathcal{E}=(2\pi/a)\mathbb{Z}$",ha="center",fontsize=20,color=GREEN)
txt(ax,.73,.36,"The circle drawn is the phase",ha="center",fontsize=12,color=MUTED)
txt(ax,.73,.30,r"of $a_1$, not a length scale.",ha="center",fontsize=12,color=MUTED)
txt(ax,.5,.155,r"scalar center: $C=\mathbb{C},\quad K=\mathbb{R},\quad\mathcal{E}=\{0\}$",
    ha="center",fontsize=17)
txt(ax,.5,.055,"No factor-realization existence claim is made.",ha="center",fontsize=13,color=MUTED)

ax=axes[0,1]
panel(ax,"B  The irrational torus flow")
txt(ax,.5,.815,r"$s\longmapsto(s,\sqrt{2}s)\ \mathrm{mod}\ \mathbb{Z}^2,\quad 0\leq s\leq2$",
    ha="center",fontsize=17)
torus=ax.inset_axes([.06,.25,.44,.49])
torus.set(xlim=(0,1),ylim=(0,1),aspect="equal")
torus.set_xticks([0,.5,1]);torus.set_yticks([0,.5,1])
torus.set_xlabel(r"$x$",fontsize=13,labelpad=1);torus.set_ylabel(r"$y$",fontsize=13,rotation=0,labelpad=6)
torus.grid(color="#e1e7ec",lw=.7)
# Split at every exact crossing of a horizontal or vertical square edge.
sqrt2=np.sqrt(2)
breaks=sorted(set([0.,1.,2.]+[j/sqrt2 for j in range(1,3)]))
segments=[]
for lo,hi in zip(breaks[:-1],breaks[1:]):
    mid=(lo+hi)/2
    floorx=int(np.floor(mid));floory=int(np.floor(sqrt2*mid))
    ss=np.array([lo,hi]);xx=ss-floorx;yy=sqrt2*ss-floory
    torus.plot(xx,yy,color=BLUE,lw=2.2)
    segments.append({"s_start":float(lo),"s_end":float(hi),"x_floor":floorx,"y_floor":floory})
for n,color in [(0,BLUE),(1,ORANGE),(2,GREEN)]:
    x=0.;y=(sqrt2*n)%1
    torus.scatter([x],[y],s=55,color=color,zorder=5,clip_on=False)
    torus.text(.04,y+.035 if n<2 else y-.075,f"s={n}",fontsize=11,color=color)
txt(ax,.75,.66,r"$K=\{0\}$",ha="center",fontsize=22,color=BLUE)
txt(ax,.75,.51,r"$\theta_1(\chi_{1,0})=\chi_{1,0}$",ha="center",fontsize=17)
txt(ax,.75,.37,r"$\theta_1(\chi_{0,1})$",ha="center",fontsize=17)
txt(ax,.75,.28,r"$=e^{2\pi i\sqrt{2}}\chi_{0,1}$",ha="center",fontsize=17)
txt(ax,.5,.12,"Opposite square edges are identified. Only one finite segment is drawn.",
    ha="center",fontsize=12,color=MUTED)
txt(ax,.5,.047,"The full Fourier proof establishes ergodicity.",ha="center",fontsize=13,color=MUTED)

ax=axes[1,0]
panel(ax,"C  A dense frequency group with no periods")
txt(ax,.5,.81,r"$p/(2\pi)=m+\sqrt{2}n,\quad -3\leq m,n\leq3$",
    ha="center",fontsize=18)
freq=ax.inset_axes([.07,.55,.87,.18])
vals=sorted([(m+sqrt2*n,m,n) for m in range(-3,4) for n in range(-3,4)])
freq.axhline(0,color="#b7c4cf",lw=1)
freq.scatter([v[0] for v in vals],[0]*len(vals),s=30,color=BLUE,zorder=3)
freq.plot([.5,.5],[0,.09],":",color=ORANGE,lw=1)
freq.scatter([.5],[.09],s=55,facecolors="none",edgecolors=ORANGE,linewidths=1.5,zorder=4)
freq.text(.5,.18,r"$1/2\notin\mathbb{Z}+\sqrt{2}\mathbb{Z}$",ha="center",fontsize=12,color=ORANGE)
freq.set(xlim=(-7.7,7.7),ylim=(-.18,.28),yticks=[])
freq.set_xticks([-6,-3,0,3,6]);freq.set_xlabel(r"$p/(2\pi)$",fontsize=13,labelpad=1)
freq.spines[["top","right","left"]].set_visible(False)
txt(ax,.5,.39,"49 exact algebraic sample frequencies; these dots do not prove density.",
    ha="center",fontsize=12,color=MUTED)
txt(ax,.5,.275,r"$0<|q\sqrt{2}-p|<1/N$",ha="center",fontsize=19,color=GREEN)
txt(ax,.5,.18,"Small nonzero group elements approximate every real number by multiples.",
    ha="center",fontsize=12,color=MUTED)
txt(ax,.5,.068,r"conditional type III: $S=\{0,1\}$,  $T=2\pi(\mathbb{Z}+\sqrt{2}\mathbb{Z})$",
    ha="center",fontsize=16)

ax=axes[1,1]
panel(ax,"D  Translation crossing: the exact shear")
txt(ax,.5,.815,r"$N_0=L^\infty(\mathbb{R}),\quad \tau_0(f)=\int e^x f(x)\,dx$",
    ha="center",fontsize=17)
txt(ax,.5,.70,r"$\theta_s f(x)=f(x+s),\qquad \tau_0\theta_s=e^{-s}\tau_0$",
    ha="center",fontsize=17)
txt(ax,.24,.555,r"$(r,x)$",ha="center",fontsize=20,color=BLUE)
txt(ax,.75,.555,r"$(y,z)=(x-r,x)$",ha="center",fontsize=20,color=GREEN)
arrow(ax,(.36,.57),(.52,.57))
txt(ax,.24,.435,r"$r\mapsto r-s$",ha="center",fontsize=17,color=BLUE)
txt(ax,.75,.435,r"$y\mapsto y+s,\quad z\mapsto z$",ha="center",fontsize=16,color=GREEN)
arrow(ax,(.36,.455),(.52,.455))
txt(ax,.5,.31,r"$W P W^*=B(L^2(\mathbb{R}_y))\otimes I_{L^2(\mathbb{R}_z)}$",
    ha="center",fontsize=17)
txt(ax,.5,.20,r"$K=\{0\},\quad S(P)=\{1\},\quad T(P)=\mathbb{R}$",
    ha="center",fontsize=19,color=ORANGE)
txt(ax,.5,.075,"A semifinite factor: trace scaling alone does not imply type III.",
    ha="center",fontsize=13,color=MUTED)

fig.text(.5,.025,"Proofs: MIV6.d–f (complete Fourier basis), MIV6.h–o (all periods and eigenfrequencies), MIV6.p–x (full semifinite crossing).",
         ha="center",fontsize=12,color=MUTED)
for ext in ("png","svg"):
    fig.savefig(HERE/f"modular-invariants.{ext}",dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
data={
 "title":"Center flows: periods and eigenfrequencies",
 "license":"CC0-1.0 to the extent of rights held; font terms separate",
 "circle":{"a":"log(4)","flow":"theta_s f(r)=f(r+s)","character":"exp(2*pi*i*r/a)",
           "displayed_time":"a/4","displayed_phase":"i","K":"a Z","E":"(2*pi/a) Z",
           "phase_circle_notice":"The rendered unit circle is the value of the character, not physical circumference a."},
 "scalar":{"algebra":"C","flow":"identity","K":"R","E":"{0}"},
 "torus":{"flow":"(x,y)->(x+s,y+sqrt(2)*s) mod Z^2","interval":[0,2],
          "exact_segment_breaks":["0","1/sqrt(2)","1","sqrt(2)","2"],
          "rendered_segments":segments,"samples":[{"s":n,"exact_x":"0","exact_y":f"{n}*sqrt(2)-floor({n}*sqrt(2))"} for n in range(3)],
          "K":"{0}","E":"2*pi*(Z+sqrt(2)*Z)","fixed_algebra":"C1",
          "notice":"Finite orbit segment only; complete basis and ergodicity are proved in MIV6.c-m."},
 "frequencies":{"axis":"p/(2*pi)","range_of_indices":[-3,3],
                "sample":[{"m":m,"n":n,"exact_value":f"{m}+({n})*sqrt(2)"} for _,m,n in vals],
                "omitted_point":"1/2 is not in Z+sqrt(2) Z","notice":"Finite dots do not prove density; MIV6.n does."},
 "conditional_type_III":{"circle":{"lambda":"1/4","S":"{0} union {4^n:n in Z}","T":"(2*pi/log(4))*Z"},
                        "scalar":{"S":"[0,infinity)","T":"{0}"},
                        "torus":{"S":"{0,1}","T":"2*pi*(Z+sqrt(2)*Z)"},
                        "condition":"Only when the model is the center flow of a system with type III factor crossing; no factor realization asserted."},
 "translation":{"N":"L-infinity(R)","trace":"integral exp(x)*f(x) dx","flow":"f(x)->f(x+s)",
                "trace_scale":"exp(-s)","regular_coeff":"f(x-r)","regular_group":"xi(r-s,x)",
                "coordinates":{"y":"x-r","z":"x","inverse_r":"z-y","inverse_x":"z","absolute_jacobian":1},
                "W":"W xi(y,z)=xi(z-y,z)","transformed_group":"eta(y+s,z)",
                "whole_crossing":"B(L2(R_y)) tensor I_(L2(R_z))","K":"{0}","S":"{1}","T":"R",
                "projection":"W^*(|1_[0,1]><1_[0,1]| tensor I)W","projection_factor_trace":1},
 "proof_locators":["MIV6.d-f","MIV6.h-o","MIV6.p-x","MIV7.a-f"]
}
(HERE/"data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font=Path(font_manager.findfont("DejaVu Sans"))
license_file=font.parent/"LICENSE_DEJAVU"
if not license_file.is_file():raise FileNotFoundError("Missing bundled font terms")
shutil.copyfile(license_file,HERE/"FONT-LICENSE.txt")
(HERE/"TERMS.md").write_text(
 "# Figure terms\n\nOriginal diagram, exact mathematical data and renderer: CC0-1.0 to the extent of rights held. "
 "DejaVu font terms are retained in FONT-LICENSE.txt. No external image, source excerpt or downloaded data is included. "
 "Run python render.py with NumPy and Matplotlib to reproduce the PNG, editable SVG and data. "
 "Torus segments and frequency dots are numerical renderings of exact algebraic expressions; the complete "
 "Fourier-basis, ergodicity and density proofs are in the lesson. The conditional type III values assert no "
 "factor-realization theorem. The translation comparison is an explicitly proved semifinite factor.\n",encoding="utf-8")
print("Rendered original PNG/SVG, exact data and font terms.")
