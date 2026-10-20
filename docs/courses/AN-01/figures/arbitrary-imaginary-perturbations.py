"""Exact polynomial and error functions from Lemma 2a, Exercise 10.

GPT-6 Astra (OpenAI). Public domain (CC0).
The plots illustrate the proved identities D6-D7; sampling is not a proof.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "svg.hashsalt": "AN01-arbitrary-imaginary-perturbations",
})
y = np.linspace(-5, 4, 1801)
exact = 54 + 6*y - 8*y*y - y**3
predictor = 54 + 27*y
error = np.abs(-21*y - 8*y*y - y**3)
bound = 11*(1+np.abs(y))*np.abs(y)*(3+np.abs(y))
assert np.all(error <= bound + 1e-9)
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)
a, b = axes
a.plot(y, exact, color="#175d9c", lw=2.5, label="Exact imaginary part")
a.plot(y, predictor, color="#b45b12", ls="--", lw=1.8,
       label="Principal linear predictor")
a.axhline(0, color="#56616b", lw=0.8)
a.scatter([0, 3], [54, -27], color="#175d9c", s=35, zorder=4)
a.annotate("(0, 54)", (0, 54), xytext=(-2.8, 85),
           arrowprops={"arrowstyle": "->", "color": "#175d9c"})
a.annotate("(3, -27)", (3, -27), xytext=(0.2, -105),
           arrowprops={"arrowstyle": "->", "color": "#175d9c"})
a.set(xlabel="Additional imaginary displacement y",
      ylabel="Imaginary part", title="A. Positivity need not persist",
      xlim=(-5, 4), ylim=(-180, 180))
a.legend(loc="upper left", fontsize=10)
nonzero = np.abs(y) > 1e-12
b.plot(y, np.where(nonzero, error, np.nan), color="#175d9c",
       lw=2.5, label="Absolute error")
b.plot(y, np.where(nonzero, bound, np.nan), color="#b45b12",
       ls="--", lw=1.8, label="Proved uniform bound")
b.set(xlabel="Additional imaginary displacement y",
      ylabel="Magnitude (logarithmic scale)",
      title="B. The nonlinear error stays controlled", xlim=(-5, 4))
b.set_yscale("log")
b.legend(loc="upper center", fontsize=10)
for ax in axes:
    ax.grid(alpha=0.18)
fig.suptitle(r"$P(\zeta)=\zeta_1^3-\zeta_2^3-i(\zeta_1^2+\zeta_2^2)$"
             "\n" + r"$\xi=(3,0),\quad t=1,\quad v=(3,0),\quad V=(y,0)$",
             fontsize=15)
fig.text(0.5, -0.025, "Exact functions from Exercise 10; all-vector bounds follow from D6-D7.",
         ha="center", fontsize=10)
out = Path(__file__).resolve().parent
fig.savefig(out/"arbitrary-imaginary-perturbations.png", dpi=160,
            bbox_inches="tight", facecolor="white")
svg = out/"arbitrary-imaginary-perturbations.svg"
fig.savefig(svg, bbox_inches="tight", metadata={"Date": None})
svg.write_text("\n".join(line.rstrip() for line in
               svg.read_text(encoding="utf-8").splitlines())+"\n", encoding="utf-8")
plt.close(fig)
