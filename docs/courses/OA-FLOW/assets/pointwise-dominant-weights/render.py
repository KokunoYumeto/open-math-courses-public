"""Draw the exact selector coordinates and original-center support obstruction.

Original code and drawing: CC0-1.0. DejaVu font terms: FONT-LICENSE.txt.
Run with Python 3, NumPy and Matplotlib: python render.py
All coordinate constants are rational data, not fitted or simulated values.
"""

from fractions import Fraction
from pathlib import Path
import json
import math
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
S = DATA["selector"]
Q = lambda value: Fraction(value)
FLOAT = lambda value: float(Q(value))
BLUE, ORANGE, INK = "#176B89", "#AE4817", "#192D40"
TEAL, PALE, GREY = "#31785A", "#E8F1F4", "#657583"


def exact_checks():
    lo, hi = map(Q, S["K"])
    epsilon = Q(S["epsilon"])
    assert hi - lo == epsilon
    for k in range(-240, 241):
        r = Fraction(k, 120)
        n = 1 + math.floor(abs(r) / epsilon)
        d = r / n
        a = max(lo, lo + d)
        b = a - d
        assert abs(d) < epsilon
        assert lo <= a <= hi and lo <= b <= hi
        assert a - b == d and n * d == r
    r, d, n = Q(S["sample_global_r"]), Q(S["sample_delta"]), S["sample_n"]
    assert n == 1 + math.floor(abs(r) / epsilon)
    assert r == n * d
    assert Q(S["sample_a_delta"]) - Q(S["sample_b_delta"]) == d
    positions = list(map(Q, S["frequency_positions"]))
    assert positions == [j * d for j in range(n + 1)]
    assert DATA["support"]["psi_support"] == [1, 0]
    assert DATA["support"]["Phi_support"] == [1, 1]


exact_checks()
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "mathtext.fontset": "dejavusans", "svg.fonttype": "path",
    "svg.hashsalt": "OA-FLOW-DS-models-v1", "text.color": INK,
    "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.edgecolor": GREY, "savefig.facecolor": "white",
})
cfg = DATA["render"]
fig = plt.figure(figsize=(cfg["width_inches"], cfg["height_inches"]), facecolor="white")
fig.text(.055, .955, "Repair every frequency; preserve original central support", fontsize=21, weight="bold")
fig.text(.055, .922, "Exact translation model  ·  "+r"$Z_r=\lambda_r\otimes1$"+"  ·  "+r"$\sigma_t(Z_r)=e^{irt}Z_r$", fontsize=13)

# A: both selected parameters stay in the fixed good interval.
ax = fig.add_axes([.08, .56, .385, .27])
r = np.linspace(-.5, .5, 501)
a = np.maximum(.25, .25 + r)
b = a - r
ax.axhspan(.25, .75, color=PALE, zorder=0)
ax.plot(r, a, color=BLUE, linewidth=3, label=r"$a(r)$")
ax.plot(r, b, color=ORANGE, linewidth=3, label=r"$b(r)=a(r)-r$")
for endpoint in (-.5, .5):
    ax.axvline(endpoint, color=GREY, linestyle=":", linewidth=1)
ax.axvline(0, color="#C1CBD1", linewidth=.8)
sample_r, sample_a, sample_b = [FLOAT(S[k]) for k in ("sample_local_r", "sample_local_a", "sample_local_b")]
ax.scatter([sample_r, sample_r], [sample_a, sample_b], s=45, c=[BLUE, ORANGE], zorder=5)
ax.annotate("", xy=(sample_r, sample_a), xytext=(sample_r, sample_b),
            arrowprops={"arrowstyle": "<->", "color": INK, "lw": 1.6, "shrinkA": 7, "shrinkB": 7})
ax.text(sample_r-.018, (sample_a+sample_b)/2, r"$r=1/3$", ha="right", va="center", fontsize=12,
        bbox={"facecolor":"white", "edgecolor":"none", "pad":2})
ax.text(sample_r+.035, sample_a, r"$7/12$", fontsize=11, va="center", color=BLUE)
ax.text(sample_r+.035, sample_b+.024, r"$1/4$", fontsize=11, va="bottom", color=ORANGE)
ax.set_xlim(-.54, .54)
ax.set_ylim(.19, .80)
ax.set_xticks([-.5, 0, .5], [r"$-1/2$", r"$0$", r"$1/2$"])
ax.set_yticks([.25, .5, .75], [r"$1/4$", r"$1/2$", r"$3/4$"])
ax.set_xlabel(r"requested frequency $r$", labelpad=6)
ax.set_ylabel(r"good parameter $q\in K$", labelpad=10)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(.5, 1.22), fontsize=12)
fig.text(.055, .875, "A  Choose two good parameters", fontsize=15, weight="bold")
fig.text(.08, .494, r"$K=[1/4,3/4]\subset E=\mathbb{R}\setminus\{0\}$", fontsize=13)
fig.text(.08, .463, r"$Y(r)=X_0(a(r))X_0(b(r))^*=Z_r\quad(|r|<1/2)$", fontsize=12)
fig.text(.08, .438, "The bad value at 0 is never sampled.  DSM7–DSM10", fontsize=10.5, color=GREY)

