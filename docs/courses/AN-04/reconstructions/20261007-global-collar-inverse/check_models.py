"""Independent finite algebra and coordinate checks for global patching. CC0."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
checks=[]
I=S.eye(3);zero=S.zeros(3);q=S.sqrt(2)/2
thetas=[S.diag(1,q,0),S.diag(0,q,1)]
rhos=[S.diag(1,1,0),S.diag(0,1,1)]
P=S.Matrix([[3,1,2],[0,4,1],[1,2,5]])
Ts=[S.Matrix([[1,2,0],[0,1,3],[2,0,1]]),S.Matrix([[2,0,1],[1,3,0],[0,2,1]])]
assert sum((t*t for t in thetas),zero)==I
Q=zero;EL=zero;ER=zero
comm=lambda A,B:A*B-B*A
for t,rho,T in zip(thetas,rhos,Ts):
    Pi=P+7*(I-rho)
    assert t*P*rho==t*Pi*rho and rho*P*t==rho*Pi*t
    RE=T*Pi-I;RF=Pi*T-I
    left=t*t+t*t*RE*rho+t*comm(T,t)*Pi*rho+t*T*comm(t,P)*(I-rho)
    right=t*t+t*RF*t+rho*comm(Pi,t)*T*t+(I-rho)*comm(P,t)*T*t
    assert S.simplify(t*T*t*P-left)==zero
    assert S.simplify(P*t*T*t-right)==zero
    assert comm(T,t)!=zero and comm(P,t)!=zero
    Q+=t*T*t;EL+=left-t*t;ER+=right-t*t
assert S.simplify(Q*P-I-EL)==zero and S.simplify(P*Q-I-ER)==zero
assert S.simplify(EL-ER)!=zero
checks.append({'id':'both_exact_patch_decompositions','charts':2,
               'square_partition_exact':True,'local_models_differ_away_from_core':True,
               'nonzero_cutoff_terms_retained':True,'error_matrices_are_distinct':True})

r=S.symbols('r',real=True);m=3
M=S.Matrix([[1,r],[0,2]]);MI=M.inv()
A=S.Matrix([[r,1],[2,1-r]])
Q1=S.Matrix([[r*r,2-r],[1+r,r]])
delta=lambda A:-S.I*S.diff(A,r)
F1=M*Q1+m*M*delta(MI)+A*MI
E1=Q1*M-m*MI*delta(M)+MI*A
assert S.simplify(F1*M-M*E1)==S.zeros(2)
assert S.simplify(Q1-MI*F1-(-MI*A*MI-m*delta(MI)))==S.zeros(2)
assert S.simplify(Q1-E1*MI-(-MI*A*MI-m*delta(MI)))==S.zeros(2)
checks.append({'id':'complete_first_coefficient_cancellation','normal_order':m,
               'variable_noncommuting_leading_matrix':True,'both_sides_checked':True})

v,w,zeta=S.symbols('v w zeta',real=True)
psi=lambda x:x+x**3
L=1+v*v+v*w+w*w;J=1+3*w*w
assert S.expand(psi(v)-psi(w)-L*(v-w))==0
assert S.simplify((J/L).subs(w,v)-1)==0
assert S.simplify((psi(v)-psi(w))*(zeta/L)-(v-w)*zeta)==0
checks.append({'id':'nonlinear_chart_phase_and_density','inverse_chart':'psi(v)=v+v^3',
               'exact_phase_identity':True,'diagonal_density_ratio_is_one':True})

z=(1-r*r)**4
u=S.Matrix([1+r+r**5,2-r*r+r**4])
B=S.Matrix([[r,0],[1,r*r]])
D=lambda u,n=1:(-S.I)**n*S.diff(u,r,n)
op=lambda u:M*D(u,3)+A*D(u)+B*u
actual=S.expand(op(z*u)-z*op(u))
expected=M*(3*D(z)*D(u,2)+3*D(z,2)*D(u)+D(z,3)*u)+A*D(z)*u
assert S.simplify(actual-expected)==S.zeros(2,1)
wrong=expected+3*D(M)*D(z)*D(u)
assert S.simplify(actual-wrong)!=S.zeros(2,1)
checks.append({'id':'actual_variable_coefficient_cutoff_commutator',
               'normal_order':3,'spurious_leading_coefficient_derivative_detected':True})

source=HERE/'global-collar-inverse.md'
result={'schema':'AN04-global-collar-inverse-models/v1',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks':checks,'passed':True,'general_theorem_certified':False}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'finite_groups':len(checks),'passed':True}))
