"""Reproduce the finite p=3 Weyl-pair diagram. Original source: CC0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

plt.rcParams.update({"svg.hashsalt": "cyclic-weyl-pair-p3-v1", "font.size": 23})
fig, ax = plt.subplots(figsize=(6, 5.7))
fig.patch.set_facecolor("#fffdf8")
ax.set_facecolor("#fffdf8")
ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-2.1, 1.75)
ax.set_aspect("equal")
ax.axis("off")
points = [(0, 1.0), (-1.15, -0.65), (1.15, -0.65)]
labels = [r"$\xi_0$", r"$\xi_1$", r"$\xi_2$"]
eigenvalues = [r"$u\xi_0=\xi_0$", r"$u\xi_1=\lambda\xi_1$", r"$u\xi_2=\lambda^2\xi_2$"]
for j, ((x, y), label) in enumerate(zip(points, labels)):
    ax.add_patch(Circle((x, y), 0.26, facecolor="#e4f0ef", edgecolor="#145576", lw=1.7))
    ax.text(x, y, label, ha="center", va="center", color="#143f50", fontsize=26)
    ax.text(x, y + (0.4 if j == 0 else -0.48), eigenvalues[j], ha="center", va="center", color="#143f50")
for j in range(3):
    start, end = points[j], points[(j + 1) % 3]
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=20,
                                shrinkA=23, shrinkB=23, lw=2, color="#ab6019"))
    x, y = (start[0] + end[0]) / 2, (start[1] + end[1]) / 2
    ax.text(x + (-0.2 if j == 0 else 0.2 if j == 2 else 0), y + (0.16 if j == 1 else 0.07),
            r"$v$", color="#ab6019", ha="center", fontsize=25)
ax.text(0, -1.51, r"$\lambda=e^{2\pi i/3}$",
        ha="center", va="center", color="#143f50", fontsize=22)
ax.text(0, -1.88, r"$uv=\lambda vu,\quad u^3=v^3=1$",
        ha="center", va="center", color="#143f50", fontsize=22)
fig.tight_layout(pad=0.4)
here = Path(__file__).resolve().parent
fig.savefig(here / "cyclic-weyl-pair.svg", metadata={"Date": None, "Creator": "Course diagram, CC0"})
fig.savefig(here / "cyclic-weyl-pair.png", dpi=170, metadata={"Software": "Course diagram, CC0"})
plt.close(fig)
