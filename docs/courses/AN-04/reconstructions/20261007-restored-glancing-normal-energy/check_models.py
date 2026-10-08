"""Check signs and constants in the explicit models, supplementary to full proofs."""
from pathlib import Path
import datetime
import hashlib
import json
import sympy as s

root = Path(__file__).resolve().parent
x, k = s.symbols('x k', real=True)
a, f, chi = (s.Function(v)(x) for v in ('a', 'f', 'chi'))
# The divergence-form normal operator retains a' and both cutoff derivatives.
normal = s.diff(a * s.diff(chi * f, x), x) - chi * s.diff(a * s.diff(f, x), x)
expected = a * s.diff(chi, x, 2) * f + 2 * a * s.diff(chi, x) * s.diff(f, x) + s.diff(a, x) * s.diff(chi, x) * f
assert s.simplify(normal - expected) == 0
packet = s.diff(chi * s.sin(k*x), x, 2) + k**2 * chi * s.sin(k*x)
assert s.simplify(packet - (s.diff(chi,x,2)*s.sin(k*x) + 2*k*s.diff(chi,x)*s.cos(k*x))) == 0
eps, delta, a0, b0, C, M, beta = s.symbols('eps delta a0 b0 C M beta', positive=True)
theta = eps*delta + 2*C*eps*delta/b0
K = (2+2*C/b0)/a0
assert s.simplify((theta+eps*delta)/a0 - K*eps*delta) == 0
assert s.simplify((2*M**2/(beta**2*eps**2))*(1/(4*a0*eps*delta)) - M**2/(2*a0*beta**2*eps**3*delta)) == 0
assert s.simplify((1/(2*eps**3*delta)).subs(eps,s.sqrt(delta)) - s.Rational(1,2)*delta**(-s.Rational(5,2))) == 0
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
record = {'schema': 'an04-glancing-normal-energy-finite-models/v1',
          'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source_sha256': sha(root/'glancing-normal-energy-model.md'),
          'script_sha256': sha(Path(__file__)),
          'groups': ['Full divergence-form cutoff commutator, including coefficient derivative',
                     'Exact standing-wave packet source and cancellation',
                     'Normal-energy and absorption source constants',
                     'Exercise source power under compatible shrinking widths'],
          'passed': True, 'general_lemma_proof_by_finite_tests_claimed': False,
          'full_boundary_propagation_proved': False}
(root/'model-check.json').write_text(
    json.dumps(record, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
print({'passed': True, 'finite_groups': len(record['groups']), 'full_boundary_propagation': False})
