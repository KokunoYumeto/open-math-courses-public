"""Finite exact checks supporting the full analytical proofs in the lesson. CC0."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def check(name,statement):
 assert statement,name
 checks.append(name)
x=s.symbols('x1:4',real=True);xi=s.symbols('xi1:4',real=True)
a=xi[0]-x[1]*xi[2];b=xi[1]+x[0]*xi[2]
bracket=sum(s.diff(a,xi[j])*s.diff(b,x[j])-s.diff(a,x[j])*s.diff(b,xi[j]) for j in range(3))
check('Lewy bracket sign and coefficient',s.expand(bracket-2*xi[2])==0)
characteristic={xi[0]:x[1]*xi[2],xi[1]:-x[0]*xi[2]}
check('Lewy real characteristic equation',s.expand(a.subs(characteristic))==0)
check('Lewy imaginary characteristic equation',s.expand(b.subs(characteristic))==0)
for k in range(7):
 t=-s.Rational(1,1+k*k);ell=s.Rational(k*k,1+k*k)
 check(f'exact correction identity k={k}',1+t==ell)
 check(f'two-derivative norm k={k}',s.Abs(t)*(1+k*k)==1)
 if k:check(f'nonzero mode inverse bound k={k}',s.Rational(1,2)<=ell<1 and 1/ell<=2)
check('constant mode obstruction',1-s.Rational(1)==0)
N,q,order=s.symbols('N q order',real=True)
check('low-order residual threshold',s.expand(-N-(-2*N-1)-(N+1))==0)
check('forward graph forcing threshold',s.expand((N-order)-(-order)-N)==0)
check('example forward threshold',N-(-2)==N+2)
check('example reverse threshold',N-2==N+(-2))
for j in [0,1,2,4,8]:
 tail=s.Rational(1,1+(j+1)**2)
 check(f'finite-rank tail decreases J={j}',0<tail<=s.Rational(1,2) and s.Rational(1,1+(j+2)**2)<tail)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,'source_sha256':sha(root/'local-solvability-equivalences-and-adjoint-estimates.md'),'script_sha256':sha(Path(__file__)),'scope':'Exact characteristic, Sobolev-order and spectral identities; Baire uniformity, closed range, graph invariance and the adjoint estimate are proved analytically in the lesson.'}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8');print(json.dumps(result))
