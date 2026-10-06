"""Finite checks of normal-extension signs and ordered boundary terms.

These symbolic and discrete models verify conventions; they do not replace
the full distributional proofs in the accompanying component.
CC0, AN-04 course-writing task and OpenAI Codex, 5 October 2026.
"""
from pathlib import Path
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parent
x,t,z=s.symbols('x t z',real=True);I=s.I
D=lambda p:s.diff(p,t)*(-I)
Dx=lambda p,k=1:s.diff(p,x,k)*(-I)**k
def zero(p):
 if isinstance(p,s.MatrixBase):return all(s.expand(q)==0 for q in p)
 return s.expand(p)==0
checks=[]
# Weighted primitive: the full product rule is checked at positive normal
# orders, including tangential derivatives and its -ia term.
phi=(1+x)**8*(1+t+t**3+t**7)
psi=I*s.integrate(phi,(t,0,t))
for a in range(1,7):
 for b in range(4):
  w=t**a*(-I)**a*s.diff(Dx(psi,b),t,a)
  rhs=t**a*(-I)**(a-1)*s.diff(Dx(phi,b),t,a-1)
  assert zero(w-rhs)
  expected=t**a*(-I)**a*s.diff(Dx(phi,b),t,a)-I*a*t**(a-1)*(-I)**(a-1)*s.diff(Dx(phi,b),t,a-1)
  assert zero(D(w)-expected)
checks.append({'name':'full_weighted_primitive_and_minus_i_a_term','cases':24})
# The operator i integral_0^t has bilinear transpose +i reversed integral
# and Hilbert adjoint -i reversed integral.
v=1+I*t+t**2;g=2-I*t+t**3
Jv=I*s.integrate(v,(t,0,t))
bil=s.integrate(Jv*g,(t,0,1))
reverse=I*s.integrate(g,(t,z,1))
assert s.simplify(bil-s.integrate(v.subs(t,z)*reverse,(z,0,1)))==0
hil=s.integrate(Jv*s.conjugate(g),(t,0,1))
adj=-I*s.integrate(g,(t,z,1))
assert s.simplify(hil-s.integrate(v.subs(t,z)*s.conjugate(adj),(z,0,1)))==0
checks.append({'name':'bilinear_transpose_and_Hilbert_adjoint_signs','cases':2})
# A concrete two-component GE9 model, with a finite-smooth cutoff sufficient
# for this single integration by parts. Its coefficients are not diagonal.
u=s.Matrix([1+t+t**2,I+t**3])
A=s.Matrix([[t,1+I*t],[1-t,t**2]])
f=D(u)+A*u
phi=s.Matrix([t**2*(1-t)**2,(1+I*t)*t**2*(1-t)**2])
ps0=I*phi.applyfunc(lambda a:s.integrate(a,(t,0,t)))
ps1=ps0.subs(t,1)
chi=1-3*(t-1)**2+2*(t-1)**3
dot=lambda a,b:(a.T*b)[0]
rhs0=-dot(f,ps0)+dot(u,A.T*ps0)
rhs1=-dot(f,chi*ps1)+dot(u,A.T*(chi*ps1)-D(chi)*ps1)
assert s.simplify(s.integrate(dot(u,phi),(t,0,1))-s.integrate(rhs0,(t,0,1))-s.integrate(rhs1,(t,1,2)))==0
checks.append({'name':'first_order_bilinear_equation_with_actual_cutoff','cases':1})
# Distribution delta polynomials are dicts: derivative index -> coefficient.
def add(a,b):
 r=dict(a)
 for k,v in b.items():r[k]=s.expand(r.get(k,0*v)+v)
 return {k:v for k,v in r.items() if not zero(v)}
def deriv(a,k=1):return {j+k:(-I)**k*v for j,v in a.items()}
def mul(a,b):
 r={}
 for l,v in a.items():
  for q in range(l+1):
   val=(-1)**q*s.binomial(l,q)*s.diff(b,t,q).subs(t,0)*v
   r=add(r,{l-q:val})
 return r
for m in range(1,7):
 for mu in range(7):
  out=mul(deriv({mu:1},m),t**m)
  assert out=={mu:I**m*s.factorial(mu+m)/s.factorial(mu)}
  for j in range(m):
   low=mul(mul(deriv({mu:1},j),1+t+t**3),t**m)
   assert all(k<mu for k in low)
checks.append({'name':'weighted_delta_top_coefficient_and_all_lower_orders','cases':42})
# Verify every variable coefficient term against a test-function pairing.
b=1+(2+I)*t+3*t**2-t**4;h=2+t+t**2+t**5+t**8
for l in range(8):
 left=(-1)**l*s.diff(b*h,t,l).subs(t,0)
 right=sum(v*(-1)**k*s.diff(h,t,k).subs(t,0) for k,v in mul({l:1},b).items())
 assert s.simplify(left-right)==0
checks.append({'name':'complete_variable_coefficient_delta_product','cases':8})
# Independent iterative ambient differentiation of H*u versus the closed
# intrinsic-jet boundary defect, including matrices and tangential derivatives.
u=s.Matrix([(1+x)**9*(1+t+t**3+t**6),(1+x+x**8)*(I+t**2+t**5)])
for m in range(1,5):
 jets={};interior=u;normal=[({},u)]
 for j in range(1,m+1):
  jets=add(deriv(jets),{0:-I*interior.subs(t,0)})
  interior=D(interior);normal.append((jets,interior))
 actual={};closed={}
 for j in range(1,m+1):
  a=s.eye(2) if j==m else s.Matrix([[1+t,x+t**2],[I*t,x+1]])
  order=0 if j==m else 2*j+1
  for k,vj in normal[j][0].items():
   # Matrix coefficient multiplication is handled columnwise.
   dv=Dx(vj,order)
   for row in range(2):
    scalar={}
    for col in range(2):scalar=add(scalar,mul({k:dv[col]},a[row,col]))
    for l,val in scalar.items():
     vec=s.zeros(2,1);vec[row]=val;actual=add(actual,{l:vec})
  for r in range(j):
   vj=-I*(-I)**(j-1-r)*Dx((-I)**r*s.diff(u,t,r).subs(t,0),order)
   for row in range(2):
    scalar={}
    for col in range(2):scalar=add(scalar,mul({j-1-r:vj[col]},a[row,col]))
    for l,val in scalar.items():
     vec=s.zeros(2,1);vec[row]=val;closed=add(closed,{l:vec})
 assert all(zero(actual.get(k,s.zeros(2,1))-closed.get(k,s.zeros(2,1))) for k in set(actual)|set(closed))
 assert not mul(actual,t**m)
checks.append({'name':'ordered_matrix_boundary_defect_and_weighted_annihilation','cases':4})
# Finite nesting and signs of the monotone conormal inclusion for real
# requested indices, including negative orders and the no-iteration case.
for k0 in [-12.5,-4.25,-1.0]:
 for k in [-20.25,-5.0,0.125,10.75]:
  N=max(0,math.ceil(k-k0))
  collars=[1+(j+1)/(N+2) for j in range(N+1)]
  assert all(collars[j]<collars[j+1] for j in range(N))
  assert k0+N>=k and max(collars)<2
  for l in range(20):assert 2**(-l*(k0+N-k))<=1+1e-12
checks.append({'name':'finite_compact_nesting_and_conormal_inclusion_direction','cases':12})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},
 'finite_checks_replace_proofs':False,'U031_restored':False}
(ROOT/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))
