"""Render the exact induced-corner diagram, using only its local data and fonts.

Run: python render.py
Outputs: induced-corners.svg and induced-corners.png in this directory.
All geometry is independently specified here; no source-page image is loaded.
"""
from pathlib import Path
import json
import argparse
import hashlib
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--shared-font-dir', type=Path, default=ROOT.parent / 'typeiii-zero-decomposition')
args = parser.parse_args()
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
for name in ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf",
             "DejaVuSansDisplay.ttf", "STIXNonUniIta.ttf", "cmsy10.ttf"):
    fm.fontManager.addfont(str((args.shared_font_dir if name in {'DejaVuSans.ttf', 'DejaVuSans-Bold.ttf'} else ROOT) / name))

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "mathtext.fontset": "dejavusans", "axes.unicode_minus": True,
    "svg.fonttype": "path", "svg.hashsalt": "induced-central-corners-20261007",
    "figure.facecolor": "#f6f8fb", "savefig.facecolor": "#f6f8fb",
})
NAVY = "#203348"
BLUE = "#2466a5"
ORANGE = "#bb5b14"
TEAL = "#167a67"
MUTED = "#617082"
PALE = "#e6eef7"
LINE = "#bccbdc"

h = DATA["hit_sample"]
assert h["R2"] == h["R1"] - h["a"] + h["a_next"]
assert h["R2"] == h["next_pair"][1] - h["first_pair"][1]
for x, y in h["displayed_pairs"]:
    right = min(t for t in h["first_section"] if t > x)
    assert x <= y < right
    assert y == min(t for t in h["second_section"] if x <= t < right)
assert DATA["coincident_sample"]["a"] == DATA["coincident_sample"]["b"] == 0
d = DATA["deck_square"]
assert d["source_top"][0] - d["top_displacement"] == d["target_top"][0]
assert d["source_top"][0] - d["left_roof"] == d["source_bottom"][0]
assert d["target_top"][0] - d["right_roof"] == d["target_bottom"][0]
assert d["source_bottom"][0] - d["bottom_displacement"] == d["target_bottom"][0]
for a in [0, h["a"], h["a_next"], -2, 17]:
    for s in [-5, 0, 9]:
        assert (s - a) + a == s

fig = plt.figure(figsize=(15.2, 12.2), dpi=180)
fig.text(.055, .965, "Return corners and the exact section-pairing maps",
         fontsize=23, weight="bold", color=NAVY, va="top")
fig.text(.055, .925,
         "Two partitions make the return unitary; paired hits determine the roof difference.",
         fontsize=13, color=MUTED, va="top")

def arrow(ax, start, end, color=BLUE, style="-|>", scale=15,
          width=1.7, connection="arc3,rad=0", **kw):
    a = FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=scale,
                        linewidth=width, color=color, connectionstyle=connection,
                        shrinkA=0, shrinkB=0, **kw)
    ax.add_patch(a)
    return a

# A: symbolic central bands. Their drawing widths are deliberately not weights.
ax = fig.add_axes([.055, .605, .41, .26])
ax.set_xlim(-.45, 6.8); ax.set_ylim(-.85, 3.45); ax.axis("off")
ax.text(0, 3.27, "A  Two orthogonal central partitions",
        fontsize=14, weight="bold", color=NAVY)
xs = [0, 1.7, 3.4, 5.1]
src = [r"$e_1$", r"$e_2$", r"$e_3$", r"$\cdots$"]
dst = [r"$\alpha(e_1)$", r"$\alpha^2(e_2)$",
       r"$\alpha^3(e_3)$", r"$\cdots$"]
maps = [r"$u e_1$", r"$u^2 e_2$", r"$u^3 e_3$", r"$u^n e_n$"]
for x, a, b, m in zip(xs, src, dst, maps):
    for y, label in [(2.1, a), (.1, b)]:
        ax.add_patch(Rectangle((x, y), 1.27, .60,
                               facecolor=PALE, edgecolor=BLUE, linewidth=1.3))
        ax.text(x+.635, y+.30, label, ha="center", va="center",
                color=NAVY, fontsize=13)
    arrow(ax, (x+.635, 2.03), (x+.635, .78), color=ORANGE)
    ax.text(x+.78, 1.42, m, color=ORANGE, fontsize=11, ha="left",
            bbox=dict(facecolor="#f6f8fb", edgecolor="none", pad=.6))
ax.text(0, -.34, r"$e=\sum_{n\geq1}e_n=\sum_{n\geq1}\alpha^n(e_n)$",
        fontsize=14, color=NAVY)
ax.text(0, -.77, "Band widths carry no trace or probability.  [IC7–12]",
        fontsize=10.5, color=MUTED)

# B: exact horizontal times. All arrows remain in a finite window.
ax = fig.add_axes([.525, .585, .425, .285])
ax.set_xlim(-1.25, 11.3); ax.set_ylim(-.2, 4.8); ax.axis("off")
ax.text(-1.05, 4.47, "B  Pair the first hit in each occupied interval",
        fontsize=14, weight="bold", color=NAVY)
for y, title in [(3.25, r"$\Omega_1$"), (2.0, r"$\Omega_2$")]:
    arrow(ax, (-.45, y), (10.7, y), color=LINE, width=1.2, scale=9)
    ax.text(-1.0, y, title, ha="center", va="center", color=NAVY, fontsize=13)
for x in [0, 4, 8]:
    ax.scatter([x], [3.25], s=49, color=BLUE, zorder=4)
    ax.text(x, 3.01, str(x), ha="center", va="top", color=BLUE)
