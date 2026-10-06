"""Original CC0 scalar examples; all displayed estimates are exact formulae."""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/"assets"; ASSETS.mkdir(exist_ok=True)
plt.rcParams.update({"font.size":14, "mathtext.fontset":"dejavusans","svg.hashsalt":"oa-flow-scalar-convergence-v1"})
x=np.linspace(0,1,1201)
fig,axs=plt.subplots(1,2,figsize=(14,5.5))
colors=["#157a8c","#c5543d","#8064a2"]
left=axs[0]
left.plot(x,np.ones_like(x),color="#64748b",ls="--",lw=1.7,label=r"$g=1$")
for n,c in zip([3,7,15],colors):
 left.plot(x,x**n,color=c,lw=2.4,label=rf"$n={n}$: $\|u_n\|_1=1/{n+1}$")
left.fill_between(x,0,x**3,color=colors[0],alpha=.11)
left.set_title(r"Domination: $u_n(x)=x^n$",pad=15)
left.text(.05,.68,r"$h_n=\sup_{k\geq n}|u_k|=x^n$"+"\n"+r"$h_n\downarrow0$ a.e.; $\int h_n=1/(n+1)$",
          fontsize=13,ha="left",va="center",bbox={"facecolor":"white","alpha":.9,"edgecolor":"#cbd5e1"})
left.scatter([1],[1],color="#1f2937",zorder=10,s=24)
left.annotate("one null exception",xy=(1,1),xytext=(.56,1.11),
              fontsize=12,arrowprops={"arrowstyle":"->","color":"#475569"})
right=axs[1]
right.plot(x,x,color="#1f2937",lw=2.6,label=r"limit $F(x)=x$")
for n,c in zip([1,2,3],colors):
 right.plot(x,(1-2**(-n))*x,color=c,lw=2.4,label=rf"$F_{n}=(1-2^{{-{n}}})x$")
right.fill_between(x,(1-2**(-3))*x,x,color=colors[2],alpha=.18)
right.set_title(r"Summable differences: $d_j(x)=2^{-j}x$",pad=15)
right.text(.045,.75,r"$F-F_N=2^{-N}x$"+"\n"+r"$\|F-F_N\|_p=2^{-N}(p+1)^{-1/p}$"+"\n"+r"$1\leq p<\infty$",
           fontsize=13,ha="left",va="center",bbox={"facecolor":"white","alpha":.91,"edgecolor":"#cbd5e1"})
for ax in axs:
 ax.set_xlim(0,1.025); ax.set_ylim(0,1.21); ax.set_xlabel(r"$x\in[0,1]$"); ax.set_ylabel("function value")
 ax.set_xticks([0,.25,.5,.75,1]); ax.set_yticks([0,.25,.5,.75,1])
 ax.grid(alpha=.16); ax.legend(loc="lower right",framealpha=.94,fontsize=12)
 ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
fig.suptitle("Two scalar examples on [0,1] with Lebesgue measure",fontsize=19,y=.98)
fig.text(.5,.017,"SC-05: decreasing integrable envelopes       •       SC-07: norm control by summable tails",ha="center",fontsize=12)
fig.subplots_adjust(left=.062,right=.98,bottom=.15,top=.81,wspace=.23)
fig.savefig(ASSETS/"scalar-convergence.png",dpi=180)
fig.savefig(ASSETS/"scalar-convergence.svg",metadata={"Date":None,"Creator":"Original CC0 scalar-convergence figure source"})
plt.close(fig)
data={"rights":"CC0-1.0 original figure and code only",
      "domain":{"interval":[0,1],"measure":"Lebesgue; interval length normalization SC-02"},
      "domination":{"formula":"u_n(x)=x^n","n":[3,7,15],"integrals":[str(Fraction(1,n+1)) for n in [3,7,15]],
                    "tail_envelope":"x^n","null_exception":[1],"a_e_limit":0},
      "summable_differences":{"d_j":"2^(-j)x, j>=1","F_N":"(1-2^(-N))x","N":[1,2,3],
                   "norm_error":"2^(-N)(p+1)^(-1/p), 1<=p<infinity","shaded_N":3},
      "sources":[{"url":"https://measure.axler.net/MIRA.pdf","locators":["3.11","7.20"]}],
      "sampling":"1201 evenly spaced x-values only for rendering; no numerical estimate used in proofs",
      "blender":"Not useful for these planar scalar function graphs"}
(ASSETS/"figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
sourceimages=ROOT/"sources"/"rendered"; sourceimages.mkdir(parents=True,exist_ok=True)
for name,pages in [("axler-mira",[93,211,219]),("lebl-basic-analysis-I",[159,204])]:
 source=ROOT/"sources"/(name+".pdf")
 if not source.is_file():
  continue
 import fitz
 pdf=fitz.open(source)
 for n in pages:
  pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(sourceimages/(name+f"-pdf-{n}.png"))
print("Rendered original 2520x990 figure. Comparison-source page rendering is optional when private PDFs are present.")
