"""Exact finite checks accompanying the proofs; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S
t,s,v=S.symbols('t s v',real=True)
I=S.eye(2);N=S.Matrix([[0,1],[0,0]]);M=N.T
groups=[]
def group(name,checks):
 checks=list(checks)
 for label,x in checks:
  if isinstance(x,S.MatrixBase): assert x.applyfunc(S.simplify)==S.zeros(*x.shape),(name,label,x)
  else: assert S.simplify(x)==0,(name,label,x)
 groups.append({'name':name,'cases':len(checks),'all_passed':True})
def H(x):return (I+x*N)*(I+x*M)
a=H(t+s/2);ai=a.subs(s,-s)
E=S.simplify((a+ai)/2);O=S.simplify((a-ai)/(2*s))
group('Two exchanges and polynomial solution',[
 ('I squared',-(-s)-s),('J squared',t+s-s-t),('J invariant w',t+s-s/2-(t+s/2)),
 ('a J invariant',a.subs({t:t+s,s:-s},simultaneous=True)-a),
 ('even part',E-H(t)-s*s*N*M/4),('odd part',O-(N+M)/2-t*N*M),
 ('matrix inverse',H(v)*(I-v*M)*(I-v*N)-I),('determinant',H(v).det()-1),
 ('contract A',O-O*E.inv()*E)])
checks=[]
for p in range(5):
 # Independent polynomial coefficients and direct expansion check both parity formulas.
 aa=sum((s**(2*j)*(t+s/2)**(2*(p-j)+3) for j in range(p+1)),S.Integer(0))
 ee=S.expand((aa+aa.subs(s,-s))/2).coeff(s,2*p)
 oo=S.expand((aa-aa.subs(s,-s))/(2*s)).coeff(s,2*p)
 ep=sum(S.diff(t**(2*(p-j)+3),t,2*p-2*j)/(2**(2*p-2*j)*S.factorial(2*p-2*j)) for j in range(p+1))
 op=sum(S.diff(t**(2*(p-j)+3),t,2*p-2*j+1)/(2**(2*p-2*j+1)*S.factorial(2*p-2*j+1)) for j in range(p+1))
 checks.extend([(f'E coefficient {p}',ee-ep),(f'O coefficient {p}',oo-op)])
group('Parity coefficients through power eight',checks)
# Two independent symbolic matrices verify product parity with no commutation assumed.
HE=S.Matrix([[1,t],[0,1]]);HO=M;uE=I+v*M;uO=N+t*M
h=HE+s*HO;u=uE+s*uO
group('Ordered product and both gauge reductions',[
 ('product even',(h*u+(HE-s*HO)*(uE-s*uO))/2-HE*uE-s*s*HO*uO),
 ('product odd',(h*u-(HE-s*HO)*(uE-s*uO))/(2*s)-HE*uO-HO*uE),
 ('odd rearrangement',HE*uO+HO*uE-N*(HE*uE+s*s*HO*uO)-((HE-s*s*N*HO)*uO-(N*HE-HO)*uE)),
 ('even rearrangement',HE*uE+s*s*HO*uO-s*s*N*(HE*uO+HO*uE)-((HE-s*s*N*HO)*uE+s*s*(HO-N*HE)*uO))])
C=N+t*M;f=I+M;R=(I-s*C).inv()*(I+s*C);q=2*s*(I-s*C).inv()*f
d=I+t*N;RB=-R;qB=2*(I-s*C).inv()*d
group('Both exact difference recurrences',[
 ('A homogeneous',(I-s*C)*R-(I+s*C)),('A forcing',(I-s*C)*q-2*s*f),
 ('B homogeneous',(I-s*C)*RB+(I+s*C)),('B forcing',(I-s*C)*qB-2*d)])
RN=I+2*s*N;RM=I+2*s*M;e1=S.Matrix([1,0]);ss=S.Rational(1,4)
group('Solved exercises and exact figure coordinates',[
 ('ordered product',RN*RM-I-2*s*(N+M)-4*s*s*N*M),
 ('commutator',RN*RM-RM*RN-4*s*s*S.diag(1,-1)),
 ('first endpoint',(RN*RM*e1).subs(s,ss)-S.Matrix([S.Rational(5,4),S.Rational(1,2)])),
 ('second endpoint',(RM*RN*e1).subs(s,ss)-S.Matrix([1,S.Rational(1,2)])),
 ('forced solution even',((t+s/2)+(t-s/2))/2-t),
 ('forced solution odd',((t+s/2)-(t-s/2))/(2*s)-S.Rational(1,2)),
 ('I image w',S.Rational(1,5)-S.Rational(3,10)+S.Rational(1,10)),
 ('J image w',S.Rational(4,5)-S.Rational(3,10)-S.Rational(1,2)),
 ('final translation',S.Rational(2,5)-8*S.Rational(1,5)+S.Rational(6,5))])
root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'groups':groups,'total_cases':sum(g['cases'] for g in groups),
 'source_sha256':sha(root/'matrix-parity-and-folded-transport.md'),'script_sha256':sha(Path(__file__)),
 'scope':'Exact rational and symbolic identities; the smooth existence and all-derivative estimates are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'total_cases':out['total_cases'],'groups':len(groups)}))
