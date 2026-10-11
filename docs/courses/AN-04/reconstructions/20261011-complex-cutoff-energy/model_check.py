"""Finite exact identities; the analytic operator proofs are in the lesson."""
from pathlib import Path
import hashlib, json
import sympy as S

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'adaptive-square-roots-and-complex-cutoff-energy.md'
s, e, alpha = S.symbols('s e alpha', real=True)
beta = s - S.Rational(1, 2) + 3 * e / 2
checks = []

def identity(name, lhs, rhs):
    assert S.simplify(lhs - rhs) == 0, name
    checks.append({'name': name, 'kind': 'exact_identity', 'passed': True})

identity('weak order', 2 * beta, 2 * s - 1 + 3 * e)
identity('small-root bracket gap', beta - (s-S.Rational(1,2)+e), e/2)
identity('middle/high-root meeting', (1-e)/2-1+2*e, e-(1-e)/2)
identity('maximum bracket exponent', (1-e)/2-1+2*e, beta-s)
identity('mixed remainder one gap', beta-(s-1+2*e), (1-e)/2)
identity('mixed remainder two gap', beta-(s-S.Rational(3,2)+4*e), 1-5*e/2)
identity('joint IMS gap', 2*beta-(2*s-1+2*e), e)
identity('norm IMS gap', 2*beta-(2*s-2+2*e), 1+e)
identity('finite band truncation required loss', 2*s+1-2*beta, 2-3*e)
identity('norm truncation required loss', 2*s-2*beta, 1-3*e)
identity('small root square exponent', 2*alpha+4*(S.Rational(1,2)-alpha)-2, -2*alpha)
identity('large root square exponent', 2*alpha+4*e-2, 2*alpha-2+4*e)
identity('small root double commutator weight', alpha+2*(S.Rational(1,2)-alpha)-1, -alpha)
identity('large root double commutator weight', alpha+2*e-1, alpha-1+2*e)
identity('cross parameter at smallest root', e+S.Rational(1,2)-1, e-S.Rational(1,2))
identity('uniform curvature cutoff scale', (1-2*e)+2*e, 1)
for endpoint in [S.Integer(0), S.Rational(1,4)]:
    for name, exponent in [
        ('square maximum', -1+4*e),
        ('double commutator maximum', -S.Rational(1,2)+2*e),
        ('remainder one excess', -(1-e)/2),
        ('remainder two excess', -1+5*e/2),
        ('small bracket excess', -e/2),
        ('joint IMS excess', -e),
        ('norm IMS excess', -1-e),
    ]:
        value = S.simplify(exponent.subs(e, endpoint))
        assert value <= 0
        checks.append({'name': f'{name} at e={endpoint}', 'kind': 'exact_rational_inequality', 'value': str(value), 'passed': True})
Q, A = S.symbols('Q A', commutative=False)
comm = lambda x,y: x*y-y*x
assert S.expand(Q*A*A-A*A*Q-2*A*comm(Q,A)-comm(comm(Q,A),A)) == 0
checks.append({'name': 'exact double commutator identity', 'kind': 'noncommutative_identity', 'passed': True})
p, T = S.symbols('p T', commutative=False)
assert S.expand(comm(p,comm(T,p))-(2*p*T*p-p*p*T-T*p*p)) == 0
checks.append({'name': 'exact IMS sign', 'kind': 'noncommutative_identity', 'passed': True})
assert len(checks) == 32
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result = {'passed': True, 'source_sha256': sha(SOURCE), 'script_sha256': sha(Path(__file__)), 'total_cases': len(checks), 'exact_algebraic_checks': len(checks), 'numerical_checks': 0, 'checks': checks, 'scope': 'Finite exponent and operator-algebra identities only. The full metric, calculus, localization and energy proofs are written in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(result, indent=2)+'\n', 'utf-8')
print(json.dumps({'passed': True, 'exact_checks': len(checks)}))