for y in [1, 7, 10]:
    ax.scatter([y], [2.0], s=49, color=TEAL, zorder=4)
    ax.text(y, 1.77, str(y), ha="center", va="top", color=TEAL)
for (x, y), label in zip(h["displayed_pairs"], [r"$a=1$", r"$a'=3$", ""]):
    arrow(ax, (x, 3.13), (y, 2.13), color=ORANGE,
          width=1.8 if label else 1.0, scale=12)
    if label:
        ax.text((x+y)/2+.08, 2.66, label, fontsize=12, color=ORANGE,
                bbox=dict(facecolor="#f6f8fb", edgecolor="none", pad=.5))
arrow(ax, (0, 3.8), (4, 3.8), style="<->", scale=10)
ax.text(2, 3.95, r"$R_1=4$", color=BLUE, ha="center", fontsize=12)
arrow(ax, (1, 1.24), (7, 1.24), color=TEAL, style="<->", scale=10)
ax.text(4, .96, r"$R_2=6=4-1+3$", color=TEAL, ha="center", fontsize=12)
ax.text(-1.05, .39, "Coincident hits:", color=NAVY, fontsize=10.5)
for x in [3.4, 6.3, 9.2]:
    ax.scatter([x], [.38], s=76, facecolors="none", edgecolors=BLUE, linewidth=1.8)
    ax.scatter([x], [.38], s=16, color=TEAL, zorder=4)
ax.text(6.3, .02, r"$a=b=0,\quad W=\mathrm{id}$",
        ha="center", color=TEAL, fontsize=11)
ax.text(-1.05, -.18, "Finite orbit windows; no periodic closure.  [IC41–46]",
        color=MUTED, fontsize=10.5)

# C: commuting point square for the unsheared full product map.
ax = fig.add_axes([.055, .19, .895, .325])
ax.set_xlim(0, 13.2); ax.set_ylim(-.85, 4.4); ax.axis("off")
ax.text(0, 4.12, "C  The unsheared product map commutes with the deck maps",
        fontsize=16, weight="bold", color=NAVY)
node = dict(boxstyle="round,pad=.5", facecolor="white",
            edgecolor=BLUE, linewidth=1.4)
for xy, text in [((2.1, 3.03), r"$(9,x)$"),
                 ((10.7, 3.03), r"$(8,Wx)$"),
                 ((2.1, .77), r"$(5,x')$"),
                 ((10.7, .77), r"$(2,Wx')$")]:
    ax.text(*xy, text, fontsize=17, ha="center", va="center",
            color=NAVY, bbox=node)
arrow(ax, (3.2, 3.03), (9.4, 3.03), color=ORANGE, width=2)
ax.text(6.3, 3.36, r"$\mathcal{J}:\ s\mapsto s-a,\quad a=1$",
        fontsize=13, color=ORANGE, ha="center")
arrow(ax, (3.2, .77), (9.4, .77), color=ORANGE, width=2)
ax.text(6.3, .40, r"$\mathcal{J}:\ s\mapsto s-a',\quad a'=3$",
        fontsize=13, color=ORANGE, ha="center")
arrow(ax, (2.1, 2.62), (2.1, 1.17), color=BLUE, width=2)
ax.text(.3, 1.89, r"$\Gamma_1^E$"+"\n"+r"$-R_1=-4$",
        fontsize=13, color=BLUE, ha="left", va="center")
arrow(ax, (10.7, 2.62), (10.7, 1.17), color=TEAL, width=2)
ax.text(11.16, 1.89, r"$\Gamma_2^E$"+"\n"+r"$-R_2=-6$",
        fontsize=13, color=TEAL, ha="left", va="center")
ax.text(6.3, 2.09, r"$9-4-3=9-1-6=2$", color=NAVY,
        fontsize=17, ha="center")
ax.text(6.3, 1.50, r"$\mathcal{B}(5,x')A_{1,x}=A_{2,Wx}\mathcal{B}(9,x)$",
        color=NAVY, fontsize=13, ha="center")
ax.text(0, -.26, "The arrows include the full fiber maps and normal inverses.  [IC50–59]",
        color=MUTED, fontsize=11)
ax.text(0, -.76,
        r"After the shear: $D=H\mathcal{J}$,   $(HG)(s,y)=G(s-a(Vy),y)$,   "
        r"$D(1\otimes x)=1\otimes\Phi(x)$.",
        color=NAVY, fontsize=12)

fig.text(.055, .106,
         "Height alignment extracts the coefficient conjugacy; it does not claim that D intertwines the full variable-roof decks.",
         fontsize=11.2, color=MUTED)
fig.text(.055, .066,
         "Exact objects and proofs: OA-FLOW-IC, IC7–12, IC41–46 and IC50–60.",
         fontsize=11.2, color=NAVY)
fig.text(.055, .038,
         "Original mathematical illustration • reproducible Python / Matplotlib • CC0-1.0; bundled fonts retain their license.",
         fontsize=10.2, color=MUTED)

fig.savefig(ROOT / "induced-corners.png", dpi=180,
            metadata={"Software": "Original induced-corners renderer"})
fig.savefig(ROOT / "induced-corners.svg",
            metadata={"Date": None, "Creator": "Original induced-corners renderer",
                      "Title": DATA["title"]})
plt.close(fig)
for name in ["induced-corners.svg", "induced-corners.png"]:
    p = ROOT / name
    print(name, hashlib.sha256(p.read_bytes()).hexdigest())
