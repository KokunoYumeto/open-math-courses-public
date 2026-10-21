"""Reproduce exact coefficient radii, signed cone columns and graph-Cech maps."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "svg.hashsalt":"GL-DMOD-GI-20261021"})
fig,(a,b)=plt.subplots(1,2,figsize=(14,8.4),facecolor="#f7f9fd")
ink="#14243d";blue="#2758aa";teal="#00818d";gold="#a76912"
a.set(xlim=(.245,.92),ylim=(0,1));a.axis("off")
b.set(xlim=(0,1),ylim=(0,1));b.axis("off")
a.set_title("Exact shrinking radii (N=2) and signed cone columns",fontweight="bold",color=ink,pad=18)
b.set_title("Actual proper-image coefficient model",fontweight="bold",color=ink,pad=18)
t=Fraction(1,3);N=2;rows=[]
a.axvline(float(t),ymin=.33,ymax=.95,color=gold,lw=1.3,ls="--")
a.text(float(t),.98,r"$t=1/3$",ha="center",color=gold,fontsize=12)
for index,q in enumerate([2,1,0,-1,-2]):
 radius=t+(1-t)*Fraction(2)**(q-N-1);y=.88-.11*index
 a.plot([float(t),float(radius)],[y,y],color=teal,lw=2)
 a.plot(float(radius),y,"o",ms=7,color=blue)
 a.text(.255,y,f"q={q}",va="center",ha="left",color=ink,fontsize=11)
 a.text(.735,y,rf"$t_{{{q}}}={radius.numerator}/{radius.denominator}$",
  va="center",ha="left",color=blue,fontsize=12)
 rows.append({"q":q,"t_q_numerator":radius.numerator,"t_q_denominator":radius.denominator})
a.text(.56,.31,"GI.25: every finite stage has a radius strictly above t",
 ha="center",va="center",color=ink,fontsize=9.8)
a.text(.56,.225,r"$D(a,e)=(d_La,\ ha-d_Ee)$",ha="center",va="center",color=blue,fontsize=14)
a.text(.56,.145,r"$D(a,e)=0\quad\Longrightarrow\quad d_La=0,\ ha=d_Ee$",
 ha="center",va="center",color=ink,fontsize=12)
a.text(.56,.065,r"New columns: $d_L=a$, $h=+e$",
 ha="center",va="center",color=teal,fontsize=12)
a.text(.56,.015,"Cone cohomology in the current degree is killed; GI.28.",
 ha="center",va="center",color=ink,fontsize=9.5)
def box(y,text,sub,h=.132):
 b.add_patch(FancyBboxPatch((.025,y-h/2),.95,h,
  boxstyle="round,pad=0.012",edgecolor=blue,facecolor="white",linewidth=1.2))
 b.text(.5,y+.018,text,ha="center",va="center",color=ink,fontsize=10.5)
 b.text(.5,y-.043,sub,ha="center",va="center",color=blue,fontsize=9.4)
def down(y1,y2):
 b.annotate("",(.5,y2),(.5,y1),arrowprops={"arrowstyle":"->","color":teal,"lw":1.6})
box(.89,"Closed analytic graph of each actual overlap",
 r"$j_I:T_I\to D_0\times\Omega_I^0$; full defining ideals, GI.31")
down(.81,.75)
box(.675,"Nested acyclic covers give finite Cech complexes",
 r"$E^\bullet\to F^\bullet$; subnuclear quasi-isomorphism, GI.34–GI.37")
down(.595,.535)
box(.46,"Finite free coefficient model on one smaller base",
 r"$L^\bullet\to E^\bullet_t$; all degrees and smaller-base comparisons")
down(.38,.32)
box(.245,"Stalks identify coherent cohomology sheaves",
 r"$\mathcal{H}^q(\mathcal{L})=j_*R^qf_*\mathcal{S}$; GI.38–GI.42")
b.text(.5,.11,"Arbitrary proper analytic maps and coherent coefficients",
 ha="center",va="center",color=teal,fontsize=10.4)
b.text(.5,.06,"Singular and nonreduced spaces; no base-flatness hypothesis",
 ha="center",va="center",color=ink,fontsize=9.8)
b.text(.5,.015,"Boxes are maps and complexes, not a metric picture of a fibre.",
 ha="center",va="center",color=ink,fontsize=9.2)
fig.subplots_adjust(left=.025,right=.985,top=.91,bottom=.05,wspace=.09)
fig.savefig(r/"general-analytic-coherent-images.png",dpi=170,facecolor=fig.get_facecolor())
fig.savefig(r/"general-analytic-coherent-images.svg",metadata={"Date":None},facecolor=fig.get_facecolor())
(r/"general-analytic-coherent-images-data.json").write_text(json.dumps({
 "kind":"exact rational radius samples and signed cone/proper-image diagram",
 "proofs":["GI.25--GI.28","GI.31--GI.42"],
 "target_radius":[t.numerator,t.denominator],"N":N,"radius_rows":rows,
 "cone_differential":["d_L a","h a - d_E e"],
 "new_differential_column":"a","new_chain_map_column":"+e",
 "sample_radii_are_the_general_proof":False,
 "all_hypotheses_and_full_proofs_are_in_source":True,
 "diagram_is_a_metric_picture_of_a_fibre":False},indent=2)+"\n",encoding="utf-8")
plt.close(fig)
