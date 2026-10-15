"""Exact finite identities supporting the written proof; not a proof verifier. CC0."""
from pathlib import Path
import sympy as s,json,hashlib
root=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
    assert s.simplify(expr)==0,(name,expr)
    checks.append(name)
f,e,c,k=s.symbols('f e c k',real=True)
at,bt,ay,by=s.symbols('at bt ay by',real=True)
ut=at+s.I*bt;uy=ay+s.I*by
ur=(f+s.I*c)*ut-s.I*e*uy
z=s.Matrix([ut,ur,uy])
M=s.diag(1,-1,-1)+s.I*s.Matrix([[0,-c,0],[c,0,-e],[0,e,0]])
assert M==s.conjugate(M).T
checks.append('M Hermitian entry by entry')
Q=(s.conjugate(z).T*M*z)[0];Zu=f*ut-k*ur
flux=-2*s.re((M*z)[1]*s.conjugate(Zu))-k*Q
K=s.Matrix([[k*(1-e*e),k*e*(c-s.I*f)],[k*e*(c+s.I*f),2*f*f-k*(f*f+1+c*c)]])
v=s.Matrix([uy,ut])
check('full complex boundary matrix',flux-(s.conjugate(v).T*K*v)[0])
det=K.det()
check('determinant',det-(2*k*f*f*(1-e*e)-k*k*(f*f+1+c*c-e*e)))
check('strict Lorentz determinant',f*f*(1+c*c-e*e)-(f*c)**2-f*f*(1-e*e))
K0=K.subs({f:1,e:s.Rational(1,2),c:0,k:s.Rational(1,4)})
check('base determinant',K0.det()-s.Rational(17,64))
check('base trace',s.trace(K0)-s.Rational(27,16))
check('base coercivity ratio',K0.det()/s.trace(K0)-s.Rational(17,108))
check('base full gradient constant',s.Rational(17,108)/3-s.Rational(17,324))
check('shifted skew square',s.Rational(1,4)/(1-s.Rational(1,16))-s.Rational(4,15))
K1=K.subs({f:1,e:s.Rational(1,2),c:2,k:s.Rational(1,64)})
check('large c determinant',K1.det()-s.Rational(361,16384))
check('large c trace',s.trace(K1)-s.Rational(491,256))
check('large c form lower bound',K1.det()/s.trace(K1)-s.Rational(361,31424))
check('large c gradient lower bound',K1.det()/s.trace(K1)/11-s.Rational(361,345664))
sig=(e*e-1)/(2*e);alpha=(e*e+1)/(2*e)
check('wave mode',alpha*alpha-sig*sig-1)
check('boundary mode',alpha+sig-e)
check('growing temporal root',sig.subs(e,s.Rational(3,2))-s.Rational(5,12))
check('growing normal root',alpha.subs(e,s.Rational(3,2))-s.Rational(13,12))
check('growing lower amplitude exponent',sig.subs(e,s.Rational(3,2))+alpha.subs(e,s.Rational(3,2))-s.Rational(3,2))
check('exercise f square',1-s.Rational(1,4)-s.Rational(3,4))
check('exercise VW',-2+s.Rational(1,8)+s.Rational(15,8))
check('exercise c square',s.Rational(15,8)**2/s.Rational(3,4)-s.Rational(75,16))
check('exercise e square',s.Rational(75,16)-s.Rational(63,16)-s.Rational(3,4))
check('exercise strict determinant',s.Rational(3,4)*(1+s.Rational(63,16))-s.Rational(15,8)**2-s.Rational(3,16))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,
 'source_sha256':sha(root/'strict-complex-oblique-boundary-energy.md'),
 'script_sha256':sha(Path(__file__)),'scope':'Finite exact identities only; analytic arguments are in the lesson.'}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_algebraic_checks':len(checks)}))
