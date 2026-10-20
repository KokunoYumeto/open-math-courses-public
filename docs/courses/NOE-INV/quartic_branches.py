"""Finish the exact singular-quartic elimination and check the flexes."""
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parent/'quartic-certificates'
A,B,D,E,x,y,z=s.symbols('A B D E x y z')
local={str(t):t for t in (A,B,D,E)}
data=json.loads((root/'case-2.1.json').read_text())
p=[s.fraction(s.sympify(data['values'][n],locals=local))[0]
   for n in ('I9','I12','I15','I18')]
out={}
first=[s.expand(q.subs({A:-s.Rational(3,2),E:-s.Rational(3,2)})) for q in p]
g1=s.groebner(first,D,B,order='lex')
print('First branch',g1,flush=True)
out['first_branch_basis']=[str(q) for q in g1.polys]
relation=4*A*A-6*A+9
second=[s.expand(q.subs(E,s.Rational(3,2)-A)) for q in p]+[relation]
g2=s.groebner(second,D,B,A,order='lex')
print('Second branch',g2,flush=True)
out['second_branch_basis']=[str(q) for q in g2.polys]
F=x*y*z*z+(x**3+y**3)*z+A*y**4+B*x*y**3-s.Rational(9,2)*x*x*y*y+D*x**3*y+E*x**4
L1=3*x+3*y-2*z
Q1=2*x**3+3*x*x*y+3*x*y*y+2*y**3+2*x*y*z
assert s.expand(F.subs({A:-s.Rational(3,2),E:-s.Rational(3,2),B:-s.Rational(15,4),D:-s.Rational(15,4)})+L1*Q1/4)==0
assert s.expand(Q1.subs(z,s.Rational(3,2)*(x+y))-2*(x+y)**3)==0
assert [s.diff(Q1,t).subs({x:-1,y:1,z:0}) for t in (x,y,z)]==[3,3,-2]
L2=x+(2*A/3-1)*y+4*A*z/9
Q2=x**3+(A-s.Rational(3,2))*x*x*y-A*x*y*y+y**3+x*y*z
def rem(q):
    return s.rem(s.Poly(s.expand(q),A),s.Poly(relation,A)).as_expr()
assert rem(F.subs({E:s.Rational(3,2)-A,B:s.Rational(15,4)-5*A/2,D:5*A/2})-(s.Rational(3,2)-A)*L2*Q2)==0
P={x:1-2*A/3,y:1,z:0}
assert rem(Q2.subs(P))==0 and rem(L2.subs(P))==0
gradient=[rem(s.diff(Q2,t).subs(P)) for t in (x,y,z)]
print('Second flex gradient',gradient,flush=True)
constant=rem(gradient[0])
assert all(rem(gradient[i]-constant*s.diff(L2,t))==0 for i,t in enumerate((x,y,z)))
# On L2=0, solve for z using 1/A=(6-4*A)/9.
zline=-(6-4*A)/4*(x+(2*A/3-1)*y)
restriction=rem(Q2.subs(z,zline))
assert rem(restriction-(x+(2*A/3-1)*y)**3)==0
out.update(first_factorization=str(-L1*Q1/4),second_factorization=str((s.Rational(3,2)-A)*L2*Q2),
           second_flex_point=[str(P[t]) for t in (x,y,z)],second_flex_gradient=[str(t) for t in gradient],
           second_line_restriction=str(restriction),all_factor_and_flex_checks=True)
(root/'case-2.1-branches.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8',newline='\n')
