"""Exact finite model checks supplementary to the written general proof."""
from pathlib import Path
import datetime,hashlib,json
import sympy as s
r=Path(__file__).resolve().parents[1];c=r/'courses/AN-04'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
rho,a,l,b=s.symbols('rho a l b',real=True,nonzero=True)
p=a*rho**2+2*l*rho+b
ref=-rho-2*l/a
assert s.simplify(p.subs(rho,ref)-p)==0
assert s.simplify(ref.subs(rho,ref)-rho)==0
assert s.simplify((a*rho+l).subs(rho,ref)+(a*rho+l))==0
checks=[{'model':'Full mixed quadratic normal reflection','passed':True,
         'identities':['principal square preserved','involution','normal Hamilton velocity reversed']}]
G=s.Matrix([[2,1],[1,3]]);K=s.Rational(5,2)
tau,eta=s.symbols('tau eta',real=True)
wave=2*rho**2+2*rho*eta+3*eta**2-tau**2
assert s.expand(wave-(2*(rho+eta/2)**2-(tau**2-K*eta**2)))==0
assert s.expand(wave.subs(rho,-rho-eta)-wave)==0
for tv,ev in [(2,1),(3,-1),(1,0)]:
    A=s.Rational(tv)**2-K*s.Rational(ev)**2
    assert A>0
    for sign in [-1,1]:
        root=-s.Rational(ev,2)+sign*s.sqrt(A/2)
        assert s.simplify(wave.subs({rho:root,tau:tv,eta:ev}))==0
checks.append({'model':'Positive anisotropic metric and exact roots','matrix':str(G),'hyperbolic_samples':3,'passed':True})
t,rr=s.symbols('t rr',real=True)
minus=s.Function('F')(t-rr);plus=s.Function('F')(t+rr)
for term in [minus,plus]:
    assert s.simplify(-s.diff(term,rr,2)+s.diff(term,t,2))==0
normal=s.simplify((-s.I*s.diff(minus-plus,rr)).subs(rr,0))
assert normal==2*s.I*s.Subs(s.Derivative(s.Function('F')(t),t),t,t).doit()
checks.append({'model':'Dirichlet difference and intrinsic normal trace','normal_trace':'2 i F-prime','passed':True,
               'distributional_validity':'The smooth derivative identity extends to arbitrary one-variable distributions by pullback along a submersion.'})
freq=s.symbols('freq',positive=True)
u=s.exp(-rr*freq)
assert s.simplify(-s.diff(u,rr,2)+freq**2*u)==0
assert u.subs(rr,0)==1
checks.append({'model':'Decaying elliptic normal mode','passed':True,'dirichlet_value':1})
L,initial=s.symbols('L initial',positive=True)
times=[L-initial,2*L-initial,3*L-initial]
pieces=[initial+t,L-(t-times[0]),t-times[1]]
assert s.simplify(pieces[0].subs(t,times[0])-L)==0
assert s.simplify(pieces[1].subs(t,times[1]))==0
assert s.simplify(pieces[2].subs(t,times[2])-L)==0
assert [s.diff(v,t) for v in pieces]==[1,-1,1]
checks.append({'model':'Three transverse strip reflections','passed':True,'times':[str(v) for v in times]})

import sympy as S
x = S.symbols('x0:3')
xi = S.symbols('xi0:3')
X = S.symbols('X0:3')
Xi = S.symbols('Xi0:3')
p = sum(S.Function(f'g{j}{k}')(*x)*xi[j]*xi[k]
        for j in range(3) for k in range(j,3))
lhs = -sum(S.diff(p,x[k])*X[k] for k in range(3))/2
lhs += sum(xi[j]*(S.diff(p,xi[j],x[k])*X[k] +
                       S.diff(p,xi[j],xi[k])*Xi[k])
           for j in range(3) for k in range(3))/2
rhs = sum(S.diff(p,x[k])*X[k]+S.diff(p,xi[k])*Xi[k] for k in range(3))/2
assert S.expand(lhs-rhs) == 0
assert S.expand(sum(xi[k]*S.diff(p,xi[k]) for k in range(3))/2-p) == 0
checks.append({'model':'Canonical pairing for a general variable quadratic in three covariables',
               'passed':True,'coefficient_functions':6,
               'checks':['d_s(xi dot X)=one-half directional derivative of p',
                         'theta(H_p/2)=p'],
               'scope':'Exact polynomial identities; smooth flow and inverse-function hypotheses remain in the written proof.'})

r = S.symbols('r',real=True)
A = S.Matrix([[r,r**2],[1-r,2*r]])
C = S.Matrix([[1,r],[r**2,-2]])
B = S.Matrix([[r,2],[3,1-r]])
u = S.Matrix([S.Function('u')(r),S.Function('v')(r)])
D = lambda v: -S.I*v.diff(r)
left = lambda v: D(v)-(-C-A)*v
right = lambda v: D(v)-A*v
actual = D(D(u))+C*D(u)+B*u-left(right(u))
predicted = (B-S.I*A.diff(r)+C*A+A*A)*u
assert all(S.expand(t)==0 for t in actual-predicted)
reversal = left(right(u))-right(left(u))
assert any(S.expand(t)!=0 for t in reversal)
checks.append({'model':'Variable noncommuting coefficients in ordered normal factors',
               'passed':True,'checks':['Full derivative term and multiplication order',
                                      'Every normal derivative of the input cancels in the remainder',
                                      'Uncorrected reversal changes the full product'],
               'scope':'Finite matrix model supplementary to the full symbol proof.'})


from datetime import datetime, timezone
source = Path(__file__).resolve().parent/'boundary-reflection-preparation.md'
result = {'recorded_utc':datetime.now(timezone.utc).isoformat(),
          'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
          'checks':checks,'finite_groups':len(checks),'passed':True,
          'finite_checks_do_not_replace_complete_proofs':True}
(source.parent/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'finite_groups':len(checks),'passed':True}))
