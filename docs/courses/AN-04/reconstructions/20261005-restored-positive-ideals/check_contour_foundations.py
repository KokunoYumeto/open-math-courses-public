"""Independent exact and numerical controls; never substitutes for the written proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent
checks=[]

# The full nonholomorphic homotopy identity, with two curved coordinates.
u,v,t=s.symbols('u v t',real=True)
zz=s.Matrix([u+s.I*t*(u+v*v),v+t*u*v+s.I*t*v])
cols=zz.jacobian([u,v]);vel=zz.diff(t);det=cols.det()
dets=[cols.copy() for _ in range(2)]
for j in range(2):dets[j][:,j]=vel
dj=[m.det() for m in dets]
z1,z2,b1,b2=s.symbols('z1 z2 b1 b2')
w=z1*z1*b2+b1*z2*z2+z1*z2
sub={z1:zz[0],z2:zz[1],b1:s.conjugate(zz[0]),b2:s.conjugate(zz[1])}
pull=s.expand(w.subs(sub))
lhs=s.diff(pull*det,t)-sum(s.diff(pull*dj[j],x) for j,x in enumerate([u,v]))
rhs=sum(s.diff(w,b).subs(sub)*(s.conjugate(vel[k])*det-sum(s.conjugate(cols[k,j])*dj[j] for j in range(2))) for k,b in enumerate([b1,b2]))
assert s.expand(lhs-rhs)==0
assert s.simplify(lhs.subs({u:s.Rational(1,3),v:s.Rational(2,5),t:s.Rational(1,2)}))!=0
checks.append({'name':'Exact curved nonholomorphic determinant homotopy','passed':True,
 'scope':'Full two-coordinate identity A4, all columns and conjugate defects; dropping the defect fails.'})

# Square-root derivative in a genuinely noncommuting direction.
E=np.array([[.08+.02j,.04-.01j],[.04-.01j,-.07+.015j]])
D=np.array([[.3,.2j],[.2j,-.4]])
powers=[np.eye(2,dtype=complex)]
for k in range(45):powers.append(powers[-1]@E)
C=np.eye(2,dtype=complex);der=np.zeros((2,2),complex);c=1.
for k in range(1,45):
 c*= (1.5-k)/k
 C+=c*powers[k]
 der+=c*sum((powers[j]@D@powers[k-1-j] for j in range(k)),np.zeros((2,2),complex))
assert np.linalg.norm(C@C-np.eye(2)-E)<2e-14
assert np.linalg.norm(C-C.T)<2e-14
assert np.linalg.norm(der@C+C@der-D)<2e-14
assert np.linalg.norm(2*C@der-D)>1e-3
checks.append({'name':'Symmetric square series and noncommuting derivative','passed':True,
 'scope':'Forty-four terms, square identity, symmetry and full ordered derivative; the commuting shortcut fails.'})

# Direct two-dimensional quadrature versus the independent matrix-path ODE.
M=np.array([[2+1j,.4-.3j],[.4-.3j,1.5+.7j]])
I=np.eye(2);D=M-I
def trace(q):return np.trace(np.linalg.solve(I+q*D,D))
integral=quad(lambda q:trace(q).real,0,1,epsabs=1e-13)[0]+1j*quad(lambda q:trace(q).imag,0,1,epsabs=1e-13)[0]
expected=2*np.pi*np.exp(-integral/2)
nodes,weights=np.polynomial.hermite.hermgauss(90)
X,Y=np.meshgrid(nodes,nodes,indexing='ij')
W=weights[:,None]*weights[None,:]
Q=M[0,0]*X*X+2*M[0,1]*X*Y+M[1,1]*Y*Y
integrand=W*np.exp(-Q/2+X*X+Y*Y)
actual=integrand.sum()
mom=np.array([[(integrand*X*X).sum(),(integrand*X*Y).sum()],
              [(integrand*X*Y).sum(),(integrand*Y*Y).sum()]])
assert abs(actual-expected)<3e-12
assert np.linalg.norm(mom-np.linalg.inv(M)*actual)<3e-12
# In dimension three the principal scalar root of the determinant has the wrong sign.
scalar=1+2j
correct=scalar**(-1.5);wrong=(scalar**3)**(-.5)
assert abs(correct+wrong)<1e-14 and abs(correct-wrong)>.1
checks.append({'name':'Matrix Gaussian path, full moments and branch sign','passed':True,
 'quadrature_error':float(abs(actual-expected)),
 'scope':'Independent 90-by-90 quadrature and path integration, all second moments, and a three-dimensional wrong-principal-root control.'})

# Every original exact model identity M1--M7.
x1,x2,p,y,a=s.symbols('x1 x2 p y a',real=True)
f=x1*x1/2+x2*x2/2+s.I*(x2-p)**2
T=(4+2*s.I)*p/5;f0=(2+s.I)*p*p/5
assert s.simplify(s.diff(f,x2).subs(x2,T))==0
assert s.simplify(f.subs({x1:0,x2:T})-f0)==0
assert s.simplify(s.im(f.subs({x1:0,x2:u+s.I*y}))-((u-p+y/2)**2+p*y-5*y*y/4))==0
assert s.expand(f-f0-x1*x1/2-(1+2*s.I)*(x2-T)**2/2)==0
assert s.simplify(s.im(f0)-s.Rational(5,4)*s.im(T)**2)==0
theta=.5*np.arctan(.5)
assert abs(np.sin(2*theta)+2*np.cos(2*theta)-np.sqrt(5))<1e-14
assert abs(np.exp(1j*theta)*5**(-.25)-(2-1j)**(-.5))<1e-14
checks.append({'name':'Complete semipositive virtual-critical-point model','passed':True,
 'scope':'Exact stationarity, value, translation, square completion, shift bound, final damping and Gaussian branch M1--M7.'})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'AN04-contour-foundation-checks/v1','passed':True,'checks':checks,
 'script_sha256':sha(Path(__file__)),'foundations_sha256':sha(HERE/'contour-and-gaussian-foundations.md'),
 'companion_sha256':sha(HERE/'complex-stationary-contract.md'),
 'general_theorems_certified_by_finite_checks':False}
(HERE/'contour-foundation-checks.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'gaussian_quadrature_error':float(abs(actual-expected))}))
