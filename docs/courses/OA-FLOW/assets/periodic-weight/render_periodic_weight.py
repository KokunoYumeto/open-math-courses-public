"""Exact M3 illustration of PW2--PW5. Run in this directory or by absolute path."""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "mathtext.fontset": "dejavusans",
    "svg.hashsalt": "oa-flow-periodic-weight-pw-v1",
    "svg.fonttype": "path",
    "axes.spines.top": False,
    "axes.spines.right": False,
})
navy = "#173654"
blue = "#1769aa"
orange = "#c95524"
green = "#16806a"
gray = "#697989"
bg = "#f5f8fb"

fig = plt.figure(figsize=(15.6, 10.8), facecolor="white")
grid = fig.add_gridspec(2, 2, left=.075, right=.97, bottom=.13,
                       top=.86, wspace=.26, hspace=.45)
fig.text(.075, .96, "A bounded phase removes a given inner modular period",
         fontsize=22, weight="bold", color=navy)
fig.text(.075, .918,
         "Exact example: P = 1, M = M₃(ℂ), ψ(a) = Tr(Da).  "
         "The matrix example illustrates the arbitrary-weight proof.",
         fontsize=12.5, color=gray)

ax = fig.add_subplot(grid[0, 0])
ax.set_aspect("equal")
ang = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(ang), np.sin(ang), color="#c4d1de", linewidth=2)
ax.axhline(0, color="#e1e7ed", linewidth=.7)
ax.axvline(0, color="#e1e7ed", linewidth=.7)
for theta, label, offset in [
    (0, "b₁ = 1\nΘ₁ = 0\non ker(1 − b)", (1.23, .12)),
    (np.pi/2, "b₂ = i\nA₂ = −1,  Θ₂ = π/2", (.15, 1.18)),
    (3*np.pi/2, "b₃ = −i\nA₃ = 1,  Θ₃ = 3π/2", (.15, -1.36)),
]:
    point = (np.cos(theta), np.sin(theta))
    ax.scatter(*point, s=90, color=blue if theta else orange, zorder=4)
    ax.annotate(label, xy=point, xytext=offset, fontsize=11.3,
                color=navy, arrowprops={"arrowstyle": "-", "color": gray},
                ha="left", va="center")
for t in [.45, 2.45, 4.1]:
    ax.add_patch(FancyArrowPatch((.87*np.cos(t), .87*np.sin(t)),
        (.87*np.cos(t+.35), .87*np.sin(t+.35)), arrowstyle="-|>",
        mutation_scale=13, color=green, connectionstyle="arc3,rad=.12"))
