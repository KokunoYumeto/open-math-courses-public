"""Finite evidence for U015. The smooth infinite argument is in the lesson."""
import hashlib,json,math
from pathlib import Path
import sympy as S
import mpmath as mp
here=Path(__file__).resolve().parent;checks=[]
t,z,s,rho,scale=S.symbols('t z s rho scale',real=True)
y=S.Matrix([t,z,s]);zero=S.zeros(3,1)
def compose(a,b):
    return a.subs(dict(zip(y,b)),simultaneous=True).applyfunc(S.simplify)
def equal(a,b):
    assert all(S.simplify(v)==0 for v in a-b)
def record(name,detail):checks.append({'name':name,'passed':True,'bounded_evidence':detail})
f=S.Matrix([t,z,-s]);g0=S.Matrix([t+s,z,-s])
equal(compose(f,f),y);equal(compose(g0,g0),y)
equal(compose(f,g0),S.Matrix([t+s,z,s]))
equal(compose(g0,f),S.Matrix([t-s,z,s]))
vf=S.Matrix([0,0,1]);vg=S.Matrix([-S.Rational(1,2),0,1])
equal(f.jacobian(y)*vf,-vf);equal(g0.jacobian(y)*vg,-vg)
# The radial frame uses (t,s,rho), not the three ordinary coordinates (t,z,s).
radial_frame=S.Matrix([[0,-S.Rational(1,2),0],[1,1,0],[0,0,rho]])
assert S.simplify(radial_frame.det())==rho/2
record('ordered products, reflection lines and radial independence',
       'Exact involution matrices, both product signs, and determinant rho/2 for the independent radial frame.')
lg=S.Matrix([t+S.log(1+s),z,-s/(1+s)])
Ulog=S.Matrix([S.exp(t)-1,z,s*S.exp(t)])
Ug=compose(Ulog,lg);expected=compose(g0,Ulog)
# exp(log(1+s)) simplifies on the local real domain s>-1.
equal(Ug,expected)
assert S.simplify(Ulog.jacobian(y).det())==S.exp(2*t)
assert S.simplify(compose(lg,lg)[2]-s)==0
record('exact logarithmic first normalization',
       'Full coordinate conjugacy and nonzero Jacobian; involution normal component checked exactly, tangential log identity verified on s>-1 in the proof.')
U=S.Matrix([t*(1+s*s),z+t*s*s,s])
Ui=S.Matrix([t/(1+s*s),z-t*s*s/(1+s*s),s])
ng=compose(Ui,compose(g0,U))
equal(ng,S.Matrix([t+s/(1+s*s),z-s**3/(1+s*s),-s]))
equal(compose(ng,ng),y);equal(compose(U,ng),compose(g0,U))
equal(compose(U,f),compose(f,U))
assert S.simplify(U.jacobian(y).det())==1+s*s
record('nonlinear spectator conjugacy',
       'Exact rational involution with changing spectator; full conjugacy and parity, not only its derivative at the fixed hypersurface.')
def trunc(m,limits):
    return S.Matrix([S.series(q,s,0,n+1).removeO().expand() for q,n in zip(m,limits)])
def jetcompose(a,b,limits):
    return trunc(a.subs(dict(zip(y,b)),simultaneous=True),limits)
h=S.Matrix([t+z,t*t]);H=t+z
V=z*t+t*t/2
v=S.Matrix([z*t*t/2+t**3/6-t*t/2-z*t,-t**3/3])
equal(v.diff(t),S.Matrix([V-h[0],-h[1]]))
assert S.simplify(S.diff(V,t)-H)==0
u=S.Matrix([t+s*s*v[0],z+s*s*v[1],s+s**3*V])
uimin=S.Matrix([t-s*s*v[0],z-s*s*v[1],s-s**3*V])
g3=S.Matrix([t+s+s**3*h[0],z+s**3*h[1],-s+s**4*H])
inner=jetcompose(g3,uimin,[3,3,4])
conj=jetcompose(u,inner,[3,3,4]);equal(conj,g0)
g2=S.Matrix([t+s+s*s*h[0],z+s*s*h[1],-s+s**3*H])
square=jetcompose(g2,g2,[2,2,3])
equal(square,S.Matrix([t+2*s*s*h[0],z+2*s*s*h[1],s-2*s**3*H]))
record('weighted normal coefficient corrections',
       'Even k=2 forced coefficients and odd k=3 full conjugation jets, including the normal coefficient one order later and both homological-equation signs.')
