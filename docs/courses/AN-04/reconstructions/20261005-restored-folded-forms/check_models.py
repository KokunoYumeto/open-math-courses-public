"""Bounded coordinate, flow and form checks for U016; no general-proof certification."""
import hashlib,json,itertools
from pathlib import Path
import sympy as S
import mpmath as mp
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
x,z,s,rho,a,kappa,time=S.symbols('x z s rho a kappa time',real=True)
u=S.Matrix([x,z,s,rho])
def dform(lam,coord=u):
    return S.Matrix(len(coord),len(coord),lambda i,j:S.diff(lam[j],coord[i])-S.diff(lam[i],coord[j]))
def wedge(v,w):return v*w.T-w*v.T
def eq(A,B):assert all(S.simplify(e)==0 for e in A-B)
def record(name,evidence):checks.append({'name':name,'passed':True,'bounded_evidence':evidence})
def pfaff4(B):return S.simplify(B[0,1]*B[2,3]-B[0,2]*B[1,3]+B[0,3]*B[1,2])
def d2(B,coord=u):
    return {ijk:S.simplify(S.diff(B[j,k],coord[i])+S.diff(B[k,i],coord[j])+S.diff(B[i,j],coord[k]))
            for ijk in itertools.combinations(range(len(coord)),3) for i,j,k in [ijk]}
B0=dform(S.Matrix([s*s/2,rho,0,0]))
assert B0.subs(s,0).rank()==2 and B0.extract([0,1,3],[0,1,3]).rank()==2
assert pfaff4(B0)==-s
rad=B0.subs(s,0).nullspace();assert len(rad)==2
# Counterexample uses (x,y,z,s); these are four independent temporary coordinates.
xx,yy,zz,ss=S.symbols('xx yy zz ss',real=True);uc=S.Matrix([xx,yy,zz,ss])
ex=S.Matrix([1,0,0,0]);ey=S.Matrix([0,1,0,0]);es=S.Matrix([0,0,0,1])
d_sz=S.Matrix([0,0,ss,zz])
Bc=wedge(ex,es)+wedge(ey,d_sz)
assert pfaff4(Bc)==ss and Bc.subs(ss,0).rank()==2
assert Bc.subs(ss,0).extract([0,1,2],[0,1,2]).rank()==0
assert all(e==0 for e in d2(Bc,uc).values())
record('ambient/restricted radicals and simple-zero counterexample',
       'Exact four-dimensional ranks and top Pfaffians; a closed form with a simple top zero but zero restricted rank fails the stated theorem hypothesis.')
A=1+z*z;aa=z+rho;bb=1+rho*rho
alpha=S.Matrix([A,aa,0,bb])
B=dform(S.Matrix([0,rho,0,0])+s*s*alpha/2)
F=S.Matrix([x,z-bb*s*s/2,s*S.sqrt(A),rho+aa*s*s/2]);J=F.jacobian(u)
norm=dform(S.Matrix([s*s/2,rho,0,0]))
pulled=J.T*norm.subs(dict(zip(u,F)),simultaneous=True)*J
difference=B-pulled
for e in difference:
    assert S.simplify(e.subs(s,0))==0
    assert S.simplify(S.diff(e,s).subs(s,0))==0
assert S.simplify(J.det().subs(s,0))==S.sqrt(A)
reflection=S.diag(1,1,-1,1)
eq(reflection.T*B.subs(s,-s)*reflection,B)
record('first-jet mixed-pair normalization',
       'Full nonlinear closed example; every coefficient of the model pullback error vanishes to second normal order; collar Jacobian and exact reflection pullback checked.')
h=z+rho*rho
beta=S.Matrix([kappa*s**3*h,0,0,0])
Delta=dform(beta)
relative=S.Matrix([S.integrate(Delta[2,j].subs(s,S.Symbol('v')), (S.Symbol('v'),0,s)) for j in range(4)])
eq(relative,beta)
Bt=B0+dform(S.Matrix([time*kappa*s**3,0,0,0]))
betaconst=S.Matrix([kappa*s**3,0,0,0])
Wt=S.simplify(Bt.inv()*betaconst)
eq(Wt,S.Matrix([0,0,-kappa*s*s/(1+3*time*kappa*s),0]))
eq(Bt.T*Wt,-betaconst)
mp.mp.dps=90;flow_samples=[];kap=mp.mpf('.3')
def flow(si,ti):
    ww=mp.findroot(lambda w:w*w/2+ti*kap*si*w**3-mp.mpf('.5'),mp.mpf(1))
    return si*ww
