"""Exact deterministic graph and index schematic for CA; no finite-matrix approximation claim."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"assets";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                    "mathtext.fontset":"dejavusans","svg.fonttype":"path",
                    "svg.hashsalt":"oa-flow-countable-amplification-ca-v1"})
navy,blue,green,orange,gray,pale="#173654","#1769aa","#16806a","#c95524","#697989","#edf3f8"
fig=plt.figure(figsize=(16,12),facecolor="white")
fig.text(.06,.95,"Countable amplification preserves the complete modular graph",
         fontsize=22,weight="bold",color=navy)
fig.text(.06,.91,"Any faithful normal semifinite base weight, on arbitrary Hilbert spaces.",
         fontsize=13.5,color=gray)
fig.text(.06,.882,"Finite windows below illustrate the full countable domains; proper infiniteness is used only to return to M.",
         fontsize=12.7,color=gray)

ax=fig.add_axes([.06,.49,.42,.34]);ax.set_axis_off();ax.set(xlim=(-.8,5.6),ylim=(-1,5.6))
ax.text(-.8,5.32,"1. Transpose indices and apply the base involution",fontsize=14,weight="bold",color=navy)
for i in range(4):
    for j in range(4):
        col=blue if (i,j)==(1,3) else orange if (i,j)==(3,1) else pale
        ax.add_patch(Rectangle((j,3-i),.88,.88,facecolor=col,edgecolor="white"))
        lab=r"$\xi_{13}$" if (i,j)==(1,3) else r"$S_\psi\xi_{13}$" if (i,j)==(3,1) else r"$H_\psi$"
        ax.text(j+.44,3-i+.44,lab,ha="center",va="center",
                fontsize=13.5 if (i,j)==(3,1) else 14,color="white" if col in [blue,orange] else gray)
for k in range(4):
    ax.text(k+.44,4.05,str(k),ha="center",color=gray)
    ax.text(-.23,3-k+.44,str(k),ha="right",va="center",color=gray)
ax.text(1.8,4.55,"column j",color=gray,fontsize=12)
ax.text(-.69,2.15,"row i",rotation=90,color=gray,fontsize=12)
ax.add_patch(FancyArrowPatch((3.85,2.42),(1.90,.44),connectionstyle="arc3,rad=-.38",
                             arrowstyle="-|>",mutation_scale=17,color=orange,lw=2))
ax.text(4.22,2.7,"(1,3)",color=blue,fontsize=12)
ax.text(4.22,2.22,"→ (3,1)",color=orange,fontsize=12)
ax.text(-.15,-.63,r"$(T\xi)_{ij}=S_\psi\xi_{ji}$",color=navy,fontsize=20)

ax=fig.add_axes([.55,.49,.39,.34]);ax.set_axis_off();ax.set(xlim=(0,1),ylim=(0,1))
ax.text(0,.96,"2. The graph norm controls both tails (CA3–4)",fontsize=14,weight="bold",color=navy)
ax.text(0,.81,r"$\|\xi\|_T^2=\sum_{i,j}(\|\xi_{ij}\|^2+\|S_\psi\xi_{ij}\|^2)$",
        fontsize=16,color=navy)
ax.text(0,.64,"First: cut to F × F. Both squared-sum tails tend to zero.",
        fontsize=12.3,color=green)
ax.text(0,.53,"Then: approximate finitely many base graph coordinates.",
        fontsize=12.3,color=green)
ax.text(0,.38,r"$VS_\rho V^*=T$",fontsize=23,color=green)
ax.text(0,.23,r"$D(T^*T)=\{\xi:\xi_{ij}\in D(\Delta_\psi),$",
        fontsize=16,color=navy)
ax.text(.21,.12,r"$\sum_{i,j}\|\Delta_\psi\xi_{ij}\|^2<\infty\}$",
        fontsize=16,color=navy)
ax.text(0,.01,"The proof checks both graph inclusions and the adjoint.",fontsize=11.8,color=gray)

ax=fig.add_axes([.06,.07,.88,.33]);ax.set_axis_off();ax.set(xlim=(0,1),ylim=(0,1))
ax.text(0,.97,"3. An exact filling example in B(ℓ²ℕ₀): every basis vector occurs once (CA6)",fontsize=15,weight="bold",color=navy)
ax.text(0,.82,r"$v_je_m=e_{\,2^j(2m+1)-1},\quad"
        r"L(\delta_j\otimes e_m)=e_{\,2^j(2m+1)-1}$",fontsize=20,color=navy)
colors=[blue,green,orange,"#7858a6"]
for j in range(4):
    yy=.63-.135*j
    ax.text(.0,yy,"j = "+str(j),va="center",fontsize=13,color=colors[j])
    for m in range(4):
        xx=.105+.115*m
        ax.add_patch(Rectangle((xx,yy-.049),.079,.098,facecolor=pale,edgecolor="none"))
        ax.text(xx+.0395,yy,str(2**j*(2*m+1)-1),ha="center",va="center",fontsize=16,color=colors[j])
    ax.text(.59,yy,"⋯",va="center",fontsize=20,color=colors[j])
ax.text(.02,.045,"⋮",ha="center",fontsize=22,color=gray)
ax.text(.70,.62,"Unique factorization:",fontsize=14,color=navy)
ax.text(.70,.47,r"$n+1=2^j(2m+1)$",fontsize=18,color=green)
ax.text(.70,.32,"orthogonal ranges",fontsize=14,color=navy)
ax.text(.70,.19,r"$\sum_{j\geq0}v_jv_j^*=1$",fontsize=19,color=green)
ax.text(.105,.017,"Shown: j,m = 0,1,2,3. The full infinite bijection supplies onto-ness.",fontsize=11.7,color=gray)
fig.savefig(OUT/"countable-amplification-mechanism.png",dpi=160,facecolor="white",
            metadata={"Software":"OA-FLOW original renderer"})
fig.savefig(OUT/"countable-amplification-mechanism.svg",facecolor="white",
            metadata={"Date":None,"Creator":"OA-FLOW original renderer"})
plt.close(fig)
p=OUT/"countable-amplification-mechanism.svg"
p.write_text(p.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
table=[[2**j*(2*m+1)-1 for m in range(4)] for j in range(4)]
sample=[]
for n in range(128):
    odd=n+1;j=0
    while odd%2==0:odd//=2;j+=1
    m=(odd-1)//2
    assert 2**j*(2*m+1)-1==n
    sample.append({"n":n,"j":j,"m":m})
data={"base_Hilbert_space_arbitrary":True,"grid_is_finite_window":True,
      "input_coordinate":[1,3],"output_coordinate":[3,1],
      "entry_map":"xi_13 -> S_psi xi_13","complete_operator":"(T xi)_ij=S_psi xi_ji",
      "graph_norm":"sum_ij(||xi_ij||^2+||S_psi xi_ij||^2)",
      "cutoff_order":["finite square F x F","then finite base graph approximants"],
      "filling_example_algebra":"B(ell2(N0)), type I infinity",
      "bijection":"b(j,m)=2^j(2m+1)-1","displayed_table":table,
      "exact_inverse_sample":sample,
      "finite_sample_is_not_proof":"The complete bijection is proved in the caption.",
      "proof_locators":["ca-2","ca-3","ca-4","ca-6"]}
(ROOT/"FIGURE_DATA.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
