"""Exact fractional-part disintegration diagram; original code and data CC0-1.0.

Run with Python and matplotlib. Outputs are written beside this script.
Mathematical source: OA-FLOW-L75, equations (E1)--(E10).
Font: DejaVu Sans; see FONT_LICENSE_DEJAVU.txt in this directory.
The display is an infinite fibre with a finite illustrated window, not a
finite approximation to a probability measure.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent
Y = Q(1, 4)
N = range(-2, 3)
a = {n: Q(1, 3 * 2 ** abs(n)) for n in N}
b = {n: Q(1, 2 * 3 ** abs(n)) for n in N}
tail_a = Q(1, 12)
tail_b = Q(1, 36)
assert sum(a.values()) + 2 * tail_a == 1
assert sum(b.values()) + 2 * tail_b == 1
for c in (Q(1, 2), Q(3, 2)):
    assert c * (1 / c) == 1
    for n in N:
        assert a[n] * (c * b[n]) / (c * a[n]) == b[n]
assert Q(1, 2) * Q(1, 2) + Q(1, 2) * Q(3, 2) == 1

data = {
    "license": "CC0-1.0",
    "proof_locator": "OA-FLOW-L75.md#oa-flow.kernel.example; E1-E10",
    "base_point": str(Y),
    "atoms": [{"n": n, "x": str(Y+n), "a_n": str(a[n]),
               "b_n": str(b[n]), "counting_mass": "1"} for n in N],
    "infinite_tail_masses": {
        "a_n_le_minus3": str(tail_a), "a_n_ge3": str(tail_a),
        "b_n_le_minus3": str(tail_b), "b_n_ge3": str(tail_b)},
    "base_change": [
        {"interval": "[0,1/2)", "density_c": "1/2", "conditional_mass": "2",
         "probability_base_mass": "1/4", "product": "1"},
        {"interval": "[1/2,1)", "density_c": "3/2", "conditional_mass": "2/3",
         "probability_base_mass": "3/4", "product": "1"}],
    "exact_checks": "All displayed rational identities asserted with fractions.Fraction."
}
(OUT / "fractional-part-exact-data.json").write_text(
    json.dumps(data, indent=2) + "\n", encoding="utf-8")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "mathtext.fontset": "dejavusans", "svg.fonttype": "path"})
fig = plt.figure(figsize=(15, 10), facecolor="#f7fafc")
ink, blue, orange, muted = "#182b3a", "#176b9d", "#b65b20", "#526677"
fig.text(.055, .965, "One fibre, two measures", fontsize=27, color=ink,
         weight="bold", va="top")
fig.text(.055, .885,
         r"Fractional part $p(x)=x-\lfloor x\rfloor$  |  $y=\frac{1}{4}$  |  $p^{-1}\{y\}=y+\mathbb{Z}$",
         fontsize=17, color=muted)

ax = fig.add_axes([.055, .405, .89, .455])
ax.set_xlim(-3.55, 3.55)
ax.set_ylim(-.73, 2.26)
ax.axis("off")

def qmath(q):
    if q.denominator == 1:
        return str(q.numerator)
    sign = "-" if q < 0 else ""
    return sign + r"\frac{" + str(abs(q.numerator)) + "}{" + str(q.denominator) + "}"

def line(y, color):
    ax.add_patch(FancyArrowPatch((-3.35, y), (3.35, y), arrowstyle="<->",
                                mutation_scale=15, color=color, linewidth=1.4))

ax.text(-3.4, 2.1, r"Probability $\kappa_y$: mass $a_n=2^{-|n|}/3$", color=blue,
        fontsize=17, weight="bold")
line(1.46, blue)
for n in N:
    ax.plot(n, 1.46, "o", ms=8 + 24*float(a[n]), color=blue, zorder=3)
    ax.text(n, 1.77, "$"+qmath(a[n])+"$", ha="center", color=blue, fontsize=19)
    ax.text(n, 1.13, "$"+qmath(Y+n)+"$", ha="center", color=ink, fontsize=16)
ax.text(-3.02, 1.79, "left tail\n" + r"$1/12$", ha="center", va="center",
        color=muted, fontsize=13)
ax.text(3.02, 1.79, "right tail\n" + r"$1/12$", ha="center", va="center",
        color=muted, fontsize=13)
ax.text(3.33, 1.10, "$x$", ha="center", color=ink)

for n in N:
    ax.annotate("", xy=(n, .63), xytext=(n, .96),
                arrowprops={"arrowstyle": "->", "color": muted, "lw": 1.1})
ax.text(2.80, .74, "divide by\n" + r"$w(y+n)=a_n$", ha="center", va="center",
        color=ink, fontsize=14,
        bbox={"boxstyle": "round,pad=.25", "facecolor": "#f7fafc", "edgecolor": "none"})

line(.16, orange)
for n in N:
    ax.plot(n, .16, "o", ms=11, color=orange, zorder=3)
    ax.text(n, .40, "$1$", ha="center", color=orange, fontsize=18)
    ax.text(n, -.18, "$"+qmath(Y+n)+"$", ha="center", color=ink, fontsize=16)
ax.text(-3.02, .45, "unit mass at\nevery translate", ha="center", va="center",
        color=muted, fontsize=12)
ax.text(3.33, -.18, "$x$", ha="center", color=ink)
ax.text(-3.4, -.57, r"Counting $\mu_y$: each atom has mass $1$; total mass is $\infty$",
        color=orange, fontsize=17, weight="bold")

fig.text(.055, .39, "A new normalization rescales the base and the conditional measure",
         fontsize=18, color=ink, weight="bold")
fig.text(.055, .35, r"$v(y+n)=c(y)b_n$,   $b_n=3^{-|n|}/2$,   $\sum_n b_n=1$",
         fontsize=17, color=muted)

dax = fig.add_axes([.083, .115, .36, .185])
dax.set_facecolor("#f7fafc")
dax.set_xlim(-.02, 1.05)
dax.set_ylim(0, 1.82)
dax.spines[["top", "right"]].set_visible(False)
dax.spines[["left", "bottom"]].set_color("#acb9c4")
dax.set_xticks([0, .5, 1], ["0", r"$1/2$", "1"])
dax.set_yticks([.5, 1.5], [r"$1/2$", r"$3/2$"])
dax.tick_params(length=0, colors=ink, pad=7)
dax.fill_between([0, .5], .5, color=blue, alpha=.13)
dax.fill_between([.5, 1], 1.5, color=blue, alpha=.13)
dax.plot([0, .5], [.5, .5], color=blue, lw=3)
dax.plot([.5, 1], [1.5, 1.5], color=blue, lw=3)
for x, y, closed in [(0,.5,True),(.5,.5,False),(.5,1.5,True),(1,1.5,False)]:
    dax.plot(x,y,"o",ms=7,markeredgecolor=blue,markerfacecolor=blue if closed else "#f7fafc",
             markeredgewidth=1.6,zorder=5)
dax.text(.25,.23,r"area $1/4$",ha="center",color=ink,fontsize=12)
dax.text(.75,.74,r"area $3/4$",ha="center",color=ink,fontsize=12)
dax.text(.02,1.7,r"base density $c(y)$",fontsize=13,color=blue)
dax.set_xlabel("base point $y$", color=ink, labelpad=8)

rax = fig.add_axes([.51, .092, .435, .218])
rax.axis("off")
rax.add_patch(FancyBboxPatch((0,0),1,1,boxstyle="round,pad=.012",fc="#eaf0f4",
                            ec="none",transform=rax.transAxes))
rax.text(.045,.84,r"$d\nu_v=c(y)\,dy$",fontsize=18,color=blue)
rax.text(.045,.61,r"$\kappa_y^v=\sum_n b_n\delta_{y+n}$",fontsize=17,color=blue)
rax.text(.045,.37,r"$\mu_y^v=c(y)^{-1}\sum_n\delta_{y+n}$",fontsize=17,color=orange)
rax.text(.045,.11,r"$\frac{1}{2}\cdot2=1$      and      $\frac{3}{2}\cdot\frac{2}{3}=1$",
         fontsize=20,color=ink)
fig.text(.055, .025, "Exact values, with infinite tails retained.  OA-FLOW L75 · equations (E1)–(E10)",
         fontsize=11, color=muted)
fig.savefig(OUT / "fractional-part-disintegration.png", dpi=180, facecolor=fig.get_facecolor())
fig.savefig(OUT / "fractional-part-disintegration.svg", facecolor=fig.get_facecolor())
plt.close(fig)
print(json.dumps({"outputs": ["fractional-part-disintegration.png",
                            "fractional-part-disintegration.svg",
                            "fractional-part-exact-data.json"],
                  "exact_rational_checks": "passed"}))
