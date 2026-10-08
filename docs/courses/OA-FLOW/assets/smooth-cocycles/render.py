"""Reproduce the exact smooth-cocycle figure; see TERMS.md for dependencies."""
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

def eta(v):
    v = np.asarray(v, dtype=float)
    out = np.zeros_like(v)
    out[v >= .75] = 1
    mid = (v > .25) & (v < .75)
    a, b = v[mid] - .25, .75 - v[mid]
    logit = -1 / a + 1 / b
    out[mid] = 1 / (1 + np.exp(np.clip(-logit, -700, 700)))
    return out

def eta_prime(v):
    v = np.asarray(v, dtype=float)
    out = np.zeros_like(v)
    mid = (v > .25) & (v < .75)
    a, b = v[mid] - .25, .75 - v[mid]
    e = eta(v[mid])
    out[mid] = e * (1 - e) * (1 / a**2 + 1 / b**2)
    return out

def smooth():
    cfg = DATA["smooth"]
    fig, axes = plt.subplots(2, 1, figsize=(12, 7.6), sharex=True,
                             gridspec_kw={"height_ratios": [1.1, 1]})
    fig.subplots_adjust(left=.09, right=.96, top=.81, bottom=.19, hspace=.23)
    heading(fig, "A measurable return phase becomes a norm-smooth cocycle",
            "Exact flat interpolation on three consecutive unequal roofs; the complex path is exp(i Φ).")
    for j, roof in enumerate(cfg["roofs"]):
        start, length = roof["start"], roof["length"]
        q, phase0 = math.pi * roof["q_over_pi"], math.pi * roof["initial_phase_over_pi"]
        v = np.linspace(0, 1, cfg["samples_per_roof"])
        xx = start + length * v
        phase = (phase0 + q * eta(v)) / math.pi
        slope = q * eta_prime(v) / length / math.pi
        col = [GOLD, BLUE, TEAL][j]
        axes[0].plot(xx, phase, color=col, lw=2.8)
        axes[1].plot(xx, slope, color=col, lw=2.6)
        for ax in axes:
            ax.axvspan(start, start + length / 4, color=col, alpha=.065)
            ax.axvspan(start + 3 * length / 4, start + length, color=col, alpha=.065)
        text(axes[0], start + length / 2, .64,
             ["r = 5/4,  q = π/4", "r = 1,  q = π/2", "r = 3/2,  q = −π/3"][j],
             ha="center", size=10, color=col)
    for ax in axes:
        ax.grid(axis="y", alpha=.2)
        for cross in [-1.25, 0, 1, 2.5]:
            ax.axvline(cross, color="#93a0af", ls=":", lw=1)
        ax.set_xlim(-1.30, 2.55)
    axes[0].set_ylim(-.34, .74)
    axes[0].set_ylabel("phase Φ / π", fontproperties=REG)
    axes[1].set_ylabel("phase derivative Φ′ / π", fontproperties=REG)
    axes[1].set_xlabel("orbit coordinate v", fontproperties=REG)
    axes[1].set_xticks([-1.25, 0, 1, 2.5], ["−5/4", "0", "1", "5/2"])
    axes[1].axhline(0, color="#93a0af", lw=.8)
    text(axes[0], .06, -.18, "Every positive jet vanishes at a crossing", size=10)
    fig.text(.09, .115,
             "Flat endpoint neighborhoods glue all derivatives.  δ = 1 gives |p⁽ᵏ⁾| ≤ Bₖ δ⁻ᵏ.",
             fontproperties=BOLD, fontsize=11, color=INK)
    fig.text(.09, .077,
             "SMC15, SMC17–25: signed products, exact gauge cancellation, and the uniform difference-quotient bound.",
             fontproperties=REG, fontsize=10, color=INK)
    fig.text(.09, .041,
             "Shading marks constant neighborhoods. Curves are samples of the stated exact formula; Bₖ is a proved symbolic bound.",
             fontproperties=REG, fontsize=9, color=INK)
    finish(fig, cfg["filename"])


if __name__ == "__main__":
    smooth()
    print(json.dumps({"figure": DATA["smooth"]["filename"], "matplotlib": matplotlib.__version__, "numpy": np.__version__}))
