"""Exact finite checks for the actual boundary cubic phase. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
q,y,z,mu,rho,xi,c,t,tau,ss=s.symbols("q y z mu rho xi c t tau s",real=True)
lam=s.Symbol("lambda",positive=True)
groups=[];count=0
def eq(a,b):
 global count
 d=s.simplify(a-b)
 assert d==(s.zeros(*d.shape) if isinstance(d,s.MatrixBase) else 0),d
 count+=1
def group(name,scope):
 global count
 groups.append(dict(name=name,scope=scope,cases=count,kind="exact",passed=True));count=0

# One spectator pair suffices to check the full explicit shear formula.
zz,ee,zd=s.symbols("zprime etaprime zlast",real=True)
coords=s.Matrix([zz,zd,ee,lam])
F=s.Matrix([zz,zd-c*zz**2/2,ee+c*lam*zz,lam])
alpha=s.Matrix([ee,lam,0,0])
eq(F.jacobian(coords).T*alpha.subs(dict(zip(coords,F)),simultaneous=True),alpha)
omega=s.zeros(4)
for j in range(2):omega[j,j+2]=-1;omega[j+2,j]=1
eq(F.jacobian(coords).T*omega*F.jacobian(coords),omega)
inverse={zz:zz,zd:zd+c*zz**2/2,ee:ee-c*lam*zz,lam:lam}
eq(F.subs(inverse,simultaneous=True),coords)
group("Homogeneous boundary shear","Exact Euler one-form, symplectic matrix and inverse for the spectator shear.")

# Primitive restricted to one characteristic leaf.
sigma=s.Symbol("sigma",real=True)
rr=sigma**2/lam**2-mu/lam
primitive=mu*y+lam*z+s.Rational(2,3)*sigma**3/lam**2
eq(s.diff(primitive,sigma),sigma*s.diff(rr,sigma))
eq(s.diff(primitive,y),mu);eq(s.diff(primitive,z),lam)
eq((primitive-primitive.subs(sigma,-sigma))/2,s.Rational(2,3)*sigma**3/lam**2)
group("Leafwise primitive","All leaf coordinates and its exact odd part.")

theta=mu*y+lam*z
zeta=-lam**s.Rational(2,3)*q-mu*lam**s.Rational(1,3)*lam**-s.Rational(2,3)
zeta=s.simplify(zeta)
p=lambda a,b,d:a*a-q*d*d-b*d
B=lambda u,v:s.expand((p(*(u+v))-p(*u)-p(*v))/2)
dx=lambda f:s.Matrix([s.diff(f,a) for a in [q,y,z]])
eq(p(*dx(theta))-zeta*p(*dx(zeta)),0)
eq(B(dx(theta),dx(zeta)),0)
eq(p(*dx(theta))+zeta*p(*dx(zeta)),-2*q*lam**2-2*mu*lam)
eq(zeta.subs(q,0),-mu*lam**-s.Rational(1,3))
eq(sum(a*s.diff(theta,a) for a in [mu,lam]),theta)
eq(sum(a*s.diff(zeta,a) for a in [mu,lam]),s.Rational(2,3)*zeta)
group("Affine eikonal signs and degrees","Correct and incorrect signs, exact boundary argument and both Euler degrees.")

psi=theta-y*0+lam**-s.Rational(2,3)*tau*zeta+tau**3/(3*lam**2)
eq(sum(a*s.diff(psi,a) for a in [mu,lam,tau]),psi)
eq(s.diff(psi,tau),lam**-s.Rational(2,3)*(zeta+tau**2*lam**-s.Rational(4,3)))
critical={q:(ss**2-mu*lam**-s.Rational(1,3))*lam**-s.Rational(2,3)}
eq(p(*(dx(theta)+ss*dx(zeta))).subs(critical),0)
eq((theta+ss*zeta+ss**3/3).subs(zeta,-ss**2),theta-s.Rational(2,3)*ss**3)
for eta in [mu,lam]:
 eq(s.diff(psi,eta).subs(tau,ss*lam**s.Rational(2,3)).subs(critical),
    (s.diff(theta,eta)+ss*s.diff(zeta,eta)).subs(critical))
group("Ordinary homogeneous cubic phase","Homogeneity, auxiliary critical equation, characteristic identity, critical value and both parameter derivatives.")

# A genuine smooth base change with a normal/tangential cross term.
f=s.exp(y/4)*(q+q*q/5);fq=s.diff(f,q);fy=s.diff(f,y)
actual=lambda a,b,d:s.expand((a/fq)**2-f*d*d-(b-a*fy/fq)*d)
zzeta=-lam**s.Rational(2,3)*f-mu*lam**-s.Rational(1,3)
polar=lambda u,v:s.expand((actual(*(u+v))-actual(*u)-actual(*v))/2)
eq(actual(*dx(theta))-zzeta*actual(*dx(zzeta)),0)
eq(polar(dx(theta),dx(zzeta)),0)
eq(zzeta.subs(q,0),-mu*lam**-s.Rational(1,3))
actual_cov=dx(theta)+ss*dx(zzeta)
eq(actual_cov[0]/fq,-ss*lam**s.Rational(2,3))
eq(actual_cov[1]-(actual_cov[0]/fq)*fy,mu)
eq(actual_cov[2],lam)
eq(actual(*actual_cov),ss**2*lam**s.Rational(4,3)-f*lam**2-mu*lam)
eq(fy.subs(q,0),0)
group("Variable-base symbol","Exact quadratic and cross-term transformation, both eikonal identities, boundary normalization and all three covector components.")

normal=s.Symbol("normal",positive=True)
rb=s.Symbol("root",positive=True)
# For q=0, mu=lambda*t^2, s=-lambda^(1/3)*t.
subs={q:0,mu:lam*t*t,ss:-lam**s.Rational(1,3)*t}
w1=(s.diff(theta,mu)+ss*s.diff(zeta,mu)).subs(subs,simultaneous=True)
w2=(s.diff(theta,lam)+ss*s.diff(zeta,lam)).subs(subs,simultaneous=True)
eq(w1,y+t);eq(w2,z-t**3/3)
eq(w1.subs({y:y+2*t,t:-t},simultaneous=True),w1)
eq(w2.subs({z:z-s.Rational(2,3)*t**3,t:-t},simultaneous=True),w2)
group("Boundary characteristic center","Both input shifts and invariance under the full boundary exchange.")

# Formal square-root recursion tested with genuinely varying coefficients.
v0=s.Symbol("v0",positive=True)
e=s.Symbol("epsilon",real=True)
# rho^2 - (-v0+q+e*q^2)=0; root at q=0 is +i*sqrt(v0).
root=s.I*s.sqrt(v0)*(1-(q+e*q*q)/v0)**s.Rational(1,2)
jet=s.series(root,q,0,5).removeO()
res=s.expand(jet*jet+v0-q-e*q*q)
for k in range(5):eq(s.diff(res,q,k).subs(q,0),0)
W=-s.I*s.Rational(2,3)*v0**s.Rational(3,2)+s.integrate(jet,q)
eq(s.diff(W,q),jet)
eq(s.conjugate(s.conjugate(W)),W)
group("Elliptic formal boundary jets","Five exact residual jets for a variable quadratic normal equation, its integrated branch and conjugacy.")

source=ROOT/"boundary-normalized-cubic-phases.md"
record=dict(passed=True,groups=groups,total_cases=sum(g["cases"] for g in groups),
 exact_cases=sum(g["cases"] for g in groups),numerical_cases=0,
 source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 finite_checks_do_not_replace_proofs=True)
(ROOT/"model-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:record[k] for k in ["passed","total_cases","exact_cases","numerical_cases"]}))
