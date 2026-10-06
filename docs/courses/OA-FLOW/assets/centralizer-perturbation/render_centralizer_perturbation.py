"""CC0-1.0. Exact finite samples of the CZ-8 integer-indexed example."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.labelsize": 11,
    "svg.hashsalt": "oa-flow-centralizer-cz8-exact",
    "savefig.facecolor": "#fbfcfe",
})
navy, teal, orange, pale = "#153147", "#087f8c", "#c66526", "#e8f4f4"
fig = plt.figure(figsize=(14, 9), facecolor="#fbfcfe")
gs = fig.add_gridspec(2, 2, left=.075, right=.94, top=.84, bottom=.09,
                     hspace=.41, wspace=.32, width_ratios=[1.05, 1])
fig.suptitle("Unbounded density, full finite domains, exact cocycle",
             x=.5, y=.963, fontsize=19, fontweight="bold", color=navy)
fig.text(.5, .913,
         r"$M=\ell^\infty(\mathbb{Z})$,  $\varphi(a)=\sum_n a_n$,  "
         r"$h_n=2^n$,  $\varphi_h(a)=\sum_n2^n a_n$",
         ha="center", fontsize=14, color=navy)

ax = fig.add_subplot(gs[0, 0])
indices = np.arange(-6, 7)
density = np.array([float(Fraction(2) ** int(n)) for n in indices])
ax.axvspan(-2.45, 2.45, color=pale)
ax.plot(indices, density, "o-", color=teal, lw=2, ms=6)
ax.set_yscale("log", base=2)
ax.set_xticks(indices[::2])
ax.set_yticks([2.**j for j in [-6, -3, 0, 3, 6]],
             [r"$2^{-6}$", r"$2^{-3}$", r"$1$", r"$2^3$", r"$2^6$"])
ax.set_xlabel("coordinate n (finite displayed sample)")
ax.set_ylabel(r"$h_n=2^n$")
ax.set_title("Spectral bands grow to the whole domain", loc="left",
             color=navy, pad=14)
ax.text(0, 2**-5.3, r"$p_4=1_{[1/4,4]}(h)$"+"\nexactly −2 ≤ n ≤ 2",
        ha="center", color=navy, fontsize=10)
ax.annotate("h → ∞", xy=(6, 64), xytext=(3.7, 40),
            arrowprops=dict(arrowstyle="->", color=navy), color=navy)
ax.annotate("h → 0; h⁻¹ → ∞", xy=(-6, 1/64), xytext=(-6, .105),
            arrowprops=dict(arrowstyle="->", color=navy), color=navy, fontsize=10)
ax.grid(axis="y", alpha=.17)

ax = fig.add_subplot(gs[0, 1])
theta = np.linspace(0, 2*np.pi, 401)
ax.plot(np.cos(theta), np.sin(theta), color="#b5c9d2", lw=1.5)
phases = [(1, 0), (0, 1), (-1, 0), (0, -1)]
labels = [r"$n=4k:\ 1$", r"$n=4k+1:\ i$",
          r"$n=4k+2:\ -1$", r"$n=4k+3:\ -i$"]
for (x, y), label in zip(phases, labels):
    ax.plot([0, x], [0, y], color=teal, alpha=.4)
    ax.plot(x, y, "o", color=teal, ms=8)
    ax.text(1.20*x, 1.20*y, label,
            ha="left" if x > 0 else "right" if x < 0 else "center",
            va="center", color=navy, fontsize=11)
ax.annotate("", xy=(.24, .97), xytext=(.96, .27),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.32",
                            color=orange, lw=2))
ax.text(0, .06, r"$i^n$", ha="center", fontsize=16, color=navy)
ax.text(0, -.27, "positive phase", ha="center", fontsize=10, color=orange)
ax.set_xlim(-1.65, 1.65); ax.set_ylim(-1.48, 1.48)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(r"At $t_0=\pi/(2\log2)$: $(D\varphi_h:D\varphi)_{t_0}=i^n$",
             color=navy, loc="left", pad=14)
ax.text(0, -1.43, r"$\sigma^\varphi=\sigma^{\varphi_h}=\mathrm{id}$"
        " still does not determine this cocycle",
        ha="center", fontsize=10, color=navy)

ax = fig.add_subplot(gs[1, 0]); ax.axis("off")
ax.set_title("Neither finite ideal contains the other", color=navy,
             loc="left", pad=14)
ax.text(.02, .91, r"$x_n=2^{-n/2}$ for $n\geq0$; 0 otherwise",
        transform=ax.transAxes, color=orange, fontsize=12)
ax.text(.04, .70, r"$\varphi(x^*x)=2$"+"     "+r"$\varphi_h(x^*x)=\infty$",
        transform=ax.transAxes, color=navy, fontsize=14)
ax.text(.04, .55, r"$x\in N_\varphi\setminus N_{\varphi_h}$",
        transform=ax.transAxes, color=orange, fontsize=13)
ax.text(.02, .32, r"$y_n=1$ for $n\leq-1$; 0 otherwise",
        transform=ax.transAxes, color=teal, fontsize=12)
ax.text(.04, .12, r"$\varphi(y^*y)=\infty$"+"     "+r"$\varphi_h(y^*y)=1$",
        transform=ax.transAxes, color=navy, fontsize=14)
ax.text(.04, -.035, r"$y\in N_{\varphi_h}\setminus N_\varphi$",
        transform=ax.transAxes, color=teal, fontsize=13)

ax = fig.add_subplot(gs[1, 1]); ax.axis("off")
ax.set_title("The shift fixes the base weight and scales the trace",
             color=navy, loc="left", pad=14)
ax.text(.02, .89, r"$(\beta a)_n=a_{n-1}$,  $H_n=2^n$",
        transform=ax.transAxes, color=navy, fontsize=13)
ax.text(.02, .70, r"$\varphi\circ\beta=\varphi$,  $\beta(H)=H/2$",
        transform=ax.transAxes, color=navy, fontsize=13)
ax.text(.02, .48, r"$\tau=\varphi_{H^{-1}}$,  $\tau(a)=\sum_n2^{-n}a_n$",
        transform=ax.transAxes, color=navy, fontsize=13)
ax.text(.02, .26,
        r"$\tau(\beta a)=\sum_m2^{-(m+1)}a_m=\frac{1}{2}\tau(a)$",
        transform=ax.transAxes, color=teal, fontsize=14)
ax.text(.02, .045, "Exact infinite sums; finite window above is illustrative.",
        transform=ax.transAxes, color=navy, fontsize=10)

fig.text(.075, .025,
         "CZ-3: full finite-domain criterion   •   CZ-6: balanced normalization   "
         "•   CZ-7–8: exact scaling and examples", fontsize=10, color=navy)
for ax in fig.axes:
    for spine in ax.spines.values():
        spine.set_color("#b5c9d2")
fig.savefig(OUT / "centralizer-density-domains.png", dpi=200,
            metadata={"Software": "Original reproducible OA-FLOW CZ-8 figure"})
fig.savefig(OUT / "centralizer-density-domains.svg",
            metadata={"Date": None, "Creator": "Original OA-FLOW CZ-8 construction"})
plt.close(fig)

data = {
    "licence": "CC0-1.0 to the extent of rights held",
    "scope": "Exact commutative infinite example; density window is a finite sample.",
    "proof_locators": ["CZ11", "CZ15", "CZ32", "CZ35-CZ39"],
    "indices": [int(n) for n in indices],
    "h_rationals": [str(Fraction(2)**int(n)) for n in indices],
    "p4_indices": [-2, -1, 0, 1, 2],
    "cocycle_t0": "pi/(2 log 2)",
    "exact_phases_residue_0_1_2_3": phases,
    "domain_values": {"phi_xx": "2", "phi_h_xx": "infinity",
                      "phi_yy": "infinity", "phi_h_yy": "1"},
    "trace_scaling": {"beta_a_n": "a_(n-1)", "beta_H": "H/2",
                      "tau_beta": "tau/2"},
    "finite_geometric_checks": [
        {"N": N, "phi_xx_partial": str(sum(Fraction(1, 2)**n for n in range(N+1))),
         "phi_h_xx_partial": N+1,
         "phi_h_yy_partial": str(sum(Fraction(1, 2)**n for n in range(1, N+1)))}
        for N in [1, 2, 4, 8, 16]
    ],
}
(HERE / "figure-data.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
for f in [OUT/"centralizer-density-domains.png", OUT/"centralizer-density-domains.svg",
          HERE/"figure-data.json"]:
    print(f.name, hashlib.sha256(f.read_bytes()).hexdigest())
