"""Exact planar witnesses for WFC8-9 and WFC14; reproducible PNG/SVG sources."""
from pathlib import Path
import argparse, json, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Arc, Polygon
import numpy as np

OWN = Path(__file__).resolve().parent
BLUE, GREEN, ORANGE, INK = "#2369a2", "#187d58", "#bd671d", "#182d40"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15, "svg.hashsalt": "AN02-WFC049", "axes.spines.top": False, "axes.spines.right": False})

def export(fig, target, name):
    fig.savefig(target / (name + ".png"), dpi=150, facecolor="white", metadata={"Software": "AN02 WFC049 reproducible figure"})
    fig.savefig(target / (name + ".svg"), facecolor="white", metadata={"Date": None, "Creator": "AN02 WFC049 reproducible figure"})
    plt.close(fig)

def cones(target):
    fig = plt.figure(figsize=(12, 7.5), layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.25, 1])
    ax, notes = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    ax.set_aspect("equal")
    ax.add_patch(Wedge((0, 0), 4.05, -30, 30, color=BLUE, alpha=.12))
    ax.add_patch(Wedge((0, 0), 4.05, -15, 15, color=GREEN, alpha=.18))
    for angle in [-30, 30]:
        ax.plot([0, 4.05 * math.cos(math.radians(angle))], [0, 4.05 * math.sin(math.radians(angle))], "--", color=BLUE, lw=2)
    for angle in [-15, 15]:
        ax.plot([0, 4.05 * math.cos(math.radians(angle))], [0, 4.05 * math.sin(math.radians(angle))], color=GREEN, lw=2)
    ax.axhline(0, color="#bbc4ce", lw=1); ax.axvline(0, color="#bbc4ce", lw=1)
    ax.add_patch(Arc((0, 0), 2.3, 2.3, theta1=15, theta2=30, color=ORANGE, lw=3))
    ax.text(1.19, .57, r"gap $\pi/12$", color=ORANGE, fontsize=14)
    ax.scatter([3, 1], [0, 2], color=[GREEN, BLUE], s=65, zorder=5)
    ax.text(2.45, -.34, r"$\xi=(3,0)$", color=GREEN)
    ax.text(.52, 2.24, r"$\eta=(1,2)$", color=BLUE)
    ax.annotate("", xy=(3, 0), xytext=(1, 2), arrowprops={"arrowstyle": "-|>", "lw": 2.5, "color": ORANGE})
    ax.text(1.64, 1.23, r"$\xi-\eta=(2,-2)$", color=ORANGE, rotation=-45, fontsize=14)
    ax.text(3.48, 1.59, r"$+\pi/6$", color=BLUE, fontsize=13)
    ax.text(3.48, -.86, r"$-\pi/12$", color=GREEN, fontsize=13)
    ax.set_xlim(-.35, 4.65); ax.set_ylim(-2.35, 2.7)
    ax.set_xlabel("first frequency coordinate"); ax.set_ylabel("second frequency coordinate")
    ax.set_title("Two-dimensional frequency section", fontsize=17)
    notes.axis("off")
    blocks = [
        (.96, "Nested directions at one base point", INK, 17),
        (.83, "Blue: open good cone\n−π/6 < angle < π/6", BLUE, 16),
        (.66, "Green: closed smaller direction interval\n−π/12 ≤ angle ≤ π/12", GREEN, 15),
        (.48, "Minimum angular gap = π/12\nδ = 2 sin(π/24)\nc = sin(π/24)", ORANGE, 16),
        (.25, "WFC8–WFC9, all allowed directions:\n|ξ − η| ≥ c (|ξ| + |η|)", INK, 16),
        (.09, "Sample: 2√2 > c (3 + √5).\nThese are covectors, not physical supports.", INK, 14),
    ]
    for y, text, color, size in blocks:
        notes.text(0, y, text, transform=notes.transAxes, va="top", color=color, fontsize=size, linespacing=1.55)
    export(fig, target, "cones-and-frequency-separation")

