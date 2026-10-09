"""Finite exact identities for the adjoint construction; original work: CC0."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
q,t,y=s.symbols('q t y',real=True);I=s.I
checks=[]
def zero(name,value):
    vals=list(value) if isinstance(value,s.MatrixBase) else [value]
    assert all(s.simplify(s.expand(x))==0 for x in vals),name
    checks.append({'name':name,'passed':True,'method':'exact symbolic identity'})
ip=lambda a,b:(b.conjugate().T*a)[0]

# Full normal Green sign with nonconstant, non-Hermitian matrices.
B=s.Matrix([[I*q,1+t],[q*t,-I]])
C=s.Matrix([[t,I*q],[y,1-I*t]])
u=(1-q)**3*s.Matrix([1+q*t+I*q*q, t+I*q])
v=(1-q)**3*s.Matrix([t*q+I,1+q*q+I*t])
L=lambda w:-w.diff(q,2)+B*w.diff(q)+C*w
Ls=lambda w:-w.diff(q,2)-(B.conjugate().T*w).diff(q)+C.conjugate().T*w
integrand=s.expand(ip(L(u),v)-ip(u,Ls(v)))
boundary=(ip(u.diff(q),v)-ip(u,v.diff(q)+B.conjugate().T*v)).subs(q,0)
zero('exact Green orientation and matrix order',s.integrate(integrand,(q,0,1))-boundary)
zero('formal adjoint first and zero coefficients',Ls(v)-(-v.diff(q,2)-B.conjugate().T*v.diff(q)+(C.conjugate().T-B.conjugate().T.diff(q))*v))

# Independently expand the full variable principal formal adjoint.
coords=[q,t,y]
G=s.Matrix([[-1,0,0],[0,2+q,t*y/5],[0,t*y/5,-2-y*y]])
Bs=[B,s.Matrix([[q,I*t],[y,1]]),s.Matrix([[I,y],[0,t*q]])]
v=s.Matrix([q*q+t*y+I*t*t,q*y*y+I*q*t+t])
direct=sum(((G[a,b]*v).diff(coords[a],coords[b]) for a in range(3) for b in range(3)),s.zeros(2,1))
direct-=sum(((Bs[a].conjugate().T*v).diff(coords[a]) for a in range(3)),s.zeros(2,1))
direct+=C.conjugate().T*v
Bt=[2*sum((G[a,b].diff(coords[a])*s.eye(2) for a in range(3)),s.zeros(2))-Bs[b].conjugate().T for b in range(3)]
Ct=sum((G[a,b].diff(coords[a],coords[b])*s.eye(2) for a in range(3) for b in range(3)),s.zeros(2))
Ct-=sum((Bs[a].conjugate().T.diff(coords[a]) for a in range(3)),s.zeros(2));Ct+=C.conjugate().T
expanded=sum((G[a,b]*v.diff(coords[a],coords[b]) for a in range(3) for b in range(3)),s.zeros(2,1))
expanded+=sum((Bt[a]*v.diff(coords[a]) for a in range(3)),s.zeros(2,1))+Ct*v
zero('full variable principal adjoint expansion',direct-expanded)
zero('adjoint first normal coefficient',Bt[0]+B.conjugate().T)

A=s.Matrix([[I,1],[0,-I]]);H=A.conjugate().T
T=s.cos(q)*s.eye(2)-s.sin(q)*H
Ti=s.cos(q)*s.eye(2)+s.sin(q)*H
zero('constant adjoint matrix square',H*H+s.eye(2))
zero('constant test gauge inverse',Ti*T-s.eye(2))
zero('constant test gauge equation',T.diff(q)+H*T)
test=s.Matrix([q*t+I*y,t*t+q*q*y])
normaladj=lambda w:-w.diff(q,2)+w.diff(t,2)-H*w.diff(q)
zero('constant conjugated adjoint',Ti*normaladj(T*test)-(-test.diff(q,2)+test.diff(t,2)+H*test.diff(q)))

H=s.Matrix([[t,1],[-t*t,-t]]);Ht=H.diff(t)
T=s.eye(2)-q*H;Ti=s.eye(2)+q*H
zero('time-dependent nilpotence',H*H)
zero('ordered H times time derivative',H*Ht+H)
zero('ordered time derivative times H',Ht*H-H)
zero('time-dependent inverse',Ti*T-s.eye(2))
op=lambda w:-w.diff(q,2)+w.diff(t,2)-H*w.diff(q)
expected=-test.diff(q,2)+test.diff(t,2)+H*test.diff(q)
expected+=(-2*q*Ht+2*q*q*H)*test.diff(t)+(-q*H.diff(t,2)-q*q*H*H.diff(t,2))*test
zero('all time-dependent adjoint gauge coefficients',Ti*op(T*test)-expected)
zero('exact transformed test Robin condition',(T*test).diff(q)+H*T*test-T*test.diff(q))

chi=t**3-2*t+1
opA=lambda w:-w.diff(q,2)+w.diff(t,2)+A*w.diff(q)
zero('entire temporal cutoff commutator',opA(chi*test)-chi*opA(test)-2*s.diff(chi,t)*test.diff(t)-s.diff(chi,t,2)*test)
zero('temporal cutoff preserves normal trace',(chi*test).diff(q).subs(q,0)-chi*test.diff(q).subs(q,0))

# First inverse one-sided multiplier on an exact terminal input.
r,h=s.symbols('r h',positive=True)
tau=s.symbols('tau',real=True)
kernel=s.exp(-h*(r-tau))
zero('backward resolvent kernel differential equation',h*kernel-s.diff(kernel,tau))
a=s.exp(-1/t);b=s.exp(-1/(1-t));cut=b/(a+b)
zero('flat cutoff midpoint',cut.subs(t,s.Rational(1,2))-s.Rational(1,2))
zero('flat cutoff midpoint slope',s.diff(cut,t).subs(t,s.Rational(1,2))+2)
zero('solution gauge boundary cancellation',-I*s.diff(s.exp(-I*q),q)+s.exp(-I*q))
zero('adjoint gauge boundary cancellation',s.diff(s.exp(-q),q)+s.exp(-q))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'source_sha256':sha(ROOT/'causal-matrix-robin-existence-and-regularity.md'),
        'script_sha256':sha(Path(__file__)),'checks':checks,
        'scope':'Exact finite identities only. Supported existence, trace recovery and continuation are proved in the lesson.',
        'public_release_authorized':False}
(ROOT/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_cases':len(checks)}))
