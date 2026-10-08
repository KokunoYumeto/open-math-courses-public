"""Reproduce the exact carrier geometry and Gaussian contour diagrams."""
from pathlib import Path
import json
import os
import tempfile
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

with tempfile.TemporaryDirectory(prefix="an02-own216-mpl-") as font_cache:
    os.environ["MPLCONFIGDIR"] = font_cache
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon, Rectangle

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.titlesize": 12, "svg.hashsalt": "convex-carriers-gaussian-localization",
    })
    magenta = "#a03487"
    blue = "#256799"
    gold = "#c48614"
    green = "#16866b"
    original = np.array([[0, 0], [2, 0], [0, 1]], dtype=float)
    reflected = -original
    rectangle = np.array([[-.5, -.25], [.5, -.25], [.5, .25], [-.5, .25]])
    hull = np.array([[-2.5, -.25], [-.5, -1.25], [.5, -1.25], [.5, .25], [-2.5, .25]])
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.9), constrained_layout=True)
    ax = axes[0]
    for shift, weight in zip(reflected, [1, 2, 3]):
        ax.add_patch(Polygon(rectangle + shift, facecolor=magenta, alpha=.23,
                             edgecolor=magenta, linewidth=1.6))
        ax.text(*(shift + [0, .35]), f"weight {weight}", ha="center", color=magenta)
    ax.add_patch(Polygon(hull, fill=False, edgecolor=blue, linewidth=2.2,
                         linestyle="--", label="convex hull"))
    ax.add_patch(Polygon(reflected, fill=False, edgecolor=green, linewidth=1.7,
                         linestyle=":", label="reflected support triangle"))
    ax.scatter(reflected[:, 0], reflected[:, 1], color=green, s=24)
    for point, label, offset in zip(
        reflected, ["(0, 0)", "(-2, 0)", "(0, -1)"],
        [[58, -20], [-4, -32], [58, -40]],
    ):
        ax.annotate(label, point, xytext=offset, textcoords="offset points",
                    ha="center", color=green,
                    arrowprops={"arrowstyle": "-", "color": green, "linewidth": .8})
    ax.set_title(r"Actual support: $K_2-\operatorname{supp}\mu$")
    ax.set_xlim(-3.15, 1.05); ax.set_ylim(-1.9, 1.05)
    ax.set_aspect("equal"); ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.legend(loc="upper left", fontsize=9)
    ax.text(-1.0, -.73, r"$K_v=K_2+K_-$", color=blue, ha="center")
    ax = axes[1]
    ax.add_patch(Rectangle((-3, -2), 4, 3, color=blue, alpha=.09))
    ax.add_patch(Rectangle((-3, -2), 4, 3, fill=False, edgecolor=blue,
                           linewidth=1.8, linestyle="--"))
    ax.add_patch(Rectangle((-1, -1), 2, 2, color=gold, alpha=.16))
    ax.add_patch(Rectangle((-1, -1), 2, 2, fill=False, edgecolor=gold,
                           linewidth=1.8, linestyle="--"))
    ax.add_patch(Polygon(rectangle, facecolor=magenta, alpha=.45,
                         edgecolor=magenta, linewidth=1.8))
    ax.text(-2.5, .52, r"$X=(-3,1)\times(-2,1)$", color=blue, fontsize=10)
    ax.text(-.92, .72, r"$X_\mu=(-1,1)^2$", color=gold)
    ax.text(0, 0, r"$K_2$", color=magenta, ha="center", va="center", fontsize=13)
    ax.set_title("The compact analytic carrier lies in the convolution domain")
    ax.set_xlim(-3.25, 1.3); ax.set_ylim(-2.25, 1.4)
    ax.set_aspect("equal"); ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    for ax in axes:
        ax.axhline(0, color="#8c8c8c", linewidth=.6, zorder=0)
        ax.axvline(0, color="#8c8c8c", linewidth=.6, zorder=0)
        ax.grid(alpha=.12)
    name = "reflected-carriers-and-convex-domain"
    fig.savefig(OUT / (name + ".png"), dpi=190, metadata={"Software": "Matplotlib"})
    fig.savefig(OUT / (name + ".svg"), metadata={"Date": None})
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.8), constrained_layout=True)
    ax = axes[0]
    x, eta = .4, .2
    ax.plot([-2, 2], [0, 0], color=blue, linewidth=2.4, label="real interval")
    ax.plot([-2, 2], [eta, eta], color=green, linewidth=2.4,
            label="shifted interval")
    for edge in [-2, 2]:
        ax.plot([edge, edge], [0, eta], color=gold, linewidth=2.4)
    ax.annotate("", xy=(1.3, eta), xytext=(.8, eta),
                arrowprops={"arrowstyle": "->", "color": green})
    ax.annotate("", xy=(1.3, 0), xytext=(.8, 0),
                arrowprops={"arrowstyle": "->", "color": blue})
    ax.scatter([x], [eta], color=magenta, s=55, zorder=5)
    ax.annotate(r"$z=2/5+i/5$", (x, eta), xytext=(x - .75, .52),
                arrowprops={"arrowstyle": "-", "color": magenta}, color=magenta)
    ax.text(-2, -.18, "-2", ha="center"); ax.text(2, -.18, "2", ha="center")
    ax.text(-2, .43, r"left side: $\leq-143/25$", ha="center", color=gold, fontsize=10)
    ax.text(2, .43, r"right side: $\leq-63/25$", ha="center", color=gold, fontsize=10)
    ax.text(0, -.35, r"side labels bound $j^{-1}\log|e^{-j(z-w)^2}|$",
            ha="center", fontsize=10)
    ax.set_xlim(-3.15, 3.15); ax.set_ylim(-.55, .78)
    ax.set_xlabel(r"$\operatorname{Re}w$"); ax.set_ylabel(r"$\operatorname{Im}w$")
    ax.set_title("A contour move to the observation height")
    ax.legend(loc="upper center", fontsize=9, ncol=2)
    ax = axes[1]
    t = np.linspace(-2, 2, 501)
    ax.plot(t, -(x-t)**2+eta**2, color=blue, linewidth=2.2,
            label="real contour: imaginary growth remains")
    ax.plot(t, -(x-t)**2, color=green, linewidth=2.2,
            linestyle="--", label="shifted contour: real Gaussian")
    ax.axhline(-15/16, color=gold, linestyle=":", linewidth=1.5,
               label="general vertical-side upper bound")
    ax.scatter([-2, 2], [-143/25, -63/25], color=gold, s=42)
    ax.annotate(r"$-143/25$", (-2, -143/25), xytext=(-1.7, -5.35), color=gold)
    ax.annotate(r"$-63/25$", (2, -63/25), xytext=(.75, -3.25), color=gold,
                arrowprops={"arrowstyle": "-", "color": gold})
    ax.set_xlim(-2.15, 2.15); ax.set_ylim(-6.25, .5)
    ax.set_xlabel(r"horizontal coordinate $t$")
    ax.set_ylabel(r"$j^{-1}\log|e^{-j(z-w)^2}|$")
    ax.set_title("The exact exponent controls endpoint errors")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.18), fontsize=9)
    ax.grid(alpha=.15)
    name = "gaussian-contour-localization"
    fig.savefig(OUT / (name + ".png"), dpi=190, metadata={"Software": "Matplotlib"})
    fig.savefig(OUT / (name + ".svg"), metadata={"Date": None})
    plt.close(fig)

geometry = {
    "proof_locators": ["Theorem 5.1, equation (5.9)", "Lemma 4.1, equation (4.9)"],
    "original_kernel_support": original.tolist(), "kernel_weights": [1, 2, 3],
    "reflected_kernel_support": reflected.tolist(),
    "analytic_carrier_rectangle": rectangle.tolist(),
    "convex_annihilator_carrier": hull.tolist(),
    "open_domain": {"x": [-3, 1], "y": [-2, 1]},
    "open_convolution_domain": {"x": [-1, 1], "y": [-1, 1]},
    "gaussian": {"R": 1, "interval": [-2, 2], "observation": ["2/5", "1/5"],
                 "left_side_bound": "-143/25", "right_side_bound": "-63/25",
                 "general_side_bound": "-15/16",
                 "exponent": "-((Re(z)-Re(w))^2-(Im(z)-Im(w))^2)"},
    "authorship": "Original mathematical diagrams; GPT-6.1 Sol (OpenAI), Ultra; CC0 1.0.",
}
(OUT / "geometry216.json").write_text(json.dumps(geometry, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"figures": 2, "exact_geometry": str((OUT/"geometry216.json").resolve())}))
