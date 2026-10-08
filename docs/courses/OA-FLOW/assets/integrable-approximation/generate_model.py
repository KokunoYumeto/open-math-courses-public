"""Reproduce the original Package A interval model. No source or font copies."""
from pathlib import Path
import json
import math
import hashlib

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent
DELTA = math.log(2)
FONT = font_manager.findfont("DejaVu Sans")
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 12,
    "svg.fonttype": "none",
    "svg.hashsalt": "oa-flow-integrable-interval-v1",
    "savefig.facecolor": "#f7f9fb",
    "mathtext.fontset": "dejavusans",
})
navy, teal, orange = "#16324f", "#087f8c", "#d07824"
q = np.linspace(-DELTA, DELTA, 401)
y = np.linspace(-2, 2, 401)
h = np.exp(q)
envelope = np.exp(DELTA * np.abs(y))
assert np.all(h >= 0.5 - 1e-14) and np.all(h <= 2 + 1e-14)
assert abs(np.exp(2 * DELTA) - 4) < 1e-14
assert abs(envelope[0] - 4) < 1e-14

fig, ax = plt.subplots(2, 2, figsize=(15, 10), layout="constrained")
fig.set_facecolor("#f7f9fb")
fig.suptitle("A narrow density change retains an infinite fixed matrix factor",
             fontsize=21, color=navy)

a = ax[0, 0]
a.set_title(r"Interval spectrum: $h=e^Q\otimes1$", loc="left", color=navy)
a.plot(q, h, color=teal, lw=3)
a.scatter([-DELTA, 0, DELTA], [0.5, 1, 2], color=teal, s=45, zorder=3)
a.set_xticks([-DELTA, 0, DELTA], [r"$-\log2$", "0", r"$\log2$"])
a.set_yticks([0.5, 1, 2], [r"$1/2$", "1", "2"])
a.set_xlabel(r"coordinate $q$ in $I=[-\delta,\delta]$, with $\delta=\log2$")
a.set_ylabel(r"scalar multiplier $e^q$")
a.set_xlim(-DELTA * 1.12, DELTA * 1.12)
a.set_ylim(0.25, 2.35)
a.text(0.03, 0.94, "width = 2 log 2     spectral ratio = 4",
       transform=a.transAxes, va="top", color=navy)
a.grid(alpha=0.18)

a = ax[0, 1]
a.set_title("Entire cocycle: exact vertical growth", loc="left", color=navy)
a.plot(y, envelope, color=orange, lw=3)
a.set_xlabel(r"imaginary coordinate $y=\operatorname{Im}z$")
a.set_ylabel(r"$\|h^{i(t+iy)}\|=2^{|y|}$")
a.set_xticks([-2, -1, 0, 1, 2])
a.set_yticks([1, 2, 4])
a.set_ylim(0.75, 4.75)
a.text(0.5, 0.93, r"$d_U(\varphi,\varphi_h)=\delta$",
       ha="center", va="top", transform=a.transAxes, color=navy, fontsize=15)
a.grid(alpha=0.18)

a = ax[1, 0]
a.set_title("The fixed matrix factor has infinitely many coordinates", loc="left", color=navy)
a.set_xlim(0, 8)
a.set_ylim(0, 5.5)
a.axis("off")
a.text(0.1, 4.8, r"$K=L^2(I)\otimes\ell^2,\qquad D=1\otimes B(\ell^2)\subset M_\psi$",
       color=navy, fontsize=15)
for n in range(6):
    x = 0.25 + n * 1.08
    a.add_patch(Rectangle((x, 2.7), 0.82, 1.2, facecolor="#d5edf0",
                          edgecolor=teal, lw=1.5))
    a.text(x + 0.41, 3.42, rf"$e_{n+1}$", ha="center", va="center", color=navy)
    a.text(x + 0.41, 3.02, r"$L^2(I)$", ha="center", va="center", fontsize=11)
a.text(6.9, 3.3, r"$\cdots$", fontsize=24, color=navy)
a.annotate("same modulation on every coordinate",
           xy=(3.2, 2.65), xytext=(3.2, 1.92), ha="center", color=teal,
           arrowprops={"arrowstyle": "->", "color": teal})
