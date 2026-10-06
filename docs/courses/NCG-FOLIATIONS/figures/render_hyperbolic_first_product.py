"""Original CC0 illustrations for the hyperbolic first-product supplement.

Reproduce with: python render_hyperbolic_first_product.py
Writes only beside this source.  Curves are numerical samples of exact formulas;
the commutator panel plots a proved upper bound, not measured commutators.

Human source context: Alain Connes, A survey of foliations and operator algebras,
Section 12, pp. 613--615; Alain Connes and Georges Skandalis, The longitudinal
index theorem for foliations; G. G. Kasparov, Clifford Bott/product framework.
Exact proof locators are supplied in captions.md for the integrating supplement.
"""
from pathlib import Path
import json
import math
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
BG = "#fbfcfe"
INK = "#26364e"
TEAL = "#00798a"
RUST = "#b25315"
PURPLE = "#8055a5"
GRAY = "#7b8798"
PALE = "#eef5f8"
PARAMETERS = (0.0, 0.5, 1.0)
COLORS = (INK, TEAL, RUST)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "mathtext.fontset": "dejavusans", "svg.fonttype": "none",
    "svg.hashsalt": "kt-hyperbolic-first-product-v1",
    "axes.titlesize": 16, "axes.labelsize": 13,
    "xtick.labelsize": 12, "ytick.labelsize": 12,
    "axes.edgecolor": "#526177", "axes.titlepad": 15,
    "savefig.facecolor": BG,
})

def note(ax, x, y, content, size=14, color=INK, weight="normal", **kw):
    return ax.text(x, y, content, transform=ax.transAxes, va="top",
                   fontsize=size, color=color, fontweight=weight, **kw)

def card(ax, title, color=TEAL):
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1,
                 boxstyle="round,pad=0.013,rounding_size=0.022",
                 transform=ax.transAxes, facecolor=PALE, edgecolor="#d4dfe8",
                 linewidth=1.2, clip_on=False))
    note(ax, .035, .955, title, size=17, color=color, weight="bold")

def footer(fig, locators):
    fig.text(.04, .071, locators, fontsize=11, color="#4d5c71")
    fig.text(.04, .048,
             "Human source context: Connes, Survey §12, pp. 613–615; "
             "Connes–Skandalis, longitudinal index context;",
             fontsize=11, color="#4d5c71")
    fig.text(.04, .025,
             "Kasparov, Clifford Bott/product framework. "
             "Original exact diagrams and formula samples; proof locators in the accompanying caption.",
             fontsize=11, color="#4d5c71")

def save(fig, stem, description):
    fig.savefig(ROOT / (stem+".png"), dpi=180)
    fig.savefig(ROOT / (stem+".svg"), metadata={
        "Title": stem.replace("-", " "), "Description": description,
        "Creator": "Matplotlib; original CC0 mathematical illustration",
        "Rights": "CC0 1.0", "Date": None,
    })
    plt.close(fig)

# Figure one: complete estimates and the finite calibration, separately typed.
fig = plt.figure(figsize=(18, 12.8), facecolor=BG)
gs = fig.add_gridspec(2, 6, left=.045, right=.976, bottom=.13, top=.87,
                      height_ratios=(1, 1.13), hspace=.47, wspace=.64)
ax_density = fig.add_subplot(gs[0, 0:2])
ax_angle = fig.add_subplot(gs[0, 2:4])
ax_tail = fig.add_subplot(gs[0, 4:6])
radius = np.linspace(0, 4, 601)
cutoff = np.linspace(1, 6, 601)
for lam, color in zip(PARAMETERS, COLORS):
    if lam == 0:
        density = np.ones_like(radius)
        angular = 1/cutoff
    else:
        density = np.divide(np.sinh(lam*radius), lam*radius,
                            out=np.ones_like(radius), where=radius != 0)
        angular = 2*np.sinh(lam/2)/np.sinh(lam*cutoff)
    ax_density.plot(radius, density, color=color, lw=2.5,
                    label=rf"$\lambda={lam:g}$; curvature ${(-lam**2 if lam else 0):g}$")
    ax_angle.plot(cutoff, angular, color=color, lw=2.5,
                  label=rf"$\lambda={lam:g}$")
