"""Sublevel areas, logarithmic cuts and circular point sources.

Original figure by GPT-6 Astra (OpenAI), October 2026. CC0.
Python, NumPy and Matplotlib reproduce the PNG and SVG beside this file.
Level curves are evaluated from exact equations, not fitted numerical contours.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                    "svg.hashsalt":"AN01-sublevels-cuts-circular-sources"})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,2,figsize=(14,10),layout="constrained")
colors=["#2166ac","#c75a16","#238b45"]
theta=np.linspace(0,2*np.pi,801)
levels=[.64,.16,.04]
ax=axes[0,0]
for eps,color in zip(levels,colors):
    x=np.sqrt(eps)*np.cos(theta);y=.5*np.sqrt(eps)*np.sin(theta)
    ax.plot(x,y,color=color,label=fr"$\varepsilon={eps:g}$")
ax.scatter([0],[0],s=22,color="black")
ax.set(xlabel="$x$",ylabel="$y$",aspect="equal",xlim=(-.95,.95),ylim=(-.65,.65),
       title=r"A. Nondegenerate minimum: $g=x^2+4y^2$")
ax.text(-.88,.5,r"$|\{g\leq\varepsilon\}|=\pi\varepsilon/2$")
ax.legend(loc="lower left",fontsize=10);ax.grid(alpha=.15)

ax=axes[0,1]
for eps,color in zip(levels,colors):
    y=np.linspace(-eps**.25,eps**.25,801)
    x=np.sqrt(np.maximum(eps-y**4,0))
    ax.plot(x,y,color=color,label=fr"$\varepsilon={eps:g}$")
    ax.plot(-x,y,color=color)
ax.scatter([0],[0],s=22,color="black")
ax.set(xlabel="$x$",ylabel="$y$",aspect="equal",xlim=(-.95,.95),ylim=(-1.1,1.1),
       title=r"B. Degenerate minimum: $g=x^2+y^4$")
ax.text(-.89,.98,r"Coordinate scales: $\varepsilon^{1/2}$ and $\varepsilon^{1/4}$",fontsize=10)
ax.text(-.89,-1.01,r"Area / $\varepsilon=C\varepsilon^{-1/4}\to\infty$",fontsize=10)
ax.legend(loc="lower left",bbox_to_anchor=(0,.08),fontsize=10);ax.grid(alpha=.15)

ax=axes[1,0]
x=np.linspace(-1.25,1.25,601)
ax.axhspan(0,.8,color=colors[0],alpha=.09)
ax.axhline(0,color=colors[0],lw=2,label=r"$f=y=0$")
ax.plot(x,-x*x,color=colors[1],lw=2,label=r"$g=y+x^2=0$")
ax.scatter([0],[0],s=28,color="black",zorder=4)
ax.text(-1.17,.58,r"$D=\{y>0\}$",color=colors[0])
ax.text(-1.17,.3,r"$\log|g|_{y=0}=2\log|x|\in L^1_{\rm loc}$")
ax.set(xlabel="$x$",ylabel="$y$",xlim=(-1.25,1.25),ylim=(-1.65,.8),
       title="C. A tangential cut with an integrable surface logarithm")
ax.legend(loc="lower center",fontsize=10);ax.grid(alpha=.15)

ax=axes[1,1]
ax.plot(np.cos(theta),np.sin(theta),color="0.65",lw=1)
k=np.arange(1,13);angles=2*np.pi*k/13
ax.scatter(np.cos(angles),np.sin(angles),s=40,color=colors[0],
           label=r"Roots of $s_{12}$; each mass $2\pi/12$")
ax.scatter([1],[0],s=75,facecolors="none",edgecolors=colors[1],lw=2,
           label=r"Omitted grid point $1$")
ax.annotate(r"$1$",xy=(1,0),xytext=(1.13,.15),color=colors[1],
            arrowprops={"arrowstyle":"-","color":colors[1]})
ax.set(xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$",aspect="equal",
       xlim=(-1.35,1.35),ylim=(-1.45,1.35),
       title=r"D. $\Delta(n^{-1}\log|s_n|)\longrightarrow dS_{|z|=1}$")
ax.legend(loc="lower center",fontsize=9);ax.grid(alpha=.15)
fig.suptitle("Concentration, integrable traces and circular sources",fontsize=19)
fig.savefig(out/"sublevels-cuts-and-circular-sources.png",dpi=150)
svg=out/"sublevels-cuts-and-circular-sources.svg"
fig.savefig(svg,metadata={"Date":None})
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
plt.close(fig)
