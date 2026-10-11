"""Exact algebra checks accompanying the analytic weighted reverse estimate."""
from pathlib import Path
import json,hashlib
import sympy as s
checks=[]
def eq(name,a,b=0):
 r=s.simplify(a-b);assert r==0,(name,r)
 checks.append({'name':name,'passed':True,'exact_residual':str(r)})
mu,lam=s.symbols('mu lam',positive=True)
sig=s.Rational(2,3)*mu**s.Rational(3,2)*lam**(-s.Rational(1,2))
a=mu/lam
eq('phase mu derivative',s.diff(sig,mu),s.sqrt(a))
eq('phase lambda derivative',s.diff(sig,lam),-a**s.Rational(3,2)/3)
eq('phase Euler identity',mu*s.diff(sig,mu)+lam*s.diff(sig,lam),sig)
eq('mu-mu Hessian',s.diff(sig,mu,2),1/(2*s.sqrt(mu*lam)))
eq('mu-lambda Hessian',s.diff(sig,mu,lam),-s.sqrt(mu)/(2*lam**s.Rational(3,2)))
eq('lambda-lambda Hessian',s.diff(sig,lam,2),mu**s.Rational(3,2)/(2*lam**s.Rational(5,2)))
eq('Hessian determinant',s.det(s.hessian(sig,(mu,lam))))
eq('squared displacement',s.diff(sig,mu)**2+s.diff(sig,lam)**2,a+a**3/9)
av=s.Rational(1,25)
eq('illustrated first displacement',s.sqrt(av),s.Rational(1,5))
eq('illustrated last displacement',-av**s.Rational(3,2)/3,-s.Rational(1,375))
eq('illustrated Airy argument',-av*s.Integer(4096)**s.Rational(2,3),-s.Rational(256,25))
for eps in [-1,1]:
 shift=eps*s.Rational(1,5)
 eq(f'left endpoint for sign {eps}',-s.Rational(1,10)+shift,s.Rational(-1+2*eps,10))
 eq(f'right endpoint for sign {eps}',s.Rational(1,10)+shift,s.Rational(1+2*eps,10))
 A,V,Z=s.symbols('A V Z')
 raw=A+Z*V;k=-s.I*eps*Z*V
 eq(f'opposite branch coefficient sign {eps}',raw+s.I*(-eps)*k,A)
 eq(f'same branch coefficient sign {eps}',raw+s.I*eps*k,A+2*Z*V)
 eq(f'recovered multiplier sign {eps}',((raw+s.I*eps*k)-(raw-s.I*eps*k))/2,Z*V)
ell,modF,L=s.symbols('ell modF L',positive=True)
eq('exact first weight constant',s.pi**-1*ell**s.Rational(5,3)*(s.sqrt(s.pi)/modF)**2,ell**s.Rational(5,3)/modF**2)
eq('stable weight decomposition',ell**s.Rational(5,3)/modF**2+L,
 s.pi**-1*ell**s.Rational(5,3)*(s.sqrt(s.pi)/modF)**2+L)
eq('normal inverse loss',s.Rational(1,3)-s.Rational(1,6),s.Rational(1,6))
eq('energy coefficient exponent',1-s.Rational(1,6),s.Rational(5,6))
eq('buffer beyond shifted interval',s.Rational(2,5)-s.Rational(3,10),s.Rational(1,10))
x,y=s.symbols('x y',real=True)
eq('finite-dimensional inclusion norm',s.expand_complex((x+s.I*y)*s.conjugate(x+s.I*y)),x*x+y*y)
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(HERE/'weighted-recovery-of-localized-airy-fields.md'),'script_sha256':sha(Path(__file__)),
 'checks':checks,'scope':'Exact phase derivatives, canonical displacement, coefficient signs, norm constants and example coordinates. The smoothing kernels, localization, PDE residual and reverse inequalities are proved in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