# B: one exact global frequency obtained as a power of a local frequency.
fig.text(.54, .875, "B  Add the local frequency three times", fontsize=15, weight="bold")
fig.text(.54, .824, r"$r=7/6,\quad n=1+\lfloor2|r|\rfloor=3$", fontsize=14)
fig.text(.54, .784, r"$\delta=r/n=7/18<1/2$", fontsize=14)
fig.text(.54, .738, r"$a(\delta)=23/36,\quad b(\delta)=1/4$", fontsize=13)
freq = fig.add_axes([.54, .588, .395, .11])
freq.set_xlim(-.08, 1.24)
freq.set_ylim(-.33, .5)
freq.axis("off")
positions = [FLOAT(x) for x in S["frequency_positions"]]
freq.plot([0, positions[-1]], [0, 0], color="#C7D2D8", linewidth=1.2)
labels = [r"$0$", r"$7/18$", r"$7/9$", r"$7/6$"]
for p, label in zip(positions, labels):
    freq.scatter(p, 0, c=INK, s=23, zorder=3)
    freq.text(p, -.16, label, ha="center", va="top", fontsize=12)
for p, q in zip(positions, positions[1:]):
    freq.add_patch(FancyArrowPatch((p,.015), (q,.015), connectionstyle="arc3,rad=-.38",
        arrowstyle="-|>", mutation_scale=14, linewidth=2, color=TEAL, shrinkA=4, shrinkB=4))
    freq.text((p+q)/2, .245, r"$+7/18$", ha="center", fontsize=12, color=TEAL)
fig.text(.54, .545, r"$X(7/6)=(Z_{23/36}Z_{1/4}^*)^3=Z_{7/18}^{\,3}=Z_{7/6}$", fontsize=13)
fig.text(.54, .498, "The proof adds eigenfrequencies,", fontsize=12)
fig.text(.54, .469, "with no group law required for the selected field.", fontsize=12)
fig.text(.54, .438, "DSEL14–DSEL16; DSM11", fontsize=10.5, color=GREY)

# C: central supports in the original two-summand algebra, not a metric model.
fig.add_artist(plt.Line2D([.055,.945],[.403,.403], transform=fig.transFigure, color="#CED9DF", linewidth=1))
fig.text(.055, .365, "C  The original center prevents a missing summand from being filled", fontsize=15, weight="bold")
support = fig.add_axes([.07, .115, .42, .213])
support.set_xlim(-.42, 2.08)
support.set_ylim(-.05, 2.23)
support.axis("off")
support.text(.5, 2.06, r"$B_1$", ha="center", fontsize=14)
support.text(1.55, 2.06, r"$B_2$", ha="center", fontsize=14)
support.text(-.08, 1.47, r"$s(\psi)$", ha="right", va="center", fontsize=13)
support.text(-.08, .52, r"$s(\Phi)$", ha="right", va="center", fontsize=13)
for y, active in [(1.08, DATA["support"]["psi_support"]), (.13, DATA["support"]["Phi_support"])]:
    for j, value in enumerate(active):
        x = .05 + j*1.05
        support.add_patch(Rectangle((x,y), .90,.78, facecolor=BLUE if value else "white",
            edgecolor=INK, linewidth=1.2, hatch=None if value else "///"))
        support.text(x+.45,y+.39, str(value), color="white" if value else GREY, ha="center", va="center", fontsize=20, weight="bold")
support.plot([1.025,1.025], [.07,1.96], color=INK, linewidth=1.5)
fig.text(.55, .305, r"$\psi=\nu\oplus0,\qquad\Phi=\nu\oplus\nu$", fontsize=14)
fig.text(.55, .261, r"$a=(a_1,a_2),\quad a^*a=(1,0)\ \Longrightarrow\ a_2=0$", fontsize=13)
fig.text(.55, .217, r"$aa^*=(a_1a_1^*,0)\ne(1,1)$", fontsize=14, color=ORANGE)
fig.text(.55, .172, r"$z_M(s(\psi))=(1,0)\ne1$", fontsize=13)
fig.text(.55, .135, "Two central summands; no off-diagonal operators in M.", fontsize=11)
fig.text(.07, .085, "Filled cell: support equals 1 in that summand.  Hatched cell: support equals 0.  Cell area has no trace or dimension meaning.", fontsize=10.4, color=GREY)
fig.text(.07, .055, "Proofs: OA-FLOW-DS §3, §6, §8 (DSM7–DSM11, DSM16–DSM17).  Original diagram and exact data: CC0-1.0.", fontsize=10, color=GREY)
fig.text(.07, .030, "Context: M. Takesaki, Theory of Operator Algebras II, XII.4.18–4.20, pp. 417–418.  DejaVu font: accompanying font license.", fontsize=9.7, color=GREY)

fig.savefig(ROOT / "ds-models.svg", metadata={"Title": DATA["title"], "Description": DATA["human_source_context"], "Date": None})
fig.savefig(ROOT / "ds-models.png", dpi=cfg["dpi"], metadata={"Title": DATA["title"], "Description": DATA["human_source_context"]})
license_source = Path(matplotlib.get_data_path()) / "fonts" / "ttf" / "LICENSE_DEJAVU"
shutil.copyfile(license_source, ROOT / "FONT-LICENSE.txt")
plt.close(fig)
print(json.dumps({"outputs": ["ds-models.svg", "ds-models.png", "FONT-LICENSE.txt"], "exact_rational_checks": "passed", "size_pixels": [cfg["width_inches"]*cfg["dpi"], cfg["height_inches"]*cfg["dpi"]], "matplotlib": matplotlib.__version__}))
