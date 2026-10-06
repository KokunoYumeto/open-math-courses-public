"""Author checks of explicit U027 models; general classification remains written proof."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
import numpy as np
import sympy as s

here=Path(__file__).resolve().parent
lesson=here/'quadratic-hamilton-maps-and-positive-complex-planes.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def omega(n):return s.zeros(n).row_join(-s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
def ham(B):return -omega(B.rows//2)*B
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
checks=[]
p=subprocess.run([sys.executable,'-X','utf8',str(here/'check_algebra.py'),'--check-only'],check=True,capture_output=True,text=True,encoding='utf-8')
historical=json.loads(p.stdout.strip())
assert historical['passed'] and historical['checks']==8 and not historical['writes']
checks.append({'name':'Retained eight preparation model families','passed':True,
 'preparation_script_sha256':sha(here/'check_algebra.py'),
 'scope':'All eight finite matrix, spectral, graph and hypothesis model families run without state writes or book inputs.'})

x,p,t=s.symbols('x p t',real=True)
J1=omega(1)
f=x*x+3*p*p+2*x*x*p
assert s.hessian(f,(x,p)).subs({x:0,p:0})==s.diag(2,6)
hf=-J1*s.Matrix([s.diff(f,x),s.diff(f,p)])
assert hf==s.Matrix([6*p+2*x*x,-2*x-4*x*p])
assert hf.jacobian((x,p)).subs({x:0,p:0})==2*s.Matrix([[0,3],[-1,0]])
r=(s.Rational(3,2))**s.Rational(1,4)
change=s.Matrix([[r,0],[1/r,1/r]])
B=s.Matrix([[5,2],[2,2]])
assert zero(change.T*J1*change-J1)
assert zero(change.inv().T*B*change.inv()-s.sqrt(6)*s.eye(2))
assert zero((s.Matrix([x,p]).T*(change.T*s.Matrix([[0,0],[1,0]])*change-s.Matrix([[0,0],[1,0]]))).T-s.Matrix([x,0]))
checks.append({'name':'Exact critical-point factor and complete oscillator coordinate change','passed':True,
 'scope':'Full Hamilton derivative, entire canonical matrix, normalized quadratic form and one-form coefficient difference.'})

J=omega(2)
B4=s.Matrix([[0,0,0,0],[0,1,0,0],[0,0,0,-1],[0,0,-1,0]])
F4=ham(B4)
T=s.eye(4)+t*F4+t*t*F4**2/2+t**3*F4**3/6
expected=s.Matrix([[1,t*t/2,-t**3/6,-t],[0,1,-t,0],[0,0,1,0],[0,-t,t*t/2,1]])
assert T==expected
assert zero(s.diff(T,t)-F4*T)
assert zero(T.T*J*T-J) and zero(T.T*B4*T-B4)
assert T*s.Matrix([0,0,1,0])==s.Matrix([-t**3/6,-t,1,t*t/2])
alternate=ham(s.diag(1,1,0,-1))
q=s.symbols('q')
assert alternate.charpoly(q).as_expr()==q**4-q*q
assert F4.charpoly(q).as_expr()==q**4
mixed=ham(s.diag(2,3,1,-1,2,3,0,0))
assert s.factor(mixed.charpoly(q).as_expr())==q**4*(q*q+4)*(q*q+9)
assert mixed.rank()==6 and all((mixed**j).rank()==4 for j in [2,3,4])
checks.append({'name':'Full nilpotent exponential and all graded real block invariants','passed':True,
 'scope':'Whole polynomial flow and conserved matrices, same-inertia inequivalence by spectra, and exact mixed 8-dimensional ranks and characteristic polynomial.'})

u=s.symbols('u',real=True)
BJ=s.Matrix([[1,u/2,0,-s.I*u/2],[u/2,1,s.I*u/2,0],[0,s.I*u/2,1,u/2],[-s.I*u/2,0,u/2,1]])
FJ=ham(BJ)
M=s.eye(2).col_join(s.I*s.eye(2))
N=s.Matrix([[1,u],[0,1]])
assert zero(FJ*M-M*s.I*N)
assert s.factor(FJ.charpoly(q).as_expr())==(q*q+1)**2
assert zero((FJ*FJ+s.eye(4))**2)
assert (FJ.subs(u,1)-s.I*s.eye(4)).rank()==3
assert (FJ.subs(u,0)-s.I*s.eye(4)).rank()==2
flow=s.exp(s.I*t)*(s.eye(2)+s.I*t*s.Matrix([[0,u],[0,0]]))
assert zero(s.diff(flow,t)-s.I*N*flow)
assert zero(s.I*s.conjugate(M).T*J*M-2*s.eye(2))
# Hermite interpolation produces a whole-matrix exact upper spectral projector.
projection=s.eye(4)/2-s.I*(FJ**3+3*FJ)/4
standard=s.eye(4)/2-s.I*ham(s.eye(4))/2
assert zero(projection-standard)
assert zero(projection**2-projection) and zero(FJ*projection-projection*FJ)
P=s.re(BJ);R=s.im(BJ)
for value in [s.Rational(0),s.Rational(1,3),s.Rational(2,3),s.Rational(1)]:
    pn=np.array(P.subs(u,value),dtype=float);rn=np.array(R.subs(u,value),dtype=float)
    assert np.linalg.eigvalsh(pn).min()>=.5-1e-12
    assert all(np.linalg.eigvalsh(pn+sign*rn).min()>0 for sign in [1,-1])
checks.append({'name':'Actual sectorial Jordan homotopy, exact generalized projection and flow','passed':True,
 'parameter_scope':'Exact polynomial identities for every real u; sector/positivity samples u=0,1/3,2/3,1',
 'scope':'Full 4-by-4 Hamilton matrix, nonsemisimple spectrum, changing geometric multiplicity, fixed positive generalized plane, Hermite projector and entire restricted exponential.'})

maximum_contour=0.
for value in [0.,1/3,2/3,1.]:
    f=np.array(FJ.subs(u,value),dtype=complex)
    expected=np.array(projection.subs(u,value),dtype=complex)
    # Counterclockwise circle centered at i; radius .75 includes +i, excludes -i.
    theta=2*np.pi*np.arange(1024)/1024
    actual=sum(.75*np.exp(1j*a)*np.linalg.inv((1j+.75*np.exp(1j*a))*np.eye(4)-f) for a in theta)/1024
    maximum_contour=max(maximum_contour,float(np.linalg.norm(actual-expected)))
    assert np.linalg.norm(actual-expected)<1e-12
    assert np.linalg.norm(actual@actual-actual)<1e-12
    assert np.linalg.norm(-actual-expected)>2 # detects the opposite resolvent sign with unchanged orientation
assert maximum_contour<1e-12
checks.append({'name':'Independent oriented resolvent integration through the Jordan degeneracy','passed':True,
 'parameter_samples':4,'angular_samples_each':1024,'maximum_projection_residual':maximum_contour,
 'scope':'Actual numerical resolvent quadrature compared with the independently derived exact Hermite projection; wrong-sign control fails. Not a general spectral-continuity proof.'})

A1=s.Matrix([[1,2],[2,-1]])
A2=s.Matrix([[2,s.Rational(1,3)],[s.Rational(1,3),1]])
assert A2.inv()==s.Matrix([[9,-3],[-3,18]])/17
D=(A2+s.sqrt(17)*s.eye(2)/3)/s.sqrt(3+2*s.sqrt(17)/3)
assert zero(D*D-A2)
change=D.row_join(s.zeros(2)).col_join((-D.inv()*A1).row_join(D.inv()))
assert zero(change.T*J*change-J)
graph=s.eye(2).col_join(A1+s.I*A2)
image=change*graph
assert zero(image[2:,:]-s.I*image[:2,:])
IR=(-A2.inv()*A1).row_join(A2.inv()).col_join((-A2-A1*A2.inv()*A1).row_join(A1*A2.inv()))
assert IR*IR==-s.eye(4) and IR.T*J*IR==J
G=J*IR
assert G==G.T
for m in range(1,5):assert G[:m,:m].det()>0
assert zero(s.I*s.conjugate(graph).T*J*graph/2-A2)
checks.append({'name':'Exact full graph normalization, Hermitian factor and compatible metric','passed':True,
 'scope':'Closed radical square root, whole real canonical matrix, positive complex graph, full structure identities and every leading metric minor.'})

scalar=(2+s.I)*s.eye(2);fs=ham(scalar);v=s.Matrix([1,s.I])
assert zero(fs*v-(-1+2*s.I)*v)
assert s.simplify(s.I*(s.conjugate(v).T*J1*fs*v)[0]/2-(-1+2*s.I))==0
bad=ham(s.diag(1,0,s.I,-s.I));X=s.Matrix([0,0,1,s.I])
assert (s.conjugate(X).T*s.diag(1,0,s.I,-s.I)*X)[0]==0
assert bad*X==s.Matrix([s.I,1,0,0])
bad2=ham(s.Matrix([[1,s.I],[s.I,-1]]));X2=s.Matrix([1,s.I])
assert zero(bad2*X2) and bad2*s.re(X2)!=s.zeros(2,1) and bad2*s.im(X2)!=s.zeros(2,1)
zero_sector_b=s.diag(1,-1)
assert s.im(zero_sector_b)==s.zeros(2) and ham(zero_sector_b).eigenvals()=={-1:1,1:1}
weak=s.Matrix.hstack(s.Matrix([0,0,1,0]),s.Matrix([0,1,0,s.I]))
assert weak.T*J*weak==s.zeros(2) and s.simplify(s.I*s.conjugate(weak).T*J*weak)==s.diag(0,2)
weakgraph=s.eye(2).col_join(s.I*s.diag(1,0))
rotation=s.Matrix([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,-1,0,0]])
assert rotation.T*J*rotation==J and (rotation*weakgraph)[:2,:].rank()==1
checks.append({'name':'Complex scalar numerical range, sector failures including C=0 and non-strict planes','passed':True,
 'scope':'Exact scalar value, genuine kernel failures, indefinite real form under the vacuous zero-sector inequality, all weak-plane pairings and full Fourier rotation; does not establish the arbitrary quotient proof.'})

text=lesson.read_text(encoding='utf-8')
assert text.count('**Exercise ')==text.count('**Solution.**')==14
assert not any(ord(ch)<32 and ch not in '\n\r' for ch in text)
assert not re.search(r'(?<![\\A-Za-z])(?:qquad|quad)\b',text)
assert '=left(' not in text
report={'schema':'author-quadratic-form-computational-check/v1','passed':True,
 'lesson':lesson.name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'checks':checks,'exercise_solution_count':14,'general_mathematical_certification':False,
 'limitations':'The unrestricted signature exhaustion, generalized spectral pairing, common-contour continuation, compatible-structure uniqueness and positive quotient arguments are written proofs; finite models do not certify them. Independent review remains open.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'lesson_sha256':sha(lesson),'independent_review':False}))
