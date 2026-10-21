"""Reproduce the characteristic, Euler and finite-generator diagrams."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":17,
 "svg.hashsalt":"initial-analytic-generators-20261020","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(8,11.8),dpi=150,facecolor="#f7f9fc")
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ink="#142d4e";green="#256a51";blue="#195c96"
def text(x,y,t,size=17,color=ink,weight="normal"):
 ax.text(x,y,t,fontsize=size,color=color,fontweight=weight,va="center")
def panel(y0,y1):
 ax.add_patch(FancyBboxPatch((.035,y0),.93,y1-y0,
  boxstyle="round,pad=.012,rounding_size=.015",fc="white",ec="#cdd8e7",lw=1.3))
text(.055,.967,"Ordinary generators from a cutoff",21,weight="bold")
panel(.657,.925)
text(.065,.895,"A   Every lifted component  (GG.B–GG.C)",18,weight="bold")
text(.09,.850,r"$\Lambda'=\{t=0,\ (x,\xi)\in\mathrm{Char}\,M,\ \tau\ne0\}$",18)
text(.09,.797,r"$\xi\ne0:\quad A\ \longmapsto\ A'$",21)
text(.09,.745,r"$\xi=0:\quad \delta_t\otimes\mathcal{O}^{\,r}$",21)
text(.09,.692,"Both cases give generic regularity.",17,color=green)
panel(.352,.612)
text(.065,.581,"B   The actual normal identity  (GG.D)",18,weight="bold")
text(.09,.531,r"$D_t t=tD_t+1,\qquad D_t t\,L\subset L$",20)
text(.09,.477,r"$h=D_t^{-1},\qquad tL=hD_t t\,L\subset hL$",20)
text(.09,.423,r"$(tD_t+1)\,h^a\delta=a\,h^a\delta$",21)
text(.09,.376,"The Euler degree includes the +1.",17,color=green)
panel(.035,.308)
text(.065,.277,"C   One finite maximum  (GG.E–GG.F)",18,weight="bold")
text(.09,.229,r"$B_kM=\sum_\nu D_{\leq k-a_\nu}\,m_\nu$",21)
text(.09,.180,r"$q\geq\max_{\alpha,\nu}a_{\nu,\alpha}$",21)
text(.09,.131,r"$G=B_qM,\qquad DG=M$",21)
text(.09,.081,r"$B_{q+r}M=D_{\leq r}G\quad(r\geq0)$",21,color=green)
fig.savefig(r/"initial-analytic-generators.png",dpi=150)
fig.savefig(r/"initial-analytic-generators.svg",metadata={"Date":None})
plt.close(fig)
data={
 "kind":"Algebraic diagrams; no geometric scale.",
 "panel_A":{"lifted_support":"t=0, (x,xi) in Char M, tau!=0",
  "nonzero_source_covector":"Image of B_0 tensor A, characteristic-stable by GG.13--GG.14",
  "original_zero_section":"Normal delta tensor a horizontal frame, GG.15--GG.16",
  "proof":"GG.B--GG.C"},
 "panel_B":{"h":"D_t^(-1)","identity":"D_t*t=t*D_t+1",
  "inclusion":"tL=h*D_t*t*L subset hL",
  "Euler_action":"(tD_t+1)h^a delta=a*h^a delta","proof":"GG.D and GG.24"},
 "panel_C":{"finite_local_pieces":"B_k M=sum D_(<=k-a_nu) m_nu",
  "bound":"q>=max_(alpha,nu) a_(nu,alpha), finite cover of a compact set",
  "generator":"G=B_q M, D G=M",
  "all_nonnegative_pieces":"B_(q+r)M=D_(<=r)G","proof":"GG.E--GG.F"},
 "flat_example":{"threshold":"0","delta_order":str(Fraction(1,2)),
  "first_nonzero_piece":1,"proof":"GG.G"}}
(r/"initial-analytic-generators-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
