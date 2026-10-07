"""Original CC0 finite checks for the typed anchored descent proofs.

The finite model supplements written proofs. It does not establish infinite
KK assertions, product existence, exactness, or a nonamenable quotient claim.
"""
from pathlib import Path
import argparse
import itertools
import json
import numpy as np

HERE = Path(__file__).resolve().parent
RNG = np.random.default_rng(6100623)
G = list(itertools.product(range(2), range(2), range(2)))
CHECKS = []


def check(name, condition, detail=None):
    CHECKS.append({"name": name, "passed": bool(condition), "detail": detail})


def close(a, b):
    return np.allclose(a, b, atol=3e-10, rtol=3e-10)


def src(g):
    return g[2]


def ran(g):
    return g[2] ^ g[0]


def inv(g):
    return g[0], g[1], ran(g)


def comp(g, h):
    assert src(g) == ran(h)
    return g[0] ^ h[0], g[1] ^ h[1], src(h)


UNITS = [(0, 0, y) for y in range(2)]
J = [np.eye(2), np.array([[1., -1.], [1., 1.]]) / np.sqrt(2)]
K = [np.eye(3), np.array([[0., 0., 1.], [0., 1., 0.], [-1., 0., 0.]])]
R = np.diag([1., -1.])
Q = np.diag([1., 1., -1.])
U = {g: J[ran(g)] @ (R if g[1] else np.eye(2)) @ J[src(g)].T for g in G}
V = {g: K[ran(g)] @ (Q if g[1] else np.eye(3)) @ K[src(g)].T for g in G}
UV = {g: np.kron(U[g], V[g]) for g in G}
GR1 = [j @ np.diag([1., -1.]) @ j.T for j in J]
GR2 = [k @ np.diag([1., -1., 1.]) @ k.T for k in K]


def rnd(shape=()):
    return RNG.normal(size=shape) + 1j * RNG.normal(size=shape)


def vectors(d):
    return {g: rnd((d,)) for g in G}


def scalar_coeff():
    return {g: complex(rnd()) for g in G}


def matrix_coeff():
    return {g: rnd((2, 2)) for g in G}


def alpha(g, a):
    return U[g] @ a @ U[g].conj().T


def convolution(a, b, action=lambda g, x: x):
    out = {}
    for g in G:
        out[g] = sum((multiply(a[h], action(h, b[comp(inv(h), g)]))
                      for h in G if ran(h) == ran(g)), 0)
    return out


def multiply(a, b):
    return a * b if np.ndim(a) == 0 or np.ndim(b) == 0 else a @ b


def star(a, action=lambda g, x: x):
    return {g: action(g, np.asarray(a[inv(g)]).conj().T) for g in G}


def right(xi, b):
    return {g: sum((xi[h] * b[comp(inv(h), g)]
                    for h in G if ran(h) == ran(g)), np.zeros_like(xi[g])) for g in G}


def inner(xi, eta):
    return {g: sum((np.vdot(xi[inv(h)], eta[comp(inv(h), g)])
                    for h in G if ran(h) == ran(g)), 0j) for g in G}


def left(a, xi, action, representation=lambda y, b: b):
    return {g: sum((multiply(representation(ran(g), a[h]),
                            action[h] @ xi[comp(inv(h), g)])
                    for h in G if ran(h) == ran(g)), np.zeros_like(xi[g])) for g in G}


def same_core(a, b):
    return all(close(a[g], b[g]) for g in G)


def regular(a, x, d=1, action=lambda g, b: b):
    col = [g for g in G if src(g) == x]
    blocks = [[np.atleast_2d(action(inv(g), a[comp(g, inv(l))]))
               for l in col] for g in col]
    mat = np.block(blocks)
    assert mat.shape == (len(col) * d, len(col) * d)
    return mat


def tensor_core(xi, eta):
    return {g: sum((np.kron(xi[h], V[h] @ eta[comp(inv(h), g)])
                    for h in G if ran(h) == ran(g)), np.zeros(6, dtype=complex)) for g in G}


