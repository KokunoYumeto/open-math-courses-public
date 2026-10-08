"""Reproduce numerical illustrations of the exact original example formulas."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os

OWN = Path(__file__).resolve().parent


def draw():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import mpmath as mp
    import numpy as np
    from scipy.integrate import cumulative_trapezoid

    mp.mp.dps = 65
    out = OWN / "figures"
    out.mkdir(exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 16,
        "axes.titlesize": 16, "axes.labelsize": 15,
        "xtick.labelsize": 13, "ytick.labelsize": 13,
        "legend.fontsize": 12, "svg.fonttype": "none",
        "axes.spines.top": False, "axes.spines.right": False,
    })
    ns = np.arange(1, 2001)
    h = np.cumsum(1.0 / ns)
    fig, axes = plt.subplots(2, 1, figsize=(6.5, 8.5), layout="constrained")
    a = axes[0]
    a.plot(ns, np.sqrt(h), color="#165d9c", linewidth=2.5,
           label=r"$\|b^{(N)}\|_2=\sqrt{H_N}$")
    a.plot(ns, np.sqrt(np.log(ns+1)), "--", color="#287b46",
           label=r"Lower bound $\sqrt{\log(N+1)}$")
    a.plot(ns, np.sqrt(1+np.log(ns)), ":", color="#ae5523", linewidth=2,
           label=r"Upper bound $\sqrt{1+\log N}$")
    a.set(xscale="log", xlabel=r"Truncation length $N$",
          ylabel="Inverse norm", title="Inverse norms have no common bound")
    a.legend(loc="upper left")
    a.grid(alpha=.18)
    a = axes[1]
    nt = np.arange(1, 41)
    bound = np.power(3.0, -nt) / np.sqrt(8*(nt+1))
    a.semilogy(nt, bound, color="#6c3993", linewidth=2.5)
    a.set(xlabel=r"Truncation length $N$",
          ylabel="Upper bound on image error",
          title=r"$\|a-a^{(N)}\|_2\leq 3^{-N}/\sqrt{8(N+1)}$")
    a.grid(alpha=.18)
    for ext in ("png", "svg"):
        fig.savefig(out / ("dense-range-and-growing-inverse-norms."+ext),
                    dpi=180, metadata={"Creator": "Open Mathematics Courses"})
    plt.close(fig)

    radius = mp.mpf(1)/4
    integral = mp.quad(lambda t: mp.exp(-1/(1-16*t*t)),
                       [-radius, 0, radius])
    normalization = 1/integral
    grid = np.linspace(-1, 1, 8193)

    def rho(t):
        z = np.zeros_like(t)
        mask = np.abs(t) < .25
        z[mask] = float(normalization)*np.exp(-1/(1-16*t[mask]**2))
        return z

    psi = rho(grid-.5)-rho(grid+.5)
    phi = -cumulative_trapezoid(psi, grid, initial=0)
    fig, axes = plt.subplots(2, 1, figsize=(6.5, 8), layout="constrained")
    a = axes[0]
    a.plot(grid, psi, color="#165d9c", linewidth=2.3)
    a.axhline(0, color="#555555", linewidth=.8)
    a.text(-.5, -2.6, "Mass −1", ha="center", fontsize=14)
    a.text(.5, 2.6, "Mass +1", ha="center", fontsize=14)
    a.set(xlim=(-1, 1), xlabel=r"$x$", ylabel=r"$\psi(x)$",
          title=r"Zero total mass: $\rho(x-\frac{1}{2})-\rho(x+\frac{1}{2})$")
    a = axes[1]
    a.plot(grid, phi, color="#287b46", linewidth=2.5,
           label=r"$\phi(x)=-\int_{-\infty}^x\psi(t)\,dt$")
    a.axhline(0, color="#555555", linewidth=.8)
    a.plot([-.25, .25], [1, 1], color="#287b46", linewidth=4)
    a.text(0, .58, r"$-\phi'=\psi$", ha="center")
    a.text(0, 1.06, "Exact plateau: 1", ha="center", fontsize=14)
    for endpoint in (-.75, .75):
        a.axvline(endpoint, color="#8a8a8a", linestyle=":", linewidth=1.2)
    a.set(xlim=(-1, 1), ylim=(-.08, 1.3), xlabel=r"$x$",
          ylabel=r"$\phi(x)$", title="The primitive retains compact support")
    a.set_xticks([-.75, -.25, .25, .75],
                 [r"$-\frac{3}{4}$", r"$-\frac{1}{4}$",
                  r"$\frac{1}{4}$", r"$\frac{3}{4}$"])
    a.text(0, .23, r"$\phi(x)=-\int_{-\infty}^x\psi(t)\,dt$",
           ha="center", fontsize=13)
    for ext in ("png", "svg"):
        fig.savefig(out / ("zero-mass-dual-range-and-compact-primitive."+ext),
                    dpi=180, metadata={"Creator": "Open Mathematics Courses"})
    plt.close(fig)
    geometry = {
        "formula_authority": "Exact formulas and proofs in the learner chapter",
        "first_figure": {
            "multiplier": "3^(-k)", "image_coordinates": "3^(-k)/sqrt(k)",
            "inverse_norm": "sqrt(sum_(k=1)^N 1/k)",
            "inverse_bounds": ["sqrt(log(N+1))", "sqrt(1+log(N))"],
            "image_norm_squared": "log(9/8)",
            "image_error_upper_bound": "3^(-N)/sqrt(8(N+1))",
            "inverse_sample_range": [1, 2000],
            "error_bound_sample_range": [1, 40],
            "lower_panel_is_upper_bound_not_exact_error": True,
        },
        "second_figure": {
            "rho": "c exp(-1/(1-16t^2)) for |t|<1/4;0 elsewhere",
            "normalization_c": str(normalization),
            "decimal_precision_for_normalization": 65,
            "psi": "rho(x-1/2)-rho(x+1/2)",
            "phi": "-integral_(-infinity)^x psi(t)dt",
            "negative_bump_mass": -1, "positive_bump_mass": 1,
            "support_bounds": ["-3/4", "3/4"],
            "exact_plateau": {"interval": ["-1/4", "1/4"], "value": 1},
            "adjoint_sign": "-D phi=psi",
            "sample_count": 8193,
            "drawing_integral_method": "Composite trapezoid for numerical samples",
            "sampled_plateau_max_error": float(np.max(np.abs(
                phi[(grid >= -.25) & (grid <= .25)]-1))),
            "curves_are_numerical_samples_not_a_proof": True,
        },
    }
    (out / "geometry228.json").write_text(
        json.dumps(geometry, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"figures": 2, "formats": ["png", "svg"],
                      "plateau_sample_error":
                      geometry["second_figure"]["sampled_plateau_max_error"]}))


if __name__ == "__main__":
    with TemporaryDirectory(prefix="an02-own228-mpl-") as task_cache:
        os.environ["MPLCONFIGDIR"] = task_cache
        draw()
