"""Reproduce the exact tensor-period figure; see TERMS.md for dependencies."""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import Circle, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--font-dir", type=Path, default=ROOT.parent / "typeiii-zero-decomposition")
FONT_DIR = parser.parse_args().font_dir
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
REG = FontProperties(fname=str(FONT_DIR / "DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(FONT_DIR / "DejaVuSans-Bold.ttf"))
fontManager.addfont(str(FONT_DIR / "DejaVuSans.ttf"))
fontManager.addfont(str(FONT_DIR / "DejaVuSans-Bold.ttf"))
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "svg.fonttype": "path", "svg.hashsalt": "oa-flow-after-lacunary-20261007",
    "axes.edgecolor": "#6e7b8b", "axes.labelcolor": "#243346",
    "xtick.color": "#4b596b", "ytick.color": "#4b596b",
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "#fbfcfe", "axes.facecolor": "#fbfcfe",
})
INK, BLUE, TEAL, GOLD, RED = "#243346", "#2563aa", "#008477", "#cb8d1e", "#b74b52"

def text(ax, x, y, s, size=11, bold=False, **kw):
    return ax.text(x, y, s, fontproperties=BOLD if bold else REG,
                   fontsize=size, color=kw.pop("color", INK), **kw)

def finish(fig, filename):
    for ax in fig.axes:
        for lab in ax.get_xticklabels() + ax.get_yticklabels():
            lab.set_fontproperties(REG)
            lab.set_fontsize(10)
    fig.savefig(ROOT / (filename + ".svg"),
                metadata={"Date": None, "Creator": "Original OA-FLOW mathematical figure; CC0"})
    fig.savefig(ROOT / (filename + ".png"), dpi=180,
                metadata={"Software": "Original OA-FLOW mathematical figure; CC0"})
    plt.close(fig)

def heading(fig, title, subtitle):
    fig.text(.055, .95, title, fontproperties=BOLD, fontsize=21, color=INK)
    fig.text(.055, .91, subtitle, fontproperties=REG, fontsize=11, color=INK)

def tensor():
    cfg = DATA["tensor"]
    fig = plt.figure(figsize=(12, 7.3))
    heading(fig, "Which Fourier modes survive the tensor product?",
            "P has type III₀, Q has type III₁/₄.  With c = log 2, the full product center has period c.")
    grid = fig.add_axes([.075, .32, .41, .46])
    for k in range(cfg["k_range"][0], cfg["k_range"][1] + 1):
        for m in range(cfg["m_range"][0], cfg["m_range"][1] + 1):
            good = k == 0
            grid.scatter([m], [k], s=75 if good else 34,
                         color=TEAL if good else "#c5ced8", zorder=3)
            if good:
                text(grid, m, -.30, str(2*m), size=9, ha="center", color=TEAL)
    grid.axhline(0, color=TEAL, alpha=.5, lw=1)
    grid.set_xlim(-3.6, 3.6); grid.set_ylim(-2.6, 2.6)
    grid.set_xticks(range(-3, 4)); grid.set_yticks(range(-2, 3))
    grid.grid(alpha=.15)
    grid.set_xlabel("integer m", fontproperties=REG)
    grid.set_ylabel("integer k", fontproperties=REG)
    text(grid, -3.6, 3.18, "n = 2(m + bk) ∈ ℤ", size=14, bold=True)
    text(grid, -3.6, 2.78, "b irrational  ⇒  k = 0,  n = 2m", size=11)
    fig.text(.075, .225, "Green labels: input circle degree n", fontproperties=REG, fontsize=10, color=TEAL)
    ax = fig.add_axes([.54, .29, .41, .49])
    ax.set_xlim(-2.2, 2.4); ax.set_ylim(-1.7, 1.9); ax.set_aspect("equal"); ax.axis("off")
    centers = [(-1.15, .30), (1.18, .30)]
    rr = .66
    for (xx, yy), col in zip(centers, [BLUE, TEAL]):
        ax.add_patch(Circle((xx, yy), rr, fill=False, color=col, lw=2))
        text(ax, xx, yy + 1.02, "input: period 2c" if col == BLUE else "output: period c",
             ha="center", bold=True, size=10, color=col)
    left, right = centers
    points = [(left[0]+rr,left[1]),(left[0]-rr,left[1])]
    for xy in points:
        ax.plot(*xy, marker="o", ms=6, color=GOLD)
    ax.plot(right[0]+rr,right[1], marker="o", ms=7, color=TEAL)
    text(ax, left[0]+rr, left[1]-.26, "q=0", ha="center", size=9)
    text(ax, left[0]-rr, left[1]-.26, "q=c", ha="center", size=9)
    text(ax, left[0], left[1]-.05, "z", ha="center", size=17, color=BLUE)
    text(ax, right[0], right[1]-.05, "z²", ha="center", size=17, color=TEAL)
    ax.add_patch(FancyArrowPatch((-.37,.72),(.36,.72), arrowstyle="-|>", mutation_scale=14,
                                color=INK, lw=1.5))
    text(ax, 0, .99, "square", ha="center", size=10)
    text(ax, 0, -.74, "z = exp(−iπq/c),   w = a z²", ha="center", size=10)
    text(ax, 0, -1.05, "at a = 1; other phases rotate the output", ha="center", size=9)
    text(ax, 0, -1.44, "Θₛ(w) = exp(2πis/c) w", ha="center", size=11, bold=True)
    fig.text(.075, .17, "H = 2ℤ.  Fejér sums recover the entire fixed center W*(w), and its spectral measure is Haar.",
             fontproperties=REG, fontsize=11, color=INK)
    fig.text(.075, .115, "Output subtype: exp(−c) = 1/2.  Using the same-time diagonal would double the speed.",
             fontproperties=BOLD, fontsize=11, color=INK)
    fig.text(.075, .065, "TP19, TP23–26, TP28–32. The grid is a finite window of the proved integer condition, not a test by rounding.",
             fontproperties=REG, fontsize=9, color=INK)
    finish(fig, cfg["filename"])


if __name__ == "__main__":
    tensor()
    print(json.dumps({"figure": DATA["tensor"]["filename"], "matplotlib": matplotlib.__version__, "numpy": np.__version__}))
