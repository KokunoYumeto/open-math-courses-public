"""Finite exact checks; the full general arguments remain in the lesson."""
from pathlib import Path
import hashlib,json,runpy
import sympy as S
import numpy as np
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=S.symbols('d',integer=True,positive=True)
r=S.symbols('r',real=True);j,J=S.symbols('j J',integer=True,nonnegative=True)
assert S.simplify((2*S.pi)**(d/4)*(2*S.pi)**(-d)-(2*S.pi)**(-3*d/4))==0
assert S.simplify(r-d/4+d/2-d/4-r)==0
assert S.simplify((r-(J+2)+1)-(r-J-1))==0
# Actual ordinary nonhomogeneous coefficient and removable time solution.
R=S.symbols('R',positive=True);t,s,beta=S.symbols('t s beta',real=True)
c=S.sin(S.log(R));u=R**r*(1-S.exp(-S.I*beta*(t-s)))/beta
assert S.simplify(-S.I*S.diff(u,t)+beta*u-R**r)==0
assert S.simplify(S.limit(u,beta,0)-S.I*R**r*(t-s))==0
poly=S.sin(S.log(R))
for k in range(1,7):
 poly=S.simplify(R*S.diff(poly,R)-(k-1)*poly)
 assert S.simplify(R**k*S.diff(c,R,k)-poly)==0
 assert not poly.has(R**-1)
# The explicit compact bump used for the mathematical figure.
f=runpy.run_path(str(ROOT/'figures/draw_annular_bumps.py'))
v=np.array([1,9/8,5/4,3/2,7/4,15/8,2])
assert np.array_equal(f['bump'](v),np.array([0,0,1,1,1,0,0]))
grid=f['bump'](np.linspace(1,2,2001));assert np.all(grid>=0) and np.all(grid<=1)
for k in range(1,5):
 lo=S.Rational(9,8)*4**k;hi=S.Rational(15,8)*4**k;center=S.Rational(3,2)*4**k
 assert 4**k<lo<center<hi<2*4**k
 assert hi<S.Rational(9,8)*4**(k+1)
 assert S.Rational(5,4)*4**k<center<S.Rational(7,4)*4**k
result={'passed':True,'finite_groups':3,'groups':[
 'Exact graph normalization, coefficient/distribution order and the first summable remainder order',
 'Ordinary coefficient radial recursion through six derivatives, exact complex transport and removable resonant value',
 'Explicit plotted bump, exact plateau and support endpoints, disjoint annuli and unit-height sample frequencies'],
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.relative_to(ROOT).as_posix():sha(p) for p in [
 ROOT/'global-kernel-corrections-from-directional-symbols.md',ROOT/'figures/draw_annular_bumps.py',
 ROOT/'figures/annular-bumps.svg',ROOT/'figures/annular-bumps.png']},
 'full_theorems_proved_by_these_finite_checks':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':3}))
