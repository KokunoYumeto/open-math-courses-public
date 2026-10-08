"""Exact model checks for the homogeneous glancing-pair proof. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
r,z,w,v,mu,lam=s.symbols("r z w sigma mu lambda",real=True)
# Keep the positive model radius symbolic without imposing conditions on positions.
lam=s.Symbol("lambda",positive=True)
t,u,a,b,c,h=s.symbols("t u a b c h",real=True)
x=s.Matrix([r,z,w]);xi=s.Matrix([v,mu,lam])
coords=[r,z,w,v,mu,lam]
pb=lambda f,g:sum(s.diff(f,xi[j])*s.diff(g,x[j])-s.diff(f,x[j])*s.diff(g,xi[j]) for j in range(3))
p=v*v-r*lam*lam-mu*lam
groups=[];n=0
def eq(lhs,rhs):
 global n
 q=s.simplify(lhs-rhs)
 assert q==(s.zeros(*q.shape) if isinstance(q,s.MatrixBase) else 0),q
 n+=1
def group(name,scope):
 global n
 groups.append(dict(name=name,cases=n,kind="exact",scope=scope,passed=True));n=0
eq(pb(p,r),2*v);eq(pb(p,pb(p,r)),2*lam**2);eq(pb(r,pb(r,p)),2)
group("Second brackets","Exact signs for the ordered model defining functions.")

orbit={r:u*u,v:lam*u,z:-u,w:-s.Rational(2,3)*u**3,mu:0}
for f in [r,v,z,w,mu,lam]:
 eq(lam*s.diff(orbit.get(f,f),u),pb(p,f).subs(orbit,simultaneous=True))
eq(p.subs(orbit,simultaneous=True),0)
group("Tangent characteristic orbit","Every Hamilton equation and the characteristic identity at arbitrary positive radius.")

rr=2*h*lam*t+lam**2*t*t
vv=h*lam+lam**2*t
zz=-lam*t
ww=-2*h*lam**2*t*t-s.Rational(2,3)*lam**3*t**3-h*h*lam*t
end=-2*h/lam
eq(rr.subs(t,end),0);eq(vv.subs(t,end),-h*lam)
eq(zz.subs(t,end),2*h);eq(ww.subs(t,end),-s.Rational(2,3)*h**3)
eq(vv**2-rr*lam**2-h*h*lam**2,0)
group("Ambient chord and endpoint exchange","Exact return time, both endpoint position shifts and the full characteristic polynomial.")

q=s.Matrix([z,w,h,lam]);F=s.Matrix([z+2*h,w-s.Rational(2,3)*h**3,-h,lam])
df=lambda f:s.Matrix([s.diff(f,vv) for vv in q])
wedge=lambda f,g:df(f)*df(g).T-df(g)*df(f).T
omega=wedge(h*h*lam,z)+wedge(lam,w)
eq(F.subs(dict(zip(q,F)),simultaneous=True),q)
eq(F.jacobian(q).T*omega.subs(dict(zip(q,F)),simultaneous=True)*F.jacobian(q),omega)
bad=s.Matrix([z+2*h,w,-h,lam])
eq(bad.jacobian(q).T*omega.subs(dict(zip(q,bad)),simultaneous=True)*bad.jacobian(q)-omega,
   2*h*h*wedge(lam,h))
group("Two-fold form and mandatory cubic correction","Involution, exact pulled-back form, and nonzero error when the cubic position correction is omitted.")

J=s.zeros(6)
for k in range(3):J[k,k+3]=-1;J[k+3,k]=1
Delta=s.zeros(6);Delta[0,4]=c;Delta[4,0]=-c
A=J.inv()*Delta
eq(A*A,s.zeros(6));eq((J+t*Delta)*(s.eye(6)-t*A)*J.inv(),s.eye(6))
eq((J+t*Delta).det(),J.det())
group("Glancing linear homotopy","Rank-two nilpotence, full inverse identity and determinant, for symbolic perturbation and time.")

f=p/lam
grad=s.Matrix([s.diff(f,vv) for vv in coords]);dr=s.Matrix([1,0,0,0,0,0])
dd=grad*dr.T-dr*grad.T
rad=s.Matrix([0,0,0,v,mu,lam])
eq(dd.T*rad,f*dr)
eq((J+t*dd).det(),(1+2*t*v/lam)**2)
V=s.Matrix([0,0,0,-f/(1+2*t*v/lam),0,0])
eq((J+t*dd).T*V,-f*dr)
eq(s.diff(v+t*f,t)+sum(s.diff(v+t*f,coords[k])*V[k] for k in range(6)),0)
group("Nonconstant homogeneous relative correction","Euler primitive, determinant, exact Moser equation and conserved corrected normal momentum for delta=d(p_F/lambda) wedge dr.")

anchor={r:0,z:0,w:0,v:0,mu:0}
for k in range(1,5):
 aa=c*(1+k*r+z+v/lam);bb=b*(1+w+k*mu/lam)
 pp=aa*p;qq=bb*r
 eq(pb(qq,pb(qq,pp)).subs(anchor),2*c*b*b)
 eq(pb(pp,pb(pp,qq)).subs(anchor),2*c*c*b*lam**2)
group("Variable defining factors","Four nonconstant homogeneous units test both second-bracket identities, including cancellation of their derivative terms.")
source=ROOT/"homogeneous-glancing-pairs-and-boundary-signs.md"
record=dict(passed=True,groups=groups,total_cases=sum(g["cases"] for g in groups),
 exact_cases=sum(g["cases"] for g in groups),numerical_cases=0,
 source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 finite_checks_do_not_replace_proofs=True)
(ROOT/"model-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:record[k] for k in ["passed","total_cases","exact_cases","numerical_cases"]}))
