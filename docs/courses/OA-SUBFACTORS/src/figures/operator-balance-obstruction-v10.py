"""Independent CC0 diagram and exact abelian support check; not a Jones realization."""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

here=Path(__file__).resolve().parent
# Four joint atoms ordered (s1,r1),(s1,r2),(s2,r1),(s2,r2).
# P0 averages the two atoms with the same larger label.
k=(F(3,2),F(1,2),F(1,2),F(3,2))
vlabel=(0,1,0,1)
slabel=(0,0,1,1)
mean=lambda values,label:[sum(values[i] for i in range(4) if label[i]==j)/2 for j in range(2)]
assert mean(k,vlabel)==[F(1),F(1)]
assert mean(k,slabel)==[F(1),F(1)]
q=mean(tuple((x-1)**2 for x in k),vlabel)
assert q==[F(1,4),F(1,4)]
diffnorm=max(sum(abs((k[i]-1)/2) for i in range(4) if vlabel[i]==j) for j in range(2))
assert diffnorm==F(1,2)
assert max(q)/max(abs(x-1) for x in k)==F(1,2)
# Conditional variance for the projection of the first smaller label.
t=(F(1),F(1),F(0),F(0))
pt=mean(t,vlabel)
variance=[mean(tuple(x*x for x in t),vlabel)[j]-pt[j]**2 for j in range(2)]
assert variance==[F(1,4),F(1,4)]
check={
 "scope":"Exact four-point abelian illustration; no actual core realization is asserted.",
 "primary_evidence":"Complete analytic proofs BC3.1–BC3.4 in the associated lesson",
 "normalizations":"Original uniform probability trace, all atoms have weight1/4.",
 "checks":{"both_kappa_marginals_one":True,"q_kappa":[str(x) for x in q],
           "P_kappa_minus_P0_norm":str(diffnorm),"exact_physical_fix_channel_delta_lower_bound":"1/4",
           "projection_conditional_variance":[str(x) for x in variance]},
 "license":"CC0-1.0"
}
(here/"operator-balance-obstruction-v10-checks.json").write_text(json.dumps(check,indent=2)+"\n",encoding="utf-8")

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                    "mathtext.fontset":"dejavusans","svg.fonttype":"path"})
fig=plt.figure(figsize=(15,10),facecolor="#f5f7fa")
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis("off")
blue="#244a72"; ink="#162b40"; orange="#9b4b1a"; green="#286555"
def panel(x,y,w,h,title,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.03,rounding_size=0.12",
              edgecolor=color,facecolor="white",linewidth=1.6))
 ax.text(x+.23,y+h-.3,title,color=color,weight="bold",va="top",fontsize=15)
def text(x,y,s,**kw):ax.text(x,y,s,color=kw.pop("color",ink),va="top",**kw)
def arrow(x1,y1,x2,y2,label=None):
 ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops={"arrowstyle":"->","color":blue,"lw":1.7})
 if label: ax.text((x1+x2)/2,(y1+y2)/2+.1,label,ha="center",color=blue,fontsize=11)

text(.4,9.73,"Joint state balance cannot be replaced by operator balance",fontsize=22,weight="bold")
text(.4,9.27,"Actual ordinary core • inherited trace • finite common basis • arbitrary target and singular states",fontsize=12)

panel(.4,5.54,9.25,3.28,"The actual finite-basis transfer",blue)
text(.68,8.15,r"$D_0=Z(S)\vee Z(R)$",fontsize=17)
text(6.75,8.15,r"$V=Z(R)$",fontsize=17)
arrow(3.35,7.99,6.42,7.99,r"$P_\kappa(t)=P_0(\kappa t)$")
text(.68,7.42,r"$\iota(t)\in B$",fontsize=16)
text(6.75,7.42,r"$d\,\iota(P_\kappa t)$",fontsize=16)
arrow(2.58,7.28,6.42,7.28,r"$\mathcal{I}(X)=\sum_i b_iXb_i^*$")
text(.68,6.77,r"$\sum_i b_ib_i^*=d1,\qquad P_0(\kappa)=1$",fontsize=17)
text(.68,6.22,r"$\Phi|_M=j,\quad \Phi\iota=\Phi\iota P_0"
     r"\quad\Longrightarrow\quad\Phi\iota(q_\kappa)=0$",fontsize=15,color=orange)
text(.68,5.83,r"$q_\kappa=P_0((\kappa-1)^2)\geq0$; faithful on the larger center forces $\kappa=1$.",fontsize=12)

panel(9.9,5.54,4.7,3.28,"Approximate channel: fixed tests",orange)
text(10.17,8.14,r"$b_i=\sum_\ell c_{i\ell}v_{i\ell}$",fontsize=16)
text(10.17,7.72,r"$A_i=\sum_\ell |c_{i\ell}|$",fontsize=15)
text(10.17,7.24,"Physical unitary error ≤ ε\nJoint-center operator error ≤ δ",fontsize=12)
text(10.17,6.65,r"$\|P_\kappa-P_0\|\leq2\delta$"
     "\n"+r"$+\frac{2}{d}\sum_i A_i^2(\sqrt{2\epsilon}+\epsilon)$",fontsize=15)
text(10.17,5.92,"No row length or postselected averaging cost.\nProof: BC3.9–BC3.14.",fontsize=11)

panel(.4,2.27,7.04,2.91,"Balanced cyclic GNS: the same expected pair",green)
text(.68,4.51,r"$A\subset_{E_A}B\quad\longrightarrow\quad"
     r"\pi(A)\subset_{\bar E_A}\pi(B)$",fontsize=15)
text(.68,3.98,r"$\psi_e(T)=\operatorname{Tr}(eT),\qquad c_B(e)=1$",fontsize=15)
text(.68,3.49,"π is normal and faithful. Hypertraces pull back bijectively.\nThe cyclic state is balanced; returned states need not\nshare its cyclic center marginal.",fontsize=12)
text(.68,2.73,"A separator on the balanced state set gains no\nstrict operator lower bound under this representation.",fontsize=11,color=green)

panel(7.69,2.27,6.91,2.91,"Quotient relations kill conditional variance",orange)
text(7.97,4.51,r"$q\iota(t)=q\iota(P_0t)\quad(t\in D_0)$",fontsize=15)
text(7.97,4.01,r"$v_t=P_0(t^2)-(P_0t)^2$",fontsize=15)
text(7.97,3.58,r"$q\iota(v_t)=0,\qquad"
     r"\psi_e(\iota(v_t))=\|t-P_0t\|_2^2>0$",fontsize=14)
text(7.97,2.99,"When P₀ differs from the identity, this quotient cannot\nrepresent the full balanced state set containing ψₑ.\nProof: BC3.16 and Proposition BC3.4.",fontsize=12)

panel(.4,.45,14.2,1.44,"Scope of the correction",blue)
text(.68,1.26,"These are exact failures of operator-balance and faithful-GNS shortcuts.\n"
     "They do not prove that an actual separator exists, and do not exclude a suitable joint-balanced hypertrace.\n"
     "The unrestricted simultaneous finite-row input and the original full partition remain unresolved in the general case.",fontsize=12)
fig.savefig(here/"operator-balance-obstruction-v10.png",dpi=170,facecolor=fig.get_facecolor())
fig.savefig(here/"operator-balance-obstruction-v10.svg",facecolor=fig.get_facecolor())
svg_path=here/"operator-balance-obstruction-v10.svg"
svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
print(json.dumps(check["checks"]))
