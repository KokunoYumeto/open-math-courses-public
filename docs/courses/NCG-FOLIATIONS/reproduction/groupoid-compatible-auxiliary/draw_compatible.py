"""Original CC0 diagram for 11R.1--11R.4. Run with --output-dir PATH.

Uses only the exact one-dimensional cone slice named in the proof.
This generator does not construct a kernel or a Kasparov factor.
Font/software notices are retained beside the source.
"""
from pathlib import Path
import argparse
import json
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
import numpy as np

HERE = Path(__file__).resolve().parent
REGULAR = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans-Bold.ttf"))
BLUE = "#155e94"
GREEN = "#087858"
ORANGE = "#b65d16"
INK = "#19334a"

def label(ax, x, y, s, size=14, bold=False, **kwargs):
    return ax.text(x, y, s, fontsize=size,
                   fontproperties=BOLD if bold else REGULAR,
                   color=INK, **kwargs)

def box(ax, xy, width, height, color="#edf4f9"):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.018",
                 linewidth=1.2, edgecolor=BLUE, facecolor=color))

def arrow(ax, p, q, color=BLUE):
    ax.annotate("", xy=q, xytext=p,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.0,
                            "shrinkA": 2, "shrinkB": 2})

def render(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams.update({"svg.hashsalt": "coherent-groupoid-auxiliary-CA-v1",
                                "svg.fonttype": "path", "axes.unicode_minus": True})
    fig = plt.figure(figsize=(15, 11), facecolor="white")
    gs = fig.add_gridspec(2, 2, height_ratios=[1.02, 1.23],
                         width_ratios=[1.06, 1.0], hspace=.18, wspace=.17,
                         left=.055, right=.97, top=.92, bottom=.075)
    a = fig.add_subplot(gs[0, :]); a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
    label(a, .0, .97, "A  The typed transfer and its exact unit restriction", 18, True)
    label(a, .0, .88, "G ⇒ T is an actual étale groupoid; C = C₀(T). All coefficients remain present.", 13)
    xs = [.07, .28, .49, .70, .93]
    nodes = ["Aᵣ", "Pᵣ", "Pₘ", "Aₘ", "ℂ"]
    for x, n in zip(xs, nodes):
        box(a, (x-.042, .64), .084, .105)
        label(a, x, .692, n, 22, True, ha="center", va="center")
    labels = [("jᵣ(η)", "degree k"), ("v", "degree 0"),
              ("jₘ(d)", "degree k"), ("dₘ", "degree q")]
    for i, (top, bottom) in enumerate(labels):
        arrow(a, (xs[i]+.05, .693), (xs[i+1]-.05, .693))
        label(a, (xs[i]+xs[i+1])/2, .79, top, 16, ha="center")
        label(a, (xs[i]+xs[i+1])/2, .60, bottom, 11, ha="center")
    label(a, .0, .47, "SUPPLIED:  proper P, factors η and d, coefficient inverse v, descent identities, normal dₘ.", 12, True)
    box(a, (.01, .15), .97, .245, "#eff8f3")
    label(a, .03, .345, "iᵣ ⊗ dᵣ = γ₀ ⊗ dN     with γ₀ = For(η ⊗ d),  dN = iₘ ⊗ dₘ", 17, True)
    label(a, .03, .26, "Whole normal restriction: γ₀ = 1C suffices.  Original local test: bU ⊗ γ₀ = bU suffices.", 12)
    label(a, .03, .185, "Then (bU ⊗ iᵣ) ⊗ dᵣ = +1.  No inverse of qA or equivariant-unit identity was inserted.", 12)
    label(a, .0, .035, "11R.1–11R.2: the unit restriction is proved by Φ(e ⊗ k)(g) = e(rg)k(g), not by choosing one fibre.", 12)

    b = fig.add_subplot(gs[1, 0]); b.set_xlim(0, 1); b.set_ylim(0, 1); b.axis("off")
    label(b, .0, .98, "B  What a proper coefficient must supply", 17, True)
    label(b, .0, .90, "11R.3: Q = K(E), E a full nonzero Hilbert field over Y.", 12)
    box(b, (.025, .65), .94, .15)
    label(b, .055, .755, "ZM(Q) = Cb(Y)", 17, True)
    label(b, .055, .687, "central, nondegenerate C₀(Z) action", 12)
    arrow(b, (.49, .64), (.49, .54))
    box(b, (.025, .38), .94, .15, "#eff8f3")
    label(b, .055, .483, "y ↦ zy : Y → Z", 17, True)
    label(b, .055, .414, "continuous, anchored and equivariant", 12)
    arrow(b, (.49, .37), (.49, .27))
    box(b, (.025, .08), .94, .18, "#fff4e7")
    label(b, .055, .206, "Z proper  ⇒  Y proper", 18, True)
    label(b, .055, .143, "compact transporters pull back", 12)
    label(b, .055, .096, "A different proper Bott algebra is still possible.", 11)

    c = fig.add_subplot(gs[1, 1])
    c.set_xlim(-1.35, 1.35); c.set_ylim(-.08, 2.05)
    c.spines[["top", "right"]].set_visible(False)
    v = np.linspace(-1.35, 1.35, 500)
    c.fill_between(v, v*v, 2.05, color="#eff8f3")
    c.plot(v, v*v, color=GREEN, lw=2)
    c.axhline(.75, color="#526477", lw=1.2, linestyle=(0, (4, 3)))
    c.plot([-.5, -.5], [.25, .75], color=BLUE, lw=2)
    c.plot([.5, .5], [.25, .75], color=ORANGE, lw=2)
    c.scatter([-.5, .5], [.75, .75], s=74, color=[BLUE, ORANGE], zorder=5)
    arrow(c, (-.44, .75), (.44, .75), GREEN)
    label(c, -.5, .90, "(−½, ¾)", 13, ha="center")
    label(c, .5, .90, "(½, ¾)", 13, ha="center")
    label(c, -.63, .45, "½", 12, ha="right")
    label(c, .63, .45, "½", 12, ha="left")
    label(c, .0, .64, "b = 1", 12, ha="center")
    label(c, -1.30, 1.95, "C  Exact one-dimensional cone slice", 16, True)
    label(c, -1.28, 1.72, "Z: t ≥ v²; L = 1; ψ(g) = b² = 1", 12)
    label(c, -1.28, 1.50, "t′ = t + 2vb + b² = ¾ − 1 + 1 = ¾", 12, True)
    label(c, -1.28, 1.28, "Excess t − v² = ½ is preserved.", 12)
    c.set_xlabel("real fibre coordinate v", fontproperties=REGULAR, fontsize=12)
    c.set_ylabel("height t", fontproperties=REGULAR, fontsize=12)
    for tick in c.get_xticklabels()+c.get_yticklabels(): tick.set_fontproperties(REGULAR)
    fig.text(.055, .975, "Coherent groupoid auxiliaries: restriction, proper coefficient and cone", fontsize=21, fontproperties=BOLD, color=INK)
    fig.text(.055, .021, "11R.1–11R.4. Cone slice is exact; the general topology is weak. Compatible kernels and proper Bott/Dirac factors are separate inputs.",
             fontsize=11, fontproperties=REGULAR, color=INK)
    notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
    png = output_dir / "groupoid-compatible-auxiliary.png"
    svg = output_dir / "groupoid-compatible-auxiliary.svg"
    fig.savefig(png, dpi=200, metadata={"Software": "Matplotlib; original diagram CC0 1.0", "Description": notice})
    fig.savefig(svg, metadata={"Date": None, "Creator": "Original CC0 mathematical diagram", "Description": notice})
    plt.close(fig)
    svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
    ET.parse(svg)
    data = {"figure_scope": "typed conditional transfer; full compact-field centre criterion; exact real cone slice",
            "slice": {"L": 1, "b": 1, "v": -.5, "t": .75,
                      "v_prime": .5, "t_prime": .75,
                      "excess": .5, "psi": 1, "proper_bound": 3},
            "proved_locators": ["11R.1", "11R.2", "11R.3", "11R.4"],
            "not_claimed": ["existence of a general holonomy kernel", "proper Bott/Dirac factorization", "full target 55"]}
    (output_dir / "figure-data.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8", newline="\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=HERE / "figures")
    render(parser.parse_args().output_dir.resolve())
