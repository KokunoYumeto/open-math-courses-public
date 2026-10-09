"""CC0 1.0. Exact illustrations for PEE6, PEE10 and PEE12.

No source figure is reused. Curves use the stated explicit formulas.
The plotted line example is an illustration, not the general constructed f.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

HERE = Path(__file__).resolve().parent

matplotlib.rcParams['svg.hashsalt'] = 'SH02-PEE-20261008'

def render(portrait):
    plt.rcParams.update({'font.size': 15 if portrait else 11, 'axes.titlesize': 17 if portrait else 13, 'figure.dpi': 180})
    fig, axes = plt.subplots(3, 1, figsize=(6.4, 16)) if portrait else plt.subplots(1, 3, figsize=(15, 4.8))
    if portrait:
        fig.subplots_adjust(left=.17, right=.96, top=.91, bottom=.07, hspace=.62)
        fig.suptitle('Proper embedding: avoid zeros,\nprevent escape, preserve compact control', fontsize=17, y=.98)
    else:
        fig.subplots_adjust(left=.055, right=.98, top=.79, bottom=.24, wspace=.32)
        fig.suptitle('Proper embedding: avoid zeros, prevent escape, preserve compact fiber locations', fontsize=16, y=.96)
    # PEE6: exact parameter dimension inequality, shown for n=1, q=3, L=2.
    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")
    ax.set_title("1. Finite parameter avoidance\nPEE5–PEE9")
    ax.add_patch(Rectangle((.4, 4.65), 9.2, 1.8, fill=False, edgecolor="#2968a2", linewidth=2))
    ax.text(5, 5.75, r"Parameter space: $\mathbb{R}^{Lq}=\mathbb{R}^6$", ha="center")
    ax.text(5, 5.12, r"Test dimensions: pairs $d=2$, tangents $d=1$", ha="center", fontsize=(15 if portrait else 10))
    ax.annotate("", xy=(5, 3.8), xytext=(5, 4.5), arrowprops={"arrowstyle": "->", "lw": 2})
    ax.add_patch(Rectangle((.4, 1.6), 9.2, 2.1, facecolor="#e8f1f8", edgecolor="#2968a2"))
    ax.text(5, 3.05, r"Solve one vector coefficient block $a_\ell$", ha="center")
    ax.text(5, 2.42, r"Source dimension: $d+(L-1)q$", ha="center", fontsize=(15 if portrait else 10))
    ax.text(5, 1.91, r"Pairs: $5<6$; tangents: $4<6$", ha="center")
    ax.text(5, .6, "Countable box-null images cannot fill\nany parameter ball." if portrait else "Countable box-null images cannot fill any parameter ball.",
            ha="center", va="center", fontsize=(15 if portrait else 10), wrap=True)

    # Exact one-dimensional example: f(t) bounded, rho(t)=t^2 proper,
    # e(t)=(f1(t),0,0,t^2) in R^4; panel is exact coordinate projection.
    ax = axes[1]
    t = np.linspace(-4, 4, 1200)
    u = t / np.sqrt(1+t*t)
    ax.plot(u, t*t, color="#2968a2", lw=2.4)
    ax.axhline(4, color="#bb5b1d", ls="--")
    ax.fill_between(np.linspace(-1, 1, 100), 0, 4, color="#bb5b1d", alpha=.08)
    markers = np.array([-2, -1, 0, 1, 2])
    ax.scatter(markers/np.sqrt(1+markers**2), markers**2, color="#bb5b1d", zorder=4)
    ax.set_xlim(-1.05, 1.05); ax.set_ylim(-.25, 16.7)
    ax.set_xlabel(r"$f_1(t)=t/\sqrt{1+t^2}$")
    ax.set_ylabel(r"$\rho(t)=t^2$")
    ax.set_title("2. Appending a proper coordinate\nPEE10")
    ax.text(.0, 11, r"$e(t)=(f_1(t),0,0,t^2)\in\mathbb{R}^4$",
            ha="center", fontsize=(15 if portrait else 10))
    ax.text(.0, 6.2, r"$\rho^{-1}([0,4])=[-2,2]$", ha="center",
            color="#8a4217")
    ax.grid(alpha=.18)

    # Exact compact control in B^2 for L=closed disk radius 1/2.
    ax = axes[2]
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#555", linewidth=2))
    ax.add_patch(Circle((0, 0), .5, facecolor="#e3f0e2", edgecolor="#387335", linewidth=2))
    ax.plot([0, .5], [0, 0], color="#387335", lw=2)
    ax.text(.18, .08, r"$r=1/2$", fontsize=(15 if portrait else 10), color="#2d642a")
    ax.scatter([.98, .99], [.12, .06], color="#bb5b1d", s=22)
    ax.annotate("Boundary escape forbidden", xy=(.99, .06), xytext=(0, -1.25),
                ha="center", fontsize=(15 if portrait else 10), arrowprops={"arrowstyle": "->", "color": "#bb5b1d"})
    ax.text(0, .7, r"$S^1$", ha="center")
    ax.text(0, -.25, r"$L_B=\overline{B}_{1/2}(0)$", ha="center", fontsize=(15 if portrait else 10))
    ax.text(0, 1.3, r"$(di)^t(\xi,\zeta)=(\xi,(de)^t\zeta)$", ha="center", fontsize=(15 if portrait else 10))
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.5, 1.65)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("3. AE50 retains every fiber covector\nPEE12")


    caption = ('Exact examples and dimension counts.\nFinite plotting window |t| ≤ 4.\nGeneral proof: PEE5–PEE12.' if portrait else 'Exact examples and dimension counts; finite plotting window |t| ≤ 4. General proof: PEE5–PEE12. No sampled curve is used as proof.')
    fig.text(.5, .015 if portrait else .045, caption, ha='center', fontsize=14 if portrait else 10)
    stem = 'proper_embedding_mechanism_mobile' if portrait else 'proper_embedding_mechanism'
    fig.savefig(HERE / (stem + '.png'))
    fig.savefig(HERE / (stem + '.svg'), metadata={'Date': '2026-10-08T00:00:00Z'})
    plt.close(fig)

render(False)
render(True)
