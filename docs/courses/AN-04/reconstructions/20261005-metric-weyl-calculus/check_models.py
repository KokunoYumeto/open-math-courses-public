"""Exact finite diagnostics. General metric/operator proofs are in the text."""
from pathlib import Path
import sympy as s,json,hashlib
P=Path(__file__).parent;checks={}
G1=s.Matrix([[2,1],[1,3]]);G2=s.Matrix([[4,1],[1,1]])
z=s.Matrix(s.symbols('z0:2'));e=s.Matrix(s.symbols('e0:2'))
v=(G1+G2).inv()*z
objective=((G1*v+e).T*G1.inv()*(G1*v+e)+(G2*v-e).T*G2.inv()*(G2*v-e))[0]
assert s.expand(objective-(z.T*(G1+G2).inv()*z)[0]-(e.T*(G1.inv()+G2.inv())*e)[0])==0
checks['exact_dual_sum_with_noncommuting_forms']=True
J=s.Matrix([[0,-1],[1,0]])
dual=lambda G:J*G.inv()*J.T
assert dual(dual(G1))==G1
assert dual(G1/2)==2*dual(G1)
checks['symplectic_duality_and_scaling']=True
B0=s.Matrix([[0,0,0,-1],[0,0,1,0],[0,1,0,0],[-1,0,0,0]])
G=s.diag(G1,G2);B=B0/4
assert (B.T*G*B).inv()==16*(B0.T*G*B0).inv()
assert (B0.T*G*B0).inv()==s.diag(dual(G2),dual(G1))
checks['actual_phase_dual_factor_sixteen']=True
p,q,r,t,x,xi=s.symbols('p q r t x xi',real=True)
composite=p*(x+q/2)+r*(x+q+t/2)
combined=(p+r)*(x+(q+t)/2)
assert s.expand(composite-combined-(q*r-p*t)/2)==0
checks['ordered_plane_wave_cocycle']=True
def star(a,b):
 out=0
 for j in range(7):
  term=sum((-1)**k*s.binomial(j,k)*s.diff(a,xi,j-k,x,k)*s.diff(b,x,j-k,xi,k) for k in range(j+1))
  out+=(-s.I/2)**j/s.factorial(j)*term
 return s.expand(out)
assert star(x,xi)==x*xi+s.I/2
assert star(xi,x)==x*xi-s.I/2
assert star(x*xi,x*xi)==x*x*xi*xi+s.Rational(1,4)
assert star(x*x,xi*xi)==x*x*xi*xi+2*s.I*x*xi-s.Rational(1,2)
checks['Weyl_sign_and_second_order_remainder']=True
b1,b2,c1,c2,x1,x2,tt=s.symbols('b1 b2 c1 c2 x1 x2 tt',real=True)
bc=b1*c1+b2*c2;cx=c1*x1+c2*x2;bx=b1*x1+b2*x2;cn=c1*c1+c2*c2
phi=bx*cx/cn-bc*cx*cx/(2*cn*cn)
assert s.simplify(c1*s.diff(phi,x1)+c2*s.diff(phi,x2)-bx)==0
shift=phi.subs({x1:x1+tt*c1,x2:x2+tt*c2},simultaneous=True)
assert s.simplify(shift-phi-tt*bx-tt*tt*bc/2)==0
checks['original_coordinate_affine_gauge']=True
A=s.Matrix([[2,1],[1,1]]);L=s.Matrix([[1,2],[2,0]]);R=s.Matrix([[0,1],[1,3]])
Z=s.zeros(2);I=s.eye(2);S=s.BlockMatrix([[I,Z],[L,I]]).as_explicit()*s.diag(A,A.T.inv())*s.BlockMatrix([[I,R],[Z,I]]).as_explicit()
JJ=s.BlockMatrix([[Z,-I],[I,Z]]).as_explicit()
assert S.T*JJ*S==JJ and S.det()==1
# A symplectic rotation has a singular position block; the t=1 shear repairs it.
rot=s.BlockMatrix([[Z,I],[-I,Z]]).as_explicit()
upper=s.BlockMatrix([[I,I],[Z,I]]).as_explicit()
assert (upper*rot)[:2,:2].det()!=0
checks['symplectic_block_factorization_and_singular_case']=True
zz,qq=s.symbols('z q')
for M in range(1,6):
 for N in range(1,6):
  poly=sum((qq*zz)**j/s.factorial(j) for j in range(N))
  rem=s.Poly(s.expand(poly**M-sum((M*qq*zz)**j/s.factorial(j) for j in range(N))),zz)
  assert all(mon[0]>=N for mon,coef in rem.terms() if coef!=0)
checks['finite_step_Taylor_coefficients']=True
k=s.symbols('k',real=True)
conv=x*xi-s.I*k
assert conv.subs(k,-s.Rational(1,2))==x*xi+s.I/2
checks['left_to_Weyl_quantization_sign']=True
shear=s.Matrix([[1,0],[-1,1]]);g=s.diag(s.Rational(1,4),1);gp=shear.T*g*shear
assert gp==s.Matrix([[s.Rational(5,4),-1],[-1,1]])
assert gp.det()==g.det()==s.Rational(1,4)
assert gp==dual(gp)/4 and g==dual(g)/4
ct,st=s.symbols('c t');orig=s.Matrix([2*ct,st]);pull=shear.inv()*orig
assert s.expand((pull.T*gp*pull)[0]-ct*ct-st*st)==0
checks['exact_shear_ellipses_area_and_Planck_parameter']=True
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'scope':'Exact finite algebra diagnostics; complete general proofs and hypotheses are in the text and exact proof map.',
 'script_sha256':sha(Path(__file__)),'source_hashes':{p.name:sha(p) for p in P.glob('*.md')},
 'figure_source_sha256':sha(P/'figures/symplectic_metric_shear.py'),
 'general_metric_L2_theorem_included':False,'Fefferman_Phong_operator_theorem_included':False,'U033_restored':False}
(P/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))
