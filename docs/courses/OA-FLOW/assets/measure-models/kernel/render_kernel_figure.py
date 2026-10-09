# Original mathematical diagram, reproduction code and exact data: CC0-1.0.
# DejaVu font terms retained in FONT-LICENSE.txt.
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-measure-models-kernel-20261009-v1"
from matplotlib.patches import FancyBboxPatch

D = Path(__file__).resolve().parent
lam = [F(1,8), F(3,8), F(1,3), F(1,6)]
mu0 = [F(3,8), F(1,8), F(3,8), F(1,8)]
r = [a/b for a,b in zip(lam,mu0)]
smear = [F(3,4)*lam[i]+F(1,4)*lam[i^1] for i in range(4)]
eta = [F(3,4), F(1,4), F(3,4), F(1,4)]
cond = [a*b for a,b in zip(r,eta)]
assert sum(lam) == sum(mu0) == sum(smear) == 1
assert sum(cond[:2]) == sum(cond[2:]) == 1
assert [F(1,2)*a for a in cond] == lam
data = dict(group="Z/2Z, swap each pair", points=["a0","a1","b0","b1"],
    w={"e":"3/4","t":"1/4"}, base={"A":"1/2","B":"1/2"},
    original=[str(a) for a in lam], smear=[str(a) for a in smear],
    reference_mixture=[str(a) for a in mu0], density=[str(a) for a in r],
    reference_fibers=[str(a) for a in eta], conditional_fibers=[str(a) for a in cond],
    proof="OA-FLOW-L69.md#oa-flow.orbits.reference through #oa-flow.orbits.conditional, (K7)-(K16)",
    terms="CC0-1.0 original diagram, code and data; Matplotlib font terms retained")
(D/"kernel-figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")

fig=plt.figure(figsize=(15,9),dpi=180,facecolor="#f7f9fc")
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,15); ax.set_ylim(0,9); ax.axis("off")
ink="#18243b"; blue="#23649a"; teal="#087d79"; muted="#56677d"
ax.text(.6,8.45,"Recover the orbit probabilities from one scalar density",
        fontsize=22,weight="bold",color=ink)
ax.text(.6,7.95,"General mechanism: a Borel orbit quotient and section are already constructed.",
        fontsize=13,color=muted)

def box(x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.08,rounding_size=0.12",
        facecolor="white",edgecolor=color,linewidth=1.8))
    ax.text(x+w/2,y+h-.35,title,ha="center",va="center",fontsize=15,weight="bold",color=color)
    ax.text(x+w/2,y+.42,body,ha="center",va="center",fontsize=12,color=ink,linespacing=1.5)
def arrow(x1,y1,x2,y2,label,dy=.16):
    ax.annotate("",(x2,y2),(x1,y1),arrowprops=dict(arrowstyle="->",lw=1.9,color=muted))
    ax.text((x1+x2)/2,(y1+y2)/2+dy,label,ha="center",fontsize=11,color=muted)

box(.7,6.2,3.0,1.2,r"Original probability $\lambda$",r"$q_*\lambda=\nu$",blue)
box(5.8,6.2,3.1,1.2,r"Orbit reference $\eta_y$","push forward "+r"$w(g)\,dg$"+"\n"+r"by $g\mapsto gs(y)$",teal)
box(10.95,6.2,3.3,1.2,r"Mixture $\mu_0$",r"$\mu_0=\int\eta_y\,d\nu(y)$",teal)
arrow(3.8,6.8,5.7,6.8,"same base")
arrow(9.0,6.8,10.85,6.8,"integrate")
ax.text(.9,5.62,r"Haar smearing:  $\bar\lambda=\int w(g)\,g_*\lambda\,dg\sim\lambda$",
        fontsize=14,color=blue)
ax.text(.9,5.13,r"Pointwise kernel classes give  $\bar\lambda\sim\mu_0$;  hence  $r=d\lambda/d\mu_0>0$.",
        fontsize=14,color=ink)
ax.text(.9,4.62,r"Recover  $\lambda_y=r\,\eta_y$:  $\int r\,d\eta_y=1$ a.e. because both base measures are $\nu$.",
        fontsize=14,color=teal)

ax.plot([.6,14.4],[4.15,4.15],color="#c9d3de",lw=1)
ax.text(.7,3.72,"Exact finite example",fontsize=17,weight="bold",color=ink)
ax.text(.7,3.31,r"$G=\mathbb{Z}/2\mathbb{Z}$ swaps $a_0,a_1$ and $b_0,b_1$;  $s(A)=a_0$, $s(B)=b_0$.",
        fontsize=13,color=ink)
ax.text(.7,2.97,r"Counting Haar measure: $w(e)=3/4$, $w(t)=1/4$, and $\nu(A)=\nu(B)=1/2$.",
        fontsize=13,color=muted)
cols=[r"$a_0$",r"$a_1$",r"$b_0$",r"$b_1$"]
rows=[r"$\lambda$",r"$\bar\lambda$",r"$\mu_0$",r"$r$",r"$\lambda_y$"]
vals=[[str(x) for x in xs] for xs in [lam,smear,mu0,r,cond]]
tbl=ax.table(cellText=[[label]+values for label,values in zip(rows,vals)],
             colLabels=[""]+cols,cellLoc="center",colWidths=[.12,.22,.22,.22,.22],
             bbox=[.07,.075,.80,.22])
tbl.auto_set_font_size(False); tbl.set_fontsize(13)
for (i,j),cell in tbl.get_celld().items():
    cell.set_edgecolor("#cad5df"); cell.set_linewidth(.7)
    cell.set_facecolor("#e7f0f7" if i==0 else ("#e9f6f3" if i==5 else "white"))
    cell.set_text_props(color=ink)
ax.text(.7,.27,"Each last-row pair sums to 1; multiplying it by the base mass 1/2 recovers the first row.",
        fontsize=11,color=muted)
fig.savefig(D/"haar-kernel-construction.png",dpi=180)
fig.savefig(D/"haar-kernel-construction.svg", metadata={'Date': None})
plt.close(fig)
print("Figure and exact rational data written.")
