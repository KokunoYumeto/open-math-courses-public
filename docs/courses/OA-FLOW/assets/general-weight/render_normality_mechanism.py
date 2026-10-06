"""Exact diagonal example for NF-3/NF-4; finite display, infinite proof in caption."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

D = Path(__file__).resolve().parent
(D / "assets").mkdir(exist_ok=True)
j = np.arange(1, 9)
tails = (j[None, :] >= j[:, None]).astype(int)
n = np.arange(1, 11)
omega = 4.0 ** (1-n)
f = 2.0 ** (1-n)
fixed_m = 4
compressed = np.where(n <= fixed_m, 2.0**(1-n)-2.0**(-fixed_m), 0)
bound = 2*compressed + 2**(1-fixed_m)
m = np.arange(1, 11)
errors = 2.0**(-m)
fig, axs = plt.subplots(1, 3, figsize=(14, 5.4), layout="constrained")
fig.suptitle("Closed sum forms turn order continuity into predual approximation",
             fontsize=17, fontweight="bold")
ax = axs[0]
ax.imshow(tails, cmap=ListedColormap(["#ecf0f4", "#287b8e"]), vmin=0, vmax=1,
          interpolation="nearest", aspect="equal")
ax.axvline(3.5, color="#c26c20", lw=3)
ax.set_xticks(np.arange(8), j)
ax.set_yticks(np.arange(8), j)
ax.set_xlabel(r"coordinate $j$; the orange line cuts at $m=4$")
ax.set_ylabel(r"tail projection $a_n=1_{\{j\geq n\}}$")
ax.set_title(r"$T=\sum_n a_n=\mathrm{diag}(1,2,3,\ldots)$"+"\n"+
             r"$r_m=1_{\{j\leq m\}},\quad r_mTr_m\leq m r_m$", fontsize=12)
ax.text(6.7, .2, "1", fontsize=15, color="white")
ax.text(.2, 6.7, "0", fontsize=15, color="#354957")
ax = axs[1]
ax.semilogy(n, f, "o-", color="#287b8e", label=r"$f(a_n)=2^{1-n}$")
ax.semilogy(n, omega, "s-", color="#6b59a5", label=r"$\omega(a_n)=4^{1-n}$")
ax.semilogy(n, bound, "--", lw=2.2, color="#c26c20",
            label=r"NF9 bound, fixed $m=4$")
ax.set_xlabel(r"$n$")
ax.set_ylabel("Exact positive values (logarithmic scale)")
ax.set_title("First choose the cutoff, then the tail", fontsize=12)
ax.legend(fontsize=10, loc="lower left")
ax.grid(alpha=.25)
ax = axs[2]
ax.semilogy(m, errors, "o-", color="#287b8e", lw=2)
ax.set_xlabel(r"$m$")
ax.set_ylabel(r"Predual norm error $\|f-f_m\|=2^{-m}$")
ax.set_title("NF-4: normal coefficients converge in norm", fontsize=12)
ax.text(.05, .35, r"$\Omega_j=\sqrt{3}\,2^{-j}$"+"\n"+
        r"$(\eta_m)_j=1_{\{j\leq m\}}/\sqrt{3}$"+"\n"+
        r"$f_m(x)=\langle x\Omega,\eta_m\rangle$",
        transform=ax.transAxes, fontsize=13, va="top",
        bbox={"facecolor":"white","edgecolor":"#d9dfe5","alpha":.95})
ax.grid(alpha=.25)
fig.savefig(D / "assets" / "normality-mechanism.png", dpi=180)
fig.savefig(D / "assets" / "normality-mechanism.svg")
(D / "normality-figure-numerics.json").write_text(json.dumps({
    "scope": "Exact finite samples of the infinite diagonal example, not a general proof",
    "cutoff_m": fixed_m,
    "n": n.tolist(), "f_tail": f.tolist(), "omega_tail": omega.tolist(),
    "compressed_f_tail": compressed.tolist(), "NF9_bound": bound.tolist(),
    "m": m.tolist(), "predual_norm_error": errors.tolist(),
    "form_at_Omega_exact": "4/3"
}, indent=2)+"\n", encoding="utf-8")
