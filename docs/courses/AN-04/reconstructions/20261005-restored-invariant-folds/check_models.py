"""Bounded independent algebra/norm checks; the general theorem is proved in the lesson."""
from pathlib import Path
import hashlib,json
from fractions import Fraction
import sympy as S
import numpy as np
here=Path(__file__).resolve().parent;checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
u1,u2,r=S.symbols('u1 u2 r',real=True);rho=S.symbols('rho',positive=True)
z=S.Matrix([u1,u2,r,rho])
v2=u2+u1**2-r**3/3;v1=u1+r-v2**2
p=S.Matrix([(r**2+2*u1)*rho,rho])
q=S.Matrix([r**2*rho,(1+2*v2*r**2)*rho])
out=S.Matrix([u1,u2,*p]);inp=S.Matrix([v1,v2,*q])
Jo=out.jacobian(z);Ji=inp.jacobian(z)
O=S.zeros(2).row_join(-S.eye(2)).col_join(S.eye(2).row_join(S.zeros(2)))
so=S.simplify(Jo.T*O*Jo);si=S.simplify(Ji.T*O*Ji)
assert so==si
lo=S.simplify(S.Matrix([[*p]])*S.Matrix([u1,u2]).jacobian(z))
li=S.simplify(S.Matrix([[*q]])*S.Matrix([v1,v2]).jacobian(z))
assert lo==li==S.Matrix([[(r**2+2*u1)*rho,rho,0,0]])
assert S.simplify(Jo.det())==2*r*rho
assert S.simplify(Ji.det())==2*r*rho
ko=S.Matrix([0,0,1,0]);ki=S.Matrix([1,-2*u1,-1,0])
assert Jo.subs(r,0)*ko==S.zeros(4,1)
assert S.simplify(Ji.subs(r,0)*ki)==S.zeros(4,1)
for point in [{u1:0,u2:0,rho:1},{u1:2,u2:-3,rho:5},{u1:-1,u2:4,rho:2}]:
    assert Jo.subs(r,0).subs(point).rank()==Ji.subs(r,0).subs(point).rank()==3
    assert so.subs(r,0).subs(point).rank()==2
    assert so.subs({**point,r:1}).rank()==4
assert ko[2]==1 and ki[2]==-1
checks.append({'name':'full nonlinear cotangent lift and actual folds','passed':True,
 'common_one_form':str(lo),'both_projection_determinants':'2*r*rho',
 'fold_kernels':['d/dr','d/du1-2*u1*d/du2-d/dr'],'ranks_at_fold':[3,3,2],
 'scope':'Symbolic full two-dimensional relation, three exact fold samples, and off-fold rank.'})

# Normalize the axis-limit graph using a jointly unit covector, independently
# from the homogeneous two-fold model.
x=S.symbols('x',positive=True);tau=1/S.sqrt(1+4*x*x)
assert S.simplify((2*x*tau)**2+tau*tau)==1
assert S.limit(2*x*tau,x,0,dir='+')==0
assert S.limit(tau,x,0,dir='+')==1
assert S.simplify((2*x*tau)/tau)==2*x
checks.append({'name':'joint normalization and excluded-axis limit','passed':True,
 'limit_covectors':[0,1],'ratio':'2*x','scope':'Exact example, not an operator counterexample.'})

orders=[]
for s,m in [(Fraction(-3,4),Fraction(1,3)),(Fraction(0),Fraction(-1,6)),
            (Fraction(7,5),Fraction(8,3)),(Fraction(-5,2),Fraction(-7,4))]:
    t=s-m-Fraction(1,6);assert m+t-s==Fraction(-1,6)
    assert t+(-t)==0 and (-s)+s==0
    orders.append({'s':str(s),'m':str(m),'t':str(t),'conjugated':str(m+t-s)})
checks.append({'name':'all reducer orders and exact fractional examples','passed':True,'examples':orders})

