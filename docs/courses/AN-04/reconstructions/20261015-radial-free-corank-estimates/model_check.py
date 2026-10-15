"""Finite identities only; the uniform analytic proofs are in the lesson."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,itertools
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
    assert condition,name
    checks.append({'name':name,'passed':True})
for n,a,b,N in [(0,1,1,2),(1,1,0,3),(2,2,3,5),(0,2,3,4),(3,0,0,3)]:
    d=2*n+a+b;k=a+b
    check(f'partial normalization n={n},a={a},b={b},N={N}',
          -F(d+2*N,4)+F(N+n,2)-n==-n-F(k,4))
    output=-F(k,4)+F(b,3)+F(n,4)+F(a,6)
    input_=F(n,4)+F(b,6)
    check(f'two Jacobians n={n},a={a},b={b}',output-input_==-F(k,12))
for shared_count in range(4):
    weight=shared_count*F(1,2)+(3-shared_count)*F(1,3)
    check(f'cubic weight {shared_count} shared',weight-1==(F(0) if shared_count==0 else F(shared_count,6)))
check('fourth remainder weight',4*F(1,3)-1==F(1,3))
for r in [1,2,3]:
    I=s.eye(r);Z=s.zeros(r)
    J=Z.row_join(I).col_join((-I).row_join(Z))
    Q=s.diag(*range(1,r+1))
    L=I.row_join(Z).col_join(Q.row_join(I))
    U=I.row_join(-Q).col_join(Z.row_join(I))
    check(f'Fourier shear sign dimension {r}',J.inv()*L*J==U)
    A=s.eye(r)
    for j in range(r-1):A[j,j+1]=1
    P=s.diag(*range(2,r+2));E=s.diag(*range(3,r+3))
    lower=I.row_join(Z).col_join(P.row_join(I))
    diag=A.row_join(Z).col_join(Z.row_join(A.inv().T))
    upper=I.row_join(E).col_join(Z.row_join(I))
    S=lower*diag*upper
    aa=S[:r,:r];bb=S[:r,r:];cc=S[r:,:r];dd=S[r:,r:]
    check(f'symplectic product dimension {r}',S.T*J*S==J)
    check(f'block factorization dimension {r}',
          cc*aa.inv()==P and aa.inv()*bb==E and dd==cc*aa.inv()*bb+aa.inv().T)
R,t=s.symbols('R t',positive=True); f=s.Function('F')(t)
x=f-t*s.diff(f,t);y=-s.diff(f,t)
check('closed example primitive',s.simplify(R*s.diff(x,t)-R*t*s.diff(y,t))==0)
check('closed example form coefficient',s.simplify(s.diff(x,t)+t*s.diff(f,t,2))==0)
X,Y,h=s.symbols('X Y h',positive=True)
check('zero-shared-block cubic',s.simplify((h**F(1,3)*X)**2*(h**F(1,3)*Y)/h-X**2*Y)==0)
for a,b in [(1,1),(0,2),(2,0),(3,4)]:
    k=a+b
    check(f'necessary line k={k}',-F(k,4)+F(k,6)==-F(k,12))
for length in [1,2,5,9]:
    # Every coordinate is in at most 3 enlarged input and 5 output intervals.
    js=range(length)
    input_max=max(sum(abs(p-j)<=1 for j in js) for p in range(-2,length+2))
    output_max=max(sum(abs(p-j)<=2 for j in js) for p in range(-3,length+3))
    check(f'finite overlaps {length}',input_max<=3 and output_max<=5)
source=ROOT/'corank-estimates-without-radial-restrictions.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'schema':'AN04-radial-free-corank-finite-checks/v1','passed':True,
 'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'scope':'Exact finite normalization, symplectic, cubic, Jacobian and overlap identities; no analytic certification.',
 'analytic_proof_established_by_finite_checks':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
