"""Reproducible schematic of the actual finite-order Ext proof.

No geometry is numerically sampled. The right panel is the exact integer
illustration d=2, n=3, m=5, q=5 of EC.C4, EC.D7 and EC.E1--EC.E5.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path)
args=parser.parse_args()
out = args.output_dir.resolve() if args.output_dir else root
out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "mathtext.fontset": "dejavusans",
                     "svg.hashsalt": "actual-analytic-micro-ext-EC-20261010"})
fig = plt.figure(figsize=(15, 10), dpi=160, facecolor="#fbfcfe")
fig.text(.04, .952, "Actual finite-order microlocal Ext: the proof mechanism",
         fontsize=23, weight="bold", color="#153b55")
fig.text(.04, .908, "The analytic commutative proof EC.A is included. All arrows use actual finite modules and finite witnesses.",
         fontsize=14, color="#294c68")

def panel(rect, title):
    ax = fig.add_axes(rect)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.add_patch(FancyBboxPatch((.01, .01), .98, .97, boxstyle="round,pad=.008",
                              linewidth=1.4, edgecolor="#58758d", facecolor="#f1f6fa"))
    ax.text(.07, .88, title, fontsize=17, weight="bold", color="#153b55")
    return ax

left = panel([.035, .415, .455, .43], "1. One actual boundary lift")
left.text(.065, .79, r"$H^j=\mathrm{Ext}_{A}^{j}(M_0,A)$,   $A=E_0$", fontsize=19)
left.text(.065, .66, r"$H^j/H^jh\ \hookrightarrow\ \mathrm{Ext}_{R}^{j}(\bar M_0,R)$", fontsize=20)
left.text(.065, .53, r"$\bar z=d\bar y\ \Longrightarrow\ z-dy=wh$", fontsize=18)
left.text(.065, .41, r"$0=d(wh)=(dw)h\ \Longrightarrow\ dw=0$", fontsize=18)
left.text(.065, .29, r"$[z]=[w]h$: the kernel is exactly $H^jh$.", fontsize=16)
left.text(.065, .15, "If the right-hand Ext is zero, finite right\nNakayama gives $H^j=0$ at that stalk.",
          fontsize=14, linespacing=1.5)

lower = panel([.035, .115, .455, .275], "2. Rank and the support bound")
lower.text(.065, .715, r"$\Pi=\sum_i\partial_{z_i}\wedge(\partial_{x_i}-z_i\partial_t)$", fontsize=19)
lower.text(.065, .52, r"$\mathrm{rank}\,\Pi=2d$,  $\ker\Pi=\langle dt+\sum_i z_i\,dx_i\rangle$", fontsize=16)
lower.text(.065, .30, r"$\dim U\leq d+1\quad\Rightarrow\quad\dim\mathrm{Supp}\,V\geq d$", fontsize=18)
lower.text(.065, .12, "U is the conormal at a smooth support point (EC.D7).", fontsize=12)

right = panel([.52, .115, .445, .73], "3. The exact degree comparison")
right.text(.065, .805, r"Illustration: $d=2$, $n=d+1=3$, $m=2d+1=5$", fontsize=16)
right.text(.065, .705, r"Lagrangian normalized support: dimension $d=2$", fontsize=15)
right.text(.065, .635, r"Its commutative codimension: $m-d=3=n$", fontsize=15)
right.text(.065, .535, r"For $j<3$: EC.A and the injection give zero.", fontsize=15)
right.text(.065, .44, r"For $j=4$: $m-j=1<2=d$, so EC.D7 gives zero.", fontsize=15)
right.text(.065, .355, r"Every $j>3$ has the same strict contradiction.", fontsize=15)
right.text(.065, .26, r"Only $\mathrm{Ext}^{3}_{E}(M,E)$ can remain.", fontsize=21, weight="bold", color="#153b55")
right.text(.065, .155, r"General degree: $r=n=\dim_{\mathbf{C}}X$", fontsize=18)
right.text(.065, .07, r"$R\mathrm{Hom}_{E}(M,E)[n]$: a right module in degree $0$.", fontsize=15)

fig.text(.04, .051, "Exact proof locators: EC.C4–EC.C7, EC.D2–EC.D7, EC.E1–EC.E5. This is a schematic of finite",
         fontsize=12, color="#294c68")
fig.text(.04, .026, "module maps and dimension inequalities. It proves no infinite-coefficient depth or I23 section separation.",
         fontsize=12, color="#294c68")
fig.savefig(out / "actual-microlocal-ext-mechanism.png", dpi=160, facecolor=fig.get_facecolor())
fig.savefig(out / "actual-microlocal-ext-mechanism.svg", facecolor=fig.get_facecolor(),
            metadata={"Date": None, "Creator": "Open mathematics course proof schematic"})
plt.close(fig)
data = {
    "kind": "finite actual module-map and dimension schematic",
    "proof_locators": ["EC.C4--EC.C7", "EC.D2--EC.D7", "EC.E1--EC.E5"],
    "general_dimensions": {"base": "n=d+1", "contact": "m=2d+1", "holonomic_contact_support": "d"},
    "illustration": {"d": 2, "n": 3, "m": 5, "q": 5, "commutative_codimension": 3,
                     "j_test": 4, "j_test_upper_support_dimension": 1,
                     "minimum_nonzero_actual_support_dimension": 2},
    "principal_Hom_map": "Ext_A^j(M0,A)/Ext_A^j(M0,A)h injects Ext_R^j(M0/hM0,R)",
    "conormal_bound": "dim U <= d+1",
    "infinite_coefficient_depth_proved": False,
    "I23_proved": False,
    "commutative_analytic_premise": "EC.A; complete analytic proof AC.2--AC.15"
}
(out / "actual-microlocal-ext-mechanism-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print("Actual finite-order Ext schematic and exact data generated.")
