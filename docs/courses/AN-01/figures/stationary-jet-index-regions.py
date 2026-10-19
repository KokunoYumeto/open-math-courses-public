"""Exact finite index sets in F15/F25 and F37, not a numerical proof.
Original diagram by GPT-6 Astra (OpenAI), CC0.
Run with Python, NumPy and Matplotlib; outputs are beside this source.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,2,figsize=(12.8,5.8),constrained_layout=True)
pairs=[(j,mu) for j in range(5) for mu in range(2*j+1)]
assert len(pairs)==25
points=axes[0].scatter([j for j,mu in pairs],[mu for j,mu in pairs],
                      c=[2*j-mu for j,mu in pairs],cmap="viridis",s=72,
                      vmin=0,vmax=8,zorder=3)
axes[0].plot([0,4],[0,8],"--",color="#505050",linewidth=1.3)
axes[0].set(title="Stationary coefficient indices",xlabel=r"coefficient order $j$",
            ylabel=r"cubic-remainder power $\mu$",xlim=(-.4,4.5),ylim=(-.5,9.4),
            xticks=range(5),yticks=range(0,9,2))
axes[0].text(.1,8.7,r"$0\leq j<5,\quad 0\leq\mu\leq 2j$")
bar=fig.colorbar(points,ax=axes[0],ticks=[0,2,4,6,8],shrink=.74,pad=.02)
bar.set_label(r"maximum amplitude order $2j-\mu$")
N,r=6,3
cancelled=[];remaining=[]
for j in range(N):
 for nu in range(j*(r-1)+1):
  (cancelled if j+nu<N else remaining).append((j,nu))
assert len(cancelled)==14 and len(remaining)==22
assert all(j>=2 for j,nu in remaining)
for pts,color,marker in [(cancelled,"#89949c","o"),(remaining,"#b84b13","s")]:
 axes[1].scatter([p[0] for p in pts],[p[1] for p in pts],s=65,color=color,marker=marker,zorder=3)
axes[1].plot([0,5],[0,10],"--",color="#505050",linewidth=1.3)
axes[1].plot([0,5],[6,1],":",color="#6f3581",linewidth=1.8)
axes[1].axvline(2,color="#b84b13",alpha=.3)
axes[1].set(title=r"Quadratic exchange: $N=6,\ r=3$",
 xlabel=r"inverse-frequency order $j$",ylabel=r"quadratic power $\nu$",
 xlim=(-.4,5.5),ylim=(-.5,11.7),xticks=range(6),yticks=range(0,11,2))
axes[1].text(.1,10.9,r"$\nu\leq2j,\quad j+\nu\geq6\ \Rightarrow\ j\geq2$")
axes[1].legend(handles=[
 Line2D([],[],linestyle="",marker="o",color="#89949c",label="cancels"),
 Line2D([],[],linestyle="",marker="s",color="#b84b13",label="may remain"),
 Line2D([],[],linestyle=":",color="#6f3581",label=r"$j+\nu=6$")],
 loc="upper left",bbox_to_anchor=(.02,.85),fontsize=10)
for ax in axes:
 ax.grid(alpha=.2)
 ax.spines[["top","right"]].set_visible(False)
fig.suptitle("Vanishing order determines the finite coefficient regions",fontsize=17)
for ext in ["svg","png"]:
 fig.savefig(out/f"stationary-jet-index-regions.{ext}",dpi=160)
plt.close(fig)
svg=out/"stationary-jet-index-regions.svg"
svg.write_text("\n".join(s.rstrip() for s in svg.read_text(encoding="utf-8").splitlines())+"\n",
               encoding="utf-8",newline="\n")
