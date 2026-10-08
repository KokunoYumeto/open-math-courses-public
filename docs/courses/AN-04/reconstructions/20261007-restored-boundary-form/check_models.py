"""Finite sign/order checks supplement, rather than certify, the full form proof."""
from pathlib import Path
import datetime, hashlib, json
import sympy as s
r=Path(__file__).resolve().parent
source=r/'boundary-form-localization.md'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
I=s.I
A=s.Matrix([[1,I,2],[0,2-I,1],[I,1,3]])
Ast=A.conjugate().T
D=[s.Matrix([[0,I,1],[-I,2,0],[1,0,-1]]),s.Matrix([[2,1,I],[1,0,2],[-I,2,1]])]
u=s.Matrix([1+I,2-I,3]);v=A*u
g=[[s.diag(2,-1,3),s.diag(1+I,2,0)],[s.diag(-I,1,2-I),s.diag(-3,1,2)]]
ell=[s.diag(I,1,2),s.diag(1,2-I,0)]
m=[s.diag(2,-I,1),s.diag(0,1,I)]
c=s.diag(1+I,2,-I)
inner=lambda x,y:(y.conjugate().T*x)[0]
comm=lambda h:h*A-A*h
C=[Dj*A-A*Dj for Dj in D]
Cs=[Dj*Ast-Ast*Dj for Dj in D]
def form(x,y):
    return (sum(inner(g[i][j]*D[j]*x,D[i]*y) for i in range(2) for j in range(2))+
            sum(inner(ell[j]*D[j]*x,y) for j in range(2))+
            sum(inner(m[i]*x,D[i]*y) for i in range(2))+inner(c*x,y))
defect=(sum(inner(comm(g[i][j])*D[j]*u,D[i]*v)+inner(g[i][j]*C[j]*u,D[i]*v)-inner(g[i][j]*D[j]*u,Cs[i]*v) for i in range(2) for j in range(2))+
        sum(inner(comm(ell[j])*D[j]*u,v)+inner(ell[j]*C[j]*u,v) for j in range(2))+
        sum(inner(comm(m[i])*u,D[i]*v)-inner(m[i]*u,Cs[i]*v) for i in range(2))+inner(comm(c)*u,v))
assert s.expand(form(v,v)-form(u,Ast*v)-defect)==0
x=s.symbols('x',real=True)
ch,ur=s.symbols('chi u',cls=s.Function)
ch,ur=ch(x),ur(x)
assert s.expand(s.diff(ch*ur,x)**2-s.diff(ur,x)*s.diff(ch**2*ur,x)-s.diff(ch,x)**2*ur**2)==0
vv=(1+x)*s.exp(-2*x*x)
assert s.diff(vv,x).subs(x,0)==1 and vv.subs(x,0)==1
assert s.simplify(s.integrate(-s.diff(vv,x,2)*vv-s.diff(vv,x)**2,(x,0,s.oo)))==1
for k in [1,2,3]:
    w=x**k*s.exp(-x)
    weak=s.integrate(s.diff(w,x),(x,0,1))-s.integrate(s.diff(w,x),(x,1,2))
    assert s.simplify(weak-2*w.subs(x,1)+w.subs(x,2))==0
record={'schema':'an04-boundary-form-finite-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
        'groups':['Full complex noncommuting principal/lower-term matrix defect','Exact real multiplication defect','Positive Neumann boundary contribution','Tent-source signs against three smooth tests'],
        'passed':True,'general_form_or_propagation_proof_by_finite_tests_claimed':False,'full_boundary_propagation_proved':False}
(r/'model-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'passed':True,'finite_groups':4,'general_proof_certificate':False})
