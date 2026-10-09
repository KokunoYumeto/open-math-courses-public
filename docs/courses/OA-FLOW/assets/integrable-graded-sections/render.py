"""Moving multiplier projections, their weak-star integral, and scalar convolution.

Original renderer, figure and exact data: CC0-1.0 to the extent of rights held.
Run with Python 3 and Matplotlib. All displayed shapes have exact linear formulas.
"""

from pathlib import Path
from fractions import Fraction
import json
import math
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-integrable-graded-sections-20261009-v1"
from matplotlib import font_manager
from matplotlib.patches import Polygon


OUT = Path(__file__).resolve().parent
INK, MUTED = "#172c40", "#475569"
BLUE, ORANGE = "#1565a9", "#b14c0b"


def polygon_area(points):
    return abs(sum(x*y1-x1*y for (x, y), (x1, y1)
                   in zip(points, points[1:]+points[:1]))) / 2


def axes_style(ax, xlabel, ylabel):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#94a3b8")
    ax.tick_params(labelsize=12, colors=MUTED)
    ax.set_xlabel(xlabel, fontsize=17, loc="right", labelpad=2)
    ax.set_ylabel(ylabel, fontsize=17, rotation=0, loc="top", labelpad=4)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    projection_triangle = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)),
                           (Fraction(1), Fraction(1))]
    convolution_triangle = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(1)),
                            (Fraction(2), Fraction(0))]
    assert polygon_area(projection_triangle) == Fraction(1, 2)
    assert polygon_area(convolution_triangle) == 1
    x0, t0 = Fraction(1, 3), Fraction(2, 3)
    assert 1-x0 == Fraction(2, 3)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                         "mathtext.fontset": "dejavusans", "svg.fonttype": "none",
                         "savefig.facecolor": "#f8fafc"})
    fig = plt.figure(figsize=(18, 8.5), facecolor="#f8fafc")
    fig.text(.04, .942, "Weak-star integration of moving projections", fontsize=29,
             weight="bold", color=INK)
    fig.text(.04, .884,
             r"$a(t)(x)=1_{[0,t]}(x)$ for $0<t<1$, zero elsewhere"
             "      |      "
             r"$M=L^\infty([0,1]),\quad H=L^2([0,1])$",
             fontsize=21, color=INK)
    fig.text(.04, .796, "1. VERTICAL PROJECTIONS, HORIZONTAL LENGTHS", fontsize=14,
             weight="bold", color=MUTED)
    fig.text(.365, .796, "2. THE WEAK-STAR INTEGRAL", fontsize=14,
             weight="bold", color=MUTED)
    fig.text(.70, .796, "3. RECTANGLE CONVOLVED WITH ITSELF", fontsize=14,
             weight="bold", color=MUTED)

    left = fig.add_axes([.068, .27, .255, .455])
    left.add_patch(Polygon([(0, 0), (1, 0), (1, 1)], closed=True,
                           facecolor="#e1edf8", edgecolor="none"))
    left.plot([0, 1], [0, 1], color=INK, lw=1.8)
    left.plot([float(t0), float(t0)], [0, float(t0)], color=ORANGE, lw=4)
    left.annotate("", xy=(1, float(x0)), xytext=(float(x0), float(x0)),
                  arrowprops=dict(arrowstyle="<->", lw=2.4, color=BLUE))
    left.text(.70, .405, r"length $2/3$", ha="center", fontsize=16, color=BLUE)
    left.text(.265, .82, r"$x>t$: zero", fontsize=16, color=MUTED)
    left.text(.76, .10, r"$a(t)(x)=1$", fontsize=16, ha="center", color=INK)
    left.text(.725, .64, r"$x=t$", fontsize=15, color=INK)
    left.set_xlim(-.025, 1.065)
    left.set_ylim(-.025, 1.065)
    left.set_xticks([0, 1/3, 2/3, 1], ["0", r"$1/3$", r"$2/3$", "1"])
    left.set_yticks([0, 1/3, 2/3, 1], ["0", r"$1/3$", r"$2/3$", "1"])
    axes_style(left, r"$t$", r"$x$")
    fig.text(.068, .202, r"Orange: $a(2/3)$ projects onto $L^2([0,2/3])$.",
             fontsize=15, color=ORANGE)
    fig.text(.068, .161, r"Blue: $h(1/3)=|[1/3,1)|=2/3$.",
             fontsize=15, color=BLUE)

    middle = fig.add_axes([.40, .27, .24, .455])
    middle.fill([0, 1, 0], [0, 0, 1], color="#e1edf8")
    middle.plot([0, 1], [1, 0], color=BLUE, lw=3)
    middle.plot([float(x0), float(x0)], [0, float(t0)], color=BLUE, ls="--", lw=1)
    middle.plot([0, float(x0)], [float(t0), float(t0)], color=BLUE, ls="--", lw=1)
    middle.plot([float(x0)], [float(t0)], "o", color=BLUE, markersize=8)
    middle.text(.50, .78, r"$h(x)=1-x$", fontsize=23, color=BLUE)
    middle.text(.28, .25, r"area $=1/2$", fontsize=19, color=INK)
    middle.set_xlim(-.025, 1.065)
    middle.set_ylim(-.025, 1.065)
    middle.set_xticks([0, 1/3, 1], ["0", r"$1/3$", "1"])
    middle.set_yticks([0, 2/3, 1], ["0", r"$2/3$", "1"])
    axes_style(middle, r"$x$", r"$h$")
    fig.text(.40, .202, r"$\int a(t)\xi\,dt=h\xi$ for every $\xi\in H$.",
             fontsize=17, color=INK)
    fig.text(.40, .161, r"$\langle h,g\rangle=\int_0^1(1-x)g(x)\,dx$.",
             fontsize=17, color=INK)

    rect = fig.add_axes([.735, .58, .225, .145])
    rect.fill([0, 1, 1, 0], [0, 0, 1, 1], color="#ffead7")
    rect.plot([-.15, 0, 0, 1, 1, 2.1], [0, 0, 1, 1, 0, 0], color=ORANGE, lw=2.5)
    rect.set_xlim(-.15, 2.1)
    rect.set_ylim(-.02, 1.30)
    rect.set_xticks([0, 1, 2])
    rect.set_yticks([0, 1])
    rect.text(1.16, .80, r"$f=1_{[0,1]}$", fontsize=18, color=ORANGE)
    axes_style(rect, r"$t$", r"$f$")

    tri = fig.add_axes([.735, .27, .225, .22])
    tri.fill([0, 1, 2], [0, 1, 0], color="#ffead7")
    tri.plot([-.15, 0, 1, 2, 2.1], [0, 0, 1, 0, 0], color=ORANGE, lw=3)
    tri.text(1.20, .99, r"$f*f=\Lambda$", fontsize=19, color=ORANGE)
    tri.text(.57, .25, r"area $=1$", fontsize=19, color=INK)
    tri.set_xlim(-.15, 2.1)
    tri.set_ylim(-.02, 1.30)
    tri.set_xticks([0, 1, 2])
    tri.set_yticks([0, 1])
    axes_style(tri, r"$t$", r"$\Lambda$")
    fig.text(.735, .202, r"$\|f*f\|_1=1=\|f\|_1^2$.", fontsize=18, color=ORANGE)
    fig.text(.735, .161, "Young equality: no scalar cancellation.", fontsize=14, color=MUTED)

    fig.text(.04, .085,
             r"$\|a(t)-a(s)\|=1$ for distinct $s,t\in(0,1)$; "
             "vector continuity and the weak-star integral remain valid.", fontsize=20, color=INK)
    fig.text(.04, .03,
             "Exact coordinates and proofs: SEC7.c–l. Endpoint changes have measure zero. The jump at t = 1 and the failure of operator-norm Bochner measurability are retained.",
             fontsize=13, color=MUTED)
    fig.savefig(OUT / "projections-and-convolution.png", dpi=160)
    fig.savefig(OUT / "projections-and-convolution.svg", metadata={"Date": None})
    plt.close(fig)

    data = {
        "operator_model": {"M": "L-infinity([0,1],dx)", "H": "L2([0,1],dx)",
                           "a": "a(t)(x)=1_[0,t](x) for 0<t<1, and zero otherwise",
                           "norm_integral": 1, "pairwise_norm_distance_on_open_interval": 1,
                           "vector_orbit_continuity": "R except t=1; left limit at 1 is xi, value is zero",
                           "not_essentially_norm_separable": True},
        "region": {"horizontal_axis": "t", "vertical_axis": "x", "vertices": [[0, 0], [1, 0], [1, 1]],
                   "horizontal_test_x": "1/3", "horizontal_interval": ["1/3", "1"],
                   "horizontal_length": "2/3", "vertical_test_t": "2/3", "vertical_interval": ["0", "2/3"], "area": "1/2"},
        "weakstar_integral": {"h": "h(x)=1-x a.e.", "predual": "L1([0,1])",
                              "pairing": "integral (1-x)*g(x) dx", "norm": 1, "pairing_with_one": "1/2"},
        "vector_test_xi_one": {"integral_vector_norm": "2/3", "norm_vector_integral": "1/sqrt(3)"},
        "scalar_model": {"f": "1_[0,1]", "convolution_vertices": [[0, 0], [1, 1], [2, 0]],
                         "convolution": "t on [0,1], 2-t on [1,2], zero elsewhere", "norm": 1,
                         "involution": "conjugate reflection"},
        "matrix_diagnostic": {"D": [[4, 0], [0, 1]], "omega": "log(4)", "L": "pi/log(4)",
                              "c_at_L": "(-2i/log(4))*e11", "convolution_norm": "8/log(4)^2",
                              "young_upper_bound": "pi^2/log(4)^2"},
        "point_support": "Zero in the a.e. L1 quotient, not a Dirac measure",
        "exact_rational_area_checks": "passed",
        "proof_locators": ["SEC7.c", "SEC7.d", "SEC7.e", "SEC7.f", "SEC7.g", "SEC7.h", "SEC7.j", "SEC7.k", "SEC7.l"],
    }
    (OUT / "data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    font = Path(font_manager.findfont("DejaVu Sans"))
    if (font.parent / "LICENSE_DEJAVU").is_file():
        shutil.copyfile(font.parent / "LICENSE_DEJAVU", OUT / "FONT-LICENSE.txt")
    print(json.dumps({"rendered": ["projections-and-convolution.png", "projections-and-convolution.svg"],
                      "data": "data.json", "exact_area_checks": "passed"}))


if __name__ == "__main__":
    main()
