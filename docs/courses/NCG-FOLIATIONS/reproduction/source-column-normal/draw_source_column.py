"""Actual source column, exact smooth overlap weights and twisted-fibre spectrum.

New mathematical expression and generator: CC0-1.0. Bundled unmodified fonts
retain the complete notice embedded in both outputs.
"""
from pathlib import Path
import argparse
import math
import os
import tempfile

HERE = Path(__file__).resolve().parent
CACHE = tempfile.TemporaryDirectory(prefix="source-column-normal-")
os.environ["MPLCONFIGDIR"] = CACHE.name
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path, default=HERE.parents[1] / "figures")
args = parser.parse_args()
OUT = args.output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
REG = FontProperties(fname=str(HERE / "fonts/DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts/DejaVuSans-Bold.ttf"))
plt.rcParams.update({"svg.fonttype": "path", "svg.hashsalt": "actual-source-column-20261006"})
INK, BLUE, GREEN, RED = "#213547", "#2669a8", "#24795f", "#b5404b"
fig, axes = plt.subplots(2, 2, figsize=(16, 10.8))
fig.patch.set_facecolor("white")

def label(a, x, y, s, size=11, bold=False, color=INK, ha="center"):
    return a.text(x, y, s, fontsize=size, fontproperties=BOLD if bold else REG,
                  color=color, ha=ha, va="center", transform=a.transAxes,
                  linespacing=1.28, zorder=12)

def arrow(a, start, end, color=INK, width=1.8):
    a.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17,
                              linewidth=width, color=color, transform=a.transAxes))

for a in axes.flat:
    a.set_xlim(0, 1)
    a.set_ylim(0, 1)
    a.axis("off")

a = axes[0, 0]
label(a, .5, .965, "A. One actual source per leaf", 14, True)
label(a, .5, .855, "G = V ×_B V       T = σ(B)       Y = G|sT ≅ V", 12)
for cx in [.22, .77]:
    a.add_patch(Circle((cx, .55), .14, transform=a.transAxes,
                      facecolor="#edf4f9", edgecolor=BLUE, linewidth=2))
    a.plot([cx], [.41], "o", color=RED, markersize=7, transform=a.transAxes)
    label(a, cx, .56, "V_b", 13, True)
label(a, .22, .31, "σ(b)", 12, True, RED)
label(a, .77, .31, "fixed source σ(b)", 11, False, RED)
arrow(a, (.36, .57), (.62, .57), BLUE)
label(a, .49, .66, "v ↦ (v,σ(b))", 11, True, BLUE)
label(a, .5, .20, "Leaf circles are schematics; the fibre may be any closed L.", 10)
label(a, .5, .10, "H = L²(V,p*D_B)     D_H = normal horizontal Dirac\nNo second source coordinate, and no leaf spin-c assumption.", 11)

a = axes[0, 1]
label(a, .5, .965, "B. Buffered charts glued by an exact projection", 14, True)
label(a, .5, .855, "J u = (χ₀u,χ₁u)      P = JJ*      χ₀²+χ₁² = 1", 12)
t = np.linspace(0, 1, 2001)
radius = .36
def bump(t, center):
    d = np.abs((t - center + .5) % 1 - .5)
    z = np.zeros_like(t)
    inside = d < radius
    z[inside] = np.exp(-1 / (1 - (d[inside] / radius) ** 2))
    return z
b0, b1 = bump(t, .25), bump(t, .75)
den = np.sqrt(b0*b0+b1*b1)
c0, c1 = b0/den, b1/den
plot = a.inset_axes([.12, .32, .80, .39])
plot.plot(t, c0, color=BLUE, linewidth=2.2, label="χ₀")
plot.plot(t, c1, color=GREEN, linewidth=2.2, label="χ₁")
plot.plot(t, c0*c1, color=RED, linewidth=1.8, linestyle="--", label="P₀₁ = χ₀χ₁")
plot.set_xlim(0, 1); plot.set_ylim(-.04, 1.06)
plot.set_xticks([0, .25, .5, .75, 1]); plot.set_yticks([0, .5, 1])
for item in plot.get_xticklabels()+plot.get_yticklabels(): item.set_fontproperties(REG); item.set_fontsize(9)
plot.spines[["top", "right"]].set_visible(False)
leg = plot.legend(loc="lower center", bbox_to_anchor=(.5, 1.00), ncol=3, frameon=False,
                  prop=FontProperties(fname=str(HERE/"fonts/DejaVuSans.ttf"), size=9))
