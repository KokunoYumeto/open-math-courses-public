"""Reproduce two original characteristic-ray figures without temporary copies."""
from pathlib import Path
from io import BytesIO
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT/"characteristic-ray-figures.json").read_text(encoding="utf-8"))
OUT = ROOT/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
    "svg.fonttype": "none", "svg.hashsalt": "characteristic-ray-mathematics",
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
        data = stream.getvalue()
        if fmt == "svg":
            data = ("\n".join(line.rstrip() for line in data.decode().splitlines())+"\n").encode()
        target = OUT/(name+"."+fmt)
        if target.exists():
            assert target.read_bytes() == data, "Reproduction mismatch: "+target.name
        else:
            target.write_bytes(data)
    plt.close(fig)


r = np.linspace(*DATA["imaginary_push"]["r_interval"], 401)
epsilon = DATA["imaginary_push"]["epsilon"]
T = DATA["imaginary_push"]["T"]
fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
axes[0].plot(r, epsilon*r, color=BLUE, lw=2.4, label=r"$\operatorname{Im}\zeta_1=r/3$")
axes[0].plot(r, T+epsilon*r, color=RED, lw=2.4, label=r"$\operatorname{Im}\zeta_2=4+r/3$")
axes[0].set(xlabel=r"$r=\operatorname{Re}\zeta_1$", ylabel="Imaginary coordinate",
    title="A graph that avoids polynomial zeros", xlim=(0, 12), ylim=(0, 9))
axes[0].legend(loc="upper left", frameon=False, fontsize=10)
axes[0].text(0.5, 0.12, r"$P(\zeta)=\zeta_2+2i$"+"\n"+r"$\operatorname{Im}P=6+r/3>0$",
    transform=axes[0].transAxes, ha="center", va="center", fontsize=11)
axes[1].plot(r, np.exp(-epsilon*r), color=BLUE, lw=2.4)
axes[1].set(xlabel=r"$r$", ylabel=r"$|e^{i(1,0)\cdot\zeta}|$", xlim=(0, 12), ylim=(0, 1.08),
    title="Decay at the excluded base point")
axes[1].text(0.42, 0.75, r"$x_0=(1,0)$"+"\n"+r"$|e^{ix_0\cdot\zeta}|=e^{-r/3}$",
    transform=axes[1].transAxes, fontsize=12)
for ax in axes:
    ax.grid(alpha=0.18)
save(fig, "imaginary-frequency-push")

fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), layout="constrained")
for ax in axes:
    ax.set_aspect("equal")
    ax.set(xlim=(-1.7, 1.8), ylim=(-1.8, 1.8))
    ax.axhline(0, color=GRAY, lw=0.8, alpha=0.45)
    ax.axvline(0, color=GRAY, lw=0.8, alpha=0.45)
    ax.grid(alpha=0.13)
axes[0].axhline(0, color=GRAY, lw=2)
axes[0].axvline(0, color=GRAY, lw=2)
axes[0].annotate("", (1, 0), (0, 0), arrowprops={"arrowstyle": "->", "color": RED, "lw": 2.7})
axes[0].scatter([1], [0], color=RED, s=35, zorder=5)
axes[0].annotate("", (1, 1), (1, 0), arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 2.7})
axes[0].text(0.1, -0.42, r"$\xi_0=(1,0)$", color=RED)
axes[0].text(0.05, 1.2, r"$a(\xi_0)=(0,1)$", color=BLUE)
axes[0].set(xlabel=r"$\xi_1$", ylabel=r"$\xi_2$", title=r"Frequency space: $p_2=\xi_1\xi_2$")
axes[1].plot([0, 0], [-1.8, 1.8], color=BLUE, lw=2)
for s in DATA["line_and_covector"]["attached_covector_base_heights"]:
    axes[1].annotate("", (1, s), (0, s), arrowprops={"arrowstyle": "->", "color": RED, "lw": 2.2})
axes[1].annotate("", (0, -0.5), (0, -1.5), arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 2.7})
axes[1].text(-1.55, 0.65, r"$L=\{x_1=0\}$", color=BLUE)
axes[1].text(0.22, 0.25, "Positive covectors", color=RED, fontsize=10)
axes[1].set(xlabel=r"$x_1$", ylabel=r"$x_2$", title="Base space: the covector stays fixed")
save(fig, "fixed-covector-and-moving-base")
print("Both original figures reproduced exactly.")
