"""Figure 22.5: exact normalized lattice for y^2=x^3-x (Example 22.74)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans"})
fig, ax = plt.subplots(figsize=(10.6, 7.0), facecolor="white")
fig.subplots_adjust(left=0.08, right=0.69, bottom=0.13, top=0.86)
xy = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
ax.scatter(*zip(*xy), s=36, color="#64748b", zorder=3)
ax.axhline(0, color="#94a3b8", lw=1)
ax.axvline(0, color="#94a3b8", lw=1)
ax.fill([0, 1, 1, 0], [0, 0, 1, 1], color="#dbeafe", alpha=.75)
for endpoint, color in [((1, 0), "#1d4ed8"), ((0, 1), "#b45309")]:
    ax.annotate("", endpoint, (0, 0),
                arrowprops={"arrowstyle": "-|>", "lw": 3, "color": color,
                            "mutation_scale": 19}, zorder=5)
ax.text(1.12, -.2, r"$1=\Omega/\Omega$", color="#1d4ed8", fontsize=13)
ax.text(.12, 1.14, r"$i=(i\Omega)/\Omega$", color="#b45309", fontsize=13)
theta = np.linspace(0, np.pi/2, 120)
ax.plot(.65*np.cos(theta), .65*np.sin(theta), color="#047857", lw=2)
ax.annotate("", (0, .65), (.07, .646),
            arrowprops={"arrowstyle": "-|>", "color": "#047857", "lw": 2})
ax.text(.42, .5, r"$\times i$", color="#047857", fontsize=13)
ax.set(xlim=(-2.45, 2.45), ylim=(-2.45, 2.45), aspect="equal",
       xticks=range(-2, 3), yticks=range(-2, 3),
       xlabel=r"$\operatorname{Re}(z/\Omega)$",
       ylabel=r"$\operatorname{Im}(z/\Omega)$")
ax.grid(color="#e2e8f0", lw=.7)
for spine in ax.spines.values():
    spine.set_color("#cbd5e1")
fig.suptitle("A square lattice and its holomorphic periods",
             x=.49, y=.96, fontsize=18, weight="bold")
fig.text(.73, .77, r"$E:\ y^2=x^3-x$", fontsize=16)
fig.text(.73, .67, r"$\Lambda_E=\Omega\,\mathbf{Z}[i]$", fontsize=16)
fig.text(.73, .56, "Real lattice rank: 2", fontsize=13)
fig.text(.73, .47, "Algebraic relation", fontsize=13)
fig.text(.73, .41, r"$-i\,\Omega+(i\Omega)=0$", fontsize=15)
fig.text(.73, .29, r"$\mathcal{P}_{\rm hol}(E)"
                      r"=\overline{\mathbf{Q}}\,\Omega$", fontsize=16)
fig.text(.73, .21, "Period-space dimension: 1", fontsize=12)
fig.text(.08, .035, "Normalized coordinates only; no numerical value of "
                   r"$\Omega$ is assumed.  Example 22.74.", fontsize=11,
         color="#475569")
dest = Path(__file__).with_suffix(".png")
fig.savefig(dest, dpi=180, facecolor="white")
plt.close(fig)
print(dest)
