"""Exact translation-probability example, OA-FLOW-L72 (PM1)-(PM12)."""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
STEM = "translation-probability"
DATA = {
    "space": "R",
    "measure_density": "rho(x)=exp(-abs(x))/2",
    "translation_t": 1,
    "Radon_Nikodym_derivative": "r_t(x)=exp(abs(x)-abs(x-t))",
    "unitary_action": "(U_t xi)(x)=sqrt(r_t(x))*xi(x-t)",
    "density_unitary": "(J xi)(x)=sqrt(rho(x))*xi(x)",
    "averaging_domain": "L_infinity(lambda) intersect L_1(dx)",
    "panels": [
        {"vector": "xi", "support": [0, 1], "amplitude_exact": "1",
         "squared_norm_exact": "(1-exp(-1))/2"},
        {"vector": "B_1 xi", "support": [1, 2], "amplitude_exact": "1",
         "squared_norm_exact": "exp(-1)*(1-exp(-1))/2"},
        {"vector": "U_1 xi", "support": [1, 2], "amplitude_exact": "sqrt(e)",
         "squared_norm_exact": "(1-exp(-1))/2"}
    ],
    "constant_vector_distance_squared": "2-2*(1+abs(t)/2)*exp(-abs(t)/2)",
    "proof_locator": "OA-FLOW-L72, (PM1)-(PM12)",
    "drawing": "Graphs show amplitudes. Norm labels are exact integrals against lambda."
}
(ROOT / (STEM + ".json")).write_text(
    json.dumps(DATA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "svg.hashsalt": "oa-flow-translation-probability",
    "savefig.facecolor": "white"
})
fig, axes = plt.subplots(1, 3, figsize=(15.3, 5.8))
fig.suptitle("Translation in a faithful probability model", fontsize=22, y=.97)
fig.text(.5, .865, r"Every panel uses $d\lambda(x)=\frac{1}{2} e^{-|x|}\,dx$",
         fontsize=17, ha="center")
specs = [
    (0, 1, 1, "#186c88", "Original vector",
     r"$\xi=1_{[0,1]}$", r"$\|\xi\|_\lambda^2=\frac{1-e^{-1}}{2}$"),
    (1, 2, 1, "#727887", "Plain pullback",
     r"$B_1\xi=1_{[1,2]}$", r"$\|B_1\xi\|_\lambda^2=e^{-1}\frac{1-e^{-1}}{2}$"),
    (1, 2, math.sqrt(math.e), "#b55428", "Unitary image",
     r"$U_1\xi=\sqrt{e}\,1_{[1,2]}$", r"$\|U_1\xi\|_\lambda^2=\frac{1-e^{-1}}{2}$")
]
for ax, (a, b, height, color, title, formula, norm) in zip(axes, specs):
    ax.plot([-.4, a, a, b, b, 2.6], [0, 0, height, height, 0, 0], color=color, lw=3)
    ax.fill_between([a, b], [height, height], color=color, alpha=.12)
    ax.set(xlim=(-.4, 2.6), ylim=(-.05, 2.2), xlabel="x")
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, math.sqrt(math.e)])
    ax.set_yticklabels(["0", "1", r"$\sqrt{e}$"])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title, fontsize=16, pad=12)
    ax.text(1.1, 2.02, formula, ha="center", fontsize=15)
    ax.text(.5, -.32, norm, transform=ax.transAxes, ha="center", fontsize=17, color=color)
axes[0].set_ylabel("Amplitude")
fig.text(.5, .055, "The square-root density factor restores the original weighted norm.",
         ha="center", fontsize=15)
fig.subplots_adjust(left=.055, right=.985, bottom=.29, top=.73, wspace=.24)
fig.savefig(ROOT / (STEM + ".png"), dpi=180)
fig.savefig(ROOT / (STEM + ".svg"), metadata={"Date": None, "Creator": "OA-FLOW course project"})
plt.close(fig)
