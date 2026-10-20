"""Reproduce the exact algebraic diagram of indicial order and finite poles."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
matplotlib.rcParams.update({
    "font.family":"DejaVu Sans","font.size":17,
    "svg.hashsalt":"indicial-order-zero-20261020",
    "mathtext.fontset":"dejavusans",
})
fig=plt.figure(figsize=(8,10.5),dpi=150,facecolor="#f7f9fc")
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ink="#142d4e";blue="#195c96";green="#256a51";red="#9b3e36"
def text(x,y,t,size=17,color=ink,weight="normal",ha="left"):
    ax.text(x,y,t,fontsize=size,color=color,fontweight=weight,ha=ha,va="center")
def panel(y0,y1):
    ax.add_patch(FancyBboxPatch((.035,y0),.93,y1-y0,
        boxstyle="round,pad=.012,rounding_size=.015",
        fc="white",ec="#cdd8e7",lw=1.3))
def arrow(x0,y0,x1,y1):
    ax.annotate("",xy=(x1,y1),xytext=(x0,y0),
        arrowprops={"arrowstyle":"->","color":blue,"lw":2})
text(.055,.967,"Indicial order and one finite target",21,weight="bold")
panel(.663,.925)
text(.065,.894,"A   The half-order sign",19,weight="bold")
text(.09,.844,r"$\Theta=-tD_t-\frac{1}{2}$",21)
text(.09,.791,r"$t^{-1}\quad\longmapsto\quad\log t$",22)
text(.09,.746,r"order $+\frac{1}{2}$                 order $-\frac{1}{2}$",18,color=green)
text(.09,.695,r"One primitive lowers order by 1.",17)
panel(.351,.625)
text(.065,.593,"B   Artin–Rees gives a finite filtration",18,weight="bold")
text(.09,.546,r"$L'\subset L,\qquad F^{N+1}=0$",21)
text(.09,.493,r"$\mathrm{gr}^{j}F$ is a subquotient of",18)
text(.09,.452,r"$h^jL/h^{j+1}L:\quad\beta\longmapsto\beta-j$",20)
text(.09,.402,"No root moves to the right.",18,color=green)
panel(.035,.311)
text(.065,.279,"C   One ordinary coefficient bound",19,weight="bold")
text(.09,.230,r"$\mathrm{Re}\,\beta<m,\qquad N=m+2$",20)
text(.09,.177,r"$e'(M_{0,p})\ \subset\ f^{-N}L_{\Sigma,0}/\mathcal{O}_0^q$",21)
text(.09,.122,"The target is finite over the local",17)
text(.09,.086,"holomorphic ring; so is its submodule.",17)
fig.savefig(root/"indicial-order-zero.png",dpi=150)
fig.savefig(root/"indicial-order-zero.svg",metadata={"Date":None})
plt.close(fig)
data={
 "kind":"Exact algebraic diagram; no spatial or numerical scale.",
 "panel_A":{"input":"t^(-1)","primitive_mod_holomorphic":"log(t)",
            "input_order":"1/2","primitive_order":"-1/2","generator":"-t*Dt-1/2"},
 "panel_B":{"filtration":"F^j=(L' intersect h^jL + hL')/hL'",
            "last":"F^(N+1)=0","residue_shift":"beta-j",
            "reference":"IO.18--IO.20"},
 "panel_C":{"premise":"Re beta < m, m a nonnegative integer",
            "pole_integer":"N=m+2","target":"f^(-N)L_Sigma/O^q",
            "reference":"IO.23--IO.30"},
 "proof_locators":["IO.17","IO.18--IO.21","IO.26--IO.30"],
}
assert Fraction(1,2)-1==Fraction(-1,2)
(root/"indicial-order-zero-exact-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
