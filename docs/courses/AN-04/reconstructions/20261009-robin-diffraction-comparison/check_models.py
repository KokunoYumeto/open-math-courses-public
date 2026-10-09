"""CC0-1.0. Exact checks of extension jets, Sobolev indices and affine geometry."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parent
checks=[]
def equal(name,a,b):
 assert S.simplify(a-b)==0,(name,a,b)
 checks.append(name)
x,s,rho,mu,lam,a,b,c,n,m=S.symbols('x s rho mu lam a b c n m',real=True)
lampos=S.symbols('L',positive=True)
w=a+b*x+c*x*x
ext=3*w.subs(x,-x)-2*w.subs(x,-2*x)
equal('negative polynomial',ext,a+b*x-5*c*x*x)
equal('extension value jump',w.subs(x,0)-ext.subs(x,0),0)
equal('extension first-jet jump',S.diff(w,x).subs(x,0)-S.diff(ext,x).subs(x,0),0)
equal('even extension derivative jump',S.diff(w,x).subs(x,0)-S.diff(w.subs(x,-x),x).subs(x,0),2*b)
equal('second derivative may jump',S.diff(w-ext,x,2),12*c)
aa,bb=S.symbols('aa bb')
assert S.solve([aa+bb-1,-aa-2*bb-1],[aa,bb])=={aa:3,bb:-2}
checks.append('unique two reflection coefficients')
equal('mixed norm Fourier polynomial',(lampos**2+rho**2)**2,lampos**4+2*rho**2*lampos**2+rho**4)
for idx in [-S.Rational(7,3),-1,0,S.Rational(5,2)]:
 equal('trace average '+str(idx),(idx+(idx-1))/2,idx-S.Rational(1,2))
 equal('normal trace average '+str(idx),((idx-1)+(idx-2))/2,idx-S.Rational(3,2))
 equal('fixed epsilon receiving index '+str(idx),idx-(idx-2),2)
indices=[-S.Rational(7,3)+S.Rational(j,2) for j in range(8)]
assert indices==list(map(S.Rational,['-7/3','-11/6','-4/3','-5/6','-1/3','1/6','2/3','7/6']))
checks.append('eight exact half-step indices')
assert indices[-2]<1<=indices[-1];checks.append('seven gains first reach H1')
M=S.Matrix([[0,m],[0,0]]);I=S.eye(2);Q=I/n-M/n**2;B=n*I+M
assert S.simplify(Q*B)==I;checks.append('ordered left Robin inverse')
assert S.simplify(B*Q)==I;checks.append('ordered right Robin inverse')
assert S.simplify(B/n-I)==M/n;checks.append('discarded Robin coefficient leaves error')
p=rho**2-x*lam**2-mu*lam
orbit={x:s*s,rho:s,mu:0,lam:1}
y1=-s;y2=-2*s**3/3
equal('Hamilton x equation',S.diff(s*s,s),S.diff(p,rho).subs(orbit))
equal('Hamilton rho equation',S.diff(s,s),-S.diff(p,x).subs(orbit))
equal('Hamilton y1 equation',S.diff(y1,s),S.diff(p,mu).subs(orbit))
equal('Hamilton y2 equation',S.diff(y2,s),S.diff(p,lam).subs(orbit))
equal('characteristic orbit',p.subs(orbit),0)
equal('physical time',y1+y2,-s-2*s**3/3)
equal('omitted spatial coordinate',y1-y2,-s+2*s**3/3)
equal('marked cap x',(s*s).subs(s,-S.Rational(1,4)),S.Rational(1,16))
equal('marked cap time',(y1+y2).subs(s,-S.Rational(1,4)),S.Rational(25,96))
assert S.diff(y1+y2,s)<0;checks.append('physical time decreases along the tangent orbit')
assert (n*I+M).conjugate()*(-1)==-S.conjugate(n)*I-S.conjugate(M)
checks.append('conjugation reverses the complete conormal row')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(ROOT/'robin-diffraction-by-dirichlet-comparison.md'),
 'script_sha256':sha(Path(__file__)),'scope':'Exact model identities and index arithmetic only; the analytic comparison and weak-domain proof are in the lesson.',
 'internal_export_proof_closure_claimed':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
