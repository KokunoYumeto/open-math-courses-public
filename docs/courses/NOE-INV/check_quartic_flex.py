"""Check all coefficient reductions and their explicit null-cone weights."""
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parent/'quartic-certificates'
A,B,C,D,E,L,M,N=s.symbols('A B C D E L M N')
local={str(t):t for t in (A,B,C,D,E,L,M,N)}
def values(case):
    r=json.loads((root/('case-'+case+'.json')).read_text())
    return {n:s.sympify(v,locals=local) for n,v in r['values'].items()}
p=values('1.1')
assert s.factor(p['I6'].subs(A,-L**2/6))==-5*L**4/s.Integer(746496)
p=values('1.2')
assert p['I3']==A/12 and p['I6']==C/20736
assert p['I15'].subs({A:0,C:0})==1125*D**2/s.Integer(165112971264)
assert s.factor(p['I18'].subs({A:0,C:0,D:0,E:-s.Rational(89,65)*B**2}))==6251*B**4/s.Integer(114831654912)
p=values('2.2')
assert s.factor(p['I12'].subs({A:0,C:0}))==-B**2*(3*B-D**2)/s.Integer(26873856)
assert s.factor(p['I18'].subs({A:0,C:0,E:0}))==-139968*B**3*D*(9*B+D**2)/s.Integer(8666449635704832)
numerator=s.expand(p['I12']*34828517376)
reduced=s.expand(numerator.subs({C:0,E:0})).subs(A**2,s.Rational(42,125)*B**2*D).subs(B,s.Rational(2,45)*D**2)
assert s.expand(reduced)==-s.Rational(5216,375)*D**6
p=values('2.3')
assert s.factor(p['I12'].subs({C:0,E:0}))==B**2*D**2/s.Integer(26873856)
weights={'triple_at_z':([1,1,-2],[(3,0,1),(2,1,1),(1,2,1),(0,3,1),(4,0,0),(3,1,0),(2,2,0),(1,3,0),(0,4,0)]),
         'double_line_flex':([4,-1,-3],[(2,0,2),(2,1,1),(3,0,1),(1,3,0),(2,2,0),(3,1,0),(4,0,0)]),
         'cuspidal_cubic_times_line':([-3,-1,4],[(2,0,2),(0,3,1)]),
         'triple_at_y':([1,-2,1],[(1,1,2),(3,0,1),(3,1,0),(4,0,0)])}
for name,(w,monomials) in weights.items():
    assert sum(w)==0 and all(sum(a*b for a,b in zip(w,e))>0 for e in monomials)
(root/'nullcone-reductions.json').write_text(json.dumps({'exact_coefficient_reductions':True,'positive_weights':weights},indent=2)+'\n',encoding='utf8',newline='\n')
print('All four short reductions and explicit positive weights passed.')
