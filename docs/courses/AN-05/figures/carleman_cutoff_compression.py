"""Exact local cutoff jets illustrating (R24)--(R25), not sampled operators."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_suffix(".png"))
    args = parser.parse_args()
    x = np.linspace(0.25, 0.75, 501)
    chi = 1 - x*x
    chi_prime = -2*x
    chi_second = -2*np.ones_like(x)
    repair = (chi_prime**2 - chi*chi_second)/2
    assert np.max(np.abs(repair - (1+x*x))) < 1e-14
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.24, top=0.80,
                        wspace=0.20)
    colors = ["#2c7fb8", "#f28e2b", "#a51d2d"]
    for tau, color, label in zip([1, 4, 9], colors,
                                  [r"$\tau=1$",r"$\tau=4$",r"$\tau=9$"]):
        missing = tau*chi*chi_prime
        axes[0].plot(x, missing, lw=2.5, color=color,
                     label=label)
    axes[0].set_title("Cutoff inserted into the symbol\n"
                      r"Missing term $\tau\chi\chi'$ in (R24)")
    axes[0].set_ylabel("Exact Weyl-symbol correction")
    axes[0].legend(frameon=False)
    axes[1].plot(x, repair, lw=3, color="#217a58")
    axes[1].set_title("Actual symmetric operator compression\n"
                      r"$(\chi'^2-\chi\chi'')/2=1+x^2$ in (R25)")
    axes[1].text(0.5, 1.08, "Same curve for every parameter",
                 ha="center", color="#217a58")
    for ax in axes:
        ax.set_xlabel(r"Local coordinate $x$")
        ax.set_xlim(0.25, 0.75)
        ax.grid(alpha=0.2)
    fig.suptitle(r"$n=m=1,\quad p=\xi,\quad\phi=x,\quad"
                 r"q_\tau=\xi+i\tau,\quad\chi=1-x^2$ on $[1/4,3/4]$",
                 fontsize=14)
    fig.text(0.5, 0.035,
             "Local jets of a smooth compact cutoff; these formulas hold before any numerical sampling.\n"
             "Source: Hörmander IV, Theorem 28.2.3, printed p. 237; receiving proof (R23)–(R25).",
             ha="center", fontsize=10)
    fig.savefig(args.output, dpi=180, bbox_inches="tight",
                metadata={"Title": "Exact cutoff correction and symmetric compression",
                          "Description": "Exact cutoff correction and its cancellation by symmetric compression",
                          "License": "CC0-1.0",
                          "Software": "Matplotlib"})
    plt.close(fig)
    print(args.output.resolve())


if __name__ == "__main__":
    main()
