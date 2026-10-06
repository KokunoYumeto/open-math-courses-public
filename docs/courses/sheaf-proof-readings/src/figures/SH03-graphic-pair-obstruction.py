"""Two analytic circle maps and their incompatible descended germs.
Original programme illustration, GPT-6 Astra (Ultra), CC0.
Run this file to regenerate the adjacent course figure.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2] / "figures"
ROOT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "svg.hashsalt": "SH03-graphic-pair-obstruction-v1", "svg.fonttype": "none"})
fig = plt.figure(figsize=(13.8, 6.1), facecolor="#fafafa")
axes = [fig.add_axes(rect) for rect in
        [(0.055, 0.36, 0.23, 0.46), (0.385, 0.36, 0.23, 0.46),
         (0.715, 0.36, 0.23, 0.46)]]
orange, blue, purple = "#b85c15", "#216394", "#792b82"
theta = np.linspace(0, 2*np.pi, 800)
for ax, color, sign in [(axes[0], orange, "+"), (axes[2], blue, "-")]:
    ax.plot(np.cos(theta), np.sin(theta), color=color, lw=2.7)
    ax.scatter([0, 0], [1, -1], s=45, color=purple, zorder=5)
    ax.axhline(0, color="#b3b3b3", lw=.7)
    ax.axvline(0, color="#b3b3b3", lw=.7)
    ax.set(xlim=(-1.25,1.25), ylim=(-1.2,1.2), aspect="equal",
           xlabel="$u$", ylabel="$v$")
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
    ax.set_title("$M_"+sign+"$: $u^2+v^2=1$", fontsize=14, pad=12)
    ax.text(.10, 1.02, "$u=0$", color=purple, fontsize=10)
    for spine in ax.spines.values(): spine.set_visible(False)

ax=axes[1]
x=np.linspace(0,1,150)
ax.plot(x,x,color=orange,lw=3)
ax.plot(-x,x,color=blue,lw=3)
ax.scatter([0],[0],s=65,color=purple,zorder=6)
ax.axhline(0,color="#b3b3b3",lw=.7)
ax.axvline(0,color="#b3b3b3",lw=.7)
ax.set(xlim=(-1.25,1.25),ylim=(-.16,1.25),xlabel="$x$",ylabel="$z$")
ax.set_xticks([-1,0,1]);ax.set_yticks([0,1])
ax.set_title("The compact graph $z=|x|$",fontsize=14,pad=12)
ax.text(.51,.35,"$h_+(x)=x$",color=orange,fontsize=12)
ax.text(-1.16,.35,"$h_-(x)=-x$",color=blue,fontsize=12)
ax.text(.12,.04,"same value, different germs",color=purple,fontsize=9)
for spine in ax.spines.values():spine.set_visible(False)

fig.text(.17,.22,r"$\Phi_+(u,v)=(u^2,u^2)$",ha="center",color=orange,fontsize=15)
fig.text(.83,.22,r"$\Phi_-(u,v)=(-u^2,u^2)$",ha="center",color=blue,fontsize=15)
fig.text(.50,.21,r"Both source circles have $E=\varnothing$.",ha="center",fontsize=12)
fig.text(.5,.075,r"Over $x=0$, a pair from opposite circles cannot share one analytic germ: $0\in\phi(E_2)$.",
         ha="center",fontsize=13,color=purple)
fig.suptitle("The fibre comparison detects what separate local descents miss",
             fontsize=18,y=.96)
fig.savefig(ROOT/"SH03-graphic-pair-obstruction.svg",bbox_inches="tight", metadata={"Date": None, "Creator": "GPT-6 Astra (Ultra); original programme illustration; CC0"})
plt.close(fig)
