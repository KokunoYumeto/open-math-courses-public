"""Exact lacunary weight and reflected polynomial limits, with editable labels."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT=Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
STEM="constant-strength-global-solvability-024"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,"svg.fonttype":"none",
    "svg.hashsalt":"AN02-GS-024","axes.titleweight":"bold","axes.spines.top":False,"axes.spines.right":False})
fig,(left,right)=plt.subplots(1,2,figsize=(20,10),dpi=120)
fig.subplots_adjust(left=.065,right=.96,bottom=.25,top=.77,wspace=.25)
fig.suptitle("Exact frequency windows and reflected adjoint limits",fontsize=27,weight="bold",y=.966)
fig.text(.5,.914,"The weight follows selected centers. The transpose reverses their shift.",fontsize=18,ha="center")
centers=np.array([3**j for j in range(1,7)],dtype=float)
xi=np.unique(np.r_[np.linspace(0,104,2601),centers[centers<=104],(centers[:-1]+centers[1:])/2])
xi=xi[(xi>=0)&(xi<=104)]
g=1+np.abs(xi[:,None]-centers).min(axis=1)
left.axvspan(79,83,color="#f3d8ad",zorder=0)
left.plot(xi,g,color="#216b93",lw=2.7)
left.scatter([3,9,27,81],[1,1,1,1],color="#216b93",s=55,zorder=5)
left.text(3,43,r"$g(\xi)=1+\mathrm{dist}(\xi,\{3^j:j\geq1\})$",fontsize=17)
left.text(3,38,"All powers gˢ are moderate, including s < 0.\nThe center set continues beyond this interval.",fontsize=15,linespacing=1.4)
left.annotate("Exact window around 81:\ng(81 + h) = 1 + |h| for |h| ≤ 2",xy=(81,3),xytext=(42,32),
    arrowprops={"arrowstyle":"->","color":"#9c5b20","lw":1.7},fontsize=15,color="#9c5b20")
for point,index in ((3,1),(9,2),(27,3),(81,4)):
    left.text(point,3.2,f"j={index}",fontsize=12,ha="center",color="#174b69")
left.set(xlim=(0,104),ylim=(0,46),xlabel=r"real frequency $\xi$",ylabel=r"lacunary weight base $g(\xi)$")
left.set_title("GS7-GS8: each center reads one power weight",fontsize=17,pad=20)
left.grid(alpha=.14)

freq=np.linspace(-4,4,1001)
palette=["#ad5727","#947e23","#367851","#216b93"]
for eta,color in zip((3,9,27,81),palette,strict=True):
    value=(-freq-eta-3)/np.sqrt((eta+3)**2+1)
    right.plot(freq,value,color=color,lw=2.4,label=rf"$\eta={eta}$")
right.axhline(-1,color="#323d47",lw=1.6,ls="--",label="limit: -1")
right.text(-3.8,-.03,r"$P(\xi)=\xi-3$,  $S_P(-\eta)=\sqrt{(\eta+3)^2+1}$",fontsize=16)
right.text(-3.8,-.18,r"$Q_\eta^t(\xi)=(-\xi-\eta-3)/S_P(-\eta)$",fontsize=17)
right.set(xlim=(-4,4),ylim=(-1.82,.12),xlabel=r"centered frequency $\xi$",ylabel=r"normalized transposed polynomial $Q_\eta^t(\xi)$")
right.set_title("GS4, GS16: use the reflected symbol weight",fontsize=17,pad=20)
right.legend(loc="lower left",ncol=2,framealpha=.95,fontsize=13)
right.grid(alpha=.14)
fig.text(.065,.121,"Left: an exact nearest-center weight on the displayed interval; later centers remain part of its definition.\n"
    "Right: exact affine polynomial graphs at four centers, converging to a nonzero scalar. Neither panel plots a solution or support.",
    fontsize=16,linespacing=1.5)
fig.text(.065,.043,"Original figure · Proof locators GS4, GS7-GS8, GS16, GS33-GS38 · GPT-6.1 Sol (OpenAI), Ultra · CC0",fontsize=13,color="#465361")
fig.savefig(OUT/f"{STEM}.png",dpi=120,metadata={"Software":"AN02 original deterministic mathematical figure"})
fig.savefig(OUT/f"{STEM}.svg",metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI), Ultra; CC0"})
plt.close(fig)
geometry={"schema":"exact-mathematical-figure/v1","left":{"center_set":"{3^j:integer j>=1}",
    "displayed_interval":[0,104],"displayed_centers":[3,9,27,81],"weight":"1+dist(xi,center_set)",
    "highlighted_closed_window":[79,83],"exact_window_profile":"g(81+h)=1+abs(h) for abs(h)<=2",
    "later_centers_omitted_from_definition":False,"next_center":243,"finite_renderer_centers":[3,9,27,81,243,729],
    "why_finite_renderer_is_exact":"For xi<=104 every omitted center is>=2187 and cannot beat the nearer included center81 or243."},
    "right":{"polynomial":"P(xi)=xi-3","full_norm_squared":"(xi-3)^2+1","reflected_normalization":"sqrt((eta+3)^2+1)",
        "transpose_polynomial":"(-xi-eta-3)/sqrt((eta+3)^2+1)","centers":[3,9,27,81],"coefficient_limit":-1,
        "displayed_frequency_interval":[-4,4],"graphs_are_exact_polynomials":True},
    "both_panels_are_solution_or_support_graphs":False,"proof_locators":["GS4","GS7-GS8","GS16","GS33-GS38"],
    "width":2400,"height":1200,"original_expression_license":"CC0-1.0","external_figure_reproduced":False}
(OUT/f"{STEM}.json").write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure":STEM,"width":2400,"height":1200,"exact_lacunary_centers":[3,9,27,81],"reflected_limit":-1}))
