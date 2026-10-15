"""Exact finite examples; the analytic estimates are proved in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def eq(name,a,b):
    assert s.simplify(a-b)==0,(name,a,b)
    checks.append({'name':name,'passed':True})
rho,m,n,a,b,q=s.symbols('rho m n a b q',real=True)
delta=1-rho;eps=2*rho-1
eq('Taylor quotient plus frequency derivative',m+delta-rho,m-eps)
eq('graph density order',m+2*n/4-n/2,m)
eq('graph adjoint product order',m+(-m),0)
eq('Sobolev graph reduction',(q-m)+m-q,0)
eq('partial ambient dimension',(n+a)+(n+b),2*n+a+b)
eq('partial amplitude order',m+((n+a)+(n+b)-2*n)/4,m+(a+b)/4)
eq('partial Fourier normalization',-((n+a)+(n+b)+2*n)/4,-n-(a+b)/4)
eq('parameter normalization ratio',n-((n+a)+(n+b)+2*n)/4,-(a+b)/4)
eq('corank reduced order',(q-m-(a+b)/4)+m-q,-(a+b)/4)
for r in [s.Rational(3,5),s.Rational(3,4),s.Integer(1)]:
    eq('metric uncertainty rho='+str(r),r-(1-r),2*r-1)
    eq('scaled base derivative rho='+str(r),-(1-r)+(1-r),0)
    eq('scaled frequency derivative rho='+str(r),r-r,0)
eq('lifting amplitude order',s.Rational(-1,4)+(3-2)/s.Integer(4),0)
eq('lifting normalization',s.Rational(-5,4)+s.Rational(1,4),-1)
eq('circle-family amplitude order',s.Rational(-1,2)+(4-2)/s.Integer(4),0)
eq('circle-family normalization',s.Rational(-3,2)+s.Rational(1,2),-1)
eq('circle-family graph norm factor',s.Rational(-2,4)+s.Rational(1,2),0)
U=s.Matrix([[0,1],[0,0]]);V=s.Matrix([[0,0],[1,0]])
assert U*V==s.diag(1,0) and V*U==s.diag(0,1)
checks.append({'name':'ordered noncommuting projection ranges','passed':True})
rho0=s.Rational(3,4);r0=s.Integer(16)
eq('metric box base half-width',r0**(-(1-rho0)),s.Rational(1,2))
eq('metric box frequency half-width',r0**rho0,8)
x=s.symbols('x',positive=True)
err=1/s.log(2+s.sqrt(1+(x+1)**2))
assert s.simplify(s.diff(err,x)) .is_negative
checks.append({'name':'exact compact approximation error strictly decreases','passed':True})
assert s.limit(err,x,s.oo)==0
checks.append({'name':'exact compact approximation error tends to zero','passed':True})
# Noncommutative inverse comparison uses free ordered words.
B,A,C=s.symbols('B A C',commutative=False)
assert s.expand(B*(1-A*C)+(B*A-1)*C)==B-C
checks.append({'name':'left-right inverse comparison sign and order','passed':True})
source=ROOT/'general-symbol-graph-and-corank-continuity.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'numerical_checks':0,'checks':checks,'source_sha256':sha(source),
        'script_sha256':sha(Path(__file__)),
        'scope':'Finite order, normalization, scale, inverse and explicit example identities only; no certification of analytic proofs.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'cases':len(checks)}))
