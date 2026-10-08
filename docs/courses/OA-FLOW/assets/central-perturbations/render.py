"""Reproduce the exact central-perturbation diagram; no source/font files copied."""
from pathlib import Path
from fractions import Fraction
import argparse, json, hashlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle

HERE=Path(__file__).resolve().parent
DEFAULT_FONT_DIR=HERE.parent/"typeiii-zero-decomposition"

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--font-dir",type=Path,default=DEFAULT_FONT_DIR,
                    help="Existing directory containing DejaVuSans.ttf and DejaVuSans-Bold.ttf; fonts are not copied.")
    ap.add_argument("--output-dir",type=Path,default=HERE)
    args=ap.parse_args()
    data=json.loads((HERE/"data.json").read_text(encoding="utf-8"))
    for name in ["DejaVuSans.ttf","DejaVuSans-Bold.ttf"]:
        p=args.font_dir/name
        if not p.is_file():
            raise SystemExit(f"Missing external font: {p}. Supply --font-dir; no font downloading or copying is performed.")
        font_manager.fontManager.addfont(str(p))
    family=font_manager.FontProperties(fname=str(args.font_dir/"DejaVuSans.ttf")).get_name()
    plt.rcParams.update({"font.family":family,"font.size":12,"svg.fonttype":"path",
                         "svg.hashsalt":"oa-flow-central-perturbations-v1",
                         "axes.unicode_minus":True})
    d=list(map(Fraction,data["old_log_density"]))
    a=list(map(Fraction,data["middle_implementer"]))
    b=[x-y for x,y in zip(d,a)]
    assert b==list(map(Fraction,data["new_log_density"]))
    old=sorted({x-y for x in d for y in d})
    new=sorted({x-y for x in b for y in b})
    pairs=sorted({(d[i]-d[j],b[i]-b[j]) for i in range(4) for j in range(4)})
    mu=Fraction(data["mu"])
    assert old==list(map(Fraction,data["expected_old_spectrum"]))
    assert new==list(map(Fraction,data["expected_new_spectrum"]))
    assert not any(mu<=abs(x)<=2*mu for x in old)
    assert max(map(abs,a))<=mu/2
    assert max(abs(x-y) for x,y in pairs)==1
    assert all(abs(x-y)<=mu for x,y in pairs)
    assert all(y==0 for x,y in pairs if abs(x)<=mu)
    # The exact zero commutators characterize the two centralizers.
    assert all((d[i]==d[j])==(i==j) for i in range(4) for j in range(4))
    assert all((b[i]==b[j])==(i//2==j//2) for i in range(4) for j in range(4))
    navy="#15304a";green="#237c65";red="#aa3849";gold="#a3680c";gray="#617082"
    fig=plt.figure(figsize=(14,10),facecolor="#fafbfc")
    fig.text(.06,.955,"A central density cancels the middle frequencies",fontsize=23,weight="bold",color=navy)
    fig.text(.06,.92,"βₜ = Ad(exp(−it a)) αₜ     |     k = exp(−a)     |     μ = 2",fontsize=16,color=navy)
    ax=fig.add_axes([.09,.50,.82,.33])
    ax.set_xlim(-8,8);ax.set_ylim(-.42,1.52)
    ax.set_xticks(range(-8,9));ax.set_yticks([])
    for spine in ["top","right","left"]: ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#bec6ce")
    ax.tick_params(axis="x",labelsize=11,colors=gray)
    ax.set_xlabel("positive eigenfrequency r:  αₜ(x) = exp(itr)x",fontsize=12,color=gray)
    for y in [1,0]: ax.hlines(y,-8,8,color="#b7c2cd",linewidth=1)
    for left,right in data["old_excluded_closed_annuli"]:
        ax.add_patch(Rectangle((left,.84),right-left,.32,facecolor="#f7dce1",edgecolor=red,hatch="///",linewidth=.8))
    ax.hlines(1,-2,2,color=green,linewidth=7)
    ax.plot([-2,2],[1,1],"o",mfc="white",mec=green,ms=7,zorder=5)
    ax.hlines(1,-8,-4,color=navy,linewidth=4);ax.hlines(1,4,8,color=navy,linewidth=4)
    ax.plot([-4,4],[1,1],"o",mfc="white",mec=navy,ms=7,zorder=5)
    ax.text(-8,1.30,"OLD: annuli [−4,−2] and [2,4] are empty",weight="bold",color=navy,fontsize=13)
    ax.text(0,1.20,"middle algebra Q",ha="center",color=green,fontsize=12)
    ax.add_patch(Rectangle((-2,-.12),4,.24,facecolor="#e4f1eb",edgecolor="none"))
    ax.hlines(0,-8,-2,color=navy,linewidth=4);ax.hlines(0,2,8,color=navy,linewidth=4)
    ax.plot([-2,2],[0,0],"o",color=navy,ms=6)
    ax.plot([0],[0],"o",color=green,ms=9)
    ax.text(-8,.25,"NEW: spectrum ⊂ (−∞,−2] ∪ {0} ∪ [2,∞)",weight="bold",color=navy,fontsize=13)
    ax.annotate("",xy=(0,.06),xytext=(0,.84),arrowprops={"arrowstyle":"->","color":green,"lw":2})
    ax.text(.17,.48,"Q becomes fixed",color=green,fontsize=12)
    ax.text(-5.3,.52,"outer shift ≤ 2",ha="center",color=navy,fontsize=12)
    ax.text(5.3,.52,"outer shift ≤ 2",ha="center",color=navy,fontsize=12)
    fig.text(.09,.858,"GENERAL BOUND   ‖a‖ ≤ 1  ⇒  each linking leg has frequencies in [−1,1]  ⇒  total error [−2,2]",
             fontsize=12,color=gray)
    bx=fig.add_axes([.09,.16,.82,.22])
    bx.set_xlim(-8,8);bx.set_ylim(-.25,1.35);bx.set_yticks([])
    bx.set_xticks(range(-8,9));bx.tick_params(axis="x",labelsize=11,colors=gray)
    for spine in ["top","right","left"]:bx.spines[spine].set_visible(False)
    bx.spines["bottom"].set_color("#bec6ce")
    for y in [1,0]:bx.hlines(y,-8,8,color="#bec6ce",linewidth=1)
    for x,y in pairs:
        color=green if y==0 else gold
        bx.annotate("",xy=(float(y),.06),xytext=(float(x),.94),
                    arrowprops={"arrowstyle":"->","color":color,"lw":1.7,"alpha":.85},zorder=2)
    bx.scatter(list(map(float,old)),[1]*len(old),s=45,color=navy,zorder=4)
    bx.scatter(list(map(float,new)),[0]*len(new),s=70,color=green,zorder=4)
    bx.text(-7.9,1.19,"Sp(α)",fontsize=12,color=navy,weight="bold")
    bx.text(-7.9,.14,"Sp(β)",fontsize=12,color=green,weight="bold")
    fig.text(.09,.432,"EXACT M₄ MODEL   d = (½, −½, 13/2, 11/2),   a = (½, −½, ½, −½)",fontsize=14,color=navy,weight="bold")
    fig.text(.09,.400,"New log density d − a = (0, 0, 6, 6).  Exact displacements are at most 1; the theorem allows 2.",
             fontsize=12,color=gray)
    fig.text(.09,.094,"Containments above: CPB4, CPB11, CPB13–15.  Exact matrix-unit arrows below: CPB31–32.",fontsize=11,color=gray)
    fig.text(.09,.064,"Finite-dimensional illustration, not a type III factor.  Human source: Takesaki II, XII.4.7–4.9, pp.407–410.",fontsize=10,color=gray)
    fig.text(.09,.035,"Original diagram and rational data · CC0-1.0 · Existing programme DejaVu font used without copying font files.",
             fontsize=10,color=gray)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for ext in ["png","svg"]:
        p=args.output_dir/f"central-perturbations.{ext}"
        meta={"Software":"Original OA-FLOW central-perturbations renderer"} if ext=="png" else {"Date":None,"Creator":"Original OA-FLOW central-perturbations renderer"}
        fig.savefig(p,dpi=180,metadata=meta,facecolor=fig.get_facecolor())
        print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
    plt.close(fig)
    print("Exact rational spectral checks passed; 16 matrix units and both full centralizers checked.")

if __name__=="__main__":
    main()
