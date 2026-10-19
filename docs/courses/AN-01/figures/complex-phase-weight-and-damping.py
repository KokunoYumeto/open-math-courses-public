"""Exact functions in Weighted cancellation for complex phases, W16/W21/W22.
Original figure by GPT-6 Astra (OpenAI), CC0. Numerical samples are illustrations,
not proof or numerical verification of the integral theorem.
Run with Python, NumPy and Matplotlib; outputs are beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 13, "svg.fonttype": "none"})
fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.4), constrained_layout=True)
colors = ["#245c92", "#b04912", "#366e44"]
t = np.linspace(0, 9, 901)
for m, color in zip([0, 1, 3], colors):
    maximum = 1.0 if m == 0 else float(m**m * np.exp(-m))
    values = np.exp(-t) if m == 0 else t**m * np.exp(-t) / maximum
    axes[0].plot(t, values, color=color, linewidth=2.4, label=f"$m={m}$")
    axes[0].scatter([m], [1], color=color, s=40, zorder=3)
axes[0].set(title="Damping profiles", xlabel=r"$t=\omega\varepsilon$",
            ylabel=r"$t^m e^{-t}/M_m$", xlim=(-0.15, 9), ylim=(0, 1.16))
axes[0].text(4.2, 1.04, r"Maximum at $t=m$", fontsize=12)
axes[0].legend(loc="upper right", bbox_to_anchor=(1, 0.88))
x = np.linspace(-0.8, 0.8, 801)
for eps, label, color in zip([0, 0.25, 1], ["0", "1/4", "1"], colors):
    axes[1].plot(x, 5*x*x+eps, color=color, linewidth=2.4,
                 label=rf"$\varepsilon={label}$")
    axes[1].scatter([0], [eps], color=color, s=35, zorder=3)
axes[1].set(title=r"Phase $f(x)=i(x^2+\varepsilon)$", xlabel="$x$",
            ylabel=r"$H(x)=5x^2+\varepsilon$", xlim=(-0.8, 0.8), ylim=(-0.15, 4.4))
axes[1].legend(loc="upper center")
for ax in axes:
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Cancellation and damping share the weight "
             r"$H=|\nabla f|^2+\operatorname{Im}f$", fontsize=16)
for ext in ["svg", "png"]:
    fig.savefig(out / f"complex-phase-weight-and-damping.{ext}", dpi=160)
plt.close(fig)
svg = out / "complex-phase-weight-and-damping.svg"
svg.write_text("\n".join(line.rstrip() for line in
                        svg.read_text(encoding="utf-8").splitlines()) + "\n",
               encoding="utf-8", newline="\n")
