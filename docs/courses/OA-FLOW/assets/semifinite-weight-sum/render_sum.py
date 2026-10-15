"""A reflected pair of weight domains. Original exposition and drawing, CC0-1.0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

matplotlib.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
                           "svg.hashsalt":"oa-flow-nwr-weight-sum-20261015"})
OUT=Path(__file__).resolve().parent/"assets"
OUT.mkdir(exist_ok=True)
fig=plt.figure(figsize=(15,10),dpi=200,facecolor="#f5f7fa")
fig.text(.05,.955,"Two semifinite weights can have a nonsemifinite sum",
         fontsize=22,weight="bold",color="#17354c")
fig.text(.05,.917,"An exact reflection on "+r"$H=\ell^2(\mathbb{N}_{\geq1})$"+
         " determines the entire missing finite-domain direction.",
         fontsize=13,color="#465e70")

def panel(pos,title):
    ax=fig.add_axes(pos);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
    ax.add_patch(FancyBboxPatch((.005,.01),.99,.98,boxstyle="round,pad=0,rounding_size=.03",
                               fc="white",ec="#bdcbd7",lw=1))
    ax.text(.025,.88,title,size=15,weight="bold",color="#17354c")
    return ax

def box(ax,x,y,w,h,lines,color="#dcecf5",size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.012,rounding_size=.025",
                               fc=color,ec="#7895aa",lw=1))
    ax.text(x+w/2,y+h/2,lines,ha="center",va="center",fontsize=size,
            linespacing=1.55,color="#17354c")

def arrow(ax,start,end):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=17,
                                color="#4c758d",lw=1.5))

a=panel([.05,.63,.90,.24],"1  Dense individually; a proper closure in common  (NWR24, NWR28)")
box(a,.03,.23,.29,.43,r"$\mathcal{D}=\{\xi:\sum 4^n|\xi_n|^2<\infty\}$"+
    "\n"+r"$\overline{\mathcal{D}}=H$",size=14)
box(a,.68,.23,.29,.43,r"$U\mathcal{D}$"+"\n"+r"$\overline{U\mathcal{D}}=H$",size=14)
box(a,.37,.23,.26,.43,r"$U=1-2P_v$"+"\n"+r"$v_n=\sqrt{3}\,2^{-n}$",color="#e3e8f4",size=14)
arrow(a,(.33,.45),(.355,.45));arrow(a,(.645,.45),(.67,.45))
a.text(.03,.08,r"$v\notin\mathcal{D},\quad \|v\|=1,\quad "
       r"\mathcal{D}\cap U\mathcal{D}=\mathcal{D}\cap v^\perp,\quad "
       r"\overline{\mathcal{D}\cap U\mathcal{D}}=v^\perp$",size=14,color="#17354c")

b=panel([.05,.30,.90,.30],"2  The range test determines the finite corner  (NWR25–NWR31)")
box(b,.03,.39,.37,.35,r"$\varphi(a)=\sum 4^n\langle ae_n,e_n\rangle$"+
    "\n"+r"$\psi(a)=\varphi(UaU)$",size=14)
box(b,.57,.39,.40,.35,r"$(\varphi+\psi)(a)<\infty$"+
    "\n"+r"$\Longrightarrow\ a^{1/2}H\subset v^\perp$"+
    "\n"+r"$\Longrightarrow\ a=qaq,\quad q=1-P_v$",color="#f8e2cc",size=14)
arrow(b,(.415,.565),(.55,.565))
b.text(.035,.24,r"$\varphi,\psi$: faithful, normal, semifinite",size=14,color="#17354c")
b.text(.035,.10,r"$\omega=\varphi+\psi$: faithful and normal; support $p=1$, finite-domain projection $q<1$",
       size=14,color="#17354c")
b.text(.57,.24,r"Finite rank-one projections span $qH$.",size=13,color="#17354c")


c=panel([.05,.075,.90,.195],"3  The same obstruction for dual-invariant targets  (NWR32–NWR33)")
c.text(.03,.59,r"$B(H)\rtimes_{\mathrm{id}}\mathbb{Z}/2=B(H)\oplus B(H),"
       r"\qquad T(A,B)=\pi((A+B)/2)$",size=15,color="#17354c")
c.text(.03,.34,r"$D\varphi,\ D\psi$: faithful normal semifinite and invariant under interchange",
       size=14,color="#17354c")
c.text(.03,.10,r"$D\varphi+D\psi=D\omega$: finite-domain projection $(q,q)<(1,1)$",
       size=14,color="#17354c")
fig.text(.05,.035,"Algebraic schematic, not a finite-dimensional model of dense subspaces. "
         "All identities: NWR7, equations NWR24–NWR33.",size=11,color="#465e70")
fig.savefig(OUT/"semifinite-weight-sum.png",dpi=200,
            metadata={"Software":"OA-FLOW NWR weight-sum renderer"})
fig.savefig(OUT/"semifinite-weight-sum.svg",
            metadata={"Date":None,"Creator":"OA-FLOW NWR weight-sum renderer"})
plt.close(fig)
q=OUT/"semifinite-weight-sum.svg"
q.write_text("\n".join(line.rstrip() for line in q.read_text(encoding="utf-8").splitlines())+"\n",
             encoding="utf-8")
data={
 "hilbert_space":"ell2(N_ge_1)","coordinate_weights":"4^n",
 "unit_vector":"v_n=sqrt(3)*2^(-n)","normalization":"3*sum_{n>=1}4^(-n)=1",
 "reflection":"U=1-2*P_v","finite_vector_domain":"D={xi:sum 4^n |xi_n|^2<infinity}",
 "intersection":"D intersect U D = D intersect v_perp",
 "intersection_closure":"v_perp",
 "weights":{"phi":"sum 4^n <a e_n,e_n>","psi":"phi(U a U)","omega":"phi+psi"},
 "sum_support":"1","sum_finite_domain_projection":"1-P_v",
 "crossed_product":"B(H) direct_sum B(H), trivial Z/2 action",
 "original_Haar":"counting","dual_Haar_point_mass":"1/2",
 "dual_sum_finite_domain_projection":"(1-P_v,1-P_v)",
 "proof_locator":"OA-FLOW-NWR.md, NWR7, NWR24-NWR33",
 "schematic_not_finite_dimensional":True,"native_pixels":[3000,2000]
}
(OUT/"semifinite-weight-sum-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print("Rendered exact domain, corner and dual-weight diagram.")