ax_density.set(title="Source density", xlabel=r"$r=|v|$ in the scaled source metric",
               ylabel=r"$J_\lambda(r)$")
ax_density.legend(loc="upper left", fontsize=11)
note(ax_density, .04, .62, r"$J_\lambda(r)=\frac{\sinh(\lambda r)}{\lambda r}$"+
     "\n"+r"$J_0=1,\quad J_\lambda(0)=1$", size=13,
     bbox={"facecolor":"white", "edgecolor":"none", "alpha":.88})

angular_uniform = np.cosh(.5)/cutoff
full_uniform = angular_uniform+1/(1+cutoff**2)**1.5
ax_angle.plot(cutoff, angular_uniform, color=PURPLE, lw=2.5, ls="--",
              label=r"uniform: $\cosh(1/2)/R$")
ax_angle.set(title="Angular bound, propagation c = 1",
             xlabel=r"$R$: lower bound on both endpoint radii",
             ylabel=r"upper bound on $|v/r-w/s|$")
ax_angle.legend(loc="upper right", fontsize=11)

ax_tail.plot(cutoff, full_uniform, color=TEAL, lw=3,
             label="whole commutator-tail bound")
ax_tail.plot(cutoff, angular_uniform, color=PURPLE, lw=2, ls="--",
             label="angular term")
ax_tail.plot(cutoff, 1/(1+cutoff**2)**1.5, color=GRAY, lw=2, ls=":",
             label="radial-amplitude term")
ax_tail.set(title=r"Uniform tail bound, $K_f=c=1$",
            xlabel=r"cutoff radius $R$", ylabel="proved upper bound")
ax_tail.legend(loc="upper right", fontsize=11)
note(ax_tail, .37, .56,
     r"$\frac{\cosh(1/2)}{R}+\frac{1}{(1+R^2)^{3/2}}$", size=15,
     bbox={"facecolor":"white", "edgecolor":"none", "alpha":.88})
for ax in (ax_density, ax_angle, ax_tail):
    ax.grid(alpha=.18)
    ax.set_axisbelow(True)
fig.text(.046, .498,
         "Curves sample the exact density and proved upper bounds. "
         "The right panel contains no measured commutator norms.",
         fontsize=11.8, color="#4d5c71")

finite = fig.add_subplot(gs[1, 0:3])
product = fig.add_subplot(gs[1, 3:6])
card(finite, "The entire inverse module fixes the phase")
note(finite, .04, .83,
     "Canonical: "+r"$S=1\oplus L,\quad W=\overline{S}\,\widehat{\otimes}_P\Lambda F_{\mathbb{C}}=1\oplus L^*$",
     size=15)
note(finite, .04, .705,
     r"$\Gamma_W=\sigma_z,\qquad b_W=(\sigma_y,\sigma_x),\qquad -i b_{W,1}b_{W,2}=-\Gamma_W$",
     size=15)
note(finite, .04, .585,
     r"$R_x(v)=-\frac{b_{W,x}(v)}{\sqrt{1+|v|^2}}$", size=21)
note(finite, .39, .565, "calibrated inverse\nradial phase", size=13, color=TEAL)
note(finite, .04, .415,
     r"$\widehat f(p)=\int e^{-ip\cdot v}f(v)\,dv:\quad -b_Wv\longmapsto-i b_W\partial_p$",
     size=14)
note(finite, .04, .292,
     r"$S\widehat{\otimes} W\cong\Lambda F_{\mathbb{C}},\quad"
     r"\varepsilon\otimes1\mapsto a,\quad\Gamma_S\otimes b_W\mapsto b=i(e-\iota)$",
     size=14)
note(finite, .04, .16,
     "An even line twist is retained: S ⊗ H pairs with W ⊗ H*.\n"
     "Both full transition phases cancel, including torsion phases.",
     size=13)

card(product, "The first product and its exact scope")
note(product, .04, .83,
     r"$Q=\sum_j c_j\partial_{p_j}+\sum_j a_jp_j,\quad"
     r"Q^2=-\Delta+|p|^2+2N-2$", size=16)
note(product, .04, .685,
     "Entire kernel: Gaussian × exterior vacuum 1\n"
     "even, invariant, trivial C(V) line", size=15, color=TEAL)
