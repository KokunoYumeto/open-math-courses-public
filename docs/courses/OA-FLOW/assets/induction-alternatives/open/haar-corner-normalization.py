"""Draw the exact k=1 Haar-normalization example in OA-FLOW-L55, (OA5)-(OA6)."""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
STEM = "haar-corner-normalization"
DATA = {
    "group": "R semidirect_2 Z",
    "multiplication": "(b,n)(d,m)=(b+2^n*d,n+m)",
    "left_Haar_density_on_level_n": "2^(-n) db",
    "modular_function": "Delta(b,n)=2^(-n)",
    "coset_index_k": 1,
    "source_level_n": -1,
    "source_interval": [0, 1],
    "source_measure_density": 2,
    "source_amplitude": 1,
    "target_measure_density": 1,
    "target_amplitude_exact": "sqrt(2)",
    "source_squared_norm": 2,
    "target_squared_norm": 2,
    "general_unitary": "(T xi)_k(h)=2^(k/2) xi(h,-k,k)",
    "proof_locator": "OA-FLOW-L55, (OA1)-(OA6)",
    "drawing": "Heights are function amplitudes; squared norms use the labelled measures."
}
(ROOT / (STEM + ".json")).write_text(
    json.dumps(DATA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "svg.hashsalt": "oa-flow-haar-corner-normalization",
    "savefig.facecolor": "white"
})
fig, axes = plt.subplots(1, 2, figsize=(12, 5.2))
fig.suptitle("The Haar factor preserves the squared norm", fontsize=21, y=.96)
panels = [
    (1, "#186c88", r"Source: $H t_1^{-1}$, level $-1$",
     r"$\xi(b)=1_{[0,1]}(b)\,v$", r"Measure: $2\,db$", r"$\|\xi\|^2=2\int_0^1 1\,db=2$", "b"),
    (math.sqrt(2), "#b55428", r"Target: subgroup $H$",
     r"$(T\xi)_1(h)=\sqrt{2}\,1_{[0,1]}(h)\,v$", r"Measure: $dh$",
     r"$\|T\xi\|^2=\int_0^1 2\,dh=2$", "h")
]
for ax, (height, color, title, formula, measure, norm, coordinate) in zip(axes, panels):
    ax.plot([-.25, 0, 0, 1, 1, 1.25], [0, 0, height, height, 0, 0], color=color, lw=3)
    ax.fill_between([0, 1], [height, height], color=color, alpha=.12)
    ax.set(xlim=(-.25, 1.25), ylim=(-.05, 1.95), xlabel=coordinate)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1, math.sqrt(2)])
    ax.set_yticklabels(["0", "1", r"$\sqrt{2}$"])
    ax.set_ylabel("Amplitude along the unit vector v")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title, fontsize=15, pad=12)
    ax.text(.5, 1.82, formula, ha="center", va="center", fontsize=14)
    ax.text(.5, -.25, measure, transform=ax.transAxes, ha="center", fontsize=14)
    ax.text(.5, -.43, norm, transform=ax.transAxes, ha="center", fontsize=16, color=color)
fig.subplots_adjust(left=.08, right=.98, bottom=.31, top=.78, wspace=.28)
fig.savefig(ROOT / (STEM + ".png"), dpi=180)
fig.savefig(ROOT / (STEM + ".svg"), metadata={"Date": None, "Creator": "OA-FLOW course project"})
plt.close(fig)
