"""Figure 10.25: the proved elementary lcm recurrence. CC0.

Original figure: OpenAI Codex, GPT-6.1 Sol, Ultra effort.
Human mathematical method and interval choices: N. Costa Pereira (1989),
free publisher full text cited in TR-BAKER-10 Section 37.
"""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import chebyshev_certificate as cert

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 10, "axes.titlesize": 12,
                     "axes.labelsize": 10, "figure.facecolor": "#fafbf9"})
fig, axes = plt.subplots(1, 3, figsize=(15, 5),
                         gridspec_kw={"width_ratios": [1.3, 1.2, 0.8]})
colors = {1: "#217a87", 2: "#a45435", 3: "#785f97"}
n = np.arange(901)
axes[0].step(n, [cert.floor_weight(int(k)) for k in n], where="post",
             color="#344451", lw=0.9)
for s, pairs in cert.UPPER_INTERVALS.items():
    for b, c in pairs:
        axes[0].plot([b, c], [s - 0.08] * 2, color=colors[s], lw=4)
    axes[0].plot([], [], color=colors[s], lw=4, label=f"Selected F >= {s}")
for s, a in {1: 66, 2: 17, 3: 19, 4: 439, 0: 877}.items():
    axes[0].axvline(a, color="#87929a", ls=":", lw=0.7)
axes[0].set(xlim=(0, 900), ylim=(-1.3, 4.6), xlabel="Integer n",
            ylabel="F(n)", title="Actual floor combination and interval levels")
axes[0].legend(loc="lower left", fontsize=8)
axes[0].text(0.97, 0.97, "Cutoffs: 17, 19, 66, 439, 877",
             transform=axes[0].transAxes, ha="right", va="top", fontsize=8)

lo, hi, _, _ = cert.prime_power_intervals(1200)
mass_lo, mass_hi = 0, 0
values = []
for k in range(1, 1201):
    mass_lo += lo[k]
    mass_hi += hi[k]
    values.append((mass_lo + mass_hi) / (2 * cert.Q * k))
axes[1].plot(np.arange(1, 1201), values, color="#217a87", lw=0.7)
axes[1].axhline(27 / 26, color="#a45435", ls="--", lw=1,
                label="27/26, for x >= 114")
axes[1].axhline(107 / 103, color="#785f97", ls=":", lw=1,
                label="107/103, for all x > 0")
axes[1].scatter([113], [values[112]], color="#344451", s=24, zorder=5)
axes[1].annotate("Global maximum at 113", (113, values[112]),
                 xytext=(330, 1.061), arrowprops={"arrowstyle": "->", "lw": 0.8},
                 fontsize=9)
axes[1].set(xlim=(1, 1200), ylim=(0.79, 1.09), xlabel="Integer n",
            ylabel="psi(n) / n", title="Prime-power mass; proved infinite bound")
axes[1].legend(loc="lower right", fontsize=8)

margins = [Fraction(6731, 26000000), Fraction(11523, 26000000)]
axes[2].bar([0, 1], [float(m) * 10**4 for m in margins],
            color=["#217a87", "#a45435"], width=0.55)
axes[2].set(xticks=[0, 1], xticklabels=["Upper recurrence", "Lower recurrence"],
            ylim=(0, 5.6), ylabel="Certified positive margin, times 10^4",
            title="Both induction comparisons are strict")
axes[2].tick_params(axis="x", labelrotation=18)
for k, m in enumerate(margins):
    axes[2].text(k, float(m) * 10**4 + 0.13, str(m),
                 ha="center", fontsize=8)
axes[2].text(0.5, 0.94, "Factorial error <= 9/40000\nfor every x >= 1,000,000",
             transform=axes[2].transAxes, ha="center", va="top", fontsize=8)
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.16)
fig.suptitle("A complete elementary certificate for log lcm(1,...,k) < (107/103)k",
             fontsize=15, y=1.015)
fig.tight_layout()
fig.savefig(HERE / "chebyshev-recurrence.png", dpi=180, bbox_inches="tight")
plt.close(fig)
