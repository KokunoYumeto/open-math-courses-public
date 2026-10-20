"""Reproduce the exact full Euler division and Laurent-sector illustration."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"SNC-infinity-function-SI-v1"})
fig=plt.figure(figsize=(17,12),dpi=150,facecolor="#f5f8fc")
ink="#19334d";blue="#205e99";green="#18765f";muted="#53687f"
fig.text(.5,.956,"Actual infinite-order division and holomorphic SNC functions",
         ha="center",color=ink,fontsize=25)
fig.text(.5,.912,"A. Full coefficients; finitely many relation rows; SI.18–SI.26",
         ha="center",color=muted,fontsize=18)
ax=fig.add_axes([.055,.62,.89,.25]);ax.axis("off")
ax.add_patch(FancyBboxPatch((.01,.02),.98,.94,boxstyle="round,pad=.01",
                          fc="white",ec="#b7cbdc",lw=1.5))
ax.text(.5,.78,r"$P=R(P)+\sum_iQ_i(z_iD_iI-B_i)+\sum_jH_jD_{y_j}$",
        ha="center",color=blue,fontsize=23)
ax.text(.5,.47,r"$R(P)W=\sum_{I,n}c_{I,n}(z_{I^c},y)"
        r"\left(\prod_{i\in I}C_i(n_i)\right)z_I^{-n}W$",
        ha="center",color=ink,fontsize=23)
ax.text(.5,.17,r"$\Psi(gV)=\sum_{\nu=1}^{r}(P_{Zg})_\nu\otimes W_\nu$",
        ha="center",color=green,fontsize=23)
fig.text(.26,.568,"B. Integer Laurent exponents: exact negative sets",
         ha="center",color=muted,fontsize=17)
plot=fig.add_axes([.08,.17,.36,.34])
palette={():blue,(0,):"#ba6c28",(1,):green,(0,1):"#8660a9"}
for a in range(-4,5):
    for b in range(-4,5):
        I=tuple(i for i,v in enumerate([a,b])if v<0)
        plot.plot(a,b,"o",color=palette[I],ms=7)
plot.axvline(-.5,color="#7c8c9a",lw=1.5,ls="--")
plot.axhline(-.5,color="#7c8c9a",lw=1.5,ls="--")
plot.axvline(0,color="#c6d1dc",lw=.8)
plot.axhline(0,color="#c6d1dc",lw=.8)
plot.set_xlim(-4.7,4.7);plot.set_ylim(-4.7,4.7)
plot.set_xticks([-4,-2,0,2,4]);plot.set_yticks([-4,-2,0,2,4])
plot.set_xlabel(r"$z_1$ exponent");plot.set_ylabel(r"$z_2$ exponent")
plot.text(2.25,3.4,"I = empty",ha="center",color=blue)
plot.text(-2.5,3.4,"I = {1}",ha="center",color=palette[(0,)])
plot.text(2.25,-3.8,"I = {2}",ha="center",color=green)
plot.text(-2.5,-3.8,"I = {1,2}",ha="center",color=palette[(0,1)])
fig.text(.26,.10,"Finite sample: exponents −4,…,4 in each coordinate.",
         ha="center",color=muted,fontsize=14)
fig.text(.74,.568,"C. Nilpotent factorial and full positive head",
         ha="center",color=muted,fontsize=17)
right=fig.add_axes([.51,.13,.45,.39]);right.axis("off")
for y,text in [
 (.89,"A = [[1/3, 1], [0, 1/3]]"),
 (.68,"C(2) = [[10/9, −7/3], [0, 10/9]]"),
 (.47,"C(2)⁻¹ = [[9/10, 189/100], [0, 9/10]]")]:
    right.add_patch(FancyBboxPatch((.025,y-.095),.95,.15,
                   boxstyle="round,pad=.012",fc="white",ec="#b7cbdc"))
    right.text(.5,y-.016,text,ha="center",va="center",color=blue,fontsize=18)
right.text(.5,.20,r"$\sum_{n\geq0}\frac{(-1)^n}{(n!)^2}"
           r"D_z^n(1/z)=e^{1/z}/z$",ha="center",color=green,fontsize=22)
right.text(.5,.04,"All epsilon bounds and actual tensor inverse: SI.9–SI.26.",
           ha="center",color=muted,fontsize=14)
fig.text(.5,.05,"A and C are exact algebraic diagrams with no geometric scale. B samples an infinite integer partition.",
         ha="center",color=muted,fontsize=15)
fig.savefig(out/"snc-infinity-function.png",metadata={"Software":"Matplotlib"})
fig.savefig(out/"snc-infinity-function.svg",metadata={"Date":None})
plt.close(fig)
data={"normal_form":"SI.18","inverse":"SI.26","finite_relation_rows":"k+m",
      "Laurent_sample":{"range":[-4,4],"dimension":2,
                        "negative_set":"I={i: exponent_i<0}","zero_is_nonnegative":True},
      "A":[["1/3","1"],["0","1/3"]],
      "C2":[["10/9","-7/3"],["0","10/9"]],
      "C2_inverse":[["9/10","189/100"],["0","9/10"]],
      "full_head":"sum_n (-1)^n/(n!)^2 D_z^n(1/z)=exp(1/z)/z",
      "proof_tags":["SI.9","SI.16","SI.18","SI.25","SI.26","SI.35"],
      "human_source":"Kashiwara–Kawai HolIII II.2.2.4 and III.4.9",
      "general_singular_divisor_comparison_is_not_claimed":True}
(out/"snc-infinity-function-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
