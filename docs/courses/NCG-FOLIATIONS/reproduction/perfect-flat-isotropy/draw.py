"""Original CC0 diagram; exact groups, coordinates and proved flatness bounds."""
from pathlib import Path
from io import BytesIO
import os

HERE = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(HERE / "runtime-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                    "svg.fonttype": "none", "svg.hashsalt": "ncg-pfg-20261011"})

def make():
    fig = plt.figure(figsize=(17, 10), dpi=100, facecolor="#f5f7fb")
    fig.text(.04,.957,"Perfect flat isotropy: local characters do not assemble",fontsize=23,
             fontweight="bold",color="#17283e")
    fig.text(.04,.920,"Actual smooth germs in a coherent ML₁ᶜ-oriented foliation; no reduced KK-class asserted",fontsize=13,color="#44546a")
    def panel(x,y,w,h,title):
        fig.add_artist(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
            transform=fig.transFigure,facecolor="white",edgecolor="#d6dfeb",zorder=0))
        fig.text(x+.014,y+h-.039,title,fontsize=15,fontweight="bold",color="#17283e")
    panel(.04,.51,.44,.355,"A. Injective stages; zero character transition")
    panel(.52,.51,.44,.355,"B. Actual intervals accumulating at zero")
    panel(.04,.10,.44,.355,"C. Exact upper bounds for all fixed derivatives")
    panel(.52,.10,.44,.355,"D. Whole actual isotropy and normal data")
    ax=fig.add_axes([.057,.548,.40,.245]);ax.set_axis_off()
    ax.text(0,.91,"φ(a) = [a,b]     φ(b) = [a,b²]",fontsize=14,color="#145e82")
    ax.text(0,.73,"F₁  →  F₂  →  F₃  →  ···  →  Γ",fontsize=18,fontweight="bold")
    ax.text(0,.57,"Every Fᵢ has rank two; all arrows inject (PFG.1–3).",fontsize=12)
    ax.text(0,.41,"(Fᵢ)ₐᵦ = ℤ²   →⁰   (Fᵢ₊₁)ₐᵦ = ℤ²",fontsize=16,color="#985034")
    ax.text(0,.24,"Γ = [Γ,Γ] ≠ 1; Hom(Γ, ℝ) = 0.",fontsize=15,fontweight="bold")
    ax.text(0,.05,"Every nontrivial finitely generated subgroup is free.\nIts own map to ℤ cannot extend compatibly over Γ.",fontsize=11.5)
    ax=fig.add_axes([.552,.653,.375,.125]);ax.set_ylim(-.14,.17);ax.set_xlim(-.17,.60)
    ax.axhline(0,color="#65758a",lw=1)
    ax.plot(0,0,"o",color="#a13838",ms=8)
    for n in range(1,7):
        c=2**(-n);r=2**(-n-3)
        ax.fill_between([c-r,c+r],-.04,.04,color="#287d9d",alpha=.80)
        if n<=4:ax.text(c,.067,"I"+str(n),ha="center",fontsize=11)
        else:
            ax.annotate("I"+str(n),xy=(c,.04),xytext=(c if n==5 else -.025,.135 if n==5 else .095),
                        ha="center",fontsize=10,arrowprops={"arrowstyle":"-","color":"#65758a","lw":.8})
    ax.set_yticks([]);ax.set_xticks([-.125,0,.125,.25,.5]);ax.set_xticklabels(["−1/8","0","1/8","1/4","1/2"])
    ax.set_xlabel("original transverse coordinate x",labelpad=2)
    for spine in ("left","right","top"):ax.spines[spine].set_visible(False)
    fig.text(.551,.584,"cₙ = 2⁻ⁿ, rₙ = 2⁻ⁿ⁻³; Iₙ = (cₙ−rₙ, cₙ+rₙ)",fontsize=12)
    fig.text(.551,.549,"Identity on x < 0; at 0 the actual isotropy is Γ.\nOnly six intervals drawn; every neighborhood has a faithful tail.",fontsize=11)
    ax=fig.add_axes([.089,.196,.352,.183])
    for k,color in [(0,"#166a97"),(1,"#c07729"),(2,"#8760a6")]:
        ns=list(range(max(1,k),11));ys=[(n+3)*(n+1-k) for n in ns]
        ax.plot(ns,ys,"o-",color=color,lw=2,ms=4,label="k = "+str(k))
    ax.set_xlabel("interval index N");ax.set_ylabel("−log₂(proved bound)")
    ax.set_xticks(range(1,11));ax.grid(alpha=.15);ax.legend(loc="upper left",frameon=False)
    ax.spines["top"].set_visible(False);ax.spines["right"].set_visible(False)
    fig.text(.070,.128,"|∂ₓᵏ(hᵢ,ₛ−id)| ≤ 2⁻⁽ᴺ⁺³⁾⁽ᴺ⁺¹⁻ᵏ⁾   for N ≥ max(i,k,1).",fontsize=11.5)
    fig.text(.070,.108,"These are proved upper bounds, not measured displacements.",fontsize=10.5,color="#44546a")
    ax=fig.add_axes([.549,.132,.377,.248]);ax.set_axis_off()
    ax.text(0,.95,"V = (S̃ × ℝ) / π₁S; dim V = 3, q = 1",fontsize=14,fontweight="bold")
    ax.text(0,.78,"Actual holonomy germs of the global hᵢ,ₛ:",fontsize=12)
    ax.text(.03,.62,"H₀⁰ = Γ  ⊂  ker D  ∩  ker j∞",fontsize=18,color="#a13838")
    ax.text(0,.43,"Lift: √Dh > 0, central phase 1; chain rule coherent.",fontsize=11.5)
    ax.text(0,.27,"Full inverse: −Lₜ₁; final right Cl₁ retained.",fontsize=13,color="#145e82")
    ax.text(0,.08,"Actual source counting and suspension plaques retained.\nIdentity germs collapse their old labels; Γ-arrows stay distinct.",fontsize=11)
    fig.text(.04,.050,"Proof: PFG.1–PFG.12. Actual germ equalities: PFG.10–PFG.11. Suspension labels are not added to the effective groupoid.",fontsize=11,color="#44546a")
    fig.text(.04,.027,"Original CC0 mathematical expression and generator. The general normalized reduced normal class, with original disk pairing +1, remains required.",fontsize=10.5,color="#44546a")
    return fig

