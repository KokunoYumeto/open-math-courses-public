"""Exact algebra supporting the complete analytic collar proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
h,L=s.symbols('h L',real=True)
g=s.exp(-h*h/4)/(2*s.sqrt(s.pi))
check('Exact Gaussian Fourier ODE',s.simplify(s.diff(g,h)+h*g/2)==0)
check('Inverse Gaussian kernel integrates to one',s.integrate(g,(h,-s.oo,s.oo))==1)
check('Every exponential normal weight is absorbed by a Gaussian',s.expand(L*h-h*h/4-(L*L-(h-2*L)**2/4))==0)
z=s.symbols('z',positive=True)
ell=s.symbols('ell',integer=True,positive=True)
check('Two exact outer convolution tails',s.simplify(2*z**2/(1-z**2)-(2/(z**-2-1)))==0)
n=s.symbols('n',real=True)
check('Nearest normal index has sufficient tangential radius',s.expand(4*(1+n*n)-(1+2*n*n+s.Rational(1,2)))==2*n*n+s.Rational(5,2))
F,t,C,c,p=s.symbols('F t C c p',positive=True)
check('Energy-to-norm Young inequality is an exact square',s.simplify(F/2+C*C*t/(2*c*p)-C*s.sqrt(t*F/(c*p))-(s.sqrt(F)-C*s.sqrt(t/(c*p)))**2/2)==0)
x,w=s.symbols('x w',positive=True)
check('Physical input test has x^-1/2 w^-1/2',s.simplify(s.sqrt(x)*s.sqrt(w)/(x*w)-x**s.Rational(-1,2)*w**s.Rational(-1,2))==0)
M,q=s.symbols('M q',integer=True,nonnegative=True)
check('One sufficient far-output exponent leaves half a power',s.simplify((L-s.Rational(1,2)-M-q).subs(L,M+q+1))==s.Rational(1,2))
Q=s.Matrix([[1,0],[0,0]]);S=s.Matrix([[1,t],[t,t*t]]);f=s.Matrix([-s.I*t/(1+s.I),1]);a=(Q+s.I*S)*f
check('Positive rank-one regularizer has eigenvalues zero and 1+t^2',S.det()==0 and S.trace()==1+t*t)
check('Exact cancellation leaves second output of order t^2',all(s.simplify(v)==0 for v in a-s.Matrix([0,s.I*t*t/(1+s.I)])))
check('Norm-domination obstruction has squared ratio t^-2',s.simplify((Q*f).dot(s.conjugate(Q*f))-t*t/2)==0 and s.simplify(a.dot(s.conjugate(a))-t**4/2)==0)
q0,s0=s.symbols('q0 s0',real=True)
check('Commuting positive mode identity retains both squares',s.expand((q0+s.I*s0)*(q0-s.I*s0)-q0*q0-s0*s0)==0)
source=HERE/'scalar-collar-tests-with-all-tangential-directions-allowed.md'
j={'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'analytic_proofs_in_lesson':True,'analytic_theorem_proved_by_finite_checks':False}
(HERE/'model-check.json').write_text(json.dumps(j,indent=2)+'\n','utf-8');print(json.dumps(j))
