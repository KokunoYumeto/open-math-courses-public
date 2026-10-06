"""Six bounded algebraic/flow models for U022, not certification of general smooth germs."""
from pathlib import Path
import hashlib,json
import sympy as s
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

# Independent dual-correction models with nonzero skew matrices.
dual=[]
for A in [s.Matrix([[0,3],[-3,0]]),s.Matrix([[0,2,-1],[-2,0,5],[1,-5,0]])]:
    d=A.rows;O=s.zeros(d).row_join(s.eye(d)).col_join(-s.eye(d).row_join(s.zeros(d)))
    K=s.eye(2*d)[:,:d];L=s.eye(2*d)[:,d:]+K*(-A/2)
    # Columns store vectors: (1.3) adds K*A/2, since A is skew.
    # This initial choice has L.T*O*L=A.
    assert s.simplify(L.T*O*L)==A
    corrected=L+K*(A/2)
    assert corrected.T*O*corrected==s.zeros(d)
    assert K.T*O*corrected==s.eye(d)
    wrong=L-K*(A/2)
    assert wrong.T*O*wrong==2*A
    dual.append({'dimension':2*d,'initial_skew_matrix':str(A),'corrected_pairings_zero':True,'wrong_sign_doubles':True})
checks.append({'name':'alternating dual correction and opposite sign','passed':True,'models':dual,
 'scope':'Explicit canonical dual vectors with nonzero initial pairings; general radical/complement argument remains in the proof.'})

x1,x2,e1,e2=s.symbols('x1 x2 e1 e2',real=True);z=s.Matrix([x1,x2,e1,e2])
target=s.Matrix([x1,x2,e1+x2**2,e2+2*x1*x2])
O=s.zeros(2).row_join(-s.eye(2)).col_join(s.eye(2).row_join(s.zeros(2)))
J=target.jacobian(z);assert s.simplify(J.T*O*J)==O
primitive=s.Matrix([[target[2],target[3]]])*target[:2,0].jacobian(z)
old=s.Matrix([[e1,e2]])*s.Matrix([x1,x2]).jacobian(z)
assert primitive-old==s.Matrix([[s.diff(x1*x2**2,a) for a in z]])
checks.append({'name':'ordinary nonlinear canonical completion','passed':True,
 'exact_primitive_difference':'d(x1*x2^2)','scope':'Full two-dimensional nonlinear map, including all brackets.'})

tau1,tau2,z1,z2,ell,w,b=s.symbols('tau1 tau2 z1 z2 ell w b',real=True)
vars=s.Matrix([tau1,tau2,z1,z2,ell,w])
R=lambda f:s.diff(f,ell)+tau1*s.diff(f,tau1)+tau2*s.diff(f,tau2)
q=z2+w*w;p=-tau1+s.exp(ell)*(b+w*w)
assert R(q)==0 and s.simplify(R(p)-p)==0
assert s.diff(q,tau1)==s.diff(q,tau2)==0 and s.diff(q,z2)==1
assert s.diff(p,tau1)==-1 and s.diff(p,z1)==s.diff(p,z2)==0
for f in [tau1**2*ell+w*z1,s.exp(ell)*tau1+z2*w]:
    assert s.simplify(R(s.diff(f,tau1))-s.diff(R(f),tau1)+s.diff(f,tau1))==0
    assert s.simplify(R(s.diff(f,z1))-s.diff(R(f),z1))==0
checks.append({'name':'semidirect flow signs and full Euler equations','passed':True,
 'radial_chart':'d/dell+tau1*d/dtau1+tau2*d/dtau2',
 'position':'z2+w^2','momentum':'-tau1+exp(ell)*(b+w^2)','scope':'Exact nonconstant section data, both Hamilton commutators and all stated field equations.'})

pj=s.symbols('p',positive=True);xx=s.symbols('x',real=True);hh=(pj-2)**2
F=s.integrate(hh/pj,pj)-s.integrate(hh/pj,pj).subs(pj,2);qj=xx-F
assert s.simplify(pj*s.diff(qj,pj)+hh*s.diff(qj,xx))==0
assert qj.subs(pj,2)==xx and s.diff(qj,pj).subs(pj,2)==0
assert s.diff(qj,xx)==1
checks.append({'name':'exceptional nonzero-momentum position correction','passed':True,
 'b_J':2,'h':'(p-2)^2','exact_correction':str(F),
 'scope':'Nonzero variable h, including logarithmic integral, marked differential and exact Euler equation.'})

