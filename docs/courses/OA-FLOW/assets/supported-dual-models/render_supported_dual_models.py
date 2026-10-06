"""Exact moving-support model for OA-FLOW-L32 Section 5.

Original code, data and diagram: CC0-1.0 to the extent of rights held.
Run: python render_supported_dual_models.py
Requires Matplotlib and SymPy. Outputs remain beside this source.
Rendered glyph outlines retain the complete terms in FONT-LICENSE.txt.
"""
from pathlib import Path
import hashlib
import json
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import sympy as sp

HERE = Path(__file__).resolve().parent
V = sp.Matrix([[0, 1], [1, 0]])
p = sp.diag(1, 0)
q = sp.diag(0, 1)
I = sp.eye(2)
Z = sp.zeros(2)
S = sp.BlockMatrix([[I, I], [I, -I]]).as_explicit() / sp.sqrt(2)
W = sp.diag(I, V)
U = S * W
lam = sp.BlockMatrix([[Z, I], [I, Z]]).as_explicit()
a, b, c, d = sp.symbols("a b c d")
A = sp.Matrix([[a, b], [c, d]])
regular_pi = sp.diag(A, V*A*V)
assert V*p*V == q
assert U*U.H == sp.eye(4)
assert sp.simplify(U*regular_pi*U.H) == sp.diag(A, A)
assert sp.simplify(U*lam*U.H) == sp.diag(V, -V)
assert sp.diag(V, V)*sp.diag(V, -V) == sp.diag(I, -I)
support = sp.diag(p, p)
swap = sp.BlockMatrix([[Z, I], [I, Z]]).as_explicit()
assert swap*support*swap.H == support
dual_density = sp.diag(p/2, p/2)
assert sp.trace(dual_density*sp.diag(p, Z)) == sp.Rational(1, 2)
assert sp.trace(dual_density*sp.diag(Z, p)) == sp.Rational(1, 2)
assert sp.trace(dual_density) == 1

def mat(m):
    return [[str(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]

data = {
    "license": "CC0-1.0 to the extent of rights held; font terms separate",
    "group": "Z/2Z",
    "original_Haar_singleton_mass": 1,
    "dual_Haar_singleton_mass": "1/2",
    "coordinate_order_input": ["e1", "e2"],
    "coordinate_order_crossed_chart": ["(+,e1)", "(+,e2)", "(-,e1)", "(-,e2)"],
    "V": mat(V), "input_support_p": mat(p), "moved_support_q": mat(q),
    "input_weight": "psi(a)=a11",
    "original_action": "alpha_1(a)=V a V",
    "original_support_image": mat(V*p*V),
    "pi_chart": "pi(a)=(a,a)",
    "lambda_chart": "(V,-V)",
    "dual_action": "theta_1(A,B)=(B,A)",
    "dual_weight": "Dpsi(A,B)=(A11+B11)/2",
    "dual_density": mat(dual_density),
    "dual_support": mat(support),
    "dual_support_image": mat(swap*support*swap.H),
    "values": {
        "psi(p)": "1", "psi(q)": "0",
        "Dpsi(p,0)": "1/2", "Dpsi(0,p)": "1/2", "Dpsi(1,1)": "1"
    },
    "regular_chart_unitary": mat(U),
    "checks": {
        "unitary": True, "pi_conjugation": True, "lambda_conjugation": True,
        "moved_original_support": True, "fixed_dual_support": True,
        "positive_half_values": True
    },
    "proof_locators": [
        "OA-FLOW-L32.md#l32-5", "L32.5.a", "L32.5.b",
        "L32.5.c", "L32.5.d", "L32.5.e"
    ],
    "figure_kind": "Exact two-dimensional matrix-coordinate diagram; no approximation",
    "native_png_pixels": [2400, 1639],
}
(HERE/"supported-dual-models-data.json").write_text(
    json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "font.size": 13,
    "svg.fonttype": "path",
    "svg.hashsalt": "oa-flow-l32-supported-dual-models-v1",
})
fig = plt.figure(figsize=(12, 8.2), dpi=200, facecolor="#f4f6f8")
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 12), ylim=(0, 8.2))
ax.set_aspect("equal")
ax.axis("off")
INK = "#142b3a"
MUTED = "#506674"
BLUE = "#007eaf"
BLUE_LIGHT = "#d8edf7"
RED = "#b84734"
RED_LIGHT = "#fbe4dc"
BORDER = "#d1dce2"

def label(x, y, text, size=14, color=INK, ha="left", **kw):
    return ax.text(x, y, text, fontsize=size, color=color, ha=ha,
                   va="center", **kw)

def card(x, y, w, h):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.16",
        facecolor="white", edgecolor=BORDER, linewidth=1))

