"""Original CC0 figure for Corollary 7.1 and Exercise 7.

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

COURSE = Path(__file__).resolve().parents[2]
FIGURES = COURSE / "figures"


def main():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "svg.hashsalt": "AN02-strict-support-annulus",
    })
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.4), layout="constrained")
    blue, orange, gray = "#d9edf5", "#d88a32", "#e2e4e8"
    gap = 9 / 256
    for ax, bounds in zip(axes, [(-1.08, 1.08, -1.08, 1.08), (-.64, .64, -.19, .085)]):
        x0, x1, y0, y1 = bounds
        z = np.linspace(x0, x1, 1601)
        surface = -(z ** 4)
        ax.fill_between(z, np.maximum(surface, y0), y1, color=blue, zorder=0)
        ax.fill_between(z, y0, np.maximum(surface, y0), color=gray, zorder=0)
        zz, ss = np.meshgrid(np.linspace(x0, x1, 1201), np.linspace(y0, y1, 1001))
        radius2 = zz ** 2 + ss ** 2
        possible = (radius2 >= .25) & (radius2 <= 1) & (ss <= -(zz ** 4))
        ax.contourf(zz, ss, possible.astype(float), levels=[.5, 1.5], colors=[orange], alpha=.78, zorder=1)
        angle = np.linspace(0, 2 * np.pi, 1601)
        for radius in [.5, 1]:
            ax.plot(radius * np.cos(angle), radius * np.sin(angle), color="#747a84", lw=1.1, ls=":", zorder=2)
        ax.plot(z, surface, color="#153e54", lw=2, zorder=3)
        ax.axhline(0, color="#27313b", lw=1.1, ls="--")
        ax.axhline(-gap, color="#a33e2d", lw=1.3, ls="-.")
        ax.scatter([0], [0], color="#a33e2d", s=30, zorder=5)
        ax.set(xlim=(x0, x1), ylim=(y0, y1), xlabel=r"$z$", ylabel=r"$s$")
        ax.grid(alpha=.13)
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
    axes[0].set_aspect("equal", adjustable="box")
    axes[0].set_title("Strict support with flat curvature")
    axes[0].text(.14, .66, "Known smooth side", color="#153e54")
    axes[0].annotate("Possible commutator singularities", xy=(-.1, -.8), xytext=(-1.02, -.98),
                     arrowprops={"arrowstyle": "->", "color": "#573812"}, fontsize=9.3, color="#573812")
    axes[0].annotate(r"$s=-z^4$", xy=(.83, -.83**4), xytext=(.56, -.82),
                     arrowprops={"arrowstyle": "->", "color": "#153e54"}, color="#153e54")
    axes[0].annotate("Contact point", xy=(0, 0), xytext=(-.78, .27),
                     arrowprops={"arrowstyle": "->", "color": "#a33e2d"}, color="#a33e2d")
    axes[1].set_title("Source hull below the contact point")
    axes[1].text(-.60, .049, r"Supporting plane $s=0$", fontsize=10)
    axes[1].text(-.60, -.029, r"Source bound $s=-9/256$", fontsize=10, color="#a33e2d")
    axes[1].text(-.38, -.145, r"$\chi=1$ in $B(0,1/2)$", fontsize=10, color="#27313b")
    axes[1].annotate("Possible source region", xy=(.58, -.17), xytext=(.02, -.177),
                     arrowprops={"arrowstyle": "->", "color": "#573812"}, fontsize=9.5, color="#573812")
    FIGURES.mkdir(exist_ok=True)
    stem = FIGURES / "strict-support-annulus"
    fig.savefig(stem.with_suffix(".png"), dpi=175, metadata={"Software": "Open mathematics courses"})
    fig.savefig(stem.with_suffix(".svg"), metadata={"Date": None, "Creator": "Open mathematics courses"})
    vector = stem.with_suffix(".svg")
    vector.write_bytes(("\n".join(line.rstrip() for line in vector.read_text(encoding="utf-8").splitlines()) + "\n").encode("utf-8"))
    plt.close(fig)


if __name__ == "__main__":
    main()
