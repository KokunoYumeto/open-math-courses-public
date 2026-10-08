"""Exact tensor-flow figure. Run: python render.py

This program independently draws the unit-circle model from data.json.
Original code and figure: CC0-1.0. Font terms: FONT_LICENSE_DEJAVU.txt and FONT_LICENSE_STIX.txt.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
C = DATA["rendering"]["colors"]
F = Fraction


def pair(values):
    return tuple(F(x) for x in values)


def quotient(point):
    return sum(point, F(0)) % 1


def validate_exact_data():
    """All displayed transformations are checked in exact rational arithmetic."""
    d = DATA["exact"]
    a = pair(d["start"])
    t = F(d["parameter"])
    b = (a[0] + t, a[1] - t)
    c = (a[0] + t, a[1])
    diagonal = (a[0] + t, a[1] + t)
    half = (a[0] + t / 2, a[1] + t / 2)
    assert pair(DATA["model"]["circle_lengths"]) == (F(1), F(1))
    assert a == (F(1, 4), F(1, 2))
    assert pair(d["opposite_displacement"]) == (t, -t)
    assert pair(d["first_factor_displacement"]) == (t, F(0))
    assert b == pair(d["opposite_endpoint"]) == (F(1, 2), F(1, 4))
    assert c == pair(d["first_factor_endpoint"]) == (F(1, 2), F(1, 2))
    assert diagonal == pair(d["same_time_diagonal_endpoint"])
    assert half == pair(d["half_time_diagonal_endpoint"])
    assert quotient(a) == F(d["quotient_start"]) == F(3, 4)
    assert quotient(b) == F(d["quotient_opposite_endpoint"]) == F(3, 4)
    assert quotient(c) == F(d["quotient_first_factor_endpoint"]) == F(0)
    assert quotient(diagonal) == F(d["quotient_same_time_diagonal_endpoint"]) == F(1, 4)
    assert quotient(half) == F(d["quotient_half_time_diagonal_endpoint"]) == F(0)
    assert quotient(a) + t == 1
    # Exact sample identities supplement the algebraic formula printed below.
    for r in (F(0), F(1, 4), F(3, 4)):
        for s in (F(-1, 3), F(0), F(1, 4), F(7, 5)):
            assert (r + s / 2 + s / 2) % 1 == (r + s) % 1
            assert (r + s + s) % 1 == (r + 2 * s) % 1
    return a, b, c


def arrow(ax, start, end, color, width=3.0, scale=18, **kwargs):
    patch = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=scale,
                            linewidth=width, color=color, shrinkA=0, shrinkB=0,
                            zorder=6, **kwargs)
    ax.add_patch(patch)
    return patch


def circle_coordinate(r):
    return np.column_stack((np.sin(2 * np.pi * r), np.cos(2 * np.pi * r)))


def render():
    a, b, c = validate_exact_data()
    cfg = DATA["rendering"]
    plt.rcParams.update({
        "font.family": cfg["font_family"],
        "mathtext.fontset": cfg["mathtext_fontset"],
        "mathtext.fallback": cfg["mathtext_fallback"],
        "svg.fonttype": "path",
        "svg.hashsalt": cfg["svg_hashsalt"],
        "font.size": 12,
        "axes.unicode_minus": False,
        "savefig.facecolor": C["paper"],
        "figure.facecolor": C["paper"],
        "path.simplify": False,
    })
    fig = plt.figure(figsize=cfg["figure_inches"], dpi=cfg["dpi"])
    fig.text(0.055, 0.951, DATA["title"], fontsize=23, weight="bold", color=C["ink"])
    fig.text(0.055, 0.916,
             r"Coordinate convention: $(\theta_s f)(q)=f(q+s)$;  $L_1=L_2=1$.",
             fontsize=14, color=C["muted"])
    fig.text(0.085, 0.865, "A  Product of the two circles", fontsize=16,
             weight="bold", color=C["ink"])
    fig.text(0.635, 0.865, "B  The quotient circle", fontsize=16,
             weight="bold", color=C["ink"])

    ax = fig.add_axes([0.055, 0.34, 0.385, 0.50])
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(-0.12, 1.12)
    ax.set_aspect("equal")
    ax.axis("off")
    square = Rectangle((0, 0), 1, 1, facecolor="#FBFCFD",
                       edgecolor=C["ink"], linewidth=1.6, zorder=1)
    ax.add_patch(square)

    # These are straight pieces of torus fibers, not unrelated contour levels.
    # A fiber r consists of q1+q2=r and q1+q2=r+1 within the square.
    for total in [F(j, 4) for j in range(1, 8)]:
        lo, hi = max(F(0), total - 1), min(F(1), total)
        is_start_fiber = total % 1 == F(3, 4)
        color = C["orange"] if is_start_fiber else C["grid"]
        line, = ax.plot([float(lo), float(hi)],
                        [float(total - lo), float(total - hi)],
                        color=color, linewidth=1.1 if is_start_fiber else 0.9,
                        linestyle=(0, (4, 4)), alpha=0.46 if is_start_fiber else 1,
                        zorder=2)
        line.set_clip_path(square)

    # Matched directions on paired edges encode the torus edge identifications.
    for y in (0.0, 1.0):
        arrow(ax, (0.66, y), (0.75, y), C["muted"], width=1.4, scale=12)
        arrow(ax, (0.71, y), (0.80, y), C["muted"], width=1.4, scale=12)
    for x in (0.0, 1.0):
        arrow(ax, (x, 0.67), (x, 0.78), C["muted"], width=1.4, scale=12)

    for value, label in [(0, "0"), (0.25, r"$1/4$"), (0.5, r"$1/2$"),
                         (0.75, r"$3/4$"), (1, "1")]:
        ax.plot([value, value], [0, -0.013], color=C["muted"], lw=0.8)
        ax.text(value, -0.045, label, ha="center", va="top", fontsize=11, color=C["muted"])
    for value, label in [(0, "0"), (0.5, r"$1/2$"), (1, "1")]:
        ax.plot([-0.013, 0], [value, value], color=C["muted"], lw=0.8)
        ax.text(-0.035, value, label, ha="right", va="center", fontsize=11, color=C["muted"])
    ax.text(1.10, -0.005, r"$q_1$", fontsize=15, color=C["ink"])
    ax.text(-0.012, 1.085, r"$q_2$", fontsize=15, color=C["ink"])

    av, bv, cv = [tuple(map(float, point)) for point in (a, b, c)]
    arrow(ax, av, bv, C["orange"], width=3.1, scale=18)
    arrow(ax, av, cv, C["blue"], width=3.1, scale=18)
    ax.scatter(*av, s=45, color=C["ink"], zorder=8)
    ax.scatter(*bv, s=30, color=C["orange"], zorder=8)
    ax.scatter(*cv, s=30, color=C["blue"], zorder=8)
    ax.annotate(r"$A=(1/4,\,1/2)$", av, xytext=(-8, 14),
                textcoords="offset points", ha="right", fontsize=12.5, color=C["ink"])
    ax.annotate(r"$B=(1/2,\,1/4)$", bv, xytext=(12, -4),
                textcoords="offset points", ha="left", fontsize=12.5, color=C["orange"])
    ax.annotate(r"$C=(1/2,\,1/2)$", cv, xytext=(12, 10),
                textcoords="offset points", ha="left", fontsize=12.5, color=C["blue"])
    ax.text(0.44, 0.61, r"$(s,0)$,  $s=1/4$", color=C["blue"], fontsize=12)
    ax.text(0.10, 0.15, r"$(t,-t)$,  $t=1/4$", color=C["orange"], fontsize=12)
    fig.text(0.25, 0.325, "Left ≡ right; bottom ≡ top.", ha="center",
             fontsize=12, color=C["muted"])
    fig.text(0.25, 0.299, "Dashed pieces are constant-r fibers.", ha="center",
             fontsize=11.5, color=C["muted"])

    # Q is a geometric map; its pullback is the opposite-direction algebra map.
    fig.add_artist(FancyArrowPatch((0.458, 0.632), (0.598, 0.632),
                    transform=fig.transFigure, arrowstyle="-|>", mutation_scale=20,
                    linewidth=1.8, color=C["ink"]))
    fig.text(0.528, 0.657, r"$Q(q_1,q_2)=q_1+q_2\ (\mathrm{mod}\ 1)$",
             ha="center", fontsize=13, color=C["ink"])
    fig.text(0.528, 0.595, r"$Q^*:L^\infty(\mathbb{R}/\mathbb{Z})\ \cong\ F$",
             ha="center", fontsize=12.5, color=C["muted"])
    fig.text(0.528, 0.566, r"$F=(A_1\bar\otimes A_2)^\delta$",
             ha="center", fontsize=12.5, color=C["muted"])

    ac = fig.add_axes([0.615, 0.355, 0.335, 0.485])
    ac.set_xlim(-1.45, 1.40)
    ac.set_ylim(-1.37, 1.37)
    ac.set_aspect("equal")
    ac.axis("off")
    rr = np.linspace(0, 1, cfg["circle_samples"])
    ring = circle_coordinate(rr)
    ac.plot(ring[:, 0], ring[:, 1], color=C["muted"], linewidth=1.4, zorder=1)
    for r in (0, 0.25, 0.5, 0.75):
        d = circle_coordinate(np.array([r]))[0]
        ac.plot([d[0] * 0.97, d[0] * 1.03], [d[1] * 0.97, d[1] * 1.03],
                color=C["muted"], linewidth=1, zorder=2)
    arc = circle_coordinate(np.linspace(0.75, 1.0, cfg["arc_samples"]))
    ac.plot(arc[:, 0], arc[:, 1], color=C["blue"], linewidth=3.4, zorder=4)
    arrow(ac, arc[-8], arc[-1], C["blue"], width=3.4, scale=19)
    ac.scatter([-1], [0], s=95, facecolors="white", edgecolors=C["orange"],
               linewidths=2.5, zorder=6)
    ac.scatter([-1], [0], s=22, color=C["ink"], zorder=7)
    ac.scatter([0], [1], s=38, color=C["blue"], zorder=7)
    ac.text(0, 1.15, r"$r=0$", ha="center", fontsize=14, color=C["blue"])
    ac.text(1.11, 0, r"$1/4$", va="center", fontsize=12.5, color=C["muted"])
    ac.text(0, -1.20, r"$1/2$", ha="center", fontsize=12.5, color=C["muted"])
    ac.text(-1.10, -0.16, r"$3/4$", ha="right", fontsize=12.5, color=C["ink"])
    ac.text(0, 0.11, r"$r\longmapsto r+s$", ha="center", fontsize=18, color=C["blue"])
    ac.text(0, -0.10, r"$s=1/4$", ha="center", fontsize=14, color=C["blue"])
    ac.text(0, -0.34, "Positive coordinate time\nruns clockwise.", ha="center",
             va="center", fontsize=11, color=C["muted"], linespacing=1.4)
    fig.text(0.785, 0.325, r"Opposite motion:  $Q(A)=Q(B)=3/4$",
             ha="center", fontsize=13, color=C["orange"])
    fig.text(0.785, 0.294, r"First-factor motion:  $Q(A)=3/4\ \longmapsto\ Q(C)=0$",
             ha="center", fontsize=13, color=C["blue"])

    strip = FancyBboxPatch((0.055, 0.106), 0.89, 0.148,
                          boxstyle="round,pad=0.008,rounding_size=0.012",
                          transform=fig.transFigure, facecolor=C["panel"],
                          edgecolor="none", zorder=-1)
    fig.add_artist(strip)
    fig.text(0.075, 0.219, "The residual action has one time parameter", fontsize=14,
             weight="bold", color=C["ink"])
    fig.text(0.075, 0.178,
             r"$\rho_s=(\theta^1_s\bar\otimes\mathrm{id})|_F"
             r"=(\mathrm{id}\bar\otimes\theta^2_s)|_F"
             r"=(\theta^1_{s/2}\bar\otimes\theta^2_{s/2})|_F$",
             fontsize=15, color=C["blue"])
    fig.text(0.075, 0.133,
             r"Same-time diagonal: $(\theta^1_s\bar\otimes\theta^2_s)|_F=\rho_{2s}$."
             r"   Period groups: $\ker\rho=\mathbb{Z}$; diagonal $=\frac{1}{2}\mathbb{Z}$.",
             fontsize=13.2, color=C["ink"])
    fig.text(0.055, 0.066,
             "Proof: OA-FLOW-TF, TF31–TF34.  The diagram shows the equal-circle case.",
             fontsize=10.5, color=C["muted"])
    fig.text(0.055, 0.043,
             "Human-source antecedent: Takesaki, Theory of Operator Algebras II, Exercise XII.4.2, p. 420.",
             fontsize=10.5, color=C["muted"])
    fig.text(0.945, 0.018, "Original figure / data / renderer: CC0-1.0",
             ha="right", fontsize=9, color=C["muted"])

    svg_meta = {"Title": DATA["title"], "Creator": "Original OA-FLOW illustration",
                "Description": DATA["caption"], "Date": None}
    png_meta = {"Title": DATA["title"], "Description": DATA["caption"],
                "Software": "Matplotlib; OA-FLOW-TF/render.py"}
    fig.savefig(ROOT / "tensor-flow.svg", format="svg", metadata=svg_meta)
    fig.savefig(ROOT / "tensor-flow.png", format="png", dpi=cfg["dpi"], metadata=png_meta)
    plt.close(fig)


if __name__ == "__main__":
    render()
    print("Exact rational checks passed; tensor-flow.svg and tensor-flow.png rendered.")
