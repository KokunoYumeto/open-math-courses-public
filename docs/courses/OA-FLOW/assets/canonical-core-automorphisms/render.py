"""Reproduce the canonical matrix and moving-reflection implementation models.

Run python render.py with NumPy and Matplotlib. No network or external data.
Original diagram, renderer and exact data: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                     "mathtext.fontset":"dejavusans","svg.fonttype":"none","svg.hashsalt":"OA-FLOW-canonical-core-automorphisms-v1"})
INK="#213345";MUTED="#596c7c";BLUE="#176495";GREEN="#2c7c50";ORANGE="#b25725"
fig,axes=plt.subplots(2,2,figsize=(18,13))
fig.patch.set_facecolor("#fbfcfe")
fig.subplots_adjust(left=.035,right=.975,bottom=.075,top=.88,hspace=.19,wspace=.12)
fig.suptitle("Canonical implementation: exact phases and strong convergence",
             y=.968,fontsize=23,fontweight="bold",color=INK)
fig.text(.5,.925,"Weighted two-by-two matrices and moving reflections on the full Hilbert–Schmidt space",
         ha="center",fontsize=16,color=MUTED)

def panel(ax,title):
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.add_patch(Rectangle((0,0),1,1,fill=False,edgecolor="#cbd5df",lw=1.2))
    ax.text(.025,.953,title,va="top",fontsize=18,fontweight="bold",color=INK)

def txt(ax,x,y,value,**kw):
    ax.text(x,y,value,color=kw.pop("color",INK),**kw)

def arrow(ax,a,b,color=MUTED):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=16,color=color,lw=1.5))

def matrix(ax,left,bottom,entries,label):
    width=.115;height=.15
    for i in range(2):
        for j in range(2):
            val=entries[i][j]
            shade="#f2f6f9" if val==0 else ("#d9e9f2" if val==1 else "#6ca8ca")
            ax.add_patch(Rectangle((left+j*width,bottom+(1-i)*height),width,height,
                                   facecolor=shade,edgecolor="white",lw=1.5))
            txt(ax,left+(j+.5)*width,bottom+(1.5-i)*height,str(val),
                ha="center",va="center",fontsize=23)
    txt(ax,left+width,bottom+.355,label,ha="center",fontsize=18)

ax=axes[0,0]
panel(ax,"A  The transported density and its cocycle")
matrix(ax,.18,.40,[[1,0],[0,4]],r"$h$")
matrix(ax,.60,.40,[[4,0],[0,1]],r"$vhv^*$")
arrow(ax,(.43,.56),(.575,.56))
txt(ax,.5,.665,"flip",ha="center",fontsize=13,color=MUTED)
txt(ax,.5,.28,r"$c_t=(vhv^*)^{it}h^{-it}=\operatorname{diag}(4^{it},4^{-it})$",
    ha="center",fontsize=17)
txt(ax,.5,.16,r"$r_0=\pi/(2\log4),\qquad c_{r_0}=\operatorname{diag}(i,-i)$",
    ha="center",fontsize=17,color=BLUE)
txt(ax,.5,.055,r"$\varphi(x)=\operatorname{Tr}(hx),\quad\varphi(1)=5$; exact balanced normalization.",
    ha="center",fontsize=13,color=MUTED)

ax=axes[0,1]
panel(ax,"B  The field coordinate removes the r-phase")
txt(ax,.5,.81,r"$V(r)A=h^{-ir}vh^{ir}Av^*,\qquad (F\xi)(r)=h^{ir}\xi(r)$",
    ha="center",fontsize=16)
txt(ax,.22,.64,r"$E_{11}$",ha="center",fontsize=24,color=BLUE)
txt(ax,.76,.64,r"$-iE_{22}$",ha="center",fontsize=24,color=BLUE)
arrow(ax,(.32,.66),(.62,.66),BLUE)
txt(ax,.47,.71,r"$V(r_0)$",ha="center",fontsize=15,color=BLUE)
txt(ax,.22,.365,r"$E_{11}$",ha="center",fontsize=24,color=GREEN)
txt(ax,.76,.365,r"$E_{22}$",ha="center",fontsize=24,color=GREEN)
arrow(ax,(.32,.385),(.62,.385),GREEN)
txt(ax,.47,.435,r"$U_v(A)=vAv^*$",ha="center",fontsize=14,color=GREEN)
arrow(ax,(.22,.595),(.22,.43))
arrow(ax,(.76,.595),(.76,.43))
txt(ax,.085,.51,r"$F(r_0)$",fontsize=13)
txt(ax,.795,.51,r"$F(r_0)$",fontsize=13)
txt(ax,.5,.245,r"$F(r_0)A=\operatorname{diag}(1,i)A$",ha="center",fontsize=17)
txt(ax,.5,.145,r"$F\pi_\varphi(x)F^*=L_x,\qquad F\lambda(t)F^*=L_{h^{it}}T_t$",
    ha="center",fontsize=17)
txt(ax,.5,.055,r"$T_t\xi(r)=\xi(r-t)$; both unitary field maps act on all of $L^2(\mathbb{R},H)$.",
    ha="center",fontsize=12,color=MUTED)

ax=axes[1,0]
panel(ax,"C  An order-two test detects a wrong phase")
txt(ax,.5,.81,r"$\alpha^2=\mathrm{id},\qquad U_\alpha^2=I,\qquad V_\alpha^2=I$",
    ha="center",fontsize=18)
for y,labels,color,op in [(.63,[r"$E_{11}$",r"$E_{22}$",r"$E_{11}$"],GREEN,r"$U_\alpha$"),
                           (.37,[r"$E_{11}$",r"$iE_{22}$",r"$-E_{11}$"],ORANGE,r"$iU_\alpha$")]:
    for x,label in zip([.16,.50,.84],labels):txt(ax,x,y,label,ha="center",fontsize=22,color=color)
    arrow(ax,(.255,y+.02),(.405,y+.02),color);arrow(ax,(.605,y+.02),(.745,y+.02),color)
    txt(ax,.33,y+.085,op,ha="center",fontsize=13,color=color)
    txt(ax,.675,y+.085,op,ha="center",fontsize=13,color=color)
txt(ax,.5,.205,r"same conjugation, but $(iU_\alpha)^2=-I$ and $(iV_\alpha)^2=-I$",
    ha="center",fontsize=16,color=ORANGE)
txt(ax,.5,.115,r"$iU_\alpha(I_2)=iI_2\notin\mathcal{P}$",ha="center",fontsize=18)
txt(ax,.5,.035,"Replacing v by iv is different: its two conjugation phases cancel.",
    ha="center",fontsize=12,color=MUTED)

ax=axes[1,1]
panel(ax,"D  A fixed vector converges; the norm stays 2")
txt(ax,.5,.81,r"$v_n=I-2p_n,\quad U_nA=v_nAv_n,\quad c_t^{\alpha_n}=1$",
    ha="center",fontsize=17)
plot=ax.inset_axes([.12,.41,.80,.31])
ns=np.arange(1,9);errors=2*np.sqrt(3)*2.0**(-ns)
plot.plot(ns,np.full(8,2),color=ORANGE,lw=1.5,marker="s",markersize=5,
          label=r"$\|U_n-I\|=\|V_n-I\|=2$")
plot.plot(ns,errors,color=BLUE,lw=1.5,marker="o",markersize=5,
          label=r"$\|(U_n-I)A\|_2=2\sqrt{3}\,2^{-n}$")
plot.set(xlim=(.7,8.3),ylim=(-.02,2.2),xticks=ns,yticks=[0,.5,1,1.5,2])
plot.set_xlabel(r"$n$",fontsize=12,labelpad=0)
plot.grid(color="#e1e7ec",lw=.7);plot.spines[["top","right"]].set_visible(False)
plot.legend(loc="center right",fontsize=11,frameon=True,facecolor="#fbfcfe",edgecolor="#d5dfe7")
txt(ax,.5,.22,r"$A=\sqrt{3}\sum_{j\geq1}2^{-j}E_{j0},\qquad\|A\|_2=1$",
    ha="center",fontsize=17)
txt(ax,.5,.105,r"moving witness: $U_nE_{n0}=-E_{n0}$,  $\|E_{n0}\|_2=1$",
    ha="center",fontsize=15)
txt(ax,.5,.035,"Eight samples shown; the formulas and full strong/u proofs hold for all n.",
    ha="center",fontsize=12,color=MUTED)

fig.text(.5,.025,"Proofs: CIM6.d–n (full matrix and field identities), CIM6.o–p (phase obstruction), CIM6.s–v and CIM7.d–f (infinite model).",
         ha="center",fontsize=12,color=MUTED)
for ext in ("png","svg"):
    fig.savefig(HERE/f"canonical-core-automorphisms.{ext}",dpi=160,facecolor=fig.get_facecolor(),**({"metadata":{"Date":None}} if ext == "svg" else {}))
plt.close(fig)

data={
 "title":"Canonical implementation: phases and strong convergence",
 "license":"CC0-1.0 to the extent of rights held; font terms separate",
 "matrix":{"h":[[1,0],[0,4]],"v":[[0,1],[1,0]],"transported_h":[[4,0],[0,1]],
           "weight":"Tr(h*x)","weight_of_identity":5,
           "cocycle":"diag(exp(i*t*log(4)),exp(-i*t*log(4)))",
           "V":"V(r)A=h^(-i*r)*v*h^(i*r)*A*v*",
           "entries":"V(r)[[a,b],[c,d]]=[[z*d,z*c],[z^-1*b,z^-1*a]], z=exp(i*r*log(4))",
           "r0":"pi/(2*log(4))","cocycle_at_r0":[["i",0],[0,"-i"]],
           "V_E11_at_r0":"-i E22","F":"F(r)A=h^(i*r)*A","F_at_r0":"left diag(1,i)",
           "F_V_Fstar":"constant U_v: A -> v*A*v*","F_pi_x_Fstar":"constant left x",
           "F_lambda_t_Fstar":"left h^(i*t) times T_t","T_t":"xi(r)->xi(r-t)",
           "full_domain":"L2(R, Hilbert-Schmidt M2)"},
 "phase":{"canonical_square":"I","canonical_E11_orbit":["E11","E22","E11"],
          "noncanonical_square":"-I","noncanonical_E11_orbit":["E11","i E22","-E11"],
          "cone_test":"i U(I2)=i I2 is not positive","matrix_rephasing_notice":"v->i v leaves U_v and V_v unchanged"},
 "infinite":{"K":"ell2(N0)","H":"Hilbert-Schmidt operators on K","n_range":"n>=1",
             "trace":"full faithful normal semifinite Tr","v_n":"I-2*|e_n><e_n|",
             "cocycle":"1 from exact whole-positive weight preservation and BC22",
             "canonical_U_n":"A->v_n*A*v_n","V_n":"constant U_n on all L2 sections",
             "fixed_vector":"A=sqrt(3)*sum_(j>=1) 2^-j E_j0","fixed_vector_norm":1,
             "fixed_error":"2*sqrt(3)*2^-n","operator_norm_error":2,
             "moving_witness":"E_n0","moving_witness_error":2,
             "section_witness":"1_[0,1](r) E_n0","section_witness_norm":1,
             "fixed_shift":"S e_j=e_(j+1)","fixed_shift_operator_error":2,
             "sample":[{"n":int(n),"fixed_error_exact":f"2*sqrt(3)/2^{int(n)}","operator_norm_error":2} for n in ns],
             "sample_notice":"Only n=1,...,8 is plotted. Analytic full-H and u proofs are retained in CIM6.s-v."},
 "proof_locators":["CIM6.d-n","CIM6.o-p","CIM6.s-v","CIM7.a-f"]
}
(HERE/"data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font=Path(font_manager.findfont("DejaVu Sans"));license_file=font.parent/"LICENSE_DEJAVU"
if not license_file.is_file():raise FileNotFoundError("Missing bundled font terms")
shutil.copyfile(license_file,HERE/"FONT-LICENSE.txt")
(HERE/"TERMS.md").write_text(
 "# Figure terms\n\nOriginal diagram, renderer and exact mathematical data: CC0-1.0 to the extent of rights held. "
 "DejaVu font terms are retained in FONT-LICENSE.txt. No external images, excerpts or downloaded data are included. "
 "Run python render.py with NumPy and Matplotlib to reproduce PNG, editable SVG and data. "
 "The matrix panels are exact algebraic identities. The infinite-model plot renders eight values of exact formulas; "
 "the complete all-vector strong/strong-star and normal-functional u-convergence proofs are retained in the lesson. "
 "The constant norm obstruction and all displayed limiting claims have analytic proofs, not extrapolations from the plot.\n",encoding="utf-8")
print("Rendered exact matrix/phase panels and labeled infinite-model samples.")
