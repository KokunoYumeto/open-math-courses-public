"""Exact algebraic and rational checks for the complete operator estimates."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent;source=HERE/'nirenberg-treves-estimates-and-square-root-commutators.md'
rows=[]
def exact(name,l,r=0):
 d=S.expand(l-r)
 if isinstance(d,S.MatrixBase):ok=all(S.simplify(v)==0 for v in d)
 else:ok=S.simplify(d)==0
 assert ok,name
 rows.append({'name':name,'kind':'exact_identity','passed':True})
def inequality(name,v):
 assert bool(v),name
 rows.append({'name':name,'kind':'exact_rational_inequality','passed':True})
x,y,t,r,lam=S.symbols('x y t r lambda',real=True)
aa,bb,T,M,Q,F,U,L=S.symbols('a0 a1 T M Q F U L',positive=True)
exact('arctangent quartic primitive',S.diff(S.atan((y-1/y)/S.sqrt(2)),y),S.sqrt(2)*(1+y*y)/(1+y**4))
upper=S.sqrt(t)*(1+S.I)/S.sqrt(2)*(1/(lam-S.I*t)-S.I/t)
lower=S.sqrt(t)*(1-S.I)/S.sqrt(2)*(1/(lam+S.I*t)+S.I/t)
exact('paired resolvent integrand',upper+lower,S.sqrt(2)*(lam*S.sqrt(t)+lam**2/S.sqrt(t))/(lam**2+t**2))
for j in range(5):
 n=7
 lhs=sum(S.prod(k-i for i in range(j))/S.prod(n-i for i in range(j))*S.binomial(n,k)*x**k*(1-x)**(n-k) for k in range(n+1))
 exact(f'Bernstein monomial identity degree {j}',lhs,x**j)
n=7
exact('Bernstein mean',sum(S.Rational(k,n)*S.binomial(n,k)*x**k*(1-x)**(n-k) for k in range(n+1)),x)
exact('Bernstein variance',sum((S.Rational(k,n)-x)**2*S.binomial(n,k)*x**k*(1-x)**(n-k) for k in range(n+1)),x*(1-x)/n)
c=[S.Rational(1,2)]
for k in range(2,9):c.append(S.Rational(2*k-3,2*k)*c[-1])
g=1-sum(v*x**(i+1) for i,v in enumerate(c))
for k in range(1,9):exact(f'square-root series coefficient {k}',S.expand(g*g-1+x).coeff(x,k))
split=2/S.pi*(2*aa*S.sqrt(r)+bb/S.sqrt(r))
exact('optimized resolvent split',split.subs(r,bb/(2*aa)),4*S.sqrt(2)/S.pi*S.sqrt(aa*bb))
exact('double commutator constant',(4*S.sqrt(2)/S.pi)**2,32/S.pi**2)
lowerpi=sum(S.Rational((-1)**j,2*j+1) for j in range(26))
inequality('exact lower bound for pi over four',lowerpi>S.Rational(31,40))
inequality('pi-squared rational comparison',S.Rational(961,100)>S.Rational(48,5))
A,B,V=S.symbols('A B V',commutative=False)
comm=lambda a,b:a*b-b*a
exact('symmetric square factorization',(A*V*V+V*V*A)/2,V*A*V+comm(comm(A,V),V)/2)
exact('Jacobi residual',comm(B,comm(A,V))-comm(comm(B,A),V),comm(A,comm(B,V)))
exact('first energy error constant',2*T*(M/3)*S.Rational(3,2),T*M)
exact('solution estimate denominator',2*T/(S.Rational(1,2)-T*M),4*T/(1-2*T*M))
exact('retained energy square completion',Q**2+T*T*L*(3*F+M*U)**2-T*S.sqrt(L)*Q*(6*F+2*M*U),(Q-T*S.sqrt(L)*(3*F+M*U))**2)
exact('final eighteen-two bound',18*F*F+2*M*M*U*U-(3*F+M*U)**2,(3*F-M*U)**2)
b=S.diag(-1,1);a=S.Matrix([[1,r],[r,1]])
exact('matrix first commutator',comm(b,a),S.Matrix([[0,-2*r],[2*r,0]]))
exact('matrix second commutator',comm(b,comm(b,a)),S.Matrix([[0,4*r],[4*r,0]]))
for sign,root in [('+',S.diag(0,1)),('-',S.diag(1,0))]:
 exact('matrix root double commutator '+sign,comm(comm(a,root),root),S.Matrix([[0,r],[r,0]]))
for val in [S.Rational(1,16),S.Rational(1,4),S.Rational(1,2),S.Integer(1)]:
 inequality('fourth-power double-root bound at '+str(val),val**4<=S.Rational(10,3)**4*(1+val)*(2*val)**2*(4*val))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,'checks':rows,'scope':'Exact polynomial, resolvent, commutator and energy identities, rational constant comparisons and matrix examples. The full infinite-dimensional calculus and analytic bounds are proved in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))
