"""Finite exact checks of the full proofs; no check substitutes for an argument."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
import sympy as s
here=Path(__file__).resolve().parent
r,a=s.symbols('r a',positive=True);I=s.I;checks=[]
D=lambda x:-I*s.diff(x,r)
u=s.exp(-r)
assert s.simplify(D(u)-I*u)==0
assert -I*u.subs(r,0)+I==0
checks.append({'name':'Smooth normal derivative and exact cancellation of its negative-i boundary source','passed':True})
H=s.Matrix([[0,0],[1,0]]);A=s.diag(2,1+1/s.sqrt(2));Z=s.zeros(2);Id=s.eye(2)
M=Id.row_join(r*H).col_join(Z.row_join(Id))
AA=A.row_join(Z).col_join(Z.row_join(A))
expected=A.row_join(r*(H*A-A*H)).col_join(Z.row_join(A))
assert s.simplify(M*AA*M.inv()-expected)==s.zeros(4)
assert s.simplify(expected*M-M*AA)==s.zeros(4)
assert (H*A-A*H)[1,0]==1-1/s.sqrt(2)
assert s.diff(expected,r)!=s.zeros(4)
checks.append({'name':'Exact domain-correct conjugation and genuine normal dependence of an order-zero circle model','passed':True})
M=s.Matrix([[1,r],[0,1]]);AA=s.Matrix([[r*r,1+r],[r**3,2]])
AF=M*AA*M.inv();P2=s.Matrix([[1,2],[0,1]]);P1=s.Matrix([[0,1],[2,1]]);P0=s.Matrix([[3,0],[1,2]])
v=s.Matrix([r**6,r**7+1]);PP=lambda v:M*D(D(D(v)))+P2*D(D(v))+P1*D(v)+P0*v
C2=P2*AA-AF*P2+3*M*D(AA)
C1=P1*AA-AF*P1+2*P2*D(AA)+3*M*D(D(AA))
C0=P0*AA-AF*P0+P1*D(AA)+P2*D(D(AA))+M*D(D(D(AA)))
assert s.simplify(PP(AA*v)-AF*PP(v)-C2*D(D(v))-C1*D(v)-C0*v)==s.zeros(2,1)
B2=P2;B1=P1;B0=P0;AG=s.Matrix([[2,1],[0,3]])
tr=lambda v:v.subs(r,0)
BB=lambda v:B2*tr(D(D(v)))+B1*tr(D(v))+B0*tr(v)
bound=(B2*tr(AA)-AG*B2)*tr(D(D(v)))+(B1*tr(AA)-AG*B1)*tr(D(v))+(B0*tr(AA)-AG*B0)*tr(v)+2*B2*tr(D(AA))*tr(D(v))+B2*tr(D(D(AA)))*tr(v)+B1*tr(D(AA))*tr(v)
assert s.simplify(BB(AA*v)-AG*BB(v)-bound)==s.zeros(2,1)
checks.append({'name':'Complete cubic interior and boundary product rules with noncommuting variable matrices','passed':True})
cases=0
for m in range(1,9):
 for k in range(m+1):
  for x in [F(0),F(1,7),F(1,2),F(1),F(3,2),F(4),F(17)]:
   ratio2=(1+x*x)*(x*x/(1+x*x))**k if x<=1 else (1+1/(x*x))**(m-k)
   assert ratio2<=2**m;cases+=1
ss,tt=F(-7,2),F(0);initial=ss+tt
for _ in range(6):ss+=1;tt-=1;assert ss+tt==initial
assert (ss,tt)==(F(5,2),F(-6))
for _ in range(7):ss+=1
assert (ss,tt)==(F(19,2),F(-6)) and ss+min(tt,0)==F(7,2)
checks.append({'name':'Mixed normal-recovery ratios and the exact two-stage real-index sequence','cases':cases,'passed':True})
stable=s.Matrix([1,I*a]);B=s.eye(2);image=B*stable
assert image.rank()==1 and image.shape==(2,1) and image[0]==1
assert s.simplify(D(s.exp(-a*r))-I*a*s.exp(-a*r))==0
assert s.simplify(D(D(s.exp(-a*r)))+a*a*s.exp(-a*r))==0
checks.append({'name':'Stable scalar solution, redundant measurement rank and retained Dirichlet minor','passed':True})
assert s.Rational(1,2)*1+s.Rational(1,2)*(-1)==0
for k in [-3,-1,0,1,3]:
 for e in [s.Rational(1,4),-s.Rational(1,4),I/4,(1+I)/4]:
  for theta in [s.Rational(0),s.Rational(1,3),s.Rational(1)]:
   val=k*k+1+theta*e
   assert s.re(val)>=k*k+s.Rational(1,2)
checks.append({'name':'Failure of unrestricted convex inversion and verified normalized small-perturbation lower bound','passed':True})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(here/'elliptic-boundary-wavefront.md'),'script_sha256':sha(Path(__file__)),'passed':True,'checks':checks,'finite_checks_replace_proofs':False}
(here/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_check_groups':len(checks),'normal_recovery_cases':cases}))
