"""Exact tensor-weight models and original figure. CC0-1.0, except font terms.

Run with Python 3 and Matplotlib. Outputs stay beside this file.
DejaVu Sans font terms are copied in full from Matplotlib's font distribution.
The figure uses vector glyph paths in its SVG and contains no external assets.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "path",
    "svg.hashsalt": "tensor-trace-exact-v1",
    "font.size": 12,
    "axes.unicode_minus": False,
})
NAVY = "#17324d"
BLUE = "#2563a6"
TEAL = "#087f8c"
ORANGE = "#b65c18"
GRAY = "#5c6b78"
LIGHT = "#e8edf2"
PAPER = "#fbfcfe"

# Outer-then-inner order (i,a). All checks below use exact rational arithmetic.
labels = ["(1,1)", "(1,2)", "(2,1)", "(2,2)", "(3,1)", "(3,2)"]
X = [
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
]
d = [2, 5, 2, 5, 2, 5]
c = Fraction(2)
K = [[Fraction(v, 2) for v in row] for row in X]
column_energy = [sum(X[r][s] ** 2 for r in range(6)) for s in range(6)]
row_energy = [sum(v ** 2 for v in row) for row in X]
omega_xstarx = sum(d[s] * column_energy[s] for s in range(6))
omega_xxstar = sum(d[r] * row_energy[r] for r in range(6))
kernel_norm = c*c*sum(d[s]*K[r][s]**2 for r in range(6) for s in range(6))
assert omega_xstarx == kernel_norm == 22
assert omega_xxstar == 31
assert c*c*Fraction(1, 2)**2 == 1

# A separate blockwise calculation checks index placement.
block_norms = []
block_adjoint_norms = []
for i in range(3):
    for j in range(3):
        block_norms.append(sum(d[b]*X[2*i+a][2*j+b]**2 for a in range(2) for b in range(2)))
        block_adjoint_norms.append(sum(d[a]*X[2*i+a][2*j+b]**2 for a in range(2) for b in range(2)))
assert block_norms == [2, 5, 0, 8, 0, 0, 0, 0, 7]
assert block_adjoint_norms == [2, 2, 0, 20, 0, 0, 0, 0, 7]

# Hadamard basis change in the first two outer coordinates; irrational factors
# occur twice, so all diagonal weights below are exact halves.
old_diagonal = [Fraction(10), Fraction(5), Fraction(7)]
new_diagonal = [Fraction(15, 2), Fraction(15, 2), Fraction(7)]
assert sum(old_diagonal) == sum(new_diagonal) == 22
graph_n = list(range(1, 7))
graph_norms = [(1-Fraction(1, 4**n))/3 for n in graph_n]
assert all(v == sum(Fraction(1, 4**k) for k in range(1, n+1))
           for n, v in zip(graph_n, graph_norms))
graph_half_norms = [sum(Fraction(4**k, 4**k) for k in range(1, n+1)) for n in graph_n]
assert graph_half_norms == graph_n

data = {
    "title": "Tensor weights: exact blocks, Haar normalization and graph domains",
    "license": "CC0-1.0 to the extent of rights held; DejaVu font terms retained separately",
    "coefficient_density": [2, 5],
    "outer_inner_basis_order": labels,
    "operator_matrix_X": X,
    "six_dimensional_density": d,
    "block_squared_gns_norms_row_major": block_norms,
    "block_adjoint_squared_gns_norms_row_major": block_adjoint_norms,
    "Omega_XstarX": omega_xstarx,
    "Omega_XXstar": omega_xxstar,
    "old_diagonal_weight_contributions": [str(v) for v in old_diagonal],
    "new_diagonal_weight_contributions": [str(v) for v in new_diagonal],
    "haar_singleton_mass": str(c),
    "kernel_K": [[str(v) for v in row] for row in K],
    "normalized_kernel_operator_rule": "X_rs = c K(r,s)",
    "weighted_kernel_squared_norm": str(kernel_norm),
    "rank_one_projection_kernel_nonzero_entry": "1/2",
    "rank_one_projection_usual_trace": 1,
    "graph_example": {
        "weight": "phi(a)=sum_{n>=0}4^n <a e_n,e_n>",
        "orthonormal_GNS_basis": "f_mn=2^(-n) Lambda(e_mn)",
        "half_power_on_basis": "Delta^(1/2) f_mn = 2^(m-n) f_mn",
        "vector": "xi=sum_{n>=1}2^(-n) f_n0",
        "partial_indices": graph_n,
        "partial_squared_norms": [str(v) for v in graph_norms],
        "partial_squared_half_power_norms": [str(v) for v in graph_half_norms],
        "limit_squared_norm": "1/3",
        "limit_in_half_power_domain": False,
    },
    "nonseparable_scope": {
        "E": "ell^2(I), I arbitrary uncountable",
        "Omega_1_tensor_pF": "7 |F|",
        "indexing": "all finite subsets F of I ordered by inclusion",
        "no_sequence_exhaustion_claim": True,
    },
    "proof_locators": ["OA-FLOW-TW.html#tw-matrix-model",
                       "OA-FLOW-TW.html#tw-basis-diagnostic",
                       "OA-FLOW-TW.html#tw-haar-diagnostic",
                       "OA-FLOW-TW.html#tw-domain-diagnostic"],
    "human_antecedent": {
        "work": "Takesaki, Theory of Operator Algebras II",
        "locator": "VIII.4, Lemma4.1, Definition4.2, Proposition4.3, printed133-134",
        "url": "https://doi.org/10.1007/978-3-662-10451-4",
        "relationship": "Tensor-weight theorem context; example and artwork are original",
    },
}
(OUT/"tensor-trace-data.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")

fig = plt.figure(figsize=(16, 11.2), dpi=200, facecolor=PAPER)
fig.text(.04, .962, "Tensor weights: the norm, its normalization, and its domain",
         fontsize=23, color=NAVY, weight="bold", va="top")
fig.text(.04, .923, "Exact finite models for the arbitrary-Hilbert tensor theorem",
         fontsize=13.5, color=GRAY, va="top")

def panel(x, y, w, h):
    fig.add_artist(FancyBboxPatch((x, y), w, h, transform=fig.transFigure,
                   boxstyle="round,pad=0.006,rounding_size=0.008",
                   facecolor="white", edgecolor="#d6dfe8", linewidth=1.2, zorder=0))

panel(.04, .472, .442, .405)
panel(.518, .472, .442, .405)
panel(.04, .07, .442, .365)
panel(.518, .07, .442, .365)
fig.text(.056, .856, "A   An operator with weighted coefficients", fontsize=15,
         weight="bold", color=NAVY, va="top")
fig.text(.534, .856, "B   Its GNS vector weights the columns", fontsize=15,
         weight="bold", color=NAVY, va="top")
fig.text(.056, .411, "C   Haar mass belongs in the kernel", fontsize=15,
         weight="bold", color=NAVY, va="top")
fig.text(.534, .411, "D   Norm convergence is not graph convergence", fontsize=14.1,
         weight="bold", color=NAVY, va="top")
fig.text(.056, .821, r"$D=\operatorname{diag}(2,5),\quad E=\mathbb{C}^3$",
         fontsize=13, color=GRAY)
fig.text(.534, .821, r"$[\Lambda_\Omega(X)]_{ij}=X_{ij}D^{1/2}$",
         fontsize=13, color=GRAY)

def matrix_axes(bounds, values):
    ax = fig.add_axes(bounds)
    ax.set_xlim(-1.10, 6.10)
    ax.set_ylim(-.18, 6.62)
    ax.set_aspect("equal")
    ax.axis("off")
    for r in range(6):
        for s in range(6):
            val = values[r][s]
            active = val != "0"
            ax.add_patch(Rectangle((s, 5-r), 1, 1,
                         facecolor=("#e1f1f2" if active else "#f9fbfd"),
                         edgecolor=LIGHT, linewidth=.5))
            ax.text(s+.5, 5-r+.5, val, ha="center", va="center",
                    color=TEAL if active else "#b0bac4",
                    fontsize=(12.5 if val.startswith("$2") else 14) if active else 10.5,
                    weight="bold" if active else "normal")
    for k in [0, 2, 4, 6]:
        ax.plot([0, 6], [k, k], color=NAVY, lw=1.3)
        ax.plot([k, k], [0, 6], color=NAVY, lw=1.3)
    for i, label in enumerate(labels):
        ax.text(i+.5, 6.27, label, ha="center", va="center", fontsize=9.5, color=GRAY)
        ax.text(-.18, 5-i+.5, label, ha="right", va="center", fontsize=9.5, color=GRAY)
    return ax

matrix_axes([.076, .534, .36, .267], [[str(v) for v in row] for row in X])
gns = [["0"]*6 for _ in range(6)]
for r in range(6):
    for s in range(6):
        if X[r][s]:
            prefix = "" if X[r][s] == 1 else str(X[r][s])
            gns[r][s] = "$"+prefix+r"\sqrt{"+str(d[s])+"}$"
matrix_axes([.554, .534, .36, .267], gns)
fig.text(.064, .507, r"$\Omega(X^*X)=22,\qquad \Omega(XX^*)=31$",
         fontsize=16.5, color=NAVY)
fig.text(.542, .507, r"$2+5+8+2+5=22$", fontsize=18, color=TEAL, weight="bold")

fig.text(.064, .371, r"$G=\mathbb{Z}/3\mathbb{Z},\qquad c=2,\qquad K=X/2$",
         fontsize=14, color=GRAY)
fig.text(.064, .324, r"$[T_K\xi](r)=c\sum_s K(r,s)\xi(s)$",
         fontsize=18, color=NAVY)
fig.text(.064, .278, r"$X_{rs}=cK(r,s)$", fontsize=20, color=TEAL)
fig.text(.064, .230, r"$\|\Lambda_\Omega(T_K)\|^2"
                    r"=c^2\sum_{r,s}\varphi(K_{rs}^*K_{rs})$",
         fontsize=16.5, color=NAVY)
fig.text(.064, .184, r"$=4\,(22/4)=22$", fontsize=20, color=TEAL)
fig.text(.064, .135, r"Rank-one projection:  $k_j(j,j)=1/2$",
         fontsize=13.5, color=GRAY)
fig.text(.064, .098, r"$c\,k_j(j,j)=1,\qquad \operatorname{Tr}(p_j)=1$",
         fontsize=16, color=NAVY)

fig.text(.542, .355, r"$\xi_N=\sum_{n=1}^{N}2^{-n}f_{n0},"
                    r"\qquad \Delta^{1/2}f_{n0}=2^n f_{n0}$",
         fontsize=13.2, color=GRAY)
left = fig.add_axes([.555, .177, .162, .130])
right = fig.add_axes([.764, .177, .162, .130])
for ax in (left, right):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["bottom", "left"]].set_color("#b4c1ce")
    ax.tick_params(labelsize=9.5, color="#b4c1ce", labelcolor=GRAY)
    ax.set_xlim(.65, 6.35)
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_xlabel("$N$", fontsize=12, labelpad=2)
    ax.grid(axis="y", color=LIGHT, lw=.8)
    ax.set_axisbelow(True)
left.scatter(graph_n, [float(v) for v in graph_norms], s=28, color=TEAL, zorder=3)
left.axhline(1/3, color=TEAL, lw=1, ls="--")
left.set_ylim(0, .365)
left.set_yticks([0, .25, 1/3], ["0", "1/4", "1/3"])
left.set_title(r"$\|\xi_N\|^2=(1-4^{-N})/3$", fontsize=11.5, pad=10, color=NAVY)
right.scatter(graph_n, graph_n, s=28, color=ORANGE, zorder=3)
right.set_ylim(0, 6.65)
right.set_yticks([0, 2, 4, 6])
right.set_title(r"$\|\Delta^{1/2}\xi_N\|^2=N$", fontsize=11.5, pad=10, color=NAVY)
fig.text(.544, .113, r"$\xi_N\longrightarrow\xi,\qquad \|\xi\|^2=1/3,$",
         fontsize=16, color=NAVY)
fig.text(.544, .081, r"$\xi\notin D(\Delta^{1/2})$", fontsize=16, color=ORANGE)

fig.text(.04, .036,
         "Proofs: TW §7, Diagnostics 4–5.  Exact matrix entries and finite partial sums; no separability assumption in the theorem.",
         fontsize=10.4, color=GRAY)
fig.text(.04, .017, "Original figure and data: CC0-1.0.  DejaVu Sans font terms retained.",
         fontsize=9.3, color=GRAY)

fig.canvas.draw()
renderer = fig.canvas.get_renderer()
width, height = fig.canvas.get_width_height()
for t in fig.texts:
    box = t.get_window_extent(renderer)
    assert box.x0 >= 0 and box.y0 >= 0 and box.x1 <= width and box.y1 <= height, t.get_text()
fig.savefig(OUT/"tensor-trace.png", dpi=200, facecolor=PAPER,
            metadata={"Title": data["title"], "Description": "Exact original tensor-weight examples; CC0-1.0"})
fig.savefig(OUT/"tensor-trace.svg", facecolor=PAPER,
            metadata={"Title": data["title"], "Date": None,
                      "Description": "Exact original tensor-weight examples. CC0-1.0; DejaVu font terms retained."})
plt.close(fig)
font_terms = Path(matplotlib.get_data_path())/"fonts/ttf/LICENSE_DEJAVU"
shutil.copyfile(font_terms, OUT/"FONT-LICENSE.txt")
print(json.dumps({
    "image_size": [width, height],
    "Omega_XstarX": omega_xstarx,
    "Omega_XXstar": omega_xxstar,
    "weighted_kernel_norm": str(kernel_norm),
    "basis_changed_diagonal": [str(v) for v in new_diagonal],
    "font_terms_sha256": hashlib.sha256((OUT/"FONT-LICENSE.txt").read_bytes()).hexdigest(),
    "matplotlib": matplotlib.__version__,
}, indent=2))
