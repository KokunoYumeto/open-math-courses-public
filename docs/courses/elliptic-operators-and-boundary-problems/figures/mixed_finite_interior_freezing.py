from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15.0,7.7),dpi=150)
fig.patch.set_facecolor("#f8fafc")
ax.set_xlim(0,15.5);ax.set_ylim(0,7.7);ax.axis("off")
def box(x,y,w,h,title,lines,color,face):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.12,rounding_size=.13",linewidth=2,edgecolor=color,facecolor=face))
    ax.text(x+.17,y+h-.25,title,fontsize=13,fontweight="bold",va="top",color="#0f172a")
    for j,line in enumerate(lines):ax.text(x+.17,y+h-.72-.40*j,line,fontsize=11,va="top",color="#334155")
def arr(a,b,c,d,color):
    ax.add_patch(FancyArrowPatch((a,b),(c,d),arrowstyle="-|>",mutation_scale=18,linewidth=2.3,color=color))
ax.text(.52,7.31,"Matched finite mixed inverses: boundary row and both error sides",fontsize=19,fontweight="bold",color="#0f172a")
ax.text(.54,6.85,"Original fixed collar, complete tangential operators, real normal tails",fontsize=11.5,color="#475569")
box(.60,4.54,4.18,1.77,"Variable finite route",
    [r"Original $A_\ell(h(r))D_r^\ell$, $0\leq\ell\leq m$",
     r"$C_P=C_0+\Delta^c,\quad Q_N:F\to E$",
     r"$\mathcal{R}_E:E\to E,\quad\mathcal{R}_F:F\to F$"],
    "#2563eb","#eff6ff")
box(10.72,4.54,4.18,1.77,"Frozen finite route",
    [r"Frozen $A_\ell(0)D_r^\ell$, $0\leq\ell\leq m$",
     r"$C_0,\quad\widetilde Q_N:F\to E$",
     r"$\widetilde{\mathcal{R}}_E:E\to E,\quad\widetilde{\mathcal{R}}_F:F\to F$"],
    "#7c3aed","#f5f3ff")
box(5.75,4.54,3.95,1.77,"Matched boundary row",
    [r"$Q(y,0;z,s)=\widetilde Q(y,0;z,s)$",
     r"both corrections lie in $\mathcal{L}^{-m-1}$",
     r"$\gamma_k$ difference: order $k-a-1$"],
    "#0f766e","#f0fdfa")
arr(4.9,5.45,5.64,5.45,"#334155");arr(10.61,5.45,9.81,5.45,"#334155")
box(.72,2.13,6.37,1.67,"Full source and measured gain",
    [r"$\Delta^c$: each $q\geq1$ contributes order $m_j-a-q$",
     r"$B_jr^+(Q_NC_P-\widetilde Q_NC_0):\mathcal{C}^s\to\mathcal{D}^{s+1}$",
     r"every original $m_j$; no principal-coefficient replacement"],
    "#0891b2","#ecfeff")
box(8.32,2.13,6.37,1.67,"Exact finite resolvent identity",
    [r"$\widetilde Q_N(P_{c,0}-P_c)Q_NC_P$",
     r"$-\mathcal{E}_{0,N}Q_NC_P+\widetilde Q_N\mathcal{F}_NC_P+\widetilde Q_N\Delta^c$",
     r"$\mathcal{E}_{0,N}\in\mathcal{L}^{-N}(E),\ \mathcal{F}_N\in\mathcal{L}^{-N}(F)$"],
    "#b45309","#fffbeb")
arr(7.75,4.42,4.1,3.94,"#0891b2");arr(7.95,4.42,11.5,3.94,"#b45309")
ax.plot([.54,14.91],[1.58,1.58],color="#cbd5e1",lw=1.2)
ax.text(.7,1.23,r"$P_cQ_N=I_F-(-\mathcal{R}_F)^N,\quad Q_NP_c=I_E-(-\mathcal{R}_E)^N$",
        fontsize=13,color="#2563eb")
ax.text(.7,.80,r"$P_{c,0}\widetilde Q_N=I_F-(-\widetilde{\mathcal{R}}_F)^N,\quad \widetilde Q_NP_{c,0}=I_E-(-\widetilde{\mathcal{R}}_E)^N$",
        fontsize=13,color="#7c3aed")
ax.text(.7,.30,"Proof: IF15–IF21, AC1–AC9 and AT1–AT15. No finite error is called smooth.",fontsize=10.8,color="#64748b")
fig.savefig(out/"mixed_finite_interior_freezing.png",bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(out/"mixed_finite_interior_freezing.svg",bbox_inches="tight",facecolor=fig.get_facecolor())
plt.close(fig)
print(out/"mixed_finite_interior_freezing.png")


