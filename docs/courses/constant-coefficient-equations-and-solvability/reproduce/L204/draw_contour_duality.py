"""Exact two-dimensional illustrations for contour duality and analytic choice."""
from pathlib import Path
import json, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"svg.hashsalt": "AN02-contour-duality302", "font.size": 11, "axes.titlesize": 12, "font.family": "DejaVu Sans", "savefig.facecolor": "white"})
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)
blue, red, green = "#17618a", "#b55422", "#167748"
def save(fig, name):
    fig.savefig(OUT / (name + ".png"), dpi=160, metadata={"Software": "Matplotlib"})
    p = OUT / (name + ".svg")
    fig.savefig(p, metadata={"Date": None})
    p.write_text("\n".join(line.rstrip() for line in p.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
    plt.close(fig)

fig, ax = plt.subplots(1, 2, figsize=(11, 4.7), layout="constrained")
x = np.linspace(-4, 4, 1601)
b = np.exp(-x*x)
ax[0].plot(x, np.cos(2*x), color=blue, alpha=.6, linestyle="--", label=r"$\mathrm{Re}\,v=\cos(2x)$")
ax[0].plot(x, b*np.cos(2*x), color=red, linewidth=2.2, label=r"$\mathrm{Re}(bv)=e^{-x^2}\cos(2x)$")
ax[0].plot(x, b, color=green, linewidth=1, alpha=.6)
ax[0].plot(x, -b, color=green, linewidth=1, alpha=.6)
ax[0].set(xlim=(-4, 4), ylim=(-1.15, 1.15), xlabel=r"physical coordinate $x$", ylabel="real part", title="Multiply a plane wave by a Schwartz function")
ax[0].legend(loc="lower center", fontsize=10)
xi = np.linspace(-8, 4, 1601)
density = np.exp(-(xi+2)**2/4)/(2*np.sqrt(np.pi))
ax[1].fill_between(xi, 0, density, color=red, alpha=.15)
ax[1].plot(xi, density, color=red, linewidth=2.2, label=r"$(2\pi)^{-1}\widehat{bv}=(2\sqrt{\pi})^{-1}e^{-(\xi+2)^2/4}$")
ax[1].annotate("", xy=(-2, .44), xytext=(-2, 0), arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2})
ax[1].annotate("unit point mass at −2\n(arrow height is schematic)", xy=(-2, .44), xytext=(-7.5, .40), fontsize=10, arrowprops={"arrowstyle": "-", "color": blue})
ax[1].text(.1, .15, r"$\int (2\pi)^{-1}\widehat{bv}\,d\xi=1$", fontsize=11)
ax[1].set(xlim=(-8, 4), ylim=(0, .51), xlabel=r"frequency $\xi$", ylabel="density with respect to real frequency", title="A point mass becomes an integrable Gaussian")
ax[1].legend(loc="upper right", bbox_to_anchor=(1, .72), fontsize=9)
for a in ax: a.grid(alpha=.16)
save(fig, "a-plane-wave-after-schwartz-smoothing")

fig, ax = plt.subplots(1, 2, figsize=(10.6, 4.7), layout="constrained")
theta = np.linspace(0, 2*np.pi, 1201)
radius, image_radius = 3/4, 12/25
lam = radius*np.exp(1j*theta)
v = image_radius*np.exp(-1j*theta)
def arrow(a, points, j, color):
    a.annotate("", xy=(points[j+28].real, points[j+28].imag), xytext=(points[j].real, points[j].imag), arrowprops={"arrowstyle": "-|>", "lw": 2, "color": color})
for a in ax:
    a.axhline(0, color="#888888", lw=.65); a.axvline(0, color="#888888", lw=.65)
    a.set_aspect("equal"); a.grid(alpha=.15)
ax[0].plot(lam.real, lam.imag, color=blue, lw=2)
ax[1].plot(v.real, v.imag, color=red, lw=2)
for j in [100, 400, 700, 1000]:
    arrow(ax[0], lam, j, blue); arrow(ax[1], v, j, red)
for idx, color in [(0, green), (300, "#8b3e90")]:
    ax[0].plot(lam[idx].real, lam[idx].imag, "o", color=color)
    ax[1].plot(v[idx].real, v[idx].imag, "o", color=color)
ax[0].annotate(r"$\lambda=3/4$", xy=(.75, 0), xytext=(.18, -.24), fontsize=11, arrowprops={"arrowstyle": "-", "color": green})
ax[0].annotate(r"$\lambda=3i/4$", xy=(0, .75), xytext=(.14, .87), fontsize=11)
ax[1].annotate(r"$v=12/25$", xy=(.48, 0), xytext=(.11, .15), fontsize=11, arrowprops={"arrowstyle": "-", "color": green})
ax[1].annotate(r"$v=-12i/25$", xy=(0, -.48), xytext=(-.68, -.69), fontsize=11)
ax[1].plot(0, 0, "ko", ms=4)
ax[1].annotate(r"holomorphic solution: $(u,v)=(1,0)$", xy=(0, 0), xytext=(-.76, .70), fontsize=10, arrowprops={"arrowstyle": "-", "color": "#444444"})
ax[0].set(xlim=(-1, 1), ylim=(-1, 1), xlabel=r"$\mathrm{Re}\,\lambda$", ylabel=r"$\mathrm{Im}\,\lambda$", title=r"Parameter: $\lambda=(3/4)e^{i\theta}$")
ax[1].set(xlim=(-.85, .85), ylim=(-.85, .85), xlabel=r"$\mathrm{Re}\,v$", ylabel=r"$\mathrm{Im}\,v$", title=r"Least-norm choice: $v=(12/25)e^{-i\theta}$")
fig.suptitle(r"$u+\lambda v=1$: on this circle the least-norm coordinate is $u=16/25$", fontsize=12)
save(fig, "least-norm-choice-and-complex-conjugation")
print(json.dumps({"figures": 2, "formats": ["PNG", "SVG"], "output": str(OUT)}))
