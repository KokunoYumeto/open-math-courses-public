"""Six exact, bounded U023 models; the general smooth induction is proved in prose."""
import hashlib,json
from pathlib import Path
import sympy as s
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def form(n):return s.zeros(n).row_join(-s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
def planes(n,k):
    eye=s.eye(2*n)
    A=eye[:,n:]
    B=eye[:,n:n+k].row_join(eye[:,k:n])
    return A,B

dimensions=[]
for n,k in [(1,1),(2,1),(2,2),(3,1),(3,2),(4,3),(4,4)]:
    A,B=planes(n,k);I=s.eye(2*n)[:,n:n+k]
    assert A.rank()==B.rank()==n and I.rank()==k
    assert 2*n-A.row_join(B).rank()==k
    assert A.T*form(n)*A==B.T*form(n)*B==s.zeros(n)
    radial=s.eye(2*n)[:,n]
    assert I.row_join(radial).rank()==k
    As=A[:,1:];Bs=B[:,1:];Is=I[:,1:]
    assert As.rank()==Bs.rank()==n-1 and Is.rank()==k-1
    assert 2*(n-1)-As.row_join(Bs).rank()==k-1
    assert (2*n-1)-As.row_join(Bs).rank()==k
    annihilator=A.row_join(B).T.nullspace()
    Hamilton=s.Matrix.hstack(*[-form(n)*v for v in annihilator])
    assert Hamilton.rank()==k and I.row_join(Hamilton).rank()==k
    dimensions.append({'n':n,'k':k,'slice_dimensions':[2*n-1,n-1,n-1,k-1],'common_normals':k})
checks.append({'name':'full clean planes, radial slice and common Hamilton dimensions','passed':True,'models':dimensions,
 'scope':'Exact model tangent spaces and the annihilator-to-Hamilton identification; arbitrary clean charts remain in Lemma 1.1.'})

def check_models(n,k,q,p,Q,P,iq,ip,y,z):
    sourceA={**{q[j]:0 for j in range(n-1)},p[-1]:0}
    sourceB={**{q[j]:0 for j in range(k-1)},**{p[j]:0 for j in range(k-1,n)}}
    assert all(v.subs(sourceA,simultaneous=True)==0 for v in Q)
    assert all(Q[j].subs(sourceB,simultaneous=True)==0 for j in range(k))
    assert all(P[j].subs(sourceB,simultaneous=True)==0 for j in range(k,n))
    targetA={a:0 for a in y}
    targetB={**{y[j]:0 for j in range(k)},**{z[j]:0 for j in range(k,n)}}
    assert all(iq[j].subs(targetA,simultaneous=True)==0 for j in range(n-1))
    assert ip[-1].subs(targetA,simultaneous=True)==0
    assert all(iq[j].subs(targetB,simultaneous=True)==0 for j in range(k-1))
    assert all(ip[j].subs(targetB,simultaneous=True)==0 for j in range(k-1,n))

homogeneous=[]
for n,k in [(2,2),(3,2),(3,3),(4,2),(4,3),(4,4),(5,3)]:
    q=s.symbols('q1:'+str(n+1));p=s.symbols('p1:'+str(n+1));x=s.Matrix([*q,*p])
    preQ=list(q);preP=list(p)
    preQ[0]=q[0]+q[-1]*p[-1]/p[0];preQ[-1]=p[-1]/p[0]
    preP[-1]=-q[-1]*p[0]
    permutation=[*range(k-1),n-1,*range(k-1,n-1)]
    assert len(set(permutation))==n
    Q=s.Matrix([preQ[j] for j in permutation]);P=s.Matrix([preP[j] for j in permutation])
    mapping=s.Matrix([*Q,*P]);J=mapping.jacobian(x)
    assert s.simplify(J.T*form(n)*J)==form(n)
    assert s.simplify(P.T*Q.jacobian(x)-s.Matrix([p])*s.Matrix(q).jacobian(x))==s.zeros(1,2*n)
    R=s.Matrix([*([0]*n),*p])
    assert s.simplify(Q.jacobian(x)*R)==s.zeros(n,1)
    assert s.simplify(P.jacobian(x)*R)==P
    y=s.symbols('Q1:'+str(n+1));z=s.symbols('P1:'+str(n+1));prey=[None]*n;prez=[None]*n
    for index,old in enumerate(permutation):prey[old]=y[index];prez[old]=z[index]
    iq=list(prey);ip=list(prez)
    iq[0]=prey[0]+prez[-1]*prey[-1]/prez[0];iq[-1]=-prez[-1]/prez[0]
    ip[-1]=prey[-1]*prez[0]
    iq=s.Matrix(iq);ip=s.Matrix(ip);inverse=s.Matrix([*iq,*ip])
    forward_sub={**dict(zip(q,iq)),**dict(zip(p,ip))}
    reverse_sub={**dict(zip(y,Q)),**dict(zip(z,P))}
    assert s.simplify(mapping.subs(forward_sub,simultaneous=True)-s.Matrix([*y,*z]))==s.zeros(2*n,1)
    assert s.simplify(inverse.subs(reverse_sub,simultaneous=True)-x)==s.zeros(2*n,1)
    check_models(n,k,q,p,Q,P,iq,ip,y,z)
    marked={**{a:0 for a in q},**{a:0 for a in p},p[0]:1}
    assert mapping.subs(marked)==s.Matrix([*([0]*n),1,*([0]*(n-1))])
    homogeneous.append({'n':n,'k':k,'paired_permutation':[j+1 for j in permutation],
      'both_full_model_images_and_reverse_containments':True,'primitive_form_degrees_inverse_marked_point':True})
checks.append({'name':'full simultaneous homogeneous rotation and paired permutation','passed':True,'models':homogeneous,
 'scope':'All coordinates, rational identities, both model directions and two-sided inverses in seven dimensions/index counts; positive first momentum is the denominator domain.'})

ordinary=[]
for n,k in [(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,3)]:
    q=s.symbols('q1:'+str(n+1));p=s.symbols('p1:'+str(n+1));x=s.Matrix([*q,*p])
    preQ=list(q);preP=list(p);preQ[-1]=p[-1];preP[-1]=-q[-1]
    permutation=[*range(k-1),n-1,*range(k-1,n-1)]
    Q=s.Matrix([preQ[j] for j in permutation]);P=s.Matrix([preP[j] for j in permutation])
    mapping=s.Matrix([*Q,*P]);J=mapping.jacobian(x)
    assert J.T*form(n)*J==form(n)
    delta=P.T*Q.jacobian(x)-s.Matrix([p])*s.Matrix(q).jacobian(x)
    assert delta==s.Matrix([[s.diff(-q[-1]*p[-1],a) for a in x]])
    y=s.symbols('Q1:'+str(n+1));z=s.symbols('P1:'+str(n+1));prey=[None]*n;prez=[None]*n
    for index,old in enumerate(permutation):prey[old]=y[index];prez[old]=z[index]
    iq=list(prey);ip=list(prez);iq[-1]=-prez[-1];ip[-1]=prey[-1]
    iq=s.Matrix(iq);ip=s.Matrix(ip)
    assert s.Matrix([*iq,*ip]).subs({**dict(zip(y,Q)),**dict(zip(z,P))},simultaneous=True)==x
    assert mapping.subs({**dict(zip(q,iq)),**dict(zip(p,ip))},simultaneous=True)==s.Matrix([*y,*z])
    check_models(n,k,q,p,Q,P,iq,ip,y,z)
    ordinary.append({'n':n,'k':k,'exact_primitive_correction':'-d(q_n*p_n)','both_model_images':True})
q1,q2,p1,p2=s.symbols('q1 q2 p1 p2');xx=s.Matrix([q1,q2,p1,p2]);F=q1*q2**2+q1**3
Q=s.Matrix([q1,q2]);P=s.Matrix([p1-s.diff(F,q1),p2-s.diff(F,q2)])
J=s.Matrix([*Q,*P]).jacobian(xx);assert J.T*form(2)*J==form(2)
assert P.T*Q.jacobian(xx)-s.Matrix([[p1,p2]])*Q.jacobian(xx)==s.Matrix([[s.diff(-F,a) for a in xx]])
assert P.subs({p1:s.diff(F,q1),p2:s.diff(F,q2)},simultaneous=True)==s.zeros(2,1)
assert P.subs({q1:0,q2:0},simultaneous=True)==s.Matrix([p1,p2])
checks.append({'name':'ordinary cylinder exchanges and nonconstant exact graph translation','passed':True,'models':ordinary,
 'graph_translation':'F=q1*q2^2+q1^3','scope':'Seven full ordinary pair changes, plus the nonlinear k=0 graph example; smooth closed-form exactness is proved by (5.1).'})

transversals=[]
for n in range(1,6):
    for k in range(n+1):
        A,B=planes(n,k);L=s.eye(n).col_join(s.diag(*([0]*k+[1]*(n-k))))
        assert L.rank()==n and L.T*form(n)*L==s.zeros(n)
        assert A.row_join(L).rank()==B.row_join(L).rank()==2*n
        transversals.append({'n':n,'k':k,'Lagrangian':True,'transverse_to_both':True})
checks.append({'name':'common transverse planes with both empty-block endpoints','passed':True,'models':transversals,
 'scope':'Twenty exact linear models, including k=0 and k=n; no global bundle field asserted.'})

x1,x2,x3,e1,e2,e3=s.symbols('x1 x2 x3 e1 e2 e3');xx=s.Matrix([x1,x2,x3,e1,e2,e3])
Q=s.Matrix([x1-x2**2-x3**3,x2,x3]);P=s.Matrix([e1,e2+2*x2*e1,e3+3*x3**2*e1])
mapping=s.Matrix([*Q,*P]);J=mapping.jacobian(xx)
assert J.T*form(3)*J==form(3)
assert P.T*Q.jacobian(xx)==s.Matrix([[e1,e2,e3]])*s.Matrix([x1,x2,x3]).jacobian(xx)
u,v=s.symbols('u v',real=True);rho=s.symbols('rho',positive=True)
conormal=s.Matrix([u*u+v**3,u,v,rho,-2*u*rho,-3*v*v*rho])
image=mapping.subs(dict(zip(xx,conormal)),simultaneous=True)
assert image==s.Matrix([0,u,v,rho,0,0])
tangent=conormal.jacobian(s.Matrix([u,v,rho])).subs({u:0,v:0})
A=s.eye(6)[:,3:];assert tangent.rank()==3 and 6-A.row_join(tangent).rank()==1
assert tangent[:,2]==s.eye(6)[:,3]
marked={x1:0,x2:0,x3:0,e1:1,e2:0,e3:0};assert mapping.subs(marked)==s.Matrix([0,0,0,1,0,0])
y1,y2,y3,z1,z2,z3=s.symbols('Q1 Q2 Q3 P1 P2 P3')
inverse=s.Matrix([y1+y2*y2+y3**3,y2,y3,z1,z2-2*y2*z1,z3-3*y3*y3*z1])
assert inverse.subs(dict(zip([y1,y2,y3,z1,z2,z3],mapping)),simultaneous=True)==xx
for alpha in [-7,s.Rational(3,2)]:
    scaledQ=s.Matrix([alpha*Q[0],Q[1],Q[2]])
    scaledP=s.Matrix([P[0]/alpha,P[1],P[2]])
    assert scaledP.T*scaledQ.jacobian(xx)==s.Matrix([[e1,e2,e3]])*s.Matrix([x1,x2,x3]).jacobian(xx)
    signed_marked={x1:0,x2:0,x3:0,e1:alpha,e2:0,e3:0}
    assert s.Matrix([*scaledQ,*scaledP]).subs(signed_marked)==s.Matrix([0,0,0,1,0,0])
checks.append({'name':'curved hypersurface conormal and full cotangent lift','passed':True,
 'exact_equation':'x1=x2^2+x3^3','clean_intersection_dimension':1,
 'additional_marked_normalization_coefficients':['-7','3/2'],
 'scope':'Full six-coordinate symplectic map, primitive, inverse, marked covector, conormal image and tangent intersection at every positive marked ray coefficient.'})

q=s.symbols('q');a=s.Matrix([q,0]);b=s.Matrix([q,q*q])
assert s.solve(q*q,q)==[0]
ta=a.diff(q).subs(q,0);tb=b.diff(q).subs(q,0)
assert ta==tb==s.Matrix([1,0])
assert ta.row_join(tb).rank()==1
checks.append({'name':'nonclean smooth set-theoretic intersection','passed':True,
 'actual_intersection_dimension':0,'tangent_intersection_dimension':1,
 'scope':'Exact curves p=0 and p=q^2; the diffeomorphism obstruction follows from the written invariant dimension argument.'})

assert len(checks)==6 and all(r['passed'] for r in checks)
lesson=here/'clean-lagrangian-pairs-and-common-transversals.md'
report={'schema':'clean-lagrangian-pair-bounded-check/v1','passed':True,'checks':checks,
 'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'general_smooth_proof_independently_certified':False,'whole_source_parent_closed':False}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'passed':True,'lesson_sha256':report['lesson_sha256']}))
