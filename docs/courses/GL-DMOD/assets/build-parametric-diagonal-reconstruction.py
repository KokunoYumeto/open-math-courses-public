"""Reproduce the actual diagonal reconstruction, normal slice and exact checks."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"parametric-diagonal-reconstruction-PD-v1"})
ink="#19334d";blue="#205e99";green="#18765f";orange="#ae632c";muted="#53687f"
fig=plt.figure(figsize=(18,15),dpi=150,facecolor="#f5f8fc")
fig.text(.5,.966,"Ordinary diagonal reconstruction with holomorphic parameters",
         ha="center",color=ink,fontsize=25)
fig.text(.5,.936,"A. Under the supplied SNC modification; PD.5, PD.22, PD.27–PD.34a",
         ha="center",color=muted,fontsize=18)
ax=fig.add_axes([.045,.69,.91,.225]);ax.axis("off")
ax.add_patch(FancyBboxPatch((.01,.02),.98,.94,boxstyle="round,pad=.01",
                          fc="white",ec="#b7cbdc",lw=1.5))
ax.text(.18,.75,r"$B_X\otimes_{\mathcal{D}_X}Q$",ha="center",color=blue,fontsize=25)
ax.text(.71,.75,r"$\delta^{-1}R\Gamma_\Delta\,\mathrm{DR}_y^0(Q^{[X]})[2n]$",
        ha="center",color=blue,fontsize=22)
ax.annotate("",(.43,.78),(.31,.78),arrowprops={"arrowstyle":"<->","color":blue,"lw":2})
ax.text(.18,.30,r"$Rj_*H=j_*H$",ha="center",color=green,fontsize=24)
ax.text(.71,.30,r"$\delta^{-1}R\Gamma_\Delta R\bar{j}_*F[2n]$",
        ha="center",color=green,fontsize=22)
ax.annotate("",(.43,.33),(.31,.33),arrowprops={"arrowstyle":"<->","color":green,"lw":2})
ax.annotate("",(.18,.47),(.18,.66),arrowprops={"arrowstyle":"->","color":green,"lw":2})
ax.text(.23,.53,r"$\Phi_Q$",color=green,fontsize=21)
ax.annotate("",(.71,.47),(.71,.66),arrowprops={"arrowstyle":"->","color":green,"lw":2})
ax.text(.71,.08,r"$r_n(-1)^n(-1)^{n^2}r_n=1,\qquad r_n=(-1)^{n(n-1)/2}$",
        ha="center",color=muted,fontsize=18)
fig.text(.25,.65,"B. Diagonal and input boundary: a real slice",ha="center",color=muted,fontsize=18)
plot=fig.add_axes([.08,.345,.36,.27])
t=np.linspace(-1,1,501)
plot.axhline(0,color=orange,lw=2,ls="--")
plot.plot(t[t<0],t[t<0],color=green,lw=3)
plot.plot(t[t>0],t[t>0],color=green,lw=3)
plot.scatter([0],[0],s=130,facecolor="white",edgecolor=orange,lw=2,zorder=5)
plot.text(.38,.74,r"$\Delta\cap W$",color=green,fontsize=20)
plot.text(-.94,.075,r"$y=0$ excluded from $W$",color=orange,fontsize=15)
plot.set_xlim(-1.05,1.05);plot.set_ylim(-1.05,1.05);plot.set_aspect("equal")
plot.set_xlabel(r"$\mathrm{Re}\,x$");plot.set_ylabel(r"$\mathrm{Re}\,y$")
plot.grid(alpha=.18)
fig.text(.26,.292,"Im x = Im y = 0; equal axis scale.",ha="center",color=muted,fontsize=15)
fig.text(.26,.272,"Full normal w = y - x is complex (real dimension 2).",ha="center",color=muted,fontsize=14)
fig.text(.73,.65,"C. Left ideals need not be two-sided; PD.39–PD.47",ha="center",color=muted,fontsize=17)
right=fig.add_axes([.48,.30,.48,.32]);right.axis("off")
rows=[
 ("S = [[0, 1], [1, 0]]",.87),
 ("T = [[0, -1], [1, -1]]",.72),
 (r"$S^2=I,\quad T^3=I,\quad STS=T^2$",.52),
 (r"$v_0=(1,0)^{\mathsf{t}},\quad (S-T)v_0=0$",.31),
 (r"$(S-T)Sv_0=(2,1)^{\mathsf{t}}\ne0$",.10)]
for text,y in rows:
 right.text(.5,y,text,ha="center",color=blue if y>.6 else green,fontsize=21)
fig.text(.73,.272,"Cyclic nonabelian representation; exact integer matrices.",ha="center",color=muted,fontsize=14)
fig.text(.5,.237,"D. Absolute degrees in the derived diagonal; PD.5 and PD.51–PD.54",
         ha="center",color=muted,fontsize=18)
tab=fig.add_axes([.08,.10,.84,.11]);tab.axis("off")
cell=[
 ["free operator module", "n", "n (holomorphic)", "0", r"$B_X$"],
 ["flat trivial bundle", "0", "2n (real normal)", "0", r"$\mathcal{O}_X$"],
 ["point module", "n", "n (holomorphic)", "0", r"$\mathcal{H}^n_{\{0\}}(\mathcal{O}_X)$"]]
table=tab.table(cellText=cell,colLabels=["input","relative degree","support degree","after [2n]","output"],
                loc="center",cellLoc="center",colWidths=[.25,.17,.25,.15,.18])
table.auto_set_font_size(False);table.set_fontsize(15);table.scale(1,1.8)
for (i,j),c in table.get_celld().items():
 c.set_edgecolor("#b7cbdc");c.set_facecolor("#e7f0fa"if i==0 else "white")
 c.set_text_props(color=ink)
fig.text(.5,.05,r"$\sum_{\nu\geq0}\frac{(-1)^\nu}{(\nu!)^2}"
         r"\partial_x^\nu e_0\ \longmapsto\ [e^{1/x}/x]$  (PD.57)",
         ha="center",color=green,fontsize=22)
fig.savefig(out/"parametric-diagonal-reconstruction.png",dpi=150)
fig.savefig(out/"parametric-diagonal-reconstruction.svg",metadata={"Date":None})
plt.close(fig)
data={"formula":"B_X tensor_D Q = delta^-1 R Gamma_Delta DR_y^0(Q^[X])[2n] = Rj_*H",
 "scope":"D-type and a supplied proper locally projective SNC modification",
 "normal":{"coordinate":"w=y-x","complex_dimension":1,"real_dimension":2,
 "real_slice":"Im x=Im y=0","plotted_range":[-1,1],"equal_axis_scale":True,
 "W":"X times (Y minus 0)","diagonal_intersection":"x=y, y nonzero"},
 "sign":{"rn":"(-1)^(n(n-1)/2)","cube":"rn*(-1)^n","shift":"(-1)^(n^2)",
 "orientation":"rn","product":1},
 "nonabelian":{"S":[[0,1],[1,0]],"T":[[0,-1],[1,-1]],"v0":[1,0],
 "left_ideal_element":"S-T","right_product_defect":[2,1]},
 "absolute_degrees":[{"input":"free","relative":"n","support":"n","after_shift":0},
 {"input":"flat","relative":0,"support":"2n","after_shift":0},
 {"input":"point","relative":"n","support":"n","after_shift":0}],
 "point_head":"sum (-1)^nu/(nu!)^2 D^nu e0 -> [exp(1/x)/x]",
 "proof_locators":["PD.5","PD.22","PD.27–PD.34a","PD.39–PD.47","PD.51–PD.57"]}
(out/"parametric-diagonal-reconstruction-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
