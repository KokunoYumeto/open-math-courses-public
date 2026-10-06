"""Original CC0 diagram: exact bracket hypotheses and curvature absorption."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

k=np.linspace(-3,3,601)
with plt.rc_context({"font.family":"DejaVu Sans","font.size":11}):
    fig=plt.figure(figsize=(14,10),dpi=150,facecolor="#fffdfa")
    fig.text(0.05,0.955,"Two bracket hypotheses, one curvature-loss argument",fontsize=21,weight="bold",color="#17374b")
    fig.text(0.05,0.917,r"Exact pointwise regions: $k=\operatorname{Im}a,\quad C_0=2,\quad C_1=1$; $b$ includes the time bracket (1.1).",fontsize=12,color="#344756")
    ax=fig.add_axes([0.08,0.54,0.36,0.29])
    bound=2*np.abs(k)+1
    ax.fill_between(k,-bound,bound,color="#b8d8e7",alpha=0.8)
    ax.plot(k,bound,color="#2178a5",lw=2)
    ax.plot(k,-bound,color="#2178a5",lw=2)
    ax.scatter([0,-2],[2,-1],c=["#a45330","#2178a5"],s=55,zorder=5)
    ax.annotate("A = (0, 2): outside",xy=(0,2),xytext=(0.3,4.0),fontsize=10,arrowprops={"arrowstyle":"->","color":"#a45330"},color="#a45330")
    ax.annotate("B = (-2, -1): inside",xy=(-2,-1),xytext=(-2.85,-4.1),fontsize=10,arrowprops={"arrowstyle":"->","color":"#2178a5"},color="#2178a5")
    ax.set_title(r"Absolute control (1.2): $|b|\leq2|k|+1$",fontsize=13,pad=14)
    ax.set(xlim=(-3,3),ylim=(-7,7),xlabel=r"Imaginary symbol value $k$",ylabel=r"Full bracket $b$")
    ax.grid(alpha=0.15)
    ax.axhline(0,color="#adb9c0",lw=0.7);ax.axvline(0,color="#adb9c0",lw=0.7)
    for spine in ax.spines.values():spine.set_color("#c3cbd0")
    ax=fig.add_axes([0.57,0.54,0.36,0.29])
    boundary=-2*k-1
    ax.fill_between(k,boundary,7,color="#dac5dd",alpha=0.8)
    ax.plot(k,boundary,color="#87528f",lw=2)
    ax.scatter([0,-2],[2,-1],c=["#87528f","#a45330"],s=55,zorder=5)
    ax.annotate("A = (0, 2): inside",xy=(0,2),xytext=(0.25,4.6),fontsize=10,arrowprops={"arrowstyle":"->","color":"#87528f"},color="#87528f")
    ax.annotate("B = (-2, -1): outside",xy=(-2,-1),xytext=(-2.85,-4.4),fontsize=10,arrowprops={"arrowstyle":"->","color":"#a45330"},color="#a45330")
    ax.set_title(r"Signed control (1.3): $b\geq-2k-1$",fontsize=13,pad=14)
    ax.set(xlim=(-3,3),ylim=(-7,7),xlabel=r"Imaginary symbol value $k$",ylabel=r"Full bracket $b$")
    ax.grid(alpha=0.15)
    ax.axhline(0,color="#adb9c0",lw=0.7);ax.axvline(0,color="#adb9c0",lw=0.7)
    for spine in ax.spines.values():spine.set_color("#c3cbd0")
    fig.text(0.08,0.455,"Shading shows a finite window of each exact planar condition; A and B are points, not operator countermodels.",fontsize=11,color="#344756")
    fig.text(0.05,0.400,"The two positivity routes bound the same operator loss",fontsize=15,weight="bold",color="#17374b")
    boxes=[(0.07,0.284,0.39,0.075,"#e9f4f8","Absolute branch: quadratic positivity (4.2)–(4.4)",r"$\|Bv\|^2-2\epsilon^2 C_0^2\|Kv\|^2\leq C X^2$"),
           (0.54,0.284,0.39,0.075,"#f2edf5","Signed branch: sharp lower bound (3.1)–(3.2)",r"$(Bv,v)+\epsilon C_0(Kv,v)\geq-CX^2$")]
    for x,y,w,h,color,title,formula in boxes:
        rect=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.007",transform=fig.transFigure,facecolor=color,edgecolor="#cdd8df")
        fig.add_artist(rect)
        fig.text(x+w/2,y+0.049,title,ha="center",fontsize=11,weight="bold")
        fig.text(x+w/2,y+0.016,formula,ha="center",fontsize=12)
    fig.text(0.5,0.235,r"Common bound (5.1): $M^2\leq\kappa\|Kv\|X+CX^2,\quad M^2=\max(0,-(Bv,v))$",ha="center",fontsize=13,color="#344756")
    fig.text(0.5,0.184,r"(5.3): $\frac{3}{2}E^2\geq(2-3\kappa)\tau X^2-\Delta X^2,\quad \Delta=2C+\frac{9}{4}\kappa^2$",ha="center",fontsize=13,color="#344756")
    fig.text(0.5,0.135,r"Fixed $\kappa\leq1/3$, then $\tau\geq\max(1,4C+1/2)$: $\tau X^2\leq3E^2$ (5.4).",ha="center",fontsize=14,color="#246a50")
    fig.text(0.05,0.064,r"$X=\|v\|,\ E=\|Tv\|$; compact time / Schwartz transverse variables. No ellipticity or derivative conclusion.",fontsize=10,color="#566779")
    fig.text(0.05,0.035,"Full proofs: Sections 2–5; region comparison: Exercise 2. Hörmander IV, Proposition 28.1.6, pp. 229–230. Original CC0; reproducible Python source.",fontsize=10,color="#566779")
    fig.savefig(Path(__file__).with_name("bracket-control-and-curvature-loss.png"),dpi=150)
    plt.close(fig)
