"""Reproduce the exact fibre geometry, dimensions and cusp period."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
import numpy as np
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
args=parser.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
 "svg.hashsalt":"finite-monodromy-envelope-PM-v1"})
fig=plt.figure(figsize=(17,12),dpi=150,facecolor="#f5f8fc")
blue="#175c9d";ink="#172e46";green="#117760";muted="#52677f"
fig.text(.5,.958,"Finite monodromy under full special kernel actions",
 ha="center",color=ink,fontsize=25)
ax=fig.add_axes([.035,.44,.40,.43]);ax.set_aspect("equal")
ax.set_xlim(-2.23,2.23);ax.set_ylim(-2.23,2.23);ax.axis("off")
ax.add_patch(Circle((0,0),2,fc="white",ec=blue,lw=2))
ax.add_patch(Circle((0,0),1,fill=False,ec=muted,lw=1.2,ls="--"))
ax.add_patch(Circle((0,0),.5,fc="#e2f0eb",ec=green,lw=1))
roots=[(-.4,0),(.1,.25),(.25,-.3)]
for i,(re,im)in enumerate(roots):
 ax.plot(re,im,"o",ms=7,color="#a94d36")
 ax.text(re-.09,im+.12,str(i+1),color="#a94d36",fontsize=13)
a=complex(1.5,0);t=complex(.6,.2)
ax.plot(a.real,a.imag,"s",ms=8,color=blue)
ax.text(1.48,-.22,r"$a=1.5$",ha="center",color=blue)
ax.plot(t.real,t.imag,"o",ms=7,color=ink)
ax.text(.62,.34,r"$t=0.6+0.2i$",color=ink,fontsize=14)
ax.annotate("",xy=(t.real,t.imag),xytext=(a.real,a.imag),
 arrowprops={"arrowstyle":"->","color":blue,"lw":2})
ax.text(-1.1,-1.67,r"$D_R,\ R=2$",color=blue)
ax.text(-.7,.99,r"$r=1$",color=muted)
ax.text(-.67,-.77,r"$D_{r/2}$",color=green)
fig.text(.235,.428,"One exact three-puncture fibre; PM.1, PM.9.",
 ha="center",color=muted,fontsize=14)
fig.text(.235,.399,"The drawn segment avoids every puncture.",
 ha="center",color=muted,fontsize=14)
right=fig.add_axes([.48,.45,.49,.40]);right.axis("off")
def box(x,y,w,h,text,color=blue,size=21):
 right.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.012",
  facecolor="white",edgecolor=color,linewidth=1.6))
 right.text(x+w/2,y+h/2,text,ha="center",va="center",color=ink,fontsize=size)
box(.02,.70,.95,.25,
 r"$0\ \longrightarrow\ \mathbb{W}_0\ \longrightarrow\ \mathbb{W}"
 r"\ \longrightarrow\ V_t\ \longrightarrow\ 0$"+"\n"+
 r"$qm\qquad\qquad q(m+1)\qquad\quad q$",size=19)
box(.02,.35,.95,.23,
 r"$Q=P_0+V_J,\qquad Qf\ \in\ {\cal F}(\mathfrak{b})$"+"\n"+
 r"$\mathfrak{b}=\mathrm{Ann}(V\oplus\mathbb{W})\subset\mathfrak{a}$",size=19)
box(.02,.02,.95,.21,
 r"$\dim\,\mathbb{C}[\pi]/\mathfrak{b}\ \leq\ q^2(m+2)^2$",green,20)
fig.text(.728,.417,"All operator coefficients and tails share this finite envelope.",
 ha="center",color=muted,fontsize=14)
fig.text(.728,.388,"The bound is on monodromy type, not the joint span of all outputs.",
 ha="center",color=muted,fontsize=13)
fig.add_artist(plt.Line2D([.04,.96],[.356,.356],color="#d0dce8"))
fig.text(.5,.32,"A period can remain singular on the base discriminant",
 ha="center",color=blue,fontsize=21)
low=fig.add_axes([.05,.07,.28,.21]);low.set_aspect("equal");low.axis("off")
low.set_xlim(-.28,.28);low.set_ylim(-.16,.16)
low.axhline(0,lw=.8,color=muted)
low.plot([-.125,.125],[0,0],"o",color="#a94d36")
low.text(-.125,-.06,r"$-1/8$",ha="center",color=ink)
low.text(.125,-.06,r"$1/8$",ha="center",color=ink)
ang=np.linspace(0,2*np.pi,241)
low.plot(.125+.04*np.cos(ang),.04*np.sin(ang),color=blue,lw=2)
low.annotate("",xy=(.125,.04),xytext=(.142,.036),
 arrowprops={"arrowstyle":"->","color":blue})
low.text(0,.115,r"$x=1/4,\quad s=\pm x^{3/2}$",
 ha="center",color=muted,fontsize=14)
fig.text(.64,.24,r"$f(s,x)=\dfrac{1}{s^2-x^3},\qquad J=1,\quad P_0=0$",
 ha="center",color=ink,fontsize=22)
fig.text(.64,.165,
 r"$\Delta V_Jf=\pi i\,x^{-3/2}\quad"
 r"\left(=8\pi i\ \mathrm{at}\ x=1/4\right)$",
 ha="center",color=blue,fontsize=22)
fig.text(.64,.105,
 "This period is holomorphic in the full output variable t,",
 ha="center",color=muted,fontsize=15)
fig.text(.64,.067,
 "and is singular at x=0. It lies in the precise gauge G.  [PM.20–PM.21]",
 ha="center",color=muted,fontsize=15)
fig.text(.5,.027,
 "Exact plotted coordinates and proved dimensions; the arbitrary-rank argument is PM.A–PM.D.",
 ha="center",color=muted,fontsize=13)
stem="finite-monodromy-envelope"
fig.savefig(out/(stem+".png"),dpi=150,metadata={"Software":"Matplotlib"})
fig.savefig(out/(stem+".svg"),metadata={"Date":None,"Creator":"Open mathematics course figures"})
plt.close(fig)
data={"fibre":{"R":2,"r":1,"a":[1.5,0],"t":[.6,.2],"roots":roots,
 "segment_avoids_roots":True,"example_m":3},
 "ranks":{"input":"q","period":"q*m","relative":"q*(m+1)",
 "output_envelope":"q*(m+2)","annihilator_codimension_bound":"q^2*(m+2)^2"},
 "cusp":{"polynomial":"s^2-x^3","x":"1/4","roots":["-1/8","1/8"],
 "positive_root_loop_radius":"1/25","orientation":"counterclockwise",
 "period":"pi*i*x^(-3/2)","period_at_x":"8*pi*i"},
 "proof_locators":["PM.1","PM.5–PM.7","PM.9–PM.19","PM.20–PM.21"],
 "nature":"Exact illustrative fibres and proved maps/bounds; no numerical solution of a holonomic module."}
(out/(stem+"-data.json")).write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
