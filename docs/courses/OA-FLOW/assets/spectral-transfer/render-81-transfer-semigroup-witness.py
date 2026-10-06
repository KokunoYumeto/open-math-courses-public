"""Reproduce Figure 81.1 from exact translation data."""
from pathlib import Path
import json
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "81-transfer-semigroup-witness-data.json").read_text(encoding="utf-8"))
assert data["schema"] == "oa-flow-figure81/v1"
e, q, moved = (Fraction(data[key]) for key in ("e", "q", "e_plus_q"))
assert e + q == moved and (e, q, moved) == (Fraction(1, 4), Fraction(-3, 5), Fraction(-7, 20))
assert data["support_f_schematic"][0] < float(e) < data["support_f_schematic"][1]
assert data["support_g_schematic"][0] < float(moved) < data["support_g_schematic"][1]
assert data["support_f_schematic"][0] > 0 and data["support_g_schematic"][1] < 0

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
fig, ax = plt.subplots(figsize=(14, 6), dpi=130)
fig.patch.set_facecolor("#fbfcfd")
ax.set_facecolor("#fbfcfd")
ax.set_xlim(-.8, 1.05)
ax.set_ylim(-.3, 4.55)
ax.axis("off")
ink, blue, green, orange = "#173447", "#1b7897", "#287d63", "#b66e2e"
ax.text(-.72, 4.1, "A translation outside the spectral semigroup", fontsize=22,
        color=ink, weight="bold")
ax.text(-.72, 3.55, "E = [0, +infinity)    S_E = [0, +infinity)",
        fontsize=17, color=green, weight="bold")
ax.plot([-.72, .98], [2.7, 2.7], color="#738d9b", linewidth=1.7)
ax.plot([0, .98], [2.7, 2.7], color=green, linewidth=9, solid_capstyle="butt")
ax.scatter(0, 2.7, s=150, color=green, zorder=4)
ax.text(0, 2.35, "0", ha="center", color=ink)

ax.plot(data["support_f_schematic"], [2.7, 2.7], color=blue,
        linewidth=17, alpha=.54, solid_capstyle="butt")
ax.plot(data["support_g_schematic"], [2.7, 2.7], color=orange,
        linewidth=17, alpha=.65, solid_capstyle="butt")
ax.scatter([float(e), float(moved)], [2.7, 2.7], s=200,
           color=[blue, orange], edgecolor="white", linewidth=2, zorder=5)
ax.text(float(e), 3.0, "e = 1/4  (inside E)", ha="center", color=blue,
        fontsize=14, weight="bold")
ax.text(float(moved), 3.0, "e+q = -7/20  (outside E)", ha="center",
        color=orange, fontsize=14, weight="bold")
ax.add_patch(FancyArrowPatch((float(e), 1.85), (float(moved), 1.85),
                             arrowstyle="-|>", mutation_scale=20,
                             linewidth=2.5, color="#a14d55"))
ax.text(float((e + moved) / 2), 1.48, "q = -3/5", ha="center",
        color="#a14d55", fontsize=16, weight="bold")
ax.text(-.72, .72, "Local f near e and g near e+q give", color=ink, fontsize=15)
ax.text(-.72, .31, "h(q) = integral g(r) f(r-q) dr > 0.",
        color=green, fontsize=16, weight="bold")
fig.tight_layout(pad=2)
fig.savefig(HERE / "81-transfer-semigroup-witness.png", dpi=130,
            facecolor=fig.get_facecolor(), metadata={"Software": "OA-FLOW Figure 81.1"})
plt.close(fig)
