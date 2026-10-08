"""Reproduce the exact type III_0 return-model figure. Python + NumPy + Matplotlib."""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Wedge
import numpy as np

BASE = Path(__file__).resolve().parent
font_manager.fontManager.addfont(BASE / "DejaVuSans.ttf")
font_manager.fontManager.addfont(BASE / "DejaVuSans-Bold.ttf")
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.titlesize": 16, "axes.labelsize": 12,
    "svg.fonttype": "path", "svg.hashsalt": "typeiii-zero-roof-v1",
    "savefig.facecolor": "#f7f9fc",
})
DATA = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
c = math.log(2)
b = (math.sqrt(5)-1)/2
assert 0.5 < b < 1 and 0 < 2*b-1 < 0.5
assert DATA["roof_multiples_of_log2"] == [2, 1, 2]
assert math.isclose(math.exp(-c/4)/8, math.exp(-3*c)*math.exp(-c/4))
assert math.isclose(math.exp(-7*c/4)*4, math.exp(c/2)*math.exp(-c/4))
ink, blue, orange, green, red = "#1b2d42", "#2866a1", "#b36020", "#147a62", "#af3045"
fig, axs = plt.subplots(2, 2, figsize=(18, 13.6))
fig.patch.set_facecolor("#f7f9fc")
fig.subplots_adjust(top=.88, bottom=.16, left=.065, right=.97, hspace=.43, wspace=.30)
fig.suptitle("A nonconstant return roof and its exact trace density",
             x=.065, y=.971, ha="left", fontsize=23, fontweight="bold", color=ink)
fig.text(.065,.929,
         "c = log 2;  Tω = ω + (√5 − 1)/2 (mod 1);  r = 2c on [0,1/2), r = c on [1/2,1)",
         fontsize=15, color=ink)
for ax in axs.flat:
    ax.set_facecolor("white")
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(colors=ink)
    ax.xaxis.label.set_color(ink)
    ax.yaxis.label.set_color(ink)

ax = axs[0,0]
ax.set_title("A. Two returns: height recurs, base advances", loc="left", color=ink, pad=16)
for j, roof in enumerate([2,1,2]):
    grad = np.exp(-c*np.linspace(0,roof,256)).reshape(-1,1)
    ax.imshow(grad, extent=(j-.23,j+.23,0,roof), origin="lower",
              aspect="auto", cmap="Blues", vmin=0, vmax=1, alpha=.34)
    ax.add_patch(Rectangle((j-.23,0),.46,roof, fill=False, edgecolor=blue, lw=1.4))
    ax.hlines(roof,j-.24,j+.24,color=blue,lw=1.5,linestyles="dashed")
    ax.text(j,roof+.12, f"roof = {roof}c" if roof!=1 else "roof = c",
            ha="center",fontsize=11,color=blue)
ax.annotate("", (0,1.98),(0,.25), arrowprops=dict(arrowstyle="-|>",lw=2.7,color=green))
ax.annotate("", (1,.03),(0,2), arrowprops=dict(arrowstyle="-|>",lw=2.1,color=orange,
                                             connectionstyle="arc3,rad=-.20"))
ax.annotate("", (1,.98),(1,0), arrowprops=dict(arrowstyle="-|>",lw=2.7,color=green))
ax.annotate("", (2,.025),(1,1), arrowprops=dict(arrowstyle="-|>",lw=2.1,color=orange,
                                              connectionstyle="arc3,rad=-.20"))
ax.annotate("", (2,.25),(2,0), arrowprops=dict(arrowstyle="-|>",lw=2.7,color=green))
ax.scatter([0,2],[.25,.25],s=80,c=green,zorder=8)
ax.text(-.30,.31,"u = c/4",ha="right",color=green,fontsize=11)
ax.text(2.27,.32,"u′ = c/4",ha="left",color=green,fontsize=11)
ax.text(.55,1.30,"γ²\ntrace × 1/4",ha="center",color=orange,fontsize=11,
        bbox=dict(facecolor="white",edgecolor="none",alpha=.9,pad=2))
ax.text(1.54,.68,"γ\ntrace × 1/2",ha="center",color=orange,fontsize=11,
        bbox=dict(facecolor="white",edgecolor="none",alpha=.9,pad=2))
ax.set_xlim(-.68,2.80);ax.set_ylim(-.12,2.50)
ax.set_xticks([0,1,2],["ω = 0","Tω = b","T²ω = 2b − 1"])
ax.set_yticks([0,.25,1,2],["0","1/4","1","2"])
ax.set_ylabel("height / c")
ax.text(.02,-.23,"t = 3c;  total roof = 3c;  coefficient trace × 1/8\n"
        "e^(−u′) / 8 = e^(−3c) e^(−u)   [ZDC64]",
        transform=ax.transAxes,fontsize=12,color=ink)

ax=axs[0,1]
ax.set_title("B. The height density supplies the real scaling",loc="left",color=ink,pad=16)
x=np.linspace(0,2.1,400)
ax.plot(x,2.0**(-x),color=blue,lw=3,label="correct density e^(−u) = 2^(−u/c)")
ax.plot(x,np.ones_like(x),color=red,lw=2,linestyle="--",label="unweighted density 1")
ax.fill_between(x,0,2.0**(-x),color=blue,alpha=.10)
ax.set_xlim(0,2.1);ax.set_ylim(0,1.24)
ax.set_xlabel("u / c");ax.set_ylabel("scalar density")
ax.set_xticks([0,.5,1,1.5,2]);ax.set_yticks([0,.25,.5,1])
ax.legend(loc="upper right",fontsize=10,frameon=False)
ax.text(.85,.66,"one local step t = c/2:\n"
        "e^(−(u+t)) / e^(−u) = 1/√2",color=blue,fontsize=12)
