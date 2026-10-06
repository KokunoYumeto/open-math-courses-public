"""Reproduce the exact finite action schematic in NATIVE-INSERTION.md, Figure 5.1.

This is a discrete illustration, not a drawing of an actual foliation chart.
No TeX executable, AI image generator, or network request is used.
"""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent
SOURCE_CLASSES = (("A", ("a_0", "a_1", "a_2")),
                  ("C", ("c_0", "c_1")))
TARGET_CLASS = ("b_0", "b_1")
LIFT = {"a_0": "b_0", "a_1": "b_1", "a_2": "b_0",
        "c_0": "b_1", "c_1": "b_0"}
CUTOFF = {"a_0": Fraction(1, 2), "a_1": Fraction(1, 3),
          "a_2": Fraction(1, 6), "c_0": Fraction(1, 4),
          "c_1": Fraction(3, 4)}
ROW_Y = {"a_0": 6.4, "a_1": 5.35, "a_2": 4.3,
         "c_0": 2.4, "c_1": 1.35}
COL_X = {"b_0": 3.0, "b_1": 6.35}
COLORS = {"A": "#286a8f", "C": "#925329"}

# The numerical assertions in the illustration are exact rational checks.
for class_name, members in SOURCE_CLASSES:
    assert sum((CUTOFF[a] for a in members), Fraction(0)) == 1
    assert all(LIFT[a] in TARGET_CLASS for a in members)
    assert all(0 < CUTOFF[a] <= 1 for a in members)

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans"})
fig, axes = plt.subplots(1, 3, figsize=(16.8, 8.0),
                         gridspec_kw={"width_ratios": [1.0, 1.12, 1.05]})
fig.patch.set_facecolor("#ffffff")
for ax in axes:
    ax.set(xlim=(0, 9), ylim=(0, 8.3))
    ax.axis("off")

def arrow(ax, start, end, color="#7a8790", style="->", lw=1.6, alpha=1.0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=13, linewidth=lw,
                                color=color, alpha=alpha,
                                shrinkA=7, shrinkB=7))

def group_box(ax, x, y, width, height, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                               boxstyle="round,pad=0.12,rounding_size=0.14",
                               facecolor=color, edgecolor=color,
                               linewidth=1.0, alpha=0.065))

def dot(ax, x, y, color, size=60):
    ax.scatter([x], [y], s=size, color=color, zorder=5)

ax = axes[0]
ax.text(4.5, 8.0, "1. A Borel lift selects one point", ha="center",
        fontsize=14, fontweight="bold")
ax.text(1.55, 7.5, "$N_1$", ha="center", fontsize=16)
ax.text(7.2, 7.5, "$N_2$", ha="center", fontsize=16)
group_box(ax, 0.65, 3.82, 2.0, 3.04, COLORS["A"])
group_box(ax, 0.65, 0.88, 2.0, 1.94, COLORS["C"])
group_box(ax, 6.25, 2.7, 1.8, 3.3, "#5d6870")
target_y = {"b_0": 5.3, "b_1": 3.25}
for class_name, members in SOURCE_CLASSES:
    color = COLORS[class_name]
    for a in members:
        y = ROW_Y[a]
        dot(ax, 1.6, y, color)
        ax.text(1.12, y, f"${a}$", ha="right", va="center")
        arrow(ax, (1.75, y), (7.0, target_y[LIFT[a]]), color=color,
              lw=1.25, alpha=0.63)
for b in TARGET_CLASS:
    dot(ax, 7.0, target_y[b], "#424e56", 70)
    ax.text(7.35, target_y[b], f"${b}$", va="center")
