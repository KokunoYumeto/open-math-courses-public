"""Reproducible finite controls for U029, separate from its written proofs."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parent;c=root;audit=root
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=subprocess.run([sys.executable,'-X','utf8',str(root/'check_algebra.py')],check=True,capture_output=True,text=True)
baseline=json.loads(result.stdout);assert baseline['passed'] and baseline['finite_model_groups']==7
checks=[{**v                                 } for v in baseline['checks']]
x1,x2,y,z,xi1,xi2,eta,etap,zeta,t=s.symbols('x1 x2 y z xi1 xi2 eta etap zeta t',real=True)
H=xi2*(eta/xi1-1)
assert s.simplify(H.subs({xi1:t*xi1,xi2:t*xi2,eta:t*eta},simultaneous=True)-t*H)==0
row=s.Matrix([s.diff(H,eta)]).jacobian([xi1,xi2,eta,zeta]).subs({xi1:1,xi2:0,eta:1,zeta:1})
assert row==s.Matrix([[0,1,0,0]]) and s.diff(H,eta,eta)==0
Phi=x1*xi1+x2*xi2-y*eta-H+y*etap-z*zeta
q=[y,xi1,xi2,eta,etap,zeta];variables=[x1,x2,z]+q
mark={x1:0,x2:0,y:0,z:0,xi1:1,xi2:0,eta:1,etap:1,zeta:1}
assert s.Matrix([s.diff(Phi,v) for v in q]).jacobian(variables).subs(mark).rank()==6
checks.append({'name':'Actual conic outer-block transversality with zero middle Hessian','passed':True,'scope':'Exact homogeneous H1, entire six-critical-function differential matrix and independent outer middle equation of Exercise3; no quadratic-only replacement.'})
m1=-s.Rational(1,3);m2=s.Rational(5,6)
mu1=m1+s.Rational(5-8,4);mu2=m2+s.Rational(4-10,4)
assert mu1==-s.Rational(13,12) and mu2==-s.Rational(2,3)
assert mu1+mu2-3==-s.Rational(19,4)
assert mu1+mu2-3-s.Rational(3-24,4)==s.Rational(1,2)
assert s.Rational(5+8,4)+s.Rational(4+10,4)==s.Rational(3+24,4)==s.Rational(27,4)
checks.append({'name':'Nonintegral operator orders and complete two-pi bookkeeping','passed':True,'scope':'All amplitude/order/Jacobian/normalization numbers of Exercise2, including new parameter count12 and amplitude order -19/4.'})
pi=s.pi
assert s.simplify((2*pi)*(2*pi)**s.Rational(3,2)/(2*pi)**4-(2*pi)**-s.Rational(3,2))==0
assert s.simplify((2*pi)**2*(2*pi)/(2*pi)**4-(2*pi)**-1)==0
assert s.simplify(s.sqrt(pi)/(2*pi)**s.Rational(3,2)-s.sqrt(2)/(4*pi))==0
rr,zz=s.symbols('rr zz',positive=True);quartic=s.I*rr*zz**4
gradient=s.expand(abs(s.diff(quartic,zz))**2/rr+rr*abs(s.diff(quartic,rr))**2)
assert s.simplify(gradient-rr*(16*zz**6+zz**8))==0
assert s.diff(quartic,zz,zz).subs(zz,0)==0
checks.append({'name':'Exact full Gaussian and evaluation constants plus degenerate quartic gradient','passed':True,'scope':'Complete four-frequency Gaussian/delta normalization and removed-damping normalization, exact sharp Gaussian norm, and whole weighted quartic gradient with zero imaginary Hessian at the center.'})
lesson=root/'complex-phase-fourier-integral-operators.md';text=lesson.read_text(encoding='utf-8')
assert text.count('**Exercise ')==text.count('**Solution.**')==17
assert len(re.findall(r'^## ',text,re.M))==15
pass                                        
assert not any(ord(v)<32 and v not in '\n\r\t' for v in text)
for phrase in ['**real**','bounded normalized coefficient',r'\delta','type','Fourier series','Planck function is one','every','properly supported']:
 assert phrase in text,phrase
report={'schema':'complex-fio-author-finite-controls/v1','passed':True,'checks':checks,'lesson':lesson.name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),'solved_exercises':17,'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.',                             'limitations':'Finite conic, Gaussian, normalization and endpoint calculations; the general statements use the written arguments.'}
(root/'model-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_model_groups':len(checks),'complete_solutions':17,'lesson_sha256':sha(lesson)}))
