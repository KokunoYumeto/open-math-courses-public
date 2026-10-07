"""Finite symbolic models test signs and order; they do not certify the general proof."""
from pathlib import Path
import datetime,hashlib,json
import sympy as s
r=Path(__file__).resolve().parents[4];c=Path(__file__).resolve().parent
b,h,t,xi,delta,theta=s.symbols('b h t xi delta theta',real=True)
I=s.eye(2);D=s.diag(1,-1);T=s.Matrix([[1,b],[0,1]]);Ti=T.inv()
S=Ti.T*Ti;B=T*D*Ti
def zero(M):
    for x in M:
        value=s.simplify(x)
        if value!=0:value=s.simplify(s.expand_complex(value))
        if value!=0:return False
    return True
checks=[]
def check(name,ok):
    assert ok,name
    checks.append({'name':name,'passed':True})
check('Shear inverse, symmetrization and metric',zero(T*Ti-I) and zero(S*B-B.T*S) and zero(T.T*S*T-I) and s.simplify(S.det()-1)==0)
Q=(S+I)/s.sqrt(4+b*b)
check('Positive square-root algebra',zero(Q*Q-S))
Rp=T*s.diag(1,0)*Ti;Rm=T*s.diag(0,1)*Ti
check('Both nonorthogonal projectors and S orthogonality',zero(Rp*Rp-Rp) and zero(Rm*Rm-Rm) and zero(Rp*Rm) and zero(Rp+Rm-I) and zero(Rp.T*S-S*Rp) and zero(Rm.T*S-S*Rm))
u=s.Matrix([s.cos(theta)+s.sin(theta),s.sin(theta)])
check('Exact component ellipse',s.trigsimp((u.T*S.subs(b,1)*u)[0]-1)==0)
Bh=s.Matrix([[h,1],[0,-h]])
Uh=s.Matrix([[s.exp(-s.I*t*h*xi),-s.I*s.sin(t*h*xi)/h],[0,s.exp(s.I*t*h*xi)]])
check('Closing-gap evolution and initial trace',zero(Uh.diff(t)+s.I*xi*Bh*Uh) and zero(Uh.subs(t,0)-I))
N=s.Matrix([[0,1],[0,0]])
Uj=s.exp(-s.I*t*xi)*(I-s.I*t*xi*N)
check('Jordan evolution and initial trace',zero(Uj.diff(t)+s.I*xi*(I+N)*Uj) and zero(Uj.subs(t,0)-I))
bt=s.Function('b')(t);Tt=s.Matrix([[1,bt],[0,1]]);Tit=Tt.inv();Bt=Tt*D*Tit
v=s.Matrix([s.Function('vp')(t),s.Function('vm')(t)])
check('Time-connection cancellation',zero((Tt*v).diff(t)-Tt.diff(t)*Tit*(Tt*v)-Tt*v.diff(t)))
# A Fourier branch solves u_t+i xi B(t)u-T'(t)T(t)^(-1)u=0 exactly.
bs=s.symbols('bs',real=True);Ts=s.Matrix([[1,bs],[0,1]])
Ut=Tt*s.diag(s.exp(-s.I*delta*xi),s.exp(s.I*delta*xi))*Ts.inv()
derivative=Ut.diff(t)+Ut.diff(delta)
check('Two moving-frame Fourier branches',zero(derivative+s.I*xi*Bt*Ut-Tt.diff(t)*Tit*Ut) and zero(Ut.subs({delta:0,bs:bt})-I))
# Check the ordered inverse cancellation in SM26--SM27 on arbitrary matrices.
qxi=s.Matrix(2,2,lambda i,j:s.Symbol('qx'+str(i)+str(j)))
tx=s.Matrix(2,2,lambda i,j:s.Symbol('tx'+str(i)+str(j)))
b1=s.Matrix(2,2,lambda i,j:s.Symbol('b1'+str(i)+str(j)))
b1x=s.Matrix(2,2,lambda i,j:s.Symbol('bx'+str(i)+str(j)))
rminus=-(1/s.I)*qxi*tx*T
old=rminus*Ti*b1+(1/s.I)*qxi*(tx*b1+Ti*b1x)
check('Ordered inverse derivative cancellation',zero(old-(1/s.I)*qxi*Ti*b1x))
source=c/'variable-positive-symmetrizers-preparation.md'
record={'schema':'an04-variable-symmetrizer-finite-model-checks/v1',
    'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checks':checks,'finite_groups':len(checks),'passed':True,
    'finite_models_only':True,'general_proof_certified':False,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(c/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':True,'finite_model_groups':len(checks)}))