ax.text(0, 0, r"$e^{i\theta(t)}=\frac{t-i}{t+i}$" + "\n"
        + r"$\theta(t)=2\pi-2\,\mathrm{arccot}(t)$",
        ha="center", va="center", fontsize=12, color=green,
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
ax.set(xlim=(-1.5, 2.7), ylim=(-1.5, 1.5))
ax.set_axis_off()
ax.set_title("1. The phase and the actual fixed projection (PW2)",
             loc="left", fontsize=14, fontweight="bold", color=navy, pad=21)

ax = fig.add_subplot(grid[0, 1])
ax.set_axis_off()
ax.set_title("2. Subtract the bounded phase (PW3)",
             loc="left", fontsize=14, fontweight="bold", color=navy, pad=21)
table = ax.table(
    cellText=[
        ["1", "0", "0", "0"],
        ["2", "5/2", "1/2", "2"],
        ["3", "−1/2", "3/2", "−2"],
    ],
    colLabels=["j", "log Dⱼ / π", "Θⱼ / π", "log Qⱼ / π"],
    cellLoc="center", colLoc="center", colWidths=[.1, .29, .28, .33],
    bbox=[0, .48, 1, .43])
table.auto_set_font_size(False)
table.set_fontsize(13)
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor("white")
    cell.set_facecolor("#e5edf5" if row == 0 else bg)
    if row == 0:
        cell.set_text_props(color=navy, weight="bold", fontsize=11.2)
    else:
        cell.set_text_props(color=green if col == 3 else navy)
ax.text(.02, .31, r"$k=e^{-\Theta},\quad Q=Dk=\mathrm{diag}(1,e^{2\pi},e^{-2\pi})$",
        fontsize=15, color=green)
ax.text(.02, .15, r"$e^{-2\pi}I\leq k\leq I,\qquad e^{-2\pi}\psi\leq\phi\leq\psi$",
        fontsize=15, color=navy)
ax.text(.02, .015, "The second inequality is a weight inequality on the whole cone.",
        fontsize=11.2, color=gray)

ax = fig.add_subplot(grid[1, 0])
times = np.linspace(0, 1, 501)
ax.plot(times, np.cos(2*np.pi*times), color=blue, linewidth=2.4,
        label="Real part: cos(2πt)")
ax.plot(times, -np.sin(2*np.pi*times), color=orange, linewidth=2.4,
        label="Imaginary part: −sin(2πt)")
ax.axhline(0, color=gray, linewidth=.8)
ax.set(xlim=(0, 1), ylim=(-1.12, 1.22), xlabel="t (one given period P = 1)",
       ylabel="Coefficient of E₁₂")
ax.set_xticks([0, .25, .5, .75, 1], ["0", "1/4", "1/2", "3/4", "1"])
ax.grid(alpha=.15)
ax.legend(loc="upper center", ncols=1, frameon=False, fontsize=10.5)
ax.set_title("3. The repaired orbit closes and averages to zero",
             loc="left", fontsize=13.4, fontweight="bold", color=navy, pad=19)
ax.text(.5, -.31, r"$\sigma_t^\phi(E_{12})=e^{-2\pi it}E_{12},"
        r"\qquad \int_0^1e^{-2\pi it}\,dt=0$",
        transform=ax.transAxes, ha="center", color=green, fontsize=13.5)

ax = fig.add_subplot(grid[1, 1])
ax.set_axis_off()
ax.set_title("4. Compact averaging gives diagonal pinching (PW4–5)",
             loc="left", fontsize=13.4, fontweight="bold", color=navy, pad=19)
ax.text(.08, .89, "Positive X", fontsize=12, color=navy)
ax.text(.62, .89, "E(X)", fontsize=12, color=green)
left = [["2", "1/4", "0"], ["1/4", "1", "1/5"], ["0", "1/5", "3"]]
right = [["2", "0", "0"], ["0", "1", "0"], ["0", "0", "3"]]
for x0, data, color in [(0, left, navy), (.57, right, green)]:
    tab = ax.table(cellText=data, cellLoc="center", bbox=[x0, .42, .41, .40])
    tab.auto_set_font_size(False)
    tab.set_fontsize(14)
    for (row, col), cell in tab.get_celld().items():
        cell.set_edgecolor("white")
        cell.set_facecolor("#e5edf5" if row == col else bg)
        cell.set_text_props(color=color)
ax.text(.49, .62, "→", ha="center", va="center", fontsize=29, color=gray)
ax.text(.015, .23, r"$\phi(X)=\tau(E(X))=2+e^{2\pi}+3e^{-2\pi}$",
        color=green, fontsize=14.5)
ax.text(.015, .06, "Here Mφ is the diagonal algebra ℂ³, not a factor.\n"
        "A period alone gives no factoriality assertion.",
        fontsize=12, color=navy, linespacing=1.5)

fig.savefig(OUT / "periodic-phase-and-average.png", dpi=160,
            facecolor="white", metadata={"Software": "OA-FLOW original renderer"})
fig.savefig(OUT / "periodic-phase-and-average.svg",
            facecolor="white", metadata={"Date": None, "Creator": "OA-FLOW original renderer"})
plt.close(fig)
svg = OUT / "periodic-phase-and-average.svg"
svg.write_text(svg.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")

D = np.diag(np.exp(np.pi*np.array([0, 2.5, -.5])))
theta = np.pi*np.array([0, .5, 1.5])
Q = np.diag(np.exp(2*np.pi*np.array([0, 1, -1])))
k = np.diag(np.exp(-theta))
X = np.array([[2, .25, 0], [.25, 1, .2], [0, .2, 3]])
assert np.allclose(D @ k, Q)
assert np.linalg.eigvalsh(X).min() > 0
assert np.allclose(np.exp(1j*theta), np.exp(1j*np.log(np.diag(D))))
assert np.allclose(np.exp(1j*np.log(np.diag(Q))), np.ones(3))
assert np.allclose(np.exp(1j*(2*np.pi-2*np.arctan2(1, np.array([-1, 1])))),
                   np.array([1j, -1j]))
data = {
    "exact_period_P": 1,
    "log_D_over_pi": ["0", "5/2", "-1/2"],
    "Theta_over_pi": ["0", "1/2", "3/2"],
    "log_Q_over_pi": ["0", "2", "-2"],
    "b": ["1", "i", "-i"],
    "A_on_complement_of_ker_1_minus_b": ["-1", "1"],
    "k_diagonal": ["1", "exp(-pi/2)", "exp(-3*pi/2)"],
    "X": [["2", "1/4", "0"], ["1/4", "1", "1/5"], ["0", "1/5", "3"]],
    "E_X": [["2", "0", "0"], ["0", "1", "0"], ["0", "0", "3"]],
    "exact_weight_X": "2 + exp(2*pi) + 3*exp(-2*pi)",
    "whole_cone_bound": "exp(-2*pi)*psi <= phi <= psi",
    "X_strict_diagonal_dominance_lower_bounds": ["7/4", "11/20", "14/5"],
    "proof_locators": ["PERIODIC_WEIGHT_PROOF.md#pw-2",
                       "PERIODIC_WEIGHT_PROOF.md#pw-3",
                       "PERIODIC_WEIGHT_PROOF.md#pw-4",
                       "PERIODIC_WEIGHT_PROOF.md#pw-5",
                       "PERIODIC_WEIGHT_FIGURE.md"],
    "numerical_checks": {"max_density_identity_error": float(np.abs(D@k-Q).max()),
                         "X_min_eigenvalue": float(np.linalg.eigvalsh(X).min())},
    "sampled_curves_are_not_proofs": True,
}
(ROOT / "FIGURE_DATA.json").write_text(json.dumps(data, indent=2) + "\n",
                                       encoding="utf-8", newline="\n")
