"""Exact finite identities supporting the proof; no numerical PDE claim."""
from pathlib import Path
import hashlib, json
import sympy as s

ROOT = Path(__file__).resolve().parent
q,t,y,lam = s.symbols('q t y lam', real=True)
I=s.I
checks=[]
def zero(name, value):
    values=list(value) if isinstance(value,s.MatrixBase) else [value]
    assert all(s.simplify(x)==0 for x in values), name
    checks.append({'name':name,'passed':True,'method':'exact symbolic identity'})

M=s.Matrix([[t,1],[-t*t,-t]])
Mt=M.diff(t); S=s.eye(2)-I*q*M; H=s.eye(2)+I*q*M
zero('nilpotent matrix',M*M)
zero('ordered M times derivative',M*Mt+M)
zero('ordered derivative times M',Mt*M-M)
zero('both gauge inverses',H*S-s.eye(2))
zero('noncommuting derivative correction',S.diff(t)-(-I*q*Mt*S)-q*q*M)
u=s.Matrix([q*q*t+I*y*t*t+q*y, t*q+y*y+I*q*q*y])
D=lambda f,x:-I*f.diff(x)
P=lambda f:D(D(f,q),q)-D(D(f,t),t)+D(D(f,y),y)+M*D(f,q)
claimed=P(u)-2*M*D(u,q)+(2*q*Mt-2*I*q*q*M)*D(u,t)+(-I*q*M.diff(t,2)+q*q*M*M.diff(t,2))*u
zero('full time-dependent conjugated operator',H*P(S*u)-claimed)
zero('exact entire normal flux',(D(S*u,q)+M*S*u)-S*D(u,q))
L0=s.Matrix([[1,I],[2,-1]]); M0=s.Matrix([[0,1],[I,2]])
A=-M0
zero('boundary Robin cancellation',M0+A)
zero('remaining normal derivative',L0+M0+2*A-(L0-M0))

# Independent variable-coefficient, complex-vector differentiation of the current.
coords=[q,t,y]
G=s.Matrix([[-1,0,0],[0,2+q,t/3],[0,t/3,-2-y*y]])
W=G[:,1]
B=[s.Matrix([[I*q,1],[t,-I]]),
   s.Matrix([[y,I],[0,q*t]]),s.Matrix([[t,0],[I*y,1]])]
C=s.Matrix([[I,t],[q,-y]])
ip=lambda a,b:(b.conjugate().T*a)[0]
real=lambda x:s.expand(s.re(x))
der=[u.diff(x) for x in coords]
Wu=sum((W[j]*der[j] for j in range(3)),s.zeros(2,1))
Q=sum(G[b,c]*ip(der[b],der[c]) for b in range(3) for c in range(3))
norm=ip(u,u)
J=[2*real(sum(G[a,b]*ip(der[b],Wu) for b in range(3)))-W[a]*Q+W[a]*norm for a in range(3)]
Lu=sum((G[a,b]*u.diff(coords[a],coords[b]) for a in range(3) for b in range(3)),s.zeros(2,1))
lower=sum((B[a]*der[a] for a in range(3)),s.zeros(2,1))+C*u
Lu+=lower
divW=sum(W[a].diff(coords[a]) for a in range(3))
R=2*real(sum(G[a,b].diff(coords[a])*ip(der[b],Wu) for a in range(3) for b in range(3)))
R+=2*real(sum(G[a,b]*W[c].diff(coords[a])*ip(der[b],der[c]) for a in range(3) for b in range(3) for c in range(3)))
R-=divW*Q+sum(W[a]*G[b,c].diff(coords[a])*ip(der[b],der[c]) for a in range(3) for b in range(3) for c in range(3))
R+=divW*norm+2*real(ip(u,Wu))-2*real(ip(lower,Wu))
zero('full current divergence with variable metric and complex matrices',
     sum(J[a].diff(coords[a]) for a in range(3))-2*real(ip(Lu,Wu))-R)
zero('physical normal flux',J[0]+2*real(ip(der[0],Wu)))
avec=G[1,1]; bvec=s.Matrix([G[0,1],G[2,1]])
spatial=[der[0],der[2]]; Csp=G.extract([0,2],[0,2])
energy=ip(avec*der[1]+sum((bvec[j]*spatial[j] for j in range(2)),s.zeros(2,1)),
          avec*der[1]+sum((bvec[j]*spatial[j] for j in range(2)),s.zeros(2,1)))
energy+=sum((bvec*bvec.T-avec*Csp)[j,k]*ip(spatial[j],spatial[k]) for j in range(2) for k in range(2))+avec*norm
zero('completed-square positive time current',J[1]-energy)
weight=s.exp(-lam*t)
zero('weighted divergence sign',sum((weight*J[a]).diff(coords[a]) for a in range(3))+lam*weight*J[1]-weight*(2*real(ip(Lu,Wu))+R))

# Exact Green orientation and prescribed normal jet.
z=s.symbols('z',real=True)
profile=(1-q)**2
test=1-q
form=s.integrate(s.diff(profile,q)*s.diff(test,q),(q,0,1))
interior=s.integrate(-s.diff(profile,q,2)*test,(q,0,1))
zero('Green boundary sign on compact interval',form-interior+I*D(profile,q).subs(q,0)*test.subs(q,0))
beta=s.Matrix([1+I*t,y-t*t])
lift=I*q*(1-q*q)**3*beta
zero('natural lifting exact flux',(D(lift,q)+M*lift).subs(q,0)-beta)
zero('natural lifting zero value',lift.subs(q,0))
theta=s.symbols('theta',real=True)
c=s.Rational(6,5); shift=s.Rational(1,2)
uy=s.sin(theta)/c; ut=s.cos(theta)-shift*uy
zero('figure exact unit energy ellipse',s.trigsimp((ut+shift*uy)**2+c*c*uy*uy-1))
jet=s.Matrix([0,1]); gauged=(S*jet).subs(t,0)
zero('figure gauge profile',gauged-s.Matrix([-I*q,1]))
zero('figure original flux cancellation',(D(gauged,q)+M.subs(t,0)*gauged))

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'source_sha256':sha(ROOT/'matrix-robin-energy-and-weak-uniqueness.md'),
        'script_sha256':sha(Path(__file__)),'checks':checks,
        'scope':'Finite identities only; weak approximation, domain of dependence and uniqueness are proved in the lesson.',
        'public_release_authorized':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_cases':len(checks)}))
