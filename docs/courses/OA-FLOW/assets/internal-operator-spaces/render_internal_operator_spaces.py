"""Exact coordinate illustration for OA-FLOW-L131, equations O12--O14.

Original code, diagram and data: CC0-1.0 to the extent of rights held.
Run with Python, NumPy and Matplotlib. No input files are required.
The matrices are compressions of specified infinite operators, not a
finite-dimensional Cuntz representation.
"""

from pathlib import Path
import json
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-internal-operator-spaces-20261009-v1"
from matplotlib.colors import ListedColormap
from matplotlib.patches import FancyBboxPatch
import numpy as np

DEST = Path(__file__).resolve().parent
matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "svg.fonttype": "none",
    "savefig.facecolor": "#f8fafc",
})
navy, blue, purple = "#17324d", "#147d92", "#7046a0"
N = 8
j = np.zeros((N, N), dtype=int)
for n in range(N // 2):
    j[2*n, 2*n+1] = 1
rho = np.diag([1, 1, 0, 0, 0, 0, 0, 0])
product = j @ rho
assert np.array_equal(product, rho @ j)
assert np.count_nonzero(product) == 1 and product[0, 1] == 1

objects = {
    "lesson": "OA-FLOW-L131",
    "equations": ["O12", "O13", "O14"],
    "terms": "CC0-1.0 for original diagram, data and code; DejaVu font separately licensed",
    "hilbert_space": "ell^2(N_0)",
    "coordinate_map": "W(e_r tensor e_n)=e_(2n+r), r in {0,1}, n>=0",
    "displayed_coordinates": [
        {"r": r, "n": n, "image": 2*n+r} for n in range(4) for r in range(2)
    ],
    "compression_indices": list(range(N)),
    "matrix_convention": "row=output, column=input; filled entry=1, blank entry=0",
    "j_e01": j.tolist(),
    "rho_p0": rho.tolist(),
    "product": product.tolist(),
    "meaning": "Exact compressions of infinite operators to four complete parity pairs",
}
(DEST / "objects.json").write_text(json.dumps(objects, indent=2)+"\n", encoding="utf-8")

fig = plt.figure(figsize=(13.5, 8.4), facecolor="#f8fafc")
fig.text(.055, .955, "Two coordinates, two commuting factors",
         fontsize=23, weight="bold", color=navy)
fig.text(.055, .916,
         r"$H=\ell^2(\mathbb{N}_0)$,  $K=\mathrm{span}\{s_0,s_1\}$"
         r"    and    $W_K(e_r\otimes e_n)=e_{2n+r}$",
         fontsize=15, color=navy)

ax = fig.add_axes([.055, .64, .89, .23])
ax.set_xlim(-.15, 4.15)
ax.set_ylim(-.2, 1.8)
ax.axis("off")
ax.text(-.11, 1.58, "Parity r", color=navy, weight="bold")
ax.text(1.72, 1.58, "Remaining coordinate n", color=navy, weight="bold")
for n in range(4):
    ax.text(n+.45, 1.3, f"n = {n}", ha="center", color=navy)
    for r in range(2):
        y = .83-r*.69
        color = blue if r == 0 else purple
        ax.add_patch(FancyBboxPatch((n+.08, y-.22), .75, .45,
                                    boxstyle="round,pad=0.015,rounding_size=0.05",
                                    facecolor="white", edgecolor=color, linewidth=1.8))
        ax.text(n+.455, y, rf"$e_{r}\otimes e_{n}\;\mapsto\; e_{2*n+r}$",
                ha="center", va="center", color=color, fontsize=13)
        if n == 0:
            ax.text(-.06, y, str(r), ha="right", va="center",
                    color=color, weight="bold", fontsize=13)
ax.text(4.00, .5, r"$\cdots$", color=navy, fontsize=20)

titles = [
    (r"$\Psi(e_{01})=s_0s_1^*$", "Changes parity; preserves n", j, blue),
    (r"$\rho_K(p_0)$", "Selects n = 0; preserves parity", rho, purple),
    (r"$\Psi(e_{01})\rho_K(p_0)$", r"$|e_0\rangle\langle e_1|$", product, navy),
]
for x, (title, subtitle, matrix, color) in zip([.07, .385, .70], titles):
    a = fig.add_axes([x, .155, .245, .393])
    a.imshow(matrix, cmap=ListedColormap(["white", color]), vmin=0, vmax=1)
    a.set_xticks(range(N))
    a.set_yticks(range(N))
    a.set_xticks(np.arange(-.5, N, 1), minor=True)
    a.set_yticks(np.arange(-.5, N, 1), minor=True)
    a.grid(which="minor", color="#c9d3df", linewidth=.8)
    a.tick_params(which="minor", length=0)
    a.tick_params(which="major", length=0, labelsize=10, colors=navy)
    for row, col in zip(*np.nonzero(matrix)):
        a.text(col, row, "1", ha="center", va="center", color="white", weight="bold")
    a.set_xlabel("Input index", fontsize=10, color=navy)
    a.set_ylabel("Output index", fontsize=10, color=navy)
    a.set_title(title+"\n"+subtitle, fontsize=12, pad=13, color=navy)
    for spine in a.spines.values():
        spine.set_color("#c9d3df")

fig.text(.055, .077,
         "Exact first-eight-coordinate compressions. Filled entries are 1; all other entries are 0.",
         fontsize=11, color=navy)
fig.text(.055, .043,
         "The full operators act on the infinite space. Equations O12–O14; general splitting: Sections 3–5.",
         fontsize=11, color=navy)
fig.savefig(DEST / "internal-operator-spaces.png", dpi=170)
fig.savefig(DEST / "internal-operator-spaces.svg", metadata={"Date": None})
plt.close(fig)

font_license = Path(matplotlib.get_data_path()) / "fonts" / "ttf" / "LICENSE_DEJAVU"
if font_license.is_file():
    shutil.copyfile(font_license, DEST / "FONT-LICENSE.txt")
print(json.dumps({"png": "internal-operator-spaces.png",
                  "svg": "internal-operator-spaces.svg",
                  "exact_commutation": True,
                  "nonzero_product_entries": [[0, 1]]}))
