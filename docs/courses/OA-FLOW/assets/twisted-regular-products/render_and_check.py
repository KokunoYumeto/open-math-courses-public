"""Original reproducible diagrams and finite checks for the TRP lesson.

Only writes beside this source. No external sources, fonts or PDF files are copied.
Run from this asset directory: python render_and_check.py
"""
from pathlib import Path
from itertools import permutations
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "svg.fonttype": "none", "savefig.facecolor": "#fafaf8"})
INK = "#182a36"
BLUE = "#12567a"
TEAL = "#176f63"
ORANGE = "#994b20"
PALE = "#eaf1f4"


def canvas(title, subtitle):
    fig, ax = plt.subplots(figsize=(15, 8), dpi=150)
    fig.patch.set_facecolor("#fafaf8")
    ax.set_facecolor("#fafaf8")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(.035, .96, title, fontsize=24, weight="bold", color=INK, va="top")
    ax.text(.035, .90, subtitle, fontsize=13, color=INK, va="top")
    fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
    return fig, ax


def box(ax, x, y, w, h, text, color=BLUE, fontsize=16):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.016",
                           edgecolor=color, facecolor=PALE, linewidth=1.6)
    ax.add_patch(patch)
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=fontsize, color=INK)


def arrow(ax, start, end, color=BLUE, curve=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=19,
                                color=color, lw=1.7,
                                connectionstyle=f"arc3,rad={curve}"))


def save(fig, name):
    # Stable SVG IDs and metadata make the SVG reproducible on the same runtime.
    with matplotlib.rc_context({"svg.hashsalt": "OA-FLOW-TRP-20261008"}):
        fig.savefig(OUT/f"{name}.svg", metadata={"Date": None, "Creator": "Original TRP diagram source"})
    fig.savefig(OUT/f"{name}.png", metadata={"Software": "Original TRP diagram source"})
    plt.close(fig)


