"""Exact finite sign/scale checks; general proofs are in the two companions."""
from pathlib import Path
import hashlib,json
import sympy as s
MOD=Path(__file__).resolve().parent
checks=[]
eta,xi,x,y=s.symbols('eta xi x y',real=True)
q=(1+eta**2)**s.Rational(1,4)
z=q*(x-y);theta=(xi-eta)/q
v=z*z+z*theta+3*theta*theta
Lv=2*z*z-6*theta*theta
F=s.diff(q,eta)/q
assert s.simplify(s.diff(v,xi)+s.diff(v,eta)-F*Lv)==0
assert s.simplify(F-eta/(2*(1+eta**2)))==0
assert s.simplify(s.diff(v,x)+s.diff(v,y))==0
checks.append({'name':'Moving-scale derivative identities','passed':True,'scope':'Exact first-variable derivative, frequency sum and dilation operator for a quadratic probe; general Schwartz estimates use the written proof.'})
Q=s.symbols('Q',positive=True);X,Y,Eta,Xi=s.symbols('X Y Eta Xi',real=True)
mat=s.Matrix([Q*(Y-X),(Eta-Xi)/Q]).jacobian([Y,Eta])
assert mat.det()==1
r=s.symbols('r',real=True)
assert s.simplify((r+2*s.Rational(1,2)-2)-(r-1))==0
assert s.simplify((r-s.Rational(1,2)+s.Rational(1,2)-1)-(r-1))==0
for a,b in [(0,2),(1,1),(2,0)]:
 assert (a-b)/2-a==-1
checks.append({'name':'Exact Jacobian and all ordinary second-order powers','passed':True,'scope':'Both reciprocal window factors and the constant/linear/quadratic one-order losses.'})
u=s.Matrix([1+s.I,2-s.I]);B=s.Matrix([[0,2],[-1,3]])
pair=lambda a,b:(a.T*s.conjugate(b))[0]
lhs=s.re(pair(s.I*B*u,u));rhs=s.I*pair((B-B.conjugate().T)*u,u)/2
assert s.simplify(lhs-rhs)==0 and lhs!=0
assert s.simplify(lhs+rhs)!=0
checks.append({'name':'Linear-first adjoint sign','passed':True,'scope':'A nonselfadjoint finite matrix gives a nonzero real quadratic form and rejects the reversed i/2 sign.'})
w1,w2=s.symbols('w1 w2',positive=True)
W=s.diag(w1,w2);norm=s.sqrt(s.simplify(pair(W*u,W*u)))
dual=W*W*u/norm
assert s.simplify(pair(u,dual)-norm)==0
assert s.simplify(pair(W.inv()*dual,W.inv()*dual)-1)==0
checks.append({'name':'Original weighted Hilbert norm test','passed':True,'scope':'The exact two-weight E2s dual vector has norm one and attains the original norm, with complex coefficients and linear-first pairing.'})
lam,p=s.symbols('lam p',positive=True);t=s.symbols('t',nonnegative=True)
assert s.integrate(s.exp(-p*lam*t/2),(t,0,s.oo))==2/(p*lam)
checks.append({'name':'Weighted convolution normalization','passed':True,'scope':'Exact finite-p kernel integral; endpoints and complete Young proof are in the integration companion.'})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'passed':True,'finite_groups':len(checks),'checks':checks,'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name:sha(p) for p in MOD.glob('*.md')},'finite_checks_are_not_general_proofs':True,'U030_restored':False}
(MOD/'model-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))
