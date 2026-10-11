"""Exact identities for the local sign estimate and complex phase; no operator-positivity certification."""
from pathlib import Path
import sympy as s
import json,hashlib
root=Path(__file__).resolve().parent
e,m,k=s.symbols('e m k',real=True);R=s.symbols('R',positive=True);beta=m+(3*e-1)/2
a,b,af,bf=s.symbols('a b bracket_a bracket_b',real=True)
cases=[]
def check(name,left,right=0):
 diff=s.simplify(s.expand(left-right));ok=diff==0;cases.append(dict(name=name,passed=ok,kind='exact symbolic identity'));assert ok,(name,diff)
check('complex phase identity',s.re(-s.I*(a-s.I*b)*(af+s.I*bf)),a*bf-b*af)
check('first bracket exponent',m-1+e+(1+e)/2,beta)
check('second bracket exponent',m+e+(-1+e)/2,beta)
check('switching scale squared-gradient quotient',2-(1-e),1+e)
check('Taylor finite-radius quotient at switch',(1-e)+2*e,1+e)
check('weak quadratic order',2*beta,2*m-1+3*e)
check('mixed commutator error',m+1-2+2*e,m-1+2*e)
check('symmetric product correction',m+(m+e)-(1-2*e),2*beta)
check('adjoint correction product',m-1+2*e+m+e,2*beta)
check('lower commutator product',m+m-1+2*e,2*m-1+2*e)
check('generic positivity remainder',2*m+1-2*(1-2*e),2*m-1+4*e)
check('generic order excess',(2*m-1+4*e)-2*beta,e)
g=2*R**(1-e);q=k*R**(m-1+2*e);qd=-s.I*R**(m-1+e)
check('sharp derivative quotient',R**2/g,R**(1+e)/2)
check('sharp Poisson bracket',qd*(-R),s.I*R**(m+e))
check('sharp phase value',-s.I*q*qd*(-R),k*R**(2*m-1+3*e))
check('negative imaginary contribution',-g*q**2,-2*k**2*R**(2*m-1+3*e))
check('combined sharp coefficient',-g*q**2-s.I*q*qd*(-R),(k-2*k**2)*R**(2*beta))
check('maximizing coefficient derivative',s.diff(k-2*k**2,k).subs(k,s.Rational(1,4)),0)
check('maximum coefficient',(k-2*k**2).subs(k,s.Rational(1,4)),s.Rational(1,8))
check('ordinary endpoint',beta.subs(e,0),m-s.Rational(1,2))
check('quarter endpoint',beta.subs(e,s.Rational(1,4)),m-s.Rational(1,8))
check('quarter remainder',(2*beta).subs(e,s.Rational(1,4)),2*m-s.Rational(1,4))
check('quarter generic remainder',(2*m-1+4*e).subs(e,s.Rational(1,4)),2*m)
z=s.symbols('z',positive=True);cross=(s.sqrt(65)-1)/8
check('plotted switching equation',(1+4*z-4/z).subs(z,cross),0)
source=root/'local-sign-geometry-and-complex-cutoff-phase.md';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=dict(passed=all(x['passed'] for x in cases),total_cases=len(cases),exact_algebraic_checks=len(cases),numerical_checks=0,cases=cases,source_sha256=sha(source),script_sha256=sha(Path(__file__)),full_complex_operator_estimate_proved=False)
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:result[k] for k in ['passed','total_cases','source_sha256']}))