for si in [mp.mpf('-.2'),mp.mpf('-.05'),mp.mpf('.05'),mp.mpf('.2')]:
    for ti in [mp.mpf(0),mp.mpf('.5'),mp.mpf(1)]:
        val=flow(si,ti)
        field=mp.diff(lambda t0:flow(si,t0),ti)
        expected=-kap*val*val/(1+3*ti*kap*val)
        derivative=mp.diff(lambda si0:flow(si0,ti),si)
        pull=(val+3*ti*kap*val*val)*derivative-si
        assert abs(field-expected)<mp.mpf('1e-75')
        assert abs(pull)<mp.mpf('1e-75')
        flow_samples.append({'s':str(si),'time':str(ti),'pullback_residual':mp.nstr(abs(pull),5)})
record('relative primitive and actual Moser flow',
       {'exact_relative_primitive':True,'smooth_field_and_contraction':True,
        'implicit_flow_samples':flow_samples,
        'guard':'Implicit nonlinear flows at specified initial values/times, independently differentiated; the arbitrary-form Moser theorem is proved analytically.'})
eta=s*S.sqrt(1+2*kappa*s*s)
assert S.simplify(eta*S.diff(eta,s)-s*(1+4*kappa*s*s))==0
assert S.simplify(eta.subs(s,-s)+eta)==0
Winv=-kappa*s**3/(1+4*time*kappa*s*s)
assert S.simplify(Winv.subs(s,-s)+Winv)==0
record('reflection-preserving exact remainder normalization',
       'Full odd normal coordinate and its form pullback, plus exact equivariance of the nontrivial Moser field.')
Fhom=S.Matrix([x,z,s*S.sqrt(1+2*a*s*s/rho),rho]);Jhom=Fhom.jacobian(u)
lam=S.Matrix([s*s/2+a*s**4/rho,rho,0,0])
target_lam=S.Matrix([s*s/2,rho,0,0])
eq(Jhom.T*target_lam.subs(dict(zip(u,Fhom)),simultaneous=True),lam)
Bhom=dform(lam);eq(Jhom.T*B0.subs(dict(zip(u,Fhom)),simultaneous=True)*Jhom,Bhom)
R=S.Matrix([0,0,s/2,rho])
expected_weights=S.Matrix([0,0,Fhom[2]/2,Fhom[3]])
eq(Fhom.jacobian(u)*R,expected_weights)
eq(Bhom.T*R,lam)
assert S.simplify(pfaff4(Bhom)+s*(1+4*a*s*s/rho))==0
# A different conic action has radial tangency at (x,rho)=(1,0).
Rbad=S.Matrix([x,0,0,rho]);JR=Rbad.jacobian(u)
LieB=B0.applyfunc(lambda q:sum(Rbad[j]*S.diff(q,u[j]) for j in range(4)))+JR.T*B0+B0*JR
eq(LieB,B0)
lam_bad=B0.T*Rbad
eq(lam_bad,S.Matrix([0,rho,-s*x,0]))
eq(lam_bad.subs({x:1,z:0,s:0,rho:0}),S.zeros(4,1))
record('full homogeneous normalizing map and radial exclusion',
       'Exact one-form and two-form pullbacks including mixed frequency terms; all Euler degrees; a nonzero radial field with vanishing restricted canonical one-form supplies the excluded case.')
q1,q2,p1,p2=S.symbols('q1 q2 p1 p2',real=True)
v=S.Matrix([q1,q2,p1,p2]);Om=dform(S.Matrix([p1,p2,0,0]),v)
b=S.Function('b')(p1)
candidate=S.Matrix([q1,q2+b*q1,p1,p2]);Cj=candidate.jacobian(v)
err=S.simplify(Cj.T*Om*Cj-Om)
expected=wedge(S.Matrix([0,0,0,1]),S.Matrix([b,0,q1*S.diff(b,p1),0]))
eq(err,expected)
Hq1=Om.inv()*S.Matrix([1,0,0,0])
eq(Hq1,S.Matrix([0,0,-1,0]))
flowtarget=S.Matrix([q1,q2,p1-time,p2]);eq(flowtarget.jacobian(v).T*Om*flowtarget.jacobian(v),Om)
br=S.Function('b')(s)
badtheta=wedge(S.Matrix([0,0,1,0]),S.Matrix([1+rho*br,0,0,0]))+wedge(S.Matrix([0,0,0,1]),S.Matrix([0,1,0,0]))
assert d2(badtheta)[(0,2,3)]==-br
areas=[S.integrate(s,(s,S.Rational(1,2),1))/2,
       S.integrate(s,(s,-1,-S.Rational(1,2)))/2,
       (S.Rational(1,2)-S.Rational(1,8))/2]
assert areas==[S.Rational(3,16),-S.Rational(3,16),S.Rational(3,16)]
record('full target extension, coefficient-closure defect and signed areas',
       'Exact bad negative-side coordinate pullback and actual Hamiltonian target collar; nonclosed coefficient extension; both source patch integrals and target integral with their stated orientations.')
lesson=here/'folded-forms-and-symplectic-targets.md'
report={'schema':'bounded-folded-form-computational-check/v1','passed':True,'checks':checks,
 'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'finite_examples_only':True,'full_mathematical_review':False}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'lesson_sha256':sha(lesson)}))
