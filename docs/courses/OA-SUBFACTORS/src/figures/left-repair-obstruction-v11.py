"""CC0: finite coefficient checks and an exact operator-coordinate schematic.

Run with Python, NumPy and Matplotlib from any directory. All outputs are saved
beside this source. These checks support the infinite Jones-tunnel proof in the
accompanying text; the finite coefficient space is not promoted to a Jones core.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

HERE = Path(__file__).resolve().parent
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULI = (I, X, Y, Z)


def tensor(*items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def leg(a, j):
    return tensor(*(a if i == j else I for i in range(3)))


def left(a):
    # Column-major vectorization, orthonormal normalized matrix units.
    return np.kron(np.eye(a.shape[0]), a)


def omega(n):
    return np.eye(n).reshape(-1, order="F") / np.sqrt(n)


def residual(a):
    return float(np.linalg.norm(a, ord=2))


def trace_norm(a):
    # The Q coordinate uses its inherited normalized trace, never Hilbert trace.
    return float(np.linalg.svd(a, compute_uv=False).sum() / 8)


def span_rank(basis, cup):
    cols = [(a @ cup @ b).reshape(-1) for a in basis for b in basis]
    return int(np.linalg.matrix_rank(np.column_stack(cols), tol=1e-9))


def run_checks():
    qI = np.eye(8)
    x = [leg(X, j) for j in range(3)]
    z = [leg(Z, j) for j in range(3)]
    cups = [(qI + x[0]) / 2, (qI + z[0]) / 2,
            (qI + x[0] @ x[1]) / 2, (qI + z[1]) / 2,
            (qI + x[1] @ x[2]) / 2, (qI + z[2]) / 2]
    cup_error = max(residual(p @ p - p) for p in cups)
    adjacent_error = max(residual(cups[j] @ cups[j + 1] @ cups[j]
                                  - cups[j] / 2) for j in range(5))
    distant_error = max(residual(cups[i] @ cups[j] - cups[j] @ cups[i])
                         for i in range(6) for j in range(i + 2, 6))
    parity = z[0] @ z[1] @ z[2]
    A = []
    T = []
    for indices in product(range(4), repeat=3):
        if sum(i in (1, 2) for i in indices) % 2 == 0:
            word = tensor(*(PAULI[i] for i in indices))
            A.append(word)
            if indices[0] in (0, 1):
                T.append(word)
    full_first = span_rank(A, cups[0])
    full_second = span_rank(T, cups[1])
    assert (len(A), len(T), full_first, full_second) == (32, 16, 64, 32)

    # m=1, k=2: three physical Q legs and two standard D legs.
    k = 2
    p = (qI + z[0] @ z[1]) / 2
    u = x[0]
    v = x[0] @ x[2]
    w = x[0] @ x[1]  # One fixed smaller-factor unitary commuting with p.
    rhs = np.zeros((32, 32), dtype=complex)
    lhs = rhs.copy()
    h = np.zeros((128, 128), dtype=complex)
    rows = []
    for s in range(2):
        branch = p if s == 0 else qI - p
        for r in range(2):
            c = np.zeros((2, 2), dtype=complex)
            c[r, s] = 1
            for a, b in product(range(2), repeat=2):
                V = np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b)
                row = tensor(branch, c, V) / k
                rows.append(row)
                lhs += row @ row.conj().T
                rhs += row.conj().T @ row
                Dvector = np.kron(left(c) @ omega(2), left(V) @ omega(2))
                h += np.kron(branch, np.outer(Dvector, Dvector.conj())) / k**2
    rho_plus = np.kron(np.diag([1, 0]), I)
    rho_minus = np.kron(np.diag([0, 1]), I)
    hp = tensor(rho_plus, np.eye(4)) / (2 * k**2)
    hm = tensor(rho_minus, np.eye(4)) / (2 * k**2)
    h_formula = np.kron(p, hp) + np.kron(qI - p, hm)
    rhs_formula = tensor(p, np.diag([2, 0]), I) \
        + tensor(qI - p, np.diag([0, 2]), I)
    U = np.kron(u, np.eye(16))
    Vbig = np.kron(v, np.eye(16))
    Wbig = np.kron(w, np.eye(16))
    repaired = (h + Vbig @ h @ Vbig.conj().T) / 2
    P = 4 * k**2 * repaired
    repaired_rows = [row / np.sqrt(2) for row in rows] + [
        np.kron(v, np.eye(4)) @ row / np.sqrt(2) for row in rows]
    right_after = sum((a.conj().T @ a for a in repaired_rows),
                      np.zeros_like(rhs))
    defects = {
        "old_u_L1_defect": trace_norm(U @ h @ U.conj().T - h),
        "old_adaptive_v_L1_defect": trace_norm(Vbig @ h @ Vbig.conj().T - h),
        "fixed_w_L1_defect": trace_norm(Wbig @ h @ Wbig.conj().T - h),
        "repaired_u_L1_defect": trace_norm(U @ repaired @ U.conj().T - repaired),
    }
    errors = {
        "cup_projection": cup_error,
        "adjacent_cup_half_compression": adjacent_error,
        "nonadjacent_cup_commutation": distant_error,
        "v_is_even": residual(parity @ v @ parity - v),
        "left_coisometry": residual(lhs - np.eye(32)),
        "right_sum_formula": residual(rhs - rhs_formula),
        "actual_density_formula": residual(h - h_formula),
        "old_scaled_support_projection": residual(
            (2 * k**2 * h) @ (2 * k**2 * h) - 2 * k**2 * h),
        "adaptive_support_projection": residual(P @ P - P),
        "adaptive_density_formula": residual(repaired - np.eye(128) / (4 * k**2)),
        "right_sum_preserved": residual(right_after - rhs),
    }
    assert max(errors.values()) < 1e-10
    assert abs(defects["old_u_L1_defect"] - 2) < 1e-10
    assert abs(defects["old_adaptive_v_L1_defect"] - 2) < 1e-10
    assert defects["fixed_w_L1_defect"] < 1e-10
    assert defects["repaired_u_L1_defect"] < 1e-10

    # Physical marginal on a full Pauli basis in the finite coefficient window.
    marginal_error = 0.0
    compatibility_error = 0.0
    for indices in product(range(4), repeat=5):
        qword = tensor(*(PAULI[i] for i in indices[:3]))
        dword = tensor(*(PAULI[i] for i in indices[3:]))
        Lop = tensor(qword, left(PAULI[indices[3]]),
                     left(PAULI[indices[4]]))
        actual = np.einsum("ij,ji->", h, Lop) / 8
        physical = np.trace(qword) / 8 * np.trace(dword) / 4
        marginal_error = max(marginal_error, float(abs(actual - physical)))
    # E_A acts only by physical parity; h is exactly fixed by that action.
    PARITY = np.kron(parity, np.eye(16))
    compatibility_error = residual(PARITY @ h @ PARITY - h)
    assert marginal_error < 1e-10 and compatibility_error < 1e-10
    return {
        "scope": "finite coefficient checks supporting BC4.1-BC4.23; not a substitute core",
        "normalization": "Q normalized trace times ordinary Hilbert trace on D",
        "m": 1, "k": k,
        "old_row_length": len(rows), "repaired_row_length": len(repaired_rows),
        "old_density_trace": float(np.trace(h).real / 8),
        "repaired_density_trace": float(np.trace(repaired).real / 8),
        "old_support_canonical_trace": float(np.trace(2 * k**2 * h).real / 8),
        "repaired_support_canonical_trace": float(np.trace(P).real / 8),
        "finite_fullness_dimensions": {
            "A": len(A), "T": len(T),
            "span_A_pX_A": full_first, "span_T_pZ_T": full_second},
        "residuals": errors, "defects": defects,
        "physical_marginal_full_1024_word_basis_error": marginal_error,
        "expectation_compatibility_error": compatibility_error,
        "J": 0,
        "proof_of_asymptotic_fixed_list_claim": "BC4.17-BC4.19, analytic, not sampled",
    }


def make_figure():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                         "svg.fonttype": "path"})
    fig, axes = plt.subplots(2, 2, figsize=(15.6, 11.7))
    fig.patch.set_facecolor("#f6f8fb")
    blue, gold, green, ink = "#276c9b", "#b87924", "#247761", "#18304b"
    for ax in axes.flat:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
        ax.add_patch(FancyBboxPatch((.01, .015), .98, .97,
                    boxstyle="round,pad=.01,rounding_size=.025",
                    linewidth=1, edgecolor="#c4d0db", facecolor="white"))
    def label(ax, x, y, text, size=12, color=ink, **kw):
        return ax.text(x, y, text, fontsize=size, color=color, **kw)
    def title(ax, text, proof):
        label(ax, .05, .92, text, 15, weight="bold")
        label(ax, .05, .86, proof, 10, color="#4d6276")

    ax = axes[0, 0]
    title(ax, "Actual index-two physical model", "BC4.4–BC4.12; all-smooth proof: Proposition BC4.3")
    label(ax, .06, .76, r"$N=Q^\alpha\bar\otimes D\ \subset\ M=Q\bar\otimes D$", 18)
    label(ax, .06, .66, r"$\alpha=\bigotimes_{j\geq0}\mathrm{Ad}\,Z_j,\quad u=X_0$", 15)
    label(ax, .06, .55, "Explicit cups in the ordinary parity tunnel", 12, weight="bold")
    label(ax, .06, .47, r"$g_0=(1+X_0)/2,\quad g_{2j+1}=(1+Z_j)/2$", 14)
    label(ax, .06, .39, r"$g_{2j}=(1+X_{j-1}X_j)/2\quad(j\geq1)$", 14)
    label(ax, .06, .29, r"$S=Q^\alpha\otimes1,\qquad R=Q\otimes1$", 16, color=blue)
    label(ax, .06, .19, r"$A=Q^\alpha\bar\otimes B(L^2D)\subset B=Q\bar\otimes B(L^2D)$", 13)
    label(ax, .06, .09, r"$\mathrm{Tr}=\tau_Q\otimes\mathrm{Tr}_{D}$,  $\mathrm{Tr}(e)=1$,  $J_h=0$", 13)

    ax = axes[0, 1]
    title(ax, "A correlated finite row", "Exact constants: BC4.14–BC4.18; table entries are densities")
    label(ax, .06, .76, r"$h_m=p_m\otimes h_{m,+}+(1-p_m)\otimes h_{m,-}$", 15)
    # The branch blocks are a support schematic, not scaled Hilbert dimensions.
    for s, xx in enumerate((.22, .57)):
        label(ax, xx + .12, .65, (r"$\rho(p_+)$" if s == 0 else r"$\rho(p_-)$"),
              13, ha="center")
    label(ax, .055, .51, r"$p_m$", 13)
    label(ax, .045, .34, r"$1-p_m$", 13)
    for r, yy in enumerate((.43, .26)):
        for s, xx in enumerate((.22, .57)):
            color = blue if r == s else "#f0f4f8"
            ax.add_patch(Rectangle((xx, yy), .24, .14, facecolor=color,
                                   edgecolor="#8b9eaf", linewidth=1))
            label(ax, xx + .12, yy + .07,
                  r"$1/(2k_m^2)$" if r == s else r"$0$",
                  13, color="white" if r == s else ink,
                  ha="center", va="center")
    label(ax, .06, .17, r"$L_m=4k_m^2,\quad \mathrm{Tr}(\mathrm{supp}\,h_m)=2k_m^2$", 14)
    label(ax, .06, .09, r"$\delta_u(h_m)=2$;  $u$ swaps the two physical branches.", 13, color=gold)

    ax = axes[1, 0]
    title(ax, "Every fixed finite left-N list misses this sequence", "Theorem BC4.4; the limit is proved for every fixed list")
    label(ax, .06, .76, r"$\mathcal{T}(h)=\sum_{j=1}^{s}\theta_jv_jhv_j^*,\quad v_j\in N$", 15)
    label(ax, .06, .66, r"$\delta_x(h_m)\longrightarrow0\quad(x\in N)$", 16, color=blue)
    label(ax, .06, .56, r"$\|\mathcal{T}(h_m)-h_m\|_1\leq\sum_j\theta_j\delta_{v_j}(h_m)\to0$", 13)
    label(ax, .06, .43, r"$\delta_u(\mathcal{T}h_m)\geq2-2\|\mathcal{T}h_m-h_m\|_1\to2$", 14, color=gold)
    label(ax, .06, .32, r"$g_{\mathcal{T}a}=g_a,\qquad J_{\mathcal{T}a}=J_a=0$", 16)
    label(ax, .06, .22, "Trace and original expectation stay exact.", 13)
    label(ax, .06, .13, "The obstruction concerns a fixed list independent of the row.", 12)
    label(ax, .06, .065, "It does not exclude adaptive averages or the original existence claim.", 11)

    ax = axes[1, 1]
    title(ax, "Adaptive two-term repair, with the target budget first", "BC4.20–BC4.23; full local continuation: Corollary BC4.5")
    label(ax, .06, .76, r"$v_m=X_0X_{m+1}\in N,\quad \mathcal{T}_m=(\mathrm{id}+\mathrm{Ad}\,v_m)/2$", 14)
    label(ax, .06, .65, r"$\widetilde h_m=P_m/(4k_m^2),\quad\mathrm{Tr}(P_m)=4k_m^2$", 16, color=green)
    label(ax, .06, .55, r"$P_m=1_{L^2Q}\otimes1_{L^2\mathrm{Mat}_2}\otimes q_m$", 15)
    label(ax, .06, .45, r"$L_{\rm new}=8k_m^2,\quad g_{\rm new}=g_m,\quad J_{\rm new}=0$", 14)
    label(ax, .06, .35, r"Choose $m$ first: $\max_{x\in\mathcal{F}}\|x-E_{K_m}x\|_2<\eta/2$.", 13)
    label(ax, .06, .25, r"$\delta_x(\widetilde h_m),\ \|[x,P_m]\|_2/\sqrt{\mathrm{Tr}(P_m)}<\eta$", 14, color=green)
    label(ax, .06, .14, "Theorems 60.4–60.5 apply: prescribed prefix, support 1,", 12)
    label(ax, .06, .075, "residual 0 and a generating continuation, separately from Pₘ.", 12)

    fig.suptitle("Genuine left averaging: a fixed-list obstruction and an explicit repair",
                 fontsize=20, color=ink, weight="bold", y=.985)
    fig.text(.5, .013,
             "Exact operator-coordinate schematic. Branch block areas are not dimension scales. "
             "The infinite tunnel and all-smooth quantifier are proved in the accompanying text.",
             ha="center", fontsize=10, color="#526578")
    fig.subplots_adjust(top=.948, bottom=.045, left=.025, right=.985,
                        hspace=.085, wspace=.055)
    fig.savefig(HERE / "left-repair-obstruction-v11.svg", metadata={"Creator": "CC0 original figure source"})
    fig.savefig(HERE / "left-repair-obstruction-v11.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    result = run_checks()
    (HERE / "finite-checks.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    make_figure()
    print(json.dumps(result, indent=2))
