"""Reproducible WF-3 polar-factor illustration, and exact diagonal-weight sample."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
(HERE / "assets").mkdir(exist_ok=True)
a = np.array([[1., 0.], [0., 0.]])
b = np.ones((2, 2)) / 2
d = np.diag([1., 2.])
evals, evectors = np.linalg.eigh(a + b)
c = (evectors * np.sqrt(evals)) @ evectors.T
X = np.vstack([a, b])
V = X @ np.linalg.inv(c)
Q = V @ V.T
alpha_beta = X @ d
theta_c = c @ d
errors = {
    "V_star_V_minus_identity": float(np.linalg.norm(V.T @ V - np.eye(2))),
    "V_c_minus_X": float(np.linalg.norm(V @ c - X)),
    "Q_alpha_beta_minus_alpha_beta": float(np.linalg.norm(Q @ alpha_beta - alpha_beta)),
    "V_star_alpha_beta_minus_theta_c": float(np.linalg.norm(V.T @ alpha_beta - theta_c)),
}
assert max(errors.values()) < 2e-14
assert abs(np.linalg.norm(theta_c)**2 - 3.5) < 2e-14
fig = plt.figure(figsize=(13.2, 7.4), constrained_layout=True)
gs = fig.add_gridspec(2, 3, height_ratios=[1.15, 1])
fig.suptitle("A finite weight is a vector norm; the polar column proves additivity",
             fontsize=18, fontweight="bold")
ax = fig.add_subplot(gs[0, :])
ax.axis("off")
ax.text(.01, .88, r"$M=M_2(\mathbb{C}),\quad D=\mathrm{diag}(1,2),\quad"
        r"\theta(x)=xD,\quad \Phi(t)=\mathrm{Tr}(D^2t)$",
        fontsize=18, transform=ax.transAxes)
ax.text(.01, .60, "a = [[1, 0], [0, 0]]       b = ½ [[1, 1], [1, 1]]       ab ≠ ba",
        fontsize=17, transform=ax.transAxes)
ax.text(.01, .32, r"$X=\binom{a^{1/2}}{b^{1/2}}=Vc,\quad c=(a+b)^{1/2},\quad"
        r"Q=VV^*,\quad Q\binom{\alpha}{\beta}=\binom{\alpha}{\beta}$",
        fontsize=17, transform=ax.transAxes)
ax.text(.01, .04, r"$\alpha=a^{1/2}D,\quad \beta=b^{1/2}D,\quad"
        r"\theta(c)=V^*\binom{\alpha}{\beta},\quad"
        r"\|\theta(c)\|_{\rm HS}^2=\|\alpha\|_{\rm HS}^2+\|\beta\|_{\rm HS}^2$",
        fontsize=17, transform=ax.transAxes)
ax = fig.add_subplot(gs[1, 0:2])
vals = [1, 2.5, 3.5]
ax.bar([0, 1, 2], vals, color=["#187d8a", "#427ab3", "#6a55a3"], width=.62)
ax.set_xticks([0, 1, 2], [r"$\Phi(a)=\|\alpha\|^2$", r"$\Phi(b)=\|\beta\|^2$",
                           r"$\Phi(a+b)=\|\theta(c)\|^2$"], fontsize=13)
for i, val in enumerate(vals):
    ax.text(i, val+.08, str(val), ha="center", fontsize=14)
ax.set_ylim(0, 4.15)
ax.set_ylabel("Exact squared Hilbert–Schmidt norm", fontsize=12)
ax.set_title("WF-3, (WF8)–(WF9): norm preservation on the range of Q", fontsize=12)
ax.grid(axis="y", alpha=.2)
ax = fig.add_subplot(gs[1, 2])
N = np.arange(1, 9)
w = N*(N+1)*(2*N+1)/6
ax.plot(N, w, "o-", color="#c37524", lw=2)
ax.set_xlabel(r"$N$", fontsize=12)
ax.set_ylabel(r"$\Psi(e_N)=\sum_{n=1}^{N}n^2$", fontsize=12)
ax.set_title("Strong finite cutoffs need\nno uniform weight bound", fontsize=11)
ax.text(.04, .84, r"$e_N\uparrow 1,\quad \|e_N\|=1$"+"\n"+
        r"$\Psi(e_N)\uparrow\infty$", transform=ax.transAxes, fontsize=13)
ax.set_xticks(N)
ax.grid(alpha=.2)
fig.savefig(HERE / "assets" / "weight-mechanism.png", dpi=180)
fig.savefig(HERE / "assets" / "weight-mechanism.svg")
(HERE / "figure-numerics.json").write_text(json.dumps({
    "purpose": "Numerical illustration QA, not a proof of the general theorem",
    "a": a.tolist(), "b": b.tolist(), "D": d.tolist(), "c": c.tolist(),
    "V": V.tolist(), "operator_identity_residuals": errors,
    "exact_weights": [1, 2.5, 3.5],
    "diagonal_cutoffs": [{"N": int(n), "weight": int(z)} for n, z in zip(N, w)]
}, indent=2) + "\n", encoding="utf-8")
