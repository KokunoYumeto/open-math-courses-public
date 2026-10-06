"""Bounded full-relation and phase checks for U018; general theorem proofs are analytic."""
import hashlib,json
from pathlib import Path
import sympy as S
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def eq(A,B):assert all(S.simplify(e)==0 for e in A-B)
def dform(lam,u):return S.Matrix(len(u),len(u),lambda i,j:S.diff(lam[j],u[i])-S.diff(lam[i],u[j]))
def record(name,evidence):checks.append({'name':name,'passed':True,'bounded_evidence':evidence})
models=[]
for n in [2,3,4]:
    xs=S.symbols('x1:'+str(n+1));ps=S.symbols('z2:'+str(n+1));s=S.symbols('s');rho=ps[-1]
    u=S.Matrix(list(xs)+[s]+list(ps))
    X=S.Matrix(list(xs)+[s*s*rho]+list(ps))
    Y=S.Matrix([xs[0]+s]+list(xs[1:-1])+[xs[-1]-s**3/3]+[s*s*rho]+list(ps))
    JX=X.jacobian(u);JY=Y.jacobian(u)
    assert S.simplify(JX.det()-2*s*rho)==S.simplify(JY.det()-2*s*rho)==0
    lX=JX[:n,:].T*S.Matrix(X[n:]);lY=JY[:n,:].T*S.Matrix(Y[n:]);eq(lX,lY)
    B=dform(lX,u);B0=B.subs(s,0);assert B0.rank()==2*n-2
    tang=[j for j in range(2*n) if j!=n];assert B0.extract(tang,tang).rank()==2*n-2
    kX=JX.subs(s,0).nullspace()[0];kY=JY.subs(s,0).nullspace()[0]
    assert S.Matrix.hstack(kX,kY).rank()==2
    R=S.Matrix([0]*(n+1)+list(ps));at={x:0 for x in xs};at[s]=0;at.update({p:0 for p in ps});at[rho]=1
    assert S.Matrix.hstack(kX,kY,R).subs(at).rank()==3
    assert S.simplify(B.det()-(2*s*rho)**2)==0
    models.append((n,xs,ps,s,rho,u,X,Y,lX,B))
record('full homogeneous relations in n=2,3,4',
 'Both complete projection Jacobians, equal full canonical one-forms, ambient/restricted ranks, distinct kernel lines and nonzero marked radial independence; simple fold determinant factors retained.')
for n in [1,2,3]:
    ts=S.symbols('t1:'+str(n+1));pp=S.symbols('p2:'+str(n+1));v=S.symbols('v')
    u=S.Matrix(list(ts)+[v]+list(pp));Y=S.Matrix(list(ts)+[v*v/2]+list(pp))
    X=S.Matrix([ts[0]+v/2]+list(ts[1:])+[v*v/2]+list(pp))
    JX=X.jacobian(u);JY=Y.jacobian(u)
    assert S.simplify(JX.det()-v)==S.simplify(JY.det()-v)==0
    lX=JX[:n,:].T*S.Matrix(X[n:]);lY=JY[:n,:].T*S.Matrix(Y[n:])
    primitive=v**3/12;eq(lX-lY,S.Matrix([S.diff(primitive,w) for w in u]))
    dx=X[0]-Y[0];assert S.simplify(2*dx*dx-X[n])==0
record('ordinary coefficients, full projections and signed one-form',
 'n=1,2,3: both complete determinants and signed primitive v^3/12=2(x1-y1)^3/3, with exact factor two in the relation.')
for n,xs,ps,s,rho,u,X,Y,lX,B in models:
    ys=S.symbols('y1:'+str(n+1));xi=S.symbols('xi1:'+str(n+1));tau=S.symbols('tau')
    rh=xi[-1];phase=sum((xs[j]-ys[j])*xi[j] for j in range(n))+tau*xi[0]/rh-tau**3/(3*rh**2)
    theta=S.Matrix(list(xi)+[tau]);critical=S.Matrix([S.diff(phase,t) for t in theta])
    on={ys[j]:Y[j] for j in range(n)};on.update({xi[j]:X[n+j] for j in range(n)});on[tau]=s*rho
    eq(critical.subs(on,simultaneous=True),S.zeros(n+1,1))
    assert S.simplify(phase.subs(on,simultaneous=True))==0
    eq(S.Matrix([S.diff(phase,x) for x in xs]).subs(on,simultaneous=True),S.Matrix(X[n:]))
    eq(S.Matrix([-S.diff(phase,y) for y in ys]).subs(on,simultaneous=True),S.Matrix(Y[n:]))
    assert S.simplify(sum(t*S.diff(phase,t) for t in theta)-phase)==0
    allvars=S.Matrix(list(xs)+list(ys)+list(theta));jc=critical.jacobian(allvars)
    at={x:0 for x in xs};at.update({y:0 for y in ys});at.update({t:0 for t in theta});at[rh]=1
    assert jc.subs(at).rank()==n+1
record('actual homogeneous phase, critical equations and covector signs',
 'Full conic phase in n+1 auxiliary variables: exact critical substitution, Euler degree-one identity, zero critical value, output/input covectors and independent marked critical gradients in n=2,3,4.')
