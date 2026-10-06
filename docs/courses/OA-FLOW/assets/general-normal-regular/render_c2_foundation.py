"""Original NR4 and finite-imprimitivity illustration; deterministic output."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
 "svg.hashsalt":"OA-FLOW-C2-NR4-20261004","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(15,10),facecolor="#f5f7fb")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis("off")
ink="#172d46";blue="#245e91";green="#16756b"
ax.text(.6,9.48,"Normal representation independence needs a full support",fontsize=23,weight="bold",color=ink)
ax.text(.6,9.05,"Arbitrary locally compact G • arbitrary Hilbert spaces • predual-norm continuous action",fontsize=13,color=ink)
def box(x,y,w,h,title,body,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.15",facecolor="white",edgecolor=color,linewidth=1.6))
 ax.text(x+.16,y+h-.38,title,weight="bold",fontsize=16,color=color,va="top")
 ax.text(x+.16,y+h-.85,body,fontsize=14,color=ink,va="top",linespacing=1.5)
box(.7,6.63,4.1,1.9,"Faithful normal representation",r"$K\ \cong\ E H^{(I)}$"+"\nCyclic pieces represented\nby cone vectors",blue)
box(5.5,6.63,8.7,1.9,"Full central support in the constant commutant",r"$N=(M\otimes 1_I)^\prime,\quad E\in N,\quad \overline{N E H^{(I)}}=H^{(I)}$"+"\nFaithfulness forces the central support of E to be 1.",green)
ax.annotate("",xy=(5.24,7.58),xytext=(4.99,7.58),arrowprops={"arrowstyle":"->","color":ink,"lw":2})
box(.7,4.48,13.5,1.6,"Amplify the regular algebra, then compress",
 r"$T\mathcal{E}=0,\quad T(1\otimes N)=(1\otimes N)T\quad\Longrightarrow\quad T=0$"+
 "\nThe dense commutant orbit makes compression faithful; NR3–4 prove full normality.",blue)
ax.annotate("",xy=(9.8,6.2),xytext=(9.8,6.45),arrowprops={"arrowstyle":"->","color":green,"lw":2})
ax.text(.7,3.86,"A system intertwiner must also preserve the coset algebra",fontsize=21,weight="bold",color=ink)
ax.text(.7,3.43,r"Exact example:  $G=\mathbb{Z}/2,\ H=\{e\}$,  induced space $\mathbb{C}^2$.",fontsize=14,color=ink)
box(.7,1.27,6.35,1.76,"Group action alone",r"$S(x,y)=(y,x)$"+"\n"+r"$\{S\}^\prime=\{aI+bS\}$"+"   •   complex dimension 2",blue)
box(7.65,1.27,6.55,1.76,"Group action and coset multiplication",r"$P(x,y)=(x,0)$"+"\n"+r"$\{S,P\}^\prime=\{aI\}$"+"   •   complex dimension 1",green)
ax.text(.7,.62,"Proof: NR4 and FIGURE_CAPTION.md. The upper panel is a schematic; the lower panel is an exact calculation.",fontsize=11.5,color=ink)
fig.savefig(HERE/"c2-normal-independence.png",dpi=180,metadata={"Software":"matplotlib; original OA-FLOW proof diagram"})
fig.savefig(HERE/"c2-normal-independence.svg",metadata={"Date":None,"Creator":"Original OA-FLOW proof diagram"})
plt.close(fig)
p=HERE/"c2-normal-independence.svg";p.write_text(p.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
data={"scope":"NR4: arbitrary G and Hilbert spaces under NR0; no disintegration",
 "finite_example":{"group":"Z/2","subgroup":"identity","S":[[0,1],[1,0]],"P":[[1,0],[0,0]],
 "group_commutant_complex_dimension":2,"system_commutant_complex_dimension":1},
 "upper_panel":"schematic, not a finite-dimensional assertion",
 "proof_locators":["NORMAL_REGULAR_FOUNDATION_PACKET.md NR4","FIGURE_CAPTION.md"]}
(HERE/"c2-normal-independence.data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
