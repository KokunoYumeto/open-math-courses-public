"""Exact n=1, r=1 annular example for G16--G17. CC0; no external artwork."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "svg.fonttype": "none"})
fig, (left, right) = plt.subplots(1, 2, figsize=(11.5, 4.5))
colors = ["#007c91", "#d26e26", "#7556a0"]
styles = ["-", "--", ":"]
for R, color, style in zip([2, 4, 8], colors, styles):
    xi = np.linspace(R, 2 * R, 251)
    left.plot(xi, xi, color=color, ls=style, lw=2.5, label=f"R = {R}")
    eta = xi / R
    right.plot(eta, xi / R, color=color, ls=style, lw=3.0, label=f"R = {R}")
left.set(xlabel=r"frequency $\xi$", ylabel=r"amplitude $b(\xi)=\xi$",
         title="Different annuli, the same symbol", xlim=(0, 17), ylim=(0, 17))
left.text(.04, .90, r"$\int_R^{2R}|b(\xi)|^2\,d\xi=7R^3/3$",
          transform=left.transAxes, fontsize=13)
right.set(xlabel=r"rescaled frequency $\eta=\xi/R$",
          ylabel=r"$R^{-1}b(R\eta)$", title="All three rescaled curves coincide",
          xlim=(.9, 2.1), ylim=(.8, 2.3))
right.text(.06, .92, r"$\int_1^2|\eta|^2\,d\eta=7/3$",
           transform=right.transAxes, fontsize=13)
for ax in [left, right]:
    ax.grid(alpha=.18)
    ax.legend(loc="lower right")
fig.tight_layout(pad=1.6)
fig.savefig(out / "annular-rescaling.svg")
fig.savefig(out / "annular-rescaling.png", dpi=150)
plt.close(fig)
