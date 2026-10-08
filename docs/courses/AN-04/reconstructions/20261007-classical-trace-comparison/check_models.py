"""Exact finite examples and order/sign checks, not substitutes for the proofs."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
z=s.symbols('z',positive=True)
rho=s.sqrt(1+z+z*z)/z
C=s.Matrix([[1,1/(s.I*rho)],[s.I*rho,1]])/2
q=s.Matrix([[1,z/s.I],[s.I/z,1]])/2
assert s.simplify(C*C-C)==s.zeros(2)
assert s.simplify(q*q-q)==s.zeros(2)
lower=s.series((C[1,0]-q[1,0])/s.I,z,0,3).removeO()
upper=s.series((C[0,1]-q[0,1])/s.I,z,0,4).removeO()
assert s.expand(lower-(s.Rational(1,4)+3*z/16-3*z*z/32))==0
assert s.expand(upper-(z*z/4+z**3/16))==0
assert s.limit(z*(rho-1/z)/2,z,0)==0
checks.append({'name':'Exact scalar projection and the two different weighted entry remainders','passed':True,'lower_imaginary_series':str(lower),'upper_imaginary_series':str(upper)})
count=0
for m in range(1,7):
 for a in range(m):
  for b in range(m-a):
   for source_q in range(m-a-b):
    for k in range(9):
     for v in range(k+1):
      normal=-m+b+v;tangential=m-a-b-source_q-1
      assert normal+tangential+1==v-a-source_q
      for loss in range(1,5):
       assert normal+(tangential-loss)+1<=k-a-loss
      if source_q or v<k:assert normal+tangential+1<=k-a-1
      count+=1
k=s.symbols('k',positive=True)
assert s.limit((k/s.sqrt(2)),k,s.oo)==s.oo
checks.append({'name':'All source/output order indices through m=6 and k=8; failure of the reversed normal inclusion','passed':True,'index_cases':count})
A=s.Matrix([[1,1],[0,1]]);B=s.Matrix([[0,0],[1,0]])
e=s.symbols('e');T0=A.inv();T1=-T0*B*T0;T2=T0*B*T0*B*T0
assert A*B!=B*A
assert s.expand((A+e*B)*(T0+e*T1+e*e*T2)-s.eye(2)-e**3*B*T2)==s.zeros(2)
actual=s.Matrix([[1,-1],[-e,1]])/(1-e)
assert s.simplify((A+e*B)*actual-s.eye(2))==s.zeros(2)
assert T1!=-T0*T0*B
checks.append({'name':'Ordered inverse recursion and an explicitly failing commuted coefficient','passed':True})
eta,kappa,alpha,beta,u=s.symbols('eta kappa alpha beta u',real=True)
f=eta**2*kappa+eta*kappa**2
shift=f.subs({eta:eta+u*alpha,kappa:kappa+u*beta},simultaneous=True)
approx=f+alpha*s.diff(f,eta)+beta*s.diff(f,kappa)
rem=s.integrate((1-u)*s.diff(shift,u,2),(u,0,1))
assert s.expand(shift.subs(u,1)-approx-rem)==0
assert s.diff(s.exp(-u)/2,u).subs(u,0)==-s.Rational(1,2)
assert s.diff(s.exp(u)/2,u).subs(u,0)==s.Rational(1,2)
assert s.residue(1/(1+kappa*kappa),kappa,s.I)*s.I==s.Rational(1,2)
checks.append({'name':'Mixed tangential/normal Taylor remainder and the positive cusp trace sign','passed':True})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(root/'classical-trace-comparison.md'),'script_sha256':sha(Path(__file__)),'passed':True,'checks':checks,'finite_checks_do_not_replace_general_proofs':True}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'index_cases':count}))
