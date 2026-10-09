"""Exact finite reflection and physical cup gaps. Independently authored CC0-1.0.

Run with Python, NumPy and Matplotlib; writes PNG and editable SVG beside this file.
The formula is MCF.11. The PG datum is separate from the weighted-spin curve.
Human mathematical sources: Sorin Popa, Classification of amenable subfactors
of type II; Mihai Pimsner and Sorin Popa, Entropy and index for subfactors.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

HERE = Path(__file__).resolve().parent
BLUE, TEAL, RED, INK = "#22599c", "#13776f", "#a84032", "#172a3a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans", "svg.fonttype": "none"})
fig = plt.figure(figsize=(14.0, 10.6), facecolor="white")
gs = fig.add_gridspec(2, 2, height_ratios=(1.48, 1), width_ratios=(2.4, 1),
                     hspace=0.30, wspace=0.30, left=0.07, right=0.95,
                     top=0.90, bottom=0.13)
fig.suptitle("Finite reflection changes the trace and the cup", x=0.07,
             ha="left", y=0.975, fontsize=23, color=INK, weight="bold")
fig.text(0.07, 0.937, "Exact maps in prescribed finite factors; all distances use the physical factor trace",
         fontsize=12.5, color=INK)
ax = fig.add_subplot(gs[0, :]); ax.set_axis_off()
ax.set_xlim(0, 1); ax.set_ylim(0, 1)

def box(x, y, w, h, title, content, edge):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.018",
                      facecolor="#f3f7fb", edgecolor=edge, linewidth=1.5)
    ax.add_patch(p)
    ax.text(x + w/2, y + h - .046, title, ha="center", va="top",
            fontsize=13, color=edge, weight="bold")
    ax.text(x + w/2, y + .052, content, ha="center", va="bottom",
            fontsize=15.0, color=INK, linespacing=1.55)

box(.015, .56, .35, .33, "Lower finite pair",
    r"$F_{m,i}=M_{-m}'\cap M_{-i+1}$" + "\n" +
    r"$G_{m,i}=M_{-m}'\cap M_{-i}\ \subset F_{m,i}$", BLUE)
box(.635, .56, .35, .33, "Upper finite pair",
    r"$U_{m,i}=M_{i-1}'\cap M_m$" + "\n" +
    r"$V_{m,i}=M_i'\cap M_m\ \subset U_{m,i}$", TEAL)
ax.add_patch(FancyArrowPatch((.385, .705), (.615, .705), arrowstyle="-|>",
                            mutation_scale=20, linewidth=2.0, color=INK))
ax.text(.5, .765, r"$\Theta(x)=Jx^*J$", ha="center", color=INK, fontsize=16)
ax.text(.5, .644, "linear *-anti-isomorphism", ha="center", fontsize=11.5, color=INK)
ax.text(.5, .517, r"$\tau_{M_m}(\Theta(x))=\tau_{M_{-i+1}}(\zeta_{m,i}x)$",
        ha="center", fontsize=17, color=INK)
ax.text(.5, .451, r"$\zeta_{m,i}=\kappa_{M_{-m},\,M_{-i+1}}\in Z(F_{m,i}),\quad \tau(\zeta_{m,i})=1$",
        ha="center", fontsize=14.0, color=INK)
ax.axhline(.385, color="#c8d4df", linewidth=1)
ax.text(.04, .318, "Canonical cup image", fontsize=13, color=INK, weight="bold")
ax.text(.5, .267, r"$g_i^-\ \longmapsto\ g_i^+=(\kappa_i^+)^{1/2}e_i(\kappa_i^+)^{1/2}$",
        ha="center", fontsize=17, color=TEAL)
ax.text(.5, .174, r"$\|g_i^+-e_i\|_2^2=2d^{-1}(1-a^2),\qquad a=\tau(\sqrt{\kappa})$",
        ha="center", fontsize=15.5, color=RED)
ax.text(.5, .078, r"Two-step blocking: $\|\widetilde Q_i-Q_{2i-2}\|_2^2=2d^{-2}(1-a^4)$",
        ha="center", fontsize=16, color=RED)
ax.text(.985, .984, "MCF.14–MCF.18", ha="right", fontsize=11, color="#506879")

curve = fig.add_subplot(gs[1, 0])
p = np.linspace(.005, .995, 700); pq = p*(1-p)
distance = 2*pq**2*(1-16*pq**2)
curve.plot(p, distance, color=BLUE, linewidth=2.7)
curve.set_xlim(0, 1); curve.set_ylim(-.002, .039)
curve.set_xticks([0, .25, .5, .75, 1]); curve.set_yticks([0, .01, .02, .03])
curve.set_xlabel(r"Weighted-spin parameter $p$; $q=1-p$")
curve.set_ylabel("Two-step physical distance squared")
curve.set_title("Weighted spin", loc="left", fontsize=15, weight="bold", color=INK)
curve.text(.50, .037, r"$d=(pq)^{-1},\quad a=2\sqrt{pq}$", ha="center", fontsize=13)
curve.grid(axis="y", alpha=.25)
curve.spines[["top", "right"]].set_visible(False)
spin_gap = 63/2048
curve.scatter([.25, .5], [spin_gap, 0], s=64, color=[RED, TEAL], zorder=4)
curve.annotate(r"$p=1/4:\ 63/2048$", (.25, spin_gap), xytext=(.025, .019),
               arrowprops={"arrowstyle":"->", "color":RED}, fontsize=12, color=RED)
curve.annotate(r"$p=1/2:\ 0$", (.5, 0), xytext=(.58, .007),
               arrowprops={"arrowstyle":"->", "color":TEAL}, fontsize=12, color=TEAL)
fig.text(.378, .055, r"$2p^2q^2\left(1-16p^2q^2\right)$", ha="center", fontsize=13.5)

pg = fig.add_subplot(gs[1, 1]); pg.set_axis_off()
pg.set_xlim(0, 1); pg.set_ylim(0, 1)
pg.add_patch(FancyBboxPatch((.03, .025), .94, .95,
                          boxstyle="round,pad=0.016,rounding_size=.025",
                          facecolor="#f3f7fb", edgecolor="#c8d4df"))
pg.text(.10, .88, "PG: separate actual example", fontsize=13.5, weight="bold", color=INK)
pg.text(.10, .74, r"$d=10,\qquad a^2=9/10$", fontsize=16, color=INK)
pg.text(.10, .61, "One-step distance squared", fontsize=11.8, color=INK)
pg.text(.10, .50, r"$1/50$", fontsize=23, color=RED)
pg.text(.10, .34, "Two-step distance squared", fontsize=11.8, color=INK)
pg.text(.10, .21, r"$19/5000$", fontsize=23, color=RED)
pg.text(.10, .07, "Independent of comparison depth", fontsize=10.7, color=INK)
fig.text(.07, .022, "Finite formulas: MCF.9–MCF.19. Weighted-spin curve: MCF.11. PG value: the exact index-ten construction.",
         fontsize=10.5, color="#506879")
fig.savefig(HERE/"modified-cup-trace-boundary-v26.png", dpi=170, facecolor="white")
fig.savefig(HERE/"modified-cup-trace-boundary-v26.svg", facecolor="white")
plt.close(fig)
print("Wrote modified-cup-trace-boundary-v26.png and modified-cup-trace-boundary-v26.svg")
