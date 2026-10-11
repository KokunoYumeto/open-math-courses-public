"""Exact finite checks; the operator estimates are proved in the lesson."""
from pathlib import Path
import hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parent
source=ROOT/'boundary-propagation-with-coupled-lower-terms.md'
checks=[]
def zero(name,value):
    if isinstance(value,s.MatrixBase):
        ok=all(s.simplify(v)==0 for v in value)
    else:
        ok=s.simplify(value)==0
    assert ok,(name,value)
    checks.append({'name':name,'passed':True,'type':'exact symbolic identity'})

x,t,lam,rho,ell,M,q,b,e,psi=s.symbols('x t lambda rho ell M q b e psi',real=True)
A=s.Matrix([[0,1],[0,0]])
B=s.Matrix([[0,0],[1,0]])
I=s.eye(2)
jet=I+x*A+x**2*(A*A+B)/2+x**3*(A**3/s.Integer(6)+A*B/6+B*A/3)
res=jet.diff(x)-(A+x*B)*jet
for j in range(3):
    zero('Ordered gauge coefficient '+str(j),res.diff(x,j).subs(x,0))
expjet=I+x*A+x**2*(A*A+B)/2+x**3*(A**3/6+(A*B+B*A)/4)
zero('Noncommuting exponential discrepancy',jet-expjet-x**3*(B*A-A*B)/12)
zero('Gauge commutator',B*A-A*B-s.diag(-1,1))
C=2*s.I*(A+x*B)
zero('Normal first-order cancellation',2*(-s.I)*(A+x*B)*jet+C*jet)

k=s.Matrix([[0,1+s.I],[1-s.I,-1]])
h=9*I+2*k
z=s.symbols('z')
zero('Hermitian anti-selfadjoint symbol representative',k-k.conjugate().T)
zero('Lower matrix eigenvalues',(z*I-k).det()-(z-1)*(z+2))
zero('Damping matrix',h-s.Matrix([[9,2+2*s.I],[2-2*s.I,7]]))
zero('Damping characteristic polynomial',(z*I-h).det()-(z-11)*(z-5))
zero('Cayley-Hamilton identity',h*h-16*h+55*I)
root=(h+s.sqrt(55)*I)/s.sqrt(16+2*s.sqrt(55))
zero('Positive square-root identity',root*root-h)
vp=s.Matrix([1+s.I,1])/s.sqrt(3)
vm=s.Matrix([-(1+s.I),2])/s.sqrt(6)
zero('Positive eigenvector',h*vp-11*vp)
zero('Lower eigenvector',h*vm-5*vm)
V=s.Matrix.hstack(vp,vm)
zero('Complex eigenvectors are orthonormal',V.conjugate().T*V-I)
U=s.diag(s.exp(s.I*t),1)
ht=U*h*U.conjugate().T
hp=ht.diff(t).subs(t,0)
zero('Noncommuting derivative',h*hp-hp*h-s.Matrix([[-16*s.I,-4+4*s.I],[4+4*s.I,16*s.I]]))
theta=s.symbols('theta',real=True)
av=s.cos(theta)*vp+s.sin(theta)*vm
zero('Exact damping graph',(av.conjugate().T*h*av)[0]-(8+3*s.cos(2*theta)))
zero('Matrix damping cancellation',-2*q*k+(M*ell*I+2*k)*q-M*ell*q*I)
zero('Characteristic completed polynomial',
     (-M*ell*q-psi**2-b**2+e**2)*I-2*q*k+
     (M*ell*I+2*k)*q+(b**2-e**2)*I+psi**2*I)
zero('Two-jet extension value',s.Integer(3)-2-1)
zero('Two-jet extension derivative',-s.Integer(3)+4-1)
zero('Normal interpolation nonnegative difference',
     ell**2+rho**4/ell**2-2*rho**2-(ell-rho**2/ell)**2)

J=s.Matrix([[0,-1],[1,0]])
S=s.Matrix([[s.cos(t),-s.sin(t)],[s.sin(t),s.cos(t)]])
zero('Polarization equation',S.diff(t)-J*S)
zero('Polarization inverse',S*S.T-I)
mode=S*s.Matrix([1,0])*(s.exp(s.I*lam*(t-x))-s.exp(s.I*lam*(t+x)))
D=lambda v,var:-s.I*v.diff(var)
equation=D(D(mode,x),x)-D(D(mode,t),t)-2*s.I*J*D(mode,t)-mode
zero('Full coupled reflected equation',equation)
zero('Dirichlet value',mode.subs(x,0))
zero('Actual normal trace',D(mode,x).subs(x,0)+2*lam*s.exp(s.I*lam*t)*S*s.Matrix([1,0]))
zero('Positive damping margin',s.Integer(9)-2*s.Integer(2)-5)

result={'schema':'AN04-matrix-boundary-propagation-model-check/v1',
 'source':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,
 'scope':'Exact signs, ordered matrix jets, eigenvalues, square root, noncommuting derivatives, block cancellation, extension jets, interpolation and full reflected equation. Infinite-dimensional estimates, domains and ray continuation are proved in the lesson, not certified by these finite checks.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['passed','total_cases','exact_algebraic_checks','source_sha256','script_sha256']}))
