"""Original exact bump/corner mechanism; deterministic native vector/raster output."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
E=Path(__file__).resolve().parent
OUT=E/"assets";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","svg.hashsalt":"oa-flow-cmc-20261005","font.size":18,"axes.unicode_minus":True})
fig=plt.figure(figsize=(16,11),dpi=200,facecolor="#f2f5f8")
navy="#18354c";teal="#087d9c";red="#b3422b";muted="#526d85"
fig.text(.04,.95,"Strong limits do not preserve an action's continuity",fontsize=32,weight="bold",color=navy)
fig.text(.04,.91,r"Exact $C_0(\mathbb{R})$ bumps in the universal representation, then two fixed matrix corners",fontsize=20,color=muted)
def panel(x,y,w,h,title):
    p=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.006,rounding_size=0.01",linewidth=1,edgecolor="#bccdda",facecolor="white",transform=fig.transFigure,zorder=-1)
    fig.patches.append(p);fig.text(x+.018,y+h-.046,title,fontsize=21,weight="bold",color=navy)
panel(.04,.52,.445,.33,"1  Bumps shrink; their strong limit survives")
panel(.525,.52,.435,.33,"2  A normal scalar test jumps")
panel(.04,.10,.445,.36,"3  The topology distinction is exact")
panel(.525,.10,.435,.36,"4  Two fixed corners encode a cocycle")
ax=fig.add_axes([.083,.625,.355,.145])
colors=["#087d9c","#b3422b","#7657a2"]
for n,c in zip([1,2,4],colors):
    ax.plot([-1/n,0,1/n],[0,1,0],color=c,lw=2.7,label=fr"$n={n}$")
ax.axhline(0,color=muted,lw=.8);ax.set_xlim(-1.2,1.2);ax.set_ylim(-.06,1.12)
ax.set_xlabel(r"$r$ (centre $s=0$)",fontsize=17);ax.set_ylabel(r"$f_{n,0}(r)$",fontsize=17);ax.legend(loc="upper right",fontsize=13,frameon=False)
ax.spines[["top","right"]].set_visible(False)
fig.text(.065,.537,r"$a_n=\pi(f_{n,0})\ \longrightarrow\ p_0$ strongly; $p_0\xi_0=\xi_0$",fontsize=18,color=teal)
bx=fig.add_axes([.575,.65,.33,.12])
bx.plot([-1.1,0],[0,0],color=teal,lw=3);bx.plot([0,1.1],[0,0],color=teal,lw=3)
bx.scatter([0],[0],s=100,facecolors="white",edgecolors=teal,lw=2.5,zorder=5)
bx.scatter([0],[1],s=120,color=red,zorder=5)
bx.set_xlim(-1.1,1.1);bx.set_ylim(-.12,1.15);bx.set_xticks([-1,0,1]);bx.set_yticks([0,1]);bx.set_xlabel(r"$t$",fontsize=17)
bx.spines[["top","right"]].set_visible(False)
fig.text(.55,.565,r"$\varepsilon_0(\theta_t(p_0))=\mathbf{1}_{\{0\}}(t)$",fontsize=22,color=red)
fig.text(.55,.535,"Every normal extension is forced to move the atom.",fontsize=15,color=muted)
fig.text(.067,.377,r"$\varepsilon_0(\theta_t(a_n))=\max(0,1-n|t|)$",fontsize=21,color=navy)
fig.text(.067,.325,r"For fixed $\xi_{1/3}$:  $\|(a_n-p_0)\xi_{1/3}\|$",fontsize=19,color=navy)
fig.text(.09,.280,r"$n=1,2,3,\ldots:\qquad 2/3,\ 1/3,\ 0,\ldots$",fontsize=21,color=teal)
fig.text(.067,.230,r"Moving test:  $f_{n,0}(1/(2n))=1/2$",fontsize=20,color=muted)
fig.text(.067,.170,r"$\|a_n-p_0\|=1$  for every $n$",fontsize=25,color=red)
fig.text(.067,.125,"No locally uniform limit of the translated scalar tests.",fontsize=15,color=muted)
grid=fig.add_axes([.555,.238,.37,.125]);grid.axis("off")
grid.set_xlim(0,2);grid.set_ylim(0,2)
for x,y,label in [
    (0,1,r"$\alpha_t(a)$"),
    (1,1,r"$\alpha_t(b)u_t^*$"),
    (0,0,r"$u_t\alpha_t(c)$"),
    (1,0,r"$u_t\alpha_t(d)u_t^*$")
]:
    box=FancyBboxPatch((x+.025,y+.025),.95,.95,boxstyle="round,pad=.01",facecolor="#eef5f8" if x+y==1 else "#ffffff",edgecolor="#9cb4c7",lw=1)
    grid.add_patch(box);grid.text(x+.5,y+.5,label,ha="center",va="center",fontsize=17,color=navy)
fig.text(.555,.380,r"$\gamma_t=\operatorname{Ad}\operatorname{diag}(1,u_t)\circ\alpha_t^{(2)}$",fontsize=18,color=navy)
fig.text(.55,.207,r"$e_{11},e_{22}$ fixed;  $v^*v=e_{11}$, $vv^*=e_{22}$",fontsize=18,color=teal)
fig.text(.55,.162,r"Corner actions:  $\alpha$ and $\alpha^u$",fontsize=21,color=navy)
fig.text(.55,.122,r"$\Gamma(\alpha)=\Gamma(\alpha^u)$ by the full fixed-corner theorem",fontsize=17,color=muted)
fig.text(.04,.055,"CM2–7 and M19–23: exact universal-representation obstruction. M1–11: arbitrary-LCA matrix transport.",fontsize=16,color=muted)
fig.text(.04,.027,"The right panel does not turn the discontinuous extension on the left into a continuous action.",fontsize=15,color=muted)
fig.savefig(OUT/"continuity-corners.png",dpi=200,metadata={"Software":"OA-FLOW original mathematical renderer"})
fig.savefig(OUT/"continuity-corners.svg",metadata={"Date":None,"Creator":"OA-FLOW original mathematical renderer"})
plt.close(fig)
data={
    "model":"Exact C0(R) translation/universal-representation model, plus separate general-LCA matrix construction",
    "bump_formula":"f_n,s(r)=max(0,1-n|r-s|)",
    "drawn_centre":"s=0",
    "bump_vertices":[{"n":n,"r":["-"+str(1)+"/"+str(n),"0",str(1)+"/"+str(n)],"values":[0,1,0]} for n in [1,2,4]],
    "strong_limit":"a_n,s=pi(f_n,s) -> p_s strongly; all n are positive contractions",
    "forced_extension":"theta_t(p_s)=p_(s+t)",
    "scalar_test":{"domain":"R","value_at_zero":1,"value_at_every_nonzero_t":0,"zero_point_on_baseline_excluded":True},
    "fixed_vector_check":{"vector":"xi_(1/3)","n":[1,2,3,4],"error":["2/3","1/3","0","0"]},
    "moving_test":{"r":"1/(2n)","value":"1/2","n_domain":"positive integers"},
    "operator_norm_error":"1 for every positive integer n",
    "cocycle":{"scope":"arbitrary LCH abelian G and arbitrary normal von Neumann action","identity":"u_(s+t)=u_s alpha_s(u_t)"},
    "corner_actions":{"e11":"alpha","e22":"Ad(u_t) alpha_t"},
    "connes_application_input":"Full accepted GCC equivalent-fixed-corner theorem; exact canonical preceding placement separately required",
    "negative_label_convention":"alpha_t(x)=conj(gamma(t))*x has label gamma",
    "domains_and_schematics":"The curves are exact piecewise-linear scalar graphs, not operator-norm graphs of the strong convergence; matrix panel is the actual block formula.",
    "PNG_dimensions":[3200,2200],
}
(OUT/"continuity-corners-data.json").write_text(json.dumps(data,indent=2)+"\n")
print(json.dumps({"assets":[p.name for p in sorted(OUT.iterdir())],"dimensions":[3200,2200]}))
