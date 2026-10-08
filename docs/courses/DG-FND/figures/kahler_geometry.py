"""Exact projective metric sections; see this course's complex/Kahler G.1–G.3.

Run with Python, NumPy and Matplotlib; the PNG is written beside this script.
The left panel uses points of the radius-1/2 sphere in the meridian Y=0.
The right panel uses tangent vectors at z=(1,0,...,0), complex dimension >=2.
Mathematical reading: Kartik Venkatram, notes prepared in collaboration
with Denis Auroux, MIT 18.966 lecture 14, Spring 2007 (the chapter identifies
the exact free MIT OpenCourseWare notes). The geometry and every scale used here are
proved in the chapter, including the original coordinate derivations.
New plotting code and figure: CC0 1.0. No source figure is reproduced.
"""
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse


def sphere_point(x):
    s = 1 + x*x
    return x/s, (x*x-1)/(2*s)


def main():
    navy, teal, orange, gray = "#15334d", "#007f83", "#c3571e", "#697586"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "text.color": navy, "axes.labelcolor": navy,
                         "axes.edgecolor": "#bdc7d0", "xtick.color": gray,
                         "ytick.color": gray, "figure.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(13.0, 5.8))
    fig.subplots_adjust(left=.055, right=.98, bottom=.18, top=.80, wspace=.23)
    fig.suptitle("The projective metric at two scales", fontsize=19, x=.055, ha="left", y=.97)
    fig.text(.055, .905, "Exact sections of the Fubini–Study metric  |  proofs G.1–G.3", fontsize=12, color=gray)
    ax.set_title("Points on the round projective line", loc="left", fontsize=13, pad=14)
    bx.set_title("Unit vectors at one fixed point", loc="left", fontsize=13, pad=14)
    for a in (ax, bx):
        a.set_aspect("equal", adjustable="box")
        a.spines[["top", "right"]].set_visible(False)
        a.grid(color="#e9eef2", linewidth=.7)
        a.set_axisbelow(True)
    ax.add_patch(Circle((0, 0), .5, facecolor="#edf7f7", edgecolor=navy, linewidth=1.8, zorder=2))
    ax.axhline(-.5, color=gray, linewidth=1.2)
    ax.scatter([0], [.5], c=navy, s=35, zorder=5)
    ax.annotate(r"$N=(0,\frac{1}{2})$", (0, .5), xytext=(-58, 15),
                textcoords="offset points", fontsize=12)
    for x, color, label, offset in [
        (Q(1, 2), teal, r"$F(\frac{1}{2},0)=(\frac{2}{5},-\frac{3}{10})$", (-104, -23)),
        (Q(1), orange, r"$F(1,0)=(\frac{1}{2},0)$", (13, 15)),
    ]:
        X, Z = sphere_point(x)
        assert X*X+Z*Z == Q(1, 4)
        # Both coordinates of N+(A-N)/(1+x^2) agree exactly.
        assert X == x/(1+x*x) and Z == Q(1, 2)-1/(1+x*x)
        ax.plot([0, float(x)], [.5, -.5], color=color, linewidth=1.5, zorder=3)
        ax.scatter([float(X)], [float(Z)], c=color, s=38, zorder=5)
        ax.scatter([float(x)], [-.5], c=color, marker="s", s=30, zorder=5)
        ax.annotate(label, (float(X), float(Z)), xytext=offset, textcoords="offset points",
                    color=color, fontsize=11,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2, "alpha": .93})
    ax.text(.55, -.595, r"$A(\frac{1}{2})$", color=teal, ha="center")
    ax.text(1.015, -.595, r"$A(1)$", color=orange, ha="center")
    ax.text(-.57, -.585, "south-pole\n tangent plane", fontsize=10, color=gray, va="top")
    ax.set_xlim(-.65, 1.18)
    ax.set_ylim(-.73, .77)
    ax.set_xlabel(r"$X$   (the omitted coordinate is $Y=0$)")
    ax.set_ylabel(r"$Z$")
    ax.set_xticks([-.5, 0, .5, 1])
    ax.set_yticks([-.5, 0, .5])

    bx.add_patch(Ellipse((0, 0), 4, 2*np.sqrt(2), facecolor="#edf7f7",
                        edgecolor=teal, linewidth=2.2, zorder=2))
    bx.add_patch(Circle((0, 0), 1, fill=False, edgecolor=gray, linestyle="--",
                       linewidth=1.5, zorder=3))
    bx.axhline(0, color="#bdc7d0", linewidth=.8)
    bx.axvline(0, color="#bdc7d0", linewidth=.8)
    bx.annotate("", (2, 0), (0, 0), arrowprops={"arrowstyle": "<->", "color": navy}, zorder=4)
    bx.annotate("", (0, np.sqrt(2)), (0, 0), arrowprops={"arrowstyle": "<->", "color": navy}, zorder=4)
    bx.text(1.12, -.25, r"$2$", color=navy)
    bx.text(.12, .74, r"$\sqrt{2}$", color=navy)
    bx.text(-2.05, 1.75, r"$\dfrac{(v^1)^2}{4}+\dfrac{(v^2)^2}{2}=1$", fontsize=14)
    bx.text(.8, -1.87, "Euclidean unit circle: dashed", fontsize=10, ha="center", color=gray)
    bx.set_xlim(-2.45, 2.45)
    bx.set_ylim(-2.05, 2.15)
    bx.set_xticks([-2, -1, 0, 1, 2])
    bx.set_yticks([-1, 0, 1])
    bx.set_xlabel(r"$v^1$  (parallel to $z$)")
    bx.set_ylabel(r"$v^2$  (Hermitian-orthogonal to $z$)")
    fig.text(.055, .055, r"Sphere radius $1/2$; curvature $4$; total area $\pi$.", fontsize=11)
    fig.text(.55, .055, r"At $z=(1,0,\ldots,0)$, $n\geq2$; a real tangent slice.", fontsize=11)
    output = Path(__file__).with_name("kahler-geometry.png")
    fig.savefig(output, dpi=180, facecolor="white", metadata={"Title": "Exact projective metric sections"})
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