def figures():
    fig, ax = canvas("Two sheets expose every Fourier coefficient",
                     "Exact model: N = C₂ = {e,t}, μ = 1. Entries are operators in P.  |  TR6, TR10–TR15, TR33")
    ax.text(.075, .80, "Regular coordinates", fontsize=17, color=BLUE, weight="bold")
    box(ax, .075, .57, .27, .16, r"$H_0$ at $e$"+"\n"+r"$\pi(a)=a$", fontsize=18)
    box(ax, .075, .31, .27, .16, r"$H_0$ at $t$"+"\n"+r"$\pi(a)=\beta_t(a)$", fontsize=18)
    arrow(ax, (.17, .55), (.17, .49), curve=.2)
    arrow(ax, (.25, .49), (.25, .55), curve=.2)
    ax.text(.355, .515, "$L_t$: swap\n(no scalar twist)", fontsize=14, va="center", color=INK)
    ax.text(.65, .79, r"$X=\pi(a)+\pi(b)L_t$", fontsize=20, ha="center", color=INK)
    # An actual 2-by-2 block matrix, with both row and column indices.
    x0, y0, w, h = .54, .43, .36, .28
    for row in range(2):
        for col in range(2):
            ax.add_patch(Rectangle((x0+col*w/2, y0+(1-row)*h/2), w/2, h/2,
                                   edgecolor=BLUE, facecolor="#ffffff", lw=1.5))
    for row, col, text in [(0, 0, "$a$"), (0, 1, "$b$"),
                           (1, 0, r"$\beta_t(b)$"), (1, 1, r"$\beta_t(a)$")]:
        ax.text(x0+(col+.5)*w/2, y0+(1.5-row)*h/2, text,
                fontsize=24, ha="center", va="center", color=INK)
    ax.text(x0+w/4, .735, "$e$", ha="center", fontsize=17)
    ax.text(x0+3*w/4, .735, "$t$", ha="center", fontsize=17)
    ax.text(.515, y0+3*h/4, "$e$", ha="center", va="center", fontsize=17)
    ax.text(.515, y0+h/4, "$t$", ha="center", va="center", fontsize=17)
    box(ax, .54, .29, .36, .085, r"$E_\mu(X)=X_{e,e}=a$", color=TEAL, fontsize=20)
    ax.text(.075, .19, r"$X\Omega=(\widehat{a},\widehat{\beta_t(b)})$", fontsize=19, color=INK)
    ax.text(.54, .19, r"$\|X\|_2^2=\|a\|_2^2+\|b\|_2^2$", fontsize=20, color=TEAL)
    ax.text(.075, .105, "Model A symmetry: α_z changes the t coefficient's sign",
            fontsize=15, color=INK)
    ax.text(.075, .058, "(a,b) ↦ (β_z(a), −β_z(b));  α_z(L_t) = −L_t", fontsize=16, color=BLUE)
    save(fig, "two-sheet-fourier")

    fig, ax = canvas("Innerness has a coefficient witness",
                     "Assumptions: P is a factor and β_h is outer for every h ≠ e.  |  TR20–TR23")
    box(ax, .08, .71, .84, .11, r"$X\in\mathcal{U}(M_\mu)$ implements $\alpha_g$", fontsize=22)
    arrow(ax, (.5, .69), (.5, .625))
    box(ax, .08, .50, .84, .11,
        r"$x_n=E_\mu(XL_n^*)\ne0$ for some $n\in N$", fontsize=22)
    ax.text(.5, .46, "Fourier uniqueness supplies a nonzero coefficient", fontsize=13,
            color=BLUE, ha="center")
    arrow(ax, (.5, .425), (.5, .36))
    box(ax, .08, .24, .84, .105,
        r"$x_n b=\beta_{gn^{-1}}(b)x_n\quad(b\in P)$", fontsize=22)
    ax.text(.5, .195, "Factoriality: xₙ*xₙ and xₙxₙ* are nonzero scalars; polar part is unitary",
            fontsize=14, color=INK, ha="center")
    arrow(ax, (.50, .16), (.50, .10))
    ax.text(.5, .055, r"$\beta_{gn^{-1}}$ inner  $\Longrightarrow$  $g=n\in N$",
            fontsize=23, color=TEAL, ha="center", va="center")
    ax.text(.5, .012, "Reverse inclusion: α_n = Ad(L_n), so the entire inner kernel is N.",
            fontsize=13, color=INK, ha="center")
    save(fig, "kernel-intertwiner")

    fig, ax = canvas("Finite-dimensional averaging cannot hide F₂",
                     "Exact implication for this regular tracial product. No scalar twist changes the diagonal shift.  |  TR29–TR32")
    box(ax, .035, .66, .40, .15,
        r"$F_i\uparrow M_\mu$,  finite spanning group $Q_i$"+"\n"+
        r"$\phi_i(T)=|Q_i|^{-1}\sum_{v\in Q_i}\phi_0(v^*Tv)$", fontsize=17)
    arrow(ax, (.235, .635), (.235, .54))
    box(ax, .035, .395, .40, .12,
        r"$\phi_i|_{M_\mu}=\tau_\mu$ and $F_i$-central"+"\n"+
        r"$|\phi_i(aT-Ta)|\leq2\|T\|\,\|a-a_i\|_2$", fontsize=17)
    arrow(ax, (.235, .37), (.235, .28))
    box(ax, .035, .135, .40, .12,
        "Limit ψ is M-central\n"+r"$f\mapsto\psi(D_f)$ is a left-invariant mean", fontsize=17)
    ax.text(.52, .80, "Two reduced-word partitions", fontsize=18, weight="bold", color=BLUE)
    colors = ["#d7e7f2", "#e5edf3", "#d7eee5", "#e4f0e9"]
    for y, labels, cs in [(.60, ("$A_+$", "$aA_-$"), colors[:2]),
                           (.38, ("$B_+$", "$bB_-$"), colors[2:])]:
        for k in range(2):
            ax.add_patch(Rectangle((.54+k*.19, y), .18, .115,
                                   facecolor=cs[k], edgecolor=BLUE, lw=1.4))
            ax.text(.63+k*.19, y+.0575, labels[k], fontsize=22, ha="center", va="center")
        ax.text(.93, y+.0575, "$=F_2$", fontsize=18, va="center")
    ax.text(.73, .545, "$m(A_+)+m(A_-)=1$", fontsize=19, ha="center", color=INK)
    ax.text(.73, .325, "$m(B_+)+m(B_-)=1$", fontsize=19, ha="center", color=INK)
    box(ax, .54, .15, .40, .12, "The four first-letter sets are disjoint\nand partition F₂ except {e}, of mass 0", fontsize=15, color=TEAL)
    ax.text(.52, .075, "Their total mass would be both 1 and 2.", fontsize=19,
            weight="bold", color=ORANGE)
    ax.text(.52, .025, "Therefore this F₂ regular product is not AFD.", fontsize=16, color=ORANGE)
    save(fig, "afd-mean-obstruction")


