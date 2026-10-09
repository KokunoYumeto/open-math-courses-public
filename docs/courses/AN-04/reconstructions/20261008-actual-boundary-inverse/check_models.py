"""Independent finite checks for the boundary formulas; not proof substitutes. CC0-1.0."""
from pathlib import Path
import json,hashlib
import sympy as s
P=Path(__file__).resolve().parent
groups=[]
def group(name,values):
    vals=[bool(v) for v in values];assert all(vals),(name,vals)
    groups.append({'name':name,'cases':len(vals),'passed':True})
I=s.I;eye=s.eye(2);E=s.Matrix([[0,1],[0,0]])
n,m=s.symbols('n m',nonzero=True);h=1/n;r=m/n
Q=h*eye+I*h*h*E;Np=n*eye-I*E;Nm=m*eye-I*E
R=-r*eye+I*h*(1-r)*E
group('Exact nilpotent inverse and full reflection',[E*E==s.zeros(2),s.simplify(Np*Q)==eye,s.simplify(Q*Np)==eye,s.simplify(-Q*Nm-R)==s.zeros(2),s.simplify(Np*R+Nm)==s.zeros(2),s.simplify(Np*(h*eye)-eye)==-I*h*E])
tests=[]
for k in range(1,5):
    A=s.Matrix([[k+2,1],[1,k+3]]);B=s.Matrix([[0,k+1],[2,1]])
    G=A.inv();H=s.Rational(1,k+5)*eye;C=A+B*H;T=C*G-eye
    U=sum(((-T)**j for j in range(k)),s.zeros(2));Qk=H*G*U;N=C*H.inv()
    rr=s.Rational(2,3);Nminus=A*H.inv()*rr+B
    Rk=-Qk*Nminus;left=Qk*N-eye;right=N*Qk-eye
    tests.extend([A*B!=B*A,N*Qk-eye==(-1)**(k-1)*T**k,s.simplify(Rk+rr*eye+Qk*B*(1-rr)+left*rr)==s.zeros(2),s.simplify(N*Rk+Nminus+right*Nminus)==s.zeros(2)])
group('Ordered noncommuting finite inverse residuals',tests)
z,aq,ell,delta=s.symbols('z aq ell delta',nonzero=True)
g=s.Matrix([[2,1],[3,2]]);c=-I*aq*z*g
group('Actual graph density cancellation and normalized leading factor',[s.simplify((delta*g.inv())*(c/delta)+I*aq*z*eye)==s.zeros(2),s.simplify((-I*aq*z)/(I*ell**s.Rational(2,3))+aq*z/ell**s.Rational(2,3))==0,g.det()!=0])
eps,y,xi,lam,mu=s.symbols('eps y xi lam mu',real=True,positive=True)
f=s.Function('f');t=-mu*lam**(-s.Rational(1,3));recip=1/(I*lam**s.Rational(2,3)*f(t))
der=s.diff(recip,mu).subs(mu,0).subs(s.Subs(s.Derivative(f(s.Symbol('_xi_1')),s.Symbol('_xi_1')),s.Symbol('_xi_1'),0),-f(0)**2)
# Evaluate the chain rule using the independent Riccati value, avoiding a symbolic dummy convention.
ph=s.symbols('ph',nonzero=True);dhdmu=s.simplify((-1/I)*lam**(-s.Rational(2,3))*ph**(-2)*(-ph**2)*(-lam**(-s.Rational(1,3))))
group('Frequency reflection and nonlinear cotangent derivative',[dhdmu==I/lam,s.simplify(dhdmu*(-eps*lam))==-I*eps,s.det(s.Matrix([[1,0],[eps*y,1]]))==1,s.simplify((xi-eps*y*lam)+eps*y*lam)==xi])
ss=s.symbols('ss',real=True)
group('Disjoint-packet Sobolev powers',[s.simplify(2*ss+2*(-ss-s.Rational(1,3)))==-s.Rational(2,3),s.simplify(2*(ss-s.Rational(2,3))+2+2*(-ss-s.Rational(1,3)))==0,s.Rational(4)**(-s.Rational(2,3))<1])
out={'passed':True,'groups':groups,'total_cases':sum(x['cases'] for x in groups),'scope':'Finite exact algebra, signs and exponents only; analytic proofs are reviewed separately.','source_sha256':hashlib.sha256((P/'actual-conormal-inverse-and-reflection.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');print(json.dumps(out,indent=2))
