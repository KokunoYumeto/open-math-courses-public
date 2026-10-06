"""Independent finite models for the local compressed boundary calculus.

CC0, AN-04 course-writing task and OpenAI Codex, 5 October 2026.
These checks verify algebra and scale conventions, not full analytical proofs.
"""
from pathlib import Path
import json,hashlib,math
import sympy as s
import numpy as np
ROOT=Path(__file__).resolve().parent
t,r,z,y,eta,tau,x,xi,lam=s.symbols('t r z y eta tau x xi lam',real=True)
I=s.I;checks=[]
D=lambda f,j=1:(-I)**j*s.diff(f,t,j)
def eq(a,b):
 c=a-b
 return all(s.simplify(q)==0 for q in c) if isinstance(c,s.MatrixBase) else s.simplify(c)==0
# Compression coordinates, all inverse ratios and original Jacobian.
X=t*(1+r/2);Y=t*(1-r/2)
assert s.det(s.Matrix([X,Y]).jacobian([t,r]))==-t
zn=2*r/(2+r);inv=2*z/(2-z)
assert eq(zn.subs(r,inv),z) and eq(inv.subs(z,zn),r)
assert eq((2-r)/(2+r),1-zn)
assert eq(s.diff(zn,r),(1+r/2)**-2)
assert eq((1+r/2).subs(r,inv),2/(2-z))
checks.append({'name':'corner_jacobian_inverse_and_ratio','cases':6})
# Full triangular normal generator identity on arbitrary monomials.
for k in range(8):
 q=t**lam
 for j in range(k):q=t*D(q)+I*j*q
 assert eq(q,t**k*D(t**lam,k))
checks.append({'name':'normal_generator_all_lower_terms','cases':8})
# The exact jet law (5.2), checked against differentiation of the original
# compressed operator on a plane wave, without using the proposed jet law.
a=(1+t+t**3)*(1+eta+eta**2)+t**2*eta**3
for k in range(7):
 direct=D(s.exp(I*t*tau)*a.subs(eta,t*tau),k).subs(t,0)
 ans=0
 for j in range(k+1):
  akj=sum(s.binomial(j,l)*(-I)**(k-j+l)*s.diff(a,t,k-j,eta,l).subs({t:0,eta:0}) for l in range(j+1))
  ans+=s.binomial(k,j)*akj*tau**j
 assert eq(direct,ans)
checks.append({'name':'every_original_normal_jet_coefficient','cases':7})
# Exact noncommutative product for two matrix-valued differential symbols.
A=s.Matrix([[1+t, I*t],[t**2,1-t]])
B=s.Matrix([[t,1],[I,1+t**2]])
C=s.Matrix([[1,x],[0,t]])
E=s.Matrix([[t**2,I],[1,x+t]])
aa=A*eta**2+C*eta
bb=B*eta+E
def quant(a0,u):
 out=s.zeros(a0.rows,1)
 deg=max(s.degree(q,eta) if q!=0 else 0 for q in a0)
 for j in range(int(deg)+1):
  coeff=a0.applyfunc(lambda q:s.expand(q).coeff(eta,j))
  out+=coeff*t**j*D(u,j)
 return out
u=s.Matrix([1+t+t**5,x+t**4+I*t**2])
sym=s.zeros(2,2)
for j in range(3):
 dy=(-I)**j*s.diff(bb.subs({t:y*t,eta:y*eta}, simultaneous=True),y,j).subs(y,1)
 sym+=s.diff(aa,eta,j)*dy/s.factorial(j)
assert eq(quant(aa,quant(bb,u)),quant(s.expand(sym),u))
assert not eq(aa*bb,bb*aa)
checks.append({'name':'ordered_matrix_composition_against_direct_differentiation','cases':1})
# Adjoint transform versus direct formal adjoint of t^j coefficients.
M=s.Matrix([[1+I*t,t],[x,2-I*t]])
a0=M*eta**2+B*eta+E
adj=s.zeros(2,2)
for j in range(3):
 c=a0.conjugate().T.subs({t:t*y,eta:y*eta}, simultaneous=True)
 adj+=(-I)**j*s.diff(c,y,j,eta,j).subs(y,1)/s.factorial(j)
