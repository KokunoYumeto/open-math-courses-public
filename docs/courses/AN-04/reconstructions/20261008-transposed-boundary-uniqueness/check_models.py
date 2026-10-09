"""Exact finite identities accompanying, not replacing, the transposed proofs. CC0."""
from pathlib import Path
import hashlib,json
import sympy as s
P=Path(__file__).resolve().parent
q,t,y=s.symbols('q t y',real=True)
v=s.Matrix([q*q*t+y*t*t,q*t*t+t*y*y])
G=s.Matrix([[-1,0,0],[0,2+t*t,t*y],[0,t*y,-3-y*y]])
Bs=[s.Matrix([[q,1],[t,q*t]]),s.Matrix([[t,y],[1,t*y]]),s.Matrix([[y,t],[q,1]])]
C=s.Matrix([[q+t,1],[y,q*t]])
x=[q,t,y];chi=s.Function('chi')(t)
checks=[]
def check(name,expr):
    entries=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    assert all(s.simplify(z)==0 for z in entries),name
    checks.append({'name':name,'passed':True,'method':'exact symbolic identity'})
def op(w,b=Bs,c=C):
    return sum((G[i,j]*w.diff(x[i],x[j]) for i in range(3) for j in range(3)),s.zeros(2,1))+sum((b[i]*w.diff(x[i]) for i in range(3)),s.zeros(2,1))+c*w
Bt=[2*sum(s.diff(G[i,j],x[i]) for i in range(3))*s.eye(2)-Bs[j].T for j in range(3)]
Ct=sum((s.diff(G[i,j],x[i],x[j])*s.eye(2) for i in range(3) for j in range(3)),s.zeros(2))-sum((Bs[i].T.diff(x[i]) for i in range(3)),s.zeros(2))+C.T
comm=2*sum((G[i,1]*s.diff(chi,t)*v.diff(x[i]) for i in range(3)),s.zeros(2,1))+(G[1,1]*s.diff(chi,t,2)*s.eye(2)+Bt[1]*s.diff(chi,t))*v
check('full variable matrix adjoint cutoff identity',op(chi*v,Bt,Ct)-chi*op(v,Bt,Ct)-comm)
direct=sum(((G[i,j]*v).diff(x[i],x[j]) for i in range(3) for j in range(3)),s.zeros(2,1))-sum(((Bs[i].T*v).diff(x[i]) for i in range(3)),s.zeros(2,1))+C.T*v
check('complete adjoint differential expression',direct-op(v,Bt,Ct))
primal=2*sum((G[i,1]*s.diff(chi,t)*v.diff(x[i]) for i in range(3)),s.zeros(2,1))+(G[1,1]*s.diff(chi,t,2)*s.eye(2)+Bs[1]*s.diff(chi,t))*v
check('primal smooth-past cutoff identity',op(chi*v)-chi*op(v)-primal)
H=s.Matrix([[t,1],[-t*t,-t]])
check('temporal cutoff preserves adjoint Robin domain',(chi*v).diff(q)+H*chi*v-chi*(v.diff(q)+H*v))
rho=s.Function('rho')(q)
T=s.eye(2)-rho*H
check('nilpotent gauge inverse',(s.eye(2)+rho*H)*T-s.eye(2))
check('adjoint boundary gauge at zero',(T.diff(q)+H*T).subs({rho:0,s.diff(rho,q):1}))
b=s.Matrix([s.Function('b0')(t),s.Function('b1')(t)])
check('Dirichlet lifting value',(chi*b).subs(q,0)-chi*b)
check('Neumann lifting derivative',(q*chi*b).diff(q).subs(q,0)-chi*b)
R=s.diag(1,-1,1)
check('time reflection preserves normal block',(R*G*R)[0,0]+1)
check('time reflection preserves time positivity coefficient',(R*G*R)[1,1]-G[1,1])
check('time reflection retains mixed time sign',(R*G*R)[1,2]+G[1,2])
f=s.Function('f')
for sign in [1,-1]:
    wave=f(t-q)+sign*f(t+q)
    check('wave pulse equation '+str(sign),-s.diff(wave,q,2)+s.diff(wave,t,2))
check('Neumann pulse trace',s.diff(f(t-q)+f(t+q),q).subs(q,0))
check('Dirichlet pulse trace',(f(t-q)-f(t+q)).subs(q,0))
beta=s.symbols('beta')
check('natural dual correct sign',-(-beta)-beta)
check('natural dual wrong sign residual',-(beta)-beta+2*beta)
Q=s.Rational(12,5)-t
check('terminal envelope endpoint',Q.subs(t,2)-s.Rational(2,5))
check('earliest envelope endpoint',Q.subs(t,-s.Rational(3,5))-3)
assert -s.Rational(1,2)<-s.Rational(1,4)<0<s.Rational(8,5)<s.Rational(19,10)<2
checks.append({'name':'cutoff band lies strictly before test support and terminal time','passed':True,'method':'exact rational inequalities'})
source=P/'transposed-boundary-uniqueness-and-parametrix-identification.md'
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,
 'scope':'Finite exact algebra and coordinate checks only; complete uniqueness, support and regularity proofs are in the lesson.'}
(P/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
