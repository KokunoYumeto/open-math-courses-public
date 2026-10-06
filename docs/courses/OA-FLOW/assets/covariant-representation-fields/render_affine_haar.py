"""Exact affine-group example for OA-FLOW L39. Original code and illustration: CC0-1.0.
Run: python render_affine_haar.py
Dependencies: matplotlib, sympy. Outputs stay beside this script.
The DejaVu font notice retained in this directory governs the font outlines.
"""
from pathlib import Path
import json
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch, FancyArrowPatch

OUT=Path(__file__).resolve().parent
matplotlib.rcParams.update({
    "font.family":"DejaVu Sans", "font.size":14,
    "mathtext.fontset":"dejavusans", "svg.fonttype":"path",
    "svg.hashsalt":"oa-flow-l39-affine-haar-v1",
    "axes.spines.top":False,"axes.spines.right":False,
})
a,b,a0,b0=sp.symbols("a b a0 b0", positive=True)
right=sp.Matrix([a*a0,b+a*b0]); jac=sp.simplify(right.jacobian([a,b]).det())
assert jac==a0
ratio=sp.simplify(jac/(a*a0)**2/(1/a**2))
assert ratio==1/a0
left=sp.Matrix([a0*a,b0+a0*b]); left_jac=left.jacobian([a,b]).det()
assert sp.simplify(left_jac/(a0*a)**2/(1/a**2))==1
mass_R=sp.integrate(1/a**2,(a,1,2))
mass_Rg=sp.integrate(1/a**2,(a,2,4))
assert mass_R==sp.Rational(1,2) and mass_Rg==sp.Rational(1,4)
assert sp.Rational(1,2)*mass_R==mass_Rg
v=sp.Matrix([1,0]); w=sp.Matrix([1,1])/sp.sqrt(2)
eigenvalues=(v*v.T/2-w*w.T/2).eigenvals()
assert set(eigenvalues)=={-sp.sqrt(2)/4,sp.sqrt(2)/4}
checks={
    "group_product":"(a,b)(c,d)=(ac,b+ad)",
    "left_haar":"da db / a^2",
    "left_euclidean_jacobian":str(left_jac),
    "right_euclidean_jacobian":str(jac),
    "right_haar_mass_ratio":str(ratio),
    "g":[2,1],"R_vertices":[[1,0],[2,0],[2,1],[1,1]],
    "Rg_vertices":[[2,1],[4,2],[4,3],[2,2]],
    "euclidean_areas":{"R":1,"Rg":2},
    "haar_masses":{"R":str(mass_R),"Rg":str(mass_Rg)},
    "indicator_identity":"U_g 1_(Rg) = 1/sqrt(2) * 1_R",
    "input_norm_squared":str(mass_Rg),"output_norm_squared":str(sp.Rational(1,2)*mass_R),
    "pure_state_difference_eigenvalues":[str(x) for x in eigenvalues],
    "pure_state_difference_norm":str(sum(abs(x)*n for x,n in eigenvalues.items())),
    "all_exact_assertions_pass":True,
}
(OUT/"exact_checks.json").write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8")

fig=plt.figure(figsize=(16,10),facecolor="#f8fafc")
navy="#13243b";blue="#2563a8";orange="#ca682b";muted="#4d6075"
fig.text(.06,.942,"Right translation changes Haar mass",fontsize=27,weight="bold",color=navy)
fig.text(.06,.90,r"Affine group: $(a,b)(c,d)=(ac,b+ad)$     Left Haar measure: $d\lambda=da\,db/a^2$",fontsize=18,color=muted)
axes=[fig.add_axes([.07,.37,.37,.44]),fig.add_axes([.57,.37,.37,.44])]
vertices=[[(1,0),(2,0),(2,1),(1,1)],[(2,1),(4,2),(4,3),(2,2)]]
for ax,verts,col in zip(axes,vertices,[blue,orange]):
    ax.set_facecolor("white")
    ax.set_xlim(.5,4.5);ax.set_ylim(-.2,3.6);ax.set_aspect("equal",adjustable="box")
    ax.set_xticks([1,2,3,4]);ax.set_yticks([0,1,2,3])
    ax.grid(color="#e1e8ee",linewidth=1,zorder=0)
    ax.set_xlabel(r"$a$",fontsize=19,labelpad=5);ax.set_ylabel(r"$b$",fontsize=19,rotation=0,labelpad=13)
    ax.xaxis.set_label_coords(1.055, -.005)
    ax.tick_params(colors=muted,labelsize=14)
    for spine in ax.spines.values():spine.set_color("#8292a4")
    ax.add_patch(Polygon(verts,closed=True,facecolor=col,alpha=.18,edgecolor="none",zorder=2))
    ax.add_patch(Polygon(verts,closed=True,fill=False,edgecolor=col,linewidth=2.7,zorder=3))
    ax.scatter(*zip(*verts),s=28,color=col,zorder=4)