def check_identities():
    G = list(permutations(range(3)))
    identity = (0, 1, 2)
    index = {g: i for i, g in enumerate(G)}
    mul = lambda g, h: tuple(g[h[k]] for k in range(3))
    inv = lambda g: tuple(g.index(k) for k in range(3))
    ci = lambda n, g: mul(mul(inv(g), n), g)
    phase = {g: (i+1) % 13 for i, g in enumerate(G)}
    phase[identity] = 0
    me = lambda n, k: (phase[n]+phase[k]-phase[mul(n, k)]) % 13
    le = lambda n, g: (phase[ci(n, g)]-phase[n]) % 13
    counts = {"multiplier_triples": 0, "action_triples": 0,
              "compatibility_triples": 0, "inner_pairs": 0}
    for a in G:
        for b in G:
            for c in G:
                assert (me(a, b)+me(mul(a, b), c)-me(a, mul(b, c))-me(b, c)) % 13 == 0
                counts["multiplier_triples"] += 1
                assert (le(a, mul(b, c))-le(a, b)-le(ci(a, b), c)) % 13 == 0
                counts["action_triples"] += 1
                assert (le(a, c)+le(b, c)-le(mul(a, b), c)
                        -me(ci(a, c), ci(b, c))+me(a, b)) % 13 == 0
                counts["compatibility_triples"] += 1
            assert (le(a, b)-me(b, ci(a, b))+me(a, b)) % 13 == 0
            counts["inner_pairs"] += 1
    mu = lambda n, k: np.exp(2j*np.pi*me(n, k)/13)
    lam = lambda n, g: np.exp(2j*np.pi*le(n, g)/13)
    basis = []
    for i in range(3):
        for j in range(3):
            eij = np.zeros((3, 3), complex)
            eij[i, j] = 1
            basis.append(eij)
    op = lambda fn: np.column_stack([fn(e).reshape(-1) for e in basis])
    left = lambda a: op(lambda e: a@e)
    right = lambda a: op(lambda e: e@a)
    perm = {}
    implementer = {}
    for g in G:
        pg = np.zeros((3, 3), complex)
        for k in range(3):
            pg[g[k], k] = 1
        perm[g] = pg
        implementer[g] = op(lambda e: pg@e@pg.conj().T)
    dim = 54
    def blocks(fn):
        z = np.zeros((dim, dim), complex)
        for row, col, block in fn():
            z[9*row:9*(row+1), 9*col:9*(col+1)] = block
        return z
    la = lambda a: blocks(lambda: [(index[m], index[m], left(a)) for m in G])
    rb = lambda b: blocks(lambda: [(index[m], index[m], right(perm[m]@b@perm[m].conj().T)) for m in G])
    ln = lambda n: blocks(lambda: [(index[m], index[mul(inv(n), m)],
                                    mu(n, mul(inv(n), m))*implementer[n]) for m in G])
    rn = lambda n: blocks(lambda: [(index[m], index[mul(m, inv(n))],
                                    mu(mul(m, inv(n)), n)*np.eye(9)) for m in G])
    # W in coefficient coordinates S^{-1} W S. V_g transports both coefficient labels and matrices.
    wg = lambda g: blocks(lambda: [(index[m], index[ci(m, g)],
                                    lam(m, g)*implementer[g]) for m in G])
    L = {n: ln(n) for n in G}
    R = {n: rn(n) for n in G}
    W = {g: wg(g) for g in G}
    residuals = {}
    def test(name, x, y):
        residuals[name] = max(residuals.get(name, 0.), float(np.max(np.abs(x-y))))
    for n in G:
        for k in G:
            test("left_multiplier", L[n]@L[k], mu(n, k)*L[mul(n, k)])
            test("right_reverse_multiplier", R[n]@R[k], mu(k, n)*R[mul(k, n)])
            test("left_right_shift_commutation", L[n]@R[k], R[k]@L[n])
            test("W_action", W[n]@W[k], W[mul(n, k)])
            nk = mul(mul(n, k), inv(n))
            test("W_L_covariance", W[n]@L[k]@W[n].conj().T, lam(nk, n)*L[nk])
            test("inner_action_on_L", W[n]@L[k]@W[n].conj().T, L[n]@L[k]@L[n].conj().T)
        for b in basis:
            test("left_shift_right_base_commutation", L[n]@rb(b), rb(b)@L[n])
            test("left_base_right_shift_commutation", la(b)@R[n], R[n]@la(b))
            betab = perm[n]@b@perm[n].conj().T
            test("W_base_covariance", W[n]@la(b)@W[n].conj().T, la(betab))
            test("inner_action_on_base", W[n]@la(b)@W[n].conj().T, L[n]@la(b)@L[n].conj().T)
    for a in basis:
        for b in basis:
            test("left_right_base_commutation", la(a)@rb(b), rb(b)@la(a))
    gauge_phase = {n: (i+2) % 17 for i, n in enumerate(G)}
    gauge_phase[identity] = 0
    f = lambda n: np.exp(2j*np.pi*gauge_phase[n]/17)
    D = np.diag([f(m)**-1 for m in G for _ in range(9)])
    for n in G:
        Lnew = blocks(lambda: [(index[m], index[mul(inv(n), m)],
                               mu(n, mul(inv(n), m))*f(n)*f(mul(inv(n), m))/f(m)*implementer[n]) for m in G])
        test("gauge_left", D@L[n]@D.conj().T, f(n)**-1*Lnew)
        Wnew = blocks(lambda: [(index[m], index[ci(m, n)],
                               lam(m, n)*f(ci(m, n))/f(m)*implementer[n]) for m in G])
        test("gauge_W", D@W[n]@D.conj().T, Wnew)
    assert max(residuals.values()) < 2e-12, residuals
    result = {"passed": True, "exact_mod13_checks": counts,
              "matrix_model": "S3 regular coefficients on M3 Hilbert-Schmidt, dimension54",
              "maximum_absolute_residuals": residuals,
              "limit": "Finite checks detect coordinate errors; this finite beta is inner and is not a freeness model. General analytic/freeness/kernel/AFD arguments are written proofs."}
    return result


