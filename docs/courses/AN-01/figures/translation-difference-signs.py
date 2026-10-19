"""Signed point-mass coefficients; Proposition 1.2 and Solution 11. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).parent
fig, axes = plt.subplots(2, 1, figsize=(9, 6.6), layout="constrained")
panels = [
    ([0, 1], [-1, 1], r"$h\,D_h=\delta_h-\delta_0$",
     r"$D_h\longrightarrow-\delta'_0$"),
    ([-1, 0, 1], [1, -2, 1], r"$h^2 S_h=\delta_{-h}-2\delta_0+\delta_h$",
     r"$S_h\longrightarrow\delta''_0$"),
]
for ax, (xs, ys, title, limit) in zip(axes, panels):
    ax.axhline(0, color="#64748b", linewidth=1)
    for x, y in zip(xs, ys):
        color = "#1564a3" if y > 0 else "#b64430"
        ax.annotate("", (x, y), (x, 0),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.8))
        ax.text(x + .08, y, f"{y:+d}", color=color, va="center", fontsize=13)
    ax.set_xlim(-1.35, 1.65)
    ax.set_ylim(-2.45, 1.55)
    ax.set_xticks([-1, 0, 1], [r"$-h$", "$0$", "$h$"])
    ax.set_yticks([-2, -1, 0, 1])
    ax.set_ylabel("scaled mass coefficient")
    ax.set_title(title + "       " + limit, fontsize=14, pad=12)
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Translations and derivative signs  •  h > 0", fontsize=16)
for ext in ("png", "svg"):
    fig.savefig(out / ("translation-difference-signs." + ext), dpi=160)
svg = out / "translation-difference-signs.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
plt.close(fig)
