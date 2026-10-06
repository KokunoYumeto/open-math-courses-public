"""Independent finite checks of A3, A4 and A5; the general proofs are written."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
N=s.zeros(6)
N[1,0]=N[2,1]=N[4,3]=1
C=s.eye(6)
for j in range(5):C[j,j+1]=j+1
Ni=C*N*C.inv()
v=C*s.Matrix([1,0,0,1,0,1])
ell=s.Matrix([[0,0,1,0,0,0]])*C.inv()
P=sum((Ni**j*v*ell*Ni**(2-j) for j in range(3)),s.zeros(6))
assert P*P==P and P*Ni==Ni*P and P.rank()==3
assert all(P*Ni**j*v==Ni**j*v for j in range(3))
assert [int((Ni**j).rank()) for j in range(4)]==[6,3,1,0]
K=s.Matrix.hstack(*P.nullspace())
assert P*Ni*K==s.zeros(6,3)
assert P!=P.T
checks=[{'name':'Nonorthogonal invariant chain projection in a mixed-length nilpotent matrix',
         'passed':True,'chain_lengths':[3,2,1],
         'scope':'Exact conjugated six-dimensional matrix, mixed chain generator, full functional formula, idempotence, commutation, range and invariant kernel.'}]
z=s.symbols('z')
spec=[(2*s.I,3),(-2*s.I,2),(s.Rational(1,2)+s.I,1)]
T0=N+s.diag(*[lam for lam,m in spec for _ in range(m)])
T=C*T0*C.inv()
poly=s.prod((z-lam)**m for lam,m in spec).expand()
def ev(expr):
    return sum((coef*T**power[0] for power,coef in s.Poly(expr,z).terms()),s.zeros(6))
assert s.simplify(ev(poly))==s.zeros(6)
projections=[]
for lam,m in spec:
    f=(z-lam)**m
    q=s.div(poly,f,z)[0]
    u=s.invert(q,f,z)
    pr=s.simplify(ev(s.expand(u*q)))
    assert s.simplify(pr**2-pr)==s.zeros(6) and s.simplify(pr*T-T*pr)==s.zeros(6) and pr.rank()==m
    assert s.simplify((T-lam*s.eye(6))**m*pr)==s.zeros(6)
    projections.append(pr)
assert s.simplify(sum(projections,s.zeros(6)))==s.eye(6)
assert all(s.simplify(projections[j]*projections[k])==s.zeros(6) for j in range(3) for k in range(3) if j!=k)
tn=np.array(T,dtype=complex)
expected=np.array(projections[0]+projections[2],dtype=complex)
angles=2*np.pi*np.arange(2048)/2048
actual=sum(4.5*np.exp(1j*a)*np.linalg.inv((5j+4.5*np.exp(1j*a))*np.eye(6)-tn) for a in angles)/len(angles)
error=float(np.linalg.norm(actual-expected))
assert error<1e-10 and np.linalg.norm(-actual-expected)>1
checks.append({'name':'Bezout splitting and oriented circle projection with unequal Jordan lengths',
               'passed':True,'contour_center':'5i','contour_radius':'9/2',
               'angular_samples':len(angles),'projection_residual':error,
               'scope':'Exact annihilating polynomial and all three complementary projections; independent numerical resolvent integral selects the two upper generalized summands.'})
result={'schema':'AN04-spectral-algebra-finite-checks/v1','passed':True,
        'script_sha256':sha(Path(__file__)),
        'source_sha256':sha(HERE/'spectral-algebra-and-contour-projections.md'),
        'checks':checks,'general_theorems_certified_by_finite_checks':False}
(HERE/'spectral-algebra-checks.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'checks':len(checks),'passed':True,'projection_residual':error}))
