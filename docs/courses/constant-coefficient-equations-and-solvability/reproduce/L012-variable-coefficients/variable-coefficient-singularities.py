"""Original reproducible coefficient diagrams; CC0-1.0, GPT-6.1 Sol (OpenAI)."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
OUT=HERE/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                     "svg.fonttype":"none","svg.hashsalt":"variable-coefficient-singularities",
                     "axes.spines.top":False,
                     "axes.spines.right":False})
x=np.linspace(-3,3,1201)
a=np.zeros_like(x)
mask=np.abs(x)>1
a[mask]=np.exp(-1/(x[mask]**2-1))
assert np.all(a[~mask]==0) and np.all((a[mask]>0)&(a[mask]<1))
fig,axes=plt.subplots(2,1,figsize=(11,8.2),layout="constrained")
ink="#174566";red="#a52a3a"
ax=axes[0]
ax.plot(x,a,color=ink,lw=2.6)
ax.axvspan(-1,1,color=red,alpha=.11)
ax.scatter([0],[0],color=red,s=50,zorder=5)
ax.annotate(r"target singularity $\delta_0$",xy=(0,0),xytext=(.25,.42),
            arrowprops={"arrowstyle":"->","color":red},color=red)
ax.set_title("A compact interval of zeros",loc="left",weight="bold")
ax.set_ylabel(r"$a_0(x)$")
ax.set_xlim(-3,3);ax.set_ylim(-.12,1.1)
ax.set_xticks(range(-3,4))
ax.set_xlabel(r"$P_0u=a_0u$: every image vanishes on $(-1,1)$")
ax.text(.02,.91,r"hidden singularities stay in $K'=K\cup[-1,1]$",
        transform=ax.transAxes,va="top",bbox={"facecolor":"white","edgecolor":"none","alpha":.97,"pad":3})
ax.text(.02,.78,r"$a_0=0$ for $|x|\leq1$;  $a_0=e^{-1/(x^2-1)}$ for $|x|>1$",
        transform=ax.transAxes,va="top",bbox={"facecolor":"white","edgecolor":"none","alpha":.97,"pad":3})
ax.grid(axis="x",alpha=.14)
ax=axes[1]
ax.plot(x,np.sin(np.pi*x),color=ink,lw=2.4)
integers=np.arange(-3,4)
ax.scatter(integers,np.zeros_like(integers),color=red,s=40,zorder=5)
for j in integers:
    ax.vlines(j,-.1,.22,color=red,lw=1.2,alpha=.8)
ax.set_title("Unbounded isolated zeros",loc="left",weight="bold")
ax.set_ylabel(r"$\sin(\pi x)$")
ax.set_xlim(-3,3);ax.set_ylim(-1.35,1.65)
ax.set_xticks(range(-3,4));ax.set_yticks([-1,0,1])
ax.text(.02,.95,r"$P_1u=\sin(\pi x)u'$;  $P_1^t\delta_j=0$ for every $j\in\mathbb{Z}$",
        transform=ax.transAxes,va="top")
ax.set_xlabel("Marked points show Dirac supports; the integer family continues over the whole line.")
ax.grid(axis="x",alpha=.14)
fig.savefig(OUT/"variable-coefficient-singularities.png",dpi=150,
            metadata={"Software":"Matplotlib; original diagram GPT-6.1 Sol (OpenAI)"})
fig.savefig(OUT/"variable-coefficient-singularities.svg",
            metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI)"})
plt.close(fig)
data={"title":"Compact zero regions and isolated zeros",
      "displayed_x_interval":[-3,3],"displayed_integer_supports":list(map(int,integers)),
      "flat_coefficient":{"formula":"0 if |x|<=1; exp(-1/(x^2-1)) otherwise",
                          "exact_zero_set":[-1,1],"target":"Dirac at0",
                          "compact_bound":"K union [-1,1]",
                          "range_obstruction":"Every image is zero on the open interval(-1,1)."},
      "oscillating_coefficient":{"formula":"sin(pi*x)","exact_zero_set":"all integers",
                                 "operator":"sin(pi*x) d/dx",
                                 "transpose":"-d/dx(sin(pi*x) v)",
                                 "point_kernels":"transpose delta_j=0 for every integerj"},
      "markers":"Schematic marks locate point supports,not distribution values.",
      "proofs":"Examples7.2-7.3 in Singular supports and arbitrary distribution data.",
      "authorship":"GPT-6.1 Sol (OpenAI),Ultra,October2026","license":"CC0-1.0"}
(HERE/"variable-coefficient-singularities.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","files":[str(OUT/"variable-coefficient-singularities.png"),
    str(OUT/"variable-coefficient-singularities.svg")],"mathematical_samples":len(x)}))
