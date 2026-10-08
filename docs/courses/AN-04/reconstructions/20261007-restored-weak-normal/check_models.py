"""Exact finite checks for U067. These supplement, never replace, its proofs."""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as S

HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
groups = []

# A two-space-variable model, with unrestricted smooth time dependence.
t, x, y, tau, xi, zeta = S.symbols('t x y tau xi zeta', real=True)
a, b, c = (S.Function(k)(t, x, y) for k in ['a', 'b', 'c'])
p = tau**2 - a*xi**2 - 2*b*xi*zeta - c*zeta**2
base, fiber = (t, x, y), (tau, xi, zeta)
def hp(f):
    return sum(S.diff(p, v)*S.diff(f, u)-S.diff(p, u)*S.diff(f, v)
               for u, v in zip(base, fiber))
sigma = x*xi
expected = (-2*a+x*S.diff(a,x))*xi**2 + 2*(-b+x*S.diff(b,x))*xi*zeta + x*S.diff(c,x)*zeta**2
assert S.simplify(hp(sigma)-expected) == 0
assert S.simplify(hp(tau)-(S.diff(a,t)*xi**2+2*S.diff(b,t)*xi*zeta+S.diff(c,t)*zeta**2)) == 0
for sign in [-1, 1]:
    lam = sign*tau
    eta, n, r = -sigma/lam, xi/lam, zeta/lam
    e2 = -x*S.diff(a,x)-eta*sign*S.diff(a,t)
    e1 = -2*(b+x*S.diff(b,x))*r-2*eta*sign*S.diff(b,t)*r
    e0 = -x*S.diff(c,x)*r**2-eta*sign*S.diff(c,t)*r**2
    expected = 2*(1-c*r**2)-2*p/lam**2+e0+e1*n+e2*n**2
    assert S.simplify(hp(eta)/lam-expected) == 0
groups.append({'name':'HN14–HN16 variable-coefficient clock, both frequency signs',
               'cases':4, 'scope':'Symbolic scalar principal form with one normal and one transverse spatial coordinate.'})

# Exact positive-frequency flat model and its Hamilton/physical-time conversion.
v = S.sqrt(3)/2
for time in [S.Rational(k,4) for k in range(-4,5)]:
    xpos = v*abs(time)
    normal = v if time < 0 else -v
    compressed = S.simplify(xpos*normal)
    assert compressed == -3*time/4
    assert 1-normal**2-S.Rational(1,4) == 0
    assert -compressed == 3*time/4
assert S.Rational(3,4)*2 == S.Rational(3,2)
groups.append({'name':'RB7 exact flat roots, compressed clock and time conversion',
               'cases':10, 'scope':'Nine exact points, plus de/dHamilton = (de/dt)(dt/dHamilton).'})

# Rational kappa values make sqrt(D) rational; all inequalities are exact.
cases = 0
for kappa, c0, cg, kr, cl in product(
        [S.Rational(1,4),S.Integer(1),S.Integer(4)],
        [S.Rational(1,2),S.Integer(2)],
        [S.Rational(1,3),S.Integer(3)],
        [S.Integer(1),S.Integer(7)],
        [S.Integer(0),S.Integer(5)]):
    d = 16/kappa
    cr = 2*(1+S.sqrt(d)+d)
    eps = max(S.Integer(1),16*cr*cg/c0)
    delta = min(S.Rational(1,100),c0/(16*cr*cg*eps))
    a0 = max(S.Integer(1),256*cr*kr*delta/c0,512*cl*delta*(1+2*S.sqrt(d))/c0)
    budget = [
        cr*cg*(eps*delta+1/eps),
        cr*32*kr*delta/a0,
        2*2*(16*cl*delta/a0)*(1+2*S.sqrt(d)),
        11*c0/88]
    assert all(term <= c0/8 for term in budget)
    assert c0-sum(budget) >= c0/2
    cases += 1
groups.append({'name':'HN39 four absorption budgets and retained positive half',
               'cases':cases,'scope':'Exact rational parameter grid; geometric outer-patch restrictions remain part of the analytic proof.'})

# The limiting fixed region is strictly inside every nested positive cutoff.
for j in range(12):
    dj = S.Rational(1,2)+S.Rational(1,2**(j+1))
    beta = dj
    # Normalize delta_0=epsilon=1; both boundary values dominate the open region.
    upper_phi = S.Rational(1,16)/dj + S.Rational(1,256)/dj**2
    lower_h = -S.Rational(1,16)/dj + 1+beta
    assert upper_phi < S.Rational(9,64)
    assert lower_h > S.Rational(11,8)
    next_dj = S.Rational(1,2)+S.Rational(1,2**(j+2))
    assert next_dj < dj and S.Rational(1,2) < next_dj
groups.append({'name':'HN42 common positive neighborhood and strict nested radii',
               'cases':12,'scope':'Twelve exact nested stages; the proof supplies the whole sequence.'})

lam = S.symbols('lambda', positive=True)
eye = S.eye(2)
nil = S.Matrix([[0,1],[0,0]])
matrix = eye+nil
reflection = (lam*eye+matrix).inv()*(lam*eye-matrix)
claimed = (lam-1)/(lam+1)*eye-2*lam/(lam+1)**2*nil
assert S.simplify(reflection-claimed) == S.zeros(2)
assert S.simplify(lam*(eye-reflection)-matrix*(eye+reflection)) == S.zeros(2)
inverse = (lam*eye-matrix).inv()*(lam*eye+matrix)
assert S.simplify(reflection*inverse-eye) == S.zeros(2)
assert S.simplify(inverse*reflection-eye) == S.zeros(2)
at_ten = reflection.subs(lam,10)
assert at_ten.T*at_ten != eye
assert S.simplify(reflection.det()-(lam-1)**2/(lam+1)**2) == 0
groups.append({'name':'RE7–RE8 ordered matrix reflection and both inverse identities',
               'cases':6,'scope':'Exact non-Hermitian nilpotent example; nonunitarity does not prevent high-frequency ellipticity.'})

# Figure HN-F2 draws the actual support projection at beta=3/4.
beta = S.Rational(3,4)
for alpha in [S.Rational(k,4) for k in range(-7,8)]:
    height_squared = 1+beta-alpha
    assert 0 <= height_squared < 4 and abs(alpha) <= 2
    assert alpha+height_squared == 1+beta
assert -(1+beta) == S.Rational(-7,4) and -beta == S.Rational(-3,4)
groups.append({'name':'HN-F2 exact exit parabola, envelope and incoming strip',
               'cases':16,'scope':'Fifteen exact support samples and the incoming strip endpoints.'})

result = {'schema':'AN04-weak-normal-finite-models/v1','passed':True,
          'groups':groups,'total_cases':sum(g['cases'] for g in groups),
          'source_sha256':sha(HERE/'weak-hyperbolic-normal-criterion-and-reflection.md'),
          'script_sha256':sha(Path(__file__)),
          'finite_checks_do_not_replace_proofs':True}
(HERE/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
