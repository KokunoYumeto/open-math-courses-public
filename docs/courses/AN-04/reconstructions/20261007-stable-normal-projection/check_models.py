"""Exact finite counterchecks; the analytic theorems are proved in the source."""
from pathlib import Path
import json, hashlib
import sympy as s
import mpmath as mp

ROOT = Path(__file__).resolve().parent
z, t = s.symbols('z t', real=True)
I = s.I
eye = s.eye(2)
upper = I * eye + s.Matrix([[0, 1], [0, 0]])
lower = -2 * I * eye + s.Matrix([[0, 0], [1, 0]])
M = s.Matrix([[1, 2], [0, 3]])
coeff = [M * upper * lower, -M * (upper + lower), M]

def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)

def companion(a):
    n = a[0].rows
    m = len(a) - 1
    C = s.zeros(m*n)
    for j in range(m-1):
        C[j*n:(j+1)*n, (j+1)*n:(j+2)*n] = s.eye(n)
    for j in range(m):
        C[(m-1)*n:m*n, j*n:(j+1)*n] = -a[m].inv()*a[j]
    return C

def residue_projection(a, upper_root):
    n = a[0].rows
    m = len(a)-1
    poly = sum((a[j]*z**j for j in range(m+1)), s.zeros(n))
    inv = poly.inv()
    q = s.zeros(m*n)
    for k in range(m):
        for aindex in range(m):
            term = sum((z**(k+b)*inv*a[aindex+b+1]
                        for b in range(m-aindex)), s.zeros(n))
            def residue(entry):
                # Every fixture has pole order at most two. Exact cancellation
                # exposes a regular rational function, whose derivative is
                # the simple-pole coefficient; no generic series is needed.
                regular = s.cancel((z-upper_root)**2*entry, extension=I)
                denominator = s.denom(regular)
                assert s.simplify(denominator.subs(z, upper_root)) != 0
                return s.simplify(s.diff(regular, z).subs(z, upper_root))
            q[k*n:(k+1)*n, aindex*n:(aindex+1)*n] = term.applyfunc(residue)
    return q

C = companion(coeff)
poly = sum((coeff[j]*z**j for j in range(3)), s.zeros(2))
assert s.simplify((z*s.eye(4)-C).det()-poly.det()/M.det()) == 0
assert s.factor(poly.det()/M.det()) == (z-I)**2*(z+2*I)**2
x = s.Matrix(s.symbols('x0:4'))
numerator = (coeff[1]+z*M)*x[:2, 0]+M*x[2:4, 0]
w0 = poly.inv()*numerator
w = w0.col_join(z*w0-x[:2, 0])
assert zero((z*s.eye(4)-C)*w-x)
q = residue_projection(coeff, I)
assert zero(q*q-q) and zero(C*q-q*C) and s.trace(q) == 2
assert zero((C-I*s.eye(4))**2*q)
assert zero((C+2*I*s.eye(4))**2*(s.eye(4)-q))
print('Verified the original repeated-pole projection and both spectral summands.', flush=True)
gauge = s.Rational(3, 2)
shifted = [coeff[0]+gauge*coeff[1]+gauge**2*M, coeff[1]+2*gauge*M, M]
W = s.eye(4)
W[2:4, 0:2] = -gauge*eye
assert zero(residue_projection(shifted, I-gauge)-W*q*W.inv())
c = s.Rational(2)
normal_scaled = [coeff[j]*c**j for j in range(3)]
Jc = s.diag(1, 1, 1/c, 1/c)
assert zero(residue_projection(normal_scaled, I/c)-Jc*q*Jc.inv())
rho = s.Rational(3)
frequency_scaled = [coeff[j]*rho**(2-j) for j in range(3)]
Srho = s.diag(1, 1, rho, rho)
assert zero(residue_projection(frequency_scaled, rho*I)-Srho*q*Srho.inv())
print('Verified all three exact jet comparisons.', flush=True)
checks = [{'name': 'Original leading matrix, repeated roots and all jet comparisons',
           'passed': True, 'state_dimension': 4, 'upper_multiplicity': 2,
           'retained': ['determinant factor', 'resolvent numerator', 'both spectral summands',
                        'gauge', 'normal scale', 'positive frequency scale']}]

mp.mp.dps = 60
cases = 0
R = mp.mpf(160)
max_tail = mp.mpf(0)
for sign in [-1, 1]:
    lam = mp.mpc(2, sign)
    for h in range(1, 5):
        for kappa in [-2, 0, 3]:
            # t = sign*u parametrizes the relevant half-line; dt becomes du.
            phase = (sign*mp.j)**h/mp.factorial(h-1)
            value = mp.quad(lambda u: phase*u**(h-1)*mp.exp(
                mp.j*(lam-kappa)*sign*u), list(range(0, 161, 8)))
            # The absolute tail is explicit by h-1 integrations by parts,
            # since both selected poles have |Im lambda| = 1.
            tail = mp.exp(-R)*sum(R**j/mp.factorial(j) for j in range(h))
            max_tail = max(max_tail, tail)
            target = (mp.mpf(kappa)-lam)**(-h)
            assert tail < mp.mpf('1e-60')
            assert abs(value-target)+tail < mp.mpf('1e-45'), (sign,h,kappa,value,target)
            cases += 1
checks.append({'name': 'Tested Fourier signs and factorials for both pole half-planes',
               'passed': True, 'absolutely_convergent_integrals': cases,
               'pole_orders': [1, 2, 3, 4], 'decimal_precision': 60,
               'quadrature_interval': [0, 160], 'maximum_absolute_tail_bound': str(max_tail)})
print('Verified all 24 absolutely convergent Fourier integrals.', flush=True)

N0 = s.Matrix([[0, 1], [0, 0]])
u = s.exp(-2*t)*(eye-t*N0)*s.Matrix([0, 1])
assert zero(-I*u.diff(t)-I*(2*eye+N0)*u)
assert u.subs(t, 0) == s.Matrix([0, 1])
assert u == s.Matrix([-t*s.exp(-2*t), s.exp(-2*t)])
assert zero(residue_projection([-I*(2*eye+N0), eye], 2*I)-eye)
checks.append({'name': 'Nilpotent stable solution retains the second initial coordinate',
               'passed': True, 'upper_root': '2i', 'algebraic_multiplicity': 2,
               'geometric_multiplicity': 1})

M1 = s.Matrix([[1, 0], [1, 1]])
C1 = I*s.Matrix([[1, -2], [0, -1]])
actual = residue_projection([-M1*C1, M1], I)
assert actual == s.Matrix([[1, -1], [0, 0]])
wrong = M1*actual*M1.inv()
assert wrong == s.Matrix([[2, -1], [2, -1]]) and wrong != actual
r = s.symbols('rho', positive=True)
qlap = s.Matrix([[1, 1/(I*r)], [I*r, 1]])/2
assert zero(qlap*qlap-qlap)
assert qlap*s.Matrix([1, I*r]) == s.Matrix([1, I*r])
assert qlap*s.Matrix([1, -I*r]) == s.zeros(2, 1)
checks.append({'name': 'Correct projection, wrong factor order and weighted Laplace jets',
               'passed': True, 'nonorthogonal_projection_retained': True,
               'reversed_factor_projection_is_wrong': True})

result = {'schema': 'AN04-stable-normal-projection-models/v1',
          'source_sha256': hashlib.sha256((ROOT/'stable-normal-projection.md').read_bytes()).hexdigest(),
          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'passed': True, 'general_theorem_certified': False, 'checks': checks}
(ROOT/'model-check.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'passed': True, 'groups': len(checks), 'Fourier_integrals': cases}))
