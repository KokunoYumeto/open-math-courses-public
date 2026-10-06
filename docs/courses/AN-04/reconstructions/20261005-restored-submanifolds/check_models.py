"""Bounded independent coordinate and matrix models for the U012 author check."""
import hashlib,json
from pathlib import Path
import sympy as s
import numpy as np
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def omega(n):return s.zeros(n).row_join(-s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
def symplectic_change(n):
    P=s.Matrix(n,n,lambda i,j:i+j+1);Q=s.diag(*range(1,n+1))
    return (s.eye(n).row_join(Q).col_join(s.zeros(n).row_join(s.eye(n)))
            *s.eye(n).row_join(s.zeros(n)).col_join(P.row_join(s.eye(n))))
models=[]
for N,k,l in [(5,2,2),(3,1,1),(3,2,1),(2,0,1),(2,2,0),(2,0,2)]:
    O=omega(N);M=symplectic_change(N);assert M.T*O*M==O
    # E has k radical position columns and l free position/momentum pairs.
    columns=list(range(k+l))+list(range(N+k,N+k+l))
    E=M[:,columns];orthogonal_basis=(E.T*O).nullspace()
    Ew=s.Matrix.hstack(*orthogonal_basis) if orthogonal_basis else s.zeros(2*N,0)
    assert E.rank()==k+2*l and (E.T*O*E).rank()==2*l
    assert Ew.rank()==2*N-k-2*l
    assert (Ew.T*O*Ew).rank()==2*(N-k-l)
    Z=M[:,:k];assert Z.T*O*E==s.zeros(k,k+2*l)
    W=s.Matrix.hstack(E,Ew);basis=s.Matrix.hstack(*W.columnspace())
    assert basis.rank()==2*N-k and (basis.T*O*basis).rank()==2*(N-k)
    E0=M[:,list(range(k,k+l))+list(range(N+k,N+k+l))]
    E1=M[:,list(range(k+l,N))+list(range(N+k+l,2*N))]
    assert E0.T*O*E1==s.zeros(2*l,2*(N-k-l))
    models.append({'N':N,'radical_k':k,'restricted_half_rank':l,
                   'orthogonal_rank':2*(N-k-l),'quotient_rank':2*(N-k),
                   'coisotropic':k+l==N})
checks.append({'name':'three-block and quotient dimensions after symplectic changes',
               'models':models,'passed':True})

x1,x2,xi1,xi2=s.symbols('x1 x2 xi1 xi2',real=True)
coords=s.Matrix([x1,x2,xi1,xi2]);O=omega(2)
def H(f,u=coords):
    n=len(u)//2
    return s.Matrix([s.diff(f,v) for v in u[n:]]+[-s.diff(f,v) for v in u[:n]])
def bracket(f,g,u=coords):return (H(f,u).T*s.Matrix([s.diff(g,v) for v in u]))[0]
f=xi2-x2*xi1;q=x2
Q1,qv,P1,p,t=s.symbols('Q1 q P1 p t',real=True)
params=s.Matrix([Q1,qv,P1,p])
Psi=s.Matrix([Q1-qv*qv/2,qv,P1,p+qv*P1]);J=Psi.jacobian(params)
assert s.simplify(J.T*O*J-O)==s.zeros(4)
subs=dict(zip(coords,Psi));assert s.expand(f.subs(subs,simultaneous=True))==p
assert J[:,1]==H(f).subs(subs,simultaneous=True)
assert J[:,3]==-H(q).subs(subs,simultaneous=True)
old_lambda=s.Matrix([xi1,xi2,0,0])
assert s.simplify(J.T*old_lambda.subs(subs,simultaneous=True))==s.Matrix([P1,p,0,0])
assert s.simplify(Psi.subs({P1:t*P1,p:t*p},simultaneous=True)-s.diag(1,1,t,t)*Psi)==s.zeros(4,1)
Q=s.Matrix([x1+x2*x2/2,x2,xi1,f])
brackets=s.Matrix(4,4,lambda i,j:bracket(Q[i],Q[j]))
assert brackets==O
checks.append({'name':'actual canonical-pair flow map, signs and dilation',
 'flow_map':'(Q1,q,P1,p) -> (Q1-q^2/2,q,P1,p+q P1)',
 'full_symplectic_pullback':True,'canonical_one_form_preserved':True,
 'f_is_exactly_p':True,'parameter_derivatives':'d/dq=H_f, d/dp=-H_q',
 'coordinate_brackets_checked':16,'passed':True})

q1,q2,q3,p1,p2,p3=s.symbols('q1 q2 q3 p1 p2 p3',real=True)
u=s.Matrix([q1,q2,q3,p1,p2,p3]);O3=omega(3)
F=s.Matrix([p3,q3*p2,p1]);point={q1:0,q2:0,q3:0,p1:0,p2:1,p3:0}
conorm=F.jacobian(u).subs(point)
P=s.Matrix(3,3,lambda i,j:bracket(F[i],F[j],u)).subs(point)
E=s.Matrix.hstack(*conorm.nullspace())
assert conorm.rank()==3 and P.rank()==2
assert bracket(F[0],F[1],u)==p2 and (E.T*O3*E).rank()==2
assert E.rank()-(E.T*O3*E).rank()==1
checks.append({'name':'both induction reductions in the mixed submanifold',
 'constraint_rank':3,'defining_bracket_rank':2,'restricted_rank':2,'radical_dimension':1,'passed':True})

ff=p2;gg=(1+q2*q2)*p3;X=H(ff,u);Y=H(gg,u)
comm=s.simplify(Y.jacobian(u)*X-X.jacobian(u)*Y)
assert comm==H(bracket(ff,gg,u),u)
onV={p2:0,p3:0};assert comm.subs(onV)==s.Matrix([0,0,2*q2,0,0,0])
assert bracket(ff,gg,u).subs(onV)==0
checks.append({'name':'noncommuting characteristic defining fields',
 'bracket':'2 q2 p3','commutator_on_V':'2 q2 d/dq3','bracket_vanishes_on_V':True,'passed':True})

X1,S1,S2=s.symbols('X1 S1 S2',real=True)
embedding=s.Matrix([X1,0,S1,S2]);Jv=embedding.jacobian([X1,S1,S2])
sigma=Jv.T*O*Jv;radial=s.Matrix([0,S1,S2]);lam=-sigma*radial
assert sigma.rank()==2 and sigma.nullspace()==[s.Matrix([0,0,1])]
assert lam==s.Matrix([S1,0,0]) and sigma*radial==s.Matrix([-S1,0,0])
vf=H(x2*xi2).subs(dict(zip(coords,embedding)),simultaneous=True)
assert vf==s.Matrix([0,0,0,-S2])
assert embedding.subs({S1:t*S1,S2:t*S2},simultaneous=True)==s.diag(1,1,t,t)*embedding
checks.append({'name':'one characteristic foliation with both radial behaviors',
 'restricted_rank':2,'characteristic_tangent':'d/dxi2','one_form':'xi1 dx1',
 'radial_tangent_if_and_only_if':'xi1=0','defining_Hamilton_field_on_V':'-xi2 d/dxi2','passed':True})

# Build an actual finite circle translation and complex averaging/lifting
# matrix. Its norm is checked independently of the FIO order calculation.
h=np.array([1.,-2.,.5]);ell=np.array([1.+2.j,-.5j,3.])
size=12;translation=np.roll(np.eye(size),3,axis=0)
A=np.kron(np.outer(h,ell),translation)
actual=np.linalg.norm(A,2);predicted=np.linalg.norm(h)*np.linalg.norm(ell)
test=np.kron(np.conj(ell)/np.linalg.norm(ell),np.eye(size)[:,2])
assert abs(np.linalg.norm(test)-1)<2e-15
assert abs(actual-predicted)<2e-13 and abs(np.linalg.norm(A@test)-predicted)<2e-13
assert s.Rational(0)-s.Rational(2,4)==-s.Rational(1,2)
checks.append({'name':'translated quotient graph gives the exact tensor norm',
 'actual_matrix_norm':float(actual),'predicted_norm':float(predicted),
 'equality_test_norm':float(np.linalg.norm(A@test)),'critical_FIO_order':'-1/2','passed':True})

report={'schema':'submanifold-finite-check/v1','passed':True,
 'lesson':'homogeneous-submanifold-normal-forms.md',
 'lesson_sha256':sha(here/'homogeneous-submanifold-normal-forms.md'),
 'script_sha256':sha(Path(__file__)),'checks':checks,
 'scope':'Six bounded exact linear/coordinate models and an independently assembled finite translation/averaging operator. They test dimensions, signs, example geometry and norms; they do not certify the general submanifold theorem or FIO sharpness proof.',
 'independent_mathematical_review':False}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_checks':len(checks),'lesson_sha256':report['lesson_sha256']}))
