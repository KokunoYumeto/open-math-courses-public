"""Exact norm witnesses and graded matrix product for GRD Sections 7–8.

Original renderer, data and figure: CC0-1.0 to the extent of rights held.
Run with Python 3, NumPy and Matplotlib. Plotted curves connect finite samples.
"""

from pathlib import Path
import json
import math
import shutil

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-graded-core-fibers-20261008-v1"
from matplotlib import font_manager
from matplotlib.patches import Rectangle


OUT = Path(__file__).resolve().parent
INK, MUTED = "#172c40", "#475569"
BLUE, ORANGE = "#1565a9", "#b14c0b"


def small_matrix(ax, x0, y0, entries, width=.25, height=.20):
    for i in range(2):
        for j in range(2):
            x, y = x0+j*width/2, y0+(1-i)*height/2
            active = entries[i][j] != "0"
            ax.add_patch(Rectangle((x, y), width/2, height/2,
                                   facecolor="#deecfa" if active else "#edf1f5",
                                   edgecolor="white", lw=2))
            ax.text(x+width/4, y+height/4, entries[i][j], ha="center", va="center",
                    fontsize=21, color=BLUE if active else MUTED)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    e12 = np.array([[0, 1], [0, 0]], dtype=complex)
    e21 = e12.T
    e11, e22 = e12 @ e21, e21 @ e12
    d_power = np.diag([1j, 1])
    d_inverse = d_power.conj().T
    sigma_b = d_power @ e21 @ d_inverse
    star_coefficient = d_inverse @ e21 @ d_power
    assert np.array_equal(sigma_b, -1j * e21)
    assert np.array_equal(e12 @ sigma_b, -1j * e11)
    assert np.array_equal(star_coefficient, 1j * e21)
    assert np.array_equal(star_coefficient @ (d_inverse @ e12 @ d_power), e22)
    assert np.array_equal(e12 @ (d_power @ star_coefficient @ d_inverse), e11)

    sample_k = [1, 2, 4, 8, 16, 32, 64]
    seminorm = [math.sqrt(12*(1-math.cos(math.pi/k))/(5-4*math.cos(math.pi/k))) for k in sample_k]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                         "mathtext.fontset": "dejavusans", "svg.fonttype": "none",
                         "savefig.facecolor": "#f8fafc"})
    fig = plt.figure(figsize=(18, 9), facecolor="#f8fafc")
    fig.text(.04, .945, "Fiber isometries do not force continuous norm charts",
             fontsize=27, weight="bold", color=INK)
    fig.text(.04, .887,
             r"$u(t)_n=e^{int},\quad t_k=\pi/k$"
             "      |      Exact witnesses and a modular matrix calculation",
             fontsize=21, color=INK)

    table = fig.add_axes([.04, .49, .46, .30])
    table.set_xlim(0, 4)
    table.set_ylim(0, 6)
    table.axis("off")
    headings = [r"$k$", r"$t_k$", r"$u(t_k)_k$", r"$\|u(t_k)-1\|$"]
    for j, heading in enumerate(headings):
        table.text(j+.5, 5.7, heading, ha="center", va="center", fontsize=19, color=INK)
    for row, k in enumerate(sample_k[:5]):
        y = 4-row
        values = [str(k), r"$\pi$" if k == 1 else rf"$\pi/{k}$", r"$-1$", "2"]
        for j, value in enumerate(values):
            table.add_patch(Rectangle((j+.02, y+.04), .96, .86,
                                      facecolor="#ffecd9" if j == 3 else "#e5eef7",
                                      edgecolor="white", lw=1))
            table.text(j+.5, y+.46, value, ha="center", va="center", fontsize=19,
                       color=ORANGE if j == 3 else INK)
    fig.text(.04, .818, "THE WITNESS MOVES TO COORDINATE n = k", fontsize=15,
             weight="bold", color=MUTED)

    plot = fig.add_axes([.078, .195, .412, .245])
    plot.set_xscale("log", base=2)
    plot.plot(sample_k, [2]*len(sample_k), "o-", color=ORANGE, lw=2,
              label=r"$\|u(t_k)-1\|=2$")
    plot.plot(sample_k, seminorm, "s-", color=BLUE, lw=2,
              label=r"$p_w(u(t_k)-1),\quad w_n=2^{-n}$")
    plot.set_xticks(sample_k, [str(k) for k in sample_k])
    plot.set_ylim(0, 2.35)
    plot.set_yticks([0, .5, 1, 1.5, 2])
    plot.spines[["top", "right"]].set_visible(False)
    plot.spines[["left", "bottom"]].set_color("#94a3b8")
    plot.tick_params(colors=MUTED, labelsize=12)
    plot.set_xlabel(r"$k$  (so $t_k\to0$ as $k\to\infty$)", fontsize=15)
    plot.legend(loc="center left", fontsize=13, frameon=False)

    right = fig.add_axes([.56, .16, .40, .65])
    right.set_xlim(0, 1)
    right.set_ylim(0, 1)
    right.axis("off")
    right.text(0, .985, "THE MODULAR ACTION CHANGES THE COEFFICIENT", fontsize=15,
               color=MUTED, weight="bold")
    right.text(.5, .9, r"$D=\mathrm{diag}(4,1),\quad s_0=\pi/(2\log4)$",
               ha="center", fontsize=22, color=INK)
    right.text(.145, .79, r"$e_{12}$", ha="center", fontsize=20, color=INK)
    right.text(.495, .79, r"$\sigma_{s_0}^{\varphi}(e_{21})$", ha="center", fontsize=20, color=INK)
    right.text(.845, .79, r"$-i e_{11}$", ha="center", fontsize=20, color=INK)
    small_matrix(right, .02, .55, [["0", "1"], ["0", "0"]])
    small_matrix(right, .37, .55, [["0", "0"], [r"$-i$", "0"]])
    small_matrix(right, .72, .55, [[r"$-i$", "0"], ["0", "0"]])
    right.text(.32, .65, r"$\times$", ha="center", va="center", fontsize=24, color=INK)
    right.text(.67, .65, "=", ha="center", va="center", fontsize=24, color=INK)
    right.text(.5, .465,
               r"$(e_{12}\varphi^{is_0})(e_{21}\varphi^{is_0})"
               r"=-i e_{11}\varphi^{2is_0}$",
               ha="center", fontsize=21, color=INK)
    right.text(0, .36, "THE ADJOINT HAS DEGREE −s₀", fontsize=15,
               color=MUTED, weight="bold")
    small_matrix(right, .02, .075, [["0", "0"], [r"$i$", "0"]], width=.28, height=.22)
    right.text(.64, .22, r"$(e_{12}\varphi^{is_0})^*"
               r"=i e_{21}\varphi^{-is_0}$", ha="center", fontsize=21, color=INK)
    right.text(.64, .10, r"$a^*a=e_{22},\qquad aa^*=e_{11}$", ha="center",
               fontsize=21, color=BLUE)

    fig.text(.04, .085,
             r"One plotted seminorm:  $p_w(u(t)-1)^2=12(1-\cos t)/(5-4\cos t)$."
             "  Every positive ℓ¹ functional is handled by the proof.", fontsize=18, color=INK)
    fig.text(.04, .032,
             "Exact identities: GRD.7.c–e and GRD.7.j–m.  Points and connecting segments are finite samples; they do not replace the continuity proof.",
             fontsize=13, color=MUTED)
    fig.savefig(OUT / "norm-and-product.png", dpi=160)
    fig.savefig(OUT / "norm-and-product.svg", metadata={"Date": None})
    plt.close(fig)

    data = {
        "norm_model": {"algebra": "ell-infinity(N), N={1,2,...}", "trace": "sum a_n",
                       "density": "h_n=exp(n)", "weight": "sum exp(n)*a_n", "cocycle": "u(t)_n=exp(i*n*t)"},
        "witness": {"t_k": "pi/k", "coordinate": "n=k", "phase_exact": "-1", "norm_distance_exact": 2},
        "seminorm": {"weights": "w_n=2^(-n)", "square_exact": "12*(1-cos(t))/(5-4*cos(t))",
                     "all_positive_l1_functionals_required_for_continuity": True},
        "plot_samples": [{"k": k, "time_exact": f"pi/{k}", "norm_exact": 2, "seminorm_numeric": p}
                         for k, p in zip(sample_k, seminorm)],
        "matrix_model": {"D": [[4, 0], [0, 1]], "s0": "pi/(2*log(4))",
                         "sigma_s0_e21": [["0", "0"], ["-i", "0"]],
                         "product_coefficient": [["-i", "0"], ["0", "0"]],
                         "product_degree": "2*s0", "adjoint_coefficient": [["0", "0"], ["i", "0"]],
                         "adjoint_degree": "-s0", "a_star_a": [[0, 0], [0, 1]], "a_a_star": [[1, 0], [0, 0]]},
        "scalar_direction": {"from_weight": 1, "to_weight": 4, "time": "pi/(2*log(4))", "coefficient_factor": "-i"},
        "proof_locators": ["GRD.7.c", "GRD.7.d", "GRD.7.e", "GRD.7.j", "GRD.7.k", "GRD.7.l", "GRD.7.m"],
        "matrix_checks": "passed using exact integer and imaginary-unit entries",
        "plotted_lines_only_connect_finite_samples": True,
    }
    (OUT / "data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    font = Path(font_manager.findfont("DejaVu Sans"))
    if (font.parent / "LICENSE_DEJAVU").is_file():
        shutil.copyfile(font.parent / "LICENSE_DEJAVU", OUT / "FONT-LICENSE.txt")
    print(json.dumps({"rendered": ["norm-and-product.png", "norm-and-product.svg"],
                      "data": "data.json", "matrix_checks": "passed"}))


if __name__ == "__main__":
    main()
