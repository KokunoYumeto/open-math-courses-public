"""Finite exact checks of orders and the outgoing Weyl identity; not an analytic proof."""
from pathlib import Path
import json,hashlib
import sympy as S
root=Path(__file__).resolve().parent
t,z,e,s,nu=S.symbols('t z e s nu',real=True)
cases=[]
def eq(name,lhs,rhs):
 assert S.simplify(lhs-rhs)==0,(name,lhs,rhs)
 cases.append({'name':name,'passed':True,'kind':'exact symbolic identity'})
def weyl(a,b,N=4):
 return S.expand(sum((1/(2*S.I))**j/S.factorial(j)*sum((-1)**l*S.binomial(j,l)*S.diff(a,z,j-l,t,l)*S.diff(b,t,j-l,z,l) for l in range(j+1)) for j in range(N+1)))
k=1-2*e;b=s+(3*e-1)/2
eq('Planck inverse square order',2*k,2-4*e)
eq('positivity real remainder',1-2*k,-1+4*e)
eq('mixed first commutator',s+1-(1-e),s+e)
eq('mixed second commutator',s+1-2*(1-e),s-1+2*e)
eq('left regularizer error',s-(1-e),s-1+e)
eq('regularizer error commutator',s-1+e+1-(1-e),s-1+2*e)
eq('adjoint correction order',s-k,s-1+2*e)
eq('symmetric form order',s+(s+e)-k,2*b)
eq('real-part weak margin',b-(s-1+e),(1+e)/2)
eq('outgoing weak margin',b-(s-1),(1+3*e)/2)
eq('fixed regularizer solution domain',b-s+2,(3+3*e)/2)
eq('fixed regularizer forcing domain',b-1-s+2,(1+3*e)/2)
for v in [S.Rational(0),S.Rational(1,4)]:
 eq('positivity endpoint '+str(v),(1-2*k).subs(e,v),-1+4*v)
 eq('weak endpoint '+str(v),(b-s).subs(e,v),(3*v-1)/2)
r=S.Function('r')(z)
eq('affine outer multiplication',weyl(weyl(t,r*r),t),t*t*r*r+S.diff(r*r,z,2)/4)
eq('equal outer multipliers',weyl(weyl(r,t*t),r),t*t*r*r+S.diff(r,z)**2/2-r*S.diff(r,z,2)/2)
eq('outgoing difference',weyl(weyl(t,r*r),t)-weyl(weyl(r,t*t),r),r*S.diff(r,z,2))
rv=1/(1+nu*z*z)
eq('regularizer second derivative',S.diff(rv,z,2),2*nu*(3*nu*z*z-1)/(1+nu*z*z)**3)
eq('nonzero outgoing correction at zero',(rv*S.diff(rv,z,2)).subs(z,0),-2*nu)
q,f=S.symbols('q f',real=True)
eq('real leading symbol cancellation',S.re(-S.I*q*f),0)
out={'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,'all_passed':True,'cases':cases,'scope':'Finite identities, order arithmetic and exact affine Weyl products. Analytic symbol estimates, domains, support localization and convergence are proved in the lesson.','source_sha256':hashlib.sha256((root/'shrinking-cutoffs-and-left-regularized-energy.md').read_bytes()).hexdigest()}
out.update(passed=True,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:out[k] for k in ['total_cases','exact_algebraic_checks','all_passed']}))