note(product, .04, .502,
     r"$T\otimes_A\delta_{\mathrm{inv}}=1_{C(V)}\quad"
     r"\mathrm{in}\ KK(C(V),C(V))$", size=21, color=TEAL)
note(product, .04, .35, "This gives injectivity in both K degrees.", size=14)
note(product, .04, .235,
     r"Reverse product $\delta_{\mathrm{inv}}\otimes_{C(V)}T=1_A$ remains unproved.",
     size=15, color=RUST, weight="bold")
note(product, .04, .105,
     "The same positive spinor in both flat factors leaves an odd line.\n"
     "Its class is −[L]; with the twist H, it is −[L ⊗ H²].",
     size=12.6, color=PURPLE)
fig.suptitle("A calibrated first inverse for hyperbolic-plane leaves",
             fontsize=24, fontweight="bold", color=INK, y=.965)
fig.text(.5, .916,
         "Compact V · oriented rank-two F · actual complete curvature −1 disk leaves · full prescribed spin-c structure",
         ha="center", fontsize=14, color="#4d5c71")
footer(fig, "Proof: Theorem 11.1; Lemma 11.2 (calibration); Lemma 11.3, (H.14), (H.17)–(H.18) (estimates); Remark 11.6 (reverse product).")
save(fig, "kt-hyperbolic-first-product",
     "Exact source-density and angular-bound samples; complete uniform commutator-tail bound "
     "with K_f=c=1; full calibrated W and negative radial phase; even trivial Gaussian "
     "first-product line. The reverse product remains unproved.")

# Figure two: exact geometric slice and the changing representation.
fig = plt.figure(figsize=(17, 9.5), facecolor=BG)
gs = fig.add_gridspec(1, 2, left=.055, right=.97, bottom=.215, top=.82,
                      width_ratios=(1, 1.25), wspace=.18)
disk = fig.add_subplot(gs[0, 0])
flow = fig.add_subplot(gs[0, 1])
angle = np.linspace(0, 2*np.pi, 801)
disk.plot(np.cos(angle), np.sin(angle), color=GRAY, ls="--", lw=1.7)
disk.plot([-1, 1], [0, 0], color=INK, lw=1.8)
disk.scatter([0], [0], color=INK, s=95, zorder=5)
disk.text(-.14, -.125, r"$x=0$", fontsize=15, weight="bold", color=INK,
          bbox={"facecolor":BG,"edgecolor":"none","pad":1.5})
for lam, color, label_x, label_y in ((.5, TEAL, -.47, .43), (1., RUST, -.05, .70)):
    endpoint = math.tanh(lam)
    disk.scatter([endpoint], [0], color=color, s=95, zorder=6)
    disk.annotate(rf"$\lambda={lam:g}:\ y_\lambda=(\tanh {lam:g},0)$",
                  xy=(endpoint, 0), xytext=(label_x, label_y), color=color, fontsize=13,
                  bbox={"facecolor":BG,"edgecolor":"none","pad":2},
                  arrowprops={"arrowstyle":"->","color":color,"lw":1.7,
                              "shrinkA":7,"shrinkB":9})
disk.annotate("", xy=(0, -.255), xytext=(math.tanh(1), -.255),
              arrowprops={"arrowstyle":"->","color":TEAL,"lw":2.5})
disk.text(-.44, -.45, "Full spin-c transport back to x\nalong the specified radial geodesic",
          color=TEAL, fontsize=12.7, ha="left",
          bbox={"facecolor":BG,"edgecolor":"none","pad":4}, zorder=8)
disk.text(-.78, .88, "Excluded boundary |z| = 1", color="#5f6e82", fontsize=12,
          bbox={"facecolor":BG,"edgecolor":"none","pad":3}, zorder=8)
disk.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), aspect="equal",
         title=r"One leaf: $x=0$, $v=2e_1$",
         xlabel=r"Poincaré coordinate $z_1$", ylabel=r"Poincaré coordinate $z_2$")
disk.grid(alpha=.12)
card(flow, "One parameter module, changing left action")
note(flow, .04, .85,
     r"$s_\lambda(v)=x,\quad r_\lambda(v)=y_\lambda=\exp_x(\lambda v)$", size=19)
