"""Exact model checks for the full normal commutator; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
q=s.symbols('q',real=True,nonnegative=True);I=s.I
checks=[]
def check(name,a,b=0):
 d=a-b
 ok=all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0
 assert ok,(name,s.simplify(d))
 checks.append({'name':name,'exact':True,'passed':True})
def adj(a):return s.conjugate(a.T)
def pair(f,g):return (adj(g)*f)[0]
def herm(a):return (a+adj(a))/2
def integral(a):return s.integrate(s.expand(a),(q,0,s.oo))
D=lambda u:-I*u.diff(q)

# A noncommuting variable matrix model tests the actual integrated identity.
A=s.exp(-q)*s.Matrix([[-1,q],[q,-2]])
B=s.Matrix([[q,I],[-I,1]])
H=s.Matrix([[1+q,q],[q,2]])
K=s.Matrix([[2,I*q],[-I*q,1]])
C=s.Matrix([[1+I,q],[2*I,-1+3*I]])
Q0=B-I*A.diff(q)/2
Q=lambda u:A*D(u)+Q0*u
P=lambda u:D(D(u))+C*D(u)-(H+I*K)*u
u=s.exp(-q)*s.Matrix([1+q,1+2*I*q]);v=D(u)
E=(H*A-A*H)/I
C11=2*A.diff(q)+(A*C-adj(C)*A)/I
C10=Q0.diff(q)+E/2-A*K-adj(C)*Q0/I
C01=adj(C10)
C00=herm(A*H.diff(q)+(H*Q0-Q0*H)/I)-(adj(Q0)*K+K*Q0)
boundary=(pair(A*v,v)+2*s.re(pair(Q0*u,v))+pair(herm(A*H)*u,u)).subs(q,0)
volume=integral(pair(C00*u,u)+pair(C01*v,u)+pair(C10*u,v)+pair(C11*v,v))
lhs=integral(2*s.im(pair(P(u),Q(u))))
check('Full variable noncommuting matrix Green identity',lhs,boundary+volume)
f=s.exp(-q)*s.Matrix([1,q+I]);g=s.exp(-2*q)*s.Matrix([q,1])
check('Normal multiplier Green form with ordered variable matrices',
      integral(pair(Q(f),g)-pair(f,Q(g))),I*pair(A*f,g).subs(q,0))
normal_boundary=(pair(A*v,v)+2*s.re(pair(Q0*u,v))).subs(q,0)
normal_volume=integral(2*pair(A.diff(q)*v,v)+2*s.re(pair(Q0.diff(q)*u,v)))
check('Normal second derivative contribution',integral(2*s.im(pair(D(D(u)),Q(u)))),normal_boundary+normal_volume)
HQminusQH=lambda w:H*Q(w)-Q(H*w)
check('Selfadjoint tangential contribution including normal derivative',
 integral(-2*s.im(pair(H*u,Q(u)))),s.re(pair(A*H*u,u)).subs(q,0)+integral(s.re(pair(HQminusQH(u)/I,u))))
check('Ordered imaginary tangential contribution',
 integral(-2*s.re(pair(K*u,Q(u)))),integral(-2*s.re(pair(A*K*u,v))-2*s.re(pair(adj(Q0)*K*u,u))))
check('Complex normal coefficient contribution',
 integral(2*s.im(pair(C*v,Q(u)))),integral(pair((A*C-adj(C)*A)*v/I,v)+2*s.im(pair(adj(Q0)*C*v,u))))

a,b,h,k,cR,cI=s.symbols('a b h k cR cI',real=True)
c=cR+I*cI
scalar=s.im((-1-h-I*k+I*c)*(b-I*a))
check('Scalar full identity',scalar,a*(1+h)-b*k+a*cI+b*cR)
subs={a:-1,b:2,h:3,k:5,cR:1,cI:4}
check('Scalar numerical boundary',(a*(1+h)).subs(subs),-4)
check('Scalar numerical volume',(-b*k+a*cI+b*cR).subs(subs),-12)
check('Scalar numerical total',scalar.subs(subs),-16)
check('Retained complex normal contribution',(a*cI+b*cR).subs(subs),-2)
for omega,space,expected in [(2,1,-3/s.sqrt(6)),(1,2,3/s.sqrt(6)),(1,1,0)]:
 check('Neumann boundary sign '+str((omega,space)),-(omega**2-space**2)/s.sqrt(1+omega**2+space**2),expected)
M=s.Matrix([[0,1],[0,0]]);R=s.Matrix([[0,0],[1,0]]);C=2*I*M
S=s.eye(2)+q*M;Sinv=s.eye(2)-q*M
check('Nilpotent inverse',Sinv*S,s.eye(2))
check('Ordered normal gauge equation',S.diff(q),-I*C*S/2)
check('Exact normal coefficient cancellation',2*D(S)+C*S,s.zeros(2))
check('Normal zeroth coefficient',D(D(S))+C*D(S),s.zeros(2))
check('Ordered transformed tangential matrix',Sinv*R*S,s.Matrix([[-q,-q**2],[1,q]]))
check('Quadratic noncommuting term',M*R*M,M)
check('Gauge boundary normal derivative',D(S).subs(q,0),-I*M)
check('Bare Neumann domain changes',D(S*s.Matrix([0,1])).subs(q,0),s.Matrix([-I,0]))
check('Scalar gauge cancellation',2*D(s.exp(q))+2*I*s.exp(q),0)
check('Scalar transformed potential',-(D(D(s.exp(q)))+2*I*D(s.exp(q)))/s.exp(q),-1)
check('Scalar transformed solution',D(D(s.exp(-q)))+s.exp(-q),0)
check('Scalar changed boundary slope',s.diff(s.exp(-q),q).subs(q,0),-1)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'source':'normal-commutators-on-the-weak-graph-domain.md','source_sha256':sha(HERE/'normal-commutators-on-the-weak-graph-domain.md'),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'passed':True,'checks':checks,
 'scope':'Exact integrated scalar and variable noncommuting matrix models, boundary signs and ordered gauges. General graph approximation and operator estimates are proved analytically in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_algebraic_checks':len(checks),'variable_matrix_identity':str(lhs),'variable_matrix_boundary':str(boundary),'variable_matrix_volume':str(volume)}))
