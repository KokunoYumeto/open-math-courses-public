"""Finite packet, gauge and order checks. Analytic proofs are in the lesson."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
rho,m,n,N,k=s.symbols('rho m n N k',real=True)
delta=1-rho;eps=2*rho-1;q=m-n/4;M=m+n/4;a=q+delta*n/2
checks=[]
def eq(name,x,y):
 assert s.simplify(x-y)==0,(name,x,y)
 checks.append({'name':name,'passed':True})
eq('symbol versus annular order',q+n/2,M)
eq('Taylor division coefficient order',eps+delta,rho)
eq('vanishing-symbol integration order',q+eps+delta-rho,q)
eq('near test order',rho-delta,eps)
eq('graph cutoff frequency derivative',delta-1,-rho)
eq('physical versus cutoff tube separation',rho-delta,eps)
eq('unitary packet L2 normalization',rho*n/2-rho*n/2,0)
eq('Fourier packet height',M+rho*n/2-rho*n,a)
eq('packet L2 norm exponent',a+rho*n/2,M)
eq('packet pointwise height gap',a-q,delta*n/2)
eq('smaller-radius low tail exponent',M+rho*(N-n/2)+n/2-N,M-delta*(N-n/2))
eq('larger-radius high tail exponent',n/2+M-rho*n/2-delta*N,M-delta*(N-n/2))
eq('scaled Taylor derivative R power',-rho*(1+k)+rho+delta*k,-eps*k)
eq('frequency cell volume exponent',rho*n,2*(rho*n/2))
eq('normalized cell derivative',-q+rho*k-rho*n/2+q+rho*n/2-rho*k,0)
eq('annular bound leaves height gap',-q+rho*k-rho*n/2+M-rho*k,delta*n/2)
eq('actual Lagrangian order',a+n/4,m+delta*n/2)
for r in [s.Rational(3,5),s.Rational(3,4),s.Rational(9,10)]:
 assert (1-r)/2>0 and 2*r-1>0
 checks.append({'name':'strict height gap and positive calculus drop rho='+str(r),'passed':True})
eq('ordinary endpoint gap',delta.subs(rho,1)*n/2,0)
vals={rho:s.Rational(3,4),n:2,m:0}
for name,value,expected in [('X1 q',q,s.Rational(-1,2)),('X1 M',M,s.Rational(1,2)),
 ('X1 a',a,s.Rational(-1,4)),('X1 allowed cell exponent',q+rho*n/2,s.Rational(1,4)),
 ('X1 actual order',m+delta*n/2,s.Rational(1,4))]:
 eq(name,value.subs(vals),expected)
# Exact Fourier gauge in two coordinates with a nonzero cubic mixed derivative.
x,y=s.symbols('xi eta',positive=True);h=x**3+x*y**2;v=x**2*y+1
Q=lambda f,j:s.I*s.diff(f,j)-s.diff(h,j)*f
uh=s.exp(-s.I*h)*v
eq('nonlinear first gauge x',Q(uh,x),s.exp(-s.I*h)*s.I*s.diff(v,x))
eq('nonlinear first gauge y',Q(uh,y),s.exp(-s.I*h)*s.I*s.diff(v,y))
eq('nonlinear mixed gauge and commuting Q',Q(Q(uh,x),y),-s.exp(-s.I*h)*s.diff(v,x,y))
eq('nonlinear Q commutator',Q(Q(uh,x),y)-Q(Q(uh,y),x),0)
eq('exact illustrated R delta',s.Integer(65536)**s.Rational(1,4),16)
eq('exact illustrated R rho',s.Integer(65536)**s.Rational(3,4),4096)
eq('exact illustrated tube/packet width ratio',s.Integer(65536)**s.Rational(1,2),256)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(ROOT/'iterated-tests-and-frequency-packet-regularity.md'),
 'script_sha256':sha(Path(__file__)),
 'scope':'Exact finite scale, gauge, normalization and example identities. These checks do not prove all-test bounds, distributional convergence or the counterexample.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'cases':len(checks)}))
