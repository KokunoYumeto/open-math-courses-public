"""Finite algebra supplements the complete parameter/energy arguments in the source."""
from pathlib import Path
import datetime,hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;f=r/'glancing-cutoff-scales-preparation.md'
x,rho,tau,zeta=s.symbols('x rho tau zeta',real=True);eps,delta,A,B,C=s.symbols('eps delta A B C',positive=True)
p=tau**2-(1-x)*zeta**2-rho**2
assert all(s.simplify(u-v)==0 for u,v in [(s.diff(p,tau),2*tau),(s.diff(p,zeta),-2*(1-x)*zeta),(s.diff(p,rho),-2*rho),(-s.diff(p,x),-zeta**2)])
hp_x=s.diff(p,rho);hp2_x=-s.diff(p,x)*s.diff(hp_x,rho);assert hp2_x==2*zeta**2
vp_omega=s.diff(x**2,x)*hp_x/(2*tau);assert vp_omega==-2*x*rho/tau
exact=1+vp_omega.subs({x:eps*delta,rho:s.sqrt(eps*delta),tau:1})/(eps**2*delta)
assert s.simplify(exact-(1-2*s.sqrt(delta/eps)))==0
general=C*A*eps*delta*(A*eps*delta+B*delta+s.sqrt(A*eps*delta))/(eps**2*delta)
assert s.simplify(general-C*(A**2*delta+A*B*delta/eps+A**s.Rational(3,2)*s.sqrt(delta/eps)))==0
assert s.simplify(s.sqrt(eps*delta)/eps-s.sqrt(delta/eps))==0
assert s.simplify(s.sqrt(delta/eps)/delta-1/s.sqrt(eps*delta))==0
record={'schema':'an04-glancing-cutoff-finite-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'groups':['All homogeneous Hamilton derivatives and strict tangency','Exact characteristic cutoff derivative','Every parameter power in the abstract derivative bound','Mixed-error square root and failed-delta ratio'],'passed':True,'general_lemma_proof_by_finite_tests_claimed':False,'full_boundary_propagation_proved':False}
(r/'model-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'finite_algebra_groups':4,'passed':True,'full_boundary_propagation':False})
