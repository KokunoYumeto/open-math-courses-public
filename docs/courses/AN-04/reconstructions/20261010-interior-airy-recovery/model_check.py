"""Finite exact checks of the coefficient conversion, branch geometry and orders."""
from pathlib import Path
import hashlib,json
import sympy as s
checks=[]
def eq(name,a,b=0):
 r=s.simplify(a-b)
 assert r==0,(name,r)
 checks.append({'name':name,'passed':True,'exact_residual':str(r)})
A,B,Ap,Bp=s.symbols('A B Ap Bp')
g,h,f,k,alpha,v,z=s.symbols('g h f k alpha v z')
yp=g*(A-s.I*B)+s.I*h*(Ap-s.I*Bp)
ym=g*(A+s.I*B)+s.I*h*(Ap+s.I*Bp)
eq('exact two-mode field',(yp*(f+s.I*k)+ym*(f-s.I*k))/2,
   (g*A+s.I*h*Ap)*f+(g*B+s.I*h*Bp)*k)
for ep in [1,-1]:
 ff=alpha+z*v;kk=-s.I*ep*z*v
 eq('stable decaying branch '+str(ep),ff-s.I*ep*kk,alpha)
 eq('stable normalized branch '+str(ep),ff+s.I*ep*kk,alpha+2*z*v)
 eq('recover normalized coefficient '+str(ep),((ff+s.I*ep*kk)-(ff-s.I*ep*kk))/2,z*v)
q,lam=s.symbols('q lam',positive=True)
mu=s.symbols('mu',real=True);V=q+mu/lam
phase=s.Rational(2,3)*lam*V**s.Rational(3,2)
eq('affine mu graph shift',s.diff(phase,mu),s.sqrt(V))
eq('affine lambda graph shift',s.diff(phase,lam),s.Rational(2,3)*V**s.Rational(3,2)-mu/lam*s.sqrt(V))
eq('affine normal covector',s.diff(phase,q),lam*s.sqrt(V))
eq('Airy argument derivative',s.diff(-mu*lam**(-s.Rational(1,3))-q*lam**s.Rational(2,3),q),-lam**s.Rational(2,3))
eq('normal gap sign',-2*s.sqrt(lam**s.Rational(2,3)*V)*(-lam**s.Rational(2,3)),2*lam*s.sqrt(V))
eq('branch amplitude order',s.Rational(2,3)*(-s.Rational(1,4)),-s.Rational(1,6))
eq('normal operator order',-s.Rational(1,6)*2,-s.Rational(1,3))
eq('extractor net order',s.Rational(1,3)-s.Rational(1,6),s.Rational(1,6))
eq('energy coefficient exponent',1-s.Rational(1,6),s.Rational(5,6))
r=s.symbols('r')
eq('all-shift fixed-q normalized order',r-s.Rational(1,6)-r+s.Rational(1,6))
ar,ai,br,bi=s.symbols('ar ai br bi',real=True)
aa=ar+s.I*ai;bb=br+s.I*bi
eq('complex parallelogram',s.expand_complex(abs(aa+s.I*bb)**2+abs(aa-s.I*bb)**2-2*abs(aa)**2-2*abs(bb)**2))
a,R=s.symbols('a R',positive=True)
eq('elliptic boundary weight',R**s.Rational(4,3)/(a*R**s.Rational(2,3))**s.Rational(1,2),R/s.sqrt(a))
eq('normalized weighted packet exponent',1+2*(-s.Rational(1,2)))
eq('boundary exponential rate',s.Rational(2,3)*(a*R**s.Rational(2,3))**s.Rational(3,2),s.Rational(2,3)*a**s.Rational(3,2)*R)
eq('affine differential equation',-lam**s.Rational(4,3)*(-mu*lam**(-s.Rational(1,3))-q*lam**s.Rational(2,3))-q*lam**2-mu*lam)
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(HERE/'interior-airy-coefficient-recovery.md'),'script_sha256':sha(Path(__file__)),
 'checks':checks,'scope':'Exact finite coefficient, phase, sign and order checks. Uniform analytic estimates, support reductions and the failure theorem are proved in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
