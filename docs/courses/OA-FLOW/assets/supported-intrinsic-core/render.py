"""Exact support matrices and spectral-interval trace normalization.

Original renderer, figure and data: CC0-1.0 to the extent of rights held.
Run with Python 3, NumPy and Matplotlib. The mathematical proofs are in SCW 7–8.
"""

from pathlib import Path
import json
import math
import shutil

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-supported-intrinsic-core-20261009-v1"
from matplotlib import font_manager
from matplotlib.patches import Rectangle


OUT = Path(__file__).resolve().parent
BLUE, ORANGE, INK, MUTED = "#1565a9", "#b14c0b", "#172c40", "#475569"


def matrix(ax, center_y, entries, active_second=False):
    x0, y0, w, h = .14, center_y-.12, .72, .24
    for i in range(2):
        for j in range(2):
            x, y = x0+j*w/2, y0+(1-i)*h/2
            color = BLUE if (i, j) == (0, 0) else ORANGE if (i, j) == (1, 1) and active_second else MUTED
            fill = "#dfedfa" if (i, j) == (0, 0) else "#ffead7" if (i, j) == (1, 1) and active_second else "#edf1f5"
            ax.add_patch(Rectangle((x, y), w/2, h/2,
                                   facecolor=fill, edgecolor="white", lw=2))
            ax.text(x+w/4, y+h/4, entries[i][j], color=color,
                    ha="center", va="center", fontsize=23)


