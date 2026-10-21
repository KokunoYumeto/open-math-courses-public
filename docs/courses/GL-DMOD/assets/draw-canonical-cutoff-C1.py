"""Reproduce the spectral, function and singular-extension diagrams."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":17,
 "svg.hashsalt":"canonical-cutoff-C1-20261020","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(8,11.2),dpi=150,facecolor="#f7f9fc")
a=fig.add_axes([0,0,1,1]);a.set(xlim=(0,1),ylim=(0,1));a.axis("off")
ink="#142d4e";green="#256a51";blue="#195c96"
def text(x,y,t,size=17,color=ink,weight="normal"):
 a.text(x,y,t,fontsize=size,color=color,fontweight=weight,va="center")
def panel(y0,y1):
 a.add_patch(FancyBboxPatch((.035,y0),.93,y1-y0,
  boxstyle="round,pad=.012,rounding_size=.015",fc="white",ec="#cdd8e7",lw=1.3))
text(.055,.967,"Coherent cutoffs across all strata",21,weight="bold")
panel(.672,.925)
text(.065,.894,"A   Lower roots into one top strip",19,weight="bold")
text(.09,.847,r"$c=-\frac{1}{2},\quad c-1<\beta\leq c$",20)
text(.09,.793,r"$-\frac{1}{5}\ \longmapsto\ -\frac{6}{5}$",22)
text(.09,.739,r"$\frac{7}{10}\ \longmapsto\ -\frac{3}{10}\ \longmapsto\ -\frac{13}{10}$",22)
text(.09,.693,"Nilpotent multiplicities are retained.",17,color=green)
panel(.363,.628)
text(.065,.596,"B   The exact half-order boundary",19,weight="bold")
text(.09,.548,r"$\Theta=-tD_t-\frac{1}{2}$",21)
text(.09,.495,r"$t^{2/5}(\log t)^2:\quad\beta=-\frac{9}{10}$",21)
text(.09,.443,r"$\mathrm{Re}\,\beta\leq-\frac{1}{2}$",21,color=green)
text(.09,.396,"is the strict Nilsson source cutoff.",17)
panel(.035,.319)
text(.065,.287,"C   One adjacent quotient suffices",19,weight="bold")
text(.09,.239,r"$Q=h^{-1}L'/L',\qquad hQ=0$",21)
text(.09,.190,r"$\mathcal{H}^0_W(Q)=0$",21)
text(.09,.142,r"$\Longrightarrow\ \mathcal{H}^0_W(M/L')=0$",21)
text(.09,.090,r"$L'=M_c,\qquad E_\Lambda M_c=M_c$",21,color=green)
fig.savefig(r/"canonical-cutoff-C1.png",dpi=150)
fig.savefig(r/"canonical-cutoff-C1.svg",metadata={"Date":None})
plt.close(fig)
c=Fraction(-1,2);roots=[Fraction(-1,5),Fraction(7,10)]
tops=[Fraction(-6,5),Fraction(-13,10)]
assert all(c-1<b<=c and (x-b).denominator==1 for x,b in zip(roots,tops))
data={"kind":"Exact algebraic diagrams; no geometric scale.",
 "panel_A":{"threshold":str(c),"input_roots":[str(x)for x in roots],
 "top_roots":[str(x)for x in tops],"strip":"c-1<Re(beta)<=c",
 "proof":"CK.B, finite spectral lowering and saturation"},
 "panel_B":{"input":"t^(2/5)*(log t)^2","order":"-9/10",
 "nilpotent_action":"Theta f=(-9/10)f-2*t^(2/5)*log t",
 "proof":"CK.C, exact faithful strict-Nilsson criterion"},
 "panel_C":{"Q":"h^(-1)L'/L'","hQ":0,"W":"Lambda intersect pi^(-1)(S_sing)",
 "conclusion":"L'=M_c, E_Lambda M_c=M_c",
 "proof":"CK.J--CK.K, all adjacent layers on one neighbourhood"}}
(r/"canonical-cutoff-C1-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
