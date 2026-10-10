"""Exact identities supporting the reflection proof; analytic estimates are in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent
x=s.symbols('x',positive=True);z=s.symbols('z',real=True)
c,k,nu=s.symbols('c k nu')
u=s.Function('u')(x,z);h=s.Function('h')(x,z)
D=lambda f:-s.I*s.diff(f,x)
Z=lambda f:-s.I*s.diff(f,z)
Q=lambda f:x*D(f)
P=lambda f:D(D(f))-c*c*Z(Z(f))
checks=[]
def check(name,expression):
    value=s.simplify(s.expand(expression))
    assert value==0,(name,value)
    checks.append(name)
check('full quadratic compressed generator',x*x*D(D(u))-Q(Q(u))-s.I*Q(u))
check('Theta Q on the actual weight',Q(x*u)/x-Q(u)+s.I*u)
check('Theta squared Q on the actual weight',Q(x*x*u)/(x*x)-Q(u)+2*s.I*u)
check('inverse Theta Q',x*Q(u/x)-Q(u)-s.I*u)
check('normal derivative moved outside Q',Q(D(u))-D(Q(u)+s.I*u))
check('normal derivative moved outside Q squared',Q(Q(D(u)))-D(Q(Q(u))+2*s.I*Q(u)-u))
check('exact model commutator',P(Q(u))-(Q(P(u))-2*s.I*P(u))+2*s.I*c*c*Z(Z(u)))
power=x**nu*s.exp(s.I*k*z)
check('power equation',P(power)-(-nu*(nu-1)*x**(nu-2)-c*c*k*k*x**nu)*s.exp(s.I*k*z))
check('power commutator',P(Q(power))-(Q(P(power))-2*s.I*P(power))+2*s.I*c*c*k*k*power)
cv=s.Function('a')(x,z);b=s.Function('b')(x,z);d=s.Function('d')(x,z)
B=lambda f:-4*Z(Z(f))+b*Z(f)+d*f
Pv=lambda f:D(D(f))+cv*D(f)+B(f)
V=lambda f:-2*s.I*s.diff(h,x)*f
W=lambda f:-s.diff(h,x,2)*f-s.I*cv*s.diff(h,x)*f+B(h*f)-h*B(f)
check('variable coefficient full cutoff commutator',Pv(h*u)-h*Pv(u)-V(D(u))-W(u))
check('normal input derivative for variable multiplier',h*D(u)-D(h*u)-s.I*s.diff(h,x)*u)
check('tangential differential commutes with normal derivative',D(u-s.diff(u,z,2))-D(u)+s.diff(D(u),z,2))
q=s.symbols('q',nonzero=True)
check('exact compressed symbol ratio',(q*q-4*x*x)/(q*q)-(1-4*x*x/q**2))
for edge in [s.Rational(1,2),-s.Rational(1,2)]:
    check('transition lower bound '+str(edge),1-4*s.Rational(1,8)**2/edge**2-s.Rational(3,4))
for sign in [-1,1]:
    check('characteristic coordinate '+str(sign),(sign*2*x)**2-4*x*x)
    check('outer characteristic at end '+str(sign),sign*2*s.Rational(1,8)-sign*s.Rational(1,4))
for n in [2,3]:
    K=2*n+4
    check('coarse exponent '+str(n),2-K-(-2*n-2))
    check('normal coarse exponent '+str(n),1-K-(-2*n-3))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'numerical_checks':0,'checks':checks,'source_sha256':sha(r/'reflection-with-admissible-source-and-observation-tests.md'),
        'script_sha256':sha(Path(__file__)),
        'scope':'Actual normal conjugation, derivative relocation, variable-coefficient cutoff commutator, power example, coarse exponents and exact transition geometry. Full operator bounds, support assertions and graph completion are proved in the lesson.'}
(r/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
