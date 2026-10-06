"""Reproducible figure for the radius-adapted logarithmic circuit proof.

CC0. OpenAI Codex, GPT-6.1 Sol, Ultra.
The left panel is a proved exclusion in height/modulus coordinates, not
a plotted number field. The right panel samples exact proved cost ratios.
"""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

root=Path(__file__).resolve().parents[1]
fig,axes=plt.subplots(1,2,figsize=(11.8,4.6),layout="constrained")
ink="#173247";blue="#087d9a";orange="#b8601a";light="#e3f1f3"
for ax in axes:
    ax.spines[["top","right"]].set_visible(False)
    ax.tick_params(colors=ink)
    for spine in ax.spines.values():spine.set_color(ink)
ax=axes[0]
ax.add_patch(Rectangle((0,0),1,1,facecolor=light,edgecolor=blue,
                      hatch="///",linewidth=1.7))
ax.scatter([0],[0],color=ink,s=24,zorder=5)
ax.text(.5,.59,"No nonzero logarithmic vector",ha="center",color=ink,fontsize=11)
ax.text(.5,.39,r"$h(\gamma)\leq\eta,\quad E|\lambda|/D\leq\eta$",
        ha="center",color=ink,fontsize=12)
ax.text(.07,.06,"Zero vector",ha="left",color=ink,fontsize=10)
ax.set(xlim=(0,1.3),ylim=(0,1.25),xticks=[0,1],yticks=[0,1],
       xlabel=r"Height $h(\gamma)/\eta$",
       ylabel=r"Chosen modulus $E|\lambda|/(D\eta)$",
       title="A radius-dependent exclusion")
ax.text(.5,1.08,r"$D=10^9,\ v=D,\ u=y=1,\ M=64,\ \eta=1/4096$",
        ha="center",color=ink,fontsize=10)
ax.text(.5,-.27,"Every base lies in a field of degree at most D.\n"
                  r"$\lambda\ne0,\ e^\lambda=\gamma$; proof (8.202)–(8.204).",
        transform=ax.transAxes,ha="center",color=ink,fontsize=10)
ax=axes[1]
ns=list(range(2,31))
ratios=[]
for n in ns:
    C=2**(n+25)*n**(3*n+9)
    Cp=2**(n+24)*(n-1)**(3*n+6)
    ratios.append(float(Fraction((64*n*n+4)*Cp,C)))
ax.plot(ns,ratios,color=blue,marker="o",markersize=3,linewidth=1.6)
ax.axhline(.5,color=orange,linestyle="--",linewidth=1.4)
ax.text(29,.515,"Half the original exponent",ha="right",color=orange,fontsize=10)
ax.set(xlim=(1.5,30.5),ylim=(0,.57),xlabel="Number of logarithms n",
       ylabel="Fraction of the original exponent",
       title="Both transfer costs fit")
ax.text(10,.36,r"Coefficient cost: $(64n^2+4)C_{n-1}/C_n<1/2$",
        color=ink,fontsize=10)
ax.text(10,.25,r"Multiplier cost: $64n^2/C_n<1/2$",
        color=ink,fontsize=10)
ax.text(10,.18,r"Largest multiplier fraction: $2^{-34}$ at $n=2$",
        color=ink,fontsize=10)
ax.text(.5,-.27,r"$C_n=2^{n+25}n^{3n+9}$. Points are finite samples;"
                  "\nproof (8.206)–(8.208) covers every dimension.",
        transform=ax.transAxes,ha="center",color=ink,fontsize=10)
fig.suptitle("How a small chosen logarithm controls dependent coefficients",
             fontsize=14,color=ink)
out=root/"figures"
out.mkdir(exist_ok=True)
fig.savefig(out/"radius-adapted-circuit.png",dpi=180,bbox_inches="tight")
fig.savefig(out/"radius-adapted-circuit.svg",bbox_inches="tight")
print(str((out/"radius-adapted-circuit.png").resolve()))