ax.text(.85,.16,"unweighted local ratio = 1\n"
        "so it cannot yield e^(−t)",color=red,fontsize=12)
ax.text(.02,-.23,"Across n roofs:  u′ = u + t − rₙ\n"
        "e^(−u′) e^(−rₙ) = e^(−t) e^(−u)   [ZDC47]",
        transform=ax.transAxes,fontsize=12,color=ink)

ax=axs[1,0]
ax.set_title("C. A regular nonzero height recovers the coefficient",loc="left",color=ink,pad=16)
x=np.linspace(-.15,2,400)
ax.plot(x,3*2.0**(-x),color=blue,lw=2.7)
ax.scatter([0],[3],s=85,facecolors="white",edgecolors=blue,lw=2,zorder=5)
ax.scatter([0],[99],s=95,c=red,marker="x",lw=2.5,zorder=6)
ax.annotate("arbitrary value 99\non the null section {s = 0}",
            (0,99),(.42,42),color=red,fontsize=11,
            arrowprops=dict(arrowstyle="->",color=red))
ax.axvline(.25,color=green,linestyle=":",lw=1.8)
ax.scatter([.25],[3*2**(-.25)],c=green,s=80,zorder=8)
ax.annotate("regular s₀ = c/4\n"
            "e^(s₀)b(s₀) = 3",
            (.25,3*2**(-.25)),(.82,7.5),color=green,fontsize=12,
            arrowprops=dict(arrowstyle="->",color=green))
ax.set_yscale("log")
ax.set_xlim(-.15,2);ax.set_ylim(.6,140)
ax.set_xlabel("s / c");ax.set_ylabel("b(s), logarithmic scale")
ax.set_xticks([0,.25,1,2],["0","1/4","1","2"])
ax.set_yticks([1,3,10,99],["1","3","10","99"])
ax.text(.02,-.23,"Changing the zero-height value leaves the trace unchanged.\n"
        "Fubini chooses a regular height; zero is not prescribed.   [ZDC15,66]",
        transform=ax.transAxes,fontsize=11.5,color=ink)

ax=axs[1,1]
ax.set_title("D. The return center is nonatomic and aperiodic",loc="left",color=ink,pad=16)
ax.add_patch(Wedge((0,0),1,0,180,width=.13,facecolor="#bcd4ea",edgecolor="white"))
ax.add_patch(Wedge((0,0),1,180,360,width=.13,facecolor="#efcfaf",edgecolor="white"))
vals=[0,b,2*b-1]
pts=[np.array([math.cos(2*math.pi*v),math.sin(2*math.pi*v)]) for v in vals]
for i,p in enumerate(pts):
    ax.scatter(*p,s=95,color=[green,orange,blue][i],zorder=7)
for i in range(2):
    ax.annotate("",pts[i+1]*.89,pts[i]*.89,
                arrowprops=dict(arrowstyle="-|>",lw=2,color=ink,connectionstyle="arc3,rad=.12"))
ax.text(1.10,0,"ω = 0",va="center",color=green,fontsize=12)
ax.text(-.77,-.85,"Tω = b",ha="center",color=orange,fontsize=12)
ax.text(.16,1.12,"T²ω = 2b − 1",ha="left",color=blue,fontsize=12)
ax.text(-1.43,.63,"r = 2c",color=blue,fontsize=12)
ax.text(.90,-.77,"r = c",color=orange,fontsize=12)
ax.text(0,.20,"T: irrational\nrotation",ha="center",va="center",fontsize=13,color=ink,
        bbox=dict(facecolor="white",edgecolor="none",pad=3))
ax.set_xlim(-1.65,1.8);ax.set_ylim(-1.20,1.35);ax.set_aspect("equal")
ax.axis("off")
ax.text(-.01,-.22,"Three orbit points are shown; there is no closing arrow.\n"
        "Z(N) = L∞(circle);  N = L∞(circle) ⊗ D is a nonfactor.   [ZDC61–63]",
        transform=ax.transAxes,fontsize=11.5,color=ink)
fig.text(.065,.042,
         "Theorem mechanism:  τα = τ(e^(−r)·)  →  suspended trace e^(−u)du  →  real scaling e^(−t).",
         fontsize=13,color=ink)
fig.text(.065,.018,
         "Exact model and proofs: Sections 3, 6 and 8. Diagram A separates three fibers; its horizontal spacing is schematic.",
         fontsize=10.5,color=ink)
fig.savefig(BASE/"typeiii-zero.svg",metadata={"Date":None,"Creator":"Original mathematical figure; CC0-1.0"})
fig.savefig(BASE/"typeiii-zero.png",dpi=140,metadata={"Software":"Reproducible Matplotlib mathematical figure"})
plt.close(fig)
print(json.dumps({"png":"typeiii-zero.png","svg":"typeiii-zero.svg",
                  "forward_density_identity":True,"negative_density_identity":True,
                  "size_px":[2520,1904]}))
