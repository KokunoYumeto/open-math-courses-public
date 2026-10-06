"""Reproducible exact tracial examples. No operator theorem is inferred from numerics."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans", "svg.fonttype": "none"})
navy, blue, teal, orange = "#17324d", "#2166ac", "#087f8c", "#bc5726"
fig = plt.figure(figsize=(14, 9), facecolor="#f7fafc")
fig.text(.055, .95, "Tracial densities retain every finite and infinite value",
         fontsize=23, weight="bold", color=navy)
fig.text(.055, .912, "A given faithful normal semifinite trace • arbitrary Hilbert spaces • TD-1–8",
         fontsize=12.5, color=navy)
flow = fig.add_axes([.045, .705, .91, .17]); flow.set_axis_off()
boxes = [
    (r"$\xi\in H_\tau$", "trace GNS vector"),
    (r"$T_\xi\Lambda(x)=r(x)\xi$", "close the actual graph"),
    (r"$h_\xi=T_\xi T_\xi^*$", "affiliated density"),
    (r"$\Phi_{h_\xi}(a)=\langle a\xi,\xi\rangle$", "every positive a"),
]
for j, (formula, label) in enumerate(boxes):
    x = .012 + j*.249
    flow.add_patch(FancyBboxPatch((x, .19), .226, .65,
                   boxstyle="round,pad=0.008,rounding_size=0.04",
                   facecolor="white", edgecolor="#bad0df", linewidth=1.5))
    flow.text(x+.113, .60, formula, ha="center", va="center", fontsize=14, color=blue)
    flow.text(x+.113, .34, label, ha="center", fontsize=10.5, color=navy)
    if j < 3:
        flow.annotate("", xy=(x+.245, .52), xytext=(x+.229, .52),
                      arrowprops=dict(arrowstyle="->", color=navy, lw=1.5))
flow.text(.01, .025, "TD-3: bounded spectral cutoffs lie in the finite trace ideal; their vectors converge to ξ.",
          fontsize=11.3, color=navy)

ax1 = fig.add_axes([.13, .355, .32, .255], facecolor="white")
T = np.array([[1., 1.], [0., 1.]])
h = T @ T.T
lm, lp = (3-np.sqrt(5))/2, (3+np.sqrt(5))/2
sm, sp = np.sqrt(lm), np.sqrt(lp)
assert np.allclose(np.linalg.eigvalsh(T.T@T), [lm, lp])
assert np.allclose(h, [[2, 1], [1, 1]]) and np.trace(h) == 3
for left, right, mass in [(0, sm, 0), (sm, sp, lm), (sp, 2.25, 3)]:
    ax1.plot([left, right], [mass, mass], color=blue, lw=3)
    ax1.plot(left, mass, "o", color=blue, ms=7, zorder=5)
for x, y in [(sm, 0), (sp, lm)]:
    ax1.plot(x, y, "o", mfc="white", mec=blue, mew=2, ms=7, zorder=6)
ax1.axvline(sm, color="#ccd8e1", ls=":", zorder=0)
ax1.axvline(sp, color="#ccd8e1", ls=":", zorder=0)
ax1.set(xlim=(-.03, 2.25), ylim=(-.25, 3.45),
        xlabel=r"singular-value cutoff $R$",
        ylabel=r"$\operatorname{Tr}(T e_R T^*)$")
ax1.set_xticks([0, sm, sp, 2.25], ["0", r"$s_-$", r"$s_+$", "2.25"])
ax1.set_yticks([0, lm, 3], ["0", r"$(3-\sqrt{5})/2$", "3"])
ax1.grid(axis="y", alpha=.2)
ax1.set_title("Finite cutoffs recover the whole vector", loc="left",
              fontsize=14, weight="bold", color=navy, pad=19)
fig.text(.075, .252, r"$T=(1,1;\ 0,1),\quad h=(2,1;\ 1,1),\quad \operatorname{Tr}(h)=3$",
         fontsize=12, color=navy)
fig.text(.075, .214, r"$e_R=1_{[0,R]}(|T|),\quad s_\pm=(\sqrt{5}\pm1)/2$",
         fontsize=12, color=navy)
fig.text(.075, .17, "Exact M₂ example • TD15–TD17; caption TDF1–2",
         fontsize=10.6, color=blue)

ax2 = fig.add_axes([.595, .355, .34, .255], facecolor="white")
N = np.arange(1, 13)
ax2.plot(N, N, "o-", color=orange, lw=2.4, ms=5)
ax2.set(xlim=(.5, 12.5), ylim=(0, 13),
        xlabel=r"finite spectral cutoff $N$",
        ylabel=r"$\langle c^*H_Nc\,e_1,e_1\rangle=N$")
ax2.set_xticks([1, 3, 6, 9, 12]); ax2.set_yticks([0, 3, 6, 9, 12])
ax2.grid(alpha=.2)
ax2.set_title("A bounded sandwich can lose a dense domain", loc="left",
              fontsize=14, weight="bold", color=navy, pad=19)
fig.text(.575, .252, r"$He_n=4^n e_n,\quad v_n=2^{-n},\quad c\xi=\xi_1v$",
         fontsize=12, color=navy)
fig.text(.575, .214, r"$D(q_{c^*Hc})=e_1^\perp,\quad q=0\ \mathrm{there};\quad q=\infty\ \mathrm{outside}$",
         fontsize=12, color=orange)
fig.text(.575, .17, "Infinite-value part P₁ • TD26; caption TDF3–5",
         fontsize=10.6, color=orange)

fig.text(.055, .091, "Full domains decide semifiniteness: a density form is allowed to have a nondense finite domain.",
         fontsize=13, weight="bold", color=navy)
fig.text(.055, .053, "Exact proofs: TRACIAL_DENSITY_PROOF.md, TD-3/6/7. Free human context: Hiai (2020), pp.49–50.",
         fontsize=10.7, color=navy)
for name in ["png", "svg"]:
    fig.savefig(OUT / f"tracial-density.{name}", dpi=180, facecolor=fig.get_facecolor())
plt.close(fig)

# Finite sections verify the displayed identity exactly up to floating-point arithmetic.
for n in [1, 2, 3, 6, 12]:
    v = 2.**(-np.arange(1, n+1))
    H = np.diag(4.**np.arange(1, n+1))
    assert np.isclose(v @ H @ v, n)
(OUT / "tracial-density-numerics.json").write_text(json.dumps({
    "scope": "Finite numerical checks of exact caption formulas; not a theorem proof",
    "matrix": T.tolist(), "density": h.tolist(),
    "eigenvalues": [float(lm), float(lp)], "singular_values": [float(sm), float(sp)],
    "trace": 3, "cutoffs": N.tolist(), "sandwich_values": N.tolist(),
    "rank_one_norm_squared_exact": "1/3",
    "infinite_value_domain_exact": "e_1 perpendicular"
}, indent=2)+"\n", encoding="utf-8")
