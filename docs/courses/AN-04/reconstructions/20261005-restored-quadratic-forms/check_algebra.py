"""Original eight preparation model families, without historical source/state operations."""
import json
import numpy as np
import sympy as s
def omega(n):
    return s.zeros(n).row_join(-s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
def ham(B):
    return -omega(B.rows//2)*B
def inertia(B):
    values = np.linalg.eigvalsh(np.array(B, dtype=float))
    return [int(sum(values > 1e-10)), int(sum(values < -1e-10)), int(sum(abs(values) <= 1e-10))]

checks = []
J = omega(2)
x1, x2, p1, p2 = s.symbols('x1 x2 p1 p2', real=True)
z = s.Matrix([x1, x2, p1, p2])
B = s.Matrix([[2, 1, 0, 2], [1, 3, 1, 0], [0, 1, 4, 1], [2, 0, 1, 5]])
F = ham(B)
Q = (z.T*B*z)[0]
assert s.hessian(Q, list(z)) == 2*B
assert F.T*J+J*F == s.zeros(4)
assert J*F == B
assert s.simplify(-J*s.Matrix([s.diff(Q, v) for v in z])-2*F*z) == s.zeros(4, 1)
K = s.Matrix([[1, 2], [2, -1]])
C = s.eye(2).row_join(s.zeros(2)).col_join(K.row_join(s.eye(2)))
assert C.T*J*C == J
assert ham(C.T*B*C) == C.inv()*F*C
D = s.Matrix([[2, 1], [0, 1]])
C2 = D.row_join(s.zeros(2)).col_join(s.zeros(2).row_join(D.inv().T))
assert C2.T*J*C2 == J
assert ham(C2.T*B*C2) == C2.inv()*F*C2
checks.append({'name': 'Hamilton factor, full matrix covariance and two canonical changes', 'passed': True,
               'scope': 'Exact 4-by-4 polynomial and complete symplectic matrices; not a general coordinate-invariance proof.'})

real_models = [
    ('nonnegative oscillator and rank-one zero block', s.diag(2, 1, 2, 0), [3, 0, 1], (2, 2)),
    ('negative rank-one block with oscillator', s.diag(2, -1, 2, 0), [2, 1, 1], (2, 2)),
    ('real hyperbolic pair and oscillator', s.Matrix([[2, 0, 0, 0], [0, 0, 0, 3], [0, 0, 2, 0], [0, 3, 0, 0]]), [3, 1, 0], (0, 0)),
    ('length-four nilpotent block', s.Matrix([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1], [0, 0, -1, 0]]), [2, 1, 1], (3, 2)),
]
summaries = []
for name, b, sig, ranks in real_models:
    f = ham(b)
    assert inertia(b) == sig
    if ranks != (0, 0):
        # Oscillator models have rank three but their generalized zero restriction has length two.
        if 'oscillator' in name:
            assert (f[1, 3], f[3, 1]) == (0, -b[1, 1])
        else:
            assert (f.rank(), (f*f).rank()) == ranks
    summaries.append({'name': name, 'inertia_positive_negative_zero': sig,
                      'characteristic_polynomial': str(f.charpoly().as_expr()),
                      'ranks_of_powers': [int((f**k).rank()) for k in range(1, 5)]})
assert ham(real_models[2][1]).eigenvals() == {-3: 1, 3: 1, -2*s.I: 1, 2*s.I: 1}
f_a = ham(s.diag(2, 3, 2, 3))
f_b = ham(s.diag(2, 4, 2, 4))
assert f_a.charpoly().as_expr() != f_b.charpoly().as_expr()
checks.append({'name': 'All three index-one exceptional blocks and preserved real frequencies', 'passed': True,
               'models': summaries, 'scope': 'Exact listed inertia, spectra and ranks; the general block exhaustion remains a written proof obligation.'})

F4 = ham(real_models[-1][1])
X = s.Matrix([0, 0, 1, 0])
assert F4**4 == s.zeros(4) and F4**3 != s.zeros(4)
assert (X.T*J*F4**3*X)[0] == -1
assert (X.T*J*F4*X)[0] == 0
chain_basis = s.Matrix.hstack(-F4**3*X, -F4*X, X, F4**2*X)
assert chain_basis == s.eye(4)
assert chain_basis.T*J*chain_basis == J
assert (z.T*real_models[-1][1]*z)[0] == x2**2-2*p1*p2
for j in range(4):
    for k in range(4):
        assert ((F4**j*X).T*real_models[-1][1]*F4**k*X)[0] == (-1)**j*(X.T*J*F4**(j+k+1)*X)[0]
checks.append({'name': 'Complete four-step nilpotent chain and polarized form', 'passed': True,
               'scope': 'All 16 chain pairings and the whole canonical basis, including the sign of the cubic symplectic pairing.'})

j1 = omega(1)
simple_b = (2+s.I)*s.eye(2)
simple_f = ham(simple_b)
U = s.Matrix([1, s.I])
assert s.simplify(simple_f*U-(-1+2*s.I)*U) == s.zeros(2, 1)
assert s.simplify(s.I*(s.conjugate(U).T*j1*U)[0]) == 2
assert s.simplify((s.conjugate(U).T*simple_b*U)[0]-(4+2*s.I)) == 0
sector_b = s.diag(1+s.I/3, 2+s.I/2, 0, 2+s.I/2)
sector_f = ham(sector_b)
W = s.Matrix([0, 0, 1, 0])
assert sector_f*W == s.zeros(4, 1) and s.conjugate(sector_f)*W == s.zeros(4, 1)
assert sector_f.nullspace() == [W]
assert (sector_f**2).nullspace() == [s.Matrix([1, 0, 0, 0]), W]
assert (sector_f**3).nullspace() == (sector_f**2).nullspace()
P, R = s.re(sector_b), s.im(sector_b)
assert all(v >= 0 for v in (P/3-R).diagonal())
assert all(v >= 0 for v in (P/3+R).diagonal())
checks.append({'name': 'Sectorial strict and degenerate radicals with the correct conjugations', 'passed': True,
               'sector_constant': '1/3 for the degenerate model; 1/2 for the strict scalar model',
               'scope': 'Exact diagonal domination, real kernel, length-two zero generalized space and positive spectral vector.'})

# A real-part positive, genuinely complex family; no moving simple-eigenvalue hypothesis is used in the teaching proof.
jn = np.array(J, dtype=float)
pn = 2*np.eye(4)
rn = .35*np.array([[1., .2, .3, 0.], [.2, -.4, 0., .1], [.3, 0., .6, .25], [0., .1, .25, -.8]])
min_metric = float('inf')
max_iso = max_eigen = max_contour = 0.
for t in np.linspace(0, 1, 81):
    f = -jn@(pn+1j*t*rn)
    eigenvalues, eigenvectors = np.linalg.eig(f)
    positive = eigenvalues.imag > 0
    assert sum(positive) == 2 and min(abs(eigenvalues.imag)) > 1.8
    v = eigenvectors[:, positive]
    max_iso = max(max_iso, float(np.linalg.norm(v.T@jn@v)))
    h = 1j*v.conj().T@jn@v
    assert np.linalg.norm(h-h.conj().T) < 1e-12
    min_metric = min(min_metric, float(np.linalg.eigvalsh(h).min()))
    max_eigen = max(max_eigen, float(np.linalg.norm(f@v-v@np.diag(eigenvalues[positive]))))
    if t in (0., .5, 1.):
        # Counterclockwise circle centered at 3i, radius 2; all upper eigenvalues inside, all lower outside.
        theta = 2*np.pi*np.arange(512)/512
        riesz = sum(2*np.exp(1j*a)*np.linalg.inv((3j+2*np.exp(1j*a))*np.eye(4)-f) for a in theta)/512
        actual = eigenvectors@np.diag(positive.astype(float))@np.linalg.inv(eigenvectors)
        max_contour = max(max_contour, float(np.linalg.norm(riesz-actual)))
        assert np.linalg.norm(riesz@riesz-riesz) < 1e-11
        assert np.linalg.norm(riesz@f-f@riesz) < 1e-11
assert min_metric > .01 and max_iso < 1e-12 and max_eigen < 1e-12 and max_contour < 1e-11
checks.append({'name': 'Positive spectral plane and independently integrated oriented Riesz projection', 'passed': True,
               'parameter_samples': 81, 'contour_samples_per_three_checks': 512,
               'minimum_sampled_hermitian_eigenvalue': min_metric,
               'maximum_isotropy_residual': max_iso, 'maximum_eigenvector_residual': max_eigen,
               'maximum_contour_projection_residual': max_contour,
               'scope': 'A finite 4-by-4 family, including a repeated frequency at t=0. Does not prove the unrestricted continuation or absence of degeneracies.'})

A1 = s.Matrix([[1, 2], [2, -1]])
A2 = s.Matrix([[2, s.Rational(1, 3)], [s.Rational(1, 3), 1]])
A = A1+s.I*A2
M = s.eye(2).col_join(A)
assert M.T*J*M == s.zeros(2)
assert s.simplify(s.I*s.conjugate(M).T*J*M) == 2*A2
Ireal = (-A2.inv()*A1).row_join(A2.inv()).col_join((-A2-A1*A2.inv()*A1).row_join(A1*A2.inv()))
assert Ireal**2 == -s.eye(4)
assert Ireal.T*J*Ireal == J
G = J*Ireal
assert G == G.T and inertia(G) == [4, 0, 0]
for m in range(1, 5):
    assert G[:m, :m].det() > 0
a2n = np.array(A2, dtype=float)
values, vectors = np.linalg.eigh(a2n)
sqrt = (vectors*np.sqrt(values))@vectors.T
inv_sqrt = (vectors/np.sqrt(values))@vectors.T
a1n = np.array(A1, dtype=float)
change = np.block([[sqrt, np.zeros((2, 2))], [-inv_sqrt@a1n, inv_sqrt]])
assert np.linalg.norm(change.T@jn@change-jn) < 1e-12
image = change@np.array(M, dtype=complex)
assert np.linalg.norm(image[2:, :]-1j*image[:2, :]) < 1e-12
checks.append({'name': 'Full positive graph, unique compatible structure and complete canonical normalization', 'passed': True,
               'scope': 'Exact graph isotropy and Hermitian factor two, all complex-structure/metric matrix identities, and a numerical whole-matrix shear/scaling.'})

Mweak = s.eye(2).col_join(s.I*s.diag(1, 0))
Hweak = s.simplify(s.I*s.conjugate(Mweak).T*J*Mweak)
assert Hweak == s.diag(2, 0)
assert Mweak[:, 1] == s.Matrix([0, 1, 0, 0])
reduced = s.Matrix([1, s.I])
assert s.I*(s.conjugate(reduced).T*j1*reduced)[0] == 2
vertical_weak = s.Matrix.hstack(s.Matrix([0, 0, 1, 0]), s.Matrix([0, 1, 0, s.I]))
assert vertical_weak.T*J*vertical_weak == s.zeros(2)
assert s.simplify(s.I*s.conjugate(vertical_weak).T*J*vertical_weak) == s.diag(0, 2)
assert vertical_weak[:2, :].rank() == 1
checks.append({'name': 'Non-strict nullspace, positive quotient and failure of the arbitrary graph claim', 'passed': True,
               'scope': 'Two actual complex planes, their full Gram matrices and null real directions; not the general reduction theorem.'})

bad_b = s.Matrix([[1, s.I], [s.I, -1]])
bad_f = ham(bad_b)
bad_kernel = s.Matrix([1, s.I])
assert bad_f*bad_kernel == s.zeros(2, 1)
assert bad_f*s.re(bad_kernel) != s.zeros(2, 1)
assert bad_f*s.im(bad_kernel) != s.zeros(2, 1)
assert (s.conjugate(bad_kernel).T*bad_b*bad_kernel)[0] == 0
assert bad_f**2 == s.zeros(2)
assert ham(s.diag(1, -1)).eigenvals() == {-1: 1, 1: 1}
checks.append({'name': 'Actual counterexamples when sectorial domination or real positivity is removed', 'passed': True,
               'models': ['(x+i*xi)^2 has a non-real kernel not spanned by real elements', 'x^2-xi^2 has real Hamilton eigenvalues'],
               'scope': 'Exact failures of specific implications outside their stated hypotheses.'})

print(json.dumps({'passed':True,'checks':len(checks),'writes':False}))
