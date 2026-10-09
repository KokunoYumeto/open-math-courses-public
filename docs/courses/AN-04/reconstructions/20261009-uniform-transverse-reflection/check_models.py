"""Exact finite checks accompanying the analytic reflection proof."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
x,z,c,k,mu,lam,L,j,N,rho,tau=s.symbols('x z c k mu lam L j N rho tau',real=True)
checks=[]
def check(name,expr):
    value=s.simplify(s.expand_trig(expr).rewrite(s.exp))
    assert value==0,(name,value)
    checks.append(name)
D=lambda f:-s.I*s.diff(f,x)
u=s.sin(c*k*x)*s.exp(s.I*k*z)
vp=D(u)+c*k*u;vm=D(u)-c*k*u
check('flat PDE',D(D(u))-c**2*(-s.diff(u,z,2)))
check('zero Dirichlet value',u.subs(x,0))
check('plus output',vp+s.I*c*k*s.exp(s.I*c*k*x)*s.exp(s.I*k*z))
check('minus output',vm+s.I*c*k*s.exp(-s.I*c*k*x)*s.exp(s.I*k*z))
check('plus first order equation',D(vp)-c*k*vp)
check('minus first order equation',D(vm)+c*k*vm)
check('full boundary equality',vp.subs(x,0)-vm.subs(x,0))
check('root gap',c*k-(-c*k)-2*c*k)
check('plus pointwise squared magnitude',s.expand_complex(vp*s.conjugate(vp))-c**2*k**2)
check('minus pointwise squared magnitude',s.expand_complex(vm*s.conjugate(vm))-c**2*k**2)
check('strip norm squared',s.integrate(2*s.pi*c**2*k**2,(x,j,j+L))-L*2*s.pi*c**2*k**2)
w=s.exp(s.I*lam*x-mu*x)
check('complex lower term exact evolution',D(w)-(lam+s.I*mu)*w)
check('complex lower term energy derivative',s.diff(w*s.conjugate(w),x)+2*mu*w*s.conjugate(w))
check('anti Hermitian part',(lam+s.I*mu)-s.conjugate(lam+s.I*mu)-2*s.I*mu)
check('boundary mismatch example',D(N*x*s.exp(s.I*k*z)).subs(x,0)+s.I*N*s.exp(s.I*k*z))
check('rank one projection on its mode',s.integrate(s.exp(s.I*k*(z-x))*s.exp(s.I*k*x),(x,0,2*s.pi))/(2*s.pi)-s.exp(s.I*k*z))
aa=s.Function('a')(x);cc=s.Function('C')(x);ff=s.Function('f')(x)
ap=-cc-aa
product=D(D(ff)-aa*ff)-ap*(D(ff)-aa*ff)
expected=D(D(ff))+cc*D(ff)+(s.I*s.diff(aa,x)-cc*aa-aa**2)*ff
check('complete normal factor identity',product-expected)
q=s.Function('q')(x)
check('normal derivative of the localizer',D(q*ff)-q*D(ff)+s.I*s.diff(q,x)*ff)
for sign in [-1,1]:
    xx=sign*2*tau;zz=-2*tau;xi=sign
    check('ray normal Hamilton velocity '+str(sign),s.diff(xx,tau)-2*xi)
    check('ray tangential Hamilton velocity '+str(sign),s.diff(zz,tau)+2)
    check('ray characteristic identity '+str(sign),xi**2-1)
    check('ray boundary meeting '+str(sign),xx.subs(tau,0)**2+zz.subs(tau,0)**2)
check('strip exact width',s.Rational(1)-s.Rational(1,2)-s.Rational(1,2))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'numerical_checks':0,'checks':checks,
        'source_sha256':sha(root/'uniform-transverse-reflection-with-strip-observations.md'),
        'script_sha256':sha(Path(__file__)),
        'scope':'Exact algebra, source terms, boundary cancellation, energy signs and figure coordinates. The full operator estimate is proved in the lesson; these finite checks do not replace it.'}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
