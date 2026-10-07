"""Reproduce the original L30 normalization and ordered-matrix figure.

Run with Python, NumPy and Matplotlib; no network or external data is used.
All curves except the exact zero identity are numerical samples of displayed
formulas. Frobenius norm is sqrt(Tr(X*X)), not the operator norm.
Original figure and code: CC0-1.0. See TERMS.md and FONT_LICENSE_DEJAVU.txt.
"""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "svg.fonttype": "path",
    "svg.hashsalt": "oa-flow-l30-original-20261006",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.facecolor": "#ffffff",
})
blue, orange, purple, green = "#126587", "#cc6b25", "#713f95", "#34815b"
L = math.log(2 * math.pi)
correct_value = (1 - math.exp(-1)) / (2 * math.pi)
raw_value = 1 - math.exp(-1)
B = np.array([[3, 1], [1, 2]], dtype=complex)
C = np.array([[2, 1j], [-1j, 4]], dtype=complex)

def ipower(D, t):
    eig, U = np.linalg.eigh(D)
    assert np.min(eig) > 0
    return (U * np.exp(1j * t * np.log(eig))) @ U.conj().T

times = np.linspace(0, 2, 401)
errors, cancellation_errors = [], []
for t in times:
    Bt, Ct = ipower(B, t), ipower(C, t)
    At = Ct @ Bt.conj().T
    errors.append(float(np.linalg.norm(Bt @ At - Ct, "fro")))
    cancellation_errors.append(float(np.linalg.norm(At @ Bt - Ct, "fro")))
t1_idx = int(np.argmin(np.abs(times - 1)))
assert times[t1_idx] == 1
assert max(cancellation_errors) < 2e-14
assert np.allclose((B @ C - C @ B)[0, 0], -2j)
assert math.isclose(raw_value / correct_value, 2 * math.pi, rel_tol=1e-14)
assert math.isclose(-(-1-L)-L, 1, abs_tol=1e-14)
assert math.isclose(-(-L)-L, 0, abs_tol=1e-14)

fig, axes = plt.subplots(1, 3, figsize=(18, 6.5))
fig.subplots_adjust(left=0.05, right=0.982, bottom=0.18, top=0.77, wspace=0.32)
fig.suptitle("The specified trace fixes the spectral origin; matrix factors keep their order",
             fontsize=18, y=0.97)
fig.text(0.5, 0.898,
         r"Scalar core: $\lambda(t)(p)=e^{itp}$,  $d\tau_{\rm can}=e^{-p}\,dp/(2\pi)$"
         "     |     "
         r"Matrix check at $r=0$: $V(0)=1$,  $A_t=C^{it}B^{-it}$",
         ha="center", fontsize=12)

ax = axes[0]
r = np.linspace(-3.85, 0.75, 300)
ax.axhspan(0, 1, color="#eef3f5", zorder=0)
ax.axvspan(-L-1, -L, color=blue, alpha=0.09, zorder=0)
ax.plot(r, -r-L, color=blue, linewidth=2.6, label=r"$p=-r-\log(2\pi)$")
ax.plot(r, -r, color="#8a8f96", linewidth=1.8, linestyle="--", label=r"$p=-r$ (shift omitted)")
for x, y in [(-L-1, 1), (-L, 0)]:
    ax.plot([x, x], [-2.65, y], color=blue, alpha=0.55, linestyle=":", linewidth=1.3)
    ax.scatter([x], [y], s=36, color=blue, zorder=5)