note(flow, .04, .735,
     r"$\xi(v)\in S_{y_\lambda}\widehat{\otimes} W_x$"+"\n"
     +r"left $h$: $h(y_\lambda)$; right $h$: $h(x)$", size=17)
note(flow, .04, .568,
     "The exact fixed-bundle unitary uses\n"
     "radial spin-c transport and density multiplication",
     size=15)
note(flow, .04, .46, r"$J_\lambda(v)^{1/2},\quad"
     r"J_\lambda(v)=\frac{\sinh(\lambda|v|)}{\lambda|v|},\quad J_0=1$", size=17)
note(flow, .04, .325,
     r"At $\lambda=0$: $y_0=x$, both actions are $h(x)$"+"\n"
     +r"$S_x\widehat{\otimes} W_x\cong\Lambda F_{x,\mathbb{C}}$"+"\n"
     +"Gaussian × 1 is the even trivial line", size=16, color=TEAL)
note(flow, .04, .105,
     "A scalar source stays fixed through the first-product homotopy.\n"
     "The reverse A,A product needs a separate convolution-compatible proof.",
     size=12.5, color=RUST)
fig.suptitle("The range contracts to the fixed source",
             fontsize=25, color=INK, weight="bold", y=.966)
fig.text(.5, .91,
         r"Exact slice: $y_\lambda=\tanh(\lambda|v|/2)\,v/|v|=(\tanh\lambda,0)$; "
         r"original curvature $-1$ distance $d(x,y_\lambda)=2\lambda$",
         ha="center", fontsize=15, color="#4d5c71")
fig.text(.055, .115,
         "This is one Poincaré-coordinate slice, not a global embedding of leaf images in V. "
         "The leaves themselves are disks under the stated hypotheses.",
         fontsize=12, color="#4d5c71")
footer(fig, "Proof: Lemma 11.5, (H.30)–(H.31) (range action); Lemma 11.2 (whole finite evaluation); Theorem 11.1 (Gaussian).")
save(fig, "kt-hyperbolic-range-action",
     "Exact Poincare disk slice x=0, v=2e1, y_lambda=(tanh lambda,0); full spin-c "
     "radial transport to the fixed source and J_lambda square-root density unitary; "
     "changing scalar range action and even trivial Gaussian endpoint. The reverse "
     "convolution product requires a separate proof.")

# Small numerical receipt documents the exact plotted formulas and limits.
receipt = {
    "license": "CC0 1.0",
    "runtime": {"matplotlib":matplotlib.__version__, "numpy":np.__version__},
    "first_product_scope": "compact V, oriented rank-two F, actual complete curvature -1 disk leaves",
    "parameters": list(PARAMETERS),
    "density_r_interval": [0, 4], "tail_R_interval": [1, 6],
    "density_formula": "sinh(lambda*r)/(lambda*r), continued by 1 at lambda*r=0",
    "angular_formula_positive_lambda": "2*sinh(lambda/2)/sinh(lambda*R)",
    "angular_formula_zero_lambda": "1/R",
    "uniform_full_tail_formula": "cosh(1/2)/R+1/(1+R^2)^(3/2)",
    "tail_constants": {"K_f":1,"c":1},
    "tail_is_sample_of_proved_bound": True, "tail_is_actual_commutator_data": False,
    "poincare_endpoints": {str(lam): [math.tanh(lam), 0] for lam in (.5, 1.)},
    "calibrated_radial_phase": "-b_W(v)/sqrt(1+|v|^2)",
    "calibrated_class": "delta_inv",
    "native_positive_spinor_delta_is_distinct": True,
    "ground_line": "even trivial C(V) line, entire H and H* transitions cancel",
    "reverse_product_proved": False,
    "files": ["kt-hyperbolic-first-product.png", "kt-hyperbolic-first-product.svg",
              "kt-hyperbolic-range-action.png", "kt-hyperbolic-range-action.svg"],
}
assert np.all(full_uniform >= angular_uniform)
assert abs(math.tanh(.5)-.46211715726000974)<1e-14
assert abs(math.tanh(1)-.7615941559557649)<1e-14
receipt["sha256"] = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                      for name in receipt["files"]}
(ROOT / "figure-receipt.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"figures":receipt["files"], "reverse_product_proved":False}))
