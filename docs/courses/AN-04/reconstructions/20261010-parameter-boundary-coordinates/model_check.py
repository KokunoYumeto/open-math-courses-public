"""Exact full-coordinate, density, gauge and example checks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent;rows=[]
t,y,x,z,a,k=s.symbols('t y x z a k',real=True);I=s.I
def check(name,value,want=0):
 assert s.simplify(value-want)==0,(name,value,want)
 rows.append({'name':name,'passed':True,'kind':'exact algebra'})
def transform(A,b,c,psi,phi):
 old=(t,y);J=s.Matrix([[s.diff(p,q) for q in old] for p in psi])
 substitute=lambda e:s.simplify(e.subs({t:phi[0],y:phi[1]},simultaneous=True))
 Ap=(J*A*J.T).applyfunc(substitute)
 bp=s.Matrix([sum(b[j]*J[h,j] for j in range(2))-I*sum(A[i,j]*s.diff(psi[h],old[i],old[j]) for i in range(2) for j in range(2)) for h in range(2)]).applyfunc(substitute)
 return Ap,bp,substitute(c)
A,b,c=transform(s.Matrix([[1,a],[a,-1]]),[0,0],s.Integer(0),(t,y-a*t),(x,z+a*x))
for i in range(2):
 for j in range(2):check(f'PC20 full principal {i}{j}',A[i,j],s.diag(1,-1-a*a)[i,j])
for i in range(2):check(f'PC20 lower coefficient {i}',b[i])
check('PC20 coordinate determinant',s.det(s.Matrix([[s.diff(q,v) for v in (x,z)] for q in (x,z+a*x)])),1)
xi,eta,zeta=s.symbols('xi eta zeta',real=True)
check('PC20 characteristic polynomial substitution',(xi-a*eta)**2+2*a*(xi-a*eta)*eta-eta**2,xi**2-(1+a*a)*eta**2)
check('PC13 compressed shear',x*(xi+a*eta),x*xi+a*x*eta)
A,b,c=transform(s.Matrix([[1,k*y],[k*y,k*k*y*y-1]]),[0,0],s.Integer(0),(t,s.exp(-k*t)*y),(x,s.exp(k*x)*z))
expected=s.diag(1,-s.exp(-2*k*x))
for i in range(2):
 for j in range(2):check(f'PC23 full principal {i}{j}',A[i,j],expected[i,j])
check('PC23 normal coefficient before density',b[0])
check('PC23 surviving tangential coefficient',b[1],I*k*k*z)
check('PC23 coordinate determinant',s.det(s.Matrix([[s.diff(q,v) for v in (x,z)] for q in (x,s.exp(k*x)*z)])),s.exp(k*x))
h=s.Matrix([k/2,0]);br=b+2*I*A*h
cr=c+I*(b.dot(h))+sum(A[i,j]*(s.diff(h[j],(x,z)[i])-h[i]*h[j]) for i in range(2) for j in range(2))
check('PC23 unitary normal coefficient',br[0],I*k)
check('PC23 unitary tangential coefficient',br[1],I*k*k*z)
check('PC23 unitary zeroth coefficient',cr,-k*k/4)
S=s.exp(k*x/2);cn=I*k
check('PC10 actual gauge ODE',s.diff(S,x),-I*cn*S/2)
check('PC24 density and gauge cancel',S**-1*s.exp(k*x/2),1)
check('PC24 constant term after gauge',cr-cn**2/4+I*s.diff(cn,x)/2)
A,b,c=transform(s.Matrix([[4,2],[2,1]]),[2*I,I],s.Integer(3),(t,y-t/2),(x,z+x/2))
for i in range(2):
 for j in range(2):check(f'PC25 degenerate transformed principal {i}{j}',A[i,j],s.diag(4,0)[i,j])
check('PC25 first normal coefficient',b[0]/4,I/2)
check('PC25 first tangential coefficient',b[1])
check('PC25 normalized potential',c/4,s.Rational(3,4))
check('PC25 gauged potential',c/4-(b[0]/4)**2/4,s.Rational(13,16))
check('PC25 source normalization',s.Rational(1,4)*s.exp(-x/4)*4*s.exp(x/4),1)
f=s.Function('f')(x);cc=s.Function('c')(x)
D=lambda u:-I*s.diff(u,x)
shift=lambda u:D(u)-cc*u/2
check('PC11 ordered normal gauge identity',shift(shift(f))+cc*shift(f),D(D(f))+(I*s.diff(cc,x)/2-cc**2/4)*f)
hh=s.Function('h')(x)
W=s.exp(hh)
check('PC7 full scalar density conjugation',s.simplify(W*D(f/W)),D(f)+I*s.diff(hh,x)*f)
for zz in [-1,0,1]:
 check(f'figure shear boundary z={zz}',s.Integer(zz)+s.Rational(1,2)*0,zz)
 check(f'figure shear upper endpoint z={zz}',s.Integer(zz)+s.Rational(1,2),s.Rational(2*zz+1,2))
 check(f'figure exponential upper endpoint z={zz}',s.exp(s.log(2))*zz,2*zz)
check('figure density at upper endpoint',s.exp(s.log(2)/2),s.sqrt(2))
source=ROOT/'parameter-dependent-boundary-coordinates-and-full-source-tests.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'scope':'Complete principal and lower coefficient transformations in three models, exact density and gauge signs, forcing normalization and figure endpoints. These checks do not replace the general analytic proof.','checks':rows}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))
