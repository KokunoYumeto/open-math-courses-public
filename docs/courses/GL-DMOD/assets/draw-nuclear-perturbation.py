"""Reproduce the actual factorization and finite-head coefficient diagrams."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":17,
 "svg.hashsalt":"nuclear-perturbation-20261020","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(8,11.8),dpi=150,facecolor="#f7f9fc")
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ink="#142d4e";green="#256a51"
def text(x,y,t,size=17,color=ink,weight="normal"):
 ax.text(x,y,t,fontsize=size,color=color,fontweight=weight,va="center")
def panel(y0,y1):
 ax.add_patch(FancyBboxPatch((.035,y0),.93,y1-y0,
  boxstyle="round,pad=.012,rounding_size=.015",fc="white",ec="#cdd8e7",lw=1.3))
text(.055,.967,"A finite head over the full algebra",21,weight="bold")
panel(.657,.925)
text(.065,.895,"A   Actual nuclear factorization  (NP.D)",18,weight="bold")
text(.09,.846,r"$\alpha:S\to\ell^1(B),\quad\beta:\ell^1(B)\to S$",20)
text(.09,.795,r"$v=\beta\alpha,\qquad w=\alpha\beta$",21)
text(.09,.744,r"$\mathrm{Coker}(1-v)\simeq\mathrm{Coker}(1-w)$",20)
text(.09,.692,"Both quotients are algebraic.",17,color=green)
panel(.352,.612)
text(.065,.581,"B   A diagonal example  (NP.I)",18,weight="bold")
text(.09,.529,r"$v=\mathrm{diag}(1,\frac{1}{2},\frac{1}{4},\ldots)$",21)
text(.09,.477,r"$\|v_{>2}\|=\frac{1}{4},\quad\sum_{j>2}|\lambda_j|=\frac{1}{2}$",21)
text(.09,.424,r"$\mathrm{Coker}(1-v)\simeq B$",21)
text(.09,.377,"The first coordinate is the quotient map.",17,color=green)
panel(.035,.308)
text(.065,.277,"C   Both analytic directions  (NP.H–NP.I)",18,weight="bold")
text(.09,.228,r"$R=(2,3),\quad r=(1,1)$",21)
text(.09,.179,r"$\sum_\alpha(r/R)^\alpha=3$",21)
text(.09,.130,r"$\sum_{0\leq\alpha_1,\alpha_2\leq2}(r/R)^\alpha=\frac{91}{36}$",20)
text(.09,.080,r"$T_2=\frac{17}{36}<1$",21,color=green)
fig.savefig(r/"nuclear-perturbation.png",dpi=150)
fig.savefig(r/"nuclear-perturbation.svg",metadata={"Date":None})
plt.close(fig)
head=sum(Fraction(1,2)**a*Fraction(1,3)**b for a in range(3)for b in range(3))
assert head==Fraction(91,36)and 3-head==Fraction(17,36)
data={
 "kind":"Algebraic diagrams; no geometric scale.",
 "panel_A":{"alpha":"x -> (lambda_j xi_j(x))","beta":"(b_j) -> sum b_j y_j",
  "v":"beta alpha","w":"alpha beta","cokernels":"Algebraic inverse maps induced by alpha,beta",
  "proof":"NP.12--NP.15"},
 "panel_B":{"lambda_j":"2^(1-j),j>=1","tail_after_two_operator_norm":"1/4",
  "tail_after_two_coefficient_weight":"1/2","cokernel":"B via first coordinate",
  "proof":"NP.32--NP.33"},
 "panel_C":{"R":[2,3],"r":[1,1],"total_weight":"3","box_bound":2,
  "box_weight":str(head),"tail_weight":str(3-head),"proof":"NP.28--NP.31 and NP.34"},
 "no_closed_range_or_Hausdorff_quotient_inferred_from_finiteness":True}
(r/"nuclear-perturbation-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
