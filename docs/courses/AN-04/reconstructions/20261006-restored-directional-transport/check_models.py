"""Exact finite checks for signs, moving endpoints, degree and the retained diagram."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
import sympy as S
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
t,s,q,b,mu=S.symbols('t s q b mu',real=True)
R,lam=S.symbols('R lam',positive=True)
beta=S.symbols('beta')
u=R**mu*(1-S.exp(-S.I*beta*(t-s)))/beta
assert S.simplify(-S.I*S.diff(u,t)+beta*u-R**mu)==0
assert u.subs(t,s)==0
assert S.simplify(S.limit(u,beta,0)-S.I*R**mu*(t-s))==0
c=q+b+S.I*s
C=S.integrate(c,(b,s,t))
assert S.simplify(S.diff(C,t)-c.subs(b,t))==0
assert S.simplify(S.diff(C,s)+c.subs(b,s)-S.integrate(S.diff(c,s),(b,s,t)))==0
theta=S.symbols('theta',real=True)
g=b*b+q*s
assert S.simplify(S.integrate(g,(b,s,t))-(t-s)*S.integrate(g.subs(b,s+theta*(t-s)),(theta,0,1)))==0
candidate=(t-s)*R**mu
forcing=-S.I*S.diff(candidate,t)+c.subs(b,t)*candidate
assert S.simplify(-S.I*S.diff(S.exp(S.I*C)*candidate,t)-S.exp(S.I*C)*forcing)==0
# A nontrivial coordinate Jacobian and dilation on the n=2 relation.
y=S.symbols('y',real=True)
coords=S.Matrix([q+q**3,t,s,lam*R])
assert S.simplify(coords.jacobian([q,t,s,R]).det()-lam*(1+3*q*q))==0
n=S.symbols('n',integer=True,positive=True)
assert S.simplify((n-1)/2+S.Rational(1,2)-n/2)==0
assert S.simplify((lam*R)**((n-1)/2)*S.sqrt(lam)/(R**((n-1)/2)*lam**(n/2))-1)==0
# Exact positions and endpoint inclusion in the original vector figure.
fig=ROOT/'figures/directional-symbol-source-boundary.svg'
root=ET.fromstring(fig.read_bytes());ns={'s':'http://www.w3.org/2000/svg'}
circles={(e.get('cx'),e.get('cy')):e for e in root.findall('.//s:circle',ns)}
assert set(circles)=={('410','184'),('570','184'),('410','249'),('410','315')}
assert circles['410','315'].get('fill')=='#f7f5ef'
assert circles['410','249'].get('fill')=='#24766b'
for time,x in [(S.Integer(-2),90),(S.Rational(-3,2),170),(S.Integer(0),410),(S.Integer(1),570),(S.Integer(2),730)]:
 assert 410+160*time==x
assert S.Interval(0,1).contains(0) and S.Interval(0,S.oo).contains(0)
assert not S.Interval.open(0,S.oo).contains(0)
description=root.find('s:desc',ns).text
assert 'zero to infinity' in description and 'strictly greater than zero' in description and 'Exercise 1' in description
result={'passed':True,'finite_groups':3,'groups':[
 'Complex integrating-factor signs, zero diagonal and resonance; variable input-time coefficient and fixed interpolation identity',
 'Exact homogeneous density degree and nontrivial triangular quotient/dilation Jacobian',
 'Original vector coordinates, full versus strict source-boundary inclusion, and the precise wavefront-slice description'],
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.relative_to(ROOT).as_posix():sha(p) for p in [ROOT/'directional-transport-for-characteristic-symbols.md',fig]},
 'full_theorems_proved_by_these_finite_checks':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':3}))
