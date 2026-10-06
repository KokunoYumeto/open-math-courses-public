"""Exact infinite diagonal cutoff and a noncommuting 2x2 polar-vector example."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = Path(__file__).resolve().parent
(D / "assets").mkdir(exist_ok=True)
j = np.arange(2, 10)
t = 4.0 ** (j - 1)
n = np.arange(1, 10)
m = 64
actual = (n <= 3).astype(float)
bound = np.sqrt(m) * 2.0 ** (-n)
C = np.array([[0.5, 0.2], [0.2, 0.5]])
Dm = np.diag([1.0, 4.0])
Ds = np.diag([1.0, 2.0])
B = np.array([[0.5, 0.4], [0.4, 2.0]])
lam, U = np.linalg.eigh(C)
Cs = (U * np.sqrt(lam)) @ U.T
alpha = Ds @ Cs
Falpha = Ds @ alpha.T @ np.linalg.inv(Ds)
assert np.all(actual <= bound + 1e-14)
assert np.max(np.abs(alpha @ alpha.T - B)) < 1e-12
assert np.max(np.abs(Falpha - alpha)) < 1e-12
assert np.linalg.eigvalsh(Dm - B).min() > 0

fig, axs = plt.subplots(1, 3, figsize=(15.6, 5.6), layout="constrained")
fig.suptitle("Two concrete mechanisms in the general-weight proof",
             fontsize=19, fontweight="bold")
ax = axs[0]
ax.set_title("1. A closed difference form supplies cutoffs", fontsize=12)
ax.axvspan(1.5, 4.5, color="#e0edf0")
ax.plot(j, t, "o-", color="#176d80", lw=2.2, ms=6,
        label=r"$t_j=4^{j-1}$ for $j\geq2$")
ax.axhline(m, color="#b65d1d", lw=2, ls="--", label=r"$m=64=4^3$")
ax.set_yscale("log", base=4)
ax.set_xticks(j)
ax.set_xlabel(r"Coordinate $j$ in sector 0")
ax.set_ylabel(r"Spectral value $t_j$")
ax.legend(loc="upper left", fontsize=10)
ax.text(0.03, -0.24, r"$t_1=0$; sector 1 also has value $0$."
        "\n" r"$e_{64}$ keeps sector 0 coordinates $j\leq4$"
        "\nand every coordinate in sector 1.",
        transform=ax.transAxes, fontsize=10, va="top",
        bbox=dict(boxstyle="round,pad=.5", fc="white", ec="#b8c9ce"))
ax.grid(axis="y", alpha=.2)

ax = axs[1]
ax.set_title("2. Left cutoffs make the differences summable", fontsize=12)
ax.plot(n, bound, "o--", color="#b65d1d", lw=2,
        label=r"$\sqrt{64}\,2^{-n}=2^{3-n}$")
ax.step(n, actual, where="mid", color="#176d80", lw=2.4,
        label=r"$\|e_{64}d_n\|=1_{\{n\leq3\}}$")
ax.scatter(n, actual, color="#176d80", s=27, zorder=3)
ax.set_xticks(n)
ax.set_ylim(-.12, 4.5)
ax.set_xlabel(r"Difference index $n$, where $d_n=z_{n+1}-z_n$")
ax.set_ylabel("Operator norm")
ax.legend(loc="upper right", fontsize=10)
ax.text(.98, .45, r"$e_{64}z_n=e_{64}x$ for $n\geq4$."
        "\n\n" r"$\|\Lambda(z_n-x)\|^2$"
        "\n" r"$=2^{-8(n+1)}/(1-2^{-8})$",
        transform=ax.transAxes, ha="right", fontsize=11,
        bbox=dict(boxstyle="round,pad=.5", fc="#f8fafb", ec="#b8c9ce"))
ax.grid(alpha=.2)

ax = axs[2]
ax.set_title("3. The polar vector has a positive right multiplier", fontsize=12)
ax.imshow(alpha, cmap="Blues", vmin=0, vmax=1.7)
for row in range(2):
    for col in range(2):
        ax.text(col, row, f"{alpha[row,col]:.6f}",
                color="white" if alpha[row,col] > 1 else "#123d58",
                ha="center", va="center", fontsize=15, fontweight="bold")
ax.set_xticks([0,1], ["Column 1", "Column 2"])
ax.set_yticks([0,1], ["Row 1", "Row 2"])
ax.set_xlabel(r"$\alpha_f=D^{1/2}C^{1/2}$", fontsize=14)
ax.text(.5, -.29, r"$R_{\alpha_f}(\xi)=\xi C^{1/2},\quad C=D^{-1/2}BD^{-1/2}$"
        "\n" r"$\alpha_f\alpha_f^*=B,\quad F\alpha_f=\alpha_f$"
        "\n" r"$\rho(t_f)=\|\alpha_f\|_{\rm HS}^{2}=\operatorname{Tr}B=5/2$",
        transform=ax.transAxes, ha="center", va="top", fontsize=11)

fig.savefig(D / "assets" / "extended-weight-mechanism.png", dpi=170, bbox_inches="tight")
fig.savefig(D / "assets" / "extended-weight-mechanism.svg", bbox_inches="tight")
plt.close(fig)
(D / "extended-weight-figure-numerics.json").write_text(json.dumps({
    "scope":"Finite plotted samples of the fully proved infinite diagonal example; exact 2x2 formulas are in the caption",
    "j":j.tolist(), "spectral_values":t.tolist(), "m":m,
    "n":n.tolist(), "cutoff_difference_norm":actual.tolist(),
    "proved_bound":bound.tolist(),
    "D":Dm.tolist(), "B":B.tolist(), "C":C.tolist(),
    "alpha":alpha.tolist(),
    "alpha_alpha_star_residual":float(np.max(np.abs(alpha @ alpha.T-B))),
    "F_alpha_residual":float(np.max(np.abs(Falpha-alpha))),
    "norm_squared":float(np.sum(alpha*alpha)),
    "last_routine_update_attempt_utc":None
}, indent=2)+"\n", encoding="utf-8")
