"""Exact checks for output relocation, orthogonal assembly and crossed patches."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
 v=s.simplify(s.expand(expr));assert v==0,(name,v);checks.append(name)
def truth(name,condition):
 assert bool(condition),name;checks.append(name)
z,Z,b,R,L,mu=s.symbols('z Z b R L mu',positive=True)
check('forward after inverse affine map',b+mu*((z-b)/mu)-z)
check('inverse after forward affine map',((b+mu*Z)-b)/mu-Z)
for d in [1,2,3]:
 check(f'squared Jacobian cancellation d={d}',mu**(-d)*mu**d-1)
check('generic left endpoint',R+2-s.Rational(1,2)-(R+s.Rational(3,2)))
check('generic right endpoint',R+2+s.Rational(1,2)-(R+s.Rational(5,2)))
truth('generic positive separation',s.Rational(3,2)>0)
scale=s.Rational(1,6);center=s.Rational(9,2)
check('example left endpoint',center+scale*(-3)-4)
check('example right endpoint',center+scale*3-5)
check('example output gap',4-2-2)
check('example isometry amplitude',scale**(-s.Rational(1,2))-s.sqrt(6))
check('example input argument',(z-center)/scale-(6*z-27))
check('example inverse amplitude',scale**s.Rational(1,2)-1/s.sqrt(6))
for k in range(4):
 check(f'kernel derivative factor k={k}',scale**(-s.Rational(1,2)-k)-6**(s.Rational(1,2)+k))
q1,q2,r1,r2=s.symbols('q1 q2 r1 r2',real=True)
q=s.Matrix([q1,q2,0,0]);res=s.Matrix([0,0,r1,r2]);a=q+res
check('disjoint-output norm identity',(a.T*a)[0]-(q.T*q)[0]-(res.T*res)[0])
PQ=s.diag(1,1,0,0);PS=s.diag(0,0,1,1)
check('elliptic channel extraction',sum(PQ*a-q))
check('residual channel extraction',sum(PS*a-res))
u,v=s.symbols('u v',nonnegative=True)
check('sharp three-four-five inequality',25*(u*u+v*v)-(3*u+4*v)**2-(4*u-3*v)**2)
check('sharpness ratio',(4*u-3*v).subs({u:3,v:4}))
check('cancellation without separation',sum(s.Matrix([1,2])+s.Matrix([-1,-2])))
def allowed(base,eta):return (-2<base<-1 and eta>0) or (1<base<2 and eta<0)
truth('negative base positive covector allowed',allowed(s.Rational(-3,2),1))
truth('positive base negative covector allowed',allowed(s.Rational(3,2),-1))
truth('first crossed pair excluded',not allowed(s.Rational(-3,2),-1))
truth('second crossed pair excluded',not allowed(s.Rational(3,2),1))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(r/'one-scalar-test-across-boundary-chart-patches.md'),
 'script_sha256':sha(Path(__file__)),
 'scope':'Exact affine inverses, all displayed Jacobian and derivative factors, orthogonal channel identities, norm constants and crossed-patch geometry. Full boundary-kernel membership and uniform operator estimates are proved in the lesson.'}
(r/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
