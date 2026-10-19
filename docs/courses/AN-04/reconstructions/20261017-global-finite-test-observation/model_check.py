"""Finite exact checks supporting the global analytic proof and its examples."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
t0=s.symbols('t0',real=True)
check('Signed characteristic time reaches t=1 in either orientation',all(s.simplify(t0-2*e*(-e*(1-t0)/2)-1)==0 for e in [-1,1]))
check('Exact travel-time endpoints are 5/12 and 2/3',[(1-t0).subs(t0,z)/2 for z in [-s.Rational(1,3),s.Rational(1,6)]]==[s.Rational(2,3),s.Rational(5,12)])
check('The normal travel buffer is strictly positive',s.Rational(3,2)-2*s.Rational(2,3)==s.Rational(1,6))
check('The worst lifted time reaches the circle observation at pi/2',s.simplify(-s.pi-2*(-1)*(s.pi/2))==0)
check('Reflected output at t=0 is exactly 15/4-pi',s.simplify(2-(s.Rational(1,4)+s.pi-2)-(s.Rational(15,4)-s.pi))==0)
t=s.symbols('t',real=True)
check('All six lifted reflection events lie on the alternating boundary',[s.simplify(1-s.Abs(1-s.Mod(s.Rational(1,4)+(-s.pi+m-s.Rational(1,4))+s.pi,2))) for m in range(1,7)]==[1,0,1,0,1,0])
check('Reflected wave slopes retain the characteristic equation',all(s.simplify((2*e)**2-2**2)==0 and s.Rational(2*e,2)==e for e in [-1,1]))
j,k=s.symbols('j k',integer=True,positive=True)
check('Exact square-summable diagonal tail',s.simplify(s.summation(4**(-j),(j,k,s.oo))-4**(1-k)/3)==0)
a,b,c=s.symbols('a b c',real=True)
check('Finite sum-square bound is an exact sum of differences',s.expand(3*(a*a+b*b+c*c)-(a+b+c)**2-((a-b)**2+(a-c)**2+(b-c)**2))==0)
x,xi=s.symbols('x xi',real=True);p=xi*xi-x;lam=1+x*x
H=lambda f:s.Matrix([s.diff(f,xi),-s.diff(f,x)])
check('Positive principal multiplication has the exact Hamilton correction',all(s.simplify(v)==0 for v in H(lam*p)-lam*H(p)-p*H(lam)))
q,V,W=s.symbols('q V W',real=True);qt=q+t*V+t*t*W;rem=s.expand(qt**2-q*q-2*t*q*V)
check('Coordinate witness remainder has zero constant and linear terms',rem.subs(t,0)==0 and s.diff(rem,t).subs(t,0)==0)
check('Exact graph-domain derivative constant is one half',s.integrate(x,(x,0,1))==s.Rational(1,2))
source=HERE/'global-observation-with-full-source-and-observation-tests.md'
out={'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'analytic_proofs_in_lesson':True,'analytic_theorem_proved_by_finite_checks':False}
(HERE/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');print(json.dumps(out))
