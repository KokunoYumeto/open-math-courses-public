"""Finite exact identities supporting the written uniform-solvability proof."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
source=HERE/'uniform-solvability-and-degenerate-complex-coordinates.md'
x,t,ep,r=S.symbols('x t epsilon r',real=True)
N=S.symbols('N',integer=True,nonnegative=True)
C,c,c0=S.symbols('C c c0',positive=True)
a=S.Function('a')(x);v=S.Function('v')(x)
D=lambda f:-S.I*S.diff(f,x)
H=lambda f:f-ep**2*S.diff(f,x,2)
rows=[]
def exact(name,left,right=0):
 assert S.simplify(S.expand(left-right))==0,name
 rows.append({'name':name,'kind':'exact_identity','passed':True})
exact('multiplication-resolvent inverse commutator',a*H(v)-H(a*v),ep**2*(S.diff(a,x,2)*v+2*S.diff(a,x)*S.diff(v,x)))
L=lambda f:S.diff(a,x,2)*f-2*S.I*D(S.diff(a,x)*f)
exact('signed middle resolvent operator',L(v),-(a*H(v)-H(a*v))/ep**2)
exact('move active derivative through coefficients',L(D(v)),-2*S.I*D(D(S.diff(a,x)*v))+D(S.diff(a,x,2)*v)+2*D(S.diff(a,x,2)*v)+S.I*S.diff(a,x,3)*v)
exact('complete inverse square increment',(1+ep**2*r)**2,1+2*ep**2*r+ep**4*r**2)
exact('inductive constant increment',C*(2-1/(N+2))-C*(2-1/(N+1)),C/((N+1)*(N+2)))
exact('inductive strip decrement',(c0+(c-c0)/(N+1))-(c0+(c-c0)/(N+2)),(c-c0)/((N+1)*(N+2)))
exact('initial induction constant',(C*(2-1/(N+1))).subs(N,0),C)
exact('initial induction strip',(c0+(c-c0)/(N+1)).subs(N,0),c)
exact('extension value matching',S.Integer(3)-2,1)
exact('extension derivative matching',S.Integer(-3)+4,1)
u=x-S.I*t**3/3
exact('homogeneous coordinate for a=t squared',-S.I*S.diff(u,t)+t**2*S.diff(u,x))
exact('nonvanishing coordinate derivative',S.diff(u,x),1)
exact('positive primitive branch',S.diff((t-S.Rational(1,3))**2/2,t),t-S.Rational(1,3))
exact('negative primitive branch',S.diff(-(t+S.Rational(1,3))**2/2,t),-t-S.Rational(1,3))
exact('positive primitive endpoint',((t-S.Rational(1,3))**2/2).subs(t,S.Rational(1,3)))
exact('negative primitive endpoint',(-(t+S.Rational(1,3))**2/2).subs(t,-S.Rational(1,3)))
for value in [S.Rational(1,16),S.Rational(1,8),S.Rational(1,4),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(4),S.Integer(16)]:
 assert value**3<=(1+value**2)**2
 rows.append({'name':f'half-resolvent multiplier squared at {value}','kind':'exact_rational_inequality','passed':True})
Q,A,F,P,E=S.symbols('Q A F P E',commutative=False)
comm=lambda y,z:y*z-z*y
exact('Jacobi form with commuting multipliers',comm(E,comm(P,F))-comm(F,comm(P,E)),comm(P,comm(E,F)))
exact('product commutator',comm(Q,A*F),comm(Q,A)*F+A*comm(Q,F))
exact('three-factor commutator',comm(Q,A*F*E),comm(Q,A)*F*E+A*comm(Q,F)*E+A*F*comm(Q,E))
exact('commutator with product norm',P*F*E-E*F*P-E*comm(P,F)-comm(P,E)*F,P*comm(F,E))
# The Jacobi and product-norm residuals vanish for commuting Fourier multipliers.
for scale in [S.Rational(1,2),S.Rational(1,4),S.Rational(1,8),S.Rational(1,16)]:
 q=(1+scale**2*r)**-1
 exact(f'exact inverse multiplier at epsilon={scale}',q*(1+scale**2*r),1)
assert len(rows)==32
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,'checks':rows,'scope':'Finite exact algebra and selected multiplier checks. The complete uniform estimates, infinite-weight duality and parameter proofs are in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))
