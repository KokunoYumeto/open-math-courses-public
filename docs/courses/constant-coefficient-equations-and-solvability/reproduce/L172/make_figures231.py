"""Draw exact support-set diagrams and sampled boundary-distance formulas."""
from pathlib import Path
from tempfile import TemporaryDirectory
import os
import json

OWN = Path(__file__).resolve().parent


def draw():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    out = OWN / "figures"
    out.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                         "axes.titlesize": 15, "axes.labelsize": 15,
                         "xtick.labelsize": 13, "ytick.labelsize": 13,
                         "legend.fontsize": 12, "svg.fonttype": "none",
                         "axes.spines.top": False, "axes.spines.right": False})
    blue, orange, red = "#165d9c", "#ae5523", "#a12535"
    fig, axes = plt.subplots(2, 1, figsize=(6.5, 7.6), layout="constrained")
    a = axes[0]
    a.plot([0, 3.5], [.4, .4], color="#888888", linewidth=1)
    a.scatter([1/3], [.4], color=blue, s=65, zorder=3)
    a.plot([11/4, 13/4], [.4, .4], color=orange, linewidth=10)
    a.scatter([11/4, 13/4], [.4, .4], color=orange, s=45)
    a.annotate("Singular atom", (1/3, .4), (1/3, .8),
               ha="center", fontsize=14, arrowprops={"arrowstyle": "-", "color": blue})
    a.text(3, .8, "Smooth tail\nsupport", ha="center", fontsize=14)
    a.set(xlim=(-.05, 3.55), ylim=(0, 1.15), yticks=[],
          xlabel=r"Kernel offset $t$", title="The kernel has one singular point")
    a.set_xticks([1/3, 11/4, 13/4],
                 [r"$\frac{1}{3}$", r"$\frac{11}{4}$", r"$\frac{13}{4}$"])
    a.spines["left"].set_visible(False)
    a = axes[1]
    a.axvspan(-1, 1, color="#dceaf4", alpha=.9)
    a.plot([-3.5, 1.35], [.4, .4], color="#888888", linewidth=1)
    a.plot([-13/4, -11/4], [.4, .4], color=orange, linestyle="--",
           linewidth=8, solid_capstyle="butt")
    a.scatter([-1/3], [.4], color=blue, s=65, zorder=3)
    a.scatter([-1, 1], [.4, .4], facecolors="white", edgecolors=blue,
              s=65, linewidths=1.8, zorder=3)
    a.text(0, .91, r"Solution interval $X_1=(-1,1)$", ha="center", fontsize=14)
    a.text(-3.35, .8, "Tail sampling\noutside X₁", ha="left",
           color=orange, fontsize=13)
    a.annotate("Required singular\nsample", (-1/3, .4), (-1/3, .02),
               ha="center", fontsize=13,
               arrowprops={"arrowstyle": "-", "color": blue})
    a.set(xlim=(-3.55, 1.5), ylim=(-.18, 1.17), yticks=[],
          xlabel=r"Input coordinate $y=0-t$",
          title="At output 0, the quotient needs only the atom")
    a.set_xticks([-13/4, -11/4, -1, -1/3, 1],
                 [r"$-\frac{13}{4}$", r"$-\frac{11}{4}$", r"$-1$",
                  r"$-\frac{1}{3}$", r"$1$"])
    a.spines["left"].set_visible(False)
    for ext in ("png", "svg"):
        fig.savefig(out / ("singular-sampling-and-a-remote-smooth-tail."+ext),
                    dpi=180, metadata={"Creator": "Open Mathematics Courses"})
    plt.close(fig)

    fig, axes = plt.subplots(2, 1, figsize=(6.5, 8.2), layout="constrained")
    j = np.arange(1, 6)
    x = 1-np.power(2.0, -j)
    a = axes[0]
    a.scatter(j, x, color=blue, s=65)
    a.plot(j, x, color=blue, linewidth=1.5)
    a.axhline(1, color=red, linestyle="--", linewidth=1.7)
    a.text(3, 1.018, r"Excluded equation boundary $x=1$",
           color=red, ha="center", fontsize=13)
    a.set(xlim=(.6, 5.4), ylim=(.43, 1.08), xticks=j,
          xlabel=r"Derivative order $j$ in $\delta_{x_j}^{(j)}$",
          ylabel=r"Singular point $x_j$",
          title=r"$x_j=1-2^{-j}$ tends to the boundary")
    a.grid(alpha=.15)
    j = np.arange(1, 13)
    a = axes[1]
    a.semilogy(j, np.power(2.0, -j), "-o", color=blue,
               label=r"$d_{X_2}(\{x_j\})=2^{-j}$")
    a.semilogy(j, 1+np.power(2.0, -j), "-s", color=orange,
               label=r"$d_{X_1}(\{x_j\})=1+2^{-j}$")
    a.set(xlim=(.7, 12.3), xlabel=r"Index $j$",
          ylabel="Distance to the complement",
          title="Image singularities keep\na positive boundary margin")
    a.set_xticks([1, 3, 5, 7, 9, 11])
    a.legend(loc="lower left")
    a.grid(alpha=.15)
    for ext in ("png", "svg"):
        fig.savefig(out / ("escaping-singularities-and-increasing-orders."+ext),
                    dpi=180, metadata={"Creator": "Open Mathematics Courses"})
    plt.close(fig)
    geometry = {
        "first_figure": {
            "kind": "Exact support-set diagram;vertical placement is schematic",
            "singular_atom": "1/3", "smooth_tail_support": ["11/4", "13/4"],
            "output_point": 0, "solution_interval_open": [-1, 1],
            "equation_interval_open": ["-2/3", "4/3"],
            "singular_sample": "-1/3",
            "unavailable_tail_sampling_band": ["-13/4", "-11/4"],
            "open_circles_are_excluded_domain_endpoints": True,
            "tail_band_is_support_not_function_height": True,
        },
        "second_figure": {
            "formula": "x_j=1-2^(-j)",
            "distributional_derivative_order": "j",
            "equation_domain": [-1, 1], "solution_domain": [-2, 2],
            "accumulation_point_excluded_from_equation_domain": 1,
            "input_singular_distance": "2^(-j)",
            "image_singular_distance": "1+2^(-j)",
            "point_samples": [1, 5], "distance_samples": [1, 12],
            "sampled_curves_do_not_replace_the_infinite_datum_proof": True,
        },
    }
    (out / "geometry231.json").write_text(
        json.dumps(geometry, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"figures": 2, "formats": ["png", "svg"],
                      "all_coordinates_from_exact_learner_formulas": True}))


if __name__ == "__main__":
    with TemporaryDirectory(prefix="an02-own231-mpl-") as task_cache:
        os.environ["MPLCONFIGDIR"] = task_cache
        draw()
