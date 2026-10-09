"""Exact checks of orders, compressed strip coordinates and the norm mechanism."""
from pathlib import Path
import hashlib,json
import sympy as s
P=Path(__file__).resolve().parent
checks=[]
def eq(name,a,b):
 assert s.simplify(a-b)==0,(name,a,b)
 checks.append(name)
for n in range(2,9):
 d=n-1;k=n-2;order=n+4;g=order+s.Rational(n,4)
 eq(f'critical-exponent-n{n}',2*order-2*g+s.Rational(k,2),-1)
 eq(f'lower-exponent-n{n}',2*(order-1)-2*g+s.Rational(k,2),-3)
 eq(f'solution-kernel-order-n{n}',s.Rational(d,2)-s.Rational(n+d,4),-s.Rational(1,4))
 eq(f'section-graph-order-n{n}',-s.Rational(1,4)+s.Rational(1,4),0)
 assert order-1>s.Rational(n,2);checks.append(f'continuous-order-margin-n{n}')
t,h=s.symbols('t h',real=True)
curves=[s.Rational(1,2)+h+t,s.Rational(3,2)-h-t,t-s.Rational(3,2)+h,s.Rational(7,2)-h-t]
momenta=[-1,1,-1,1]
for j,(r,rho) in enumerate(zip(curves,momenta)):
 eq(f'characteristic-branch-{j}',rho**2-1,0)
 eq(f'physical-slope-branch-{j}',s.diff(r,t),-rho)
 eq(f'Hamilton-parameter-branch-{j}',-2*s.diff(r,t),2*rho)
 eq(f'compressed-polynomial-degree-{j}',s.diff(r*(1-r)*rho,t,3),0)
for j,hit in enumerate([s.Rational(1,2)-h,s.Rational(3,2)-h,s.Rational(5,2)-h]):
 eq(f'position-continuity-hit-{j}',curves[j].subs(t,hit),curves[j+1].subs(t,hit))
 eq(f'wall-value-hit-{j}',curves[j].subs(t,hit),1 if j%2==0 else 0)
 for side in [j,j+1]:
  r=curves[side];eq(f'compressed-zero-hit-{j}-side-{side}',(r*(1-r)*momenta[side]).subs(t,hit),0)
eq('initial-interior-position',curves[0].subs(t,0),s.Rational(1,2)+h)
eq('final-interior-position',curves[-1].subs(t,3),s.Rational(1,2)-h)
r0,r1=s.symbols('r0 r1')
eq('same-branch-difference',r1*(1-r1)-r0*(1-r0),(r1-r0)*(1-r1-r0))
lam=s.symbols('lambda',positive=True)
eq('lower-norm-integral',s.integrate(lam**-3,(lam,2,s.oo)),s.Rational(1,8))
eps=s.symbols('epsilon',positive=True)
eq('critical-log-integral',s.integrate(lam**-1,(lam,2,1/(2*eps))),s.log(1/(4*eps)))
m,delta,q=s.symbols('m delta q',positive=True)
eq('strict-neighborhood-scale',q*delta/(2*q),delta/2)
eq('Baire-homogeneity-constant',2*m*2*q/delta,4*m*q/delta)
for h0 in [s.Rational(0),s.Rational(1,8),s.Rational(1,32),s.Rational(1,128)]:
 assert 0<s.Rational(1,2)-h0<=s.Rational(1,2)+h0<1
 checks.append('figure-interior-endpoints-'+str(h0))
source=P/'distributions-on-limiting-broken-rays.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'cases':checks,
 'scope':'Exact profile exponents, solution and section orders, Hamilton signs, all compressed reflection joins, endpoint coordinates and the Baire/norm mechanism. Finite checks do not replace the functional-analytic or microlocal proofs.'}
(P/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
