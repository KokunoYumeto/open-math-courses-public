"""Reproduce the full quotient curves in U049 ARX39–ARX42."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
a = 1 / 2
b = (1 - a) ** 2
eta = np.linspace(-0.4, 0.4, 1601)
colors = {1: "#176b92", -1: "#aa3f55"}
fig, axes = plt.subplots(1, 3, figsize=(14, 6))
fig.subplots_adjust(left=0.065, right=0.985, top=0.78, bottom=0.32, wspace=0.3)
for kappa in (1, -1):
    q = a * (kappa + 1j * np.abs(eta)) + 1j * (1 - a) ** 2 * np.sqrt(eta ** 2 + kappa ** 2)
    h = (kappa + 1j * np.abs(eta)) ** 2
    d = h * q ** (-1)
    real_ax = axes[0 if kappa == 1 else 1]
    real_ax.plot(eta, d.real, color=colors[kappa], lw=2.3,
                 label="Full quotient")
    tangent_eta = np.linspace(-0.13, 0.13, 131)
    real_ax.plot(tangent_eta, kappa * 1.6 + kappa * 8 / 25 * np.abs(tangent_eta),
                 color="#867149", lw=1.5, linestyle="--",
                 label="One-sided tangents at zero")
    axes[2].plot(eta, d.imag, color=colors[kappa], lw=2.3,
                 label=rf"$\kappa={kappa}$",
                 linestyle="-" if kappa == 1 else "--")
for ax, title, ordinate in zip(axes,
                              (r"Real part: $\kappa=1$",
                               r"Real part: $\kappa=-1$",
                               "Imaginary part: both axes"),
                              (r"$\operatorname{Re}d(\eta,1)$",
                               r"$\operatorname{Re}d(\eta,-1)$",
                               r"$\operatorname{Im}d(\eta,\kappa)$")):
    ax.set_title(title, fontsize=12, weight="bold", pad=12)
    ax.set_xlabel(r"Tangential covariable $\eta$", fontsize=11)
    ax.set_ylabel(ordinate, fontsize=12)
    ax.axvline(0, color="#7b8790", lw=1, alpha=0.65)
    ax.grid(alpha=0.18)
    ax.legend(loc="best", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.suptitle(r"Unequal derivative jumps at the two normal axes: "
             r"$a=\frac{1}{2},\ b=(1-a)^2=\frac{1}{4}$", fontsize=15, weight="bold")
fig.text(0.5, 0.16,
    r"$d=hq^{-1},\quad h=(\kappa+i|\eta|)^2,\quad "
    r"q=a(\kappa+i|\eta|)+i(1-a)^2\sqrt{\eta^2+\kappa^2}$" + "\n" +
    r"$j_+(d)=\frac{16+112i}{25},\quad "
    r"j_-(d)=\frac{-16+112i}{25},\quad "
    r"\mathcal{J}(d)=j_+(d)-j_-(d)=\frac{32}{25}\neq 0$" + "\n" +
    "Curves are numerical samples of the full formula. "
    "Exact proof: U049 ARX39–ARX42.",
    fontsize=11, ha="center", va="center", linespacing=1.8)
fig.savefig(out / "u049-quotient-defect-264.png", dpi=180, bbox_inches="tight",
            metadata={"Title": "U049 quotient derivative defect",
                      "Description": "Full quotient sample and exact derivative jumps; ARX39–ARX42"})
fig.savefig(out / "u049-quotient-defect-264.svg", bbox_inches="tight",
            metadata={"Title": "U049 quotient derivative defect",
                      "Description": "Full quotient sample and exact derivative jumps; ARX39–ARX42"})
plt.close(fig)
