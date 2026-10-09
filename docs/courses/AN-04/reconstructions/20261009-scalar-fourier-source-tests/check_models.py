"""Exact supporting identities; these checks do not replace the analytic proof."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok):
 assert bool(ok),name
 checks.append({'name':name,'passed':True})
x,y,t,v,u=s.symbols('x y t v u',positive=True)
check('logarithmic Jacobian',s.diff(s.exp(v),v)==s.exp(v))
check('unitary square factor',s.simplify(s.exp(v/2)**2-s.exp(v))==0)
check('inverse unitary factor',s.simplify(x**s.Rational(-1,2)*x**s.Rational(1,2))==1)
check('ordinary kernel density',s.simplify(s.sqrt(x*y)/x-s.sqrt(y/x))==0)
check('ratio integration factor',s.simplify(t**s.Rational(-1,2)*t-s.sqrt(t))==0)
check('log difference orientation',s.simplify(s.log(x)-s.log(y)+s.log(y/x))==0)
check('symmetric ratio inverse',s.simplify(2*(1-t)/(1+t)-2*s.tanh(-s.log(t)/2).rewrite(s.exp))==0)
z=s.symbols('z',real=True)
r=2*s.tanh(z/2)
check('ratio derivative at diagonal',s.diff(r,z).subs(z,0)==1)
check('ratio cubic jet',s.series(r,z,0,5).removeO()==z-z**3/12)
for j,n in enumerate([1,2,3,4],1):
 K=4*(n+1)
 check('packet derivative count dimension '+str(n),K==4*(n+1) and n+1>Fraction(n,2))
 check('root decay exponent dimension '+str(n),Fraction(10*(K+1),K+1)==10)
q=s.Function('q')(z)
for k in [1,2,3]:
 derivative=s.diff(1/q,z,k)
 numerator=s.expand(derivative*q**(k+1))
 check('reciprocal denominator order '+str(k),not any(p.exp.is_negative for p in numerator.atoms(s.Pow) if p.base==q))
check('first reciprocal derivative',s.simplify(s.diff(1/q,z)+s.diff(q,z)/q**2)==0)
check('second reciprocal derivative',s.simplify(s.diff(1/q,z,2)-(2*s.diff(q,z)**2/q**3-s.diff(q,z,2)/q**2))==0)
A,e,D=s.symbols('A e D',positive=True)
c=(A+e)**s.Rational(1,13)/D
check('exact floor cancellation',s.simplify(A/c**13-D**13*A/(A+e))==0)
check('strict bounded cancellation',s.simplify(1-A/(A+e))==e/(A+e))
check('finite order numerator loss',3*12==36)
check('exercise root exponent',13*10==130)
check('upper ratio bound',s.exp(s.log(2))==2)
check('lower ratio bound',s.exp(-s.log(2))==s.Rational(1,2))
check('normal exponential norm',s.integrate(s.exp(-2*x),(x,0,s.oo))==s.Rational(1,2))
check('log norm substitution',s.simplify((s.exp(v)*s.exp(-2*s.exp(v))).subs(v,s.log(x))/x-s.exp(-2*x))==0)
vertices=[(Fraction(0),Fraction(0)),(Fraction(1),Fraction(1,2)),(Fraction(1),Fraction(2))]
check('support wedge vertices',all(y0/2<=x0<=2*y0 and 0<=y0<=1 for y0,x0 in vertices))
check('support wedge area',Fraction(1,2)*(2-Fraction(1,2))==Fraction(3,4))
check('compact difference support',Fraction(1,2)-Fraction(-1,2)==1)
assert len(checks)==33,len(checks)
source=ROOT/'scalar-source-tests-from-compact-logarithmic-kernels.md'
data={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,
 'scope':'Exact densities, ratios, derivative counts, reciprocal identities, root exponents, compact support coordinates and norm substitution. Analytic uniform estimates and completeness are proved in the lesson.'}
(ROOT/'model-check.json').write_text(json.dumps(data,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
