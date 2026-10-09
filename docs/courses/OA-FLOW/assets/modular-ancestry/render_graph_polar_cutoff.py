"""Reproducible exact scalar schematic for CI-2/3 and HA-R5; no theorem inferred from a plot."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-modular-ancestry-20261009-v1"
from matplotlib.ticker import FixedLocator, FixedFormatter

out = Path(__file__).resolve().parent / "assets"
out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                    "axes.titlesize": 15, "axes.labelsize": 12,
                    "svg.fonttype": "none"})
fig = plt.figure(figsize=(13.5, 8.3), layout="constrained", facecolor="#fbfcfe")
grid = fig.add_gridspec(2, 2, height_ratios=[3.2, 1.2])
ax = fig.add_subplot(grid[0,0])
t = np.linspace(.04,.96,2000)
ax.plot(t,(1-t)/t,color="#1f589e",linewidth=2.6,label=r"$L(t)=(1-t)/t$")
ax.scatter([.25,.75],[3,1/3],s=70,c=["#ae4c30","#ae4c30"],zorder=4)
ax.annotate(r"$t=\frac{1}{4},\ L(t)=3$",(.25,3),xytext=(.36,7),
            arrowprops={"arrowstyle":"->","color":"#ae4c30"},color="#8c3b24")
ax.annotate(r"$1-t=\frac{3}{4},\ L(1-t)=\frac{1}{3}$",(.75,1/3),xytext=(.39,.095),
            arrowprops={"arrowstyle":"->","color":"#ae4c30"},color="#8c3b24")
ax.axhline(1,color="#8b97a8",linewidth=1,linestyle=":")
ax.axvline(.5,color="#8b97a8",linewidth=1,linestyle=":")
ax.set_yscale("log")
ax.set_xlim(0,1); ax.set_ylim(.035,30)
ax.set_xlabel(r"Scalar spectral parameter $t$ of $R=j^*j$ on the graph space $V$")
ax.set_ylabel(r"Scalar spectral value of $L=(1-R)/R$")
ax.set_title("A. Reflection becomes reciprocal spectrum\nCI-2–3, (CI5) and (CI8)–(CI12)",loc="left",pad=17)
ax.legend(loc="upper right",frameon=False)
ax.grid(alpha=.14,which="both")
ax.spines[["top","right"]].set_visible(False)

ax = fig.add_subplot(grid[0,1])
x = np.unique(np.concatenate([np.geomspace(1/10,10,3000),
                             np.array([1/8,1/4,1/2,1,2,4,8])]))
def g(t):
    return np.where(t<=1,1,np.where(t<2,2-t,0))
colors=["#9b493c","#457aa8","#2d8268"]
for n,c in zip([1,2,4],colors):
    fn=g(x/n)*g(1/(n*x))
    ax.plot(x,fn,color=c,linewidth=2.4,label=rf"$f_{n}$: support $[1/{2*n},{2*n}]$")
ax.set_xscale("log",base=2)
ax.set_xlim(1/10,10);ax.set_ylim(-.04,1.12)
ticks=[1/8,1/4,1/2,1,2,4,8]
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(FixedFormatter(["1/8","1/4","1/2","1","2","4","8"]))
ax.set_xlabel(r"Positive spectral parameter $t$ of $h$ or $k$")
ax.set_ylabel(r"Cutoff value $f_n(t)$")
ax.set_title("B. Cutoffs approach one inside the support\nHA-R5, (HR14)–(HR16)",loc="left",pad=17)
ax.legend(loc="lower center",frameon=True,facecolor="white",framealpha=.92)
ax.grid(alpha=.14,which="both")
ax.spines[["top","right"]].set_visible(False)

ax=fig.add_subplot(grid[1,:]);ax.axis("off")
ax.text(.015,.95,r"$V=D(S),\quad U:V\to H,\quad R=j^*j,\quad U R^{1/2}=j,\quad J=UKU^*,\quad\Delta=ULU^*$",
        fontsize=16,va="top",color="#24466e")
ax.text(.015,.67,r"$D(\Delta^{1/2})=D(S),\qquad S=J\Delta^{1/2},\qquad J\Delta J=\Delta^{-1}$",
        fontsize=16,va="top",color="#24466e")
ax.text(.015,.39,r"$f_n(k)\eta\in\mathcal{D}^2,\quad Ff_n(k)\eta=f_n(h)F\eta,\quad"
        r" (f_n(k)\eta,Ff_n(k)\eta)\longrightarrow(\eta,F\eta)$",
        fontsize=15,va="top",color="#28664f")
ax.text(.015,.10,"The plot shows exact scalar functions. Spectral integration, zero-kernel/support facts and domain proofs establish the operator identities.",
        fontsize=10.5,va="top",color="#4d596c")
fig.suptitle("From the closed graph to polar data and a full graph core",fontsize=20,fontweight="bold")
fig.savefig(out/"graph-polar-cutoff.png",dpi=170)
fig.savefig(out/"graph-polar-cutoff.svg", metadata={'Date': None})
plt.close(fig)
print(out/"graph-polar-cutoff.png")
