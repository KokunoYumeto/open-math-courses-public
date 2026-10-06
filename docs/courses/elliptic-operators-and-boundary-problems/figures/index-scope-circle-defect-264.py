"""Original circle index/sign schematic; U051 IG2, IG3, IG10, IG35, IT3.

Render with Python and Matplotlib. No TeX process is used. The finite window
displays the action of the infinite operator and does not approximate it.
Human convention compared: Denis Perrot, arXiv:1112.1850v1, Sections 4 and 7.
This figure and source are dedicated to the public domain (CC0).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

matplotlib.rcParams.update({"text.usetex": False, "font.family": "DejaVu Sans",
                           "font.size": 14, "svg.hashsalt": "AN03-U051-264"})
out = Path(__file__).resolve().parent
fig = plt.figure(figsize=(15, 12), facecolor="#fbfcff")
fig.suptitle("The circle operator and its exact receiving sign", fontsize=24,
             fontweight="bold", y=.97, color="#15263e")
gs = fig.add_gridspec(3, 2, height_ratios=[1.25, 1.1, .83],
                      hspace=.37, wspace=.18, top=.91, bottom=.115)
ax = fig.add_subplot(gs[0, :]); ax.set_xlim(-4, 4.8); ax.set_ylim(-.8, 2.4)
ax.axis("off")
ax.text(-3.9, 2.18, r"$Q_1=e^{ix}\Pi_++(I-\Pi_+)$", fontsize=21, color="#18365b")
ax.text(4.65, 2.18, r"$\Pi_+:\ k\geq0$", ha="right", fontsize=18)
ax.text(-3.9, 1.8, r"$e_k=(2\pi)^{-1/2}e^{ikx}|dx|^{1/2}$", fontsize=16)
for k in range(-3, 4):
    dest = k if k < 0 else k + 1
    color = "#295d98" if k < 0 else "#17805e"
    ax.add_patch(FancyArrowPatch((k, 1.23), (dest, .27), arrowstyle="-|>",
                                mutation_scale=18, lw=2.0, color=color))
    ax.plot(k, 1.3, "o", color=color, ms=8)
    ax.text(k, 1.45, str(k), ha="center")
for k in range(-3, 5):
    ax.plot(k, .2, "o", color="#c43b39" if k == 0 else "#243c56", ms=8)
    ax.text(k, -.06, str(k), ha="center", color="#c43b39" if k == 0 else "#243c56")
for x in [-3.55, 4.45]:
    ax.text(x, .75, "⋯", ha="center", fontsize=24)
ax.text(4.65, 1.3, "input modes", ha="right", va="bottom", fontsize=13)
ax.text(4.65, -.28, "output modes", ha="right", va="top", fontsize=13)
ax.text(0, -.54, r"retained zero mode in cokernel: $\ker Q_1=0$,   $\mathrm{coker}\,Q_1=\mathrm{span}\{e_0\}$",
        ha="center", fontsize=16, color="#a72a2a")
ax.text(-3.9, -.76, "Finite window of the exact infinite Fourier map; both tails continue.",
        fontsize=12, color="#526177")

for col, sign, label, g in [(0, 1, r"$\xi=+1$: outward orientation $+dx$", r"$g_1=e^{ix}$"),
                            (1, -1, r"$\xi=-1$: outward orientation $-dx$", r"$g_1=1$")]:
    ac = fig.add_subplot(gs[1, col]); ac.set_aspect("equal")
    ac.set_xlim(-1.9, 1.9); ac.set_ylim(-1.65, 1.75); ac.axis("off")
    ac.add_patch(Circle((0, 0), 1, fill=False, lw=2.7,
                       color="#17805e" if sign == 1 else "#295d98"))
    t = np.linspace(.25, 1.14, 60) if sign == 1 else np.linspace(1.14, .25, 60)
    pts = np.column_stack((np.cos(t), np.sin(t)))
    ac.plot(pts[:, 0], pts[:, 1], color="#18365b", lw=4)
    ac.add_patch(FancyArrowPatch(pts[-3], pts[-1], arrowstyle="-|>",
                                 mutation_scale=26, color="#18365b", lw=2))
    ac.text(0, .1, g, ha="center", va="center", fontsize=23)
    ac.text(0, -.32, r"$x\ \mathrm{mod}\ 2\pi$", ha="center", fontsize=14)
    ac.text(0, 1.45, label, ha="center", fontsize=16)
    integral = r"$\frac{1}{2\pi i}\int g_1^{-1}dg_1=+1$" if sign == 1 else r"$\frac{1}{2\pi i}\int g_1^{-1}dg_1=0$"
    ac.text(0, -1.42, integral, ha="center", fontsize=18)

ab = fig.add_subplot(gs[2, :]); ab.axis("off")
ab.text(.5, 1.03, r"$\omega=d\xi\wedge dx$,   $L=\xi\partial_\xi$,   $\iota(L)\omega|_{\xi=\pm1}=\pm dx$",
        ha="center", transform=ab.transAxes, fontsize=17)
rows = [(r"Radul and original odd-character value", r"$c(P,Q_1)=\int_{S^*X}\mathrm{ch}(g_1)=+1$", "#18365b"),
        (r"Actual analytic receiver", r"$\mathrm{ind}\,Q_1=\mathrm{Tr}(Q_1P-PQ_1)=-c(P,Q_1)=-1$", "#a72a2a"),
        (r"Defect of the original positive formula", r"$\mathfrak{d}_{S^1}([g_1])=-1-(+1)=-2$", "#a72a2a")]
for j, (left, right, color) in enumerate(rows):
    y = .69 - .3*j
    ab.text(.01, y, left, transform=ab.transAxes, fontsize=14, color=color)
    ab.text(.44, y, right, transform=ab.transAxes, fontsize=17, color=color)
fig.text(.5, .065, "One-dimensional schematic; complete arbitrary-dimensional proof: IG1–IG36.  Fourier defects: IG2–IG3; splitting: IT3.",
         ha="center", fontsize=12, color="#354d66")
fig.text(.5, .034, "Compared human convention: Denis Perrot, original author TeX, arXiv:1112.1850v1, Sections 4 and 7.  CC0 original figure.",
         ha="center", fontsize=11, color="#354d66")
fig.savefig(out / "index-scope-circle-defect-264.png", dpi=160,
            metadata={"Software": "Matplotlib; original U051 mathematical schematic"})
fig.savefig(out / "index-scope-circle-defect-264.svg", metadata={"Date": None})
plt.close(fig)