ax.annotate(r"$(-1-\log(2\pi),\,1)$", xy=(-L-1, 1), xytext=(-3.65, 2.5),
            fontsize=10, arrowprops={"arrowstyle": "-", "color": blue},
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
ax.annotate(r"$(-\log(2\pi),\,0)$", xy=(-L, 0), xytext=(-1.5, 1.05),
            fontsize=10, arrowprops={"arrowstyle": "-", "color": blue},
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
ax.set(xlim=(-3.85, 0.75), ylim=(-2.7, 4.25), xlabel=r"given coordinate $r$",
       ylabel=r"core coordinate $p$", title="A. The exact spectral interval")
ax.legend(loc="lower left", fontsize=10, framealpha=0.95)
ax.grid(alpha=0.18)

ax = axes[1]
p = np.linspace(0, 1, 251)
correct_density, raw_density = np.exp(-p)/(2*math.pi), np.exp(-p)
ax.plot(p, raw_density, color=orange, linewidth=2.4, label=r"omitted shift: $e^{-p}$")
ax.fill_between(p, raw_density, color=orange, alpha=0.08)
ax.plot(p, correct_density, color=blue, linewidth=2.6, label=r"correct: $e^{-p}/(2\pi)$")
ax.fill_between(p, correct_density, color=blue, alpha=0.22)
ax.set(xlim=(0, 1), ylim=(0, 1.08), xlabel=r"spectral coordinate $p$",
       ylabel="positive trace density", title=r"B. The test $F=1_{[0,1]}$")
ax.text(0.08, 0.56, r"$\tau_{\rm correct}=\dfrac{1-e^{-1}}{2\pi}$"
        f"\n                    = {correct_value:.6f}", color=blue, fontsize=12,
        transform=ax.transAxes, va="top")
ax.text(0.08, 0.34, r"$\tau_{\rm omitted}=1-e^{-1}$"
        f"\n                     = {raw_value:.6f}", color=orange, fontsize=12,
        transform=ax.transAxes, va="top")
ax.legend(loc="upper right", fontsize=9.5)
ax.grid(alpha=0.18)

ax = axes[2]
ax.plot(times, errors, color=purple, linewidth=2.7,
        label=r"reversed: $\|B^{it}A_t-C^{it}\|_{\rm F}$")
ax.plot(times, np.zeros_like(times), color=green, linewidth=2.5,
        label=r"ordered: $\|A_tB^{it}-C^{it}\|_{\rm F}=0$")
ax.scatter([1], [errors[t1_idx]], color=purple, s=38, zorder=5)
ax.annotate(f"t = 1: {errors[t1_idx]:.6f}", xy=(1, errors[t1_idx]),
            xytext=(0.24, max(errors)*0.73), fontsize=11, color=purple,
            arrowprops={"arrowstyle": "-", "color": purple})
ax.set(xlim=(0, 2), ylim=(-0.035, max(errors)*1.25), xlabel=r"modular time $t$",
       ylabel="Frobenius residual", title="C. Cancellation has an order")
ax.legend(loc="upper left", fontsize=9.3)
ax.grid(alpha=0.18)
fig.text(0.814, 0.067, "B = [[3, 1], [1, 2]]     C = [[2, i], [-i, 4]]",
         ha="center", fontsize=10)
fig.text(0.354, 0.067,
         r"Exact ratio in B: $2\pi$.   Exact identity in C: $(C^{it}B^{-it})B^{it}=C^{it}$.",
         ha="center", fontsize=11)
fig.text(0.5, 0.021, "L30.8.d–e and L30.10.e–g  •  Reversed-order curve: 401 numerical samples  •  Original mathematical figure",
         ha="center", fontsize=10, color="#555b62")
fig.savefig(OUT/"normalization-and-order.png", dpi=170)
fig.savefig(OUT/"normalization-and-order.svg", metadata={"Date": None})
plt.close(fig)

data = {
    "model": {
        "scalar_trace": "integral exp(r) f(r) dr",
        "correct_coordinate": "p = -r - log(2*pi)",
        "test_function": "F = indicator_[0,1]",
        "exact_preimage": ["-1-log(2*pi)", "-log(2*pi)"],
        "preimage_numeric": [-1-L, -L],
        "correct_trace_exact": "(1-exp(-1))/(2*pi)",
        "correct_trace_numeric": correct_value,
        "omitted_shift_trace_exact": "1-exp(-1)",
        "omitted_shift_trace_numeric": raw_value,
        "ratio_exact": "2*pi",
        "B": [[3,1],[1,2]],
        "C": [["2","i"],["-i","4"]],
        "commutator_11_exact": "-2i",
        "ordered_identity": "(C^(it) B^(-it)) B^(it) = C^(it)",
        "reversed_residual_norm": "Frobenius",
        "sample_point": {"r":0, "t":1, "reversed_residual": errors[t1_idx]},
        "maximum_numerical_ordered_residual": max(cancellation_errors),
    },
    "sampled_curves": {
        "p": p.tolist(), "correct_density": correct_density.tolist(),
        "omitted_density": raw_density.tolist(), "t": times.tolist(),
        "reversed_residual": errors,
    },
    "interpretation": "Exact zero follows algebraically; floating residual checks numerical implementation. Reversed-order samples are not a uniform lower bound.",
    "software": {"numpy":np.__version__, "matplotlib":matplotlib.__version__},
}
(OUT/"data.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"correct":correct_value,"omitted":raw_value,"matrix_t1":errors[t1_idx],
                  "ordered_numeric_max":max(cancellation_errors),"png":str(OUT/"normalization-and-order.png")}))
