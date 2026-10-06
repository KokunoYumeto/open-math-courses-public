from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15.5,8.0),dpi=150)
fig.patch.set_facecolor("#f8fafc")
ax.set_xlim(0,16);ax.set_ylim(0,8);ax.axis("off")
def box(x,y,w,h,title,body,edge,face):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.13,rounding_size=0.14",
                                edgecolor=edge,facecolor=face,linewidth=2))
    ax.text(x+0.19,y+h-0.25,title,fontsize=13,fontweight="bold",va="top",color="#0f172a")
    for j,t in enumerate(body):
        ax.text(x+0.19,y+h-0.70-j*0.40,t,fontsize=10.8,va="top",color="#334155")
def arr(x1,y1,x2,y2,color):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=18,
                                 color=color,linewidth=2.2))
ax.text(.6,7.60,"Differential layer: full source and interior coefficient freezing",fontsize=19.0,fontweight="bold",color="#0f172a")
ax.text(.62,7.12,"The two changes have different formulas; both contribute at one lower measured order",fontsize=11.5,color="#475569")
box(.65,4.88,4.0,1.75,"Variable route",
    [r"$C_P=C_0+\Delta^c$",r"$r^+T C_P$",r"$B_jr^+T C_P$"],
    "#0284c7","#eff6ff")
box(11.32,4.88,4.0,1.75,"Frozen route",
    [r"$P_0=\sum_\ell A_\ell(0)D_r^\ell$",r"$r^+T_0 C_0$",r"$B_jr^+T_0 C_0$"],
    "#7c3aed","#f5f3ff")
box(5.98,4.88,4.0,1.75,"Measured difference",
    [r"$B_jr^+(T C_P-T_0 C_0)$",
     r"$\in\Psi_{\rm tan}^{m_j-a-1}$ on input $U_a$",
     r"$\mathcal{C}^s\longrightarrow\mathcal{D}^{s+1}$"],
    "#0f766e","#f0fdfa")
arr(4.75,5.77,5.87,5.77,"#334155")
arr(11.20,5.77,10.11,5.77,"#334155")
box(.88,2.36,6.2,1.72,"Source term — IF3, IF6",
    [r"$T\Delta^c$: each $q\geq1$ contributes order $m_j-a-q$",
     r"$F_{ba}^{(q)}=i^{q-1}\mathrm{binom}(b+q,q)\,\partial_r^qA_{a+b+q+1}(0)$",
     "The original supported source is retained."],
    "#0891b2","#ecfeff")
box(8.74,2.36,6.2,1.72,"Interior term — IF4, IF8",
    [r"$t(0)-t_0(0)\in S^{-m-1}_{\rm cl}$",
     r"$D_r^u(t-t_0)|_0\in S^{-m}_{\rm cl}\ (u\geq1)$",
     r"$\gamma_k r^+(T-T_0)C_0:\ U_a\mapsto\Psi_{\rm tan}^{k-a-1}$"],
    "#a855f7","#faf5ff")
arr(3.89,4.77,3.89,4.18,"#0891b2")
arr(11.84,4.77,11.84,4.18,"#a855f7")
ax.plot([.7,15.2],[1.80,1.80],color="#cbd5e1",lw=1.2)
ax.text(.82,1.43,r"$T_0(P_0-P)TC_P$",fontsize=13.0,color="#92400e")
ax.text(4.58,1.43,r"$-R_{E,0}TC_P$",fontsize=13.0,color="#64748b")
ax.text(7.95,1.43,r"$+T_0R_FC_P$",fontsize=13.0,color="#64748b")
ax.text(11.32,1.43,r"$+T_0\Delta^c$",fontsize=13.0,color="#0e7490")
ax.text(.82,.94,"Exact BM21/IF13 comparison: the middle two kernels are smooth; the first retains every coefficient of $P_0-P$.",
        fontsize=11.3,color="#334155")
ax.text(.82,.44,"Proof: IF1–IF16, using CD10–CD11 and T16. Scalar nonzero check: TP19–TP22.",
        fontsize=10.2,color="#64748b")
fig.savefig(out/"differential_interior_freezing.png",bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(out/"differential_interior_freezing.svg",bbox_inches="tight",facecolor=fig.get_facecolor())
plt.close(fig)
print(out/"differential_interior_freezing.png")

