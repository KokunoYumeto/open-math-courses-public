"""Exact halfspace slice, two-tail mechanism, and full-sequence detector.

The triangle is a complex-time section of AM.18; tangential variables
are suppressed. The graph samples the stated exact rational function.
The central diagram records the separate complete proofs in AM.B.2–3.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path)
args = parser.parse_args()
out = args.output_dir.resolve() if args.output_dir else Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "mathtext.fontset": "dejavusans",
    "svg.hashsalt": "actual-halfspace-euler-evaluation-20261018"
})
bg, navy, blue, red = "#f9fbfd", "#173d56", "#1f6b91", "#a54835"
t = (F(3, 5), F(1, 10))
eps = F(1, 4)
vertices = [(F(0), F(-1, 20)), (F(3, 5), F(1, 10)), (F(0), F(1, 4))]
for a, b in vertices:
    assert 0 <= a <= t[0]
    assert abs(b - t[1]) <= eps * (t[0] - a)
assert abs(vertices[0][1] - t[1]) == eps * t[0]
assert abs(vertices[2][1] - t[1]) == eps * t[0]

fig = plt.figure(figsize=(16, 9), facecolor=bg)
fig.text(.035, .95, "Actual halfspace evaluation: proper geometry and two complete tails",
         fontsize=23, weight="bold", color=navy)
fig.text(.035, .90,
         r"$\mathcal{S}=\lim_D\,\mathcal{O}(D\cap\{\mathrm{Re}\,t<0\})/\mathcal{O}(D)$"
         "   ·   functions on the left, support on the right",
         fontsize=17, color=navy)

ax = fig.add_axes([.055, .295, .29, .485])
ax.set_aspect("equal")
ax.set_xlim(-.16, .76)
ax.set_ylim(-.20, .40)
ax.add_patch(Rectangle((0, -.22), .8, .66, facecolor="#e8e5d7",
                       edgecolor="none", alpha=.8))
ax.add_patch(Polygon([(float(a), float(b)) for a, b in vertices], closed=True,
                     facecolor="#b5dbed", edgecolor=blue, lw=2))
ax.scatter([float(a) for a, b in vertices], [float(b) for a, b in vertices],
           s=36, color=blue, zorder=5)
ax.scatter([float(t[0])], [float(t[1])], s=55, color=red, zorder=6)
ax.annotate(r"$t=3/5+i/10$", (.6, .1), xytext=(.34, .33),
            arrowprops={"arrowstyle": "->", "color": red}, color=red, fontsize=13)
ax.annotate(r"$i/4$", (0, .25), xytext=(-.12, .31),
            arrowprops={"arrowstyle": "->", "color": navy}, color=navy, fontsize=14)
ax.annotate(r"$-i/20$", (0, -.05), xytext=(.05, -.15),
            arrowprops={"arrowstyle": "->", "color": navy}, color=navy, fontsize=14)
ax.text(.40, -.09, r"$H=\{\mathrm{Re}\,s\geq0\}$", fontsize=13, color="#726b4d")
ax.axvline(0, color="#91876a", lw=1.4)
ax.axhline(0, color="#a6afb6", lw=.6)
ax.grid(alpha=.15)
ax.set_xlabel(r"$\mathrm{Re}\,s$")
ax.set_ylabel(r"$\mathrm{Im}\,s$")
ax.set_title("Closed proper fibre · AM.18", fontsize=16, color=navy, pad=14)
fig.text(.055, .229, r"$0\leq\mathrm{Re}\,s\leq3/5$", fontsize=15, color=navy)
fig.text(.055, .185, r"$|\mathrm{Im}\,s-1/10|\leq(3/5-\mathrm{Re}\,s)/4$",
         fontsize=14, color=navy)

center = fig.add_axes([.385, .20, .265, .60])
center.set_xlim(0, 1)
center.set_ylim(0, 1)
center.axis("off")
def box(y, title, text_lines, color):
    center.add_patch(FancyBboxPatch((.015, y), .97, .405, boxstyle="round,pad=.012",
                                    facecolor=color, edgecolor="#7290a5", lw=1.2))
    center.text(.055, y + .35, title, fontsize=15, weight="bold", color=navy, va="top")
    for offset, text, size in text_lines:
        center.text(.055, y + .35 - offset, text, fontsize=size, color=navy, va="top")
box(.545, "Positive infinite part · AM.B.2", [
    (.09, "Complex-diagonal holomorphic kernel", 12),
    (.17, "ordered Čech residue on each entry", 12),
    (.25, r"$T_+f=\sum_{j\geq0}r_j\partial_t^j f$", 17),
], "#eef4fb")
box(.06, "Negative entire tail · AM.B.3", [
    (.09, "One actual finite-order operator", 12),
    (.17, "complete anchored Volterra series", 12),
    (.25, r"$T_-f=\sum_{n\geq1}r_{-n}D_{t,a}^{-n}f$", 16),
], "#edf7f1")

ax = fig.add_axes([.715, .475, .25, .29])
ts = np.linspace(-1, -.05, 250)
ax.plot(ts, 1 / (1 - ts / 4), color=blue, lw=2.5)
for point, label, offset in [
    (-1, r"$U(-1)=4/5$", (8, 12)),
    (-.5, r"$U(-1/2)=8/9$", (-30, -28))
]:
    val = 1 / (1 - point / 4)
    ax.scatter([point], [val], s=35, color=red, zorder=4)
    ax.annotate(label, (point, val), xytext=offset, textcoords="offset points",
                color=red, fontsize=12)
ax.set_xlim(-1.05, .02)
ax.set_ylim(.75, 1.035)
ax.grid(alpha=.18)
ax.set_xlabel("Negative real t in the half-disc")
ax.set_ylabel(r"$U(t)$")
ax.set_title("Full-sequence detector · AM.C", fontsize=16, color=navy, pad=12)
fig.text(.70, .38, r"$r_j=1/(j!)^2,\quad r_{-n}=n!4^{-n}$", fontsize=15, color=navy)
fig.text(.70, .324, r"$R\log t=U(t)\log t+V_-(t)\quad(\mathrm{mod}\ \mathcal{O})$",
         fontsize=13, color=navy)
fig.text(.70, .267, r"$U(t)=1/(1-t/4)$", fontsize=18, color=navy)
fig.text(.70, .212, r"$\mathrm{jump}=2\pi i\,U(t)\neq0$  as a function",
         fontsize=16, color=navy)
fig.text(.035, .10,
         "The full-disc Taylor gauge is bounded by "
         r"$M_a(K|a|+r+|a|)^n/n!$; its factorial-weighted series converges · AM.23a–c.",
         fontsize=14, color=navy)
fig.text(.035, .047,
         "The jump obstructs extension of this representative. Its holomorphic quotient class is zero. "
         "Arbitrary constant Jordan blocks: AM.26–27.",
         fontsize=13, color=navy)
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
width, height = fig.canvas.get_width_height()
for text in list(fig.texts) + list(center.texts):
    bounds = text.get_window_extent(renderer)
    assert bounds.x0 >= 8 and bounds.x1 <= width - 8, (text.get_text(), tuple(bounds.extents))
    assert bounds.y0 >= 8 and bounds.y1 <= height - 8, (text.get_text(), tuple(bounds.extents))
fig.savefig(out / "euler-model-halfspace-and-detectors.png", dpi=150, facecolor=bg)
fig.savefig(out / "euler-model-halfspace-and-detectors.svg", metadata={"Date": None}, facecolor=bg)
plt.close(fig)
data = {
    "proof_locators": ["AM.18", "AM.B.2", "AM.B.3", "AM.23a–c", "AM.25", "AM.26–27"],
    "geometry": {
        "type": "complex-time section; tangential variables suppressed",
        "support": "Re s >= 0", "epsilon": str(eps),
        "output_t": [str(v) for v in t],
        "closed_triangle_vertices": [[str(a), str(b)] for a, b in vertices],
        "constraints": ["0 <= Re s <= 3/5", "|Im s-1/10| <= (3/5-Re s)/4"],
        "all_vertices_and_edges_included": True
    },
    "two_tails": {
        "positive": "ordinary holomorphic diagonal Cech residue; actual derived H-support comparison",
        "negative": "complete actual finite-order Volterra action; one factorial constant",
        "positive_distribution_limit_used": False
    },
    "detector": {
        "nonnegative": "r_j=1/(j!)^2", "negative": "r_-n=n!4^-n",
        "U": "1/(1-t/4)", "V_minus": "sum_{j>=1} (-1)^(j-1)/(j j! t^j)",
        "jump_as_function": "2 pi i U(t)",
        "jump_quotient_class": "zero, since U is holomorphic on the full small disc",
        "exact_marked_values": {"-1": "4/5", "-1/2": "8/9"},
        "curve": "250 samples of the exact rational function U on [-1,-1/20]"
    },
    "gauge": {"bound": "M_a (K |a|+r+|a|)^n / n!",
              "summability": "C0 (K |a|+r+|a|) < 1"},
    "generic_holonomic_classification_asserted": False
}
(out / "euler-halfspace-exact-data.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"outputs": 3, "vertices": data["geometry"]["closed_triangle_vertices"]}))
