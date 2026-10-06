"""Reproduce the exact planar example and the finite grid in CD034/L1.

The geometry is illustrative data, not a numerical proof of cycle detection.
Run from any directory; outputs stay beside this file in figures/.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np

BASE = Path(__file__).resolve().parent
OUT = BASE / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.hashsalt": "AN02-CD034-v1"})
blue, orange, dark = "#135b8c", "#b85615", "#202b35"
fig, (ax, grid) = plt.subplots(1, 2, figsize=(13.8, 6.15),
                              gridspec_kw={"width_ratios": [1.04, 1.16]})
fig.patch.set_facecolor("white")

angles = np.arange(8) * np.pi / 4
centers = np.column_stack((np.cos(angles), np.sin(angles)))
radius = 3 / 5
for j, (cx, cy) in enumerate(centers):
    ax.add_patch(Circle((cx, cy), radius, color=blue, alpha=.075, lw=0))
    ax.add_patch(Circle((cx, cy), radius, fill=False, edgecolor=blue, alpha=.45, lw=.9))
    ax.plot(cx, cy, "o", color=blue, ms=3.7)
    ax.text(1.23 * cx, 1.23 * cy, f"$U_{j}$", ha="center", va="center", color=blue)
theta = np.linspace(0, 2 * np.pi, 641)
ax.plot(np.cos(theta), np.sin(theta), color=dark, lw=2.15)
for angle in [np.pi / 6, 5 * np.pi / 6, 3 * np.pi / 2]:
    a, b = angle - .045, angle + .045
    ax.add_patch(FancyArrowPatch((np.cos(a), np.sin(a)), (np.cos(b), np.sin(b)),
                 arrowstyle="-|>", mutation_scale=16, color=dark, lw=1.6))
ax.plot(0, 0, "x", color="#a02228", ms=9, mew=2)
ax.text(0, -.16, "0 removed", ha="center", va="top", color="#a02228")
ax.annotate("one smooth arc", xy=(np.cos(.13), np.sin(.13)), xytext=(1.24, .74),
            color=orange, fontsize=10,
            arrowprops={"arrowstyle": "->", "color": orange, "lw": 1})
ax.text(0, -1.96, r"$U_j=B(e^{i\pi j/4},3/5)$,  $z=\sum_{j=0}^{7}\sigma_j$",
        ha="center", va="center", color=dark)
ax.text(0, -2.22, r"$\int_z dz/z=2\pi i$", ha="center", va="center", color=dark, fontsize=13)
ax.set(xlim=(-1.84, 1.84), ylim=(-2.39, 1.88), xlabel="real coordinate", ylabel="imaginary coordinate")
ax.set_aspect("equal", adjustable="box")
ax.set_title("A finite convex cover near a cycle", color=dark, fontsize=14, pad=12)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=.16)

positions = {}
for q in range(3):
    for p in range(3):
        x, y = 1.8 * p, 1.45 * q
        positions[p, q] = (x, y)
        grid.add_patch(Rectangle((x - .58, y - .28), 1.16, .56,
                       facecolor="#f0f5f8", edgecolor="#9bb2c2", lw=1))
        grid.text(x, y, rf"$A^{{{p},{q}}}$ / $E^{{{p},{q}}}$",
                  ha="center", va="center", color=dark, fontsize=11)
        if p < 2:
            grid.annotate("", xy=(x + 1.8 - .63, y), xytext=(x + .63, y),
                           arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.35})
            grid.text(x + .9, y + .1, r"$\delta$", color=blue, ha="center", va="bottom")
        if q < 2:
            grid.annotate("", xy=(x, y + 1.45 - .32), xytext=(x, y + .32),
                          arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.35})
            sign = "+" if p % 2 == 0 else "-"
            grid.text(x + .14, y + .7, rf"${sign}d_v$", color=blue, ha="left", va="center")
for left, right in [((0, 2), (1, 1)), ((1, 1), (2, 0))]:
    x0, y0 = positions[left]
    x1, y1 = positions[right]
    grid.add_patch(FancyArrowPatch((x0 + .42, y0 - .34), (x1 - .42, y1 + .34),
                   arrowstyle="-|>", color=orange, lw=2.25, mutation_scale=16))
grid.text(1.8, -.78, r"$D=\delta+(-1)^p d_v$,  $D^2=0$", ha="center", color=dark, fontsize=13)
grid.text(1.8, -1.2, "Orange: remove positive vertical degree\nin a total degree-two cocycle (CD5c).",
          ha="center", va="center", color=orange, fontsize=11)
grid.text(-.94, 2.9, "$q=2$", ha="right", va="center", color=dark)
grid.text(-.94, 1.45, "$q=1$", ha="right", va="center", color=dark)
grid.text(-.94, 0, "$q=0$", ha="right", va="center", color=dark)
for p in range(3):
    grid.text(1.8 * p, 3.5, f"$p={p}$", ha="center", color=dark)
grid.set_title("Finite diagonal comparison", color=dark, fontsize=14, pad=12)
grid.set(xlim=(-1.45, 4.58), ylim=(-1.53, 3.84))
grid.axis("off")
fig.subplots_adjust(left=.065, right=.985, bottom=.12, top=.88, wspace=.2)
fig.text(.5, .035, "Actual planar example at left; algebraic comparison mechanism at right.  CD2-CD6 and learner Figure L1.",
         ha="center", color=dark, fontsize=10)
fig.savefig(OUT / "cycle-detection.png", dpi=170, metadata={"Software": "AN02-CD034 native renderer"})
fig.savefig(OUT / "cycle-detection.svg", metadata={"Date": None, "Creator": "AN02-CD034 native renderer"})
plt.close(fig)
spec = {
    "schema": "AN02-CD034-diagram-geometry/v1",
    "mathematical_status": "exact coordinate example and algebraic schematic; samples are not a proof",
    "left": {
        "ambient": "C* = R^2 minus the origin",
        "centers_exact": [f"exp(i*pi*{j}/4)" for j in range(8)],
        "centers_numerical": centers.tolist(),
        "radius_exact": "3/5",
        "arcs_exact": "sigma_j(t)=exp(i*(pi*j/4-pi/8+(pi/4)*t)), 0<=t<=1",
        "arc_distance_bound_exact": "2*sin(pi/16)<3/5",
        "orientation": "counterclockwise",
        "period_exact": "integral_z dz/z = 8*(i*pi/4) = 2*pi*i",
        "scope": "covers the unit circle; not the whole noncompact punctured plane",
        "circle_samples": np.column_stack((np.cos(theta), np.sin(theta))).tolist(),
    },
    "right": {
        "bidegrees": [[p, q] for q in range(3) for p in range(3)],
        "horizontal": "delta: (p,q)->(p+1,q), alternating restrictions",
        "vertical": "(-1)^p d_v: (p,q)->(p,q+1)",
        "total": "D=delta+(-1)^p*d_v; D^2=0",
        "elimination_path": [[0, 2], [1, 1], [2, 0]],
        "proof_locator": "cycle-detection-proof.md CD5c",
        "not_a_geometric_homotopy": True,
    },
    "blender_decision": "Planar coordinates and an algebraic grid gain no clarity from a 3D scene.",
}
(OUT / "cycle-detection.geometry.json").write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"rendered": ["cycle-detection.png", "cycle-detection.svg", "cycle-detection.geometry.json"]}))
