"""Figure22.7: exact paths and matrix for Exercise22.100."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
                     "font.size": 12})
fig, ax = plt.subplots(figsize=(11.5, 7.4), facecolor="white")
ax.set(xlim=(0, 11.5), ylim=(0, 7.4))
ax.axis("off")
ax.text(5.75, 6.95, "A closed loop and two algebraic endpoints",
        ha="center", fontsize=20, weight="bold")
ax.text(5.75, 6.43, r"$E(M)=\mathbf{G}_m\times\mathbf{G}_a^2$",
        ha="center", fontsize=18)
columns = [(4, r"$\gamma_0(t)=(e^{2\pi it},0,0)$", "closed"),
           (6.8, r"$\gamma_2(t)=(2^t,t,0)$", "ends at (2, 1, 0)"),
           (9.6, r"$\gamma_3(t)=(3^t,0,t)$", "ends at (3, 0, 1)")]
for x, path, endpoint in columns:
    ax.text(x, 5.69, path, ha="center", fontsize=14)
    ax.text(x, 5.27, endpoint, ha="center", fontsize=11, color="#475569")
row_labels = [r"$dx/x$", r"$dy_1$", r"$dy_2$"]
entries = [[r"$2\pi i$", r"$\log 2$", r"$\log 3$"],
           ["0", "1", "0"], ["0", "0", "1"]]
for i, label in enumerate(row_labels):
    y = 4.4-i*.91
    ax.text(1.2, y, label, ha="center", va="center", fontsize=19)
    for j, (x, _, _) in enumerate(columns):
        val = entries[i][j]
        color = "#eff6ff" if i == 0 else ("#f0fdf4" if val == "1" else "#f8fafc")
        ax.add_patch(Rectangle((x-1.26, y-.39), 2.52, .78,
                               facecolor=color, edgecolor="#cbd5e1"))
        ax.text(x, y, val, ha="center", va="center", fontsize=21,
                color="#64748b" if val == "0" else "#0f172a")
ax.text(1.2, 5.28, "forms", ha="center", color="#475569")
ax.text(5.75, 1.48, r"$\operatorname{span}_k\{1,\,2\pi i,\,\log2,\,\log3\}$ has dimension 4",
        ha="center", fontsize=17)
ax.text(5.75, .89, "Nine entries • four zero relations • one equality between the unit entries",
        ha="center", fontsize=12, color="#334155")
ax.text(5.75, .35, r"Exact paths for $0\leq t\leq1$.  Exercise 22.100; independence from Theorem 22.72.",
        ha="center", fontsize=10, color="#475569")
fig.subplots_adjust(left=.025, right=.975, top=.98, bottom=.02)
dest = Path(__file__).with_suffix(".png")
fig.savefig(dest, dpi=180, facecolor="white")
plt.close(fig)
print(dest)
