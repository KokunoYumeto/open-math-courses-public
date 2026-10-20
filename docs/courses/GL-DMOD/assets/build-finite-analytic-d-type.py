"""Reproduce the transfer diagram and exact ramified nilpotent example."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"finite-analytic-D-type-DT-v1"})
fig=plt.figure(figsize=(17,12),dpi=150,facecolor="#f4f8fc")
ink="#1a344e";blue="#205f99";green="#16765f";muted="#52677f"
fig.text(.5,.955,"Finite analytic transfer and ramified logarithmic images",
         ha="center",color=ink,fontsize=25)
fig.text(.5,.915,"A. Boundary localization makes the Jacobian invertible; DT.8–DT.18",
         ha="center",color=muted,fontsize=18)
ax=fig.add_axes([.055,.62,.89,.25]);ax.axis("off")
ax.add_patch(FancyBboxPatch((.01,.02),.98,.94,boxstyle="round,pad=.01",
                          fc="white",ec="#b6cbdc",lw=1.5))
ax.text(.5,.79,r"$K^{-n}\ \longrightarrow\ \cdots\ \longrightarrow\ K^0"
        r"\ \longrightarrow\ M$",ha="center",va="center",color=blue,fontsize=25)
ax.text(.5,.51,r"$\eta\otimes P\otimes m\ \longmapsto\ P(f,\nabla_V)(m/J)$",
        ha="center",va="center",color=ink,fontsize=23)
ax.text(.5,.24,r"$f_+M\simeq Rf_*M\simeq (f_*E_\Sigma)(*S)$",
        ha="center",va="center",color=green,fontsize=23)
fig.text(.25,.568,r"B. Exact real slice $t=w^3$",ha="center",color=muted,fontsize=18)
plot=fig.add_axes([.085,.205,.36,.31])
ws=np.linspace(-1,1,501)
plot.plot(ws,ws**3,color=blue,lw=2.8)
plot.axhline(0,color="#aab7c4",lw=1)
plot.axvline(0,color="#aab7c4",lw=1)
plot.set_xlim(-1.06,1.06);plot.set_ylim(-1.06,1.06)
plot.set_xticks([-1,0,1]);plot.set_yticks([-1,0,1])
plot.set_xlabel(r"source $w$");plot.set_ylabel(r"target $t$")
plot.plot([0],[0],"o",color=green)
plot.grid(alpha=.15)
fig.text(.25,.14,r"$J=3w^2$; invert $w$ in the transfer.",
         ha="center",color=ink,fontsize=16)
fig.text(.25,.105,"The full complex map has three sheets off zero.",
         ha="center",color=muted,fontsize=14)
fig.text(.73,.568,"C. Full Jordan blocks in the target; DT.20",
         ha="center",color=muted,fontsize=18)
res=fig.add_axes([.52,.18,.43,.36]);res.axis("off")
res.text(.5,.88,"Source residue: [[2/5, 1], [0, 2/5]]",
         ha="center",color=ink,fontsize=18)
for k,(val,num)in enumerate([("2/15",2),("7/15",7),("12/15",12)]):
    y=.65-k*.205
    res.add_patch(FancyBboxPatch((.10,y-.09),.80,.15,
                  boxstyle="round,pad=.016",fc="white",ec="#b6cbdc"))
    res.text(.5,y-.012,f"j={k}:  [[{val}, 1/3], [0, {val}]]",
             ha="center",va="center",color=blue,fontsize=18)
res.text(.5,-.02,"Source rank 2; target rank 6; nilpotent entries survive.",
         ha="center",color=green,fontsize=15)
fig.text(.5,.05,"A and C are exact algebraic diagrams with no geometric scale. B is the stated real slice.",
         ha="center",color=muted,fontsize=15)
fig.savefig(out/"finite-analytic-d-type.png",metadata={"Software":"Matplotlib"})
fig.savefig(out/"finite-analytic-d-type.svg",metadata={"Date":None})
plt.close(fig)
data={"complex_map":"t=w^3","real_slice":{"w_interval":["-1","1"],"t":"w^3"},
      "Jacobian":"3*w^2","density":"m/J","transfer":"DT.10–DT.14",
      "proper_image":"DT.16–DT.18","source_rank":2,"target_rank":6,
      "source_residue":[["2/5","1"],["0","2/5"]],
      "target_residues":[[[q,"1/3"],["0",q]]for q in ["2/15","7/15","12/15"]],
      "residue_formula":"(A+j*I)/e","e":3,"j":[0,1,2],
      "human_source":"Kashiwara–Kawai HolIII II.2–II.3 pp.863–865",
      "analytic_log_resolution_existence_is_not_asserted":True}
(out/"finite-analytic-d-type-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