def spatial(target):
    fig = plt.figure(figsize=(12, 7.5), layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1])
    ax, notes = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    ax.set_aspect("equal")
    ax.axhspan(-3, 3, color=BLUE, alpha=.09)
    ax.axvspan(-1, 1, color=GREEN, alpha=.14)
    xx = np.linspace(-2.1, 2.1, 401)
    ax.fill_between(xx, xx-1, xx+1, color=ORANGE, alpha=.14)
    ax.plot(xx, xx-1, "--", color=ORANGE, lw=2)
    ax.plot(xx, xx+1, "--", color=ORANGE, lw=2)
    ax.add_patch(Polygon([(-1, -2), (-1, 0), (1, 2), (1, 0)], facecolor=GREEN, edgecolor="none", alpha=.25))
    for y in [-3, 3]: ax.axhline(y, ls="--", color=BLUE, lw=2)
    for y in [-2, 2]: ax.axhline(y, ls=":", color=GREEN, lw=1.5)
    for x in [-1, 1]: ax.axvline(x, ls="--", color=GREEN, lw=2)
    ax.axhline(0, color="#bbc4ce", lw=1); ax.axvline(0, color="#bbc4ce", lw=1)
    ax.set_xlim(-2.1, 2.1); ax.set_ylim(-3.5, 3.5)
    ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks(range(-3, 4))
    ax.set_xlabel("output coordinate x"); ax.set_ylabel("source coordinate y")
    ax.set_title("One-dimensional spatial section", fontsize=17)
    notes.axis("off")
    blocks = [
        (.96, "Exact WFC14 support witness", INK, 17),
        (.85, "Section: x₀ = 0, ε = 1", INK, 16),
        (.73, "Green vertical strip: |x| < 1\nOrange diagonal band: |x − y| < 1\nBlue horizontal strip: χ(y) = 1 for |y| < 3", INK, 15),
        (.49, "Their dark intersection obeys\n|y| ≤ |x| + |x − y| < 2 < 3.", GREEN, 16),
        (.30, "Thus the discarded input (1 − χ)f\ncannot meet this convolution witness:\nE₀*f = E₀*(χf) on |x| < 1.", INK, 15),
        (.10, "Only support witnesses are drawn.\nNo values or complete support of f are plotted.\nThe general proof is the same triangle inequality.", INK, 13),
    ]
    for y, text, color, size in blocks:
        notes.text(0, y, text, transform=notes.transAxes, va="top", color=color, fontsize=size, linespacing=1.55)
    export(fig, target, "spatial-support-witness")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OWN / "figures")
    target = parser.parse_args().output.resolve()
    assert target.is_relative_to(OWN) and not target.exists()
    target.mkdir(parents=True)
    cones(target); spatial(target)
    spec = {"schema": "AN02-WFC049-exact-figure-geometry/v1", "frequency_section": {"outer_open_angle_radians": [-math.pi/6, math.pi/6], "inner_closed_direction_angles_radians": [-math.pi/12, math.pi/12], "minimum_angular_gap": math.pi/12, "unit_chord_delta": 2*math.sin(math.pi/24), "WFC8_constant_c": math.sin(math.pi/24), "sample_xi": [3, 0], "sample_eta": [1, 2], "sample_difference": [2, -2], "sample_actual_length": 2*math.sqrt(2)}, "spatial_section": {"dimension": 1, "x0": 0, "epsilon": 1, "output_absolute_bound": 1, "kernel_difference_absolute_bound": 1, "resulting_source_absolute_bound": 2, "cutoff_one_absolute_bound": 3, "intersection_vertices_closure": [[-1,-2],[-1,0],[1,2],[1,0]], "distribution_values_depicted": False}, "Blender_useful": False, "Blender_reason": "Exact planar frequency directions and a planar support witness; no three-dimensional object is asserted."}
    (target / "geometry.json").write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"figures": 2, "native_png_and_svg": 4, "geometry": str(target / "geometry.json")}))

if __name__ == "__main__": main()
