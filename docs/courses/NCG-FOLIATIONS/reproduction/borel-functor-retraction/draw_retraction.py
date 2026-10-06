"""One-unit functor retraction obstruction. Original expression CC0-1.0."""
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
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ap = argparse.ArgumentParser()
ap.add_argument("--output-dir", type=Path, default=HERE)
out = ap.parse_args().output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
REG = FontProperties(fname=str(HERE / "fonts/DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts/DejaVuSans-Bold.ttf"))
plt.rcParams.update({"svg.fonttype": "path",
                     "svg.hashsalt": "borel-functor-retraction-20261006"})
INK, BLUE, RED, GREEN = "#243b53", "#2767a4", "#b73c4c", "#23765b"
fig = plt.figure(figsize=(16, 9.2), facecolor="white")
a = fig.add_axes([.04, .43, .92, .48])
a.set_xlim(0, 1)
a.set_ylim(0, 1)
a.axis("off")

def label(x, y, text, size=12, bold=False, color=INK):
    a.text(x, y, text, fontsize=size, fontproperties=BOLD if bold else REG,
           color=color, ha="center", va="center", linespacing=1.4)

for x, title, subtitle in [(.14, "1 = {e}", "source one-unit groupoid"),
                            (.50, "ℤ", "intermediate one-unit groupoid"),
                            (.86, "1 = {e}", "receiving one-unit groupoid")]:
    a.add_patch(FancyBboxPatch((x - .11, .62), .22, .24,
                              boxstyle="round,pad=.008,rounding_size=.018",
                              facecolor="#edf4fb", edgecolor=BLUE, linewidth=1.6))
    label(x, .775, title, 21, True)
    label(x, .666, subtitle, 9)
for start, end, title, subtitle, color in [
    (.26, .38, "i(e) = 0", "proper; f(h) = 1", GREEN),
    (.62, .74, "p(n) = e", "nonproper; ker p = ℤ", RED)]:
    a.add_patch(FancyArrowPatch((start, .74), (end, .74), arrowstyle="-|>",
                                mutation_scale=20, linewidth=2, color=color))
    label((start + end) / 2, .88, title, 12, True, color)
    label((start + end) / 2, .535, subtitle, 10, False, color)
label(.50, .975, "The arrow functors satisfy p ∘ i = Id₁.", 15, True)
label(.14, .38, "On 1:  Λ₁(ν_b) = b\nΛ₂(ν_b) = 2b", 16, True, BLUE)
label(.50, .38, "Both become Λ∞ on ℤ\nν₀ ↦ 0; every ν_b, b > 0 ↦ ∞", 14, True, GREEN)
label(.86, .38, "One input cannot return\nboth distinct source measures.", 13, True, RED)
for start, end in [(.25, .37), (.63, .75)]:
    a.add_patch(FancyArrowPatch((start, .38), (end, .38), arrowstyle="-|>",
                                mutation_scale=18, linewidth=2, color=INK))
label(.50, .17, "This compares the complete functionals, not only measure classes.", 13)
label(.50, .025, "Full labelled groupoids: the singleton coarse orbit sets do not erase isotropy.", 11)

b = fig.add_axes([.12, .105, .44, .255])
ns = list(range(9))
lines = {"c = 1": [2 * n + 1 for n in ns],
         "c = 2": [2 * (2 * n + 1) for n in ns]}
for title, ys, color in [("c = 1", lines["c = 1"], BLUE),
                          ("c = 2", lines["c = 2"], GREEN)]:
    b.plot(ns, ys, marker="o", color=color, linewidth=2)
    b.text(8.25, ys[-1], title, fontproperties=BOLD, color=color, fontsize=11,
           va="center")
b.set_xlim(-.15, 9.3)
b.set_ylim(0, 37)
b.set_xticks(ns)
b.set_yticks([0, 10, 20, 30])
b.grid(alpha=.25)
b.set_xlabel("Window radius N; f_N = 1 on {−N,…,N}", fontproperties=REG, fontsize=11)
b.set_ylabel("Exact integral c(2N+1), b = 1", fontproperties=REG, fontsize=11)
for t in list(b.get_xticklabels()) + list(b.get_yticklabels()):
    t.set_fontproperties(REG)
fig.text(.61, .357, "Both sequences are unbounded.", fontproperties=BOLD,
         fontsize=13, color=GREEN)
fig.text(.61, .267, "For p the action space is one point.\nCₚu = Σₙ∈ℤ u :  zero or infinity.\nThere is no normalized cutoff.",
         fontproperties=REG, fontsize=13, color=RED, linespacing=1.5)
fig.text(.61, .143, "Finite windows support the plotted mechanism.\nTheorem 5.34 proves the infinite claim.",
         fontproperties=REG, fontsize=11, color=INK, linespacing=1.4)
fig.text(.5, .975, "A proper image can lose information needed by a retraction",
         ha="center", va="top", fontproperties=BOLD, fontsize=19, color=INK)
fig.text(.5, .018, "Figure 5.34. Theorem 5.34, (5.34.4)–(5.34.8); Exercise 30. "
         "Abstract groupoids; no assertion of foliation realization.",
         ha="center", fontproperties=REG, fontsize=11, color=INK)
notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
description = "Original mathematical illustration CC0-1.0. Complete font notice:\n" + notice
png = out / "borel-functor-retraction.png"
svg = out / "borel-functor-retraction.svg"
fig.savefig(png, dpi=160, metadata={"Description": description,
                                  "Software": "Matplotlib " + matplotlib.__version__})
fig.savefig(svg, metadata={"Date": None, "Description": description})
plt.close(fig)
data = {"proof": "Theorem 5.34", "exercise": 30,
        "one_unit_groupoids": ["1", "Z", "1"], "modules": [1, 1, 1],
        "functors": {"i": "e -> 0", "p": "n -> e", "pi": "Id_1"},
        "inclusion_proper": True, "projection_proper": False,
        "zero_kernel_image": 0, "positive_kernel_image": "infinity",
        "subcutoff_plot": {"b": 1, "N": ns, "integrals": lines,
                            "windows_are_finite_samples_only": True},
        "font_notice_embedded": True, "matplotlib": matplotlib.__version__,
        "outputs": [{"path": p.name, "bytes": p.stat().st_size,
                     "sha256": hashlib.sha256(p.read_bytes()).hexdigest().upper()}
                    for p in [png, svg]]}
(out / "FIGURE-DATA.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