label(a, .5, .225, "Base t mod 1; support radius 0.36 inside chart radius 0.38.", 10)
label(a, .5, .13, "P D_loc P closes on J Dom(D_H): self-adjoint.\nIndependent open-chart closures have no such guarantee.", 11)

a = axes[1, 0]
label(a, .5, .965, "C. Antipodal sphere seam, full determinant retained", 14, True)
label(a, .5, .86, "V = (R × S²)/((t+1,x) ∼ (t,−x))      κ = π/5", 12)
theta = np.linspace(0, 2*math.pi, 241)
for cx in [.25, .75]:
    a.plot(cx+.115*np.sin(theta), .52+.18*np.cos(theta),
           color=BLUE, linewidth=1.8, transform=a.transAxes)
    a.plot([cx], [.70], "o", color=RED, markersize=6, transform=a.transAxes)
    a.plot([cx], [.34], "o", color=GREEN, markersize=6, transform=a.transAxes)
    label(a, cx, .52, "S²", 14, True, BLUE)
arrow(a, (.31,.69), (.68,.35), RED)
arrow(a, (.31,.35), (.68,.69), GREEN)
label(a, .5, .55, "x ↦ −x", 11, True)
label(a, .25, .26, "t = 1", 10)
label(a, .75, .26, "t = 0", 10)
label(a, .5, .17, "u(1,x) = exp(−iπ/5) u(0,−x)", 12, True)
label(a, .5, .065, "Original determinant exp(2iπ/5); inverse exp(−2iπ/5).\nSphere disks are meridian projections, not solid-ball fibres.", 10)

a = axes[1, 1]
label(a, .5, .965, "D. Infinite global multiplicity, compact after convolution", 14, True)
label(a, .5, .855, "D_H = −i J_N ∂t,     full normal J_N² = 1", 12)
n = np.arange(-2, 3)
even, odd = 2*n-.2, 2*n+1-.2
freq = a.inset_axes([.14, .42, .80, .29])
freq.scatter(even, np.full(5, 1.), color=BLUE, s=33)
freq.scatter(odd, np.full(5, 0.), color=GREEN, s=33)
for x,y in [(float(x),1.) for x in even]+[(float(x),0.) for x in odd]:
    freq.text(x,y+.14,"∞",fontproperties=REG,fontsize=12,ha="center",color=RED)
freq.set_xlim(-4.6,5.5); freq.set_ylim(-.35,1.5)
freq.set_xticks([-4,-2,0,2,4]);freq.set_yticks([0,1]);freq.set_yticklabels(["odd A","even A"])
for item in freq.get_xticklabels()+freq.get_yticklabels():item.set_fontproperties(REG);item.set_fontsize(9)
freq.spines[["left","top","right"]].set_visible(False)
label(a, .5, .355, "Horizontal axis ω/π: even 2n−1/5; odd 2n+1−1/5.", 10)
label(a, .5, .255, "A u(x) = u(−x). Each dot has infinite fibre multiplicity.", 10)
label(a, .5, .15, "K_k(D_H−i)⁻¹ : L² → H¹ ↪ L² is scalar compact.", 12, True, GREEN)
label(a, .5, .055, "Real normalized plaque corner: D_B exactly; original Bott +1.", 11, True)

fig.subplots_adjust(left=.02,right=.985,bottom=.075,top=.925,wspace=.10,hspace=.15)
fig.text(.5,.985,"The source-column normal inverse on a compact smooth fibre bundle",
         ha="center",va="top",fontproperties=BOLD,fontsize=18,color=INK)
fig.text(.5,.024,"Figure 11H.1. SC.1–SC.21 and Exercises 128–130. "
         "Compact-fibre bundle result; arbitrary return holonomy remains open.",
         ha="center",fontproperties=REG,fontsize=11,color=INK)
notice=(HERE/"FONT-NOTICE.txt").read_text(encoding="utf-8")
description=("Original illustration CC0-1.0. Full unmodified font terms follow.\n"+notice)
png=OUT/"source-column-normal.png";svg=OUT/"source-column-normal.svg"
fig.savefig(png,dpi=160,metadata={"Software":"Matplotlib "+matplotlib.__version__,
                                "Description":description})
fig.savefig(svg,metadata={"Date":None,"Description":description})
plt.close(fig)
print("Rendered source-column-normal.png and source-column-normal.svg")
CACHE.cleanup()
