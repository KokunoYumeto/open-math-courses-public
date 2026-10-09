"""Exact identities supporting the normal graph proof; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
source=root/'normal-graphs-from-banach-bounds.md'
x,k,s=S.symbols('x k s',positive=True)
N,j=S.symbols('N j',integer=True,nonnegative=True)
cases=[]
def check(name,value):
 assert value,name
 cases.append({'name':name,'passed':True})
r=-N+j;t=-j
check('total mixed order is invariant',S.simplify(r+t+N)==0)
check('source total order at every step',S.simplify(r+t-2+N+2)==0)
check('last input normal order',r.subs(j,N+1)==1)
check('last input tangential order',t.subs(j,N+1)==-N-1)
check('final normal order',r.subs(j,N+2)==2)
check('final tangential order',t.subs(j,N+2)==-N-2)
check('N equals two index chain',[(-2+i,-i) for i in range(5)]==[(-2,0),(-1,-1),(0,-2),(1,-3),(2,-4)])
check('value trace order',S.simplify(2-N-2-S.Rational(1,2)+N+S.Rational(1,2))==0)
check('normal trace order',S.simplify(2-N-2-1-S.Rational(1,2)+N+S.Rational(3,2))==0)
u=S.Function('u')(x);c=S.Function('c')(x)
check('complete normal cutoff commutator',S.simplify(-S.diff(c*u,x,2)+c*S.diff(u,x,2)+2*S.diff(c,x)*S.diff(u,x)+S.diff(c,x,2)*u)==0)
h=s*S.exp(-s)
for m in range(4):
 check('boundary-layer derivative '+str(m),S.simplify(S.diff(h,s,m)-(-1)**m*(s-m)*S.exp(-s))==0)
 check('exact derivative squared norm '+str(m),S.integrate((s-m)**2*S.exp(-2*s),(s,0,S.oo))==S.Rational(2*m*m-2*m+1,4))
uk=k**(-S.Rational(3,2))*(k*x)*S.exp(-k*x)
check('actual zero value',uk.subs(x,0)==0)
check('actual normal trace sign',S.simplify((-S.I*S.diff(uk,x)).subs(x,0)+S.I*k**(-S.Rational(1,2)))==0)
check('actual forcing',S.simplify(-S.diff(uk,x,2)-S.sqrt(k)*(2-k*x)*S.exp(-k*x))==0)
v=(S.exp(-k*x)-S.exp(-2*k*x))/k
for m,expected in enumerate([1/(12*k**3),1/(6*k),11*k/6]):
 check('second example norm '+str(m),S.simplify(S.integrate(S.diff(v,x,m)**2,(x,0,S.oo))-expected)==0)
check('second example zero value',v.subs(x,0)==0)
check('second example fixed normal trace',(-S.I*S.diff(v,x)).subs(x,0)==-S.I)
out={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Exact index transfer, cutoff commutator, source and trace signs, and derivative integrals. Baire, operator bounds and graph completeness are proved in the lesson.',
 'cases':cases}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
