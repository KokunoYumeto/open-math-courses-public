"""Finite mathematical checks; analytic proofs are reviewed separately. CC0."""
from pathlib import Path
import hashlib,json,re
import sympy as s
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
src=ROOT/'principal-type-hyperbolic-boundaries-and-cauchy-problems.md'
text=src.read_text('utf8')
groups = []
t, z, lam = s.symbols('t z lam', positive=True)
tau, eta, cc = s.symbols('tau eta c', real=True)
p = (tau**2-t*eta**2)*(tau-3*eta)
assert s.expand((s.diff(p,t)*s.diff(p,tau,2)).subs({tau:0,t:0})) == -18*eta**4
groups.append({'name':'Exercise 1 boundary signs', 'passed':True})
M3 = s.Matrix([[-cc,1,0],[0,-cc,1],[-t,0,1]])
M4 = s.Matrix([[cc**2,-2*cc,1,0],[0,cc**2,-2*cc,1],[0,0,1,0],[0,0,0,1]])
assert s.expand(M3.det()) == cc**2-t
assert s.expand(M4.det()) == cc**4
groups.append({'name':'Exercises 6 and 7 complete cluster basis determinants', 'passed':True})
F = 2*z**3+z**2+2*z+3
assert s.expand((1+z)*F-(z*z+1)**2) == z**4+3*z**3+z*z+5*z+2
assert s.expand(4*F-(1+2*z)**2) == 8*z**3+4*z+11
groups.append({'name':'Forward Hardy and half-power interpolation', 'passed':True})
w=s.exp(-2*lam*t)
r=w/t**2
assert s.simplify(-s.diff(r,t)-2*w*(lam/t**2+t**-3))==0
ratio=(lam/t**2+t**-3)**2/(t**-2+lam/t)
assert s.simplify(ratio.subs(lam,z/t)-t**-4*(z+1))==0
assert all(v>0 for v in s.Poly(F-z-1,z).all_coeffs())
assert s.simplify((w/t**2)**2/(w/t)-w/t**3)==0
groups.append({'name':'Additional singular-weight multiplier and interpolation coefficients', 'passed':True,
               'scope':'Scalar weight algebra only; the integrated operator argument is separately author-reviewed, not automatically certified.'})
psi=w/t
K=lam**2/t+t**-3
assert s.simplify(r*r/psi-w/t**3)==0
assert s.simplify(w*K-r*r/psi-w*lam**2/t)==0
groups.append({'name':'Retained terminal multiplier weights on the original force interval','passed':True,
               'scope':'Exact endpoint weight algebra; retained trace estimates are justified in the written argument.'})
R,Q,j=s.symbols('R Q j',real=True)
assert s.simplify(2*R+2*Q-2*j-2+1-2*(R+Q-j-s.Rational(1,2)))==0
groups.append({'name':'Scaled Fourier trace lift half-order norm exponent','passed':True,
               'scope':'Fourier change-of-variable exponent; Schwartz integrability and actual traces are proved in the draft.'})
wp=s.exp(2*lam*t)
assert s.simplify(s.diff(t*t*wp,t)-wp*(2*t+2*lam*t*t))==0
assert s.simplify(s.diff(t*wp,t)-wp*(1+2*lam*t))==0
groups.append({'name':'Backward first-order weight and lower-jet Hardy derivative', 'passed':True})
q,h,b,k,rho=s.symbols('q h b k rho',real=True)
matrix=s.Matrix([[2*q*h,s.I*q*k/rho],[-s.I*q*k/rho,2*q*h*b/rho**2]])
assert matrix==s.conjugate(matrix.T)
assert s.factor(matrix.det())==q*q*(4*b*h*h-k*k)/rho**2
groups.append({'name':'Source-oriented Hermitian matrix signs and determinant', 'passed':True})
for normal in range(-6,7):
    for tangential in range(-6,7):
        assert normal+tangential == normal+1+tangential-1
        for m in range(1,7):
            assert (normal+m)+(tangential-1) == (normal+m-1)+tangential
groups.append({'name':'Normal recovery and support induction total-order bookkeeping', 'passed':True})
for m in range(1,7):
    for j in range(m):
        for a in range(5):
            assert s.Rational(a+m-j)-s.Rational(1,2)-(a+m-1-j)==s.Rational(1,2)
            assert a+m>j+s.Rational(1,2)
groups.append({'name':'Extra data half-order and trace thresholds', 'passed':True})

r0,s0=s.symbols('r0 s0',real=True)
Rpoly=tau**3+2*tau+7
Rr=Rpoly.subs(tau,r0);Rs=Rpoly.subs(tau,s0)
V=(tau-s0)/((r0-s0)*Rr)+(tau-r0)/((s0-r0)*Rs)
assert s.simplify((Rpoly*V-1).subs(tau,r0))==0
assert s.simplify((Rpoly*V-1).subs(tau,s0))==0
Vdouble=1/Rr-s.diff(Rpoly,tau).subs(tau,r0)/Rr**2*(tau-r0)
assert s.simplify((Rpoly*Vdouble-1).subs(tau,r0))==0
assert s.simplify(s.diff(Rpoly*Vdouble-1,tau).subs(tau,r0))==0
groups.append({'name':'Both exact distinct and double quotient-ring inverses','passed':True})
ss=s.symbols('ss',real=True);xx=-2*ss**3/3;tt=ss**2;zz=ss
assert s.diff(tt,ss)==2*zz and s.diff(zz,ss)==1 and s.diff(xx,ss)==-2*tt
assert zz**2-tt==0
groups.append({'name':'Exact full Hamilton trajectory, characteristic identity and second normal derivative','passed':True})
eps=s.Rational(1,5);kap=(1-3/s.sqrt(10))**2
assert 0<kap<eps/2
for j0 in range(1,12):
 a=eps/2*(1-s.Rational(2)**(1-2*j0))
 b=eps/2*(1-s.Rational(2)**(-2*j0))
 an=eps/2*(1-s.Rational(2)**(1-2*(j0+1)))
 assert 0<a<b<an<eps/2
groups.append({'name':'Exact nested profile thresholds and strictly positive common finite-frequency collar','passed':True})
assert text.count('**Solution.**')==20
assert re.findall(r'^### \*\*Exercise (\d+) —',text,re.M)==[str(i) for i in range(1,21)]
assert re.findall(r'\\tag\{PT(\d+)\}',text)==[str(i) for i in range(1,42)]
assert re.findall(r'\\tag\{PTA(\d+)\}',text)==[str(i) for i in range(1,6)]
groups.append({'name':'All20original solved exercises and41original plus5new labels retained','passed':True})
result={'passed':True,'finite_groups':len(groups),'checks':groups,'script_sha256':sha(Path(__file__)),
 'source_hashes':{src.name:sha(src)},'original_solved_exercises':20,
 'limitations':'Finite symbolic diagnostics do not replace the full source and analytic proof review.',
 'whole_course_complete':False,'public_release_authorized':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(groups),'solutions':20}))
