"""Exact packing geometry and norm identities; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
P=Path(__file__).resolve();ROOT=P.parent;rows=[]
def check(name,condition):
 assert bool(condition),name
 rows.append({'name':name,'passed':True})
j=s.symbols('j',integer=True,positive=True)
mu=lambda j:s.Rational(1,10)/(j+1)**2
c=lambda j:1/(j+1)
center=lambda j:1/(j+1)
ratio=s.simplify((mu(j)+mu(j+1))/(center(j)-center(j+1)))
check('exact consecutive ratio',s.simplify(ratio-s.Rational(1,10)*((j+2)/(j+1)+(j+1)/(j+2)))==0)
check('maximum consecutive ratio at first index',ratio.subs(j,1)==s.Rational(13,60))
check('uniform ratio upper bound',s.expand(s.together(s.Rational(13,60)-ratio-(j-1)*(j+4)/(60*(j+1)*(j+2))).as_numer_denom()[0])==0)
for i in range(1,7):
 z=s.Rational(1,i+1);r=s.Rational(1,10*(i+1)**2)
 zn=s.Rational(1,i+2);rn=s.Rational(1,10*(i+2)**2)
 check(f'disjoint interval pair {i}',z-r>zn+rn>0)
check('first radius sum',mu(s.Integer(1))+mu(s.Integer(2))==s.Rational(13,360))
check('second radius sum',mu(s.Integer(2))+mu(s.Integer(3))==s.Rational(5,288))
for d in [1,2,3]:
 q=s.symbols('q',positive=True)
 check(f'Jacobian norm cancellation d={d}',s.simplify(q**(-d)*q**d)==1)
 for k in [0,2]:
  left=(j+1)*mu(j)**(-s.Rational(d,2)-k)
  right=10**(s.Rational(d,2)+k)*(j+1)**(1+d+2*k)
  check(f'kernel derivative factor d={d} k={k}',s.simplify(left-right)==0)
check('two-mode squared Cauchy constant',s.Rational(1,4)+s.Rational(1,9)==s.Rational(13,36))
check('two-mode equality ratio',4*s.Rational(1,4)**2+9*s.Rational(1,9)**2==s.Rational(13,36))
check('two-mode sharp equality',(s.sqrt(13)/6)**2==s.Rational(1,4)+s.Rational(1,9))
x=s.symbols('x',positive=True)
check('weight integral bound',s.integrate(x**-2,(x,1,s.oo))==1)
a=s.symbols('a',real=True)
f=1+2*s.cos(a)+3*s.sin(2*a)
expected={0:1,1:1,-1:1,2:-3*s.I/2,-2:3*s.I/2,3:0}
coeff={n:s.simplify(s.integrate(s.expand_trig(f)*s.exp(-s.I*n*a),(a,-s.pi,s.pi))/(2*s.pi)) for n in expected}
check('exact periodic Fourier coefficients',all(s.simplify(coeff[n]-expected[n])==0 for n in expected))
check('exact finite Fourier reconstruction',s.simplify(s.expand_complex(sum(v*s.exp(s.I*n*a) for n,v in coeff.items()))-f)==0)
out={'passed':True,'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,
 'source_sha256':hashlib.sha256((ROOT/'fixed-source-tests-by-residual-packing.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'scope':'Exact interval separation and sums, Jacobian and derivative factors, two-mode sharp norm identity, summable-weight bound and periodic Fourier example. Full residual convergence and operator estimates are proved in the lesson.',
 'cases':rows}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:out[k] for k in ['passed','total_cases','exact_algebraic_checks']}))
