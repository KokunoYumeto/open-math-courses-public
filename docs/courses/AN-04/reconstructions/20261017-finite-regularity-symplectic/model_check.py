"""Exact sign, scaling and fold-chart checks for the stated examples."""
from pathlib import Path
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parent
x,y,r,z,t,u,v,p=s.symbols('x y r z t u v p', real=True)
rp,k,pp=s.symbols('rp k pp',positive=True)
coords=[x,y,r,z]
checks=[]
def check(name,a,b):
    if isinstance(a,s.MatrixBase):
        ok=all(s.simplify(q)==0 for q in a-b)
    else:ok=s.simplify(a-b)==0
    assert ok,name
    checks.append(name)
def bracket(f,g):
    return s.diff(f,r)*s.diff(g,x)-s.diff(f,x)*s.diff(g,r)+s.diff(f,z)*s.diff(g,y)-s.diff(f,y)*s.diff(g,z)
def scaled(f,g):return r*bracket(f,g)
W=s.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])
check('original canonical sign',bracket(r,x),1)
check('rescaled form determinant',(W/r).det(),r**-4)
check('first inner bracket',scaled(z,y),r)
check('second and third inner brackets',scaled(y,x)**2+scaled(x,z)**2,0)
J=scaled(x,scaled(z,y))+scaled(z,scaled(y,x))+scaled(y,scaled(x,z))
check('actual nonzero Jacobi defect',J,-r)
vectors=s.Matrix([[-r,0,0],[0,0,-r],[0,r,0]])
check('three-form contraction gives the opposite Jacobi sign',-vectors.det()/r**2,r)
Df=s.diag(1,1,k,k)
check('invariant scaled form under fiber dilation',Df.T*(W/(k*r))*Df,W/r)
check('weight-minus-one bracket example',bracket(x/r,r**2),-2)
H=s.Matrix([s.diff(x/r,r),-s.diff(x/r,x)])
R=s.Matrix([0,r])
br=H.jacobian([x,r])*R-R.jacobian([x,r])*H
check('Euler commutator for degree-minus-one function',br,-2*H)
# Coordinates are (q1,q2,s,p2); ambient coordinates (x1,x2,x3,xi1,xi2,xi3).
q1,q2,normal,p2=s.symbols('q1 q2 normal p2', real=True)
target=[q1,q2,normal,pp]
ambient=s.Matrix([0,q2,q1,normal*s.sqrt(pp/2),pp,normal**2/2])
Wa=s.zeros(6)
for j in range(3):Wa[3+j,j]=1;Wa[j,3+j]=-1
D=ambient.jacobian(target)
fold=s.Matrix([[0,0,-normal,0],[0,0,0,-1],[normal,0,0,0],[0,1,0,0]])
check('complete ambient fold pullback',D.T*Wa*D,fold)
check('fold determinant has the exact double zero',fold.det(),normal**2)
assert fold.subs(normal,0).rank()==2
checks.append('ambient rank at the fold is two')
restricted=fold.subs(normal,0).extract([0,1,3],[0,1,3])
assert restricted.rank()==2
checks.append('restricted hypersurface radical has dimension one')
Dt=s.diag(1,1,s.sqrt(k),k)
check('half-degree coordinate gives a degree-one form',Dt.T*fold.subs(normal,s.sqrt(k)*normal)*Dt,k*fold)
xp=s.symbols('xp',positive=True)
q=xp+s.Rational(2,5)*xp**s.Rational(5,2)
check('C2 coordinate derivative equals the C1 form coefficient',s.diff(q,xp),1+xp**s.Rational(3,2))
check('third derivative has the stated singular coefficient',s.diff(q,xp,3),s.Rational(3,4)/s.sqrt(xp))
raw=(ROOT/'finite-regularity-forms-and-conic-calculations.md').read_bytes()
(ROOT/'model-check.json').write_text(json.dumps({'passed':True,'exact_checks':len(checks),'checks':checks,
    'source_sha256':hashlib.sha256(raw).hexdigest(),
    'scope':'Finite exact algebra checks for the conventions and explicit examples; full arguments are in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
