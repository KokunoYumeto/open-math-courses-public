"""Finite coefficient/scale checks; the full proof is in the lesson."""
from pathlib import Path
import datetime,hashlib,json
import sympy as S
r=Path(__file__).resolve().parent;p=r;source=p/'compensated-glancing-positive-commutator.md'
x,t,y,xi,zeta,tau=S.symbols('x t y xi zeta tau',real=True)
aa=S.Function('a')(x,t,y);bb=S.Function('b')(x,t,y);cc=S.Function('C')(x,t,y);B=S.Function('B')(t,y);O=S.Function('O')(t,y,zeta,tau)
ps=tau**2-aa*xi**2-2*bb*xi*zeta-cc*zeta**2
def hp(g):
 return S.diff(ps,xi)*S.diff(g,x)+S.diff(ps,zeta)*S.diff(g,y)+S.diff(ps,tau)*S.diff(g,t)-S.diff(ps,x)*S.diff(g,xi)-S.diff(ps,y)*S.diff(g,zeta)-S.diff(ps,t)*S.diff(g,tau)
hpbO=2*tau*S.diff(O,t)-2*B*zeta*S.diff(O,y)+S.diff(B,t)*zeta**2*S.diff(O,tau)+S.diff(B,y)*zeta**2*S.diff(O,zeta)
f0=hpbO/tau-2*(cc-B)*zeta*S.diff(O,y)/tau-4*x*bb*zeta/tau+S.diff(cc-B,t)*zeta**2*S.diff(O,tau)/tau+S.diff(cc-B,y)*zeta**2*S.diff(O,zeta)/tau
f1=-4*aa*x-2*bb*S.diff(O,y)+2*S.diff(bb,t)*zeta*S.diff(O,tau)+2*S.diff(bb,y)*zeta*S.diff(O,zeta)
f2=tau*(S.diff(aa,t)*S.diff(O,tau)+S.diff(aa,y)*S.diff(O,zeta))
assert S.expand(hp(x**2+O)/tau-f0-f1*xi/tau-f2*xi**2/tau**2)==0
sigma_formula=(-2*aa+x*S.diff(aa,x))*xi**2+2*(-bb+x*S.diff(bb,x))*zeta*xi+x*S.diff(cc,x)*zeta**2
assert S.expand(hp(x*xi)-sigma_formula)==0
groups=[{'name':'PC10--PC11 full variable coefficient Hamilton polynomial','cases':1,'passed':True},
 {'name':'PC15 compressed normal chain rule retains the omitted term','cases':1,'passed':True}]
v,ad,kt=S.symbols('v ad kt',positive=True);ch=S.exp(-1/v)
assert S.simplify(S.diff(ch,v)-ch/v**2)==0
# Hp(v)=-Hp(theta)/(A0 delta) and Hp(theta)=2|tau|.
assert S.simplify((-2*ch*S.diff(ch,v)*(-2*kt/ad))/(kt/ad*ch*S.diff(ch,v)))==4
assert S.simplify(ch/(ch/v)-v)==0
groups.append({'name':'PC23 main factor four and PC40 exact flat-cutoff ratio','cases':2,'passed':True})
bt,by=S.symbols('bt by',real=True)
rows=S.Matrix([[1,0,0],[-bt,-by,-2],[1,1,0]])
vb=S.Matrix([2,-2,by-bt])
assert (rows[1,:]*vb)[0]==0 and (rows[2,:]*vb)[0]==0 and rows.det()!=0
groups.append({'name':'PC6--PC8 time-dependent glancing and independent transverse first jets','cases':1,'passed':True})
reg,L,ss,cprime=S.symbols('r L s cprime',positive=True)
weight_expr=ss*cprime*zeta**2/tau**2-L*reg*cprime*zeta**2/(1+reg*(1+zeta**2+tau**2))
direct=(cprime*zeta**2*S.diff(S.log(tau**ss*(1+reg*(1+zeta**2+tau**2))**(-L/2)),tau))/tau
assert S.simplify(direct-weight_expr)==0
for kval in [.5,1,2,3]:
 for omg in [.0001,.001,.02]:
  cs=32/kval**.5;M=2/(cs*omg)
  assert 8*M*M*(2*omg)**2<=kval/2
groups.append({'name':'PC30 elliptic absorption and PC46 nonstationary weight derivative','cases':13,'passed':True})

# The weak normal factors cannot be interchanged on the Neumann form domain.
xx=S.symbols('xx',nonnegative=True)
vv=S.exp(-xx);dv=-S.I*S.diff(vv,xx)
left=S.integrate(vv*S.conjugate(dv),(xx,0,S.oo))
right=S.integrate(dv*S.conjugate(vv),(xx,0,S.oo))
assert left==-S.I/2 and right==S.I/2
groups.append({'name':'PC36 preserves the two actual normal factors including their boundary contribution','cases':2,'passed':True})
# A noncommuting finite model detects the side of the parametrix defect.
Th=S.Matrix([[1,1],[0,2]]);Tp=S.Matrix([[2,0],[1,1]])
h=S.Matrix([1+S.I,2]);v=S.Matrix([2,1-S.I])
pair=lambda a,b:(b.conjugate().T*a)[0]
E=Tp*Th-S.eye(2);wrong=Th*Tp-S.eye(2)
assert S.simplify(pair(Tp.conjugate().T*h,Th*v)-pair(h,E*v)-pair(h,v))==0
assert S.simplify(pair(Tp.conjugate().T*h,Th*v)-pair(h,wrong*v)-pair(h,v))!=0
groups.append({'name':'PC39 antidual action requires the left parametrix product','cases':2,'passed':True})

record={'schema':'an04-compensated-glancing-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'passed':True,'groups':groups,'general_theorem_certificate':False}
(p/'model-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':len(groups),'general_theorem_certificate':False})
