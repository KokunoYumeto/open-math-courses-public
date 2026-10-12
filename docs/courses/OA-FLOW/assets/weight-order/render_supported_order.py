"""Exact supported-strip models. Original expression/code: CC0-1.0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.hashsalt": "oa-flow-supported-order-v1"})
BLUE = "#20639b"
RED = "#ad3848"
GREEN = "#237f69"
fig, axes = plt.subplots(1, 3, figsize=(16, 7.4))
fig.subplots_adjust(left=.055, right=.985, top=.79, bottom=.40, wspace=.37)
fig.suptitle("A supported strip needs the support inclusion", fontsize=22, y=.98)
fig.text(.5, .9, "Exact diagonal models on three coordinates; zero extension also gives examples in B(ℓ²).",
         ha="center", fontsize=13)
x=np.arange(3); w=.32
for ax, h, k, title in [
    (axes[0], [1,0,0], [0,1,0], "A. Incomparable supports"),
    (axes[1], [1,0,0], [4,9,0], "B. Nested, unequal supports")]:
    ax.bar(x-w/2,h,w,color=BLUE,label=r"$h$")
    ax.bar(x+w/2,k,w,color=GREEN,label=r"$k$")
    ax.set_xticks(x,["1","2","3"]); ax.set_xlabel("coordinate")
    ax.set_ylabel("density eigenvalue");ax.set_title(title,pad=16)
    ax.legend(frameon=False);ax.spines[["top","right"]].set_visible(False)
    for vals,dx in [(h,-w/2),(k,w/2)]:
        for j,v in enumerate(vals):
            ax.text(j+dx,v+.04*max(1,max(k)),str(v),ha="center",va="bottom",fontsize=11)
axes[0].set_ylim(0,1.35); axes[1].set_ylim(0,11.5)
axes[0].text(.5,-.32,r"$p=E_{11},\quad q=E_{22}$"+"\n"+
             r"$h_s^{it}k_s^{-it}=0=k_s^{it}h_s^{-it}$"+"\n"+
             "Zero strip functions, but neither form order.",
             ha="center",va="top",transform=axes[0].transAxes,fontsize=11,color=RED,linespacing=1.7)
axes[1].text(.5,-.32,r"$p=E_{11}\leq q=E_{11}+E_{22}$"+"\n"+
             r"$h^{2a}\leq k^{2a}\quad(a>0)$"+"\n"+
             r"$U(z)=4^{-iz}E_{11},\quad U(0)=p$",
             ha="center",va="top",transform=axes[1].transAxes,fontsize=11,linespacing=1.7)
a=np.linspace(0,2,401)
ax=axes[2]; ax.plot(a,4.**(-a),color=BLUE,lw=2.5)
points=[0,.5,1,2]; values=[1,.5,.25,.0625]
ax.scatter(points,values,color=RED,zorder=4)
for xx,yy,label,offset in [(0,1,"1",(8,-12)),(.5,.5,"1/2",(10,6)),
                          (1,.25,"1/4",(10,6)),(2,.0625,"1/16",(-33,12))]:
    ax.annotate(label,(xx,yy),textcoords="offset points",xytext=offset,fontsize=11)
ax.set_xlim(-.04,2.06);ax.set_ylim(0,1.1);ax.set_xticks(points)
ax.set_xlabel("strip depth a");ax.set_ylabel(r"$\|U(t-ia)\|$")
ax.set_title("C. Exact endpoint norm",pad=16)
ax.spines[["top","right"]].set_visible(False);ax.grid(alpha=.15)
ax.text(.5,-.32,r"$\|U(t-ia)\|=4^{-a}$"+"\n"+
        r"$T_a=4^{-a}E_{11}$"+"\n"+"Kernel coordinates stay zero at both edges.",
        ha="center",va="top",transform=ax.transAxes,fontsize=11,linespacing=1.7)
fig.text(.5,.065,
         "Full theorem: complete form order ⇔ support inclusion + contractive supported strip.",
         ha="center",fontsize=13)
fig.text(.5,.02,"Proof: L158 §9, (PS16)–(PS22). Weight application and whole-cone order: WORD §8, (WO27)–(WO33).",
         ha="center",fontsize=11,color="#4a5965")
fig.savefig(ROOT/"supported-order.png",dpi=180,metadata={"Software":"OA-FLOW deterministic figure"})
fig.savefig(ROOT/"supported-order.svg",metadata={"Date":None})
plt.close(fig)
data={
 "schema":"oa-flow-supported-strip-exact-models-v1",
 "models":{"incomparable":{"h":[1,0,0],"k":[0,1,0],"p":[1,0,0],"q":[0,1,0],
                         "both_supported_products":"zero","neither_form_order":True},
           "nested":{"h":[1,0,0],"k":[4,9,0],"p":[1,0,0],"q":[1,1,0],
                     "strip":"U(z)=4^(-iz)E11","endpoint_norm":"4^(-a)",
                     "exact_depth_norm_pairs":[["0","1"],["1/2","1/2"],["1","1/4"],["2","1/16"]]}},
 "proof_locations":["OA-FLOW-L158.md#oa-flow.l158.supported","OA-FLOW-WORD.md#wo-supported"],
 "interpretation":"Exact multiplication models. The plotted norm samples illustrate an algebraic formula; they are not the proof of the general theorem.",
 "licence":"CC0-1.0 to the extent of rights held; installed font glyphs retain their own licence."
}
(ROOT/"supported-order.json").write_bytes((json.dumps(data,ensure_ascii=False,indent=2)+"\n").encode("utf8"))
