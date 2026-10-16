"""Finite exact identities for the positive-beam proof. CC0-1.0."""
from pathlib import Path
import sympy as S,json,hashlib
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    if isinstance(value,S.MatrixBase):
        assert all(S.simplify(x)==0 for x in value),(name,value)
    else:assert S.simplify(value)==0,(name,value)
    checks.append(name)
s,b=S.symbols('s b',real=True,positive=True)
Q=S.cos(s)+S.I*b*S.sin(s);F=-S.sin(s)+S.I*b*S.cos(s);M=F/Q
check('linear position equation',S.diff(Q,s)-F)
check('linear momentum equation',S.diff(F,s)+Q)
check('Hermitian invariant',S.conjugate(Q)*F-S.conjugate(F)*Q-2*S.I*b)
check('Riccati equation',S.diff(M,s)+1+M*M)
check('imaginary part',(M-S.conjugate(M))/(2*S.I)-b/(S.cos(s)**2+b*b*S.sin(s)**2))
check('real part',S.re(M)-(b*b-1)*S.sin(s)*S.cos(s)/(S.cos(s)**2+b*b*S.sin(s)**2))
check('focusing Q',Q.subs({b:S.Rational(1,2),s:S.pi/2})-S.I/2)
check('focusing M',M.subs({b:S.Rational(1,2),s:S.pi/2})-2*S.I)
check('initial M',M.subs(s,0)-S.I*b)
# A genuinely coupled, noncommuting 2x2 Hessian at one point.
A=S.Matrix([[1,2],[2,-1]]);B=S.Matrix([[0,3],[-2,1]]);C=S.Matrix([[2,1],[1,3]])
Q0=S.eye(2);F0=S.Matrix([[1+2*S.I,3],[3,-2+S.I]])
Qd=B*Q0+C*F0;Fd=-A*Q0-B.T*F0
check('matrix Lagrangian invariant derivative',Qd.T*F0+Q0.T*Fd-Fd.T*Q0-F0.T*Qd)
check('matrix Hermitian invariant derivative',S.conjugate(Qd).T*F0+Q0.T*Fd-S.conjugate(Fd).T*Q0-S.conjugate(F0).T*Qd)
check('matrix ordered Riccati quotient',Fd-F0*Qd-(-A-B.T*F0-F0*B-F0*C*F0))
# Direct exact gauge calculation with variable principal and complex lower terms.
t,lam=S.symbols('t lam',real=True)
phi=t+s+S.I*(s*s+t*t)/2;v=1+s*s+s*t+S.I*t*t
g=[1,-(1+s*s)];lower=[s+S.I,1+S.I*t];zero=s-S.I*t
coords=[s,t];osc=S.exp(S.I*lam*phi)
P=lambda w:sum(-g[j]*S.diff(w,coords[j],2)-S.I*lower[j]*S.diff(w,coords[j]) for j in range(2))+zero*w
pr=sum(g[j]*S.diff(phi,coords[j])**2 for j in range(2))
tr=sum(2*g[j]*S.diff(phi,coords[j])*(-S.I*S.diff(v,coords[j]))+
       (g[j]*(-S.I*S.diff(phi,coords[j],2))+lower[j]*S.diff(phi,coords[j]))*v for j in range(2))
check('full gauge identity including complex lower terms',S.expand(P(osc*v)/osc-lam**2*pr*v-lam*tr-P(v)))
# The root example has exactly the asserted real central Hessian.
x,xi,tau=S.symbols('x xi tau',real=True)
hh=-S.sqrt((1-x*x)*tau*tau-xi*xi)
at={x:0,xi:0,tau:1}
check('root oscillator yy',S.diff(hh,x,2).subs(at)-1)
check('root oscillator etaeta',S.diff(hh,xi,2).subs(at)-1)
check('root central temporal velocity',S.diff(hh,tau).subs(at)+1)
check('root central tautau',S.diff(hh,tau,2).subs(at))
phip=t+s+S.I*(t+s)**2/2;phim=t-s+S.I*(t-s)**2/2
for name,ph in [('plus',phip),('minus',phim)]:
    check(name+' exact wave eikonal',S.diff(ph,s)**2-S.diff(ph,t)**2)
    check(name+' exact wave second derivative',S.diff(ph,s,2)-S.diff(ph,t,2))
check('common boundary phase',(phip-phim).subs(s,0))
check('normal trace gap',(S.diff(phip,s)-S.diff(phim,s)).subs(s,0)-2*(1+S.I*t))
z=S.symbols('z',positive=True)
check('log integrable comparison primitive',S.diff(S.log(1+z*z)/2,z)-z/(1+z*z))
check('width at focusing',1/S.sqrt(S.im(M).subs({b:S.Rational(1,2),s:S.pi/2}))-1/S.sqrt(2))
check('width at initial',1/S.sqrt(S.im(M).subs({b:S.Rational(1,2),s:0}))-S.sqrt(2))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,'source_sha256':sha(ROOT/'positive-complex-beams-and-reflected-pairs.md'),
 'script_sha256':sha(Path(__file__)),'scope':'Finite algebraic identities; the all-order analytic arguments are in the lesson.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_algebraic_checks':len(checks)}))
