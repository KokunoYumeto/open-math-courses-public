"""Original deterministic schematic for the given-infinite-periodic-weight theorem."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT/"assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":12,
                    "mathtext.fontset":"dejavusans",
                    "svg.hashsalt":"oa-flow-generalized-trace-gt-v1",
                    "svg.fonttype":"path"})
navy, blue, green, orange, gray, pale = (
    "#173654", "#1769aa", "#16806a", "#c95524", "#697989", "#edf3f8")
fig=plt.figure(figsize=(16,12),facecolor="white")
fig.text(.06,.952,"An infinite periodic weight gives the full regular decomposition",
         fontsize=21,weight="bold",color=navy)
fig.text(.06,.914,"Given: type IIIλ factor with separable predual, 0 < λ < 1; faithful n.s.f. φ,",
         fontsize=13,color=gray)
fig.text(.06,.888,"φ(1) = ∞ and modular period P = 2π/(−log λ). No period-existence assertion is included.",
         fontsize=13,color=gray)

def panel(rect,title):
    ax=fig.add_axes(rect);ax.set_axis_off();ax.set(xlim=(0,1),ylim=(0,1))
    ax.text(0,.97,title,fontsize=14.5,weight="bold",color=navy)
    return ax

ax=panel([.06,.51,.42,.32],"1. A fixed swap proves whole-cone scaling (GT1–2)")
ax.text(0,.84,r"$\Psi(X)=\phi(x_{11})+\lambda\phi(x_{22})$",
        fontsize=16,color=navy)
for x,l in [(.08,r"$p_1K$"),(.69,r"$p_2K$")]:
    ax.add_patch(Rectangle((x,.59),.22,.13,facecolor=pale,edgecolor="none"))
    ax.text(x+.11,.655,l,ha="center",va="center",fontsize=19,color=navy)
ax.add_patch(FancyArrowPatch((.32,.655),(.66,.655),arrowstyle="-|>",
                             mutation_scale=16,color=blue))
ax.text(.49,.76,r"$v=uE_{21}\in B_\Psi$",ha="center",fontsize=14,color=blue)
ax.text(0,.45,r"$w=v+v^*,\qquad w=w^*,\quad w^2=1$",fontsize=15,color=navy)
ax.text(0,.30,r"$\lambda\phi(uxu^*)=\phi(x)\quad(x\geq0)$",fontsize=16,color=green)
ax.text(0,.15,r"$U=u^*:\quad \phi(UxU^*)=\lambda\phi(x)$",fontsize=16,color=green)
ax.text(0,.02,"Every positive x, including infinite weight values.",fontsize=12,color=gray)

ax=panel([.54,.51,.40,.32],"2. Every integer degree is a full GNS copy (GT4–5)")
ax.text(0,.84,r"$W(\delta_n\otimes\Lambda_\tau(x))=\Lambda_\phi(U^n x)$",
        fontsize=16,color=navy)
xs=[.09,.28,.47,.66,.85]
for n,x in zip(range(-2,3),xs):
    ax.add_patch(Rectangle((x-.072,.56),.144,.13,facecolor=pale,edgecolor="none"))
    ax.text(x,.625,r"$H_\tau$",ha="center",va="center",fontsize=17,color=navy)
    ax.text(x,.45,str(n),ha="center",fontsize=13,color=gray)
for x,y in zip(xs[:-1],xs[1:]):
    ax.add_patch(FancyArrowPatch((x+.076,.625),(y-.077,.625),arrowstyle="-|>",
                                mutation_scale=13,color=green))
ax.text(.01,.625,"⋯",ha="right",fontsize=17,color=gray)
ax.text(.99,.625,"⋯",ha="left",fontsize=17,color=gray)
ax.text(0,.29,r"$W^*\pi_\phi(U)W:\ n\longmapsto n+1$",fontsize=16,color=green)
ax.text(0,.15,r"$\|\Lambda_\phi(Ux)\|=\|\Lambda_\phi(x)\|$",fontsize=16,color=navy)
ax.text(0,.02,"Boxes sample the full ℤ sum; no cyclic wrap-around.",fontsize=12,color=gray)

ax=panel([.06,.08,.42,.34],"3. Two successive limits prove onto-ness (GT4)")
ax.text(0,.84,r"$x\in\mathfrak{n}_\phi,\quad 0\leq c_i\uparrow1,\quad\tau(c_i)<\infty$",
        fontsize=15.5,color=navy)
for yy,lab in [(.69,r"$\Lambda_\phi(T_L(x)c_i)\in\operatorname{Ran}W$"),
               (.42,r"$\Lambda_\phi(xc_i)\in\operatorname{Ran}W$"),
               (.15,r"$\Lambda_\phi(x)\in\operatorname{Ran}W$")]:
    ax.text(.04,yy,lab,fontsize=17,color=green)
for yy,lab in [(.62,"L → ∞, with i fixed: bounded strong Fejér limit"),
               (.35,"i increases: full right centralizer multiplier")]:
    ax.add_patch(FancyArrowPatch((.065,yy),(.065,yy-.12),arrowstyle="-|>",
                                mutation_scale=14,color=blue))
    ax.text(.115,yy-.075,lab,fontsize=11.7,color=blue)
ax.text(0,.015,"The range is closed; the last vectors are GNS-dense.",fontsize=12,color=gray)

ax=panel([.54,.08,.40,.34],"4. The second dual moves both indices down (GT6)")
ax.text(0,.83,r"$\beta_m:\ d\otimes E_{ij}\longmapsto"
        r"\theta^m(d)\otimes E_{i-m,j-m}$",fontsize=15.3,color=navy)
ax.text(0,.68,r"$\theta=\operatorname{Ad}U|_N,\quad\tau\theta=\lambda\tau$",
        fontsize=16,color=green)
ax.text(0,.54,r"$\widehat\tau\beta_m=\lambda^m\widehat\tau$",
        fontsize=19,color=green)
ax.text(0,.40,"Exact sample λ = 1/2; normalize by τ(e), 0 < τ(e) < ∞:",fontsize=11.4,color=gray)
for n,x in zip(range(-2,3),xs):
    val=Fraction(1,2)**n
    ax.text(x,.29,str(n),ha="center",fontsize=13,color=gray)
    ax.text(x,.17,str(val),ha="center",fontsize=15,color=orange)
ax.text(.0,.29,"m",fontsize=12,color=gray,ha="right")
ax.text(.0,.17,"2⁻ᵐ",fontsize=12,color=orange,ha="right")
ax.text(0,.015,"The projections θᵐ(e) are not asserted orthogonal.",fontsize=12,color=gray)
fig.savefig(OUT/"generalized-trace-mechanism.png",dpi=160,facecolor="white",
            metadata={"Software":"OA-FLOW original renderer"})
fig.savefig(OUT/"generalized-trace-mechanism.svg",facecolor="white",
            metadata={"Date":None,"Creator":"OA-FLOW original renderer"})
plt.close(fig)
p=OUT/"generalized-trace-mechanism.svg"
p.write_text(p.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
data={"schematic_not_finite_dimensional_type_III_model":True,
      "assumes_actual_infinite_periodic_weight":True,
      "balanced_weight":"Psi(X)=phi(x11)+lambda*phi(x22)",
      "v_initial":"p1","v_final":"p2","v_entry":"u at (2,1)","U":"u*",
      "whole_cone_scaling":"phi(U*x*U*)=lambda*phi(x)",
      "modular_character":"sigma_t(U)=exp(i*t*log(lambda))*U",
      "regular_map":"delta_n tensor Lambda_tau(x) -> Lambda_phi(U^n x)",
      "left_shift":"n -> n+1","left_GNS_norm_factor":"1",
      "right_GNS_norm_factor":"lambda^(-1/2)",
      "onto_limits":["L tends to infinity with i fixed","then cutoff net i"],
      "second_dual":"d tensor E_ij -> theta^m(d) tensor E_(i-m,j-m)",
      "illustrative_lambda":"1/2","visible_m":list(range(-2,3)),
      "trace_ratios":[str(Fraction(1,2)**m) for m in range(-2,3)],
      "trace_projection_iterates_assumed_orthogonal":False,
      "proof_locators":["gt-1","gt-2","gt-4","gt-5","gt-6"]}
(ROOT/"FIGURE_DATA.json").write_text(json.dumps(data,indent=2)+"\n",
                                    encoding="utf-8",newline="\n")
