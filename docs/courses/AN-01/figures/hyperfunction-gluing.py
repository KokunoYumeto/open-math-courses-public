"""Exact interval/atom model for AN01-U098, Exercise 3. CC0.

Original drawing: GPT-6 Astra (OpenAI), Ultra. Horizontal coordinates
are mathematical coordinates. Vertical offsets separate schematic rows.
Run with Python and matplotlib to regenerate PNG and SVG beside this file.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"]="AN01-U098-exact-intervals"
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

P=Path(__file__).resolve().parent
navy="#164a70";orange="#b85b17";gray="#637586"
rows=[(-2,1,2.5,1,r"$X_1=(-2,1)$",r"$a_1=\delta_0+\delta_1$"),
      (-1,2,1.5,-1,r"$X_2=(-1,2)$",r"$a_2=\delta_0+\delta_{-1}$"),
      (-2,2,.5,None,r"$X_1\cup X_2=(-2,2)$",r"$a=\delta_0$")]
assert rows[0][1]==rows[0][3] and rows[1][0]==rows[1][3]
assert all(lo<0<hi for lo,hi,*_ in rows)
fig,ax=plt.subplots(figsize=(11,6.2),layout="constrained")
fig.patch.set_facecolor("#f8fafc");ax.set_facecolor("#f8fafc")
for x in range(-2,3):
    ax.axvline(x,color="#dce3e9",lw=.8,zorder=0)
for lo,hi,y,endpoint,label,rep in rows:
    ax.plot([lo,hi],[y,y],color=navy,lw=3,zorder=2)
    ax.scatter([lo,hi],[y,y],s=66,facecolors="#f8fafc",edgecolors=navy,zorder=3)
    ax.annotate("",xy=(0,y+.37),xytext=(0,y),
                arrowprops=dict(arrowstyle="-|>",color=navy,lw=2))
    ax.text(.08,y+.28,r"$\delta_0$",color=navy,fontsize=14)
    if endpoint is not None:
        ax.annotate("",xy=(endpoint,y+.37),xytext=(endpoint,y),
                    arrowprops=dict(arrowstyle="-|>",color=orange,lw=2))
        ax.text(endpoint+(.08 if endpoint==1 else -.38),y+.28,
                r"$\delta_1$" if endpoint==1 else r"$\delta_{-1}$",
                color=orange,fontsize=14)
    ax.text(-2.48,y+.65,label,fontsize=14,color=navy,va="center")
    ax.text(2.48,y+.65,rep,fontsize=14,color=gray,ha="right",va="center")
ax.set(xlim=(-2.5,2.5),ylim=(.05,3.35),xticks=range(-2,3),yticks=[],xlabel="Real coordinate x")
ax.tick_params(axis="x",labelsize=12)
ax.xaxis.label.set_size(12)
for side in ["left","top","right"]:ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color(gray)
ax.set_title("Boundary terms vanish in each local quotient",loc="left",fontsize=17,pad=18,color=navy)
handles=[Line2D([0],[0],color=navy,lw=3,label="Open interval (open endpoints)"),
         Line2D([0],[0],color=orange,lw=2,marker="^",label="Boundary atom in the representative")]
fig.legend(handles=handles,loc="outside lower center",ncols=1,frameon=False,fontsize=11)
for ext in ["png","svg"]:
    fig.savefig(P/("hyperfunction-gluing."+ext),dpi=180,
                metadata={"Creator":"GPT-6 Astra (OpenAI), Ultra; CC0","Date":None} if ext=="svg"
                else {"Author":"GPT-6 Astra (OpenAI), Ultra","License":"CC0"})
plt.close(fig)
svg=P/"hyperfunction-gluing.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8",newline="\n")
