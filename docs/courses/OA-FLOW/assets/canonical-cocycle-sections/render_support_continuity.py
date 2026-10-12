"""Render the support-continuity counterexample WCH14a--c.

Run: python render_support_continuity.py
Original code and illustration: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.labelsize": 11,
    "svg.fonttype": "none", "svg.hashsalt": "oa-flow-support-continuity-v1",
    "figure.facecolor": "white", "savefig.facecolor": "white",
})
values = [1, 4, 16]
colors = ["#286b9b", "#278471", "#9b572b"]
p = np.linspace(-3, 6, 600)
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.1), constrained_layout=True)
for n, color in zip(values, colors):
    axes[0].plot(p, 1 / (1 + np.exp(p) / n), color=color, lw=2,
                 label=fr"$n={n}$")
axes[0].axhline(1, color="#333333", lw=1.2, linestyle="--",
               label="strong limit: 1")
axes[0].axvspan(0, 1, color="#999999", alpha=.12)
axes[0].set(xlabel="core coordinate $p$ (finite window)",
            ylabel=r"$(1+h_n(p))^{-1}$", ylim=(-.02, 1.1),
            title=r"$h_n(p)=e^p/n\ \longrightarrow\ 0$ in strong resolvent sense")
axes[0].legend(loc="lower left", frameon=False, fontsize=10)
axes[0].text(.03, .30, r"test vector $\xi=1_{[0,1]}$",
             transform=axes[0].transAxes, color="#444444")
for j, (n, color) in enumerate(zip(values, colors)):
    lo, hi = np.log(n) - 1, np.log(n)
    y = 3 - j
    axes[1].broken_barh([(lo, 1)], (y - .24, .48), facecolors=color)
    axes[1].text(hi + .10, y, "mass 1", va="center", fontsize=10, color=color)
    axes[1].text((lo + hi) / 2, y, f"$n={n}$", ha="center", va="center",
                 color="white", fontsize=11)
axes[1].axhline(0, color="#777777", lw=1, linestyle=":")
axes[1].text(-.85, .08, r"zero weight: $\mu_0=0$, mass 0",
             color="#333333", fontsize=11)
axes[1].set(xlim=(-1.2, 4.1), ylim=(-.35, 3.65),
            xlabel=r"spectral coordinate $q=\log n-p$",
            yticks=[], title="The vector spectral mass escapes to the right")
axes[1].text(.02, .96, r"$d\mu_n(q)=1_{[\log n-1,\log n]}(q)\,dq$",
             transform=axes[1].transAxes, va="top", fontsize=12)
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
axes[1].spines["left"].set_visible(False)
fig.suptitle(r"Support condition: $s(h_n)=1$ for every $n$, while $s(0)=0$",
             fontsize=16)
fig.supxlabel("Exact model WCH14a-c. Vector spectral measures; these masses are not core traces.",
              fontsize=11)
svg = ROOT / "support-continuity.svg"
png = ROOT / "support-continuity.png"
fig.savefig(svg, bbox_inches="tight", metadata={"Date": None})
fig.savefig(png, dpi=160, bbox_inches="tight")
plt.close(fig)
data = {
    "source": "OA-FLOW-WCH, WCH14a--c",
    "core_density": "h_n(p)=exp(p)/n",
    "core_trace": "tau(f)=integral exp(-p)*f(p) dp/(2*pi)",
    "limit_density": "0",
    "resolvent": "(1+exp(p)/n)^(-1)",
    "resolvent_convergence": "strong, by dominated convergence on each Hilbert vector; not asserted in norm",
    "test_vector": "xi(p)=1_[0,1](p), unit in L2(R,dp)",
    "vector_spectral_measure": "mu_n(dq)=1_[log(n)-1,log(n)](q)dq",
    "limit_vector_spectral_measure": "mu_0=0",
    "support_projection": {"each_n": "1", "limit_density": "0"},
    "coordinate_unit_difference": "kappa_n(1)-kappa_0(1)=1",
    "rendered_n": [{"n": n, "interval": [float(np.log(n)-1), float(np.log(n))],
                    "vector_mass": 1} for n in values],
    "proof_scope": "The finite plots illustrate the exact infinite-sequence formulas; the lesson supplies the convergence and failure proofs.",
    "artifacts": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in [svg, png]},
}
(ROOT / "support-continuity.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"rendered": [svg.name, png.name], "model": "WCH14a--c"}))