rotations=[]
for n,k in [(1,1),(2,1),(2,2),(3,2),(4,4)]:
    q=s.symbols('q1:'+str(n+1));p=s.symbols('p1:'+str(n+1));zz=s.Matrix([*q,*p])
    Q=s.Matrix([q[0]+sum(q[j]*p[j]/p[0] for j in range(1,k)),*(p[j]/p[0] for j in range(1,k)),*q[k:]])
    P=s.Matrix([p[0],*(-q[j]*p[0] for j in range(1,k)),*p[k:]])
    O=s.zeros(n).row_join(-s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
    assert s.simplify(s.Matrix([*Q,*P]).jacobian(zz).T*O*s.Matrix([*Q,*P]).jacobian(zz))==O
    assert s.simplify(P.T*Q.jacobian(zz)-s.Matrix([[*p]])*s.Matrix(q).jacobian(zz))==s.zeros(1,2*n)
    inv_q=s.Matrix([Q[0]+sum(P[j]*Q[j]/P[0] for j in range(1,k)),*(-P[j]/P[0] for j in range(1,k)),*Q[k:]])
    inv_p=s.Matrix([P[0],*(Q[j]*P[0] for j in range(1,k)),*P[k:]])
    assert s.simplify(inv_q-s.Matrix(q))==s.zeros(n,1)
    assert s.simplify(inv_p-s.Matrix(p))==s.zeros(n,1)
    Rv=s.Matrix([*([0]*n),*p])
    assert s.simplify(Q.jacobian(zz)*Rv)==s.zeros(n,1)
    assert s.simplify(P.jacobian(zz)*Rv)==P
    aux={q[0]:0,**{p[j]:0 for j in range(1,k)},**{q[j]:0 for j in range(k,n)},**{p[j]:0 for j in range(k,n)}}
    assert Q.subs(aux,simultaneous=True)==s.zeros(n,1)
    assert all(P[j].subs(aux)==0 for j in range(k,n))
    rotations.append({'n':n,'k':k,'primitive_and_form_preserved':True,'inverse_verified':True,'degrees':[0,1],'auxiliary_model_sent_to_fiber':True})
checks.append({'name':'homogeneous primitive-preserving rotation including empty sums','passed':True,'models':rotations,
 'scope':'Five exact dimensions/index counts, all covectors/base coordinates, and the full inverse.'})

r=s.symbols('r',real=True);rho=s.symbols('rho',positive=True)
base=s.Matrix([r*r,-s.Rational(2,3)*r**3-r**4/2]);cov=s.Matrix([(r+r*r)*rho,rho])
assert s.simplify((cov.T*base.diff(r))[0])==0
assert s.simplify((base[1]+base[0]**2/2)**2-s.Rational(4,9)*base[0]**3)==0
JJ=s.Matrix([*base,*cov]).jacobian([r,rho])
assert JJ.subs(r,0).rank()==2 and base.jacobian([r,rho]).subs(r,0).rank()==0
for rr in [s.Rational(-1,5),s.Rational(1,5)]:
    assert base.jacobian([r,rho]).subs(r,rr).rank()==1
    assert JJ.subs(r,rr).rank()==2
assert s.Matrix([r+r*r,r*r]).diff(r).subs(r,0)==s.Matrix([1,0])
checks.append({'name':'deformed cusp primitive, projection ranks and covector immersion','passed':True,
 'base_ranks':[1,0,1],'full_rank':2,'lower_tangent_at_zero':[1,0],
 'scope':'Full exact two-dimensional conic Lagrangian in the specified r range, not a global conormal claim.'})

name='prescribed-canonical-coordinates-and-isotropic-fibers.md'
report={'schema':'canonical-coordinates-finite-check/v1','passed':True,'lesson':name,
 'lesson_sha256':sha(here/name),'script_sha256':sha(Path(__file__)),
 'checks':checks,'independent_mathematical_review':False,
 'scope':'Six bounded exact alternating, nonlinear symplectic, semidirect-flow, marked-coordinate, homogeneous rotation and cusp models. General smooth existence, isotropic induction and germ recognition are proved in the lesson, not certified by models.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_checks':len(checks),'lesson_sha256':report['lesson_sha256']}))
