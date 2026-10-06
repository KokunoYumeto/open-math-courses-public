"""Bounded full-map checks for U017; general normal-form proofs are analytic."""
import hashlib,json,itertools
from pathlib import Path
import sympy as S
import mpmath as mp
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def eq(A,B):assert all(S.simplify(e)==0 for e in A-B)
def dform(lam,u):
    return S.Matrix(len(u),len(u),lambda i,j:S.diff(lam[j],u[i])-S.diff(lam[i],u[j]))
def pull(F,lam,u):return F.jacobian(u).T*lam.subs(dict(zip(u,F)),simultaneous=True)
def pull2(F,B,u):return F.jacobian(u).T*B.subs(dict(zip(u,F)),simultaneous=True)*F.jacobian(u)
def record(name,evidence):checks.append({'name':name,'passed':True,'bounded_evidence':evidence})
for n in [2,3,4]:
    xs=S.symbols('x1:'+str(n+1));ps=S.symbols('p1:'+str(n+1));u=S.Matrix(xs+ps)
    rho=ps[-1];t=ps[0]/rho
    lam=S.Matrix([ps[0]**2/rho]+list(ps[1:])+[0]*n);B=dform(lam,u)
    F=S.Matrix(list(xs)+[-ps[0]]+list(ps[1:]))
    G=S.Matrix([xs[0]+2*t]+list(xs[1:-1])+[xs[-1]-2*t**3/3]+[-ps[0]]+list(ps[1:]))
    eq(pull(F,lam,u),lam);eq(pull(G,lam,u),lam)
    eq(G.subs(dict(zip(u,G)),simultaneous=True),u)
    eq(F.subs(dict(zip(u,F)),simultaneous=True),u)
    at={x:0 for x in xs};at.update({p:0 for p in ps});at[rho]=1
    Bc=B.subs(at);assert Bc.rank()==2*n-2
    tang=[j for j in range(2*n) if j!=n];assert Bc.extract(tang,tang).rank()==2*n-2
    dg=G.jacobian(u).subs(at);df=F.jacobian(u).subs(at)
    lf=(df+S.eye(2*n)).nullspace()[0];lg=(dg+S.eye(2*n)).nullspace()[0]
    rad=S.Matrix([0]*n+list(ps)).subs(at);assert S.Matrix.hstack(lf,lg,rad).rank()==3
    assert S.simplify(B.det()-(2*ps[0]/rho)**2)==0
record('full homogeneous involution models in three dimensions',
       'n=2,3,4: exact one-/two-form pullbacks, squared maps, ambient/restricted ranks, simple determinant factor and three independent reflection/radial directions.')
x,z,s,rho,a,b,t=S.symbols('x z s rho a b t',real=True)
u=S.Matrix([x,z,s,rho]);lam=S.Matrix([s*s/2,rho,0,0]);B=dform(lam,u)
ham=lambda h:S.simplify(B.inv()*S.Matrix([S.diff(h,v) for v in u]))
ha=ham(s*s*(1+x*x)+rho)
eq(ha,S.Matrix([2*(1+x*x),1,-2*x*s,0]))
assert ham(x)[2]==-1/s
Y=S.simplify(s*ham(s));Z=S.simplify(s*ham(x));R=S.Matrix([0,0,s/2,rho])
bracket=lambda A,C:C.jacobian(u)*A-A.jacobian(u)*C
eq(Y,S.Matrix([1,0,0,0]));eq(Z,S.Matrix([0,0,-1,0]))
eq(bracket(Y,Z),S.zeros(4,1));eq(bracket(R,Z),-Z/2)
eq(bracket(R,Y),S.zeros(4,1))
normal=S.Matrix([x,z,s*S.sqrt(rho/2),rho])
target=S.Matrix([s*s/rho,rho,0,0])
eq(pull(normal,target,u),lam)
eq(normal.jacobian(u)*R,S.Matrix([0,0,normal[2],rho]))
record('smooth fields versus singular Hamiltonians and exact half-to-full degree change',
       'A nontrivial admissible Hamiltonian and singular position Hamiltonian are explicitly compared; Y,Z commutation/weights and full primitive change are exact.')
# Ordinary scalar map with genuinely nonlinear B.
v=S.Matrix([x,t]);Bn=t*(1+b*t*t);An=S.simplify(t/(Bn*S.diff(Bn,t)))
F=S.Matrix([x*An,Bn]);one=S.Matrix([t*t/2,0]);two=dform(one,v)
eq(pull2(F,two,v),two)
assert S.simplify(F.jacobian(v).det().subs(t,0))==1
eq(F.subs(t,-t),S.Matrix([F[0],-F[1]]))
Fneg=S.Matrix([4*x,-t/2]);Gneg=S.Matrix([x-8*t,-t])
G0=S.Matrix([x+t,-t])
eq(pull2(Fneg,two,v),two)
eq(Gneg.subs(dict(zip(v,Fneg)),simultaneous=True),
   Fneg.subs(dict(zip(v,G0)),simultaneous=True))
record('full nonlinear and negative-sign ordinary scalar normalization',
       'Full rational pullback for B=t(1+bt^2), parity/Jacobian, and independent exact conjugacy for G=-8t, B=-t/2, A=4.')
