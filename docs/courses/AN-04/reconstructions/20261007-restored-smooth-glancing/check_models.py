"""Finite symbolic/arithmetic checks; not a theorem certificate."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;p=r
source=p/'smooth-glancing-neighborhoods-and-windows.md'
groups=[]
def done(name,cases):groups.append({'name':name,'cases':cases,'passed':True})
kappa,M=s.symbols('kappa M',positive=True)
h=s.sqrt(kappa)/(4*M)
assert s.simplify(8*M**2*h**2-kappa/2)==0
C,w=s.symbols('C w',positive=True)
assert s.simplify(8*(2/(C*w))**2*(2*w)**2-128/C**2)==0
assert s.simplify((128/C**2).subs(C,32/s.sqrt(kappa))-kappa/8)==0
done('CG7 explicit elliptic absorption and shrinking guard',3)
beta_old,beta_new,phi_delta,hnew,hstar=s.symbols('bo bn phi hn hs')
assert s.expand((1+beta_old-phi_delta)-(1+beta_new-phi_delta))==beta_old-beta_new
assert s.expand(hnew+beta_old-beta_new-hstar-(hnew-hstar))==beta_old-beta_new
for j in range(1,65):
    nu=F(1)+F(j,2)
    assert nu-F(3,2)==F(j-1,2) and nu-1==F(j,2)
    assert F(1,2)+F(1,2**(j+1))>F(1,2)
    assert F(1,2)+F(1,2**j)>F(1,2)+F(1,2**(j+1))
done('CG23--CG25 exact energy induction and beta nesting',66)
assert F(1,4)+F(1,16)==F(5,16)<F(3,2)
assert F(3,4)/F(1,4)+F(1,2)>1 and F(1,16)<1
eps=F(1,4);hs=F(1,4)
assert [-1+eps*(hs-b) for b in [F(1),F(3,4),F(1,2)]]==[F(-19,16),F(-9,8),F(-17,16)]
done('CG26 common inner region and exact diagram endpoints',6)
pb,a,kap=s.symbols('pb a kap',positive=True)
# dR0 = dpb/a - pb da/a^2; the second term vanishes on pb=0.
dpb,da=s.symbols('dpb da')
assert s.simplify((dpb/a-pb*da/a**2).subs(pb,0)-dpb/a)==0
for d in [-1,1]:
    assert d*d*2==2
for hj in [F(-3,20),F(-1,10),F(1,10),F(3,20)]:
    delta=2*abs(hj);direction=-1 if hj>0 else 1
    assert direction*2*hj==-delta
    for L in [F(16),F(64)]:
        omega=L*delta**2
        assert 2*omega==8*L*hj**2 and 3*omega==12*L*hj**2
done('CG28/CG30--CG36 signed clocks, parabolic constants and normal-form scale',13)
out={'schema':'an04-smooth-glancing-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'passed':True,'groups':groups,'general_theorem_certificate':False}
(p/'model-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':len(groups),'general_theorem_certificate':False})
