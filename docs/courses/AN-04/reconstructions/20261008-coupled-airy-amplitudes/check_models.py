"""Independent exact checks for coupled Airy calculus; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S
q,y,mu,lam,u,w,z,a0=S.symbols('q y mu lam u w z a0', real=True)
I=S.eye(2);N=S.Matrix([[0,1],[0,0]]);M=N.T
groups=[]
def check(name,tests):
 tests=list(tests)
 for label,r in tests:
  entries=list(r) if isinstance(r,S.MatrixBase) else [r]
  for x in entries:assert S.simplify(S.expand(x))==0,(name,label,x)
 groups.append({'name':name,'cases':len(tests),'all_passed':True})
# Basis pairs represent A(zeta), A'(zeta); chain differentiation uses A''=zeta A.
x=[q,y];theta=q*q*y+y;zet=q+y*y
aa=S.Matrix([[1+q,q*y],[q*y,2+y]])
b=[N+q*M,M+y*N];cc=N*M+q*I
gg=I+q*N+y*M+q*y*N*M;hh=M+q*I+y*y*N
def diffpair(pair,j):
 f0,f1=pair;return (f0.diff(x[j])+zet*S.diff(zet,x[j])*f1,f1.diff(x[j])+S.diff(zet,x[j])*f0)
def D(pair,j):
 d0,d1=diffpair(pair,j);return (S.diff(theta,x[j])*pair[0]-S.I*d0,S.diff(theta,x[j])*pair[1]-S.I*d1)
pair=(gg,S.I*hh);got=[S.zeros(2),S.zeros(2)]
for j in range(2):
 for k in range(2):
  term=D(D(pair,k),j)
  for r in range(2):got[r]+=aa[j,k]*term[r]
 term=D(pair,j)
 for r in range(2):got[r]+=b[j]*term[r]
for r in range(2):got[r]+=cc*pair[r]
def bil(f,g):return sum(aa[j,k]*S.diff(f,x[j])*S.diff(g,x[k]) for j in range(2) for k in range(2))
def delta(f):return sum(aa[j,k]*S.diff(f,x[j],x[k]) for j in range(2) for k in range(2))
def K(f):return delta(f)*I+S.I*sum((b[j]*S.diff(f,x[j]) for j in range(2)),S.zeros(2))
def T(f,g):return 2*sum((aa[j,k]*S.diff(f,x[j])*g.diff(x[k]) for j in range(2) for k in range(2)),S.zeros(2))+K(f)*g
def P(g):return -sum((aa[j,k]*g.diff(x[j],x[k]) for j in range(2) for k in range(2)),S.zeros(2))-S.I*sum((b[j]*g.diff(x[j]) for j in range(2)),S.zeros(2))+cc*g
E1=bil(theta,theta)-zet*bil(zet,zet);E2=bil(theta,zet);Q=bil(zet,zet)
L1=T(theta,gg)+zet*T(zet,hh)+Q*hh;L2=T(theta,hh)-T(zet,gg)
want=[E1*gg+2*zet*E2*hh-S.I*L1+P(gg),S.I*(E1*hh-2*E2*gg-S.I*L2+P(hh))]
check('Full variable-coefficient matrix product rule',[(f'basis {k} entry {j}',got[k][j]-want[k][j]) for k in range(2) for j in range(4)])
s=S.symbols('s');kt=N+q*M;kz=M+y*N
vg=N+y*I;vh=M+q*I;zg=I+N*M;zh=N+M
# Independent formal derivatives of g,h along V_theta,V_zeta, and H_p s=-Q.
lift=vg+s*zg+Q*hh-s*vh-s*s*zh+(kt+s*kz)*(gg-s*hh)
rhs=vg-s*s*zh+Q*hh+kt*gg-s*s*kz*hh-s*(vh-zg+kt*hh-kz*gg)
ae=gg-s*hh;ai=gg+s*hh
ea=(ae+ai)/2;oa=(ae-ai)/(2*s/w)
firsth=N*gg+M;firsta=gg-s*firsth;firstai=gg+s*firsth
secondg=-s*s*N*hh+M;seconda=secondg-s*hh;secondai=secondg+s*hh
check('Smooth lift and both boundary parity powers',[(f'ordered lift entry {j}',lift[j]-rhs[j]) for j in range(4)]+[
 ('actual odd part',oa+w*hh),
 ('first boundary conversion',(firsta-firstai)/(2*s/w)+w*N*(firsta+firstai)/2+w*M),
 ('second boundary conversion',(seconda+secondai)/2-(s/w)**2*w*N*(seconda-secondai)/(2*s/w)-M)])
J=S.Matrix([[0,u*w],[-w,0]]);Ji=S.Matrix([[0,-1/w],[1/(u*w),0]])
check('Elliptic normal inverse and degree bookkeeping',[
 ('left inverse',Ji*J-I),('right inverse',J*Ji-I),('determinant',J.det()-u*w*w),
 ('L1 degrees',S.Rational(2,3)+S.Rational(2,3)-S.Rational(1,3)-1),
 ('L2 degrees',1-S.Rational(1,3)-S.Rational(2,3)),
 ('phase error h degree',S.Rational(2,3)+S.Rational(5,3)-S.Rational(1,3)-2),
 ('recursion sign',(-S.I)*(-S.I)+1)])
H=(I+q*N)*(I+q*M);Hi=(I-q*M)*(I-q*N);B=S.simplify(H.diff(q)*Hi)
check('Exact noncommuting gauge example',[
 ('H inverse',H*Hi-I),('first transport',H.diff(q)-B*H),
 ('second derivative',H.diff(q,2)-(B.diff(q)+B*B)*H),
 ('operator on H',-H.diff(q,2)+2*B*H.diff(q)+(B.diff(q)-B*B)*H),
 ('boundary lower matrix',H.diff(q).subs(q,0)-N-M),('boundary value',H.subs(q,0)-I),
 ('actual noncommutator',N*M-M*N-S.diag(1,-1))])
# Parametrize lambda=k^3 to make all fractional homogeneous powers exact polynomials.
k=S.symbols('k',positive=True);zet0=-q*k*k-mu/k
check('Affine eikonal and actual conormal row',[
 ('eikonal',(-q*k**6-mu*k**3)-zet0*k**4),('normal sign',-S.I*S.diff(zet0,q)-S.I*k*k),
 ('boundary argument',zet0.subs(q,0)+mu/k),('normal block determinant',S.det(S.Matrix([[0,-2*u],[2,0]]))-4*u)])
check('Scaled flat gain and exact diagram peak',[
 ('scale',(z/(lam*S.sqrt(u)))**4*u*u-z**4/lam**4),
 ('peak derivative',S.diff(z**4*S.exp(-2*z/3),z).subs(z,6)),
 ('peak value',(z**4*S.exp(-2*z/3)).subs(z,6)-(6/S.E)**4),
 ('strict peak curvature',S.diff(z**4*S.exp(-2*z/3),z,2).subs(z,6)+144/S.E**4)])
root=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'groups':groups,'total_cases':sum(g['cases'] for g in groups),
 'source_sha256':sha(root/'coupled-matrix-airy-amplitudes.md'),'script_sha256':sha(Path(__file__)),
 'scope':'Exact symbolic identities and degree checks; all existence, summation and smoothing arguments are in the lesson.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'total_cases':out['total_cases'],'groups':len(groups)}))
