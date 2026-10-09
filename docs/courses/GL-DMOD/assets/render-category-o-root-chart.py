"""Exact A2 chart and weight data for O.15--O.22. CC0."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).resolve().parent
alpha1 = np.array([1.0, 0.0])
alpha2 = np.array([-0.5, np.sqrt(3)/2])
mu = -alpha2
s1 = np.array([[-1, 1], [0, 1]], dtype=int)
s2 = np.array([[1, 0], [1, -1]], dtype=int)
w = s1 @ s2
rho_root_coefficients = np.array([1, 1], dtype=int)
assert tuple(w @ rho_root_coefficients) == (-1, 0)
positive_roots = {(1, 0), (0, 1), (1, 1)}
w_negative = {tuple(w @ -np.array(root)) for root in positive_roots}
assert w_negative & positive_roots == {(1, 0), (1, 1)}
assert w_negative - positive_roots == {(0, -1)}
assert tuple(-w @ rho_root_coefficients-rho_root_coefficients) == (0, -1)
roots = [
    ((1, 0), r"$\alpha_1$", "tangent", alpha1),
    ((1, 1), r"$\alpha_1+\alpha_2$", "tangent", alpha1+alpha2),
    ((0, -1), r"$-\alpha_2$", "normal", -alpha2),
]
data = {
    "root_system": "A2",
    "w": "s1 s2 (right reflection acts first)",
    "euclidean_simple_roots": [[1, 0], [-0.5, "sqrt(3)/2"]],
    "w_rho_simple_root_coefficients": [-1, 0],
    "Sigma_w_simple_root_coefficients": [[1, 0], [1, 1]],
    "Gamma_w_simple_root_coefficients": [[0, -1]],
    "mu_w_simple_root_coefficients": [0, -1],
    "weight_sample": [
        {"a": a, "b": b, "weight_simple_root_coefficients": [-a, -b-1],
         "multiplicity": min(a, b)+1,
         "basis_exponents": [
             {"z_alpha1": a-k, "z_alpha1_plus_alpha2": k,
              "normal_derivative_minus_alpha2": b-k}
             for k in range(min(a,b)+1)
         ]}
        for a in range(5) for b in range(5)
    ],
    "proof_locators": ["O.15-O.22", "O.33-O.34"],
    "status": "Finite displayed portion of an infinite module; all data exact"
}
for entry in data["weight_sample"]:
    assert len(entry["basis_exponents"]) == entry["multiplicity"]
    for exponents in entry["basis_exponents"]:
        r=exponents["z_alpha1"]; s=exponents["z_alpha1_plus_alpha2"]
        k=exponents["normal_derivative_minus_alpha2"]
        assert [-r-s, -1-s-k] == entry["weight_simple_root_coefficients"]
(OUT/"category-o-root-chart-data.json").write_text(json.dumps(data, indent=2))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig = plt.figure(figsize=(15.8, 8.8), facecolor="#fbfbf8")
gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.23], height_ratios=[1, .29],
                     left=.05, right=.97, top=.86, bottom=.10, wspace=.21, hspace=.16)
ax = fig.add_subplot(gs[0,0])
ax.set_aspect("equal"); ax.axis("off")
blue = "#2369a1"; red = "#b7483a"
for _, label, kind, v in roots:
    color = blue if kind == "tangent" else red
    ax.add_patch(FancyArrowPatch((0,0), tuple(v), arrowstyle="-|>",
                                mutation_scale=18, linewidth=2.8, color=color))
    p=v*1.23
    ax.text(*p, label, ha="center", va="center", color=color, fontsize=15)
ax.scatter([0],[0], s=45, color="#253243")
ax.text(-.04,.065, r"$wB$", ha="right", fontsize=12)
ax.set_xlim(-.47, 1.53); ax.set_ylim(-1.36, 1.23)
ax.set_title(r"Point-coordinate root weights in $V_w$", fontsize=16, pad=13)
ax.text(-.35,-1.26,
        r"$C_w=\{t_{-\alpha_2}=0\}\subset V_w\cong\mathbb{A}^3$",
        fontsize=14, color="#253243")

aw = fig.add_subplot(gs[0,1])
aw.set_aspect("equal"); aw.axis("off")
for a in range(5):
    for b in range(5):
        q=mu-a*alpha1-b*alpha2
        if a<4:
            qq=mu-(a+1)*alpha1-b*alpha2
            aw.plot([q[0],qq[0]],[q[1],qq[1]],color="#d6dce1",lw=.85,zorder=0)
        if b<4:
            qq=mu-a*alpha1-(b+1)*alpha2
            aw.plot([q[0],qq[0]],[q[1],qq[1]],color="#d6dce1",lw=.85,zorder=0)
        aw.scatter(*q,s=245,facecolor="#e5edf5",edgecolor=blue,lw=1.2,zorder=2)
        aw.text(*q,str(min(a,b)+1),ha="center",va="center",fontsize=12,zorder=3)
aw.scatter(*mu,s=290,facecolor="#f6d9d2",edgecolor=red,lw=1.8,zorder=4)
aw.text(*mu,"1",ha="center",va="center",fontsize=12,zorder=5)
aw.text(*(mu+np.array([.17,.20])),r"$\mu_w=-\alpha_2$",fontsize=14,color=red)
aw.annotate(r"$-\alpha_1$",xy=mu-1.32*alpha1,xytext=mu-0.42*alpha1+np.array([0,.39]),
            arrowprops={"arrowstyle":"->","color":"#253243"},fontsize=12)
aw.annotate(r"$-\alpha_2$",xy=mu-1.35*alpha2,xytext=mu-0.85*alpha2+np.array([.51,.23]),
            arrowprops={"arrowstyle":"->","color":"#253243"},fontsize=12)
aw.set_xlim(-4.5,2.85); aw.set_ylim(-4.83,.0)
aw.set_title(r"Weight $\mu_w-a\alpha_1-b\alpha_2$: multiplicity",fontsize=16,pad=13)
aw.text(-4.3,-4.73,r"$0\leq a,b\leq4$ shown; the basis continues.",fontsize=11,color="#435568")

at=fig.add_subplot(gs[1,:]); at.axis("off")
at.text(.01,.90,r"Tangent variables:  $z_{\alpha_1},z_{\alpha_1+\alpha_2}$"
        r"     |     Normal jets:  $\partial_{t_{-\alpha_2}}^k\delta_w$",
        color="#253243",fontsize=14)
at.text(.01,.48,r"$\operatorname{wt}\!\left(z_{\alpha_1}^{r}"
        r"z_{\alpha_1+\alpha_2}^{s}\partial_t^k\delta_w\right)"
        r"=-\alpha_2-r\alpha_1-s(\alpha_1+\alpha_2)-k\alpha_2$",
        fontsize=16,color="#253243")
at.text(.01,.05,r"$a=r+s,\quad b=s+k,\quad0\leq s\leq\min(a,b)$"
        r"     $\Longrightarrow$     multiplicity $=\min(a,b)+1$",
        fontsize=14,color="#253243")
fig.suptitle(r"Actual root-chart basis and the global Verma weight"
             "\n"+r"$A_2,\quad w=s_1s_2,\quad \mu_w=-w\rho-\rho=-\alpha_2$",
             fontsize=20, x=.5, y=.97, color="#203042")
fig.text(.05,.035,"Proof: O.15–O.22 and O.33–O.34. Exact roots; finite weight sample. CC0.",
         fontsize=11,color="#435568")
fig.savefig(OUT/"category-o-root-chart.png",dpi=180)
fig.savefig(OUT/"category-o-root-chart.svg")
plt.close(fig)
print("Rendered category-o-root-chart.png and SVG; exact data retained.")