n,xs,ps,s,rho,u,X,Y,lX,B=models[0]
h=s*S.sqrt(2*rho)
srcX=S.Matrix(list(xs)+[h]+list(ps))
srcY=S.Matrix(list(Y[:n])+[h]+list(ps))
assert S.simplify(srcX.jacobian(u).det()-S.sqrt(2*rho))==0
assert S.simplify(srcY.jacobian(u).det()-S.sqrt(2*rho))==0
F=S.Matrix(list(xs)+[-s]+list(ps))
G=S.Matrix([xs[0]+2*s,xs[-1]-2*s**3/3,-s,rho])
eq(X.subs(dict(zip(u,F)),simultaneous=True),X)
eq(Y.subs(dict(zip(u,G)),simultaneous=True),Y)
eq(G.subs(dict(zip(u,G)),simultaneous=True),u)
expected=srcY.jacobian(u)[:n,:].T*S.Matrix([h*h/2,rho])
eq(expected,lX)
assert S.Rational(3,4)**2==S.Rational(9,16)
assert -(S.Rational(3,4)**3)/3==-S.Rational(9,64)
record('full source charts for both converses and sheet exchanges',
 'Exact half-degree normal, both full source Jacobians, invariant projection maps and squared input exchange; complete one-form cancellation and exact marked sheet coordinates.')
# Full nonlinear target cotangent changes, independently differentiated.
x1,x2,p1,p2,y1,y2,e1,e2,a,b=S.symbols('x1 x2 p1 p2 y1 y2 e1 e2 a b')
tx=S.Matrix([x1,x2,p1,p2]);ty=S.Matrix([y1,y2,e1,e2])
KX=S.Matrix([x1+a*x2*x2/2,x2,p1,p2-a*x2*p1])
KY=S.Matrix([y1+b*y2*y2/2,y2,e1,e2-b*y2*e1])
lamX=S.Matrix([p1,p2,0,0]);lamY=S.Matrix([e1,e2,0,0])
eq(KX.jacobian(tx).T*lamX.subs(dict(zip(tx,KX)),simultaneous=True),lamX)
eq(KY.jacobian(ty).T*lamY.subs(dict(zip(ty,KY)),simultaneous=True),lamY)
XX=KX.subs(dict(zip(tx,X)),simultaneous=True);YY=KY.subs(dict(zip(ty,Y)),simultaneous=True)
eq(XX.jacobian(u)[:2,:].T*S.Matrix(XX[2:]),YY.jacobian(u)[:2,:].T*S.Matrix(YY[2:]))
assert S.simplify(XX.jacobian(u).det()-2*s*rho)==0
assert S.simplify(YY.jacobian(u).det()-2*s*rho)==0
KXi=S.Matrix([x1-a*x2*x2/2,x2,p1,p2+a*x2*p1])
KYi=S.Matrix([y1-b*y2*y2/2,y2,e1,e2+b*y2*e1])
eq(KXi.subs(dict(zip(tx,XX)),simultaneous=True),X)
eq(KYi.subs(dict(zip(ty,YY)),simultaneous=True),Y)
record('complete nonlinear canonical target changes',
 'Nonlinear cotangent lifts on both targets preserve entire one-forms and both fold determinants; exact inverse changes recover the full relation, including mixed last-frequency terms.')
q,z,v,r=S.symbols('q z v r');uc=S.Matrix([q,z,v,r])
J=2*(2+v)/S.sqrt(1+v)-4
assert S.simplify(S.diff(J,v)-v/(1+v)**S.Rational(3,2))==0
XC=S.Matrix([-v*v/2,z,q,r]);YC=S.Matrix([-J,z,q*(1+v)**S.Rational(3,2),r])
lcX=XC.jacobian(uc)[:2,:].T*S.Matrix(XC[2:])
lcY=YC.jacobian(uc)[:2,:].T*S.Matrix(YC[2:]);eq(lcX,lcY)
assert S.simplify(XC.jacobian(uc).det()-v)==0
assert S.simplify(YC.jacobian(uc).det()-v)==0
at={q:1,z:0,v:0,r:0};assert S.Matrix.vstack(XC.jacobian(uc),YC.jacobian(uc)).subs(at).rank()==4
kx=XC.jacobian(uc).subs(at).nullspace()[0];ky=YC.jacobian(uc).subs(at).nullspace()[0]
Rc=S.Matrix([q,0,0,r]);assert S.Matrix.hstack(kx,ky,Rc.subs(at)).rank()==2
eq(lcX.subs(at),S.zeros(4,1))
badY=S.Matrix([xs[0]+s,xs[-1],s*s*rho,rho])
badlam=badY.jacobian(u)[:2,:].T*S.Matrix(badY[2:])
difference=lX-badlam
eq(difference,S.Matrix([0,0,-s*s*rho,0]))
assert dform(difference,u)[2,3]==s*s
record('genuine excluded relation and missing-cubic-displacement defect',
 'Two actual homogeneous cotangent projections fold with distinct kernels and product rank four, yet common pulled-back primitive is zero at the marked point. Omitting the cubic last position creates exact nonzero signed one-/two-form defects.')
lesson=here/'canonical-relations-with-two-folds.md'
report={'schema':'bounded-canonical-fold-check/v1','checks':checks,'passed':all(x['passed'] for x in checks),
 'lesson':lesson.name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'guard':'Bounded full relations/phases do not independently certify the arbitrary-relation reduction and full target extension proofs.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':report['passed'],'checks':len(checks)}))

