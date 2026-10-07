"""Reproduce cst-models.png and cst-models.svg from data.json.

Run: python render.py
Requirements: Python 3, NumPy, Matplotlib. No network or external image assets.
The formulas in PART_MODELS.md are proofs. These bounded numerical and exact
matrix checks verify implementation of the plotted formulas, not the theorem.
Original code: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
plt.rcParams.update({
    "font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
    "font.size": 12, "axes.titlesize": 12, "axes.labelsize": 11,
    "xtick.labelsize": 10, "ytick.labelsize": 10,
    "svg.fonttype": "path", "svg.hashsalt": "CST-models-20261007",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#9aa9b1", "text.color": "#15313e",
    "axes.labelcolor": "#15313e", "xtick.color": "#435d6a",
    "ytick.color": "#435d6a", "figure.facecolor": "#ffffff",
    "savefig.facecolor": "#ffffff",
})

I = np.eye(2, dtype=complex)
C = DATA["noncommuting_cocycle"]
X = np.array(C["X"], dtype=complex)
Y = np.array(C["Y_real"]) + 1j * np.array(C["Y_imaginary"])
Z = np.array(C["Z"], dtype=complex)

def pauli_exp(t, a):
    return np.cos(t) * I + 1j * np.sin(t) * a

def v(q):
    return pauli_exp(q, X) @ pauli_exp(q, Z)

def c(s, q):
    return v(q).conj().T @ v(q + s)

def spectral(a, fun):
    eig, basis = np.linalg.eigh(a)
    return (basis * fun(eig)) @ basis.conj().T

def k(t):
    return 1 / np.sqrt(math.pi * (1 + t*t))

# Exact checks use only integer and binary-exact rational complex entries.
c_half = 1j * Y
c_quarter = (I + 1j * X + 1j * Y + 1j * Z) / 2
commutator = c_half @ c_quarter - c_quarter @ c_half
expected = 1j * (Z - X)
assert np.array_equal(commutator, expected)
assert np.array_equal((Z-X) @ (Z-X), 2*I)
assert np.array_equal(c_half.conj().T @ c_half, I)
assert np.array_equal(c_quarter.conj().T @ c_quarter, I)
ann = np.diag([1, 0]).astype(complex)
assert np.array_equal((ann @ X) @ ann, np.zeros((2, 2)))
assert np.array_equal(ann @ (X @ ann), np.zeros((2, 2)))
assert np.array_equal(ann @ ann, ann)

errors = {"cocycle": 0., "common_conjugation": 0., "linking_fixedness": 0.}
for q in [-2., -math.pi/3, 0., 0.7, math.pi]:
    for s in [-1.2, 0., math.pi/4, math.pi/2]:
        for t in [-0.8, 0., 1.3]:
            errors["cocycle"] = max(errors["cocycle"], float(np.linalg.norm(c(s+t,q)-c(s,q)@c(t,q+s))))
        conjugated = pauli_exp(-q,Z) @ v(s) @ pauli_exp(q,Z)
        errors["common_conjugation"] = max(errors["common_conjugation"], float(np.linalg.norm(c(s,q)-conjugated)))
        errors["linking_fixedness"] = max(errors["linking_fixedness"], float(np.linalg.norm(v(q+s)@c(s,q).conj().T-v(q))))
assert max(errors.values()) < 1e-12

M = DATA["modulation"]
A1 = np.array(M["A1"], dtype=float)
A2 = np.array(M["A2"], dtype=float)
B = spectral(A1, k) @ spectral(A2, k)
aa, bb, dd = 1/math.sqrt(math.pi), 1/math.sqrt(2*math.pi), 1/math.sqrt(5*math.pi)
B_formula = np.array([[aa*(aa+dd), aa*(dd-aa)], [bb*(dd-aa), bb*(aa+dd)]])/2
assert np.allclose(B, B_formula, rtol=0, atol=1e-15)
U = np.array(M["left_unitary"], dtype=float)
V = np.array(M["right_unitary"], dtype=float)
assert np.allclose(spectral(A1, lambda t: np.exp(1j*math.pi*t)), U, atol=1e-14)
assert np.allclose(spectral(A2, lambda t: np.exp(1j*math.pi*t)), V, atol=1e-14)
left, right = U @ B, B @ V
assert not np.allclose(left, right)
assert not np.allclose(B, B.T)
assert abs(np.linalg.det(B)) > 0

shift = math.log(2)
area = math.e - 1
shifted_area = math.exp(1-shift)-math.exp(-shift)
assert abs(shifted_area-area/2) < 1e-15

fig = plt.figure(figsize=(16, 12.8))
fig.text(.055, .959, DATA["title"], fontsize=23, weight="bold")
fig.text(.055, .928, "Exact formulas; finite windows and matrix samples are labelled below.", fontsize=12, color="#5b6f79")

def heading(x, y, letter, title):
    fig.text(x, y, letter, fontsize=15, weight="bold", color="#ffffff",
             bbox=dict(boxstyle="round,pad=0.28", facecolor="#15313e", edgecolor="none"))
    fig.text(x+.037, y, title, fontsize=15, weight="bold")

heading(.055, .881, "A", "Translation rescales the full trace")
heading(.545, .881, "B", "A commutator that never vanishes")
heading(.055, .477, "C", "Modulation side changes the matrix")
heading(.545, .477, "D", "A finite central cut sees the difference")

teal, purple = "#137d8c", "#7c50a7"
xmin, xmax = DATA["translation"]["domain"]
for ypos, lo, hi, color, label in [
    (.723, 0., 1., teal, r"$f=1_{[0,1]}$; area $\tau(f)=e-1$"),
    (.574, -shift, 1-shift, purple, r"$\theta_{\log 2}f$; area $\tau(\theta_{\log 2}f)=(e-1)/2$"),
]:
    ax = fig.add_axes([.082, ypos, .39, .105])
    xs = np.linspace(lo, hi, 301)
    ax.fill_between(xs, 0, np.exp(xs), color=color, alpha=.25)
    ax.plot(xs, np.exp(xs), color=color, lw=2.6)
    ax.plot([xmin, lo, lo], [0, 0, math.exp(lo)], color=color, lw=1.6)
    ax.plot([hi, hi, xmax], [math.exp(hi), 0, 0], color=color, lw=1.6)
    ax.set_xlim(xmin, xmax); ax.set_ylim(0, 3)
    ax.set_yticks([0, 1, 2]); ax.set_ylabel("weighted\nindicator", fontsize=10)
    ax.set_xticks([-shift, 0, 1-shift, 1], [r"$-\log2$", "0", r"$1-\log2$", "1"])
    ax.text(0.01, 1.10, label, transform=ax.transAxes, fontsize=12, color=color)
    ax.grid(axis="y", color="#e5ebef", linewidth=.7)
fig.text(.443, .549, r"$q$", fontsize=12)
fig.text(.082, .520, r"$\theta_s f(q)=f(q+s)$ moves supports left; $\tau\theta_s=e^{-s}\tau$.", fontsize=11)

ax = fig.add_axes([.591, .638, .225, .187])
ax.imshow(expected.imag, cmap="RdBu_r", vmin=-1, vmax=1, interpolation="none")
for i in range(2):
    for j in range(2):
        ax.text(j, i, f"{int(expected.imag[i,j]):+d}", ha="center", va="center", fontsize=22, color="white", weight="bold")
ax.set_xticks([0,1], ["column 1", "column 2"])
ax.set_yticks([0,1], ["row 1", "row 2"])
ax.set_title(r"Imaginary coefficients of $i(Z-X)$", fontsize=12, pad=12)
for spine in ax.spines.values(): spine.set_visible(False)
fig.text(.833, .765, r"$c_{\pi/2}(0)=iY$", fontsize=14)
fig.text(.833, .709, r"$c_{\pi/4}(0)$", fontsize=14)
fig.text(.833, .678, r"$=\frac{1}{2}(I+iX+iY+iZ)$", fontsize=12)
fig.text(.585, .585, r"$[c_{\pi/2}(0),c_{\pi/4}(0)]=i(Z-X),\quad\|i(Z-X)\|=\sqrt{2}$", fontsize=13)
fig.text(.585, .547, r"At every $q$: common conjugation by $e^{-iqZ}$ preserves this norm.", fontsize=11)
fig.text(.585, .520, "Exact matrix entries, not a numerical approximation to zero.", fontsize=11, color="#5b6f79")

fig.text(.082, .443, r"Actual integrands at $q=s=0$, $r=\pi$; entries rounded to 3 decimals.", fontsize=11)
norm = TwoSlopeNorm(vmin=-.25, vcenter=0, vmax=.25)
for xpos, matrix, title in [(.094, left, r"$e^{i\pi A_1}B=\mathrm{diag}(1,-1)B$"),
                            (.322, right, r"$Be^{i\pi A_2}=B$")]:
    ax = fig.add_axes([xpos, .263, .145, .145])
    ax.imshow(matrix, cmap="RdBu_r", norm=norm, interpolation="none")
    for i in range(2):
        for j in range(2):
            value = matrix[i,j]
            ax.text(j, i, f"{value:+.3f}", ha="center", va="center", fontsize=13,
                    color="white" if abs(value)>.13 else "#15313e", weight="bold")
    ax.set_xticks([0,1], ["1", "2"]); ax.set_yticks([0,1], ["1", "2"])
    ax.set_title(title, fontsize=11, pad=11)
    for spine in ax.spines.values(): spine.set_visible(False)
fig.text(.085, .222, r"$B=k(A_1)k(A_2),\qquad k(t)=[\pi(1+t^2)]^{-1/2}$", fontsize=12)
fig.text(.085, .184, r"$L_r=e^{irP}\widehat b(r)$: cancel on the left for right supports.", fontsize=11)
fig.text(.085, .151, r"$R_r=\widehat b(r)e^{irP}$: cancel on the right for left supports.", fontsize=11)
fig.text(.085, .115, r"These two integrand samples are not the integrated $L_r,R_r$.", fontsize=11, color="#5b6f79")

L = DATA["localization"]
ax = fig.add_axes([.596, .263, .34, .17])
idx = np.array(L["displayed_indices"])
ax.bar(idx-.18, L["local_a_values"], width=.34, color=teal, label=r"$\rho(az_j)=1$")
ax.bar(idx+.18, L["local_b_values"], width=.34, color=purple, label=r"$\rho(bz_j)=2$")
ax.set_xticks(idx, [r"$z_1$", r"$z_2$", r"$z_3$", r"$z_4$"])
ax.set_yticks([0,1,2]); ax.set_ylim(0,2.65); ax.set_xlim(.4,4.8)
ax.set_ylabel("local trace")
ax.text(4.62, 1.4, "…", fontsize=25, ha="center")
ax.legend(loc="upper left", ncol=2, frameon=False, fontsize=11)
ax.grid(axis="y", color="#e5ebef", linewidth=.7); ax.set_axisbelow(True)
fig.text(.596, .221, r"$\rho(a)=\rho(b)=\infty$, but $\rho(az_1)=1<2=\rho(bz_1)$.", fontsize=12)
fig.text(.596, .182, r"$a=(e_{11})_j,\quad b=(I_2)_j\quad$ in $\prod_{j\geq1}M_2(\mathbb{C})$.", fontsize=12)
fig.text(.596, .145, "Both projections are finite and full; their coordinate ranks differ.", fontsize=11)
fig.text(.596, .113, "Auxiliary comparison model: equality on central pieces fails here.", fontsize=11, color="#5b6f79")

fig.lines.append(plt.Line2D([.055,.95],[.498,.498], transform=fig.transFigure, color="#d7e0e5", lw=1))
fig.lines.append(plt.Line2D([.515,.515],[.105,.89], transform=fig.transFigure, color="#d7e0e5", lw=1))
fig.text(.055, .062, "Proof locators: CST6.3; CST6.9; CST6.16–CST6.19; CST6.20–CST6.21. Action measure: ds.", fontsize=10, color="#5b6f79")
fig.text(.055, .039, "Original figure and exact data: CC0-1.0. DejaVu font terms retained separately. See the lesson caption for human-source context.", fontsize=9, color="#5b6f79")

fig.savefig(ROOT / "cst-models.png", dpi=160, metadata={"Software": "Matplotlib; original CST renderer", "Title": DATA["title"]})
fig.savefig(ROOT / "cst-models.svg", metadata={"Date": None, "Title": DATA["title"], "Description": "Four exact models; formulas, domains, factor orders and proof locators in data.json and the lesson caption."})
plt.close(fig)
print(json.dumps({
    "exact_matrix_checks": "pass", "sample_cocycle_and_linking_checks": errors,
    "translation_area": area, "translated_area": shifted_area,
    "matrix_commutator_operator_norm": float(np.linalg.norm(expected, 2)),
    "modulation_B": B.tolist(), "left_integrand": left.tolist(), "right_integrand": right.tolist(),
    "output_pixels": [2560, 2048], "outputs": ["cst-models.png", "cst-models.svg"]
}, indent=2))
