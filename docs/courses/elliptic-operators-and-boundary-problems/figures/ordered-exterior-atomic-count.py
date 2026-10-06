"""Exact U044 atomic pairing and complete n=2 exterior-word count.

Written and dedicated to the public domain by Codex, October 2026 (CC0).
Programme proofs: ordered-weyl-exterior-reduction.md, OE1--OE23.
"""
from pathlib import Path
import itertools, json, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans", "mathtext.fontset":"dejavusans",
                     "svg.hashsalt":"an03-u044-atomic-exterior-count-264"})
labels=["ξ₁","x₁","ξ₂","x₂"]
target=(0,3,2,1)
def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
rows=[]
for pairs in itertools.permutations(range(2)):
    for reverse in itertools.product([0,1],repeat=2):
        base=tuple(k for j,r in zip(pairs,reverse)
                   for k in ((2*j+1,2*j) if r else (2*j,2*j+1)))
        base_sign=(-1)**sum(reverse)
        assert base_sign==sign(base)
        perm=[None]*4
        for a,b in zip(base,target): perm[a]=b
        relabel_sign=sign(perm)
        assert base_sign*relabel_sign==sign(target)==-1
        rows.append({"base_coordinate_string":[labels[i] for i in base],
                     "base_sign":base_sign,"relabeling_sign":relabel_sign,
                     "target_sign":base_sign*relabel_sign})
assert len(rows)==2**2*math.factorial(2)==8

fig=plt.figure(figsize=(14,9),facecolor="white")
left=fig.add_axes([.035,.36,.43,.52]); left.axis("off")
right=fig.add_axes([.51,.36,.455,.52]); right.axis("off")
left.set(xlim=(0,1),ylim=(0,1))
def panel(y,h,title,body,colour):
    left.add_patch(FancyBboxPatch((.025,y),.95,h,boxstyle="round,pad=.018",
                                 facecolor=colour,edgecolor="#52677e",linewidth=1.3))
    left.text(.5,y+h-.035,title,ha="center",va="top",fontsize=14,weight="bold")
    left.text(.5,y+h/2-.025,body,ha="center",va="center",fontsize=12,linespacing=1.6)
panel(.54,.43,"The same atomic occurrence",
      r"$\partial_u\partial_v a=\partial_v\partial_u a$"+"\n"+
      "Swap the two coordinate labels in its derivative slots.\n"+
      "The matrix word stays in its exact order.\n"+
      "The alternating sign reverses; the paired terms sum to zero.",
      "#e9eff7")
panel(.055,.43,"An outer edge between scalar cutoff slots",
      r"$(\partial_u t)(\partial_v t)=(\partial_v t)(\partial_u t)$"+"\n"+
      "Once repeated derivatives are removed, the edges form a matching.\n"+
      "Swap this edge's two labels in the complete alternation.\n"+
      "The scalar product stays equal and its alternating sign reverses.",
      "#e6f2ea")
left.text(.5,-.055,"Only n first internal brackets and N−n scalar t factors remain.",
          ha="center",fontsize=11.5,color="#354d64")

right.set_title("All eight base words, n = 2",fontsize=16,pad=12)
table=right.table(cellText=[
    [" ".join(r["base_coordinate_string"]),
     "+" if r["base_sign"]==1 else "−",
     "+" if r["relabeling_sign"]==1 else "−","−"] for r in rows],
    colLabels=["Original label string","Base sign","Relabeling sign","Target sign"],
    colWidths=[.42,.17,.24,.17],cellLoc="center",
    bbox=[0,.15,1,.77])
table.auto_set_font_size(False); table.set_fontsize(11.5)
for (r,c),cell in table.get_celld().items():
    cell.set_edgecolor("#bac6d2"); cell.set_linewidth(.75)
    cell.set_facecolor("#dce7f4" if r==0 else ("#f2f6fa" if r%2 else "white"))
    if r==0: cell.set_text_props(weight="bold",fontsize=10.5)
right.text(.5,.04,"Fixed target: ξ₁ x₂ ξ₂ x₁; its exterior sign is −1.\n"+
           r"Matrix slots stay $b_{u_1}a_{u_2}b_{u_3}a_{u_4}$ in every row.",
           ha="center",va="center",fontsize=11.5,linespacing=1.45)
right.text(.5,-.055,r"Every target has $2^n n!$ exact preimages; here $2^2\,2!=8$.",
           ha="center",fontsize=12,color="#354d64")

bottom=fig.add_axes([.055,.095,.89,.205]); bottom.axis("off")
bottom.add_patch(FancyBboxPatch((.0,.0),1,1,boxstyle="round,pad=.012",
                                facecolor="#edf3f8",edgecolor="#466881",linewidth=1.4))
bottom.text(.5,.91,"The complete receiving coefficient in this example, n = 2 and N = 3",
            ha="center",va="top",fontsize=14,weight="bold")
bottom.text(.5,.61,r"$S^2\Omega=-6t\left((db\wedge da)^2-(da\wedge db)^2\right),"
            r"\qquad\widetilde{\Omega}=\Omega$",
            ha="center",fontsize=15)
bottom.text(.5,.36,r"$\operatorname{Tr}S^2\Omega=-12t\operatorname{Tr}(db\wedge da)^2$",
            ha="center",fontsize=15)
bottom.text(.5,.10,r"$A_2^{(3)}=(2\pi)^{-2}\frac{1}{4!}"
            r"\int\operatorname{Tr}S^2\Omega"
            r"=-\frac{1}{2}(2\pi)^{-2}\int t\operatorname{Tr}(db\wedge da)^2$",
            ha="center",fontsize=14.5)
fig.suptitle("Atomic cancellation and the exact exterior multiplicity",
             fontsize=21,y=.96)
fig.text(.5,.031,"Complete programme proof: OE3–OE12. Coordinates, matrix order, signs, factorials and Fourier factor are retained.",
         ha="center",fontsize=11)
fig.savefig(HERE/"ordered-exterior-atomic-count.png",dpi=240)
fig.savefig(HERE/"ordered-exterior-atomic-count.svg",
            metadata={"Date":None,"Creator":"Codex; reproducible CC0 programme proof diagram"})
(HERE/"ordered-exterior-atomic-count.parameters.json").write_text(json.dumps({
    "license":"CC0-1.0","proof_source":"Complete programme proof OE3--OE12.",
    "configuration_dimension":2,"error_power":3,
    "reference_coordinate_order":labels,"reference_orientation":"dx1^dxi1^dx2^dxi2",
    "tilde_orientation":"dxi1^dx1^dxi2^dx2",
    "tilde_to_reference_sign":1,"target_coordinate_string":[labels[i] for i in target],
    "target_sign":-1,"matrix_occurrence_order":["b","a","b","a"],
    "base_word_count":8,"base_words":rows,
    "all_dimensional_count":"2^n*n!",
    "raw_S2_coefficient":"n!*i^n*binomial(N,n)*t^(N-n)",
    "raw_example_coefficient":"-6*t",
    "traced_example_coefficient":"-12*t",
    "analytic_example_coefficient":"-(1/2)*(2*pi)^(-2)*t",
    "mathematical_status":"Exact finite differential identity; table is a full n=2 count, not a numerical matrix experiment."
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
plt.close(fig)
