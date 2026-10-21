"""Reproduce the NT tensor, coefficient and nested-radius diagram."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
 "svg.hashsalt":"nuclear-tensor-closed-target-NT-20261020",
 "mathtext.fontset":"dejavusans"})
fig,axes=plt.subplots(3,1,figsize=(4.8,10.2),
 gridspec_kw={"height_ratios":[1.1,1.15,1.2]})
fig.patch.set_facecolor("#ffffff")
blue="#164d78"; teal="#087d76"; orange="#b96517"; ink="#17283a"
def base(ax,title):
 ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
 ax.add_patch(FancyBboxPatch((.015,.025),.97,.94,boxstyle="round,pad=0.01",
  linewidth=1.2,edgecolor="#c4d2df",facecolor="#f6f9fc"))
 ax.text(.5,.91,title,ha="center",va="center",weight="bold",color=ink,fontsize=14)
def arr(ax,a,b,color=blue):
 ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","color":color,"lw":1.7})
base(axes[0],"Tensor exactness · NT.19")
a=axes[0]
for y,label in [(.74,r"$E_1\,\widehat\otimes\,F$"),(.53,r"$E_2\,\widehat\otimes\,F$"),(.32,r"$E_3\,\widehat\otimes\,F$")]:
 a.text(.33,y,label,ha="center",va="center",color=blue,fontsize=17)
arr(a,(.33,.68),(.33,.59));arr(a,(.33,.47),(.33,.38))
a.text(.65,.64,"closed\nembedding",ha="center",va="center",color=teal)
a.text(.65,.43,"open\nsurjection",ha="center",va="center",color=teal)
a.text(.5,.13,"left image = full kernel",ha="center",va="center",color=ink)
base(axes[1],"Closed target · NT.27–31")
a=axes[1]
for x,y,label in [(.24,.70,r"$P$"),(.76,.70,r"$T$"),(.24,.36,r"$E_B$"),(.76,.36,r"$T$")]:
 a.text(x,y,label,ha="center",va="center",color=blue,fontsize=19)
arr(a,(.32,.70),(.67,.70));arr(a,(.32,.36),(.67,.36))
arr(a,(.24,.61),(.24,.45));arr(a,(.76,.61),(.76,.45))
a.text(.5,.77,r"$k$",ha="center",color=teal,fontsize=16)
a.text(.5,.42,r"$f_B$",ha="center",color=teal,fontsize=16)
a.text(.13,.53,r"$p$",ha="center",color=teal,fontsize=16)
a.text(.87,.53,r"$1_T$",ha="center",color=teal,fontsize=16)
a.text(.5,.16,r"$P=B\,\widehat\otimes\,E,\quad k=f_Bp$",ha="center",color=ink,fontsize=13)
a.text(.5,.065,r"$T$ closed in $F_B$; $p$ onto",ha="center",color=ink,fontsize=12)
base(axes[2],"Nested analytic radii · NT.23")
a=axes[2]
a.set_aspect("equal")
# The circles have the exact example radii 1,2,3,4 under scale 0.081.
cx,cy=.38,.49
for v,col in [(4,blue),(3,teal),(2,orange),(1,"#8c3f86")]:
 a.add_patch(Circle((cx,cy),.081*v,fill=False,edgecolor=col,lw=1.4))
 a.text(.81,.78-.135*(4-v),f"{['','r','s','t','R'][v]} = {v}",
  ha="center",va="center",color=col,fontsize=14)
a.text(.5,.11,r"$r<s<t<R$",ha="center",va="center",color=ink,fontsize=17)
fig.subplots_adjust(left=.035,right=.965,top=.99,bottom=.01,hspace=.10)
fig.savefig(r/"nuclear-tensor-closed-target.png",dpi=180,metadata={"Software":"Matplotlib"})
fig.savefig(r/"nuclear-tensor-closed-target.svg",metadata={"Date":None})
plt.close(fig)
data={
 "proof_locators":["NT.19","NT.27--NT.31","NT.23"],
 "scalar_sequence":{"first":"closed topological embedding",
  "last":"open surjection","middle":"left image equals full kernel"},
 "coefficient_diagram":{"P":"B completed_tensor_C E","p":"P -> E_B onto",
  "T":"B completed_tensor_A F_1, closed in F_B",
  "identity":"k = f_B p","nuclear_presentation":"k is B-nuclear"},
 "radius_example":{"r":1,"s":2,"t":3,"R":4,
  "circle_scale":"81/1000","circle_center":["19/50","49/100"],
  "coordinate_dimension":1,"weights":"(s/t)^alpha",
  "one_variable_weight_sum":3},
 "no_general_fibre_or_characteristic_geometry_depicted":True}
(r/"nuclear-tensor-closed-target-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