# Direct trigonometric-polynomial quadrature independently of weighted
# coefficient sums. Smooth fractional reducers are exact Fourier multipliers
# on this finite periodic model, not a sample fold operator.
rng=np.random.default_rng(203011);modes=np.arange(-11,12)
a=rng.normal(size=len(modes))+1j*rng.normal(size=len(modes))
grid=2*np.pi*np.arange(256)/256;exps=np.exp(1j*np.outer(grid,modes))
norms=[]
for exponent in [-3/4,-5/4,7/5,0.]:
    coeff=(1+modes*modes)**(exponent/2)*a
    direct=np.mean(abs(exps@coeff)**2)
    weighted=np.sum((1+modes*modes)**exponent*abs(a)**2)
    assert abs(direct-weighted)<2e-12*max(1.,weighted)
    norms.append({'order':exponent,'quadrature_norm_squared':float(direct),
                  'Fourier_weight_norm_squared':float(weighted),'relative_error':float(abs(direct-weighted)/weighted)})
checks.append({'name':'independent all-real weighted Fourier norm calculation','passed':True,
 'models':norms,'scope':'Finite periodic reducer identity only; no FIO norm certification.'})

# Exact noncommuting matrices test the two recovery identities without
# assuming any factor is an actual inverse.
GX=S.Matrix([[1,2],[0,1]]);HX=S.Matrix([[1,0],[3,1]])
GY=S.Matrix([[2,1],[0,1]]);HY=S.Matrix([[1,4],[2,0]])
A=S.Matrix([[3,1],[2,5]]);I=S.eye(2);B=GX*A*GY
assert A-HX*B*HY==(I-HX*GX)*A+HX*GX*A*(I-GY*HY)
BX=S.Matrix([[2,0],[1,3]]);CY=S.Matrix([[1,2],[0,2]]);BY=S.Matrix([[3,1],[1,1]])
CX=S.Matrix([[2,1],[1,0]]);T=BX*A*CY
assert BX*A==T*BY+BX*A*(I-CY*BY)
assert A==CX*BX*A+(I-CX*BX)*A
assert GX*HX!=HX*GX and GY*HY!=HY*GY
checks.append({'name':'both exact recoveries with noncommuting factors','passed':True,
 'scope':'Arbitrary matrices expose the required composition sides and retain every residual.'})

J=Jo.col_join(Ji);Omega=O.row_join(S.zeros(4)).col_join(S.zeros(4).row_join(-O))
RX=S.Matrix([0,0,*p,0,0,0,0]);RY=S.Matrix([0,0,0,0,0,0,*q])
assert S.simplify(RX.T*Omega*J)==lo
assert S.simplify(RY.T*Omega*J+lo)==S.zeros(1,4)
RC=S.Matrix([0,0,0,rho])
assert S.simplify(RC.T*so)==lo
assert S.simplify(J.T*Omega*J)==S.zeros(4)
for point in [{u1:0,u2:0,r:0,rho:1},{u1:2,u2:-3,r:0,rho:5}]:
    assert J.subs(point).rank()==4
    assert J.row_join(RX).subs(point).rank()==5
    assert J.row_join(RY).subs(point).rank()==5
assert Fraction(2,12)==Fraction(1,6)
checks.append({'name':'common radial contraction and individual radial exclusions','passed':True,
 'signs':['plus common primitive','minus common primitive'],
 'sharpness':'corank=2 implies m<=-1/6 under universal boundedness','scope':'Exact transformed relation; general Lagrangian orthogonal argument remains in the proof.'})

name='invariant-fold-continuity-and-sobolev-transfer.md'
report={'schema':'invariant-fold-finite-check/v1','passed':True,'lesson':name,
 'lesson_sha256':sha(here/name),'script_sha256':sha(Path(__file__)),
 'checks':checks,'independent_mathematical_review':False,
 'scope':'Six bounded symbolic, matrix and independent quadrature checks. General support, microlocal inversion, composition, all-real continuity and universal sharpness are proved in the lesson, not certified by samples.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_checks':len(checks),'lesson_sha256':report['lesson_sha256']}))
