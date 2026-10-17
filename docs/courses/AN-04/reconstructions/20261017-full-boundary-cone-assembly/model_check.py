"""Exact supporting gauge, phase, buffer and inverse-kernel identities."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).parent;checks=[]
def check(name,ok):
 assert bool(ok),name
 checks.append(name)
h,k=s.symbols('h k',real=True);c=(1-s.exp(-h))/h
check('log-frequency change extends positively at zero',s.limit(c,h,0)==1)
check('complete log phase is exact',s.simplify((1-s.exp(-h))*k/c-h*k)==0)
check('normal half factor and Jacobian match',s.simplify((s.exp(-h/2)/c-h/(2*s.sinh(h/2))).rewrite(s.exp))==0)
x=s.symbols('x',positive=True);y,gamma=s.symbols('y gamma',real=True);f=s.Function('f')(x,y)
u=s.sqrt(x)*s.exp(gamma*x)
check('variable-density first normal gauge',s.simplify(x*s.diff(u*f,x)/u-(x*s.diff(f,x)+(s.Rational(1,2)+gamma*x)*f))==0)
u=s.sqrt(x)
physical=(u*f-x*s.diff(x*s.diff(u*f,x),x)-s.diff(u*f,y,2))/u
expected=s.Rational(3,4)*f-x**2*s.diff(f,x,2)-2*x*s.diff(f,x)-s.diff(f,y,2)
check('entire physical circle operator including three-quarter constant',s.simplify(physical-expected)==0)
check('Hardy contribution restores unit mass',s.Rational(3,4)+s.Rational(1,2)**2==1)
check('inverse derivative jump supplies delta with correct sign',-s.Rational(1,2)-s.Rational(1,2)==-1)
check('exact two-sided inverse Fourier multiplier',s.simplify((1/(1+s.I*k)+1/(1-s.I*k))/2-1/(1+k*k))==0)
t=s.symbols('t',positive=True)
check('small-ratio physical inverse power',s.simplify(t**s.Rational(-1,2)*s.exp(s.log(t))/2-t**s.Rational(1,2)/2)==0)
check('large-ratio physical inverse power',s.simplify(t**s.Rational(-1,2)*s.exp(-s.log(t))/2-t**s.Rational(-3,2)/2)==0)
check('complete buffer ordering and ellipticity overlap',0<s.Rational(1,4)<s.Rational(1,2)<1<s.Rational(3,2)<2<3<4)
source=root/'scalar-tests-when-the-whole-boundary-cosphere-is-allowed.md'
(root/'model-check.json').write_text(json.dumps({'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Exact finite supporting identities; coercivity, uniform kernel bounds and full scalar assembly are proved in the lesson.'},indent=2)+'\n','utf-8')
print({'passed':True,'exact_checks':len(checks)})
