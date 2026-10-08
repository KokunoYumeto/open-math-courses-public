"""Reproduce the exact Krieger-tower figure; see TERMS.md for dependencies."""
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

def tower():
    cfg = DATA["tower"]
    b = DATA["coordinates"]["b"]["value"]
    fig, axes = plt.subplots(1, 2, figsize=(12, 7.2), gridspec_kw={"width_ratios": [1, 1.12]})
    fig.subplots_adjust(left=.08, right=.96, top=.79, bottom=.30, wspace=.32)
    heading(fig, "An invariant probability can give an infinite next factor",
            "Exact immediate-stop model: a type III₀ center flow on the torus, followed by a type II∞ real crossing.")
    ax = axes[0]
    t = np.linspace(*cfg["normalized_time_interval"], cfg["samples"])
    x, y = t % 1, (b * t) % 1
    split = np.r_[False, (np.abs(np.diff(x)) > .5) | (np.abs(np.diff(y)) > .5)]
    x[split] = np.nan
    y[split] = np.nan
    ax.plot(x, y, color=BLUE, lw=1.8, alpha=.9)
    x0 = cfg["vertical_section_x"]
    ax.axvline(x0, color=GOLD, ls="--", lw=1.8)
    sy = np.array([b * (x0 + k) % 1 for k in cfg["section_integers"]])
    ax.scatter(np.full(len(sy), x0), sy, c=GOLD, s=32, zorder=4,
               edgecolors="#fbfcfe", linewidths=.6)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal")
    ax.set_xticks([0, .25, .5, 1], ["0", "1/4", "1/2", "1"])
    ax.set_yticks([0, .5, 1], ["0", "1/2", "1"])
    ax.set_xlabel("x = u / c  mod 1", fontproperties=REG)
    ax.set_ylabel("y = ω + b u / c  mod 1", fontproperties=REG)
    text(ax, 0, 1.075, "Sₛ(x,y) = (x+s/c, y+bs/c)", bold=True, size=11)
    ax = axes[1]
    r = np.linspace(0, 6 * math.pi, 151)
    ax.plot(r / math.pi, r / math.pi, color=TEAL, lw=3)
    ax.set_xlim(0, 6.3); ax.set_ylim(0, 6.8)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6], ["0", "π", "2π", "3π", "4π", "5π", "6π"])
    ax.set_yticks(range(7))
    ax.grid(alpha=.2)
    ax.set_xlabel("dual cutoff R", fontproperties=REG)
    ax.set_ylabel("A[−R,R](1), in units of 1", fontproperties=REG)
    text(ax, .1, 7.28, "Paired Haar: dt and dp / (2π)", bold=True, size=11)
    text(ax, 1, 5.7, "A[−R,R](1) = R / π", color=TEAL, size=13, bold=True)
    text(ax, 2.45, .62, "Tα(1) = ∞ · 1", size=13, bold=True)
    fig.text(.08, .205, "At x = 1/4:  y = b(1/4+k) mod 1,  k ∈ ℤ", fontproperties=REG, fontsize=10, color=GOLD)
    fig.text(.08, .16, "Orbit sections are countable, so every orbit is Haar-null; Haar probability is nevertheless invariant.",
             fontproperties=REG, fontsize=10, color=INK)
    fig.text(.08, .115, "The next factor is II∞ by KT26.  The constructed initial factor therefore has ν = 0.",
             fontproperties=BOLD, fontsize=11, color=INK)
    fig.text(.08, .065, "KT23–26, KT31. Torus curves show a finite orbit sample; the zero-measure claim and the infinite weight are proved.",
             fontproperties=REG, fontsize=9, color=INK)
    finish(fig, cfg["filename"])


if __name__ == "__main__":
    tower()
    print(json.dumps({"figure": DATA["tower"]["filename"], "matplotlib": matplotlib.__version__, "numpy": np.__version__}))
