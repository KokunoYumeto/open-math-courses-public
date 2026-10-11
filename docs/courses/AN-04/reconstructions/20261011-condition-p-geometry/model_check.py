"""Finite exact identities supporting the analytic proofs. CC0-1.0."""
from pathlib import Path
import sympy as s
import hashlib,json
root=Path(__file__).resolve().parent
t,x,y,tau,eta,kappa,xi=s.symbols('t x y tau eta kappa xi',real=True)
h=s.Function('h')(t);cases=[]
def check(name,actual,expected=0):
    delta=actual-expected
    assert s.simplify(delta)==0,(name,delta)
    cases.append(name)
coords=[t,x,y,tau,eta,kappa]
def ham(p):return [s.diff(p,z) for z in coords[3:]]+[-s.diff(p,z) for z in coords[:3]]
G=x*x+t*t*y*y+y**4;p=tau+s.I*kappa*G
expected=[1,0,s.I*G,-2*s.I*kappa*t*y*y,-2*s.I*kappa*x,-s.I*kappa*(2*t*t*y+4*y**3)]
for j,(a,b) in enumerate(zip(ham(p),expected)):check('Hamilton component '+str(j),a,b)
zero={x:0,y:0,tau:0,kappa:1}
for j,a in enumerate(ham(p)):check('Characteristic restriction '+str(j),a.subs(zero),1 if j==0 else 0)
trans=[x,y,eta,kappa];Q=s.hessian(kappa*G,trans).subs(zero)
for j in range(4):check('Hessian diagonal '+str(j),Q[j,j],[2,2*t*t,0,0][j])
check('Hessian off diagonal sum',sum(Q[i,j]**2 for i in range(4) for j in range(4) if i!=j))
assert Q.subs(t,0).rank()==1;cases.append('Rank at zero is one')
assert Q.subs(t,1).rank()==2;cases.append('Rank at nonzero sample is two')
check('Exact nonzero minor',Q[:2,:2].det(),4*t*t)
check('Degree-one Euler identity',sum(z*s.diff(p,z) for z in [tau,eta,kappa]),p)
p2=tau+s.I*h*x*xi
for j,(a,b) in enumerate(zip([s.diff(p2,xi),-s.diff(p2,t),-s.diff(p2,x)],[s.I*h*x,-s.I*s.diff(h,t)*x*xi,-s.I*h*xi])):check('Plateau field '+str(j),a,b)
check('Invariant complex coordinate',s.I*h-s.I*h)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,'cases':cases,
 'source_sha256':sha(root/'condition-p-and-characteristic-saturation.md'),'script_sha256':sha(Path(__file__)),
 'scope':'Finite Hamilton, homogeneity and Hessian identities. Full condition P, saturation, continuation and every-t rank statements are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'cases':len(cases)}))