axes[0].set_title(r"$R=[1,2]\times[0,1]$",fontsize=22,pad=16,color=blue)
axes[1].set_title(r"$Rg=\{(2a,b+a):(a,b)\in R\}$",fontsize=21,pad=16,color=orange)
axes[0].text(1.5,.5,r"$R$",ha="center",va="center",fontsize=26,color=blue)
axes[1].text(3,2,r"$Rg$",ha="center",va="center",fontsize=26,color=orange)
for xy,offset in [((2,1),(-35,-25)),((4,2),(9,-5)),((4,3),(7,8)),((2,2),(-48,7))]:
    axes[1].annotate(str(xy),xy,xytext=offset,textcoords="offset points",fontsize=12,color=muted)
fig.add_artist(FancyArrowPatch((.445,.60),(.548,.60),transform=fig.transFigure,arrowstyle="-|>",mutation_scale=24,linewidth=2.5,color=navy))
fig.text(.497,.655,r"$g=(2,1)$",ha="center",fontsize=20,color=navy)
fig.text(.497,.556,r"$(a,b)\mapsto(2a,b+a)$",ha="center",fontsize=15,color=navy)
fig.text(.497,.512,"Jacobian = 2",ha="center",fontsize=16,color=muted)
fig.text(.255,.30,r"Euclidean area $=1$     Haar mass $=\frac{1}{2}$",ha="center",fontsize=18,color=blue)
fig.text(.755,.30,r"Euclidean area $=2$     Haar mass $=\frac{1}{4}$",ha="center",fontsize=18,color=orange)
box=FancyBboxPatch((.05,.042),.90,.207,boxstyle="round,pad=0.01,rounding_size=.012",transform=fig.transFigure,facecolor="white",edgecolor="#d6e0e9",linewidth=1.5)
fig.add_artist(box)
fig.text(.075,.208,"THE UNITARY PULLBACK",fontsize=13,weight="bold",color=muted)
fig.text(.075,.157,r"$U_g1_{Rg}=\frac{1}{\sqrt{2}}\,1_R$",fontsize=28,color=navy)
fig.text(.485,.157,r"$d\lambda(xg)=\frac{2\,da\,db}{(2a)^2}=\frac{1}{2}\,d\lambda(x)$",fontsize=24,color=navy)
fig.text(.075,.079,r"$\|1_{Rg}\|_2^2=\frac{1}{4}=\frac{1}{2}\,\lambda(R)=\left\|\frac{1}{\sqrt{2}}\,1_R\right\|_2^2$",fontsize=24,color=navy)
fig.text(.93,.02,"Exact regions and integrals; L39 (E6)-(E10).",ha="right",fontsize=10,color=muted)
fig.savefig(OUT/"affine-haar-norm.png",dpi=200,facecolor=fig.get_facecolor())
fig.savefig(OUT/"affine-haar-norm.svg",facecolor=fig.get_facecolor(),metadata={"Date":None,"Creator":"Original OA-FLOW illustration; CC0-1.0"})
plt.close(fig)
print(json.dumps({"outputs":["affine-haar-norm.png","affine-haar-norm.svg","exact_checks.json"],"checks":checks["all_exact_assertions_pass"]}))
