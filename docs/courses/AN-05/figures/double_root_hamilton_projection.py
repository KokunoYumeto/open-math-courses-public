"""Exact Hamilton orbit and base cusp in SV2--SV7. Public domain, CC0."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
h = np.linspace(-1, 1, 801)
x1, x2, xi1 = -h**2, -2*h**3/3, -h
assert np.max(np.abs(xi1**2+x1)) < 1e-14
fig, axes = plt.subplots(1, 3, figsize=(15, 8.8))
fig.subplots_adjust(left=0.055, right=0.98, bottom=0.37, top=0.76, wspace=0.37)
blue, orange = "#12658c", "#a65a12"
for ax in axes:
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)

base, phase, height = axes
base.axvspan(-1.08, 0, color="#eaf3f0")
base.axvline(0, color="#66736d", ls="--", lw=1.2)
for mask, color, label in [(h <= 0, blue, r"$h\leq0$"),
                           (h >= 0, orange, r"$h\geq0$")]:
    base.plot(x1[mask], x2[mask], color=color, lw=2.6, label=label)
    phase.plot(x1[mask], xi1[mask], color=color, lw=2.6)
    height.plot(h[mask], h[mask]**2, color=color, lw=2.6)
for value in (-0.78, 0.55):
    nxt = value + 0.08
    base.annotate("", xy=(-nxt**2, -2*nxt**3/3),
                  xytext=(-value**2, -2*value**3/3),
                  arrowprops={"arrowstyle": "->", "color": "#34443d", "lw": 1.5})
    phase.annotate("", xy=(-nxt**2, -nxt), xytext=(-value**2, -value),
                   arrowprops={"arrowstyle": "->", "color": "#34443d", "lw": 1.5})
for ax in (base, phase):
    ax.scatter([0], [0], color="#34443d", s=32, zorder=5)
base.set(xlim=(-1.08, 0.08), ylim=(-0.75, 0.75), xlabel=r"$x_1=-h^2$",
         ylabel=r"$x_2=-2h^3/3$", title="Base projection: a cusp")
base.text(-0.99, -0.13, r"$\psi=-x_1>0$"+"\nPositive oriented side", fontsize=11)
base.text(-0.92, 0.17, r"$\dot x(0)=(0,0)$", fontsize=11)
base.legend(loc="upper right", fontsize=10, frameon=False)
phase.set(xlim=(-1.08, 0.08), ylim=(-1.12, 1.12), xlabel=r"$x_1$", ylabel=r"$\xi_1=-h$",
          title=r"Phase projection $(x_1,\xi_1)$")
phase.text(-0.98, 0.12, "Full phase velocity at zero:\n"+r"$(\dot x_1,\dot x_2,\dot\xi_1,\dot\xi_2)$"
           +"\n"+r"$=(0,0,-1,0)\ne0$", fontsize=11)
height.set(xlim=(-1.08, 1.08), ylim=(-0.05, 1.14), xlabel="Hamilton time $h$",
           ylabel=r"$\psi(x(h))-\psi(0)=h^2$", title="Positive tangency curvature")
height.scatter([0], [0], color="#34443d", s=32, zorder=5)
height.text(0.24, 0.9, r"$\frac{d^2}{dh^2}\psi(x(h))=2$", fontsize=13,
            transform=height.transAxes)
height.text(0.28, 0.45, r"$H_p\psi(0,e_2)=0$"+"\n"+r"$H_p^2\psi(0,e_2)=2>0$",
            fontsize=11, transform=height.transAxes)

fig.suptitle("A repeated real normal root coexists with strong pseudoconvexity\n"
             r"$p=\xi_1^2+x_1\xi_2^2$, $x_0=0$, $N=-e_1$, $p(0,N)=1$", y=0.97, fontsize=16)
fig.text(0.5, 0.82, r"Full characteristic orbit: $(x_1,x_2,\xi_1,\xi_2)=(-h^2,-2h^3/3,-h,1)$; $p=0$",
         ha="center", fontsize=12)
fig.text(0.5, 0.22,
         r"Double normal root: $p(0,e_2+sN)=s^2$. For every $C^2$ defining function with $\psi'(0)=-e_1$:"
         +"\n"+r"$\{p,\{p,\psi\}\}(0,\xi)=4\xi_1^2\psi_{11}(0)+2\xi_2^2>0$ on nonzero real characteristics.",
         ha="center", fontsize=11)
fig.text(0.5, 0.13,
         r"Positive complex shifts have no characteristic: $p(0,\xi+itN)=(\xi_1-it)^2\ne0$ for real $\xi$, $t>0$.",
         ha="center", fontsize=11)
fig.text(0.5, 0.025,
         "Exact coordinate projections, not a stationary full bicharacteristic. Hamilton time h differs from normal-root s and complex-shift t.\n"
         "Receiving correction SV2--SV7; Hörmander IV, final unnumbered paragraph of Section 28.3, printed p. 242. CC0.",
         ha="center", fontsize=9.5)
fig.savefig(Path(__file__).with_name("double-root-hamilton-projection.png"), dpi=180,
            bbox_inches="tight", metadata={"Software": "Matplotlib",
                "Title": "Double normal root and exact Hamilton base projection",
                "Description": "Exact coordinates, phase projection and positive tangency curvature for SV2--SV7",
                "License": "CC0"})
plt.close(fig)
