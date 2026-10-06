"""Reproducible exact-geometry figure for equations 16-18. Original source: CC0."""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
OUT=Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
    "mathtext.fontset":"dejavusans","svg.fonttype":"none",
    "svg.hashsalt":"AN02-MX-boundary-derivative-023"})
fig,axes=plt.subplots(1,2,figsize=(13,6.8),gridspec_kw={"width_ratios":[1.1,1]})
fig.subplots_adjust(left=.07,right=.97,bottom=.21,top=.77,wspace=.33)
fig.suptitle("Point values can miss a transverse boundary derivative",fontsize=20,y=.96)
fig.text(.5,.88,r"$P=(D_t^2-D_a^2)^2,\quad B_1=1,\quad B_2=D_a+D_z,\quad f=\varphi=0$",
    fontsize=16,ha="center")
ax=axes[0]
ax.add_patch(Polygon([(-1,0),(3,0),(1,2)],closed=True,
    facecolor="#eef0f4",edgecolor="#525b68",linewidth=1.5,zorder=1))
ax.add_patch(Polygon([(0,0),(3,0),(1,2),(0,1)],closed=True,
    facecolor="#d5e8fa",edgecolor="#28699b",linewidth=1.8,zorder=2))
ax.axvline(0,color="#626b77",linestyle="--",linewidth=1.2,zorder=3)
ax.plot([0,3],[0,0],color="#28699b",linewidth=3,zorder=4)
ax.plot([0,0],[0,1],color="#c23a3a",linewidth=5,zorder=5)
ax.scatter([1],[2],s=70,color="#202733",zorder=6)
ax.annotate(r"$x=(1,0,2)$",xy=(1,2),xytext=(1.25,2.15),
    fontsize=14,arrowprops={"arrowstyle":"-","color":"#202733"})
ax.annotate(r"$R_x:\ a=z=0,\ 0\leq t\leq1$",xy=(0,.55),xytext=(-1.23,1.38),
    fontsize=12,color="#a22e2e",arrowprops={"arrowstyle":"->","color":"#a22e2e"})
ax.text(1.03,.64,r"$D_x\cap Q$",ha="center",fontsize=17,color="#1d547f")
ax.text(1.13,.28,r"$z=0$ everywhere",ha="center",fontsize=12,color="#1d547f")
ax.text(-.84,.19,"outside Q",rotation=65,fontsize=10,color="#626b77")
ax.set(xlim=(-1.3,3.4),ylim=(-.12,2.45),xlabel="normal coordinate a",ylabel="time t")
ax.set_xticks([-1,0,1,2,3]);ax.set_yticks([0,1,2])
ax.set_title("The effective backward sets lie in a plane",fontsize=14,pad=15)
ax.spines[["right","top"]].set_visible(False)
ax.set_aspect("equal",adjustable="box")
ax=axes[1]
zz=[-1.2,1.2]
ax.plot(zz,[v/math.e for v in zz],color="#7656a7",linewidth=3)
ax.axhline(0,color="#87909a",linewidth=.8)
ax.axvline(0,color="#87909a",linewidth=.8,linestyle="--")
ax.scatter([0],[0],s=60,color="#c23a3a",zorder=3)
ax.annotate(r"$g_1(0,1)=0$",xy=(0,0),xytext=(-1.12,.24),fontsize=14,
    arrowprops={"arrowstyle":"->","color":"#c23a3a"},color="#a22e2e")
ax.text(.2,.43,r"$g_1(z,1)=z/e$",fontsize=17,color="#65418e")
ax.annotate(r"$\partial_zg_1(0,1)=1/e$",xy=(.68,.68/math.e),
    xytext=(-.4,-.43),fontsize=15,color="#65418e",
    arrowprops={"arrowstyle":"->","color":"#65418e"})
ax.set(xlim=(-1.25,1.25),ylim=(-.52,.56),xlabel="transverse coordinate z",
    ylabel=r"boundary value $g_1(z,1)$")
ax.set_xticks([-1,0,1]);ax.set_yticks([-1/math.e,0,1/math.e])
ax.set_yticklabels([r"$-1/e$","0",r"$1/e$"])
ax.set_title("The transverse derivative survives",fontsize=14,pad=15)
ax.spines[["right","top"]].set_visible(False)
fig.text(.5,.105,r"$u(a,z,t)=z\,[g(t-a)+a\,g'(t-a)]-a\,g(t-a)$",
    fontsize=16,ha="center")
fig.text(.5,.045,r"$g(t)=e^{-1/t}\ (t>0),\quad g(t)=0\ (t\leq0),"
    r"\qquad u(1,0,2)=-1/e\ne0$",fontsize=15,ha="center")
stem=OUT/"mixed-determination-transverse-derivative-023"
fig.savefig(stem.with_suffix(".svg"),metadata={"Date":"2026-10-02",
    "Creator":"GPT-6.1 Sol (OpenAI)","Title":"A transverse boundary derivative outside point-value data",
    "Description":"Exact squared-wave mixed counterexample, backward cone geometry, and boundary derivative. Original CC0."})
fig.savefig(stem.with_suffix(".png"),dpi=160,metadata={
    "Author":"GPT-6.1 Sol (OpenAI)","Title":"A transverse boundary derivative outside point-value data"})
plt.close(fig)
print(str(stem.with_suffix(".png")))
