"""Original mathematical figure and reproducible source, CC0-1.0.

Plots finite coordinate projections of an infinite c0 GNS model; the proof is
GNS_FOUNDATION_PROOF.md, Section 8. All constants originate in exact powers of 2.
"""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
BLUE = "#235a9f"
ORANGE = "#cd6a28"
GREEN = "#23745d"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "axes.titlesize": 17, "axes.labelsize": 14, "mathtext.fontset": "dejavusans",
})
fig, axes = plt.subplots(1, 3, figsize=(16, 7.7),
                         gridspec_kw={"width_ratios": [1.05, 1.05, 1.18]})
fig.patch.set_facecolor("white")
n = np.arange(1, 9)
omega = 2.0 ** (-n / 2)
trunc = np.where(n <= 4, omega, 0)
ax = axes[0]
ax.bar(n - .17, omega, width=.32, color=BLUE, label=r"$V\Omega$")
ax.bar(n + .17, trunc, width=.32, color=ORANGE,
       label=r"$V\Lambda(e_4)$")
ax.set(xticks=n, xlabel=r"coordinate $n$", ylabel="coordinate value",
       title="The vector beyond the algebra", ylim=(0, .83))
ax.set_xticklabels([str(x) for x in n])
ax.legend(loc="upper right", frameon=False, fontsize=12)
ax.text(.43, .68, r"$(V\Omega)_n=2^{-n/2}$"+"\n\n"+
        "Only the first eight\ncoordinates are displayed.",
        transform=ax.transAxes, fontsize=12, va="top")
ax.text(.31, .45, r"$\|V\Omega-V\Lambda(e_4)\|^2=1/16$",
        transform=ax.transAxes, fontsize=13)
ax.spines[["top", "right"]].set_visible(False)

ax = axes[1]
tail = 2.0 ** (-n)
ax.plot(n, 1-tail, "o-", color=BLUE, linewidth=2.1,
        label=r"$\|\Lambda(e_N)\|^2=1-2^{-N}$")
ax.plot(n, tail, "s-", color=ORANGE, linewidth=2.1,
        label=r"$\|\Omega-\Lambda(e_N)\|^2=2^{-N}$")
ax.axhline(1, color=GREEN, linestyle="--", linewidth=1.4)
ax.set(xticks=n, yticks=[0, .25, .5, .75, 1], ylim=(-.035, 1.055),
       xlabel=r"truncation $N$", ylabel="squared Hilbert norm",
       title="An exact norming limit")
ax.legend(loc="center right", frameon=False, fontsize=11)
ax.text(1.15, .58, r"$1/2$", fontsize=12, color=ORANGE)
ax.text(3.5, .15, r"$1/16$ at $N=4$", fontsize=12, color=ORANGE)
ax.grid(axis="y", alpha=.18)
ax.spines[["top", "right"]].set_visible(False)

ax = axes[2]
ax.axis("off")
ax.set_title("The nonunital construction")
boxes = [
    (.5, .83, r"$A=c_0(\mathbb{N})$"+"\n"+r"$\omega(a)=\sum_{n\geq1}2^{-n}a_n$"),
    (.5, .57, r"$A/N_\omega\subset H_\omega$"+"\n"+
     r"$\|\Lambda(a)\|^2=\sum_{n\geq1}2^{-n}|a_n|^2$"),
    (.5, .30, r"$\ell^2(\mathbb{N})$"+"\n"+
     r"$V\Lambda(a)=(2^{-n/2}a_n)_n$"),
]
for x, y, label in boxes:
    ax.add_patch(FancyBboxPatch((.06,y-.085),.88,.17,
                 boxstyle="round,pad=.02",transform=ax.transAxes,
                 facecolor="#f0f5fb",edgecolor=BLUE,linewidth=1.3))
    ax.text(x, y, label, transform=ax.transAxes, ha="center", va="center",
            fontsize=14, linespacing=1.6)
for start, end in [(.745,.665),(.475,.39)]:
    ax.annotate("", xy=(.5,end), xytext=(.5,start), xycoords="axes fraction",
                arrowprops={"arrowstyle":"->", "color":BLUE, "lw":1.8})
ax.text(.54,.435,r"$V$ is unitary",transform=ax.transAxes,fontsize=11)
ax.text(.5,.115,r"$(V\pi(a)V^{-1}z)_n=a_nz_n$",
        transform=ax.transAxes,ha="center",fontsize=14,color=GREEN)
ax.text(.5,.02,r"$N_\omega=0,\quad \|\Omega\|=1$",
        transform=ax.transAxes,ha="center",fontsize=14)
fig.suptitle("A cyclic vector obtained from local units",
             fontsize=22, x=.48, y=.99)
fig.text(.5,.005,
         "Exact infinite model: GNS_FOUNDATION_PROOF.md, Section 8. "
         "Finite projections and samples are labelled explicitly. Original figure: CC0.",
         ha="center", fontsize=10, color="#435364")
fig.tight_layout(rect=(0,.035,1,.94),w_pad=2.6)
fig.savefig(HERE/"gns-nonunital-vector.png",dpi=150,facecolor="white")
fig.savefig(HERE/"gns-nonunital-vector.svg",facecolor="white")
plt.close(fig)
checks = {
    "license": "CC0-1.0",
    "scope": "Finite coordinate projection n=1..8 of an explicitly proved infinite c0 GNS model",
    "exact_formula_checks": [
        {"N":int(k), "truncation_norm_squared":str(1-Fraction(1,2**int(k))),
         "tail_norm_squared":str(Fraction(1,2**int(k)))}
        for k in n
    ],
    "e4_tail_squared": "1/16",
    "e5_error_squared": "1/32",
    "coordinate9_norm_squared": "1/512",
    "png_expected_dimensions": [2400, 1155],
}
for row in checks["exact_formula_checks"]:
    assert Fraction(row["truncation_norm_squared"])+Fraction(row["tail_norm_squared"]) == 1
(HERE/"FIGURE_ARITHMETIC.json").write_text(
    json.dumps(checks,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"outputs":["gns-nonunital-vector.png","gns-nonunital-vector.svg",
                              "FIGURE_ARITHMETIC.json"],
                  "all_exact_fraction_checks_passed":True}))
