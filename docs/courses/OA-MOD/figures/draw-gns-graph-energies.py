"""Reproduce the two energies in OA-MOD-WH, equations (WH.64–65).

Original figure and code: OpenAI GPT-6 Astra, October 2026. CC0.
Mathematical context: Takesaki, Theory of Operator Algebras II,
Exercise VII.2(1), pp. 64–65. The example and its proof are in OA-MOD-WH,
"Closed GNS graphs and the finite-star domain"; the source exercise does
not contain this example. Requires Python and Matplotlib.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    ns = list(range(1, 13))
    energies = [sum((Fraction(1, n * n) for n in range(1, N + 1)), Fraction())
                for N in ns]
    adjoint = [sum(n * n for n in range(1, N + 1)) for N in ns]
    assert all(e < 2 for e in energies)
    assert adjoint == [N * (N + 1) * (2 * N + 1) // 6 for N in ns]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                         "axes.titlesize": 20, "axes.labelsize": 19,
                         "xtick.labelsize": 16, "ytick.labelsize": 16})
    fig, axes = plt.subplots(2, 1, figsize=(8, 8), layout="constrained")
    fig.suptitle("Same matrices, different energies", fontsize=21)
    blue, orange = "#166088", "#a84618"
    axes[0].plot(ns, list(map(float, energies)), "o-", color=blue, linewidth=2.3)
    axes[0].axhline(2, color="#637080", linestyle="--", linewidth=1.5)
    axes[0].text(1.3, 2.04, "Upper bound: 2", fontsize=16, color="#384452")
    axes[0].set(title="GNS energy stays bounded", ylabel=r"$\sum_{n=1}^{N} n^{-2}$",
                ylim=(0, 2.38), yticks=[0, 1, 2])
    axes[1].plot(ns, adjoint, "o-", color=orange, linewidth=2.3)
    axes[1].set(title="Adjoint energy diverges", ylabel=r"$\sum_{n=1}^{N} n^2$",
                xlabel="Number of retained blocks, N", ylim=(0, 700), yticks=[0, 350, 700])
    axes[1].text(1.4, 540, r"$N(N+1)(2N+1)/6$", fontsize=19, color=orange)
    for ax in axes:
        ax.set_xlim(0.65, 12.35)
        ax.set_xticks([1, 4, 8, 12])
        ax.grid(axis="y", color="#d8dee5", linewidth=0.8)
        ax.set_axisbelow(True)
        ax.spines[["right", "top"]].set_visible(False)
    fig.savefig(Path(__file__).with_name("gns-graph-energies.png"), dpi=120,
                metadata={"Title": "GNS and adjoint energies of finite-block truncations",
                          "Author": "OpenAI GPT-6 Astra",
                          "Copyright": "CC0",
                          "Description": "OA-MOD-WH, equations (WH.64–65); N=1,...,12. Different vertical scales."})
    plt.close(fig)


if __name__ == "__main__":
    main()
