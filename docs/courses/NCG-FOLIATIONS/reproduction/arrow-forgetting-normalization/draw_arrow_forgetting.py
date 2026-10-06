"""Exact arrow-forgetting normalization; original expression CC0-1.0."""
from pathlib import Path
import argparse
import hashlib
import json
import os

HERE = Path(__file__).resolve().parent
os.environ["MPLCONFIGDIR"] = str(HERE / "runtime-cache")
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle

ap = argparse.ArgumentParser()
ap.add_argument("--output-dir", type=Path, default=HERE)
out = ap.parse_args().output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
REG = FontProperties(fname=str(HERE / "fonts/DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts/DejaVuSans-Bold.ttf"))
plt.rcParams.update({"svg.fonttype": "path",
                     "svg.hashsalt": "arrow-forgetting-normalization-20261006"})
INK, BLUE, RED, GREEN = "#243b53", "#2767a4", "#b73c4c", "#23765b"
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.patch.set_facecolor("white")
for a in axes:
    a.set_xlim(0, 1)
    a.set_ylim(0, 1)
    a.axis("off")
def label(a, x, y, s, size=11, bold=False, color=INK, ha="center"):
    a.text(x, y, s, fontsize=size, fontproperties=BOLD if bold else REG,
           color=color, ha=ha, va="center", transform=a.transAxes,
           linespacing=1.35, zorder=10)
def arrow(a, p, q, curve=0, color=BLUE):
    a.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=17,
                               linewidth=2, color=color, transform=a.transAxes,
                               connectionstyle="arc3,rad=" + str(curve)))
a = axes[0]
label(a, .5, .96, "A. A coarse point does not count the arrow labels", 14, True)
label(a, .5, .86, "Pair groupoid on {a₁,a₂,a₃}, with isotropy C₂", 12)
nodes = [(.20, .52), (.78, .70), (.78, .34)]
for i, (x, y) in enumerate(nodes, 1):
    a.add_patch(Circle((x, y), .043, facecolor="#eaf2fb",
                      edgecolor=BLUE, linewidth=2, transform=a.transAxes))
    label(a, x, y, "a" + "₁₂₃"[i - 1], 14, True)
for end in nodes[1:]:
    arrow(a, (.245, .52), (end[0] - .05, end[1]), .16)
    arrow(a, (.245, .52), (end[0] - .05, end[1]), -.16)
label(a, .58, .74, "two arrows a₁ → a₂", 10, color=BLUE)
label(a, .58, .285, "two arrows a₁ → a₃", 10, color=BLUE)
arrow(a, (.16, .555), (.16, .48), 2.1)
arrow(a, (.18, .566), (.23, .566), -2.1)
label(a, .08, .55, "u", 11, color=BLUE)
label(a, .205, .70, "1ₐ₁\n(identity)", 9, color=BLUE)
label(a, .50, .795, "Every transporter has label 0 or label 1.", 10)
label(a, .20, .395, "t(y) = a₁\nf₀(a₁,y) = 1/2", 11, True, RED)
label(a, .5, .24, "At each aᵢ:   C_Y f₀(aᵢ,y) = 2 × (1/2) = 1", 12, True)
a.add_patch(Rectangle((.06, .07), .88, .105, facecolor="#edf7f1",
                      edgecolor=GREEN, transform=a.transAxes))
label(a, .5, .12, "Coarse mass = 1.     Full-arrow integral = 1/2.", 12, True, GREEN)
label(a, .5, .018, "Selected transporter slice only; all units have counting mass 1.", 9)

a = axes[1]
label(a, .5, .96, "B. The exact isotropy normalization", 14, True)
label(a, .5, .86, "One unit of mass 1; one-point presentation", 12)
xs = [.13, .30, .47, .64, .86]
ks = ["1", "2", "4", "8", "∞"]
vals = [1, .5, .25, .125, 0]
baseline, scale = .30, .39
for x, k, v in zip(xs, ks, vals):
    a.add_patch(Rectangle((x - .052, baseline), .104, scale,
                         facecolor="white", edgecolor="#98a7b6",
                         linestyle=":", transform=a.transAxes))
    if v:
        a.add_patch(Rectangle((x - .044, baseline), .088, scale * v,
                             facecolor=BLUE, edgecolor=BLUE,
                             transform=a.transAxes))
    else:
        a.plot([x], [baseline], marker="o", markersize=9,
               markerfacecolor="white", markeredgewidth=2, color=RED,
               transform=a.transAxes)
    label(a, x, baseline + scale * v + .045, "1" if k == "1" else
          ("0" if k == "∞" else "1/" + k), 12, True,
          RED if k == "∞" else BLUE)
    label(a, x, .25, "k = " + k, 11)
label(a, .5, .77, "Dotted boxes: coarse mass 1 for every k", 11)
label(a, .5, .18, "Finite k: proper forgetting image = 1/k", 12, True, BLUE)
label(a, .5, .085, "Infinite k: every subcutoff is zero.\nThe forgetting functor is not proper.", 11, True, RED)
label(a, .5, .018, "The zero endpoint is not a proper direct-image value.", 9)
fig.subplots_adjust(left=.02, right=.985, bottom=.10, top=.91, wspace=.15)
fig.text(.5, .985, "Forgetting isotropy: an identity orbit map can change the measure",
         ha="center", va="top", fontproperties=BOLD, fontsize=18, color=INK)
fig.text(.5, .045, "Figure 5.32. Theorem 5.32 and Corollary 5.33; Exercises 27–29. "
         "Finite and infinite isotropy are distinguished.",
         ha="center", fontproperties=REG, fontsize=11, color=INK)
notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
description = "Original mathematical illustration CC0-1.0. Complete font notice:\n" + notice
png, svg = out / "arrow-forgetting-normalization.png", out / "arrow-forgetting-normalization.svg"
fig.savefig(png, dpi=160, metadata={"Description": description,
                                  "Software": "Matplotlib " + matplotlib.__version__})
fig.savefig(svg, metadata={"Date": None, "Description": description})
plt.close(fig)
data = {"proof": ["Theorem 5.32", "Corollary 5.33"],
        "panel_A": {"units": 3, "isotropy_order": 2, "selected_unit": 1,
                    "displayed_transporter_count": 6, "each_cutoff_weight": "1/2",
                    "unit_masses": [1, 1, 1], "presentation_points": 1,
                    "coarse_mass": "1", "full_arrow_integral": "1/2",
                    "whole_groupoid_drawn": False,
                    "identity_isotropy_label_is_included": True},
        "panel_B": {"isotropy_orders": [1, 2, 4, 8, "infinite"],
                    "coarse_masses": ["1"] * 5,
                    "subcutoff_integrals": ["1", "1/2", "1/4", "1/8", "0"],
                    "proper_functor_images_available": [True, True, True, True, False]},
        "matplotlib": matplotlib.__version__, "font_notice_embedded": True,
        "outputs": [{"path": p.name, "bytes": p.stat().st_size,
                     "sha256": hashlib.sha256(p.read_bytes()).hexdigest().upper()}
                    for p in [png, svg]]}
(out / "FIGURE-DATA.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