def interval_plot(fig, rect, interval, color, label, value):
    ax = fig.add_axes(rect)
    q = np.linspace(-1.05, 1.2, 700)
    density = np.exp(q)/(2*np.pi)
    ax.plot(q, density, color=INK, lw=2)
    qi = np.linspace(interval[0], interval[1], 250)
    ax.fill_between(qi, 0, np.exp(qi)/(2*np.pi), color=color, alpha=.26)
    for x in interval:
        ax.plot([x, x], [0, math.exp(x)/(2*math.pi)], color=color, lw=1.3, ls="--")
    ax.set_xlim(-1.05, 1.2)
    ax.set_ylim(0, .56)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["bottom", "left"]].set_color("#94a3b8")
    ax.tick_params(labelsize=11, colors=MUTED)
    ax.set_yticks([0, .2, .4])
    ax.set_xticks([-math.log(2), 0, 1-math.log(2), 1],
                  [r"$-\log2$", "0", r"$1-\log2$", "1"])
    ax.set_title(label, loc="left", fontsize=16, color=color, pad=12)
    ax.text(.035, .83, value, transform=ax.transAxes, fontsize=16, color=color)
    ax.set_xlabel(r"$q$", loc="right", fontsize=15, labelpad=0)
    return ax


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    e = np.array([[1, 0], [0, 0]], dtype=int)
    f = np.eye(2, dtype=int)-e
    b_power = np.array([[0, -1], [-1, 0]], dtype=int)
    u = e @ b_power
    assert np.array_equal(u, np.array([[0, -1], [0, 0]]))
    assert np.array_equal(u @ u.T, e)
    assert np.array_equal(u.T @ u, f)
    assert np.array_equal(u @ b_power, e)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                         "mathtext.fontset": "dejavusans", "svg.fonttype": "none",
                         "savefig.facecolor": "#f8fafc"})
    fig = plt.figure(figsize=(18, 9), facecolor="#f8fafc")
    fig.text(.04, .945, "A supported weight retains its actual corner", fontsize=28,
             weight="bold", color=INK)
    fig.text(.04, .891,
             r"$M=M_2(\mathbb{C}),\quad \varphi(x)=x_{11},\quad e=e_{11},"
             r"\quad C=M_2\,\overline{\otimes}\,L^\infty(\mathbb{R},dq)$",
             fontsize=21, color=INK)

    left = fig.add_axes([.04, .18, .28, .63])
    mid = fig.add_axes([.355, .18, .285, .63])
    for ax in (left, mid):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
    left.text(0, .98, "SUPPORTED DENSITY AND POWERS", color=MUTED,
              fontsize=15, weight="bold")
    left.text(.5, .855, r"$h_\varphi(q)$", ha="center", fontsize=22, color=INK)
    matrix(left, .68, [[r"$e^{-q}$", "0"], ["0", "0"]])
    left.text(.5, .45, r"$v_\varphi(t)(q)$", ha="center", fontsize=22, color=INK)
    matrix(left, .28, [[r"$e^{-itq}$", "0"], ["0", "0"]])
    left.text(.5, .065, r"$v_\varphi(0)=e_{11}$", ha="center", fontsize=22, color=BLUE)
    left.text(.5, -.012, "The complementary block remains zero.",
              ha="center", fontsize=13, color=MUTED)

    mid.text(0, .98, "THE AMBIENT UNIT CHANGES THE JOIN", color=MUTED,
             fontsize=15, weight="bold")
    mid.text(.5, .855, r"$D_e^\varphi\subset eCe$", ha="center", fontsize=22, color=INK)
    matrix(mid, .68, [[r"$F(q)$", "0"], ["0", "0"]])
    mid.text(.5, .495, r"$D_e^\varphi\cap eMe=\mathbb{C}e_{11}$",
             ha="center", fontsize=19, color=BLUE)
    mid.text(.5, .40, r"$D_{\mathrm{full}}^\varphi\subset C$", ha="center", fontsize=22, color=INK)
    matrix(mid, .225, [[r"$F(q)$", "0"], ["0", r"$G(q)$"]], active_second=True)
    mid.text(.5, .04, r"$D_{\mathrm{full}}^\varphi\cap M=\mathbb{C}e_{11}\oplus\mathbb{C}e_{22}$",
             ha="center", fontsize=17, color=ORANGE)

    fig.text(.688, .797, "EXACT SPECTRAL INTERVALS", color=MUTED,
             fontsize=15, weight="bold")
    fig.text(.688, .754, r"Trace density: $e^q/(2\pi)$", color=INK, fontsize=18)
    interval_plot(fig, [.695, .49, .265, .205], [0, 1], ORANGE,
                  r"$P=e_{11}\otimes1_{[0,1)}$",
                  r"$\tau(P)=(\mathrm{e}-1)/(2\pi)$")
    interval_plot(fig, [.695, .20, .265, .205], [-math.log(2), 1-math.log(2)], BLUE,
                  r"$\theta_{\log2}(P)=e_{11}\otimes1_{[-\log2,1-\log2)}$",
                  r"$\tau(\theta_{\log2}P)=(\mathrm{e}-1)/(4\pi)$")

    fig.text(.04, .093,
             r"$\tau(Y)=\int\mathrm{Tr}(Y(q))e^q\,dq/(2\pi)$"
             r"     while     $\widetilde{\varphi}(Y)=\int Y_{11}(q)\,dq/(2\pi)$",
             fontsize=21, color=INK)
    fig.text(.04, .04,
             "Exact formulas: SCW.7.f–j and SCW.8.k–l.  The plots show scalar trace density on spectral intervals; the full operator domains remain in the proof.",
             fontsize=13, color=MUTED)
    fig.savefig(OUT / "support-and-coordinate.png", dpi=160)
    fig.savefig(OUT / "support-and-coordinate.svg", metadata={"Date": None})
    plt.close(fig)

    data = {
        "model": {"M": "M_2(C)", "weight": "phi(x)=x_11", "support": [[1, 0], [0, 0]]},
        "density": [["exp(-q)", "0"], ["0", "0"]],
        "powers": [["exp(-i*t*q)", "0"], ["0", "0"]],
        "supported_join": "{diag(F(q),0): F in L-infinity(R)}",
        "full_join": "{diag(F(q),G(q)): F,G in L-infinity(R)}",
        "canonical_trace": "integral Tr(Y(q))*exp(q) dq/(2*pi)",
        "dual_weight": "integral Y_11(q) dq/(2*pi)",
        "interval": {"original": ["0", "1"], "translated": ["-log(2)", "1-log(2)"], "convention": "left closed, right open"},
        "trace_values": {"original_exact": "(exp(1)-1)/(2*pi)", "translated_exact": "(exp(1)-1)/(4*pi)",
                         "original_numeric": (math.e-1)/(2*math.pi), "translated_numeric": (math.e-1)/(4*math.pi)},
        "dual_weight_both_exact": "1/(2*pi)",
        "partial_cocycle_diagnostic": {"B": [[2, 1], [1, 2]], "t0": "pi/log(3)",
                                      "B_to_it0": b_power.tolist(), "u_t0": u.tolist(),
                                      "initial_support": f.tolist(), "final_support": e.tolist()},
        "proof_locators": ["SCW.7.f", "SCW.7.g", "SCW.7.h", "SCW.7.i", "SCW.7.j", "SCW.8.g", "SCW.8.h", "SCW.8.k", "SCW.8.l"],
        "rendered_plot_is_a_finite_sample": True,
        "exact_integer_matrix_checks": "passed",
    }
    (OUT / "data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    font = Path(font_manager.findfont("DejaVu Sans"))
    if (font.parent / "LICENSE_DEJAVU").is_file():
        shutil.copyfile(font.parent / "LICENSE_DEJAVU", OUT / "FONT-LICENSE.txt")
    print(json.dumps({"rendered": ["support-and-coordinate.png", "support-and-coordinate.svg"],
                      "data": "data.json", "exact_matrix_checks": "passed"}))


if __name__ == "__main__":
    main()
