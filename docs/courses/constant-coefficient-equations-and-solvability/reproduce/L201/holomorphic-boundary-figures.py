"""Reproduce the exact spherical direction geometry and strip multipliers."""
from pathlib import Path
from io import BytesIO
import json
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT/"holomorphic-boundary-figures.json").read_text(encoding="utf-8"))
OUT = ROOT/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
    "svg.fonttype": "none", "svg.hashsalt": "holomorphic-boundary-direction-geometry",
    "axes.spines.top": False, "axes.spines.right": False})
BLUE = "#1669aa"
RED = "#b32836"
GRAY = "#67717b"


def save(fig, name):
    for fmt in ["png", "svg"]:
        stream = BytesIO()
        metadata = ({"Software": "Original mathematical illustration"} if fmt == "png"
                    else {"Date": None, "Creator": "GPT-6.1 Sol (OpenAI), CC0"})
        fig.savefig(stream, format=fmt, dpi=150, metadata=metadata)
        b = stream.getvalue()
        if fmt == "svg":
            b = ("\n".join(line.rstrip() for line in b.decode().splitlines())+"\n").encode()
        p = OUT/(name+"."+fmt)
        if p.exists() and "--overwrite" not in sys.argv:
            assert p.read_bytes() == b, "Reproduction mismatch: "+p.name
        else:
            p.write_bytes(b)
    plt.close(fig)


angle = np.linspace(0, 2*np.pi, 401)
half = np.pi/DATA["boundary_patch"]["half_width_pi_denominator"]
patch = np.linspace(np.pi-half, np.pi+half, 101)
cone = np.linspace(-half, half, 101)
fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), layout="constrained")
for ax in axes:
    ax.set_aspect("equal")
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.55, 1.55))
    ax.axhline(0, color=GRAY, lw=0.8, alpha=0.5)
    ax.axvline(0, color=GRAY, lw=0.8, alpha=0.5)
    ax.grid(alpha=0.13)
axes[0].plot(np.cos(angle), np.sin(angle), color=GRAY, lw=1.5)
axes[0].plot(np.cos(patch), np.sin(patch), color=BLUE, lw=5)
axes[0].scatter([-1], [0], color=BLUE, s=38, zorder=5)
axes[0].annotate("", (-1, 0), (0, 0), arrowprops={"arrowstyle": "->", "lw": 2.2, "color": BLUE})
axes[0].text(-1.48, 0.25, r"$W$", color=BLUE, fontsize=14)
axes[0].text(-0.86, -0.4, r"$-\theta_0=(-1,0)$", color=BLUE, fontsize=11)
axes[0].text(0.14, 1.1, r"$|y|=1$", color=GRAY)
axes[0].set(xlabel=r"$y_1$", ylabel=r"$y_2$", title="Imaginary boundary: select a patch")
axes[1].fill(np.r_[0, 1.5*np.cos(cone), 0], np.r_[0, 1.5*np.sin(cone), 0], color=RED, alpha=0.12)
for a in [-half, half]:
    axes[1].plot([0, 1.5*np.cos(a)], [0, 1.5*np.sin(a)], color=RED, lw=1.5)
axes[1].annotate("", (1, 0), (0, 0), arrowprops={"arrowstyle": "->", "lw": 2.5, "color": RED})
axes[1].text(0.3, 0.12, r"$\theta_0=(1,0)$", color=RED, fontsize=11)
axes[1].text(0.32, -1.05, r"$\arg\xi\in[-\pi/6,\pi/6]$", color=RED, fontsize=11)
axes[1].set(xlabel=r"$\xi_1$", ylabel=r"$\xi_2$", title="Possible frequencies: the opposite cone")
save(fig, "boundary-patch-and-frequency-direction")

xi = np.linspace(*DATA["strip_multipliers"]["frequency_interval"], 501)
upper = 1/(1+np.exp(2*xi))
lower = 1/(1+np.exp(-2*xi))
fig, ax = plt.subplots(figsize=(10, 4.8), layout="constrained")
ax.plot(xi, upper, color=BLUE, lw=2.5, label=r"Upper boundary: $1/(1+e^{2\xi})$")
ax.plot(xi, lower, color=RED, lw=2.5, label=r"Lower boundary: $1/(1+e^{-2\xi})$")
ax.plot(xi, upper+lower, color=GRAY, ls="--", lw=1.2, label="Sum = 1")
ax.axvline(0, color=GRAY, lw=0.8, alpha=0.7)
ax.scatter([0], [0.5], color=GRAY, s=35, zorder=5)
ax.text(0.13, 0.54, r"$(0,1/2)$", fontsize=11)
ax.set(xlabel=r"Real frequency $\xi$", ylabel="Multiplier value", xlim=(-6, 6), ylim=(-0.03, 1.08),
    title="Two exact complementary boundary multipliers")
ax.grid(alpha=0.18)
ax.legend(loc="upper left", bbox_to_anchor=(0.03, 0.8), frameon=False, fontsize=11)
save(fig, "complementary-boundary-multipliers")
print("Both holomorphic-boundary figures regenerated." if "--overwrite" in sys.argv
      else "Both holomorphic-boundary figures reproduced exactly.")
