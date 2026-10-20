"""Numerical samples of the formulas in AN01-U009 P4 and AN01-U021 C5.

All mathematical assertions are proved in the accompanying lessons.
Original figure by GPT-6 Astra (OpenAI), 2026; CC0.
Run with NumPy and Matplotlib. Outputs are written beside this file.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
matplotlib.rcParams["svg.hashsalt"] = "AN01-local-averaging-and-lattice-partitions"

root = Path(__file__).resolve().parent


def eta(t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    positive = t > 0
    out[positive] = np.exp(-1 / t[positive])
    return out


def psi(x):
    s = (np.abs(x) - 0.55) / 0.05
    return eta(1 - s) / (eta(s) + eta(1 - s))


def weight(x):
    return psi(x) / sum(psi(x - k) for k in range(-4, 5))


x = np.linspace(-0.5, 0.5, 1801)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), layout="constrained")
ax = axes[0]
colors = ["#a14590", "#126c8c", "#be6533"]
for k, color in zip([-1, 0, 1], colors):
    ax.plot(x, weight(x - k), color=color, lw=2.3, label=fr"$\chi(x-({k}))$")
total = sum(weight(x-k) for k in [-1, 0, 1])
assert np.max(np.abs(total-1)) < 1e-12
ax.plot(x, total, "k--", lw=1.2, label="sum = 1")
ax.set(xlim=(-.5, .5), ylim=(-.04, 1.13), xlabel=r"$x$ in the fundamental interval",
       ylabel="partition weight", title="Compact support with a prescribed margin")
ax.legend(fontsize=9, loc="center")
ax.text(0, .18, r"$\psi$: plateau $[-0.55,0.55]$; support $[-0.6,0.6]$",
        ha="center", fontsize=9)

t = np.linspace(-1, 1, 20001)
raw = eta(1 - t*t)
dt = t[1]-t[0]
cdf = np.r_[0, np.cumsum((raw[1:]+raw[:-1])*dt/2)]
cdf /= cdf[-1]
epsilon = .25
y = np.linspace(-.45, .45, 1801)
smooth = np.interp(y/epsilon, t, cdf, left=0, right=1)
ax = axes[1]
ax.axvspan(-epsilon, epsilon, color="#e8edf4", label="possible error interval")
ax.plot(y, smooth, color="#126c8c", lw=2.3, label=r"$\rho_\varepsilon*H$")
ax.plot([-.45, 0], [0, 0], color="#be6533", lw=2, label=r"$H$")
ax.plot([0, .45], [1, 1], color="#be6533", lw=2)
ax.plot([0], [.5], "o", color="#126c8c")
ax.annotate(r"$F(0)=1/2$", xy=(0, .5), xytext=(-.34, .66),
            arrowprops={"arrowstyle": "->"}, fontsize=10)
ax.set(xlim=(-.45, .45), ylim=(-.04, 1.13), xlabel=r"$x$; $\varepsilon=0.25$",
       ylabel="function value", title="A shrinking layer with persistent uniform error")
ax.set_xticks([-.25, 0, .25], [r"$-\varepsilon$", "0", r"$\varepsilon$"])
ax.legend(fontsize=9, loc="lower right")
for ax in axes:
    ax.grid(alpha=.2)
fig.suptitle("Local averaging and lattice partitions — numerical samples of proved formulas",
             fontsize=13)
for suffix in ["png", "svg"]:
    target = root / f"local-averaging-and-lattice-partitions.{suffix}"
    fig.savefig(target, dpi=160, metadata={"Date": None} if suffix == "svg" else None)
    if suffix == "svg":
        target.write_text("\n".join(line.rstrip() for line in target.read_text(encoding="utf-8").splitlines()) + "\n",
                          encoding="utf-8", newline="\n")
