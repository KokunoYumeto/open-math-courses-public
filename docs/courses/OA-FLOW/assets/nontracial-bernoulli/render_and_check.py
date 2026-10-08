"""Reproduce three original mathematical schematics and finite diagnostics.

Run: python render_and_check.py
The finite tests verify signs, constants, site composition and support products;
they do not replace the infinite analytic or all-weight proof in LESSON.md.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13,
                     "svg.fonttype": "none", "svg.hashsalt": "oa-flow-nb-20261008",
                     "axes.spines.top": False, "axes.spines.right": False})
NAVY, BLUE, TEAL, ORANGE, PALE = "#15334d", "#286cac", "#087f82", "#ba5d25", "#edf4f8"


def canvas(title, subtitle):
    fig, ax = plt.subplots(figsize=(15, 8), dpi=150)
    ax.set(xlim=(0, 15), ylim=(0, 8))
    ax.axis("off")
    ax.text(.55, 7.48, title, color=NAVY, fontsize=24, weight="bold")
    ax.text(.55, 6.95, subtitle, color=NAVY, fontsize=13)
    return fig, ax


def box(ax, xy, width, height, text, color=BLUE, size=15):
    patch = FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.12",
                          linewidth=1.6, edgecolor=color, facecolor=PALE)
    ax.add_patch(patch)
    ax.text(xy[0]+width/2, xy[1]+height/2, text, ha="center", va="center",
            color=NAVY, fontsize=size)


def arrow(ax, start, end, label="", color=TEAL, dy=.23):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18,
                                linewidth=2, color=color))
    if label:
        ax.text((start[0]+end[0])/2, (start[1]+end[1])/2+dy, label,
                ha="center", va="bottom", color=color, fontsize=14)


def save(fig, name):
    fig.savefig(HERE / (name+".png"), dpi=150, facecolor="white")
    fig.savefig(HERE / (name+".svg"), facecolor="white",
                metadata={"Date": "2026-10-08", "Creator": "Original OA-FLOW lesson renderer"})
    plt.close(fig)


fig, ax = canvas("One orbit of sites: the left Bernoulli movement",
                 "Site set = G.  Arrangement below is schematic; it assigns no metric to G.")
box(ax, (.7, 3.4), 3.1, 2.1, "finite local support F\n\noperators a, b")
for y, n in [(5.4, "n"), (3.9, "n+1"), (2.4, "n+2")]:
    box(ax, (5.25, y-.4), 2.1, .85, "$h_{"+n+"}$", TEAL)
    box(ax, (10.6, y-.4), 2.6, .85, "$g h_{"+n+"}$", ORANGE)
    arrow(ax, (7.55, y+.04), (10.35, y+.04), "$h\\mapsto gh$")
ax.text(.8, 2.6, "$h_n$ eventually leaves every finite $F$.", color=NAVY)
ax.text(5.2, 1.3, r"At the target site $r$, read the old coordinate $g^{-1}r$.", color=NAVY)
ax.text(.7, .55, r"$z_n=\mathrm{diag}(1,-1)$ at $h_n$: centralizing, but "
        r"$\|\beta_g(z_n)-z_n\|_\varphi^2=8\lambda/(1+\lambda)^2>0$ for $g\ne e$.",
        fontsize=15, color=NAVY)
save(fig, "site-tail")

fig, ax = canvas("Local eigenvectors generate the modular lattice",
                 "Frequency units = |log lambda|.  Positive-eigenvalue labels below use lambda = 1/2.")
box(ax, (.9, 4.5), 3.8, 1.2, "$e_{12}$: frequency $\\log\\lambda$\nunit coordinate $-1$", TEAL)
box(ax, (5.6, 4.5), 3.8, 1.2, "diagonal directions\nfrequency $0$", BLUE)
box(ax, (10.3, 4.5), 3.8, 1.2, "$e_{21}$: frequency $-\\log\\lambda$\nunit coordinate $+1$", ORANGE)
ax.plot([1.2, 13.8], [2.75, 2.75], color=NAVY, lw=1.5)
for j in range(-4, 5):
    x = 7.5 + j*1.45
    ax.scatter([x], [2.75], s=100, color=TEAL if j < 0 else ORANGE if j > 0 else BLUE)
    ax.text(x, 3.25, str(j), ha="center", color=NAVY)
    value = 2.0**j
    label = f"1/{int(1/value)}" if value < 1 else str(int(value))
    ax.text(x, 2.1, label, ha="center", color=NAVY)
ax.text(.85, 3.9, "Tensor frequencies add. Every integer occurs using finitely many distinct sites.", color=NAVY)
ax.text(.85, 1.1, r"Complete spectrum: $\{0\}\cup\lambda^{\mathbb{Z}}$."
        r"  Zero is the limit of $\lambda^n$ as $n\to+\infty$, not an eigenvalue.", color=NAVY)
ax.text(.85, .55, "The finite window is illustrative. At lambda = 1 the operator is exactly 1.", color=NAVY)
save(fig, "modular-lattice")

fig, ax = canvas("A fixed-corner sandwich retains the frequency",
                 "D is the factorial fixed algebra.  Boxes are supports, not equal-dimensional subspaces.")
box(ax, (.9, 3.2), 2.5, 1.4, "$eH$\nchosen corner", BLUE, 14)
box(ax, (5.0, 3.2), 2.5, 1.4, "$pH$\ninitial support\nof $ax$", TEAL, 13)
box(ax, (9.3, 3.2), 2.5, 1.4, "$qH$\nrange support\nof $x$", ORANGE, 13)
box(ax, (12.8, 3.2), 1.3, 1.4, "$eH$", BLUE, 14)
arrow(ax, (3.6, 3.9), (4.8, 3.9), "$b$", dy=.9)
arrow(ax, (7.7, 3.9), (9.1, 3.9), "$x$", ORANGE, dy=.9)
arrow(ax, (12.0, 3.9), (12.65, 3.9), "$a$", dy=.9)
ax.text(.85, 2.35, r"$a\in eDq$, $ax\ne0$;  $p=s((ax)^*(ax))$;  $b\in pDe$, $axb\ne0$.", color=NAVY)
ax.text(.85, 1.55, r"$a,b$: frequency zero.  $x$: frequency $k\log\lambda$."
        r"  $y=axb\in eRe$: the same frequency.", color=NAVY)
ax.text(.85, .75, r"Factor contact provides nonzero maps; support ranges and kernels prove the product is nonzero.",
        color=NAVY)
save(fig, "corner-sandwich")


def reduce_word(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def multiply(g, h):
    return reduce_word(g+h)


g, k, h = (1,), (2,), (-1, 2)
assert multiply(g, multiply(k, h)) == multiply(multiply(g, k), h)
assert multiply(g, multiply(k, h)) != multiply(k, multiply(g, h))
residuals = {}
samples = []
z = np.diag([1., -1.])
for lam in [.125, .5, .9, 1.]:
    rho = np.diag([lam, 1.])/(1+lam)
    rho2 = np.kron(rho, rho)
    moved_difference = np.kron(z, np.eye(2))-np.kron(np.eye(2), z)
    value = float(np.trace(rho2 @ moved_difference @ moved_difference))
    expected = 8*lam/(1+lam)**2
    residuals[f"tail_displacement_lambda_{lam}"] = abs(value-expected)
    residuals[f"state_normalization_lambda_{lam}"] = abs(np.trace(rho)-1)
    samples.append({"lambda":lam, "diagonal_mean":float(np.trace(rho@z)),
                    "squared_displacement":value, "proved_formula":expected})
    e12 = np.array([[0.,1.],[0.,0.]])
    residuals[f"modular_e12_lambda_{lam}"] = float(np.max(np.abs(rho@e12@np.linalg.inv(rho)-lam*e12)))
    # Swap of two identical sites lies in the fixed algebra.
    swap = np.eye(4)[[0,2,1,3],:]
    residuals[f"fixed_swap_lambda_{lam}"] = float(np.max(np.abs(swap@rho2-rho2@swap)))
    # Site Tomita relation on all four matrix units, in the HS model.
    sq = np.sqrt(rho)
    for i in range(2):
        for j in range(2):
            a = np.zeros((2,2)); a[i,j] = 1
            delta_half_aomega = sq @ (a@sq) @ np.linalg.inv(sq)
            residuals[f"tomita_{lam}_{i}{j}"] = float(np.max(np.abs(delta_half_aomega.T-a.T@sq)))

# A finite linear-map sample of the support composition, not a finite model of
# the theorem's factorial centralizer or its full infinite frequency spectrum.
e = np.diag([1.,0.,0.]); q = np.diag([0.,1.,0.]); p = np.diag([0.,0.,1.])
a = np.zeros((3,3)); a[0,1] = 2
x = np.zeros((3,3)); x[1,2] = 3
b = np.zeros((3,3)); b[2,0] = 5
assert np.linalg.norm(a@x@b) == 30
residuals["left_support_a"] = float(np.max(np.abs(e@a@q-a)))
residuals["right_support_b"] = float(np.max(np.abs(p@b@e-b)))
residuals["corner_sandwich"] = float(np.max(np.abs(e@(a@x@b)@e-a@x@b)))
assert max(residuals.values()) < 2e-12
models = {"scope":"Finite coordinate diagnostics and support schematic; infinite proofs remain in the lesson.",
          "site_set":"G itself; finite word sample only checks left multiplication in the free group",
          "left_action_word_sample":{"g":g,"k":k,"h":h,
                                    "g_k_h":multiply(g,multiply(k,h)),
                                    "k_g_h":multiply(k,multiply(g,h))},
          "state_samples":samples,
          "site_modular_exponents":[0,0,1,-1],
          "two_site_modular_exponents":[i+j for i in [0,0,1,-1] for j in [0,0,1,-1]],
          "corner_sample":{"a":a.tolist(),"x":x.tolist(),"b":b.tolist(),
                           "axb":(a@x@b).tolist(),"nonzero_norm":30,
                           "spectral_status":"Symbolic eigenfrequency rule in Figure 3; these sample matrices test support composition only."},
          "proof_locators":["NB2","NB6","NB9","NB19","NB24","nb-trace-endpoint"]}
checks = {"passed":True,"left_group_action_and_reversed_order_distinguished":True,
          "positive_displacement_including_trace_endpoint":True,
          "maximum_absolute_residuals":residuals,
          "maximum_absolute_residual":max(residuals.values()),
          "scope":"Finite formulas, domains in the one-site HS model, and support composition; no numerical inference of all-weight subtype."}
for name, value in [("models.json",models),("checks.json",checks)]:
    (HERE/name).write_text(json.dumps(value,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":True,"maximum_absolute_residual":max(residuals.values()),
                  "outputs":6,"state_samples":len(samples)}))