def matrix(cx, cy, projection, accent, fill, name):
    cell = .43
    x, y = cx-cell, cy-cell
    for i in range(2):
        for j in range(2):
            active = int(projection[i, j]) == 1
            ax.add_patch(Rectangle((x+j*cell, y+(1-i)*cell), cell, cell,
                facecolor=fill if active else "#f6f8fa",
                edgecolor="#aebcc5", linewidth=.9))
            label(x+(j+.5)*cell, y+(1.5-i)*cell,
                  str(projection[i,j]), size=19,
                  color=accent if active else "#748694", ha="center",
                  fontweight="bold" if active else "normal")
    label(cx, cy-.60, name, size=17, ha="center", color=accent)

def arrow(start, end, color=INK, arc=0, width=1.7):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
        mutation_scale=18, linewidth=width, color=color,
        connectionstyle=f"arc3,rad={arc}"))

label(.55, 7.73, "The original support moves; its dual image stays fixed", 21,
      fontweight="bold")
label(.56, 7.24,
      r"$G=\mathbb{Z}/2\mathbb{Z}$, counting Haar;  "
      r"$\psi(a)=a_{11}$,  $p=e_{11}$,  $q=e_{22}$", 14, MUTED)

card(.4, 4.25, 11.2, 2.5)
label(.72, 6.39, "A   ORIGINAL ACTION ON THE COEFFICIENT ALGEBRA", 13,
      fontweight="bold")
matrix(2.5, 5.35, p, BLUE, BLUE_LIGHT, r"$p=e_{11}$")
matrix(9.5, 5.35, q, RED, RED_LIGHT, r"$q=e_{22}$")
arrow((3.48, 5.38), (8.48, 5.38))
label(6, 5.84, r"$\alpha_1(p)=VpV=q$", 19, ha="center")
label(6, 4.94, r"$V=e_{12}+e_{21}$", 15, MUTED, ha="center")
label(2.5, 4.43, r"$\psi(p)=1$", 14, ha="center")
label(9.5, 4.43, r"$\psi(q)=0$", 14, ha="center")

card(.4, .45, 11.2, 3.48)
label(.72, 3.57, "B   DUAL ACTION ON THE TWO CROSSED-PRODUCT SUMMANDS", 13,
      fontweight="bold")
label(6, 3.16, r"$C=M_2\oplus M_2,\qquad \pi(a)=(a,a)$", 17,
      ha="center")
matrix(2.5, 2.15, p, BLUE, BLUE_LIGHT, r"$(p,0)$")
matrix(9.5, 2.15, p, BLUE, BLUE_LIGHT, r"$(0,p)$")
arrow((3.35, 2.44), (8.63, 2.44), BLUE, arc=-.18)
arrow((8.63, 1.98), (3.35, 1.98), BLUE, arc=-.18)
label(6, 2.37, "swap the summands", 14, MUTED, ha="center",
      bbox={"facecolor":"white", "edgecolor":"none", "pad":2})
label(6, 1.83, r"$\theta_1(A,B)=(B,A)$", 16, ha="center",
      bbox={"facecolor":"white", "edgecolor":"none", "pad":2})
label(2.5, 1.16, r"$\mathcal{D}\psi(p,0)=1/2$", 14, ha="center")
label(9.5, 1.16, r"$\mathcal{D}\psi(0,p)=1/2$", 14, ha="center")
label(6, .77, r"$s(\mathcal{D}\psi)=(p,p)=\pi(p),"
      r"\qquad \theta_1(p,p)=(p,p)$", 17, ha="center")

label(.56, .19, "Exact matrices and Haar masses • OA-FLOW-L32, Section 5 • CC0 original diagram",
      9, MUTED)
png = HERE/"supported-dual-models.png"
svg = HERE/"supported-dual-models.svg"
fig.savefig(png, dpi=200, metadata={"Software":"Matplotlib",
    "Description":"Exact support and dual-action matrices, OA-FLOW-L32 Section 5"})
fig.savefig(svg, metadata={"Date":None,
    "Creator":"Original OA-FLOW mathematical illustration",
    "Description":"Exact support and dual-action matrices, OA-FLOW-L32 Section 5"})
plt.close(fig)

font_root = Path(matplotlib.get_data_path())/"fonts"/"ttf"
license_candidates = [
    font_root/"LICENSE_DEJAVU",
    Path(matplotlib.get_data_path())/"fonts"/"LICENSE_DEJAVU",
    Path(matplotlib.__file__).resolve().parent/"mpl-data"/"fonts"/"ttf"/"LICENSE_DEJAVU",
]
license_path = next((x for x in license_candidates if x.is_file()), None)
if license_path is None:
    raise FileNotFoundError("Cannot locate installed DejaVu license; retain it before delivery")
shutil.copyfile(license_path, HERE/"FONT-LICENSE.txt")
print(json.dumps({
    "png":str(png), "svg":str(svg),
    "data_sha256":hashlib.sha256((HERE/"supported-dual-models-data.json").read_bytes()).hexdigest(),
    "symbolic_checks":"all passed",
    "font_license_source":str(license_path)
}, indent=2))

