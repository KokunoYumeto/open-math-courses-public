"""Exact functional diagram for SC2--SC6 and SC19--SC24."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

matplotlib.rcParams.update({"svg.fonttype": "path", "font.family": "DejaVu Sans"})
out = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(14, 8), dpi=140)
fig.patch.set_facecolor("#ffffff")
ax.set(xlim=(0, 14), ylim=(0, 8))
ax.axis("off")

def box(x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                 facecolor=color, edgecolor="#34445c", linewidth=1.4))
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=14,
            linespacing=1.65, color="#172a45")

def arrow(a, b, text, offset=(0, 0)):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=18,
                 linewidth=1.7, color="#34445c"))
    ax.text((a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1], text,
            ha="center", va="center", fontsize=13, color="#172a45",
            bbox=dict(facecolor="white", edgecolor="none", pad=3))

ax.text(7, 7.55, "Schur's bound on the original measure spaces", ha="center",
        fontsize=22, weight="bold", color="#172a45")
ax.text(7, 6.95, r"$I=[0,1],\quad K(x,y)=1_N(x+y),\quad A=1,\quad B=0$",
        ha="center", fontsize=18, color="#172a45")
box(.45, 3.55, 3.1, 1.75,
    "Original input\n" + r"$u=1\in L^2(I,\nu)$" + "\n" + r"$\|u\|_2=1$", "#e9f2fc")
box(8.4, 4.7, 4.9, 1.45,
    "Raw output: constant one\n" + r"$\int_I |1|^2\,d\mu=\infty$", "#fff0e6")
box(8.4, 1.7, 4.9, 1.45,
    "Canonical output: zero\n" + r"$T_Ku=0\in L^2(I,\mu)=\{0\}$", "#e7f4ef")
arrow((3.7, 4.9), (8.2, 5.42), "Raw section integral", (0, .5))
arrow((3.7, 3.75), (8.2, 2.45), r"$T_K$ from the exact pairings", (-.1, -.45))
arrow((10.85, 4.5), (10.85, 3.35), r"$P_\mu:F_\mu/N_\mu\ \longrightarrow\ L^2(\mu)$", (-3.2, -.05))
ax.text(10.85, 3.88, r"$[1]=[0]$", fontsize=14, ha="center", va="center",
        bbox=dict(facecolor="white", edgecolor="none", pad=2))
ax.text(7, .96, "Every finite-measure output test is zero; here " +
        r"$F_\mu=N_\mu$" + ".", ha="center", fontsize=14, color="#172a45")
ax.text(7, .48, "N is Borel and meager, with Lebesgue-null complement. " +
        "The arrows show exact maps, not samples of N.", ha="center",
        fontsize=12, color="#34445c")
fig.savefig(out/"schur_arbitrary_measure.png", dpi=140, facecolor="white")
fig.savefig(out/"schur_arbitrary_measure.svg", facecolor="white")
plt.close(fig)
