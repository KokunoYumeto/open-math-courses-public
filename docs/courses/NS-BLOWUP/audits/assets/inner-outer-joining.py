"""Exact joining mechanism, schematic positions; no sampled mathematical data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(18,8))
fig.patch.set_facecolor("#fafbf9")
ax.set(xlim=(0,18),ylim=(0,8))
ax.axis("off")
ax.text(.3,7.65,"The five-moment join preserves the complete outer field",fontsize=23,weight="bold",color="#16362f")
ax.text(.3,7.25,"Original Appendix B · Q0–Q9     Schematic positions; endpoint formulas retain the exact radii.",fontsize=12,color="#4a6259")

def box(x,y,w,h,title,lines,color="#e8f0eb"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.10",facecolor=color,edgecolor="#90a89c",linewidth=1))
    ax.text(x+.13,y+h-.30,title,fontsize=13,weight="bold",va="top",color="#16362f")
    ax.text(x+.13,y+h-.77,"\n".join(lines),fontsize=12,va="top",linespacing=1.65,color="#223d34")
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=13,linewidth=1.4,color="#577e6d"))

xs=[.3,3.25,6.2,9.15,12.1,15.05]
titles=["Analytic axis","Activate stress","Set angular shape","Restore axial field","Five fixed bumps","Exact outer match"]
texts=[
 [r"$X\leq X_0=4/\Lambda$",r"$\mathcal{T}_0=0$",r"$\Pi(0,\eta)=\Pi_0(\eta)$","J0–J7; Q0"],
 [r"$y=\log(X/X_0)$",r"$\mathcal{T}_0=e_a B_0$",r"$B_0(0)=F(X_0)p_{s,r}(X_0)$","First collar admissible","Q2–Q5"],
 [r"$X_i=110$",r"$X_{\rm sep}=X_i e^{T_{\rm sh}}$",r"$E=P_*f(X/X_R)^{1/10}$","Length fixed before C","Q5–Q6"],
 [r"$-8<\log x<-7$",r"$U:G_i\ \longrightarrow\ 4\eta$",r"$x=X/X_R$","E stays ideal","Q7"],
 [r"$-6<\log x<-5$","2 axial + 3 angular","Full quadratic equations","All five moments restored","Q8"],
 [r"$\log x=-5$",r"Same $U,E,\Pi_0,M,I,J,S,C_p$",r"Same $\Pi,V_0,Q_s,N_s$",r"Same $p_s,a,b_s,\mathcal{T}_0$","Q8.10; G3"]
]
for i,x in enumerate(xs):
    box(x,4.2,2.65,2.65,titles[i],texts[i])
    if i<5:arrow(x+2.67,5.55,x+.29+2.65,5.55)

box(.3,1.65,8.35,2.15,"Every original moment keeps its radial factor",[
 r"$M=X_R\widehat M,\quad I=X_R^{3/2}\widehat I,\quad J=X_R^{3/2}\widehat J$",
 r"$S=X_R\widehat S,\quad C_p=\widehat C_p,\quad \Pi=\Pi_0+C_p$",
 r"$X_R=X_i(\mathsf{C} P_*)^{10},\quad x_{\rm sep}=e^{T_{\rm sh}}/(\mathsf{C} P_*)^{10}$"
])
box(9.05,1.65,8.65,2.15,"The matching tolerance is fixed before the large radius",[
 r"$Q_s\geq Q_{\min}/2,\quad E\geq e_*/2,\quad |a-.8|\leq .1$",
 r"$|N_s/(EQ_s)|\leq w_*,\quad |b_s|\leq .1/(1+w_*)$",
 r"$v_s<1,\quad P_c=(X_Rx/L)G,\quad G\geq 3Q_{\min}/7$"
],color="#e9eef5")
ax.text(.3,1.02,r"Order: outer data → tolerance, $j_0$ → $\delta_*,\sigma_*,\Lambda$ → $\mathcal{B}_k,T_{\rm sh}$ → $\mathsf{C},X_R$ → final small widths",fontsize=14,color="#16362f")
ax.text(.3,.57,"The join gives the strict relaxed cone. The separate V0–V7 audit derives the admissible shear of Appendix C.",fontsize=12,color="#5d4630")
ax.text(.3,.18,"Source: OpenAI, Finite Time Blowup for Navier–Stokes, original pages 150–157, (B.22)–(B.40). Proof: inner-outer-joining-audit.md.",fontsize=10,color="#526058")
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig(root/"inner-outer-joining.png",dpi=120,facecolor=fig.get_facecolor())
fig.savefig(root/"inner-outer-joining.svg",facecolor=fig.get_facecolor())
