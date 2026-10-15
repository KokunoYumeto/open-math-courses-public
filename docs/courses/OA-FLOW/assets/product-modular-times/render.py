"""CC0-1.0 mathematical figure for MIV8--MIV10; run with Python.
Numerical curves illustrate the proved series criterion, not a finite test of it.
Font components retain their own terms.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "svg.hashsalt": "oa-flow-product-modular-times-v1",
    "axes.spines.top": False, "axes.spines.right": False,
})
INK, BLUE, TEAL, ORANGE, PURPLE = "#17354e", "#286cac", "#087f82", "#bf6428", "#7356a8"
r = np.linspace(-1.0, 1.0, 1201)
t = 2*np.pi*r
p = 1/(1+np.exp(-1))
q = 1-p
one = 4*p*q*np.sin(t/2)**2
ns = (4, 16, 64, 256)
eps = 1/(np.arange(1, 257, dtype=float)+2)
ps = (1+eps)/2
qs = (1-eps)/2
logs = np.log1p(eps)-np.log1p(-eps)
terms = 4*ps[:, None]*qs[:, None]*np.sin(logs[:, None]*t[None, :]/2)**2
sums = np.cumsum(terms, axis=0)
tail = 2.25*t*t/(256+2)

fig, axes = plt.subplots(1, 2, figsize=(14, 7.4), dpi=170)
fig.subplots_adjust(left=.075, right=.97, top=.77, bottom=.26, wspace=.25)
fig.suptitle("Inner modular times are controlled by the tail", y=.97,
             color=INK, fontsize=23)
fig.text(.5, .90, r"$T(M)=\{t:\sum_n d_n(t)<\infty\}$,  "
         r"$d_n(t)=1-|\sum_j p_{n,j}^{\,1+it}|^2$",
         ha="center", fontsize=18, color=INK)
colors = (BLUE, TEAL, ORANGE, PURPLE)
for N, color in zip(ns[:-1], colors):
    axes[0].plot(r, N*one, color=color, lw=2, label=f"N = {N}")
axes[0].set_title("Repeated binary state: c = 1", color=INK, pad=16)
axes[0].set_ylabel(r"Partial dispersion $\sum_{n=1}^N d_n(t)$")
axes[0].legend(loc="upper right", frameon=False)
for N, color in zip(ns, colors):
    axes[1].plot(r, sums[N-1], color=color, lw=2, label=f"N = {N}")
axes[1].fill_between(r, sums[-1], sums[-1]+tail, color=PURPLE, alpha=.16,
                     label="proved tail bound above N = 256")
axes[1].set_title(r"Nearly tracial: $\varepsilon_n=1/(n+2)$", color=INK, pad=16)
axes[1].legend(loc="upper center", fontsize=10, frameon=False)
for ax in axes:
    ax.set_xlim(-1, 1)
    ax.set_ylim(bottom=0)
    ax.set_xticks([-1, -.5, 0, .5, 1])
    ax.set_xlabel(r"Normalized time $r=t/(2\pi)$")
    ax.grid(alpha=.15)
    ax.tick_params(colors=INK)
fig.text(.285, .16, r"$T(M)=2\pi\mathbb{Z}$", ha="center", color=BLUE, fontsize=20)
fig.text(.765, .16, r"$T(M)=\mathbb{R}$,  $\mathrm{Per}(\varphi)=\{0\}$",
         ha="center", color=TEAL, fontsize=20)
fig.text(.5, .085, r"Shaded height: $(9/4)(2\pi r)^2/(256+2)$.  "
         "Proof: MIV9.a-b and MIV10.a-g.", ha="center", color=INK, fontsize=13)
fig.text(.5, .035, "Curves are numerical samples. Exact periods and convergence follow from the lesson proofs.",
         ha="center", color=INK, fontsize=12)
fig.savefig(HERE/"product-modular-times.png", dpi=170,
            metadata={"Software": "Original CC0 matplotlib proof figure"})
fig.savefig(HERE/"product-modular-times.svg",
            metadata={"Date": None, "Creator": "Original CC0 mathematical figure"})
plt.close(fig)

sample_r = np.arange(-4, 5)/4
sample_t = 2*np.pi*sample_r
sample_terms = 4*ps[:, None]*qs[:, None]*np.sin(logs[:, None]*sample_t[None, :]/2)**2
sample_sums = np.cumsum(sample_terms, axis=0)
data = {
    "licence": "CC0-1.0; font components retain their terms",
    "coordinate": "r=t/(2*pi)",
    "plot_grid": {"r_min": -1, "r_max": 1, "points": 1201},
    "dispersion": "d_n(t)=1-|sum_j p_nj exp(i t log p_nj)|^2",
    "repeated_state": {"c": 1, "p": "1/(1+exp(-1))", "q": "exp(-1)/(1+exp(-1))",
                       "partial_sum": "N*4*p*q*sin(t/2)^2", "N": [4, 16, 64],
                       "inner_times": "2*pi*Z"},
    "nearly_tracial": {"n_starts_at": 1, "epsilon": "1/(n+2)",
                        "p": "(1+epsilon)/2", "q": "(1-epsilon)/2",
                        "N": list(ns), "tail_upper_bound": "(9/4)*t^2/(N+2)",
                        "inner_times": "R", "exact_state_periods": "{0}"},
    "sample_r": sample_r.tolist(),
    "nearly_tracial_partial_sums": {str(N): sample_sums[N-1].tolist() for N in ns},
    "proof_locators": ["MIV8.d", "MIV9.a", "MIV9.b", "MIV10.a", "MIV10.f", "MIV10.g"],
    "limits": "Finite numerical samples illustrate the exact formulas; they do not prove convergence or classify the factor.",
    "programme_inputs": ["OA-APPROX/infinite-tensor-products.html#theorem-6-1",
                          "OA-APPROX/infinite-tensor-products.html#theorem-7-2"],
    "human_background": "H. Araki and E. J. Woods, A Classification of Factors, https://ems.press/journals/prims/articles/2441",
}
(HERE/"data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