a.text(0.1, 1.08, r"$\gamma_t=\operatorname{Ad}(e^{itQ}\otimes1)$ fixes every $1\otimes e_{ij}$.",
       fontsize=13, color=navy)
a.text(0.1, 0.47, "The six boxes are a schematic prefix; the matrix factor is infinite.",
       fontsize=11, color=navy)

a = ax[1, 1]
a.set_title("Positive orbit averages prove integrability", loc="left", color=navy)
a.set_xlim(0, 1)
a.set_ylim(0, 1)
a.axis("off")
lines = [
    (0.89, r"$\xi_1=(2\delta)^{-1/2}1_I,\quad a_1=\theta_{\xi_1,\xi_1}\otimes q_1$", 15),
    (0.70, r"$\int_{\mathbb{R}}\gamma_t(a_1)\,dt=\frac{\pi}{\delta}\,1\otimes q_1$", 18),
    (0.52, r"$\delta=\log2:\qquad \pi/\delta\approx4.53236$", 14),
    (0.34, r"$a_n=P_n\otimes q_n\uparrow1$; each average is bounded.", 13),
    (0.19, "Unital inclusion carries these same contractions into M.", 12),
    (0.06, r"Measure: $dt$  |  Proof: (IA15)–(IA18), Sections 3–4", 11),
]
for yy, txt, fs in lines:
    a.text(0.02, yy, txt, fontsize=fs, color=navy, va="center")

for row in ax:
    for a in row:
        a.set_facecolor("white")
        for spine in a.spines.values():
            spine.set_color("#d0d9e2")

fig.savefig(OUT / "integrable-interval.svg", metadata={"Date": None,
            "Creator": "Original OA-FLOW Package A model; generate_model.py"})
fig.savefig(OUT / "integrable-interval.png", dpi=150,
            metadata={"Software": "Original OA-FLOW Package A model"})
plt.close(fig)

data = {
    "title": "Interval centralizer model for commuting integrable approximation",
    "original": True,
    "proof_locators": ["../../src/OA-FLOW-IAP.md (IA13)-(IA18)", "../../src/OA-FLOW-IAP.md (IA24)"],
    "delta_exact": "log(2)", "delta_numeric": DELTA,
    "spectrum_h_exact": ["1/2", "2"], "spectral_ratio_exact": "4",
    "interval_width_exact": "2 log(2)",
    "space": "L2([-delta,delta],dq) tensor ell2(N)",
    "h": "exp(Q) tensor 1", "fixed_matrix_factor": "1 tensor B(ell2(N))",
    "norm_formula": "norm(h^(i(t+iy))) = exp(delta abs(y)) = 2^abs(y)",
    "uniform_distance_exact": "delta",
    "rank_one_average_dt": "(pi/delta) 1 tensor q1",
    "rank_one_average_numeric": math.pi / DELTA,
    "general_average_dt": "2 pi M_(sum_{j<=n}|xi_j|^2) tensor q_n",
    "q_samples": q.tolist(), "density_samples": h.tolist(),
    "y_samples": y.tolist(), "norm_samples": envelope.tolist(),
    "samples_are": "Numerical rendering of exact proved formulas, not proof evidence",
    "schematic_scope": "First six coordinates of an infinite matrix factor; no type III factor is constructed by this plot",
    "font_reference": {"family": "DejaVu Sans",
                       "installed_file_reference": "matplotlib.get_data_path()/fonts/ttf/DejaVuSans.ttf",
                       "font_file_sha256": hashlib.sha256(Path(FONT).read_bytes()).hexdigest(),
                       "copied": False, "svg_fonttype": "none"},
    "versions": {"matplotlib": matplotlib.__version__, "numpy": np.__version__},
}
(OUT / "model-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf8")
print(json.dumps({"figure": "integrable-interval.png",
                  "average": math.pi / DELTA,
                  "font_reference": "matplotlib-data/fonts/ttf/DejaVuSans.ttf"}))
