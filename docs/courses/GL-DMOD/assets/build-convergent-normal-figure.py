"""Reproduce the exact normal-gauge and balanced-comparison diagram."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
out = parser.parse_args().output_dir
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 17,
                     "svg.hashsalt": "GL-DMOD-CN-exact-v1"})
fig = plt.figure(figsize=(16, 11), dpi=150, facecolor="#f7f9fc")
a = fig.add_axes([0, 0, 1, 1])
a.set(xlim=(0, 16), ylim=(0, 11))
a.axis("off")
ink, blue, green, muted = "#14263f", "#155ca5", "#17765d", "#52627a"

def text(x, y, value, size=19, color=ink):
    a.text(x, y, value, ha="center", va="center", fontsize=size, color=color)

def box(x, y, w, h, value, size=19):
    a.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,
        boxstyle="round,pad=0.08,rounding_size=0.09",
        facecolor="white",edgecolor=blue,linewidth=1.5))
    text(x,y,value,size)

def arrow(p, q):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=17,lw=1.7,color=blue))

text(8,10.5,"An actual infinite-order gauge for convergent normal connections",23)
text(8,9.97,r"$T(h)\ \mathrm{convergent},\quad T(0)=N\ \mathrm{nilpotent},\quad h=D_t^{-1}$",20,muted)
box(3.8,8.85,6.6,1.15,r"$Y'=T(1/\zeta)Y$"+"\n"+r"$Y(w+2\pi i)=Y(w)M$",21)
box(12.1,8.85,6.6,1.15,r"$V=Ye^{-wH},\quad W=e^{wH}Y^{-1}$"+"\n"+r"$w=\log\zeta,\quad e^{2\pi iH}=M$",21)
arrow((7.28,8.85),(8.62,8.85))
text(8,7.75,"Single-valued on an exterior annulus; both inverse matrices have the same growth bound.",16,muted)
box(8,6.89,14.5,1.05,
    r"$\|V(\zeta)\|+\|W(\zeta)\|\leq K|\zeta|^b e^{L|\zeta|^\alpha},\quad \alpha=1-1/\max(2,\ell)<1$",
    20)
text(8,6.13,r"$\ell=\mathrm{largest\ Jordan\ block\ length\ of}\ N$"+"   [CN.9–CN.13]",17,muted)
arrow((8,5.85),(8,5.42))
box(8,4.90,14.5,.86,
    r"$\|V_j\|,\|W_j\|\leq K_\epsilon\epsilon^j/j!\ (j\geq0),\quad"
    r"\|V_{-n}\|,\|W_{-n}\|\leq KR_1^n\ (n\geq1)$",20)
text(8,4.20,r"$V(\tau),W(\tau)\in\mathrm{GL}_r(B),\quad VW=WV=I,\quad A=(H-I)^{\mathsf{T}}$"
    +"   [CN.14–CN.20]",20,green)
a.plot([.65,15.35],[3.76,3.76],color="#d7dfea",lw=1.2)
text(3.65,3.10,r"$B\otimes_E N_A$",25)
text(12.05,3.10,r"$B\otimes_E M_T$",25)
arrow((5.58,3.10),(10.10,3.10))
text(7.85,3.44,r"$e_j\mapsto\sum_k V_{kj}u_k\quad(\simeq)$",20)
text(3.65,1.49,r"$C\otimes_E N_A$",25)
text(12.05,1.49,r"$C\otimes_E M_T$",25)
arrow((5.58,1.49),(10.10,1.49))
text(7.85,1.13,r"$C\otimes_B(\,\cdot\,),\quad(\simeq)$",20)
arrow((3.65,2.75),(3.65,1.85))
arrow((12.05,2.75),(12.05,1.85))
text(1.91,2.30,"injective\nAM.29",17,green)
text(13.95,2.30,"injective\nCN.21",17,green)
text(8,.48,"For t²Dₜ + 1: N² = 0, α = 1/2.  Exact maps and proved bounds; no numerical solution sample.",17,muted)
fig.savefig(out/"convergent-normal-regularization.png",dpi=150)
fig.savefig(out/"convergent-normal-regularization.svg",metadata={"Date":None})
plt.close(fig)
data = {
    "kind": "exact maps and proved bounds; no numerical samples",
    "hypotheses": ["T(h) converges at h=0", "N=T(0) nilpotent", "tangential relations D_x u=0"],
    "normal_equation": "Y'=T(1/zeta)Y",
    "monodromy": "Y(w+2 pi i)=Y(w)M; exp(2 pi i H)=M",
    "gauge": {"V":"Y exp(-wH)", "W":"exp(wH) Y^-1", "products":"VW=WV=I",
              "Euler_matrix":"(H-I)^transpose", "proof":"CN.7–CN.20"},
    "growth": {"alpha":"1-1/max(2,largest nilpotent block length)",
               "bound":"K |zeta|^b exp(L |zeta|^alpha)", "proof":"CN.9–CN.16"},
    "comparison": {"top":"B tensor_E N_A -> B tensor_E M_T",
                   "bottom":"C tensor_E N_A -> C tensor_E M_T",
                   "horizontal_maps":"actual inverse gauge isomorphisms",
                   "left_vertical":"AM.29 injective", "right_vertical":"CN.21 injective",
                   "flatness_of_C_over_B_assumed":False},
    "example": {"P":"t^2 D_t+1", "N":[[0,0],[1,0]],
                "T":[["0","-h"],["1","2h"]], "alpha":"1/2", "proof":"CN.22–CN.23"}
}
(out/"convergent-normal-regularization-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
