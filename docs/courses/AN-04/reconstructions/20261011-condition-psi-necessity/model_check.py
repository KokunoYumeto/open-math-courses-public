"""Exact finite checks for phases, operator signs and explicit error depths."""
from pathlib import Path
import hashlib,json
import sympy as s
M=Path(__file__).resolve().parent;checks=[]
def zero(name,expr):
 v=s.simplify(s.expand(expr));assert v==0,(name,v)
 checks.append({'name':name,'exact':True,'passed':True})
t,x,y,z,H,a,lam,eta=s.symbols('t x y z H a lam eta',real=True)
Z=x+s.I*H;w=Z+s.I*Z**2/2
zero('linear_symbol_real_phase',s.re(w)-x*(1-H))
zero('linear_symbol_imaginary_phase',s.im(w)-(H-H**2/2+x*x/2))
zero('linear_symbol_gradient',s.diff(w,x)-(1-H+s.I*x))
zero('exact_linear_eikonal',a*s.diff(w,H)-s.I*a*s.diff(w,x))
zero('center_covector_equation',a*s.diff(1-H,H)+a)
zero('center_imaginary_equation',a*s.diff(H-H**2/2,H)-a*(1-H))
zero('positive_transverse_hessian',s.diff(s.im(w),x,2)-1)
Z=z+s.I*t*t/2;w=Z+s.I*(y*y+Z*Z)/2
zero('simple_complex_invariant',s.diff(Z,t)-s.I*t*s.diff(Z,z))
zero('simple_adjoint_eikonal',s.diff(w,t)-s.I*t*s.diff(w,z))
zero('simple_imaginary_phase',s.im(w)-((t*t+y*y+z*z)/2-t**4/8))
zero('simple_real_phase',s.re(w)-(z-z*t*t/2))
phi=s.Function('phi')(x);phase=s.Function('w')(x)
conjugated=lambda v:-s.I*s.diff(v,x)+lam*s.diff(phase,x)*v
square=conjugated(conjugated(phi))
zero('complete_second_derivative',square-(lam**2*s.diff(phase,x)**2*phi+lam*(2*s.diff(phase,x)*(-s.I*s.diff(phi,x))-s.I*s.diff(phase,x,2)*phi)-s.diff(phi,x,2)))
xi=s.symbols('xi');centered=lambda v:conjugated(v)-lam*eta*v
for degree in range(1,7):
 q=xi**degree;lhs=phi
 for j in range(degree):lhs=conjugated(lhs)
 rhs=0;term=phi
 for j in range(degree+1):
  if j:term=centered(term)
  rhs+=s.diff(q,xi,j).subs(xi,lam*eta)*term/s.factorial(j)
 zero('exact_centered_symbol_degree_'+str(degree),lhs-rhs)
A,B,fx,fq=s.symbols('A B fx fq',real=True,nonzero=True)
yp=-(fx+A*fq)/B;ep=A*yp-B*fq
zero('center_complex_linear_equation',ep-(A+s.I*B)*yp-s.I*(fx+(A+s.I*B)*fq))
N,nu,n=s.symbols('N nu n',integer=True,nonnegative=True)
R=N+n+2;J=R+nu+2;depth=2*(R+nu+3);K=2*(depth+J+3)
for name,e,target in [('phase',1-(depth+1)/2+nu,-s.Rational(5,2)),('amplitude',-(depth+1)/2+nu,-s.Rational(7,2)),('symbol_tail',-J-1+nu,-3)]:
 zero('error_margin_'+name,e+R-target)
zero('error_margin_symbol_Taylor',1-K/2+nu+R-(-2*R-2*nu-10))
zero('weak_to_lower_norm_exponent',(-N-n)-(-N-n/s.Integer(2))+n/s.Integer(2))
zero('residual_to_lower_norm_exponent',(-R)-(-N-n/s.Integer(2))+n/s.Integer(2)+2)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'source_sha256':sha(M/'condition-psi-necessity-and-approximate-adjoint-solutions.md'),'script_sha256':sha(Path(__file__)),'checks':checks,'scope':'Exact phase identities, moving-center signs, complete quadratic transport correction, six full polynomial symbol expansions and error-depth exponents. The analytic necessity proof is in the lesson.'}
(M/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8');print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