ax.text(2.28, 6.48, "$A$", color=COLORS["A"], fontsize=14)
ax.text(2.28, 2.47, "$C$", color=COLORS["C"], fontsize=14)
ax.text(4.1, 4.0, "$F$", fontsize=16,
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
ax.text(4.5, 0.15, "$q_2F=hq_1$\nBoth source classes map to one target class.",
        ha="center", va="bottom", fontsize=11)

ax = axes[1]
ax.text(4.5, 8.0, "2. The action retains every target point", ha="center",
        fontsize=14, fontweight="bold")
ax.text(4.5, 7.52, r"$X_F\simeq R_h=\{(a,b):b\,E_2\,F(a)\}$", ha="center")
for b in TARGET_CLASS:
    ax.text(COL_X[b], 7.05, f"${b}$", ha="center", fontsize=14)
group_box(ax, 2.25, 3.82, 5.45, 3.02, COLORS["A"])
group_box(ax, 2.25, 0.88, 5.45, 1.94, COLORS["C"])
for class_name, members in SOURCE_CLASSES:
    color = COLORS[class_name]
    for a in members:
        y = ROW_Y[a]
        ax.text(1.65, y, f"${a}$", ha="right", va="center")
        arrow(ax, (COL_X["b_0"], y), (COL_X["b_1"], y),
              color="#acb5ba", style="<->", lw=0.9, alpha=0.7)
        for b in TARGET_CLASS:
            x = COL_X[b]
            dot(ax, x, y, color)
            val = CUTOFF[a]
            ax.text(x + 0.25, y + 0.12,
                    f"$g={val.numerator}/{val.denominator}$", fontsize=10,
                    va="bottom", color=color,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.5})
    for b in TARGET_CLASS:
        for a, a_next in zip(members, members[1:]):
            arrow(ax, (COL_X[b], ROW_Y[a]), (COL_X[b], ROW_Y[a_next]),
                  color=color, style="<->", lw=1.7)
ax.text(8.05, 5.35, "source\naction", ha="center", va="center", fontsize=10,
        color=COLORS["A"])
ax.text(8.05, 1.88, "source\naction", ha="center", va="center", fontsize=10,
        color=COLORS["C"])
ax.text(4.68, 3.35, "right target action changes $b$", ha="center", fontsize=10,
        color="#646e75")
ax.text(4.5, 0.15, "Source action: $(a',a)(a,b)=(a',b)$\n"
        "Each vertical source orbit has cutoff sum 1.",
        ha="center", va="bottom", fontsize=11)

ax = axes[2]
ax.text(4.5, 8.0, "3. The quotient is the pullback", ha="center",
        fontsize=14, fontweight="bold")
ax.text(4.5, 7.5, r"$Z=R_h/{\sim}\simeq h^*N_2$", ha="center", fontsize=14)
for class_name, ypos in [("A", 5.35), ("C", 2.65)]:
    color = COLORS[class_name]
    group_box(ax, 1.1, ypos - 0.75, 6.7, 1.55, color)
    for b in TARGET_CLASS:
        x = COL_X[b]
        dot(ax, x, ypos, color, 105)
        ax.text(x, ypos - 0.38, f"$(q_{class_name},{b})$", ha="center", fontsize=12)
    ax.text(4.45, ypos + 0.53, f"source leaf $q_{class_name}$", ha="center",
            fontsize=11, color=color)
ax.text(4.5, 0.58, r"$r(q,b_j)=q,\qquad\pi(q,b_j)=b_j$" "\n"
        "One point per vertical source orbit.", ha="center", fontsize=11)

fig.suptitle("Properness is the existence of a Borel normalized orbit cutoff",
             y=0.985, fontsize=18, fontweight="bold", color="#1f2e38")
fig.text(0.5, 0.047,
         "Finite schematic only: two source classes and one target class. "
         "General proof: Theorems 5.16–5.17; equations 5.15.2–5.17.12.",
         ha="center", fontsize=11, color="#394a55")
fig.subplots_adjust(left=0.015, right=0.99, top=0.90, bottom=0.10, wspace=0.04)
fig.savefig(OUT / "borel-proper-bridge.png", dpi=170, facecolor="white",
            metadata={"Title": "Principal action, orbit cutoff, and presentation pullback",
                      "Author": "GPT-6.1 Sol (OpenAI)",
                      "Description": "Exact finite schematic accompanying an original mathematical proof."})
fig.savefig(OUT / "borel-proper-bridge.svg", facecolor="white",
            metadata={"Title": "Principal action, orbit cutoff, and presentation pullback",
                      "Creator": "GPT-6.1 Sol (OpenAI)",
                      "Description": "Exact finite schematic accompanying an original mathematical proof."})
plt.close(fig)
print("Created PNG and SVG; exact cutoff sums checked for both classes.")