mp.mp.dps=100
def bump(x):
    return mp.exp(-1/(1-x*x)) if abs(x)<1 else mp.mpf(0)
def flat(v):
    return mp.exp(-1/(v*v)) if v else mp.mpf(0)
samples=[]
for ss in [mp.mpf('.08'),mp.mpf('.125'),mp.mpf('.2'),-mp.mpf('.125')]:
    for tt in [mp.mpf('-.35'),mp.mpf('.1')]:
        n=int(mp.ceil((3+abs(tt))/abs(ss)))+5
        def W(a,b):return flat(b)*sum((bump(a+k*b) for k in range(n)),mp.mpf(0))
        res=W(tt,ss)-W(tt+ss,ss)-flat(ss)*bump(tt)
        assert abs(res)<flat(ss)*mp.mpf('1e-85')
        assert abs(W(tt,ss)) <= (1+3/abs(ss))*flat(ss)
        samples.append({'t':str(tt),'s':str(ss),'relative_residual':mp.nstr(abs(res)/flat(ss),6)})
# Independently differentiate the finite active sum and use the chain/product formula.
ss=mp.mpf('.2');tt=mp.mpf('-.35');n=25
def Wfixed(a,b):return flat(b)*sum((bump(a+k*b) for k in range(n)),mp.mpf(0))
for r in range(4):
    direct=mp.diff(lambda b:Wfixed(tt,b),ss,r)
    formula=mp.mpf(0)
    for j in range(r+1):
        inner=sum((mp.mpf(k)**j*mp.diff(bump,tt+k*ss,j) for k in range(n)),mp.mpf(0))
        formula+=math.comb(r,j)*mp.diff(flat,ss,r-j)*inner
    assert abs(direct-formula)<max(mp.mpf('1e-95'),abs(direct)*mp.mpf('1e-80'))
record('flat difference series and step-size derivatives',
       {'telescoping_samples':samples,'normal_derivative_orders':[0,1,2,3],
        'guard':'Finite smooth-bump sums at specified nonzero steps; infinite smoothness and flatness are proved analytically.'})
orbits=[]
for start_s in [mp.mpf('.16'),mp.mpf('.2'),mp.mpf('.24'),-mp.mpf('.2')]:
    start_t=-mp.sign(start_s)*mp.mpf('.4')
    tt=start_t;ss=start_s;P=mp.mpf(0)
    count=int(mp.ceil(4/abs(start_s)))
    for k in range(count):
        p=mp.mpf('.01')*flat(ss)*bump(tt);P=max(P,abs(p))
        tt,ss=tt+ss+p,ss+p
        et=tt-start_t-(k+1)*start_s;es=ss-start_s
        tol=mp.mpf('1e-90')
        assert abs(es)<=(k+1)*P+tol
        assert abs(et)<=((k+1)*(k+2)/2)*P+tol
        assert abs(es)<abs(start_s)/2
    assert abs(tt)>1 and bump(tt)==0
    orbits.append({'s':str(start_s),'iterates':count,
                   't_error':mp.nstr(et,8),'s_error':mp.nstr(es,8)})
record('flat perturbations of both shear components',
       {'orbits':orbits,
        'guard':'Full nonlinear sampled iterates verify the normal-first recurrence and quadratic tangential accumulation; they do not certify an arbitrary smooth germ.'})
lesson=here/'simultaneous-reflections-and-flat-corrections.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'schema':'bounded-two-reflections-computational-check/v1','passed':True,
 'checks':checks,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'finite_examples_only':True,'full_mathematical_review':False,
 'infinite_argument':'Parameter Borel convergence and all flat-iterate derivatives are proved in the lesson, not inferred from these finite checks.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'lesson_sha256':sha(lesson)}))
