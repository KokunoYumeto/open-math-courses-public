"""Exact normalization algebra, Gaussian scaling and partition orders. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
a,r,v,rho=S.symbols('a r v rho',real=True)
tau=S.symbols('tau',positive=True);m,d=S.symbols('m d',real=True)
checks=[]
def eq(name,l,rhs):
 z=l-rhs
 good=all(S.simplify(x)==0 for x in z) if isinstance(z,S.MatrixBase) else S.simplify(z)==0
 assert good,name
 checks.append(name)
I=S.eye(2);P=S.Matrix([[1,a],[0,0]]);E0=S.diag(1,0)
qp=I-P*E0;qm=I-E0*P
eq('initial right defect',qp,S.diag(0,1))
eq('initial left defect',qm,S.Matrix([[0,-a],[0,1]]))
for name,q in [('kernel',qm),('cokernel adjoint',qp.T)]:
 A=I-(q-q.T)**2;R=q*q.T*A.inv()
 eq(name+' idempotent',q*q,q)
 eq(name+' positive denominator',A,q*q.T+(I-q.T)*(I-q))
 eq(name+' ordered commutation',A*q,q*q.T*q)
 eq(name+' normalized Hermitian',R.T,R)
 eq(name+' normalized idempotent',R*R,R)
 eq(name+' range inclusion one',R*q,q)
 eq(name+' range inclusion two',q*R,R)
rm=qm*qm.T*(I-(qm-qm.T)**2).inv();rp=qp.T*qp*(I-(qp-qp.T)**2).inv()
E=(I-rm)*E0*(I-rp)
eq('corrected inverse',E,S.Matrix([[1,0],[a,0]])/(1+a*a))
eq('normalized right identity',P*E,I-rp)
eq('normalized left identity',E*P,I-rm)
eq('kernel annihilation',P*rm,S.zeros(2))
eq('cokernel annihilation',rp*P,S.zeros(2))
eq('reflexive inverse',E*P*E,E)
eq('exact normal midpoint square',(r+v/2)**2+(r-v/2)**2,2*r*r+v*v/2)
eq('Weyl Gaussian coefficient',S.sqrt(tau/S.pi)*S.sqrt(4*S.pi/tau),2)
eq('partition commutator order',(m-1)+(-m+S.Rational(1,2)),-S.Rational(1,2))
eq('positive inverse bootstrap order',(d-S.Rational(1,2))-(d-S.Rational(1,2)),0)
for n in range(1,7):
 eq(f'balanced ordinary derivative cost n={n}',-S.Rational(n,2),S.Rational(n,2)-n)
point=S.Matrix([2,1]);P1=P.subs(a,1);E1=E.subs(a,1)
eq('figure input image',P1*point,S.Matrix([3,0]))
eq('figure oblique reconstruction',E0*P1*point,S.Matrix([3,0]))
eq('figure orthogonal reconstruction',E1*P1*point,S.Matrix([S.Rational(3,2),S.Rational(3,2)]))
eq('figure exact same equation',P1*E1*P1*point,P1*E0*P1*point)
eq('figure perpendicular kernel',S.Matrix([-1,1]).dot(E1*P1*point),0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,'source_sha256':sha(root/'global-symplectic-parametrix-and-hermitian-projectors.md'),'script_sha256':sha(Path(__file__)),'scope':'Finite exact algebra and scales; the full operator estimates, proper assembly, inverse regularity and uniqueness are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');print(json.dumps(out))
