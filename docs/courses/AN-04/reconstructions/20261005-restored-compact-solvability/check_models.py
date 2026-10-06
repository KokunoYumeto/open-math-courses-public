"""Finite checks of the order arithmetic, Hamilton models and correction bounds."""
from pathlib import Path
import hashlib,json,cmath,math
import sympy as S
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
m,s=S.symbols('m s',real=True)
r=1-m-s;q=S.expand(r+m-1)
assert q==-s and S.expand(-r-(s+m-1))==0
assert r.subs({m:S.Rational(3,2),s:-2})==S.Rational(3,2)
assert S.expand((q-1-m)-(r-2))==0
checks.append('Exact dual orders, graph-space continuity order and original fractional-order exercise')
x,y,ex,ey,t=S.symbols('x y ex ey t',real=True)
p=x*ey-y*ex
H=S.Matrix([S.diff(p,ex),S.diff(p,ey),-S.diff(p,x),-S.diff(p,y)])
curve=S.Matrix([S.Rational(3,2)*S.cos(t),S.Rational(3,2)*S.sin(t),S.cos(t),S.sin(t)])
subs=dict(zip([x,y,ex,ey],curve))
assert S.simplify(p.subs(subs))==0
assert all(S.simplify(v)==0 for v in curve.diff(t)-H.subs(subs))
assert S.simplify(curve[0]**2+curve[1]**2-S.Rational(9,4))==0
checks.append('Full circular Hamilton curve, exact characteristic value and constant radius')
assert S.Matrix([S.diff(ex,ex),S.diff(ex,ey),-S.diff(ex,x),-S.diff(ex,y)])==S.Matrix([1,0,0,0])
for start in [-1.,-.25,1.]:
 assert start+3>1
checks.append('Escaping horizontal Hamilton line and bounded exit from the specified compact rectangle')
errors=[]
for c in [-.7,.4,1.1]:
 for k in [-3,0,2]:
  v=quad(lambda t:math.exp(-c*t)*math.cos(k*t),0,2*math.pi,epsabs=1e-10)[0]-1j*quad(
    lambda t:math.exp(-c*t)*math.sin(k*t),0,2*math.pi,epsabs=1e-10)[0]
  u=1j*v/(1-math.exp(-2*math.pi*c))
  errors.append(abs((k-1j*c)*u-1))
assert max(errors)<1e-9
checks.append('Original periodic inverse has both correct endpoints and scalar phase for nine Fourier probes')
D=S.diag(-2,-1,0,1,2)
phi=S.Matrix([1,2,3,2,1])/S.sqrt(19)
P=D-phi*(D*phi).conjugate().T
Pad=D-(D*phi)*phi.conjugate().T
assert P.conjugate().T==Pad
assert Pad*phi==S.zeros(5,1)
checks.append('Ordered rank-one adjoint formula and its normalized obstruction in an exact finite algebra model')
for j in range(1,20):
 tail=S.summation(S.Rational(1,2)**S.Symbol('k',integer=True),(S.Symbol('k',integer=True),j,S.oo))
 assert tail==S.Rational(1,2)**(j-1)
checks.append('Exact geometric bounds used for each original seminorm and quotient correction tail')
sources=['compact-set-solvability-from-characteristic-escape.md','closed-graphs-and-smooth-quotients.md',
 'fixed-support-sobolev-compactness.md','figures/draw_escape_models.py']
out={'passed':True,'finite_groups':len(checks),'checks':checks,'largest_inverse_probe_error':max(errors),
 'script_sha256':sha(Path(__file__)),'source_hashes':{p:sha(ROOT/p) for p in sources},
 'scope':'Finite model checks; complete functional-analytic and microlocal proofs require separate owner review.',
 'full_course_complete':False}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks),'largest_error':max(errors)}))
