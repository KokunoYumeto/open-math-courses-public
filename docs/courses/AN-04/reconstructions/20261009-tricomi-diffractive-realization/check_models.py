"""Exact algebra checks complement, and do not replace, the analytic proof. CC0."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
t,x,y,xi,eta=S.symbols('t x y xi eta',real=True)
p=xi**2-x*eta**2
curve={x:t**2,y:-S.Rational(2,3)*t**3,xi:t,eta:S.Integer(1)}
cases=[]
def check(name,a,b=0):
    z=S.simplify(a-b);assert z==0,(name,z)
    cases.append({'name':name,'passed':True})
H=[S.diff(p,xi),S.diff(p,eta),-S.diff(p,x),-S.diff(p,y)]
for coordinate,velocity in zip([x,y,xi,eta],H):
    check('Hamilton equation '+str(coordinate),S.diff(curve[coordinate],t),velocity.subs(curve))
check('Characteristic equation',p.subs(curve))
check('Normal acceleration',S.diff(curve[x],t,2),2)
check('Compressed normal coordinate',(x*xi).subs(curve),t**3)
for name,expr in [('base x',curve[x]),('base y',curve[y]),('compressed normal',t**3)]:
    check('Zero projected velocity '+name,S.diff(expr,t).subs(t,0))
check('Nonzero ordinary normal velocity',S.diff(curve[xi],t).subs(t,0),1)
for sign in [-1,1]:
    check('Branch characteristic '+str(sign),(sign*S.sqrt(x))**2-x)
    check('Branch slope '+str(sign),S.diff(-sign*S.Rational(2,3)*x**S.Rational(3,2),x),-sign*S.sqrt(x))
f=S.Function('f')(x);A=S.Function('A')(x);B=S.Function('B')(x)
D=lambda v:-S.I*S.diff(v,x)
check('Ordered square with nonconstant complex coefficient',D(D(f)-A*f)-A*(D(f)-A*f),D(D(f))-2*A*D(f)+S.I*S.diff(A,x)*f+A**2*f)
check('Complete-square comparison',D(D(f)-A*f)-A*(D(f)-A*f)-(B+S.I*S.diff(A,x)+A**2)*f,D(D(f))-2*A*D(f)-B*f)
chi=S.Function('chi')(x);phi=S.Function('phi')(y)
ell=S.I*x*chi*phi
check('Exact lifted forcing',D(D(ell))-x*(-S.diff(ell,y,2)),-S.I*(2*S.diff(chi,x)+x*S.diff(chi,x,2))*phi+S.I*x*x*chi*S.diff(phi,y,2))
check('Lift zero value',ell.subs(x,0))
check('Lift normal datum',D(ell).subs(x,0).subs(chi.subs(x,0),1),phi)
check('Missing-i normal datum',D(x*phi).subs(x,0),-S.I*phi)
for d in [1,2,3,7,12]:
    k=d-1;beta=S.Rational(d+1,4);s=d+2;K=s+3
    check('Gaussian radial exponent d='+str(d),-2*beta+S.Rational(k,2),-1)
    check('Available datum exponent d='+str(d),2*(s+2)-2*K-1,-3)
    check('Critical datum exponent d='+str(d),2*K-2*K-1,-1)
z=S.symbols('z',positive=True)
check('Linear endpoint integral derivative',S.diff(2*S.sqrt(z),z),z**(-S.Rational(1,2)))
for m in [S.Rational(1,2),S.Integer(1),S.Rational(3,2)]:
    check('General endpoint primitive m='+str(m),S.diff(z**(1-m/2)/(1-m/2),z),z**(-m/2))
check('Borderline logarithmic primitive',S.diff(S.log(z),z),1/z)
source=root/'singularities-on-diffractive-tricomi-rays.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'scope':'Exact Hamilton, compression, ordered operator, lift, Sobolev exponent and endpoint-integral identities. Analytic existence, wavefront equality and rough-domain claims are proved in the lesson.','cases':cases}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:out[k] for k in ['passed','total_cases','source_sha256']}))