if __name__ == "__main__":
    checks = check_identities()
    models = {"two_sheet": {"N": "C2={e,t}", "mu": 1,
                            "regular_block_matrix": [["a", "b"], ["beta_t(b)", "beta_t(a)"]],
                            "expectation": "a", "L2_squared": "||a||2^2+||b||2^2"},
              "finite_kernel": {"G": "C2 x Z", "N": "C2", "mu": 1,
                                "lambda(t,t^epsilon z^k)": "(-1)^k", "inner_kernel": "C2"},
              "F2_partitions": {"first_letters": ["a", "a^-1", "b", "b^-1"],
                                "partitions": ["F2=A_plus disjoint_union aA_minus",
                                               "F2=B_plus disjoint_union bB_minus"],
                                "singleton_mass": 0, "four_piece_total": 1,
                                "two_partition_equations_total": 2}}
    (OUT/"models.json").write_text(json.dumps(models, indent=2)+"\n", encoding="utf-8")
    figures()
    outputs = []
    for name in ["two-sheet-fourier", "kernel-intertwiner", "afd-mean-obstruction"]:
        for ext in ["svg", "png"]:
            p = OUT/f"{name}.{ext}"
            outputs.append({"name": p.name, "bytes": p.stat().st_size,
                            "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    checks["figure_outputs"] = outputs
    (OUT/"checks.json").write_text(json.dumps(checks, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"passed": True, "max_residual": max(checks["maximum_absolute_residuals"].values()),
                      "figure_outputs": outputs}, indent=2))
