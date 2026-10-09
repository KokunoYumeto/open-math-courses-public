"""Exact annular support intervals and norm ratios, NS-FLUID-09 Exercise 5."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = Path(__file__).resolve().parent
fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.3), layout="constrained")
ax = axes[0]
for n in range(1, 9):
    ax.add_patch(Rectangle((n, n-.31), 1, .62, facecolor="#217687", alpha=.76))
    ax.plot([n, n+1], [n, n], "o", markerfacecolor="white",
            markeredgecolor="#174d5a", ms=5)
ax.set(xlim=(.5, 9.5), ylim=(8.7, .3), xticks=range(1, 10), yticks=range(1, 9),
       xlabel=r"Radial coordinate $\log_2(1/|x|)$", ylabel="Term n",
       title="Disjoint containing annuli for vorticity")
ax.grid(axis="x", alpha=.16)
ax.text(.5, -.19, r"$2^{-n-1}\leq |x|\leq 2^{-n}$"+"\n"
        "Vorticity is zero at the endpoints; each interval contains its support.",
        transform=ax.transAxes, ha="center", va="top", fontsize=10)
ax = axes[1]
ns = list(range(1, 9))
ax.plot(ns, ns, "o-", color="#944229", lw=2,
        label=r"$\|\nabla u_N(0)\|_{\rm F}/\|S_0\|_{\rm F}=N$")
ax.plot(ns, [1]*8, "s--", color="#217687", lw=2,
        label=r"$\|\omega_N\|_\infty/M=1$")
ax.set(xlim=(.5, 8.5), ylim=(.3, 8.7), xticks=ns, yticks=ns,
       xlabel="Number of terms N", ylabel="Exact ratio",
       title="Gradient accumulates; curl stays bounded")
ax.grid(alpha=.16)
ax.legend(loc="upper left", fontsize=11, framealpha=.95)
ax.text(.5, -.19, r"$u_N(x)=\sum_{n=1}^N2^{-n}v(2^nx)$"+"\n"
        "Exact spatial fields; no time-dependent singularity is asserted.",
        transform=ax.transAxes, ha="center", va="top", fontsize=10)
fig.suptitle("Compact Euler initial fields: the logarithmic scale", fontsize=15)
fig.savefig(HERE/"euler-frequency-bands.png", dpi=180)
fig.savefig(HERE/"euler-frequency-bands.svg")
plt.close(fig)
