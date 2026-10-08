"""Check exact errors, nonorthogonal inverse factors, ranks and ordered powers."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
e=s.symbols('e',positive=True);I=s.eye(2);zero=s.zeros(2)
checks=[]
C=s.diag(1+e,e);B=s.Matrix([[1,0]])
D=C*C-C;T=s.Matrix([1/(1+e)**2,0]);S=C*T
Tp=s.Matrix([1,0]);Tpp=s.diag(0,1/(1-e));Spp=Tpp*(I-C)
R0=I-S*B-Spp;R1=R0+Spp*C
assert s.simplify(B*C*S)==s.ones(1)
assert s.simplify(Tp*B+Tpp*(I-C))==I
assert s.simplify(C*S-S-D*T)==s.zeros(2,1)
assert s.simplify(Spp*C+Tpp*D)==zero
assert s.simplify(S*B+Spp*(I-C)+R1)==I
assert s.simplify(R1-s.diag(e/(1+e),e))==zero
z=s.symbols('z',positive=True);eps=z/(2*s.sqrt(1+z*z))
assert s.limit(eps/z,z,0)==s.Rational(1,2)
assert s.limit(eps/(1+eps)/z,z,0)==s.Rational(1,2)
checks.append({'name':'Every actual retained error and the sharp non-smoothing coefficient','passed':True})
q=s.Matrix([[1,-2],[0,0]]);b=s.Matrix([[1,3]]);c=b*q
t=c.T*(c*c.T).inv();stable=q*t
ell=b.col_join(I-q);left=(ell.T*ell).inv()*ell.T
assert q*q==q and t==s.Matrix([s.Rational(1,5),-s.Rational(2,5)])
assert c*t==s.ones(1) and b*t==-s.ones(1) and b*stable==s.ones(1)
assert left*ell==I and left[:,0]==stable
assert left[:,1:]*(I-q)==I-stable*b
r=s.symbols('r',positive=True);Da=s.diag(1,r);Db=r**s.Rational(5,2)
qw=Da*q*Da.inv();bw=Db*b*Da.inv();sw=Da*stable/Db
assert s.simplify(qw*qw-qw)==zero
assert s.simplify(qw*sw-sw)==s.zeros(2,1)
assert s.simplify(bw*sw)==s.ones(1)
checks.append({'name':'Nonorthogonal stable inverse and fractional weighted frame restoration','passed':True})
q3=s.diag(1,1,0);b3=s.Matrix([[1,0,0]]);ell3=b3.col_join(s.eye(3)-q3)
assert (b3*q3).rank()==1 and ell3.rank()==2 and ell3*s.Matrix([0,1,0])==s.zeros(4,1)
q2=s.diag(1,0);b2=s.diag(1,0);ell2=b2.col_join(I-q2)
assert (b2*q2).rank()==1 and ell2.rank()==2
checks.append({'name':'Independent onto and injective conditions with exact kernels and ranks','passed':True})
M=s.Matrix([[1,0],[2,1]]);E=e*s.Matrix([[1,2],[0,1]])
A=(I-E)*M.inv();Al=M.inv()*(I-E)
for L in range(1,6):
    powers=sum((E**j for j in range(L)),s.zeros(2))
    assert s.expand(A*M*powers-I+E**L)==zero
    assert s.expand(powers*M*Al-I+E**L)==zero
assert s.expand(A*(I+E)*M-I+E**2)!=zero
weights=[s.Rational(0),s.Rational(1),s.Rational(2)]
targets=[s.Rational(0),s.Rational(5,2),s.Rational(7)]
sigma=s.symbols('sigma');count=0
for a in weights:
 for beta in targets:
    assert s.expand((sigma-beta-s.Rational(1,2))-(a-beta)-(sigma-a-s.Rational(1,2)))==0
    count+=1
for a in weights:
 for k in weights:
    assert s.expand((sigma-a-s.Rational(1,2))-(k-a-1)-(sigma+1-k-s.Rational(1,2)))==0
    count+=1
checks.append({'name':'Both finite noncommuting correction orders and original Sobolev entry exponents','passed':True,'correction_lengths':5,'weight_cases':count})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(root/'weighted-boundary-inverse.md'),'script_sha256':sha(Path(__file__)),'passed':True,'checks':checks,'finite_checks_do_not_replace_general_proofs':True}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'weight_cases':count}))
