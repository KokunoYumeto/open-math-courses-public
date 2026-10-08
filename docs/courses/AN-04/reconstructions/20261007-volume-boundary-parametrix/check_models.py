"""Exact finite checks supplement the general proofs in the companion."""
from pathlib import Path
import hashlib,json
from datetime import datetime,timezone
import sympy as s
here=Path(__file__).resolve().parent
a,b,r=s.symbols('a b r',positive=True);I=s.I
C=s.Matrix([[1,-I/a],[I*a,1]])/2
B=s.Matrix([[1,0]]);S=s.Matrix([1,I*a]);S2=s.eye(2)-S*B
trace=s.Matrix([1/(2*a),-I/2])
assert s.simplify(C*C-C)==s.zeros(2)
assert s.simplify(C*trace)==s.zeros(2,1)
assert s.simplify(S2*C)==s.zeros(2)
assert s.simplify(B*C*S)==s.ones(1)
layer=s.Matrix([[s.Rational(1,2),-I/(2*a)]])*S2*trace
assert s.simplify(layer[0]+1/(2*a))==0
u=(s.exp(-b*r)-s.exp(-a*r))/(a*a-b*b)
assert s.simplify(-s.diff(u,r,2)+a*a*u-s.exp(-b*r))==0
assert s.simplify(u.subs(r,0))==0
res=r*s.exp(-a*r)/(2*a)
assert s.simplify(s.limit(u,b,a)-res)==0
assert s.simplify(-s.diff(res,r,2)+a*a*res-s.exp(-a*r))==0
vp=s.exp(-r)/2-s.exp(-2*r)/3;cor=-s.exp(-r)/6
assert s.simplify(vp+cor-u.subs({a:1,b:2}))==0
checks=[{'name':'Exact scalar Green solution, stable/unstable trace cancellation, source phases, resonant limit and plotted curves','passed':True}]
eps=s.symbols('epsilon');P=s.Matrix([[2,1],[0,3]]);A=s.Matrix([[1,2],[-1,0]])
Q=P.inv()*(s.eye(2)+eps*A);RF=P*Q-s.eye(2);RE=Q*P-s.eye(2)
assert RE!=RF
for n in range(1,6):
    Qn=Q*sum(((-RF)**j for j in range(n)),s.zeros(2))
    assert s.expand(P*Qn-s.eye(2)+(-RF)**n)==s.zeros(2)
    assert s.expand(Qn*P-s.eye(2)+(-RE)**n)==s.zeros(2)
checks.append({'name':'Both ordered finite inverse errors for N=1 through 5, with exact plus-error signs','passed':True})
rankone=s.Matrix([[0,1],[0,0]]);eta=s.diag(1,0);far=s.Matrix([0,1])
assert eta*far==s.zeros(2,1)
assert (rankone*eta-eta*rankone)*far==-s.Matrix([1,0])
assert eta*rankone*far+(rankone*eta-eta*rankone)*far==s.zeros(2,1)
checks.append({'name':'Separated-input commutator and the exact cancellation of localized forcing','passed':True})
F=s.Rational;orders=[0,5,F(7,2)];sigma=F(11,4)
assert [sigma-j-F(1,2) for j in orders]==[F(9,4),F(-11,4),F(-5,4)]
for split,expected in [(-2,(0,F(7,4))),(4,(6,F(-17,4)))]:
    actual=(split+2,F(-1,4)-split)
    assert actual==expected and sum(actual)==F(7,4)
assert [F(13,4)-j-F(1,2) for j in orders]==[F(11,4),F(-9,4),F(-3,4)]
ss,tt,nn,mm,nu=s.symbols('s t N m nu',real=True)
assert s.expand((ss+tt+mm)-mm+nn-(ss+nn)-tt)==0
assert s.expand((tt+mm)-mm+nn-(ss+nn)-(tt-ss))==0
assert s.expand((ss+tt+1)-(ss+1)-tt)==0
checks.append({'name':'All-real error-map arithmetic, unchanged boundary-layer input and high/fractional measurement orders','passed':True})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(here/'volume-boundary-parametrix.md'),
     'script_sha256':sha(Path(__file__)),'passed':True,'checks':checks,'finite_checks_replace_proofs':False}
(here/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_check_groups':len(checks)}))
