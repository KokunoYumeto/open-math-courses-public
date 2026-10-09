from pathlib import Path
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, axs = plt.subplots(2, 2, figsize=(15.6, 10.6))
blue, red, grey = "#165e91", "#b84d35", "#69737a"

def setup(ax, title):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0, 1.025, title, fontsize=17, weight="bold",
            transform=ax.transAxes, va="bottom")

def box(ax, x, y, text, width=.88, color=blue, size=12.5):
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=color,
            bbox=dict(boxstyle="round,pad=.6", facecolor="#f5f8fb",
                      edgecolor=color, linewidth=1.3))

ax = axs[0, 0]
setup(ax, "1. An actual maximal torus (R.6–R.10)")
box(ax, .5, .88, r"Semisimple $G$  $\longrightarrow$  semisimple $\mathfrak{g}$")
box(ax, .5, .65, r"Maximal toral $\mathfrak{h}$:  $C_{\mathfrak{g}}(\mathfrak{h})=\mathfrak{h}$")
box(ax, .5, .42, r"$S=\overline{\exp(\mathrm{ad}\,\mathfrak{h})}\subset\mathrm{Ad}G$"
    "\n" r"$T=(\mathrm{Ad}^{-1}S)^0$ is a torus; $\mathrm{Lie}(T)=\mathfrak{h}$")
for y in [.79, .56]:
    ax.annotate("", (.5, y-.07), (.5, y),
                arrowprops=dict(arrowstyle="->", color=blue, lw=1.7))
ax.text(.5, .12, "Finite adjoint kernel removes the unipotent factor.\n"
        "Every maximal torus arises this way.", ha="center", va="center")

ax = axs[0, 1]
setup(ax, "2. The root-space mechanism (R.11–R.13)")
ax.text(.5, .88, r"$[e_\alpha,f_\alpha]=h_\alpha,\quad"
        r"[h_\alpha,e_\alpha]=2e_\alpha$", ha="center", color=blue, fontsize=14)
xs = [.16, .5, .84]
for x, label in zip(xs, [r"$f_\alpha$", r"$h_\alpha$", r"$e_\alpha$"]):
    box(ax, x, .62, label, width=.18)
for left, right in zip(xs[:-1], xs[1:]):
    ax.annotate("", (right-.08, .62), (left+.08, .62),
                arrowprops=dict(arrowstyle="->", color=blue, lw=1.5))
for x, coefficient in [(.33, "+1"), (.67, "−2")]:
    ax.text(x, .72, r"$\mathrm{ad}\,e_\alpha$" + "\n" + coefficient,
            ha="center", color=blue, fontsize=10.5)
for x, label in zip(xs, [r"$-2$", r"$0$", r"$2$"]):
    ax.text(x, .48, label, ha="center", fontsize=15)
ax.text(.5, .31, r"$K_\alpha/(\mathfrak{sl}_2\oplus\ker\alpha)$ has no weight $0$.",
        ha="center", fontsize=12)
ax.text(.5, .13, "A weight 4 forces a weight 0: no double root.\n"
        "A remaining weight ±2 also forces 0: root multiplicity is 1.",
        ha="center", va="center", color=red, fontsize=12)

ax = axs[1, 0]
ax.set_aspect("equal")
ax.set_xlim(-1.45, 1.7)
ax.set_ylim(-1.38, 1.48)
ax.axis("off")
ax.text(0, 1.02, "3. A₂ sample; general proof is R.14–R.15",
        transform=ax.transAxes, fontsize=16, weight="bold", va="bottom")
a1 = np.array([1., 0.])
a2 = np.array([-.5, math.sqrt(3)/2])
positive = [a1, a2, a1+a2]
labels = [r"$\alpha_1=(1,0)$",
          r"$\alpha_2=(-\frac{1}{2},\frac{\sqrt{3}}{2})$",
          r"$\alpha_1+\alpha_2$"]
for v, label in zip(positive, labels):
    ax.annotate("", v, (0, 0),
                arrowprops=dict(arrowstyle="->", color=blue, lw=2))
    offset = np.array([.08, .09]) if v[0] >= 0 else np.array([-.12, .11])
    ax.text(*(v+offset), label, fontsize=12, ha="left" if v[0] >= 0 else "right")
    ax.annotate("", -v, (0, 0),
                arrowprops=dict(arrowstyle="->", color=grey, lw=1.3))
ax.plot(0, 0, "o", color="#26313c", ms=4)
ax.text(.1, -1.2, r"$\|\alpha_i\|=1$; Cartan matrix [[2, −1], [−1, 2]]",
        ha="center", fontsize=12)

ax = axs[1, 1]
setup(ax, "4. Characters of this group (R.9, R.16)")
box(ax, .5, .84, r"$Q\ \subset\ X(T)\ \subset\ P$", size=22)
ax.text(.5, .62, r"$Q=\sum\mathbf{Z}\alpha,\quad"
        r"P=\{\mu\in E:\mu(h_i)\in\mathbf{Z}\}$",
        ha="center", fontsize=14)
box(ax, .5, .39, r"$2\rho=\sum_{\alpha>0}\alpha\in X(T)$"
    "\n" r"$(2\rho)(h_i)=2$", color=blue, size=15)
ax.text(.5, .12, "Lie integrality alone does not make a weight\n"
        "a character of the actual central quotient.", ha="center",
        color=red, fontsize=12.5)

fig.suptitle("Root foundations at arbitrary connected complex semisimple group scope",
             fontsize=21, weight="bold", y=.995)
fig.text(.5, .01, "General proof locators: R.1–R.16 in §5A.3a. "
         "The A₂ coordinates are an explanatory sample; the general proof applies in every rank.",
         ha="center", fontsize=10.5, color="#46525c")
fig.subplots_adjust(left=.06, right=.96, bottom=.065, top=.92,
                    hspace=.26, wspace=.18)
fig.savefig(ROOT/"root-foundations.png", dpi=160)
fig.savefig(ROOT/"root-foundations.svg")
(ROOT/"figure-data.json").write_text(json.dumps({
    "sample": "A2, not a hypothesis on the group",
    "simple_roots": {"alpha1": a1.tolist(), "alpha2": a2.tolist()},
    "positive_roots": [v.tolist() for v in positive],
    "cartan_matrix": [[2,-1],[-1,2]],
    "squared_root_lengths": 1,
    "general_proof_locators": ["R.6–R.10","R.11–R.13","R.14–R.15","R.16"],
    "schematic_is_not_an_embedding_or_numerical_sample_of_arbitrary_G": True
},indent=2)+"\n",encoding="utf8")
print("Rendered root-foundations.png and root-foundations.svg")
