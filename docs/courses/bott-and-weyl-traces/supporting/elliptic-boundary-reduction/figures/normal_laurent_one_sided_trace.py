from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out=Path(__file__).resolve().parent
out.mkdir(parents=True,exist_ok=True)
fig,ax=plt.subplots(figsize=(15.8,8.9),dpi=155)
fig.patch.set_facecolor("#f8fafc")
ax.set_facecolor("#f8fafc")
ax.set_xlim(0,16)
ax.set_ylim(0,9)
ax.axis("off")

def box(x,y,w,h,title,lines,edge,face="#ffffff"):
    patch=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.14,rounding_size=0.15",
                         linewidth=2,edgecolor=edge,facecolor=face)
    ax.add_patch(patch)
    ax.text(x+0.18,y+h-0.28,title,fontsize=13.2,fontweight="bold",va="top",color="#0f172a")
    for j,t in enumerate(lines):
        ax.text(x+0.18,y+h-0.74-0.39*j,t,fontsize=10.9,va="top",color="#334155")

def arrow(x1,y1,x2,y2,color,label=None):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=17,
                                 linewidth=2.3,color=color))
    if label:
        ax.text((x1+x2)/2,(y1+y2)/2+0.17,label,fontsize=10.3,ha="center",color=color)

ax.text(0.55,8.6,"Actual finite mixed collar layer: source, tails, trace, measurement",
        fontsize=19.5,fontweight="bold",color="#0f172a")
ax.text(0.58,8.08,"Fixed collar; complete tangential operators; every original boundary order",
        fontsize=11.4,color="#475569")

box(0.6,5.3,4.2,2.12,"Full supported source",
    [r"$C_P U=\sum_{a,b,q} F_{ba}^{(q)}U_a\otimes D_r^b\delta_0$",
     r"$F_{ba}^{(q)}=i^{q-1}\mathrm{binom}(b+q,q)\partial_r^q A_{a+b+q+1}(0)$",
     r"$\mathrm{ord}\,F_{ba}^{(q)}\leq m-a-b-q-1$"],
    "#0891b2","#ecfeff")
box(5.83,5.3,4.2,2.12,"Actual finite inverse",
    [r"$Q_N=Q\sum_{j=0}^{N-1}(-\mathcal{R}_F)^j$",
     r"$q_N\sim\sum_{n\geq0}C_n(r)\kappa^{-m-n}$",
     r"same coefficients on both real tails"],
    "#2563eb","#eff6ff")
box(11.08,5.3,4.2,2.12,"One-sided Cauchy trace",
    [r"$\gamma_k r^+Q_N C_P=\sum_{a,b,q}G^{(N,q)}_{kba}U_a$",
     r"$G^{(N,q)}_{kba}\in\Psi_{\rm tan}^{\,k-a-q}$",
     r"upper analytic subtraction includes $\kappa^{-1}$"],
    "#7c3aed","#f5f3ff")
arrow(4.9,6.35,5.73,6.35,"#334155")
arrow(10.13,6.35,10.97,6.35,"#334155")

box(1.10,2.32,5.35,1.88,"Source freezing comparison",
    [r"$q=0$: the same $Q_N$ applied to $C_0U$",
     r"$q\geq1$: $\Delta^cU$; trace order $k-a-q$",
     r"the correction gains at least one tangential order"],
    "#0d9488","#f0fdfa")
box(8.92,2.32,5.35,1.88,"Original boundary measurement",
    [r"$B_j=\sum_{k<m} B_{jk}\gamma_k,\quad \mathrm{ord}\,B_{jk}\leq m_j-k$",
     r"$\mathrm{ord}\,(B_{jk}G^{(N,q)}_{kba})\leq m_j-a-q$",
     r"$\mathsf{M}_N-\mathsf{M}_N^{\rm src}:\mathcal{C}^s\to\mathcal{D}^{s+1}$"],
    "#b45309","#fffbeb")
arrow(13.2,5.15,11.6,4.33,"#b45309")
arrow(5.3,5.12,3.9,4.33,"#0d9488")

ax.plot([0.58,15.3],[1.72,1.72],color="#cbd5e1",linewidth=1.2)
ax.text(0.75,1.34,r"$P_cQ_N=I_F-(-\mathcal{R}_F)^N$",
        fontsize=14,color="#1d4ed8")
ax.text(8.35,1.34,r"$Q_NP_c=I_E-(-\mathcal{R}_E)^N$",
        fontsize=14,color="#7c3aed")
ax.text(0.75,0.76,"Two distinct error bundles remain; no idempotence or complementing condition is asserted.",
        fontsize=11.5,color="#475569")
ax.text(0.75,0.29,"Proof locators: AC1–AC9 and AT1–AT15.",
        fontsize=10.3,color="#64748b")
fig.savefig(out/"normal_laurent_one_sided_trace.png",bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(out/"normal_laurent_one_sided_trace.svg",bbox_inches="tight",facecolor=fig.get_facecolor())
plt.close(fig)
print(str(out/"normal_laurent_one_sided_trace.png"))




