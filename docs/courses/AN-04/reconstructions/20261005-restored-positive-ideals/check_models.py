"""Finite controls for U028; these do not certify the unrestricted written proofs."""
import hashlib,json,subprocess,sys,math
from pathlib import Path
import sympy as s
import numpy as np
here=Path(__file__).resolve().parent
lesson=here/'positive-lagrangian-ideals-and-distributions.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
p=subprocess.run([sys.executable,'-X','utf8',str(here/'check_algebra.py'),'--check-only'],check=True,capture_output=True,text=True,encoding='utf-8')
old=json.loads(p.stdout.strip());assert old['passed'] and old['finite_model_groups']==8 and old['no_course_or_source_writes']
checks.append({'name':'Eight retained source-preparation model families','passed':True,'scope':'Exact graph degrees, full normal phase, crossing/rank change, cubic sign obstruction, twelve actual Gaussian integrations, complete orders/constants, six flat derivatives and actual Mellin partitions.','script_sha256':sha(here/'check_algebra.py')})
p=subprocess.run([sys.executable,'-X','utf8',str(here/'check_uniform_division.py')],check=True,capture_output=True,text=True,encoding='utf-8')
division=json.loads((here/'uniform-division-checks.json').read_text(encoding='utf-8'))
assert division['passed'] and len(division['checks'])==3
checks.append({'name':'Three retained uniform-division controls','passed':True,'scope':'Whole bivariate polynomial identity, twelve genuinely nonholomorphic path integrals with wrong-sign negative control, and thirteen diagonal cutoff levels.','report_sha256':sha(here/'uniform-division-checks.json')})
B=s.Matrix([[0,1],[1,0]]);C=s.diag(1,0);e=s.Rational(1,4);u=e*B
M=C+2*e*B*B-e*e*B*C*B
assert (B+s.I*C).det()!=0 and C.det()==0 and M==s.diag(s.Rational(3,2),s.Rational(7,16))
Y=s.Matrix(s.symbols('y0 y1',real=True));U=u*Y;A=B+s.I*C
expr=s.expand(-s.im(((U-s.I*Y).T*A*(U-s.I*Y))[0]))
assert s.simplify(expr-(Y.T*M*Y)[0])==0
checks.append({'name':'Full critical-value matrix with a null imaginary direction','passed':True,'scope':'Actual invertible symmetric matrix with singular nonnegative imaginary part; complete quadratic identity and positive lower bound 7/16.'})
q=s.symbols('q');nodes=[s.Rational(-1),s.Rational(-1,3),s.Rational(1,3),s.Rational(1)]
weights=[s.prod((s.I-nodes[k])/(nodes[j]-nodes[k]) for k in range(4) if k!=j) for j in range(4)]
for k in range(4):assert s.simplify(sum(weights[j]*nodes[j]**k for j in range(4))-s.I**k)==0
for k in range(1,4):assert s.simplify(sum(weights[j]*(nodes[j]-s.I)**k for j in range(4)))==0
checks.append({'name':'Actual complex evaluation by real polynomial interpolation','passed':True,'scope':'Four real nodes reproduce evaluation at i for all cubic polynomials, and annihilate the three positive powers of s-i used in flat-residue necessity.'})
r,z=s.symbols('r z',positive=True);a=s.symbols('a',real=True);F=s.exp(-r*r/(z*z));H=-s.I*r*F
assert s.simplify(r*s.diff(H,r)+z*s.diff(H,z)-H)==0
assert s.simplify(s.diff(H,z)+2*s.I*r**3*F/z**3)==0
counter=[]
for lam in [12.,24.,48.,72.]:
    rad=math.exp(lam);ang=1/math.sqrt(lam);G=rad*math.exp(-1/(ang*ang))
    value=math.exp(-G)*rad**(-.5)
    assert abs(G-1)<3e-14
    assert abs(value/(math.exp(-1)*rad**(-.5))-1)<3e-14
    counter.append({'log_radius':lam,'imaginary_damping':G,'normalized_damped_value':value*math.sqrt(rad)})
checks.append({'name':'Actual failure of damping for nonuniform smooth-ideal coefficients','passed':True,'scope':'Degree-one flat-imaginary H and exact nonzero transverse derivative, with four increasing frequencies verifying e^-1 r^-1/2 on the moving angular support. Written derivative estimates establish S^0; this finite sampling does not prove the general symbol assertion.','samples':counter})
for t in [4.,16.,64.,256.]:
    assert math.exp(t-math.sqrt(t))>t
checks.append({'name':'Absolute error cannot be divided by exponential damping','passed':True,'scope':'Four explicit positive frequencies for E=e^-sqrt(t) illustrate the written rapid-error counterexample.'})
text=lesson.read_text(encoding='utf-8');assert text.count('**Exercise ')==text.count('**Solution.**')==17
required=['uniform symbol ideal','absolute Fourier errors','every** such phase','The plus sign','printed page 36','(10.10)','Exercise 17']
for v in required:assert v in text,v
checks.append({'name':'Authored lesson and explicit hypothesis boundaries','passed':True,'scope':'Seventeen paired original solutions and explicit source degree, bounded-ideal, Gaussian branch, absolute-error and two-way representation contracts. This is a content guard, not proof verification.'})
report={'schema':'positive-ideal-finite-author-controls/v1','passed':True,'lesson':lesson.name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),'checks':checks,'independent_review':False,'full_source_parent_closed':False,'limitations':'Finite models and explicit hypothesis controls support the original written proofs. The complete written analytic proofs are checked separately; finite controls do not certify general theorems or whole-course completion.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'checks':len(checks),'lesson_sha256':sha(lesson),'solutions':17}))
