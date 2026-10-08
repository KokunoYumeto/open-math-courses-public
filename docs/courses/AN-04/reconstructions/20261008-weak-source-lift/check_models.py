"""Exact finite checks; these supplement, and do not replace, the proofs."""
from pathlib import Path
import hashlib, json
import sympy as S

ROOT = Path(__file__).resolve().parent
groups = []
def group(name, count): groups.append({'name': name, 'cases': count, 'passed': True})

for L in range(6):
    for d in range(6):
        b = S.Rational(d + 1, 7)
        mu = 1 + S.Rational(L*L, 2)
        gap = S.expand(d*d + mu*b*b - L*d*b - (S.Rational(1,2)*d*d+b*b))
        assert gap == (d-L*b)**2/2 and gap >= 0
group('Coercivity square and exact mass choice', 36)

I = S.I
pair = lambda v,w: (w.conjugate().T*v)[0]
for k in range(1,25):
    w=S.Matrix([1+I*k,2-k]); phi=S.Matrix([k-I,1+I])
    dx=S.Matrix([k,I]); dz=S.Matrix([I*k,1]); px=S.Matrix([1,I*k]); pz=S.Matrix([k+1,I])
    l=S.Matrix([[I,k],[-1,2-I]]); m=S.Matrix([[I,1],[0,-2]]); c=S.Matrix([[k,1+I],[I,-k]])
    lower=pair(l*dx,phi)+pair(l*dz,phi)+pair(m*w,px)+pair(m*w,pz)+pair(c*w,phi)
    h=S.Rational(2-k,3); mu=k+2
    q=pair(dx,px)+h*pair(dz,pz)+lower
    a=pair(dx,px)+pair(dz,pz)+lower+mu*pair(w,phi)
    assert S.simplify(a-q-((1-h)*pair(dz,pz)+mu*pair(w,phi)))==0
group('Full complex matrix form cancellation on arbitrary jets',24)

x=S.symbols('x',nonnegative=True); w=S.exp(-x); u=-x; v=u-w
assert S.simplify(-S.diff(w,x,2)+w)==0
assert -S.diff(w,x).subs(x,0)==1
assert S.simplify(-S.diff(v,x,2)-w)==0
assert S.diff(v,x).subs(x,0)==0
group('Boundary lift and reduced local equation',4)

m=S.Matrix([[I,1],[0,-2]]); n=m*S.Matrix([1,1])
assert n==S.Matrix([1+I,-2])
assert (I*n-S.Matrix([-1+I,-2*I])).applyfunc(S.simplify)==S.zeros(2,1)
group('Retained complex flux boundary coefficient',2)

for k in range(1,65):
    n2=S.Rational(1,2); dn2=S.Rational(k*k,2*(1+k*k)); trace=S.Rational(k,1)/S.sqrt(1+k*k)
    assert S.simplify(trace**2-4*n2*dn2)==0
    assert trace<1 and dn2<S.Rational(1,2)
group('Sharp negative-half trace and bounded graph norms',64)

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'groups':groups,'total_cases':sum(g['cases'] for g in groups),
    'source_sha256':sha(ROOT/'weak-source-lifting-and-normal-flux.md'),
    'script_sha256':sha(Path(__file__)),'finite_checks_do_not_replace_proofs':True}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
