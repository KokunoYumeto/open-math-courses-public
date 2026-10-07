"""Exact finite algebra checks and a new labelled-kernel diagram.

Inputs are literal coordinates and the public COMPONENT-TERMS.md only.
No mathematical provider or private workflow file is read.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path


def reduced(word):
    stack = []
    for a in word:
        if stack and stack[-1] == -a:
            stack.pop()
        else:
            stack.append(a)
    return tuple(stack)


def inverse(word):
    return tuple(-a for a in reversed(word))


def product(*words):
    return reduced(itertools.chain.from_iterable(words))


def determinant(matrix):
    a = [list(row) for row in matrix]
    value = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            value = -value
        q = a[i][i]
        value *= q
        for j in range(i + 1, len(a)):
            scale = a[j][i] / q
            for k in range(i + 1, len(a)):
                a[j][k] -= scale * a[i][k]
    return value


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def compose(a, b):
    return tuple(a[b[i]] for i in range(3))


def pinverse(a):
    return tuple(a.index(i) for i in range(3))


def finite_checks():
    rows = []

    def check(name, predicate, detail):
        if not predicate:
            raise AssertionError(name)
        rows.append({"name": name, "passed": True, "detail": detail})

    v0, v1, v2 = (F(1), F(0)), (F(3, 5), F(4, 5)), (F(0), F(1))
    midpoint = tuple((a + b) / 2 for a, b in zip(v0, v1))
    check("exact_unit_features", all(dot(v, v) == 1 for v in (v0, v1, v2)),
          "v0=(1,0), v1=(3/5,4/5), v2=(0,1)")
    check("exact_midpoint_norm", midpoint == (F(4, 5), F(2, 5)) and
          dot(midpoint, midpoint) == F(4, 5), "||V||^2=4/5")
    check("nonnegative_gram_normalization", dot(midpoint, midpoint) >= F(1, 2),
          "sum of squared midpoint weights = 1/2")
    w = (2 / math.sqrt(5), 1 / math.sqrt(5))
    check("normalized_feature_coordinates", abs(sum(x*x for x in w) - 1) < 1e-14,
          "W=(2/sqrt(5),1/sqrt(5)); floating rendering only")

    vectors = (v0, v1, v2)
    gram = [[dot(a, b) for b in vectors] for a in vectors]
    minors = []
    for count in range(1, 4):
        for indices in itertools.combinations(range(3), count):
            minors.append(determinant([[gram[i][j] for j in indices] for i in indices]))
    check("rational_feature_gram_psd", all(q >= 0 for q in minors),
          "all 7 principal minors nonnegative, checked exactly")
    for coefficients in ((1, -1, 0), (2, -1, -1), (3, -5, 2)):
        cnd = sum((F(coefficients[i] * coefficients[j]) * (1-gram[i][j])
                   for i in range(3) for j in range(3)), F(0))
        combination = tuple(sum((F(coefficients[i])*vectors[i][j]
                                 for i in range(3)), F(0)) for j in range(2))
        check("cnd_" + "_".join(map(str, coefficients)), cnd == -dot(combination, combination)
              and cnd <= 0, "zero-sum CND identity, exact rational arithmetic")
    permuted = [vectors[2], vectors[0], vectors[1]]
    weighted = [[F(1, 3)*gram[i][j] + F(2, 3)*dot(permuted[i], permuted[j])
                 for j in range(3)] for i in range(3)]
    weighted_minors = [determinant([[weighted[i][j] for j in idx] for i in idx])
                       for n in range(1, 4) for idx in itertools.combinations(range(3), n)]
    check("invariant_weighted_gram_sample", all(q >= 0 for q in weighted_minors)
          and all(weighted[i][i] == 1 for i in range(3)), "weights 1/3 and 2/3")

    bi, bk, g = (1, 2), (2, 1, -2), (1, -2, 1)
    labels = [(), (1,), (2,), (1, 2), (-2, 1), (1, 2, -1, -2)]
    target = product(bi, g, inverse(bk))
    pairs = 0
    for h, bj in itertools.product(labels, repeat=2):
        cgh = product(bi, g, h, inverse(bj))
        ch = product(bk, h, inverse(bj))
        assert product(cgh, inverse(ch)) == target
        pairs += 1
    check("nonabelian_common_source_cancellation", pairs == 36,
          "36 reduced free-group word checks; inverse factors retain their order")

    permutations = list(itertools.permutations(range(3)))
    identity, swap = (0, 1, 2), (1, 0, 2)
    subgroup = {identity, swap}
    right_cosets = []
    for c in permutations:
        coset = {compose(h, c) for h in subgroup}
        if coset not in right_cosets:
            right_cosets.append(coset)
    same_coset = lambda a, b: any(a in c and b in c for c in right_cosets)
    check("right_coset_direction", all(same_coset(a,b) ==
          (compose(a, pinverse(b)) in subgroup) for a,b in itertools.product(permutations, repeat=2)),
          "all 36 ordered pairs in S3, with right cosets Hc")
    extended = []
    reps = [next(c for c in permutations if c in coset) for coset in right_cosets]
    for a in permutations:
        extended_row = []
        for b in permutations:
            if not same_coset(a,b):
                extended_row.append(F(0))
            else:
                c = next(c for c in reps if a in {compose(h,c) for h in subgroup})
                ha, hb = compose(a,pinverse(c)), compose(b,pinverse(c))
                extended_row.append(F(1) if ha == hb else F(3,5))
        extended.append(extended_row)
    coset_minors = [determinant([[extended[i][j] for j in idx] for i in idx])
                    for n in range(1, 7) for idx in itertools.combinations(range(6), n)]
    check("orthogonal_coset_extension_psd", all(q >= 0 for q in coset_minors),
          "all 63 principal minors of the six-label rational Gram matrix")

    near = ((1.0, 0.0), (2499/2501, 100/2501))
    epsilon = F(2,2501)
    defect_max = 0.0
    for a,b in itertools.product((0,F(1,4),F(1,2),F(3,4),1), repeat=2):
        v = tuple(float(a)*near[0][j] + (1-float(a))*near[1][j] for j in range(2))
        z = tuple(float(b)*near[0][j] + (1-float(b))*near[1][j] for j in range(2))
        nv, nz = math.sqrt(sum(x*x for x in v)), math.sqrt(sum(x*x for x in z))
        assert nv*nv >= 1-float(epsilon)-1e-14 and nz*nz >= 1-float(epsilon)-1e-14
        defect_max = max(defect_max, 1-sum(v[j]*z[j]/(nv*nz) for j in range(2)))
    check("upper_normalization_bound_sample", defect_max <= 8*float(epsilon)+1e-14,
          "25 convex pairs; epsilon=2/2501; bound=8epsilon")
    check("lower_normalization_constant", all(F(m)*F(1,2*m) == F(1,2) for m in range(1,9)),
          "eta=1/(2M), normalization at most M, for M=1,...,8")
    for r in (F(0),F(1,2),F(3,2),F(2),F(7,3)):
        n = 2*math.ceil(r)+1
        check("lower_series_R_"+str(r).replace("/","_"), F(n,2)>r,
              "N=2ceil(R)+1, each of the first N defects at least 1/2")
    finite_probabilities = (F(1,4),F(3,4))
    for values in ((F(1),F(3)),(F(0),F(4)),(F(2),F(2))):
        average = sum((a*b for a,b in zip(finite_probabilities,values)),F(0))
        assert min(values) <= average <= max(values)
    check("probability_average_witness", True,
          "three exact finite-probability examples; not a replacement for compact Haar proof")
    return {"schema":"eligible-kernel-finite-checks/v1", "scope":"finite algebra only",
            "count":len(rows), "all_passed":True, "checks":rows}


def draw(output, description):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib.patches import Arc, FancyArrowPatch, Rectangle
    from matplotlib.text import Text
    matplotlib.rcParams.update({"font.family":"DejaVu Sans", "font.size":12,
        "svg.fonttype":"none", "svg.hashsalt":"eligible-kernel-patching-v1",
        "mathtext.fontset":"dejavusans"})
    fig, axes = plt.subplots(2,2,figsize=(16,11),dpi=150)
    fig.patch.set_facecolor("#f6f8fa")
    blue, green, orange = "#135b93", "#176c4c", "#b35512"
    for ax in axes.flat:
        ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
        ax.add_patch(Rectangle((.01,.01),.98,.98,facecolor="white",edgecolor="#d4dce4",lw=1))

    def title(ax, text):
        ax.text(.045,.93,text,fontsize=15,fontweight="bold",color=blue)
    def arrow(ax,a,b,label="",color=blue,rad=0):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=14,
            linewidth=1.7,color=color,connectionstyle=f"arc3,rad={rad}"))
        if label:
            ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.035,label,ha="center",color=color)
    def box(ax,y,text):
        ax.add_patch(Rectangle((.08,y),.84,.10,facecolor="#eef5fb",edgecolor="#96b5ce"))
        ax.text(.5,y+.05,text,ha="center",va="center",fontsize=12)

    ax=axes[0,0]; title(ax,"A  Actual geometry and discrete labels")
    box(ax,.75,"N → M: compact oriented normal frames; complete Xᵢ")
    arrow(ax,(.5,.73),(.5,.66))
    box(ax,.54,"Closed local returns Cₓ: Euler products ⇒ local Lie")
    arrow(ax,(.5,.52),(.5,.45))
    box(ax,.33,"Q:N → W; actual foliated product Fw × V ≅ Q⁻¹(V)")
    ax.text(.08,.23,"D:O → GLm(ℝ),  D⁻¹dD = A,  λ:E|O → Λ discrete",color=green)
    ax.text(.08,.14,"τδ = D⁻¹δD extends on one O₀ for every admitted δ",color=green)
    ax.text(.08,.065,"Finite labels + compact endpoints ⇒ compact arrows (EG.8)",fontsize=11)

    ax=axes[0,1]; title(ax,"B  Common-source labels cancel exactly")
    x,y,z=(.14,.72),(.5,.72),(.86,.72)
    uj,uk,ui=(.14,.39),(.5,.39),(.86,.39)
    for point,label in zip((x,y,z,uj,uk,ui),("x = sh","y = rh = sg","z = rg","uj","uk","ui")):
        ax.plot(*point,"o",color=blue,markersize=5)
        label_y=point[1]+.055 if point[1]>.5 else point[1]-.065
        ax.text(point[0],label_y,label,ha="center",fontsize=11)
    arrow(ax,(.17,.72),(.46,.72),"h")
    arrow(ax,(.54,.72),(.83,.72),"g")
    for a,b,label in ((x,uj,"βj"),(y,uk,"βk"),(z,ui,"βi")):
        arrow(ax,(a[0],a[1]-.035),(b[0],b[1]+.04),color=green)
        ax.text(a[0]+.028,.55,label,color=green)
    arrow(ax,(.17,.39),(.46,.39),"ckj(h)",orange)
    arrow(ax,(.54,.39),(.83,.39),"δ = λ(βi g βk⁻¹)",orange)
    arrow(ax,(.17,.29),(.83,.29),color=orange,rad=.10)
    ax.text(.5,.165,"cij(gh) = λ(βi g h βj⁻¹)",ha="center",color=orange)
    ax.text(.5,.095,"cij(gh) ckj(h)⁻¹ = δ",ha="center",fontweight="bold")
    ax.text(.5,.04,"All h and j disappear from the tested label.  (EK.6)",ha="center",fontsize=11)

    ax=axes[1,0]; title(ax,"C  Bounded features survive convex patching")
    center=(.10,.16); scale=.55
    pt=lambda v:(center[0]+scale*v[0],center[1]+scale*v[1])
    ax.add_patch(Arc(center,2*scale,2*scale,theta1=0,theta2=90,
                     edgecolor="#bccbd8",lw=1.2))
    v0,v1,V,W=(1,0),(.6,.8),(.8,.4),(2/math.sqrt(5),1/math.sqrt(5))
    arrow(ax,center,pt(v0),color=blue); arrow(ax,center,pt(v1),color=blue)
    ax.plot([pt(v0)[0],pt(v1)[0]],[pt(v0)[1],pt(v1)[1]],color="#97a9b8",lw=2)
    arrow(ax,center,pt(W),color=green)
    for v,label,offset,color in ((v0,"v0=(1,0)",(.01,-.045),blue),
              (v1,"v1=(3/5,4/5)",(-.03,.03),blue),
              (V,"V=(4/5,2/5)",(-.15,-.08),orange),
              (W,"W=(2/√5,1/√5)",(.025,.015),green)):
        p=pt(v); ax.plot(*p,"o",color=color)
        ax.text(p[0]+offset[0],p[1]+offset[1],label,fontsize=11,color=color)
    ax.text(.66,.74,"Weights: 1/2, 1/2",fontsize=11)
    ax.text(.66,.66,"||V||² = 4/5 ≥ 1/2",fontsize=11)
    ax.text(.66,.58,"||W|| = 1",fontsize=11)
    ax.text(.08,.075,"General upper defect: 1 − Q(gh,h) ≤ 8ε (EK.7)",fontsize=11)
    ax.set_aspect("equal",adjustable="box")

    ax=axes[1,1]; title(ax,"D  Uniform lower control returns to G ⇒ T")
    ax.text(.08,.80,"kH(h,l) = Σn (1 − Qn(h,l)),   s(h)=s(l)",color=blue)
    ax.text(.08,.70,"Outside D(KH,N): Qn(gh,h) ≤ 1/2 for n ≤ N")
    ax.text(.08,.61,"Choose N/2 > R  ⇒  kH(gh,h) > R for every h",color=orange)
    arrow(ax,(.5,.56),(.5,.48))
    box(ax,.35,"kG(h,l) = ∫Px kH((h,u),(l,u)) dmx(u),  x=sh=sl")
    ax.text(.08,.26,"K ⊂ T compact ⇒ PK compact (proper frame anchor)",color=green)
    ax.text(.08,.17,"kG(gh,h) ≤ R ⇒ some u has lifted kH ≤ R",color=green)
    ax.text(.08,.075,"Increment (g,h·u) has endpoints in PK; project its compact set.",fontsize=11)
    fig.suptitle("Labelled holonomy kernels: actual paths, exact cancellation, compact control",
                 fontsize=18,fontweight="bold",y=.99,color=blue)
    fig.subplots_adjust(left=.025,right=.985,bottom=.025,top=.95,wspace=.035,hspace=.04)
    font_directory=Path(matplotlib.get_data_path())/"fonts"/"ttf"
    regular=FontProperties(fname=str(font_directory/"DejaVuSans.ttf"))
    bold=FontProperties(fname=str(font_directory/"DejaVuSans-Bold.ttf"))
    for label in fig.findobj(match=Text):
        properties=(bold if label.get_fontweight() in ("bold",700) else regular).copy()
        properties.set_size(label.get_fontsize())
        label.set_fontproperties(properties)
    fig.savefig(output/"eligible-kernel-patching.png",dpi=150,
                metadata={"Title":"Labelled holonomy kernel patching","Description":description,
                          "Software":"eligible-kernel-patching reproduction v1"})
    fig.savefig(output/"eligible-kernel-patching.svg",
                metadata={"Title":"Labelled holonomy kernel patching","Description":description,"Date":None})
    plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument("--checks-only",action="store_true")
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    checks=finite_checks()
    (args.output_dir/"finite-checks.json").write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8")
    data={"schema":"eligible-kernel-patching-data/v1","exact_features":{
        "v0":["1","0"],"v1":["3/5","4/5"],"V":["4/5","2/5"],
        "norm_V_squared":"4/5","W":["2/sqrt(5)","1/sqrt(5)"]},
        "cancellation":"cij(gh)*ckj(h)^(-1)=lambda(beta_i*g*beta_k^(-1))",
        "bounds":{"upper":"8epsilon","lower":"N/2>R","eta":"1/(2M)"},
        "geometry_panels":"typed schematics, not metric representations"}
    (args.output_dir/"eligible-kernel-patching-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    if not args.checks_only:
        terms=Path(__file__).with_name("COMPONENT-TERMS.md").read_text(encoding="utf-8")
        caption=("EG.5-EG.8, EK.2-EK.5. Features have the exact listed coordinates; "
                 "their positions are numerical renderings. Arrow and control panels are typed schematics.\n\n")
        draw(args.output_dir,caption+terms)
    print(json.dumps({"all_passed":checks["all_passed"],"finite_checks":checks["count"],
                      "figure_rendered":not args.checks_only}))


if __name__ == "__main__":
    main()
