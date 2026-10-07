"""Check finite algebraic identities in the new private system-branch preparation."""
from pathlib import Path
import datetime,hashlib,json
import sympy as s
r=Path(__file__).resolve().parents[4];c=Path(__file__).resolve().parent;f=c/'separated-system-branches-preparation.md'
rho,omega,theta=s.symbols('rho omega theta',real=True,positive=True)
R=s.Matrix([[s.cos(theta),-s.sin(theta)],[s.sin(theta),s.cos(theta)]])
J=s.Matrix([[0,-1],[1,0]]);L=s.diag(rho,-rho);K=s.Matrix([[0,omega/(2*s.I*rho)],[omega/(2*s.I*rho),0]])
zero=lambda M:all(s.simplify(v)==0 for v in M)
checks=[]
assert zero(R.T*R-s.eye(2)) and zero(R.T*R.diff(theta)-J)
checks.append('Rotating orthonormal frame and its signed time connection')
assert zero(s.I*L*K-K*s.I*L+omega*J)
checks.append('Both signed off-diagonal gap corrections cancel the connection')
z=s.symbols('z');q=s.I*L+omega*J
assert s.expand((z*s.eye(2)-q).det())==z**2+rho**2+omega**2
checks.append('Exact rotating-frame spectrum includes the lower-order correction')
x,y,w=s.symbols('x y w',real=True)
h=s.Matrix([[w,x-s.I*y],[x+s.I*y,-w]])
assert zero(h*h-(x*x+y*y+w*w)*s.eye(2))
checks.append('Pauli principal matrix has exactly the two uniformly separated branches on the unit sphere')
for sign in [1,-1]:
 pi=(s.eye(2)+sign*h)/2
 defect=pi*pi-pi
 assert all(s.simplify(s.expand(v).subs(y*y,1-x*x-w*w))==0 for v in defect)
 assert zero(h*pi-sign*pi-sign*(h*h-s.eye(2))/2)
checks.append('Both complementary Hermitian spectral projections satisfy the sphere identities')
phi=s.symbols('phi',real=True)
vn=s.Matrix([1,s.exp(s.I*phi)])/s.sqrt(2);vs=s.Matrix([s.exp(-s.I*phi),1])/s.sqrt(2)
assert zero(vs-s.exp(-s.I*phi)*vn)
heq=h.subs({x:s.cos(phi),y:s.sin(phi),w:0})
assert zero(heq*vn-vn) and zero(heq*vs-vs)
checks.append('Positive-eigenline equator frames have the exact negative-unit winding transition')
T,A,B,E,Rv,Tt,Rt=s.symbols('T A B E R Tt Rt',commutative=False)
commutation=(Tt+A*T-T*B)*E*Rv+T*E*(Rt+B*Rv-Rv*A)+T*(B*E-E*B)*Rv
direct=Tt*E*Rv+T*E*Rt+A*T*E*Rv-T*E*Rv*A
assert s.expand(commutation-direct)==0
checks.append('Ordered full-projector time commutator has the correct inverse-family sign')
t,xx=s.symbols('t xx',real=True)
th=s.Function('theta')(t);rot=R.subs(theta,th)
fplus=s.Function('fplus')(xx-t);fminus=s.Function('fminus')(xx+t)
u=rot*s.Matrix([fplus,fminus]);av=rot*s.diag(1,-1)*rot.T
residual=u.diff(t)+av*u.diff(xx)-s.diff(th,t)*J*u
for entry in residual:
    groups=s.collect(s.expand(entry),list(entry.atoms(s.Subs)),evaluate=False)
    assert all(s.trigsimp(v)==0 for v in groups.values())
assert zero(rot*rot.T-s.eye(2))
checks.append('Exact two-branch translation solves BR32 including rotating lower coefficient and initial identity')
assert zero(rot.T*(-s.diff(th,t)*J)*rot+rot.T*rot.diff(t))
checks.append('Specified lower coefficient cancels the eigenframe time connection exactly')
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
d={'schema':'an04-separated-system-branch-models/v1','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'checks':checks,'finite_groups':len(checks),'source_sha256':sha(f),'script_sha256':sha(Path(__file__)),'scope':'Finite algebraic model identities only; no general symbol, global evolution or topology theorem certified by these checks.','whole_receiving_proof_checked':False,'public_coverage_registered':False}
(c/'model-check.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
print(json.dumps({'model_groups':len(checks),'passed':True,'general_proof_certified':False}))
