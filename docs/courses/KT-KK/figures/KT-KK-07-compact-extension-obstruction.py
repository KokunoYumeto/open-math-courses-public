"""Exact finite residual matrices of Theorem D.1; reproducible CC0 figure."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = Path(__file__).resolve().parent
s0 = np.diag([1, -1])
s1 = np.diag([-1, 1])
delta = s0-s1
assert np.array_equal(delta, np.diag([2,-2]))
assert np.count_nonzero(np.linalg.eigvalsh(delta) == 2) == 1
fig, ax = plt.subplots(figsize=(10.8,4.1), dpi=150)
ax.set_xlim(0, 10.8)
ax.set_ylim(0, 4.1)
ax.axis("off")
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.12",
                 linewidth=1.1,edgecolor=color,facecolor="#fafcff"))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=11.5,color="#182a3d")

ax.text(5.4,3.85,"One split extension, a nonzero compact-homology class",
        ha="center",va="center",fontsize=16,weight="bold",color="#182a3d")
box(.35,1.75,3.0,1.35,
    "$x\\oplus y$\n$S_0=\\mathrm{diag}(1,-1)$\n$S_1=\\mathrm{diag}(-1,1)$",
    "#345b8c")
box(6.8,2.1,3.6,.92,
    "Ext: $q_L(\\mathrm{diag}(a_{00},a_{11}))=q_L(a)$\nLift: $a\\mapsto a$; class $0$",
    "#23795b")
box(6.8,.55,3.6,1.05,
    "$KK_c$: $S_0-S_1=\\mathrm{diag}(2,-2)$\n$\\mu=\\dim\\ker(S_0-S_1-2)=1$",
    "#a14449")
ax.annotate("",xy=(6.6,2.55),xytext=(3.5,2.55),
            arrowprops=dict(arrowstyle="->",lw=1.5,color="#23795b"))
ax.text(5.05,2.72,"compression (B.D.4)",ha="center",fontsize=11,color="#23795b")
ax.annotate("",xy=(6.6,1.07),xytext=(3.5,2.0),
            arrowprops=dict(arrowstyle="->",lw=1.5,color="#a14449"))
ax.text(5.0,1.2,"finite invariant (B.C.6)",ha="center",fontsize=11,color="#a14449")
ax.text(1.85,.65,"$H=\\ell^2(\\mathbb{N})$, $L=H\\oplus H$\n"
        "A: diagonal blocks B(H)\ncompact off-diagonal blocks",
        ha="center",va="center",fontsize=11,color="#182a3d")
fig.tight_layout(pad=.3)
fig.savefig(out/"KT-KK-07-compact-extension-obstruction.svg",bbox_inches="tight")
fig.savefig(out/"KT-KK-07-compact-extension-obstruction.png",bbox_inches="tight")
print({"S0":s0.tolist(),"S1":s1.tolist(),"difference":delta.tolist(),"mu":1})
