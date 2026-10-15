"""Original CC0-1.0 illustration of MIV11--13. Run with Python.
The heat map samples one scalar formula; the written proofs establish all limits.
Font components retain their terms.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
    "svg.hashsalt":"oa-flow-uncountable-product-times-v1",
    "axes.spines.top":False,"axes.spines.right":False})
INK="#17354e";TEAL="#087f82";PALE="#eff7f8";BLUE="#286cac"
r=np.linspace(-1,1,801);c=np.linspace(1,2,401)
rr,cc=np.meshgrid(r,c)
d=4*np.exp(-cc)/(1+np.exp(-cc))**2*np.sin(np.pi*rr*cc)**2
fig=plt.figure(figsize=(15,8.1),dpi=170,facecolor="white")
fig.suptitle("Arbitrary products, countable detection",fontsize=24,color=INK,y=.97)
fig.text(.5,.91,r"$d_c(t)=2e^{-c}(1+e^{-c})^{-2}(1-\cos ct),\qquad c\in[1,2]$",
         ha="center",color=INK,fontsize=18)
ax=fig.add_axes([.07,.27,.37,.50])
im=ax.contourf(r,c,d,levels=np.linspace(0,.8,41),cmap="YlGnBu",vmin=0,vmax=.8)
for sign in [-1,1]:
    ax.plot(sign/c,c,color=INK,lw=1.6,ls="--")
ax.axvline(0,color=INK,lw=1.6,ls="--")
ax.set(xlim=(-1,1),ylim=(1,2),xlabel=r"Normalized time $r=t/(2\pi)$",ylabel="Tensor-leg parameter c")
ax.set_title("Positive intervals force divergence",color=INK,pad=15,fontsize=15)
ax.text(-.82,1.35,r"$rc=-1$",rotation=57,ha="center",color=INK,fontsize=13,bbox={"facecolor":"white","alpha":.8,"edgecolor":"none","pad":2})
ax.text(.82,1.35,r"$rc=1$",rotation=-57,ha="center",color=INK,fontsize=13,bbox={"facecolor":"white","alpha":.8,"edgecolor":"none","pad":2})
ax.text(.035,1.85,r"$r=0$",color=INK,fontsize=12)
bar=fig.colorbar(im,cax=fig.add_axes([.455,.27,.014,.50]))
bar.set_label(r"Dispersion $d_c(2\pi r)$")
ax.set_xticks([-1,-.5,0,.5,1])
ax.set_yticks([1,1.25,1.5,1.75,2])

flow=fig.add_axes([.56,.23,.40,.56]);flow.set(xlim=(0,1),ylim=(0,1));flow.axis("off")
flow.set_title("A countable family of threshold witnesses",color=INK,pad=8,fontsize=15)
def box(y,head,body):
    flow.add_patch(FancyBboxPatch((.03,y),.94,.19,boxstyle="round,pad=0.015",
                   facecolor=PALE,edgecolor=TEAL,lw=1.5))
    flow.text(.5,y+.135,head,ha="center",va="center",color=INK,fontsize=16)
    flow.text(.5,y+.055,body,ha="center",va="center",color=INK,fontsize=12)
def arrow(y0,y1):
    flow.add_patch(FancyArrowPatch((.5,y0),(.5,y1),arrowstyle="-|>",
                                  color=TEAL,mutation_scale=16,lw=1.8))
box(.75,r"Rational thresholds q and intervals B",
    "Whenever a finite sum exceeds q throughout B:")
arrow(.73,.67)
box(.45,r"Select one finite witness $A_{q,B}$",
    "There are only countably many eligible pairs (q, B).")
arrow(.43,.37)
box(.15,r"$J=\bigcup_{q,B} A_{q,B}$ is countable",
    "Every strict rational threshold is still detected.")
flow.text(.5,.025,r"$\sum_{i\in I}d_i(t)=\sum_{i\in J}d_i(t)$ for every $t$",
          ha="center",color=TEAL,fontsize=18)
fig.text(.265,.14,r"$T(M)=\mathrm{Per}(\varphi)=\{0\}$",
         ha="center",color=BLUE,fontsize=19)
fig.text(.265,.09,r"An explicit detector: $J=\mathbb{Q}\cap[1,2]$.",
         ha="center",color=INK,fontsize=13)
fig.text(.76,.14,r"$T(M)=T(M_J)$; also exact state periods agree.",
         ha="center",color=TEAL,fontsize=14)
fig.text(.76,.09,"No countable generation or factor isomorphism follows.",
         ha="center",color=INK,fontsize=12)
fig.text(.5,.035,"Left: numerical samples and exact zero curves, MIV13.e-f.  Right: logical steps of the full proof, MIV13.a-c.",
         ha="center",color=INK,fontsize=12)
fig.savefig(HERE/"uncountable-product-times.png",dpi=170,
            metadata={"Software":"Original CC0 mathematical figure"})
fig.savefig(HERE/"uncountable-product-times.svg",
            metadata={"Date":None,"Creator":"Original CC0 mathematical figure"})
plt.close(fig)

sample=[]
for cv in [1,1.25,1.5,1.75,2]:
    for rv in [-1,-.5,0,.5,1]:
        value=float(4*np.exp(-cv)/(1+np.exp(-cv))**2*np.sin(np.pi*rv*cv)**2)
        sample.append({"c":cv,"r":rv,"d_c(2*pi*r)":value})
data={"licence":"CC0-1.0; font terms separate",
      "formula":"d_c(t)=2*exp(-c)/(1+exp(-c))^2*(1-cos(c*t))",
      "index_interval":[1,2],"normalized_time":"r=t/(2*pi)",
      "plot_grid":{"r_points":801,"c_points":401,"r_range":[-1,1],"c_range":[1,2]},
      "zero_curves":"r*c belongs to Z; interior plotted branches r=0 and r=+/-1/c",
      "samples":sample,
      "exact_conclusions":{"T(M)":"{0}","Per(phi)":"{0}","explicit_countable_detector":"Q intersect [1,2]"},
      "general_detection":"For continuous nonnegative d_i, rational-threshold open covers select countably many finite witness sets; their union J preserves the full extended sum at every real time.",
      "proof_locators":["MIV11.a","MIV11.b","MIV12.b","MIV12.e","MIV13.a","MIV13.b","MIV13.c","MIV13.e","MIV13.f"],
      "limits":"The heat map is a finite sampling of a scalar formula, not a proof of divergence. The diagram does not model cardinality geometrically or assert countable generation.",
      "programme_input":"OA-APPROX/infinite-tensor-products.html#theorem-4-1",
      "human_background":"H. Araki and E. J. Woods, A Classification of Factors, https://ems.press/journals/prims/articles/2441"}
(HERE/"data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
