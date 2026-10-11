"""Exact finite algebra for SW; full analytic proofs are in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def eq(name,e):
    assert s.simplify(e)==0,(name,e)
    checks.append(name)
def positive(name,e):
    assert s.simplify(e)>0,(name,e)
    checks.append(name)
Q=s.Rational
eq('frequency exponent in commutator',Q(5,6)-Q(1,3)-Q(2,3)+Q(1,6))
eq('Airy bracket exponent in commutator',-Q(3,4)+Q(1,4)+Q(1,2))
eq('three moderate weight losses',Q(5,6)+Q(2,3)+Q(1,4)-Q(7,4))
eq('full Fourier majorant exponent',1+Q(7,4)-Q(11,4))
eq('coarse Sobolev square weight',Q(2,3)+Q(1,3)-1)
mu,lam,q=s.symbols('mu lam q',positive=True)
sigma=Q(2,3)*mu**Q(3,2)*lam**Q(-1,2)
eq('mu phase derivative',s.diff(sigma,mu)-s.sqrt(mu/lam))
eq('lambda phase derivative',s.diff(sigma,lam)+(mu/lam)**Q(3,2)/3)
eq('homogeneous Euler identity',mu*s.diff(sigma,mu)+lam*s.diff(sigma,lam)-sigma)
v=s.symbols('v',nonnegative=True)
norm2=v+v**3/9
eq('squared displacement',s.sqrt(v)**2+(-v**Q(3,2)/3)**2-norm2)
eq('monotone displacement derivative',s.diff(norm2,v)-(1+v**2/3))
eq('first endpoint coordinate',s.sqrt(Q(1,16))-Q(1,4))
eq('second endpoint coordinate',-Q(1,16)**Q(3,2)/3+Q(1,192))
eq('exact endpoint norm',norm2.subs(v,Q(1,16))-Q(2305,192**2))
positive('strict rational norm bound',Q(13,50)**2-Q(2305,192**2))
x,d=s.symbols('x d',real=True)
f=x**3+2*x
translated=(s.exp(-x**2)*f.subs(x,x+d)).subs(x,x-d)
eq('exact transported cutoff',translated-s.exp(-(x-d)**2)*f)
eq('left translated support extremum',-1-Q(1,4)+Q(5,4))
eq('right translated support extremum',1+Q(1,4)-Q(5,4))
eq('observation support margin',Q(3,2)-Q(5,4)-Q(1,4))
action=Q(2,3)*lam*((q+mu/lam)**Q(3,2)-(mu/lam)**Q(3,2))
eq('boundary action cancellation',action.subs(q,0))
eq('boundary input derivative cancellation',s.diff(action,mu).subs(q,0))
eq('boundary frequency derivative cancellation',s.diff(action,lam).subs(q,0))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
     'checks':checks,'source_sha256':sha(root/'recovering-the-stable-weight-of-actual-airy-solutions.md'),
     'script_sha256':sha(Path(__file__)),'scope':'Exact weight exponents, phase derivatives, support transport, displacement bound and boundary cancellations. The analytic estimates are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps(out))