def reg_tensor(xi, zeta, x):
    return {g: sum((U[g].conj().T @ xi[h] * zeta[comp(inv(h), g)]
                    for h in G if ran(h) == ran(g)), np.zeros(2, dtype=complex))
            for g in G if src(g) == x}


def unit_vectors(e):
    return {g: e[ran(g)] if g in UNITS else np.zeros_like(e[0]) for g in G}


def pointwise(T, xi):
    return {g: T[ran(g)] @ xi[g] for g in G}


def finite_model():
    arrow_trials = 0
    exact_action = True
    for g in G:
        exact_action &= comp(g, inv(g)) == UNITS[ran(g)]
        exact_action &= comp(inv(g), g) == UNITS[src(g)]
        exact_action &= close(U[g].conj().T @ U[g], np.eye(2))
        exact_action &= close(V[g].conj().T @ V[g], np.eye(3))
        exact_action &= close(U[g] @ GR1[src(g)], GR1[ran(g)] @ U[g])
        exact_action &= close(V[g] @ GR2[src(g)], GR2[ran(g)] @ V[g])
        for h in G:
            if src(g) != ran(h):
                continue
            gh = comp(g, h)
            exact_action &= close(U[gh], U[g] @ U[h]) and close(V[gh], V[g] @ V[h])
            for k in G:
                if src(h) == ran(k):
                    exact_action &= comp(gh, k) == comp(g, comp(h, k))
                    arrow_trials += 1
    check("actual source/range composition, inverses and even arrow actions", exact_action,
          {"associativity_trials": arrow_trials, "arrows": len(G)})
    check("distinct nontrivial isotropy retained", (0, 1, 0) in G and
          close(U[(0, 1, 0)], R) and not close(R, np.eye(2)))

    names = ["coefficient convolution and adjoint", "positive core inner product",
             "right module balance and adjoint inner product", "unit tensor inner product",
             "reduced source-column intertwining", "degenerate reduced matrix norm",
             "crossed tensor balance", "crossed tensor exact inner product",
             "crossed tensor left and right actions", "unit-section tensor dense generators",
             "ordinary rank-one compact extension", "rectangular compact convolution kernel",
             "Clifford multiplication and adjoint signs", "descended product creation kernel",
             "first descended product operator and positive anticommutator"]
    passed = {name: True for name in names}
    trials = 24
    f1base = np.array([[0., 1.], [1., 0.]])
    f2base = np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., 0.]])
    F1 = [j @ f1base @ j.T for j in J]
    F2 = [k @ f2base @ k.T for k in K]
    S = [np.kron(f, np.eye(3)) for f in F1]
    F = [(S[y] + np.kron(GR1[y], F2[y])) / np.sqrt(2) for y in range(2)]

    for trial in range(trials):
        a, a2 = matrix_coeff(), matrix_coeff()
        b, c = scalar_coeff(), scalar_coeff()
        xi, xi2 = vectors(2), vectors(2)
        eta, eta2 = vectors(3), vectors(3)
        for x in range(2):
            lam_a = regular(a, x, 2, alpha)
            passed[names[0]] &= close(regular(convolution(a, a2, alpha), x, 2, alpha),
                                      lam_a @ regular(a2, x, 2, alpha))
            passed[names[0]] &= close(regular(star(a, alpha), x, 2, alpha), lam_a.conj().T)
            positive = regular(inner(xi, xi), x)
            passed[names[1]] &= close(positive, positive.conj().T)
            passed[names[1]] &= np.linalg.eigvalsh(positive).min() > -3e-9
            col = [g for g in G if src(g) == x]
            zeta = {g: complex(rnd()) for g in col}
            rt = reg_tensor(xi, zeta, x)
            rt2 = reg_tensor(left(a, xi, U), zeta, x)
            flat = np.concatenate([rt[g] for g in col])
            flat2 = np.concatenate([rt2[g] for g in col])
            passed[names[4]] &= close(flat2, lam_a @ flat)
            deg_blocks = [[np.block([[alpha(inv(g), a[comp(g, inv(l))]), np.zeros((2, 1))],
                                      [np.zeros((1, 2)), np.zeros((1, 1))]]) for l in col] for g in col]
            passed[names[5]] &= close(np.linalg.norm(np.block(deg_blocks), 2), np.linalg.norm(lam_a, 2))

        passed[names[2]] &= same_core(inner(right(xi, b), xi2), convolution(star(b), inner(xi, xi2)))
        passed[names[2]] &= same_core(star(inner(xi, xi2)), inner(xi2, xi))
        e, f = [rnd((2,)) for _ in range(2)], [rnd((2,)) for _ in range(2)]
        xb = {g: e[ran(g)] * b[g] for g in G}
        fc = {g: f[ran(g)] * c[g] for g in G}
        ie = {g: np.vdot(e[ran(g)], f[ran(g)]) if g in UNITS else 0j for g in G}
        passed[names[3]] &= same_core(inner(xb, fc), convolution(convolution(star(b), ie), c))

        passed[names[6]] &= same_core(tensor_core(right(xi, b), eta), tensor_core(xi, left(b, eta, V)))
        wx, wy = tensor_core(xi, eta), tensor_core(xi2, eta2)
        passed[names[7]] &= same_core(inner(wx, wy), inner(eta, left(inner(xi, xi2), eta2, V)))
        passed[names[8]] &= same_core(left(a, wx, UV, lambda y, m: np.kron(m, np.eye(3))),
                                      tensor_core(left(a, xi, U), eta))
        passed[names[8]] &= same_core(right(wx, b), tensor_core(xi, right(eta, b)))
        passed[names[9]] &= same_core(tensor_core(unit_vectors(e), eta),
                                      {g: np.kron(e[ran(g)], eta[g]) for g in G})

        bu, cu = [complex(rnd()) for _ in range(2)], [complex(rnd()) for _ in range(2)]
        eu, fu = unit_vectors([e[y] * bu[y] for y in range(2)]), unit_vectors([f[y] * cu[y] for y in range(2)])
        rank = [np.outer(e[y] * bu[y], (f[y] * cu[y]).conj()) for y in range(2)]
        passed[names[10]] &= same_core(right(eu, inner(fu, xi)), pointwise(rank, xi))
        kernel = {g: c[g] * np.outer(e[ran(g)], f[ran(g)].conj()) for g in G}
        kk = {g: sum((kernel[h] @ U[h] @ xi[comp(inv(h), g)]
                      for h in G if ran(h) == ran(g)), np.zeros(2, dtype=complex)) for g in G}
        theta = [np.outer(e[y], f[y].conj()) for y in range(2)]
        passed[names[11]] &= same_core(kk, pointwise(theta, left(c, xi, U)))

        parity_a, parity_b = trial % 2, (trial // 2) % 2
        aa = {g: (a[g] + (-1)**parity_a * GR1[ran(g)] @ a[g] @ GR1[ran(g)]) / 2 for g in G}
        ab = {g: (a2[g] + (-1)**parity_b * GR1[ran(g)] @ a2[g] @ GR1[ran(g)]) / 2 for g in G}
        def cliff_mat(y, m, eps):
            base = np.block([[m, np.zeros((2, 2))],
                             [np.zeros((2, 2)), GR1[y] @ m @ GR1[y]]])
            flip = np.block([[np.zeros((2, 2)), np.eye(2)], [np.eye(2), np.zeros((2, 2))]])
            return base @ flip if eps else base
        hatU = {g: np.block([[U[g], np.zeros((2, 2))], [np.zeros((2, 2)), U[g]]]) for g in G}
        ca = {g: cliff_mat(ran(g), aa[g], True) for g in G}
        cb = {g: cliff_mat(ran(g), ab[g], False) for g in G}
        cprod = convolution(ca, cb, lambda g, m: hatU[g] @ m @ hatU[g].conj().T)
        expected = convolution(aa, ab, alpha)
        passed[names[12]] &= all(close(cprod[g], (-1)**parity_b * cliff_mat(ran(g), expected[g], True)) for g in G)
        castar = star(ca, lambda g, m: hatU[g] @ m @ hatU[g].conj().T)
        astar = star(aa, alpha)
        passed[names[12]] &= all(close(castar[g], (-1)**parity_a * cliff_mat(ran(g), astar[g], True)) for g in G)

        parity = trial % 2
        xh = {g: (xi[g] + (-1)**parity * GR1[ran(g)] @ xi[g]) / 2 for g in G}
        w = tensor_core(xh, eta)
        error = {g: F[ran(g)] @ w[g] - (-1)**parity * tensor_core(xh, pointwise(F2, eta))[g] for g in G}
        d = {}
        for h in G:
            y = ran(h)
            creation = np.kron(xh[h].reshape(2, 1), np.eye(3))
            d[h] = F[y] @ creation - (-1)**parity * creation @ F2[y]
            d[h] += (-1)**parity * creation @ (F2[y] - V[h] @ F2[src(h)] @ V[h].conj().T)
        ke = {g: sum((d[h] @ V[h] @ eta[comp(inv(h), g)]
                      for h in G if ran(h) == ran(g)), np.zeros(6, dtype=complex)) for g in G}
        passed[names[13]] &= same_core(error, ke)
        passed[names[14]] &= same_core(pointwise(S, w), tensor_core(pointwise(F1, xh), eta))
        for y in range(2):
            passed[names[14]] &= close(S[y] @ F[y] + F[y] @ S[y], np.sqrt(2) * np.eye(6))
            passed[names[14]] &= close(np.kron(GR1[y], GR2[y]) @ F[y], -F[y] @ np.kron(GR1[y], GR2[y]))
            passed[names[14]] &= np.linalg.norm(F[y], 2) <= 1 + 1e-10

    for name in names:
        check(name, passed[name], {"random_trials": trials, "seed": 6100623})
    ident = {g: np.eye(2) if g in UNITS else np.zeros((2, 2)) for g in G}
    check("actual unit coefficient approximate identity in finite model",
          same_core(convolution(ident, a, alpha), a) and same_core(convolution(a, ident, alpha), a))
    matrix_module_ok = True
    for _ in range(24):
        x, y, u, v, b = [matrix_coeff() for _ in range(5)]
        ip = lambda first, second: convolution(star(first, alpha), second, alpha)
        xb = convolution(x, b, alpha)
        matrix_module_ok &= same_core(ip(xb, y), convolution(star(b, alpha), ip(x, y), alpha))
        matrix_module_ok &= same_core(convolution(convolution(x, b, alpha), u, alpha),
                                     convolution(x, convolution(b, u, alpha), alpha))
        wx, wy = convolution(x, u, alpha), convolution(y, v, alpha)
        matrix_module_ok &= same_core(ip(wx, wy), ip(u, convolution(ip(x, y), v, alpha)))
    check("noncommutative transported coefficient module and tensor identities", matrix_module_ok,
          {"coefficient": "M2(C), nontrivial conjugation action", "random_trials": 24})


def main(output):
    finite_model()
    result = {"schema": "anchored-etale-descent-finite-self-check/v1",
              "interpretation": "Finite checks supplement written infinite proofs; no product-existence or reduced-exactness theorem inferred.",
              "finite_model": "C2 x C2 acting on two units; nontrivial second-factor isotropy, moving graded 2/3-dimensional frames",
              "checks": CHECKS, "passed": all(c["passed"] for c in CHECKS)}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": result["passed"], "checks": len(CHECKS)}))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "finite-checks.json")
    main(parser.parse_args().output.resolve())