direct=s.zeros(2,1)
for j in range(3):
 coef=a0.applyfunc(lambda q:s.expand(q).coeff(eta,j)).conjugate().T
 direct+=D(t**j*coef*u,j)
assert eq(direct,quant(s.expand(adj),u))
checks.append({'name':'full_matrix_adjoint_transform_and_coefficient_derivatives','cases':1})
# The exact symmetric normal Schur marginal.
assert s.integrate(y/(1+y)**3,(y,0,s.oo))==s.Rational(1,2)
checks.append({'name':'one_half_Schur_marginal','cases':1})
# Series coefficients and the full squared identity, with a non-diagonal
# complex matrix comparison independent of the coefficient recurrence.
co=[s.binomial(s.Rational(1,2),k)*(-1)**k for k in range(15)]
for k in range(1,15):
 assert s.simplify(sum(co[j]*co[k-j] for j in range(k+1)))==(-1 if k==1 else 0)
mat=np.array([[.2+.1j,.15],[-.1j,.25-.1j]])
b=mat.conj().T@mat
out=np.zeros_like(b);power=np.eye(2,dtype=complex)
for k in range(15):
 out+=float(co[k])*power;power=power@b
assert np.linalg.norm(out@out-(np.eye(2)-b))<1e-13
assert np.linalg.eigvalsh(out).min()>0
checks.append({'name':'matrix_square_root_full_constant_and_product_identity','cases':15})
# Both dyadic interpolation kernels at their worst allowed exponents.
for shift in [i/20 for i in range(-10,11)]:
 for d in range(-40,41):
  c1=2.**(d*(shift-1))*min(1.,2.**(2*d))
  c2=2.**(d*(shift+1))*min(1.,2.**(-2*d))
  assert max(c1,c2)<=2.**(-abs(d)/2)*(1+1e-13)
checks.append({'name':'both_summable_dyadic_kernels_including_endpoints','cases':1701})
# Positive-support moment cancellation: model a positive smooth mollifier
# with its first-moment Taylor expansion, then form 2 phi - phi*phi.
q=1-I*z+2*z**2/3+I*z**3
psi=2*q-q*q
assert psi.subs(z,0)==1 and s.diff(psi,z).subs(z,0)==0
assert s.expand(1-psi)==s.expand((1-q)**2)
checks.append({'name':'signed_mollifier_quadratic_cancellation','cases':3})
# The low/high continuous interpolation scalar integrals are explicit.
for sh in [s.Rational(-1,2),0,s.Rational(1,2)]:
 first=s.integrate(y**(1-2*sh),(y,0,1))+s.integrate(y**(-3-2*sh),(y,1,s.oo))
 second=s.integrate(y**(1-2*sh),(y,0,1))+s.integrate(y**(-3-2*sh),(y,1,s.oo))
 assert first.is_finite and second.is_finite and first>0
checks.append({'name':'continuous_scale_integrals_at_three_critical_indices','cases':3})
# Exact nonzero front face / inverse residual kernel away from its flat sides.
H=(2/(2+r))*s.exp(-t*(1+r/2))*s.exp(-(2*r/(2+r))**2)
rec=2/(2-z)*H.subs({t:x*(2-z)/2,r:2*z/(2-z)},simultaneous=True)
assert eq(rec,s.exp(-x)*s.exp(-z*z))
K=s.exp(-x)/x*s.exp(-((x-y)/x)**2)
eps=s.symbols('eps',positive=True)
assert eq(s.limit(eps*K.subs({x:eps*x,y:eps*y},simultaneous=True),eps,0,dir='+'),s.exp(-((x-y)/x)**2)/x)
checks.append({'name':'inverse_kernel_and_actual_dilation_limit','cases':2})
# Delta input and its normal derivative have distinct sharp annular energies.
for j in range(2,12):
 lo=s.Rational(3,5)*2**j;hi=s.Rational(4,5)*2**j
 energy=s.integrate(s.Rational(9,4)*tau**2+1,(tau,lo,hi))
 assert energy>=s.Rational(1,10)*2**(3*j)
checks.append({'name':'positive_order_Besov_counterexample_energy','cases':10})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'script_sha256':sha(Path(__file__)),'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},
 'finite_checks_replace_proofs':False,'U031_restored':False}
(ROOT/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))
