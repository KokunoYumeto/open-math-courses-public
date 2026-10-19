"""Exact model for AN01-U091 Theorem 6 and Exercise 3. CC0-1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "svg.fonttype": "none"})
fig = plt.figure(figsize=(12, 6.8), layout="constrained")
grid = fig.add_gridspec(3, 2, width_ratios=[1.05, 1.2])
ax = fig.add_subplot(grid[:, 0])
ax.axhline(0, color="#9ba7b4", lw=0.7)
ax.axvline(0, color="#9ba7b4", lw=0.7)
ax.plot([-3.1, 3.1], [0, 0], color="#12688e", lw=3)
for t in [-2.4, -1.2, 0, 1.2, 2.4]:
    ax.annotate("", (t, 0.8), (t, 0),
                arrowprops={"arrowstyle": "-|>", "color": "#b54a25", "lw": 2})
ax.annotate("", (2.0, -0.75), (0.9, -0.75),
            arrowprops={"arrowstyle": "-|>", "color": "#12688e", "lw": 2})
ax.text(1.45, -0.98, r"$a=(1,0)$", ha="center", color="#12688e")
ax.text(0, 1.10, r"Only positive multiples of $\xi_0=(0,1)$",
        ha="center", color="#9a391b", fontsize=11)
ax.text(0, -1.35, r"$\{(t,0;0,s):\,t\in\mathbb{R},\ s>0\}$",
        ha="center", fontsize=14)
ax.text(-3.1, 0, r"$\cdots$", ha="right", va="center", fontsize=18)
ax.text(3.1, 0, r"$\cdots$", ha="left", va="center", fontsize=18)
ax.set(xlim=(-3.6, 3.6), ylim=(-1.65, 1.6), xlabel=r"base coordinate $t$",
       ylabel=r"base coordinate $z$", title="Exact wavefront prescribed by Theorem 6")
ax.set_aspect("equal", adjustable="box")
ax.text(0.5, -0.20,
        "Arrows represent cotangent directions.\n"
        "The blue base line continues in both directions.",
        transform=ax.transAxes, ha="center", va="top", fontsize=11)
z = np.linspace(-0.7, 0.7, 2401)
b = np.zeros_like(z)
inside = abs(z) < 0.5
b[inside] = np.exp(1 - 1 / (1 - 4 * z[inside]**2))
for row, T in enumerate([8, 16, 32]):
    ax = fig.add_subplot(grid[row, 1])
    ax.fill_between(z, -b, b, color="#eaf1f5")
    ax.plot(z, b * np.cos(T*z), color="#145e86", lw=1.6)
    ax.plot(z, b, color="#788994", lw=0.8, ls="--")
    ax.plot(z, -b, color="#788994", lw=0.8, ls="--")
    for endpoint in [-0.5, 0.5]:
        ax.axvline(endpoint, color="#b54a25", ls=":", lw=1)
    ax.set(xlim=(-0.7, 0.7), ylim=(-1.1, 1.1), yticks=[-1,0,1],
           ylabel="real part")
    ax.text(0.98, 0.85, rf"$T={T}$", ha="right", transform=ax.transAxes)
    if row == 0:
        ax.set_title(r"Smooth exact packets: $e^{iTz-it}b_0(z)$ at $t=0$")
    if row == 2:
        ax.set_xlabel(r"transverse coordinate $z$; support radius $1/2$")
    else:
        ax.tick_params(labelbottom=False)
fig.suptitle(r"$P=D_tD_z+D_z$: one characteristic line and narrow packets",
             fontsize=16)
for extension in ["png", "svg"]:
    destination = out / ("whole-characteristic-line." + extension)
    fig.savefig(destination, dpi=160, facecolor="white")
    if extension == "svg":
        destination.write_text("\n".join(line.rstrip() for line in
            destination.read_text(encoding="utf-8").splitlines()) + "\n",
            encoding="utf-8")
plt.close(fig)
