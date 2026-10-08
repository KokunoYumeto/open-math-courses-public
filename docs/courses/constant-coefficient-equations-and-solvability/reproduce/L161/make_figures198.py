"""Original exact illustrations of Fourier neighborhoods and real PSH translates."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.fonttype": "path", "axes.grid": True,
                     "grid.alpha": .22})
BLUE, RED, GREEN = "#15618a", "#b44236", "#26774f"

def save(fig, name):
    fig.savefig(OUT / (name + ".png"), dpi=160, bbox_inches="tight",
                metadata={"Software": "Matplotlib; original mathematical figure"})
    fig.savefig(OUT / (name + ".svg"), bbox_inches="tight",
                metadata={"Date": None, "Creator": "Original mathematical figure"})
    plt.close(fig)

j = np.arange(8, 31)
Q = 2.0 ** j
ell = j * np.log(2)
r = np.sqrt(Q / ell)
rho = r * ell
delta = rho / Q
fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.35))
axes[0].semilogy(j, r, "o-", color=BLUE, label=r"$r_j=\sqrt{2^j/(j\log 2)}$")
axes[0].semilogy(j, rho, "s-", color=RED, label=r"$\rho_j=\sqrt{2^j j\log 2}$")
axes[0].set(xlabel=r"Center index $j$", ylabel="Exact radius",
            title="Two radii grow")
axes[0].legend(fontsize=10)
axes[1].semilogy(j, delta, "o-", color=GREEN, label=r"$\rho_j/c_j$")
axes[1].axhline(.25, color=RED, ls="--", label=r"Cap $1/4$")
axes[1].set(xlabel=r"Center index $j$", ylabel="Fraction of the center",
            title="The relative radius shrinks")
axes[1].legend(fontsize=10)
eta = np.linspace(-2, 2, 301)
axes[2].plot(eta, -eta, color=BLUE, lw=2.5)
axes[2].axhline(0, color="#555555", lw=.7)
axes[2].axvline(0, color="#555555", lw=.7)
axes[2].set(xlabel=r"Imaginary parameter $\eta$", ylabel=r"$L_{\delta_{-1}}=h=-\eta$",
            title=r"Exact at every center: $C=\{-1\}$")
axes[2].text(.97, .95, "Negative support values\nare included",
             transform=axes[2].transAxes, ha="right", va="top", fontsize=10,
             bbox={"facecolor": "white", "alpha": .9, "edgecolor": "#dddddd"})
fig.suptitle(r"Expanding logarithmic neighborhoods around $c_j=2^j$", fontsize=15)
fig.tight_layout(rect=(0, 0, 1, .92))
save(fig, "expanding-logarithmic-neighborhoods")

x = np.linspace(-2*np.pi, 2*np.pi, 513)
y = np.linspace(-2, 2, 257)
X, Y = np.meshgrid(x, y)
fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.7))
translations = [0.0, np.pi/2]
zero_sets = []
for ax, a, title in zip(axes[:2], translations,
                        [r"$v(z)=\log|\sin z|$", r"$v(z+\pi/2)$"]):
    squared = np.sin(X + a)**2 + np.sinh(Y)**2
    # Clipping is a display convention; exact zero sets are marked separately.
    values = .5 * np.log(np.maximum(squared, np.exp(-6)))
    mesh = ax.imshow(values, origin="lower", extent=(-2*np.pi, 2*np.pi, -2, 2),
                     aspect="auto", cmap="viridis", vmin=-3, vmax=2)
    zeros = [float(m*np.pi-a) for m in range(-3, 4)
             if -2*np.pi-1e-12 <= m*np.pi-a <= 2*np.pi+1e-12]
    zero_sets.append(zeros)
    ax.scatter(zeros, np.zeros(len(zeros)), marker="o", facecolors="white",
               edgecolors=RED, s=38, linewidths=1.4, label=r"Zeros: value $-\infty$")
    ax.set(title=title, xlabel=r"Real parameter $x$", ylabel=r"Imaginary parameter $\eta$")
    ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
                  [r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(False)
    cb = fig.colorbar(mesh, ax=ax, fraction=.05, pad=.025)
    cb.set_label("Log modulus (clipped below −3)", fontsize=9)
axes[2].plot(y, np.log(np.cosh(y)), color=BLUE, lw=2.5,
             label=r"Envelope $M_v(\eta)=\log\cosh\eta$")
axes[2].plot(y, np.abs(y), color=RED, lw=2, ls="--",
             label=r"Indicator $h(\eta)=|\eta|$")
axes[2].set(title=r"Common carrier $[-1,1]$", xlabel=r"Imaginary parameter $\eta$",
            ylabel="Exact envelope and indicator")
axes[2].legend(loc="upper center", fontsize=8.5)
fig.suptitle("Real translations move zeros and preserve the indicator", fontsize=15)
fig.text(.5, .01, "PSH model functions; no compact Fourier realization is asserted.",
         ha="center", fontsize=11)
fig.tight_layout(rect=(0, .04, 1, .92))
save(fig, "real-translations-and-indicators")
geometry = {
    "authorship": "Original mathematics and figures; GPT-6.1 Sol (OpenAI), Ultra; CC0 1.0",
    "neighborhoods": {"centers": "c_j=2^j", "indices": j.tolist(),
                      "log_centers": ell.tolist(), "parameter_radii": r.tolist(),
                      "frequency_radii": rho.tolist(), "relative_radii": delta.tolist(),
                      "point_mass": -1, "profile": "-Im(z)", "carrier": [-1],
                      "proof_locators": ["Learner Example 1", "Formal Lemma 1.1", "Formal Theorem 3.1"]},
    "translations": {"model": "log|sin(z+a)|", "translations": translations,
                     "zero_formula": "z=m*pi-a, m integer", "shown_zero_sets": zero_sets,
                     "envelope": "log(cosh(eta))", "indicator": "abs(eta)", "carrier": [-1, 1],
                     "display_clip": [-3, 2], "zeros_have_value": "-infinity",
                     "compact_Fourier_realization_asserted": False,
                     "proof_locators": ["Learner Example 4", "Formal Lemma 2.1", "Formal Corollary 2.3"]},
    "references": ["Terence Tao, 246B Notes 2", "Lars Hörmander, Analysis of Linear Partial Differential Operators I and II"],
    "Blender_applicability": "Flat frequency-radius graphs and exact complex-parameter heatmaps need no three-dimensional scene."
}
(OUT / "geometry198.json").write_text(json.dumps(geometry, indent=2, allow_nan=False)+"\n",
                                       encoding="utf-8")
print(json.dumps({"figures": 2, "formats_per_figure": ["PNG", "SVG"],
                  "exact_original_geometry": True}))
