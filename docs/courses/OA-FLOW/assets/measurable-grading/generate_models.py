"""Exact scalar-core translation model; no source documents or font copies."""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
s = 1 / 4
indices = list(range(-3, 2))
masses = [(1 + math.exp(-1)) * (1 - math.exp(-s)) * math.exp(-2*n) / (2*math.pi)
          for n in indices]
data = {
    "translation": {"s": "1/4", "theta_s_f": "f(q-s)"},
    "trace": "tau(f) = (1/(2*pi))*integral exp(-q)*f(q) dq",
    "strips": "[2n,2n+s) union [2n+1,2n+1+s), n in Z",
    "exact_mass": "m_n(s)=(1+exp(-1))*(1-exp(-s))*exp(-2*n)/(2*pi)",
    "finite_display_indices": indices,
    "display_masses": masses,
    "proved_divergence": "m_{-k}(s) tends to infinity for fixed 0<s<1; see MG14-MG15",
    "claim_boundary": "Finite plot illustrates exact formula; it is not numerical proof of an infinite sum."
}
(OUT / "model-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
fig, (top, bottom) = plt.subplots(2, 1, figsize=(11, 7.1), layout="constrained",
                                 gridspec_kw={"height_ratios": [1, 1.25]})
for n in indices:
    top.add_patch(Rectangle((2*n, 1.5), 1, .36, color="#34698d"))
    top.add_patch(Rectangle((2*n+s, .85), 1, .36, color="#48845d"))
    for start in (2*n, 2*n+1):
        top.add_patch(Rectangle((start, .2), s, .36, color="#ca7035"))
top.set_xlim(-6.2, 3.5)
top.set_ylim(0, 2.1)
top.set_yticks([1.68, 1.03, .38], [r"$f=1$", r"$\theta_{1/4}f=1$", r"$|\theta_{1/4}f-f|=1$"])
top.set_xticks(range(-6, 4))
top.set_xlabel(r"Scalar core coordinate $q$ (finite window)")
top.set_title("Narrow translated strips cannot be discarded at finite trace cost", loc="left", weight="bold")
top.spines[["top", "right", "left"]].set_visible(False)
top.tick_params(axis="y", length=0)
bottom.bar(indices, masses, color="#ca7035", width=.56)
bottom.set_yscale("log")
bottom.set_xticks(indices)
bottom.set_ylim(min(masses)/2, max(masses)*4)
bottom.set_xlabel(r"Strip-pair index $n$; the full model uses every $n\in\mathbb{Z}$")
bottom.set_ylabel(r"Discarded trace $m_n(1/4)$ (log scale)")
bottom.set_title(r"Exact mass: $m_n(s)=\frac{(1+e^{-1})(1-e^{-s})}{2\pi}\,e^{-2n}$", loc="left", pad=14)
for n,m in zip(indices,masses):
    bottom.text(n,m*1.22,f"{m:.4g}",ha="center",va="bottom",fontsize=10)
bottom.grid(axis="y", alpha=.22)
bottom.set_axisbelow(True)
bottom.spines[["top", "right"]].set_visible(False)
fig.suptitle(r"$\tau(f)=\frac{1}{2\pi}\int e^{-q}f(q)\,dq$     |     $\theta_s f(q)=f(q-s)$", fontsize=13)
fig.savefig(OUT / "time-and-measure.png", dpi=160)
fig.savefig(OUT / "time-and-measure.svg")
plt.close(fig)
print(json.dumps({"files": ["time-and-measure.png", "time-and-measure.svg", "model-data.json"],
                  "finite_masses": masses}))

# Exact two-coordinate model: g_p(a,b)=(|a|**(1/p)+|b|**(1/p))**p.
fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.2), layout="constrained")
x = np.linspace(0, 1, 701)
for ax, p, label in zip(axes, [.5, 1, 2], ["1/2", "1", "2"]):
    y = np.maximum(0, 1 - x**(1/p))**p
    ax.fill_between(x, 0, y, color="#d7e5ee")
    ax.plot(x, y, color="#34698d", linewidth=2.3)
    ax.plot([0,1],[1,0], color="#7d8286", linestyle="--", linewidth=1)
    ax.scatter([1,0],[0,1], color="#34698d", s=30, zorder=3)
    ax.scatter([.5],[.5],color="#ca7035",s=40,zorder=4)
    midpoint = 2**(p-1)
    ax.set_title(r"Grade $p="+label+r"$"+"\n"+r"$g_p(1/2,1/2)="+({.5:r"1/\sqrt{2}",1:"1",2:"2"}[p])+"$",pad=12)
    ax.set_xlim(-.05,1.06); ax.set_ylim(-.05,1.06)
    ax.set_aspect("equal")
    ax.set_xticks([0,.5,1]); ax.set_yticks([0,.5,1])
    ax.set_xlabel(r"Coefficient $a\geq0$")
    ax.set_ylabel(r"Coefficient $b\geq0$")
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(alpha=.15)
fig.suptitle(r"Two orthogonal state densities: $g_p(a h_1^p+b h_2^p)=(|a|^{1/p}+|b|^{1/p})^p$"+"\nShaded: gauge at most one. Orange: midpoint of the two unit vectors.",fontsize=12)
fig.savefig(OUT / "norm-and-quasinorm.png", dpi=160)
fig.savefig(OUT / "norm-and-quasinorm.svg")
plt.close(fig)
(OUT / "norm-data.json").write_text(json.dumps({
    "algebra":"C direct-sum C", "densities":"h_1,h_2 of the two coordinate states; orthogonal supports",
    "gauge":"(|a|^(1/p)+|b|^(1/p))^p", "positive_quadrant_unit_boundary":"b=(1-a^(1/p))^p, 0<=a<=1",
    "grades":["1/2","1","2"], "midpoint_gauges":["1/sqrt(2)","1","2"],
    "sum_gauge":"g_p(h_1^p+h_2^p)=2^p", "proof":"GI22 and HD10"},indent=2)+'\n',encoding='utf-8')
print(json.dumps({"files":["norm-and-quasinorm.png","norm-and-quasinorm.svg","norm-data.json"]}))
