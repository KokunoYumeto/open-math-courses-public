"""Finite exact sign/constant supplements, not a general proof certificate."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;source=r/'parabolic-wavefront-windows-and-rays.md'
rho,e1,e2,y1,y2,rr=s.symbols('rho eta1 eta2 y1 y2 r',real=True)
p=rho**2-e1*e2
assert [s.diff(p,v) for v in [rho,e1,e2]]==[2*rho,-e2,-e1]
assert [-s.diff(p,v) for v in [rr,y1,y2]]==[0,0,0]
assert s.diff(p,e1).subs(e2,1)==-1
alpha,step,position=s.symbols('alpha t a',real=True)
distance=(position+step)**2+alpha**2*position**2
completed=(1+alpha**2)*(position+step/(1+alpha**2))**2+alpha**2*step**2/(1+alpha**2)
assert s.simplify(distance-completed)==0
assert s.simplify(distance.subs(position,-step))==alpha**2*step**2
L=F(32);nu=F(1,5);delta=F(1,680);B=2*L+4
assert delta<F(1,10) and delta<=1/(2*L) and delta==nu/(2*B)
assert L*delta==F(4,85) and B*delta==F(1,10)<nu
eps,t=s.symbols('epsilon delta',positive=True)
assert s.simplify((eps*t).subs(eps,L*t)-L*t**2)==0
assert s.simplify((t/eps).subs(eps,L*t)-1/L)==0
record={'schema':'an04-parabolic-window-finite-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'groups':['Full Hamilton sign, frozen momenta, principal type and clock','Exact squared-distance lower bound and witness error','Every rational threshold in Exercise 1','Correct quadratic width and fixed absorption ratio'],
        'passed':True,'general_proof_by_finite_tests_claimed':False,'full_boundary_propagation_proved':False}
(r/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print({'passed':True,'finite_groups':4,'general_proof_certificate':False})
