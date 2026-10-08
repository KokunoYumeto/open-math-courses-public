"""Finite independent checks of phases, model invariance and ordered errors."""
from pathlib import Path
import json,hashlib
import sympy as S
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=60
k,z,r,s=S.symbols('k z r s',real=True)
I=S.I
checks=[]

def subtraction(h,mu,length,scale=1):
 expansion=S.series(z**mu*h.subs(k,1/z),z,0,length).removeO().expand()
 coefficients=[expansion.coeff(z,j) for j in range(length)]
 u=[]
 for n in range(length):
  u.append(S.simplify(coefficients[n]-sum(S.binomial(mu-j,n-j)*u[j]*(I*scale)**(n-j) for j in range(n))))
 return S.cancel(h-sum(u[j]*(k+I*scale)**(mu-j) for j in range(length)))

def integrate(g):
 if g==0:return mp.mpc(0)
 fn=S.lambdify(k,g,'mpmath')
 return mp.quad(fn,[-mp.inf,-1,0,1,mp.inf])

for h,mu,expected in [(k/(k*k+1),-1,I*S.pi),(k**3/(k*k+1),1,-I*S.pi),(k*k,2,S.Integer(0))]:
 results=[]
 for scale,length in [(1,max(1,mu+2)),(2,max(1,mu+4))]:
  g=subtraction(h,mu,length,scale)
  result=integrate(g)
  target=mp.mpc(str(S.N(S.re(expected),65)),str(S.N(S.im(expected),65)))
  assert abs(result-target)<mp.mpf('1e-48'),(h,g,result,target)
  results.append(str(abs(result-target)))
checks.append({'name':'Absolutely integrated finite subtractions','passed':True,'cases':'odd reciprocal tail, cubic growth and pure polynomial','distinct_model_scales':[1,2],'lengths_changed':True})

M=1+3*r+5*r*r-r**3
normal_integrals={}
for v in range(5):
 h=k**v/(k*k+4);mu=v-2
 normal_integrals[v]=integrate(subtraction(h,mu,max(1,mu+2),2))/(2*mp.pi)
for order in range(5):
 actual=mp.mpc(0)
 for v in range(order+1):
  c=S.binomial(order,v)*(-I)**(order-v)*S.diff(M,r,order-v).subs(r,0)
  actual+=mp.mpc(str(S.N(S.re(c),65)),str(S.N(S.im(c),65)))*normal_integrals[v]
 expected=(-I)**order*S.diff(M*S.exp(-2*r)/4,r,order).subs(r,0)
 target=mp.mpc(str(S.N(S.re(expected),65)),str(S.N(S.im(expected),65)))
 assert abs(actual-target)<mp.mpf('1e-48'),(order,actual,target)
checks.append({'name':'Actual one-sided kernel derivatives','passed':True,'orders':[0,1,2,3,4],'variable_output_coefficient':str(M),'all_Leibniz_terms_retained':True})

A=S.Matrix([[1,1],[0,1]]);B=S.Matrix([[1,0],[1,1]])
assert A*B==S.Matrix([[2,1],[1,1]]) and A*B!=B*A
for n in [-2,0,2]:
 q=S.Rational(n+1,2)/S.sqrt(1+(n+1)**2)*A*B
 expected=S.integrate(S.Rational(n+1,1)/(k*k+1+(n+1)**2),(k,-S.oo,S.oo))/(2*S.pi)*A*B
 assert q==expected
assert S.Rational(1,2)/S.sqrt(2)*A*B!=S.zeros(2)
checks.append({'name':'Complete tangential Fourier shift and matrix order','passed':True,'input_modes':[-2,0,2],'pointwise_proxy_fails_at_zero':True})

P=S.Matrix([[2,1,0],[0,3,1],[1,0,2]])
Q=S.Matrix([[1,2,0],[0,1,1],[2,0,1]])/7
Qt=S.Matrix([[2,0,1],[1,3,0],[0,1,2]])/11
assert Q*P!=P*Q
actual=Q*(P*Qt-S.eye(3))-(Q*P-S.eye(3))*Qt
assert actual==Qt-Q
checks.append({'name':'Ordered difference with both error sides','passed':True,'matrix_size':3,'factors_do_not_commute':True})

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'AN04-one-sided-trace-symbols-models/v1','source_sha256':sha(ROOT/'one-sided-trace-symbols.md'),
 'script_sha256':sha(Path(__file__)),'passed':True,'general_theorem_certified':False,'checks':checks}
(ROOT/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_check_groups':len(checks),'quadrature_digits':mp.mp.dps}))
