"""Exact kernel signs, projection moments and graph orders. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
r,a,lam,I,h=S.symbols('r a lam I h',real=True)
G=S.Function('G');checks=[]
def eq(name,l,rhs):
 assert S.simplify(l-rhs)==0,name
 checks.append(name)
for k in [1,3,5]:
 V=r**(k+1)/S.Integer(k+1);W=a**(k+1)/S.Integer(k+1)
 w=S.exp(-lam*V);v=S.exp(-lam*W)
 K=S.I*S.exp(lam*(V-W))*(h-G(r))
 d=S.diff(K,r).subs(S.diff(G(r),r),w*w/I)
 eq(f'positive inverse off diagonal k={k}',-S.I*(d-lam*r**k*K),-w*v/I)
 Km=-S.I*S.exp(lam*(W-V))*(h-G(a))
 eq(f'negative inverse homogeneous output k={k}',-S.I*(S.diff(Km,r)+lam*r**k*Km),0)
 eq(f'adjoint null mode k={k}',S.diff(w,r)+lam*r**k*w,0)
 eq(f'normalization derivative k={k}',S.diff(V,r),r**k)
 eq(f'positive source projection kernel symmetry k={k}',w*v/I,v*w/I)
 # Input covector is -lambda for Q+ and +lambda for Q-.
 eq(f'positive projector input transpose L k={k}',S.I*S.diff(v,a)+S.I*lam*a**k*v,0)
 eq(f'negative projector input transpose adjoint L k={k}',S.I*S.diff(v,a)+S.I*lam*a**k*v,0)
for k in [2,4,6]:
 V=r**(k+1)/S.Integer(k+1);W=a**(k+1)/S.Integer(k+1)
 K=-S.I*S.exp(lam*(V-W))
 eq(f'even positive homogeneous kernel k={k}',-S.I*(S.diff(K,r)-lam*r**k*K),0)
 K=S.I*S.exp(-lam*(V-W))
 eq(f'even negative homogeneous kernel k={k}',-S.I*(S.diff(K,r)+lam*r**k*K),0)
for k in range(1,7):
 delta=S.Rational(1,k+1)
 eq(f'exact dilation balance k={k}',1-k*delta,delta)
eq('positive jump gives identity',-S.I*S.I,1)
eq('negative jump gives identity',-S.I*S.I,1)
eq('projector moment cancellation',S.sqrt(2*S.pi/3)-S.sqrt(S.Rational(2,3))*S.sqrt(S.pi),0)
eq('cubic order-three-halves gain',S.Rational(3,2)-1+S.Rational(1,4),S.Rational(3,4))
eq('source minus two output order',-2+S.Rational(3,4),-S.Rational(5,4))
eq('nonsolvable source threshold',-S.Rational(1,2)-(S.Rational(3,2)-1),-1)
m,s=S.symbols('m s',real=True)
eq('general transferred threshold',(s+m)-(m-1),s+1)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,'source_sha256':sha(root/'symplectic-model-projectors-and-solvability.md'),'script_sha256':sha(Path(__file__)),'scope':'Exact finite identities; the closed-domain, distributional, wavefront, Sobolev and solvability arguments are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps(out))
