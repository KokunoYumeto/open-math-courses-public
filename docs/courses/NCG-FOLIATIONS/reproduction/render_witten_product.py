"""Exact derivative formulas and whole compact-K product diagram; CC0-1.0.
The sampled formulas illustrate proved analytic bounds, not spectral tests.
Run with Python, matplotlib and numpy. Bundled DejaVu fonts retain their licence.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
HERE=Path(__file__).resolve().parent.parent/'figures'
for font_path in (Path(__file__).resolve().parent/'fonts').glob('*.ttf'):
    font_manager.fontManager.addfont(str(font_path))
plt.rcParams['font.family']='DejaVu Sans'

# The plots sample explicit proved functions, not eigenvalues or measured bounds.
radius = np.linspace(0, 6, 700)
angular = np.ones_like(radius)
angular[1:] = radius[1:] / np.tanh(radius[1:]) / np.sqrt(1 + radius[1:] ** 2)
radial = (1 + radius * radius) ** (-1.5)
fig = plt.figure(figsize=(13.2, 6.1), layout="constrained")
grid = fig.add_gridspec(1, 2, width_ratios=[1, 1.32])
ax = fig.add_subplot(grid[0, 0])
ax.plot(radius, radial, color="#1565c0", lw=2.4, label=r"Radial: $(1+r^2)^{-3/2}$")
ax.plot(radius, angular, color="#8e24aa", lw=2.4, label=r"Angular: $r\coth r/\sqrt{1+r^2}$")
ax.axhline(1, color="#607d8b", ls="--", lw=1.7, label="Proved upper bound 1")
ax.set(xlim=(0, 6), ylim=(-0.02, 1.08), xlabel="Hyperbolic distance r", ylabel="Covariant derivative eigenvalue")
ax.set_title("Exact derivative bounds for the normalized radial covector", fontsize=12, pad=16)
ax.grid(alpha=0.18)
ax.legend(loc="lower right", fontsize=10)
ax.text(
    0.04, 0.48,
    r"$\xi=r\,dr/\sqrt{1+r^2}$" + "\n\n"
    r"$\|B\|\leq 2,\quad C=\{\Theta,Q\}\geq-2$" + "\n"
    r"$\Theta=-c_+(\xi),\quad Q=d+d^*-c_+(df)$" + "\n\n"
    "WP.28–WP.30; smooth value 1 at r=0",
    transform=ax.transAxes, fontsize=11,
    bbox={"boxstyle": "round,pad=0.7", "facecolor": "#f7fafc", "edgecolor": "#cfd8dc"},
)

ax2 = fig.add_subplot(grid[0, 1])
ax2.axis("off")
ax2.set_title("The whole compact K-product and its actual unit summand", fontsize=12, pad=16)
boxes = [
    (0.88, r"$L_\xi\simeq L_{-\xi}$ by the invariant covector rotation"
     + "\n" + r"$P\widehat{\otimes}_P H\simeq H$ exactly (WP.20–WP.22)", "#e8f0fe"),
    (0.65, "Actual creation connection (WP.24–WP.27)"
     + "\n" + r"$F_QT_p-(-1)^{|p|}T_pF_D$ is compact"
     + "\n" + r"Two-pole error $\leq 2\|K_p\|/(1+t^2)$", "#edf7ed"),
    (0.40, "Actual bounded positivity (WP.31–WP.37)"
     + "\n" + r"$\{\Theta,F_Q\}=P_\infty-2(1+Q^2)^{-1/2}$"
     + "\n" + r"$P_\infty\geq0$ strongly; correction norm-integrable and compact", "#fff4e5"),
    (0.12, "Whole phase cycle (WP.17, WP.40–WP.42)"
     + "\n" + r"$\mathbb{C}g_{\rm even}\oplus(\mathbb{C}g)^\perp$"
     + "\n" + r"$g=Z^{-1/2}e^{-r^2/2}\operatorname{vol},\quad R(k)g=g$"
     + "\n" + r"Trivial Gaussian unit $\oplus$ exactly degenerate complement $=1_K$", "#f3e5f5"),
]
for y, text, color in boxes:
    ax2.text(
        0.5, y, text, ha="center", va="center", transform=ax2.transAxes,
        fontsize=11, linespacing=1.55,
        bbox={"boxstyle": "round,pad=0.7", "facecolor": color, "edgecolor": "#b0bec5"},
    )
for top, bottom in [(0.81, 0.74), (0.54, 0.49), (0.29, 0.24)]:
    ax2.annotate(
        "", xy=(0.5, bottom), xytext=(0.5, top), xycoords="axes fraction",
        arrowprops={"arrowstyle": "-|>", "color": "#455a64", "lw": 1.8},
    )
fig.suptitle("Negative Witten product on the complete hyperbolic disk", fontsize=17)
fig.savefig(HERE / "kt-hyperbolic-witten-product.png", dpi=165, metadata={"Description": "Original programme figure, CC0-1.0"})
fig.savefig(HERE / "kt-hyperbolic-witten-product.svg", metadata={"Description": "Original programme figure, CC0-1.0"})
plt.close(fig)