def make_auxiliary():
    fig=plt.figure(figsize=(17,9),dpi=100,facecolor="#f5f7fb")
    fig.text(.04,.953,"A proper action of isotropy does not supply a groupoid length",fontsize=23,
             fontweight="bold",color="#17283e")
    fig.text(.04,.911,"Explicit nonabelian construction on the whole Γ; actual bisection continuity checked separately",fontsize=13,color="#44546a")
    def panel(x,y,w,h,title):
        fig.add_artist(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
            transform=fig.transFigure,facecolor="white",edgecolor="#d6dfeb",zorder=0))
        fig.text(x+.014,y+h-.044,title,fontsize=15,fontweight="bold",color="#17283e")
    panel(.04,.47,.44,.36,"A. Positive-definite free-stage functions")
    panel(.52,.47,.44,.36,"B. Proper affine Hilbert action of Γ")
    panel(.04,.105,.92,.29,"C. Actual germ topology forces zero on the entire isotropy")
    ax=fig.add_axes([.067,.504,.39,.246]);ax.set_axis_off()
    ax.text(0,.94,"pₙ(g) = exp(−tₙ ℓₙ(g)) on the chosen free stage;\npₙ(g) = 0 off that subgroup.",fontsize=13)
    ax.text(0,.69,"Tree-edge Gram factors prove positivity.\nCoset blocks prove positivity of zero extension.",fontsize=12,color="#145e82")
    ax.text(0,.44,"pₙ(1) = 1; pₙ ∈ c₀(Γ).",fontsize=16,fontweight="bold")
    ax.text(0,.22,"For each fixed gⱼ, 1−pₙ(gⱼ) ≤ 2⁻ⁿ for n ≥ j.",fontsize=13)
    ax.text(0,.03,"Full proof and exact choices: PFG.13–PFG.14.",fontsize=11,color="#44546a")
    ax=fig.add_axes([.550,.500,.38,.253]);ax.set_axis_off()
    ax.text(0,.93,"b(g) = (πₙ(g)vₙ − vₙ)ₙ ∈ ⨁ Hₙ",fontsize=17,fontweight="bold")
    ax.text(0,.72,"‖b(g)‖² = 2 Σₙ (1−pₙ(g)) < ∞",fontsize=15)
    ax.text(0,.52,"b(gh) = π(g)b(h) + b(g)",fontsize=15,color="#145e82")
    ax.text(0,.31,"Outside ⋃ₙ≤ᴹ {pₙ ≥ 1/2}, ‖b(g)‖² > M.\nThe union is finite; choose M > R for level R.",fontsize=12)
    ax.text(0,.08,"Proper on the whole abstract Γ (PFG.15).\nΓ is perfect; no abelian character is used.",fontsize=12,color="#44546a")
    ax=fig.add_axes([.063,.142,.867,.164]);ax.set_axis_off()
    ax.text(0,.86,"For every γ ∈ H₀⁰ = Γ, choose its actual word bisection:",fontsize=14)
    ax.text(.035,.50,"[word, xₘ] = unitₓₘ    →    [word, 0] = γ     (xₘ < 0, xₘ → 0)",fontsize=19,color="#a13838")
    ax.text(.035,.14,"ψ continuous and zero on units   ⇒   ψ(γ) = 0 for every γ ∈ Γ",fontsize=17,fontweight="bold")
    fig.text(.063,.112,"The infinite discrete source fibre Γ is the zero level set. Such ψ cannot be proper there (PFG.16).",fontsize=12)
    fig.text(.04,.054,"The isotropy action is proved, but its squared norm cannot extend as a continuous normalized proper length on this actual groupoid.",fontsize=11,color="#44546a")
    fig.text(.04,.027,"This excludes that substitution, not a different normally geometric reduced class. Original q, inverse line, right Clq and disk pairing +1 remain required.",fontsize=10.5,color="#44546a")
    return fig

def render_figure(factory):
    fig=factory();out={}
    for ext in ("png","svg"):
        buf=BytesIO()
        metadata={"Software":"Original CC0 mathematical diagram"} if ext=="png" else {"Date":None,"Creator":"Original CC0 mathematical diagram"}
        fig.savefig(buf,format=ext,dpi=100,metadata=metadata)
        out[ext]=buf.getvalue()
    plt.close(fig)
    return out

def render():return render_figure(make)
def render_auxiliary():return render_figure(make_auxiliary)

if __name__=="__main__":
    target=HERE/"figures";target.mkdir(exist_ok=True)
    for stem,fn in (("perfect-flat-isotropy",render),("proper-isotropy-no-groupoid-length",render_auxiliary)):
        for ext,data in fn().items():(target/(stem+"."+ext)).write_bytes(data)
    print("Rendered exact germ-group, derivative-bound and proper auxiliary diagrams.")
