"""Reproduce the exact L40 diagrams. Original code and geometry: CC0-1.0.

Run with Python 3, matplotlib and numpy. The accompanying JSON specifies all
mathematical constants and signs. DejaVu font terms are retained separately.
"""
from fractions import Fraction
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parent
DATA = json.loads((OUT / "exact-data.json").read_text(encoding="utf-8"))
BG = "#f7fafc"
INK = "#142e47"
BLUE = "#225c88"
ORANGE = "#ad4c0a"
GREEN = "#13766a"
PALE = "#e9f4f1"
GREY = "#526678"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "path",
    "svg.hashsalt": "oa-flow-invariant-state-fields-20261006",
    "savefig.facecolor": BG,
})


def verify_mathematics():
    """Check exact phase identities, then independently sample actual matrices."""
    m = DATA["matrix_model"]
    rows = m["W_t_row_phase_exponents"]
    cols = m["W_t_adjoint_column_phase_exponents"]
    entry = m["conjugation_entry_phase_exponents"]
    assert entry == [[rows[i] + cols[j] for j in range(2)] for i in range(2)]
    assert sum(Fraction(*p) for p in m["base_masses_rational"]) == 1
    for j in range(2):
        fibre = m["fibre_" + str(j + 1)]
        exponents = fibre["unitary_coordinate_phase_exponents"]
        assert exponents == [entry[i][j] for i in range(2)]
        assert exponents[j] == 0
        assert [[exponents[i] - exponents[k] for k in range(2)] for i in range(2)] == entry
    b = np.array([[1 + 2j, -3 + 1j], [2 - 1j, 4 + 3j]], dtype=complex)
    a = np.array([[2 - 1j, 3 + 2j], [-1 + 4j, -2]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    def W(t):
        return np.diag([np.exp(1j * t), 1])
    def u(t, j):
        return np.exp(-1j * t * (1 - j)) * W(t)
    def close(x, y):
        np.testing.assert_allclose(x, y, atol=2e-14, rtol=2e-14)
    for t in (0, 0.4, np.pi / 2, 2 * np.pi):
        transformed = W(t) @ b @ W(t).conj().T
        for j in range(2):
            close(transformed[:, j], u(t, j) @ b[:, j])
            close(u(t, j) @ eye[:, j], eye[:, j])
            close(u(t, j) @ a @ u(t, j).conj().T, W(t) @ a @ W(t).conj().T)
            close(u(t - 0.7, j), u(t, j) @ u(-0.7, j))
        close(np.trace(transformed.conj().T @ transformed) / 2, np.trace(b.conj().T @ b) / 2)
    print("Exact rational masses and all symbolic phase identities pass.")
    print("Numerical column, fixed-vector, covariance, cocycle and norm checks pass.")


def box(ax, xy, width, height, fill="white", edge="#cfdee7"):
    patch = FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.012,rounding_size=0.018",
                           facecolor=fill, edgecolor=edge, linewidth=1.3)
    ax.add_patch(patch)
    return patch


def label(ax, x, y, text, size=14, color=INK, weight=None, ha="center"):
    return ax.text(x, y, text, fontsize=size, color=color, weight=weight,
                   ha=ha, va="center", linespacing=1.55)


def arrow(ax, x, y0, y1):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>",
                                mutation_scale=20, linewidth=1.8, color=BLUE))


def save(fig, name):
    fig.savefig(OUT / (name + ".svg"), bbox_inches="tight", metadata={"Date": None})
    fig.savefig(OUT / (name + ".png"), bbox_inches="tight", dpi=180)
    plt.close(fig)