# Full homogeneous map, retaining all mixed last-frequency/position terms.
u=S.Matrix([x,z,s,rho]);tr=s/rho
rr=t*(1+b*t*t);U=rr*rr;ss=S.cancel(2*t/S.diff(U,t));tt=S.cancel(t*t-2*t*U/S.diff(U,t))
F=S.Matrix([x*ss.subs(t,tr),z+x*tt.subs(t,tr),rho*rr.subs(t,tr),rho])
lh=S.Matrix([s*s/rho,rho,0,0]);Bh=dform(lh,u)
eq(pull(F,lh,u),lh);eq(pull2(F,Bh,u),Bh)
Rh=S.Matrix([0,0,s,rho]);eq(F.jacobian(u)*Rh,S.Matrix([0,0,F[2],F[3]]))
assert S.simplify(F.jacobian(u).det().subs(s,0))==1
eq(F.subs(s,-s),S.Matrix([F[0],F[1],-F[2],F[3]]))
assert all(S.simplify(e)==0 for e in [U*ss+tt-t*t,U*S.diff(ss,t)+S.diff(tt,t),S.diff(U,t)*ss-2*t])
record('full nonlinear homogeneous normalization',
       'Polynomial odd R with simple zero gives rational smooth S,T. All mixed terms of the full one-/two-form pullbacks, coordinate weights, parity and marked Jacobian are checked.')
# Independently solve/differentiate the nonlinear integral example.
mp.mp.dps=85
def rfun(tv):
    if tv==0:return mp.mpf(0)
    return mp.findroot(lambda rv:rv*(1+mp.mpf(6)/5*rv*rv)**(mp.mpf(1)/3)-tv,tv)
samples=[]
for tv in map(mp.mpf,['-.3','-.1','.1','.3']):
    rv=rfun(tv);rp=mp.diff(rfun,tv);Sv=tv/(rv*rp);Tv=tv*tv-rv*rv*Sv
    Vv=2*rv+4*rv**3;Wv=-2*rv**3/3-12*rv**5/5
    residual1=Vv-2*tv*Sv;residual2=Wv-(-2*tv**3/3+2*tv*Tv)
    assert abs(residual1)<mp.mpf('1e-70') and abs(residual2)<mp.mpf('1e-70')
    assert abs(2*rv*rp*Sv-2*tv)<mp.mpf('1e-70')
    samples.append({'t':str(tv),'first_shift_residual':mp.nstr(abs(residual1),6),
                    'last_shift_residual':mp.nstr(abs(residual2),6)})
# Exact elimination check for the same last-shift relation.
rv,tv=S.symbols('rv tv');Vs=2*rv+4*rv**3;Ws=-2*rv**3/3-S.Rational(12,5)*rv**5
Ss=Vs/(2*tv);Ts=tv*tv-rv*rv*Ss
num=S.together(Ws+2*tv**3/3-2*tv*Ts)
constraint=tv**3-rv**3-S.Rational(6,5)*rv**5
assert S.simplify(num+S.Rational(4,3)*constraint)==0
record('actual nonlinear integral inverse and both conjugacy equations',
       {'example':'V=2b+4b^3, W=-2b^3/3-12b^5/5',
        'exact_constraint_elimination':True,'independently_differentiated_inverse_samples':samples,
        'guard':'Finite full-map examples; arbitrary smooth inverse is proved by the inverse function theorem in the lesson.'})
# Genuine excluded radial example and missing-cubic-shift defect.
q,zz,uu,pp=S.symbols('q zz uu pp');uc=S.Matrix([q,zz,uu,pp])
lc=S.Matrix([0,pp,-q*uu,0]);Bc=dform(S.Matrix([uu*uu/2,pp,0,0]),uc)
G=S.Matrix([q*(1+uu)**3,zz,-uu/(1+uu),pp])
eq(pull2(G,Bc,uc),Bc);eq(G.subs(dict(zip(uc,G)),simultaneous=True),uc)
Rc=S.Matrix([q,0,0,pp]);eq(Bc.T*Rc,lc)
weights=S.Matrix([1,0,0,1]);Euler=Bc.applyfunc(lambda e:sum(Rc[k]*S.diff(e,uc[k]) for k in range(4)))
eq(Euler+S.diag(*weights)*Bc+Bc*S.diag(*weights),Bc)
at={q:1,zz:0,uu:0,pp:0};assert Bc.subs(at).rank()==2
assert Bc.subs(at).extract([0,1,3],[0,1,3]).rank()==2
lf=S.Matrix([0,0,1,0]);lg=(G.jacobian(uc).subs(at)+S.eye(4)).nullspace()[0]
assert S.Matrix.hstack(lf,lg).rank()==2
assert S.Matrix.hstack(lf,lg,Rc.subs(at)).rank()==2
assert all(e==0 for e in lc.subs(at))
Gbad=S.Matrix([x+2*s/rho,z,-s,rho])
defect=S.simplify(pull2(Gbad,Bh,u)-Bh)
assert defect[2,3]==-2*s*s/rho**3
record('two genuine hypothesis/correction failures',
       'A degree-one folded form with distinct homogeneous preserving reflections has radial vector in their span and zero restricted primitive. Omitting the cubic last-position shift has a nonzero full two-form defect.')
lesson=here/'two-reflections-in-folded-symplectic-coordinates.md'
report={'schema':'bounded-simultaneous-folded-form-check/v1','checks':checks,'passed':all(x['passed'] for x in checks),
 'lesson':lesson.name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'guard':'Exact bounded examples and numerical residuals do not independently verify the arbitrary-form spectator-flow and normal-form proofs.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':report['passed'],'checks':len(checks)}))

