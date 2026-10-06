"""Original CC0 illustration of sharp Carleman energy and packet scales.

Exact model: P=D_x, phi_+(x)=x^2/2, phi_-(x)=-x^2/2.
Source: Hormander IV, printed 235--236; proof locators N16, N21,
N32, N34, N42--N44 and N47--N48 in ../src/general-carleman-estimates-and-real-tangent-necessity.md.
This plots exact formulas; it is not a numerical validation of the theorem.
"""

from pathlib import Path
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14,
                     "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(16.2, 6.7))
fig.subplots_adjust(left=.05, right=.988, bottom=.17, top=.81, wspace=.24)
grid = fig.add_gridspec(1, 3, width_ratios=(1, 1, 1.7))
ax0 = fig.add_subplot(grid[0, 0])
ax1 = fig.add_subplot(grid[0, 1])
ax2 = fig.add_subplot(grid[0, 2])

x = np.linspace(-2.1, 2.1, 600)
ax0.plot(x, x*x/2, color="#2166ac", lw=2.8,
         label=r"$\phi_+(x)=x^2/2$")
ax0.plot(x, -x*x/2, color="#b2182b", lw=2.8,
         label=r"$\phi_-(x)=-x^2/2$")
ax0.axhline(0, color="0.75", lw=.8)
ax0.axvline(0, color="0.75", lw=.8)
ax0.set(xlabel=r"$x$", ylabel=r"$\phi(x)$",
        title="Hessian sign at the characteristic")
ax0.legend(loc="upper center", fontsize=11)
ax0.text(.04, .08, r"$q_t(0,0)=0$"+"\n"+
         r"$c_t(0,0)=+2t$ or $-2t$", transform=ax0.transAxes,
         fontsize=12, bbox={"facecolor":"white", "alpha":.9,
                           "edgecolor":"0.85"})

g = np.pi**(-.25)*np.exp(-x*x/2)
ax1.plot(x, g, color="#4d4d4d", lw=2.8)
ax1.fill_between(x, 0, g, color="#d9d9d9", alpha=.45)
ax1.set(xlabel=r"$x$", ylabel=r"$v(x)$", ylim=(0, .87),
        title="The same normalized Gaussian")
ax1.text(.5, .94, r"$v=\pi^{-1/4}e^{-x^2/2}$", ha="center",
         transform=ax1.transAxes, fontsize=14)
ax1.text(.04, .35, r"$(D-i x)v=0$"+"\n\n"+
         r"$\|(D+i x)v\|^2=2$"+"\n"+
         r"$\|(D-i x)v\|^2=0$", transform=ax1.transAxes,
         fontsize=13, bbox={"facecolor":"white", "alpha":.9,
                           "edgecolor":"0.85"})

ax2.axis("off")
ax2.set_title("Exact scales and squared-norm powers", pad=15)
rows = [
    ["Complex packet\nN18--N23", r"$\lambda^{-1/2}$",
     r"$\sim C\lambda^{2m-1-n/2}$", r"$O(\lambda^{2m-1-n/2})$"],
    ["Real first-jet obstruction\nN29--N34", r"$\lambda^{-1}$",
     r"$\sim C\lambda^{4m-3-n}$", r"$O(\lambda^{4m-4-n})$"],
    ["Negative bracket; normalized\nN37--N44", r"$\lambda^{-1/2}$",
     r"$\sim C\lambda^{2m-1}$", r"$O(\lambda^{2m-2})$"],
]
table = ax2.table(cellText=rows,
                  colLabels=["Family", "Scale", r"$M_\lambda$",
                             r"$\|e^{\lambda\phi}Pu\|^2$"],
                  colWidths=[.40, .16, .23, .25],
                  cellLoc="center", bbox=[-.015, .18, 1.04, .72])
table.auto_set_font_size(False)
table.set_fontsize(10.6)
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor("#bbbbbb")
    cell.set_linewidth(.7)
    if row == 0:
        cell.set_facecolor("#e6eef6")
        cell.set_text_props(weight="bold")
    elif row % 2:
        cell.set_facecolor("#f5f5f5")
ax2.text(.5, .065, "Real first-jet test: one-power contradiction.\n"
         "Negative-bracket family: RHS / LHS = O(1/λ).",
         transform=ax2.transAxes, ha="center", va="center",
         fontsize=12)
fig.suptitle("Carleman necessity: exact linear sign model and packet mechanisms",
             fontsize=17)
fig.text(.5, .035,
         "Hörmander IV, printed 235–236. Receiving proof N16, N21, N32–N34, "
         "N42–N48. The curves are exact formulas; compact cutoffs and tails are proved in the text.",
         ha="center", fontsize=10)
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, default=HERE / "general-carleman-necessity-packets.png")
out = parser.parse_args().output
fig.savefig(out, dpi=180, facecolor="white",
            metadata={"Title":"Sharp Carleman energy and packet scales",
                      "Description":"Exact sign models and proved packet powers",
                      "License":"CC0-1.0","Software":"matplotlib"})
plt.close(fig)
print(out)