def columns():
    fig, ax = plt.subplots(figsize=(14.5, 10))
    fig.patch.set_facecolor(BG)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    label(ax, .5, .971, "One matrix, two fixed fibres", 26, weight="bold")
    label(ax, .5, .923, r"$\varphi(a)=\frac{1}{2}\mathrm{Tr}(a)$"
          r"     |     $W_t=\mathrm{diag}(e^{it},1)$"
          r"     |     $U_t b=W_t bW_t^*$", 16)
    for j, x in enumerate((.255, .745), start=1):
        box(ax, (x - .226, .127), .452, .722, fill="white")
        label(ax, x, .812, "Fibre " + str(j) + "   ·   mass 1/2", 19, weight="bold")
        label(ax, x, .771, r"$T_t(" + str(j) + ")=" + str(j) + r"$   —   the base point stays fixed", 12.5, GREY)
        if j == 1:
            input_text = r"$\eta_1=be_1=(b_{11},b_{21})^{\mathsf{T}}$"
            phase = r"right $W_t^*$ contributes $e^{-it}$"
            op = r"$u(t,1)=e^{-it}W_t=\mathrm{diag}(1,e^{-it})$"
            output = r"$(b_{11},\,e^{-it}b_{21})^{\mathsf{T}}$"
            fixed = r"$u(t,1)e_1=e^{-it}e^{it}e_1=e_1$"
        else:
            input_text = r"$\eta_2=be_2=(b_{12},b_{22})^{\mathsf{T}}$"
            phase = r"right $W_t^*$ contributes $1$"
            op = r"$u(t,2)=W_t=\mathrm{diag}(e^{it},1)$"
            output = r"$(e^{it}b_{12},\,b_{22})^{\mathsf{T}}$"
            fixed = r"$u(t,2)e_2=W_te_2=e_2$"
        box(ax, (x - .195, .659), .39, .070, fill="#edf4f9", edge="#d3e2ee")
        label(ax, x, .696, input_text, 17)
        arrow(ax, x, .65, .581)
        label(ax, x, .551, phase, 14, ORANGE)
        label(ax, x, .504, op, 16)
        arrow(ax, x, .47, .397)
        box(ax, (x - .195, .29), .39, .083, fill="#edf4f9", edge="#d3e2ee")
        label(ax, x, .333, output, 19)
        label(ax, x, .237, "The cyclic vector is fixed", 13, GREEN, weight="bold")
        label(ax, x, .185, fixed, 16, GREEN)
    label(ax, .5, .084, r"$VU_tV^{-1}(\eta_1,\eta_2)=(u(t,1)\eta_1,u(t,2)\eta_2)$", 18)
    label(ax, .5, .034, "Arrows act within fibres.  The measure derivative is 1; orange labels are unit complex phases.", 12, GREY)
    save(fig, "column-phase-transport")


def boundary():
    fig, ax = plt.subplots(figsize=(14.5, 4.6))
    fig.patch.set_facecolor(BG)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    label(ax, .5, .924, "A null endpoint can carry a zero restriction", 23, weight="bold")
    label(ax, .5, .797, r"$A=\{f\in C([0,1]):f(0)=0\}$"
          r"     |     $\varphi(f)=\int_0^1 f(t)\,dt$", 17)
    x0, x1 = .265, .91
    label(ax, .035, .597, "Spectrum of B", 14, ha="left")
    ax.plot([x0, x1], [.598, .598], color=GREY, linewidth=4)
    ax.scatter([x0, x1], [.598, .598], s=90, color=GREY, zorder=3)
    label(ax, x0, .681, "0", 13)
    label(ax, x1, .681, "1", 13)
    label(ax, .035, .358, "Full-norm locus", 14, ha="left")
    ax.plot([x0, x1], [.357, .357], color=GREEN, linewidth=4)
    ax.scatter([x0], [.357], s=115, facecolor=BG, edgecolor=ORANGE, linewidth=2.5, zorder=3)
    ax.scatter([x1], [.357], s=90, color=GREEN, zorder=3)
    label(ax, .59, .452, r"$X_1=(0,1]\qquad \|\mathrm{ev}_x|_A\|=1\quad(x>0)$", 17, GREEN)
    label(ax, x0, .18, r"$\|\mathrm{ev}_0|_A\|=0$", 15, ORANGE)
    label(ax, .685, .18, r"$\mu(\{0\})=0$   ·   exact conull locus", 15)
    label(ax, .5, .035, "The action in this example is trivial, so this precise locus is invariant.", 12.5, GREY)
    save(fig, "full-norm-boundary")


if __name__ == "__main__":
    verify_mathematics()
    columns()
    boundary()
    print("Rendered column-phase-transport and full-norm-boundary as SVG and PNG.")
