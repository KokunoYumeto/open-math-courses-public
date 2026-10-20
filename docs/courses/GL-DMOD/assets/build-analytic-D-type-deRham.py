"""Reproduce the finite-transfer comparison and exact cusp incidence figure."""
from pathlib import Path
import argparse, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"analytic-D-type-deRham-AD-v1"})
ink="#19334d";blue="#205e99";green="#18765f";muted="#53687f"
fig=plt.figure(figsize=(18,13),dpi=150,facecolor="#f5f8fc")
fig.text(.5,.962,"Analytic transfer and the singular-divisor de Rham comparison",
         ha="center",color=ink,fontsize=25)
fig.text(.5,.926,"A. Finite transfer and canonical restriction; AD.5, AD.22–AD.26",
         ha="center",color=muted,fontsize=18)
ax=fig.add_axes([.045,.68,.91,.225]);ax.axis("off")
ax.add_patch(FancyBboxPatch((.01,.02),.98,.94,boxstyle="round,pad=.01",
                          fc="white",ec="#b7cbdc",lw=1.5))
ax.text(.5,.82,r"$T_f\otimes^L_{f^{-1}\mathcal{D}_X} f^{-1}\mathcal{O}_X"
        r"\ \simeq\ \mathcal{O}_Z,\qquad a\otimes P\ \mapsto\ a\,f^*(P1)$",
        ha="center",color=blue,fontsize=22)
ax.text(.12,.49,r"$\mathrm{DR}_X(N)$",ha="center",color=ink,fontsize=23)
ax.text(.76,.49,r"$Rf_*\mathrm{DR}_Z(M)$",ha="center",color=ink,fontsize=23)
ax.annotate("",(.55,.52),(.27,.52),arrowprops={"arrowstyle":"->","color":blue,"lw":2})
ax.text(.41,.57,r"$\theta$",ha="center",color=blue,fontsize=21)
ax.text(.12,.13,r"$Rj_*L_X[n]$",ha="center",color=green,fontsize=23)
ax.text(.76,.13,r"$Rf_*Rj_{Z,*}L_Z[n]$",ha="center",color=green,fontsize=23)
ax.annotate("",(.12,.28),(.12,.45),arrowprops={"arrowstyle":"->","color":green,"lw":2})
ax.text(.17,.34,r"$c_N$",color=green,fontsize=19)
ax.annotate("",(.76,.28),(.76,.45),arrowprops={"arrowstyle":"->","color":green,"lw":2})
ax.annotate("",(.53,.16),(.27,.16),arrowprops={"arrowstyle":"<->","color":green,"lw":2})
fig.text(.24,.642,"B. The real cusp; exact parametrization",ha="center",color=muted,fontsize=17)
plot=fig.add_axes([.075,.265,.32,.34])
t=np.linspace(-1,1,801)
plot.plot(t*t,t*t*t,color=blue,lw=3)
plot.axhline(0,color="#9aaaba",lw=.8);plot.axvline(0,color="#9aaaba",lw=.8)
plot.set_xlim(-.15,1.15);plot.set_ylim(-1.12,1.12);plot.set_aspect("equal",adjustable="box")
plot.set_xlabel(r"$x$");plot.set_ylabel(r"$y$")
plot.grid(alpha=.18)
plot.set_title(r"$y^2=x^3,\quad (x,y)=(t^2,t^3)$",fontsize=17,color=ink)
fig.text(.24,.205,r"$-1\leq t\leq1$; equal axis scale",ha="center",color=muted,fontsize=15)
fig.text(.72,.642,"C. Final incidence and multiplicities; AD.32–AD.33",ha="center",color=muted,fontsize=17)
graph=fig.add_axes([.46,.25,.50,.35]);graph.axis("off")
pos={"E1":(.14,.65),"E3":(.5,.50),"E2":(.86,.65),"C":(.5,.05)}
for key in ["E1","E2","C"]:
 graph.plot([pos["E3"][0],pos[key][0]],[pos["E3"][1],pos[key][1]],color="#72899e",lw=2,zorder=1)
for key,label in [("E1",r"$E_1:\ 2$"),("E2",r"$E_2:\ 3$"),("E3",r"$E_3:\ 6$"),("C",r"$C':\ 1$")]:
 x,y=pos[key];graph.scatter([x],[y],s=1200,color="#e3edf8",edgecolor=blue,zorder=2)
 graph.text(x+.14 if key=="C" else x,y if key=="C" else y+.13,label,ha="center",color=ink,fontsize=20,zorder=3)
graph.text(.29,.62,r"$q=\infty$",ha="center",color=green,fontsize=17)
graph.text(.72,.62,r"$q=0$",ha="center",color=green,fontsize=17)
graph.text(.58,.29,r"$q=1$",ha="center",color=green,fontsize=17)
graph.set_xlim(0,1);graph.set_ylim(-.12,.95)
fig.text(.72,.205,"Orders of f* h. Incidence only; no metric scale.",ha="center",color=muted,fontsize=15)
bottom=fig.add_axes([.07,.065,.86,.115]);bottom.axis("off")
bottom.add_patch(FancyBboxPatch((.01,.02),.98,.94,boxstyle="round,pad=.01",
                              fc="white",ec="#b7cbdc",lw=1.5))
bottom.text(.5,.69,r"$x=p^2q,\quad y=p^3q^2,\quad f^*h=p^6q^3(q-1),\quad J=p^4q^2$",
            ha="center",color=blue,fontsize=23)
bottom.text(.5,.25,r"$f^*(dx\wedge dy)=J\,dp\wedge dq,"
            r"\qquad dp\wedge dq\otimes m\ \mapsto\ dx\wedge dy\otimes(m/J)$",
            ha="center",color=green,fontsize=21)
fig.savefig(out/"analytic-D-type-deRham.png",dpi=150)
fig.savefig(out/"analytic-D-type-deRham.svg",metadata={"Date":None})
plt.close(fig)
data={"normalization":"DR^0[n], differential multiplied by (-1)^n",
 "transfer":"T_f derived-tensor f^-1 O_X -> O_Z; a tensor P maps to a f*(P1)",
 "canonical_comparison":"DR_X N -> Rf_* DR_Z M -> Rj_* L_X[n]",
 "cusp":{"equation":"y^2-x^3","real_parameter":["t^2","t^3"],"t_interval":[-1,1],"equal_axis_scale":True},
 "final_chart":{"map":["p^2*q","p^3*q^2"],"h":"p^6*q^3*(q-1)","J":"p^4*q^2"},
 "other_chart":{"map":["a*b^2","a*b^3"],"h":"a^2*b^6*(1-a)","J":"a*b^4"},
 "boundary_orders":{"E1":2,"E2":3,"E3":6,"strict_cusp":1},
 "E3_intersections":{"E1":"infinity","E2":"0","strict_cusp":"1"},
 "graph_has_metric_scale":False,"proof_locators":["AD.5","AD.22–AD.28a","AD.29–AD.35"]}
(out/"analytic-D-type-deRham-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
