"""Exact finite checks of radial transport, symplectic signs and the model clocks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
t,alpha,mu=s.symbols('t alpha mu',real=True)
r,R=s.symbols('r R',positive=True)
beta=s.symbols('beta');delta=mu*alpha+beta
V=lambda f:s.diff(f,t)+alpha*r*s.diff(f,r)
radius=r*s.exp(-alpha*t)
assert s.simplify(V(radius))==0
u=r**mu*(1-s.exp(-delta*t))/delta
assert s.simplify(V(u)+beta*u-r**mu)==0
resonant=t*r**mu
assert s.simplify(V(resonant)-mu*alpha*resonant-r**mu)==0
assert s.simplify(u.subs(t,0))==0
d=s.symbols('d');assert s.limit((1-s.exp(-d*t))/d,d,0)==t
for c in [s.Rational(1,2),s.Integer(1),s.Integer(2)]:
 assert c*2**(-s.Integer(1))==c/2 and c*2**s.Integer(1)==2*c
 assert s.simplify((c*2**t)*2**(-t)-c)==0
I=s.eye(2);Z=s.zeros(2);J=Z.row_join(I).col_join((-I).row_join(Z))
entries=s.symbols('a0:10');S=s.zeros(4);k=0
for i in range(4):
 for j in range(i,4):S[i,j]=S[j,i]=entries[k];k+=1
assert (J*S).T*(-J)+(-J)*(J*S)==s.zeros(4)
z,zeta,tt,ss=s.symbols('z zeta tt ss',real=True)
F=s.Matrix([tt,z,0,zeta,ss,z,0,zeta]);B=s.diag(-J,J)
DF=F.jacobian([tt,ss,z,zeta]);assert DF.T*B*DF==s.zeros(4)
# The kernel sign turns the difference form into the ordinary cotangent form.
K=s.Matrix([tt,z,ss,z,0,zeta,0,-zeta])
J4=s.zeros(4).row_join(s.eye(4)).col_join((-s.eye(4)).row_join(s.zeros(4)))
DK=K.jacobian([tt,ss,z,zeta]);assert DK.T*(-J4)*DK==s.zeros(4)
x,tau=s.symbols('x tau',real=True);q=(1+x*x)*tau
assert s.diff(q,tau)==1+x*x and s.diff(q,x).subs(tau,0)==0
assert s.simplify(s.diff(s.atan(x),x)*(1+x*x))==1
result={'passed':True,'finite_groups':4,'groups':[
 'Invariant radial coordinate and exact model endpoints',
 'Complex-parameter scalar transport, zero initial data and resonant limit',
 'General symmetric-Hessian variational identity and full free-relation/kernel pullbacks',
 'Positive variable multiplier and exact arctangent change of maximal clock'],
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.relative_to(ROOT).as_posix():sha(p) for p in [
 ROOT/'global-time-and-bicharacteristic-relation.md',ROOT/'figures/draw_invariant_radius.py',
 ROOT/'figures/invariant-radius-flow.svg',ROOT/'figures/invariant-radius-flow.png']},
 'full_theorems_proved_by_these_finite_checks':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':4}))
