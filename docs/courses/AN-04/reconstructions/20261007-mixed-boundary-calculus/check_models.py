"""Finite algebra/geometry checks for the original CC0 receiving companion.

These checks do not certify the general analytic theorems.
Run python -B check_models.py from any directory; SymPy is required.
"""
from pathlib import Path
import hashlib
import json
import sympy as S

HERE = Path(__file__).resolve().parent
checks = []
s, t = S.symbols('s t', real=True)
P = S.Matrix([[2, 1], [0, 1]])
B = S.Matrix([[0, 0], [1, 0]])
C = S.Matrix([[1, 2], [3, -1]])
M = P.inv()
family = (P+s*B+t*C).inv()
at0 = lambda a: a.subs({s: 0, t: 0}).applyfunc(S.simplify)
assert at0(family.diff(s)) == -M*B*M
assert at0(family.diff(s,t)) == M*B*M*C*M+M*C*M*B*M
assert -M*B*M != -M*M*B
assert -M*B*M == S.Matrix([[S.Rational(1,4),-S.Rational(1,4)],[-S.Rational(1,2),S.Rational(1,2)]])
checks.append({'id':'ordered-inverse', 'first_and_mixed_second_derivatives':True})

eta, kappa, y, r = S.symbols('eta kappa y r', real=True)
a = eta/S.sqrt(1+eta**2)
err = S.exp(S.I*y)*(a.subs(eta,eta+1)-a)
assert S.simplify(err.subs(eta,0)-S.exp(S.I*y)/S.sqrt(2)) == 0
assert S.diff(err,kappa) == 0
assert S.simplify((kappa+1)*S.exp(S.I*r)-kappa*S.exp(S.I*r)) == S.exp(S.I*r)
assert S.simplify(-S.I*S.diff(S.exp(S.I*r),r)) == S.exp(S.I*r)
checks.append({'id':'exact-fourier-shifts', 'normal_sign':True, 'tangential_error_independent_of_normal_frequency':True})

u,v,tau = S.symbols('u v tau', real=True)
plane = S.exp(S.I*(u*y+v*eta))
generator = -S.I*S.diff(plane,y,eta)
assert S.simplify(generator-S.I*u*v*plane)==0
assert S.simplify(S.diff(S.exp(S.I*tau*u*v)*plane,tau)-S.exp(S.I*tau*u*v)*generator)==0
checks.append({'id':'gauss-generator-sign', 'exact_plane_wave_identity':True})

for T,R in [(S.Integer(1),S.Integer(9)),(S.Integer(9),S.Integer(9))]:
    assert T<=R
    for j in range(361):
        angle=2*S.pi*S.Rational(j,360)
        # The parametrization proves the entire ellipse identity exactly;
        # these samples additionally check the coordinates sent to the SVG.
        xx=float(T*S.cos(angle)); yy=float(R*S.sin(angle))
        assert abs(xx*xx/float(T*T)+yy*yy/float(R*R)-1)<1e-12
assert S.Rational(1,9)<1
checks.append({'id':'metric-ellipses', 'samples':722, 'semiaxes':[[1,9],[9,9]], 'unit_metric_residual_bound':1e-12})

source=HERE/'mixed-boundary-calculus.md'
result={'schema':'AN04-mixed-boundary-calculus-models/v1',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks':checks,'passed':True,'general_theorem_certified':False}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks),'ellipse_samples':722}))
