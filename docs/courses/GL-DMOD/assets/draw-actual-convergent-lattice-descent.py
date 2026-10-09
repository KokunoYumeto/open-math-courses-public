"""Original CC0 figure for the full supplied-lattice proof in GL-DMOD-13."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
OUT=ROOT
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans","svg.fonttype":"path"})
fig,ax=plt.subplots(figsize=(16,11.5),dpi=150)
fig.patch.set_facecolor("#f8fafc")
ax.set(xlim=(0,16),ylim=(0,11.5))
ax.axis("off")
def box(x,y,w,h,title,lines,color="#e8f0fa"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.10,rounding_size=0.12",
                linewidth=1.5,edgecolor="#264663",facecolor=color))
    ax.text(x+0.20,y+h-0.32,title,fontsize=15,weight="bold",va="top",color="#16334e")
    for k,line in enumerate(lines):
        ax.text(x+0.20,y+h-0.89-k*0.40,line,fontsize=14,va="top",color="#172b40")
def arrow(start,end,label=None):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=19,
                linewidth=1.5,color="#28587a",connectionstyle="arc3"))
    if label:
        ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+0.05,label,
                fontsize=11,ha="center",va="bottom",color="#28587a")
ax.text(0.25,11.18,"Actual descent from a supplied Euler-stable lattice",fontsize=23,
        weight="bold",color="#16334e",va="top")
ax.text(0.25,10.63,r"$M$ coherent over $\mathcal{D}_X$; $L\subset\Phi(M)$ coherent, generating; $tL\subset hL$",
        fontsize=17,color="#16334e",va="top")
ax.text(0.25,10.28,r"$J$ is an actual submodule of a finite free module; $N\subset T$ are finite actual modules; the Artin–Rees formula has $r\geq c$.",
        fontsize=12,color="#4d6071",va="bottom")
box(0.25,7.90,7.15,2.23,"1  Actual coefficients and division  ·  §§5.19–5.21",[
    r"One common domain: $|p_n|\leq AC^n n!$.",
    r"$\|P\circ Q\|\leq\|P\|\|Q\|$; finite heads, $\|DE\|<1/2$.",
    r"For $F\in J$: $F=\sum_i Q_i\circ P_i+S$; $S=0$."
])
box(8.35,7.90,7.15,2.23,"2  Exact completion and nearby kernels  ·  §§5.22,5.24",[
    r"Normal $h$: $N\cap h^rT=h^{r-c}(N\cap h^cT)$.",
    r"$\widehat T^{\,I}=\widehat{A}\otimes_{A_{\rm gv}}T$: exact, faithful at $j_0$.",
    "Fixed lifted relations generate on one neighbourhood."
])
arrow((7.55,9.00),(8.20,9.00))
box(0.25,4.67,7.15,2.50,"3  General actual ambient and both bounds  ·  §5.25",[
    r"$Q=\bigoplus_a h^aF_aM$,  $V=A_{\rm gv}\otimes_AQ\subset\Phi(M)$.",
    r"$h^CV\subset L\subset h^{-B}V$ on one neighbourhood.",
    r"$h^C\widehat{Q}\subset\Lambda\subset h^{-B}\widehat{Q}$;",
    r"$\Lambda[h^{-1}]=\widehat{Q}[h^{-1}]\subset M((h))$."
],"#e5f3ef")
box(8.35,4.67,7.15,2.50,"4  Euler projection and homogeneous generators  ·  §5.23",[
    r"$(tD_t+1)h^am=a\,h^am$ for every integer $a$.",
    r"$P_{r,j}(j)=1$, $P_{r,j}(k)=0$ for $0\leq k\leq r$, $k\ne j$.",
    r"$P_{r,j}(\delta)q\longrightarrow q_j$ formally; closedness.",
    r"$\Lambda=\sum_i\widehat{R}\,h^{a_i}m_i$ (finite list)."
],"#e5f3ef")
arrow((4.10,7.73),(4.10,7.31))
arrow((11.90,7.73),(11.90,7.31))
arrow((7.55,5.96),(8.20,5.96))
box(0.25,1.40,15.25,2.59,"5  Faithful recovery is actual sheaf equality  ·  §5.26",[
    r"$L'=\sum_i A_{\rm gv}h^{a_i}(u_0\otimes m_i)$; $\widehat{L}=\widehat{L'}$ inside one completed ambient.",
    r"Both completions $\widehat{(L+L')/L}$ and $\widehat{(L+L')/L'}$ vanish.",
    r"Faithfulness, finite generators, one neighbourhood: $L=L'$ as actual coherent sheaves.",
    r"$B_kM=j_0^{-1}h^{-k}L\cap M=\sum_i\mathcal{D}_{\leq k-a_i}m_i$ for every $k$; coherent, locally good."
],"#e9effa")
arrow((4.10,4.49),(4.10,4.13))
arrow((11.90,4.49),(11.90,4.13))
ax.text(0.35,1.04,"Separate open construction: the intrinsic strict cutoff across all singular characteristic strata.",
        fontsize=15,weight="bold",color="#7b4027",va="top")
ax.text(0.35,0.58,"No initial global generator, half-order theorem, or full analytic proper regularity is inferred.",
        fontsize=13.5,color="#7b4027",va="top")
ax.text(0.35,0.17,"Full proofs: GL-DMOD-13 §§5.19–5.26. Human context: Schapira (1981), §2; Kashiwara–Kawai, HolIII, Appendix A.8. Original CC0.",
        fontsize=10.5,color="#4d6071",va="top")
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
for ext in ("png","svg"):
    fig.savefig(OUT/f"actual-convergent-lattice-descent.{ext}",dpi=150)
plt.close(fig)
print(OUT/"actual-convergent-lattice-descent.png")
