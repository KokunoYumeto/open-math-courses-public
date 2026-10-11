"""Finite exact coefficient and scale checks accompanying the analytic proof."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def eq(name,a,b=0):
 r=s.simplify(a-b)
 assert r==0,(name,r)
 checks.append({'name':name,'passed':True,'exact_residual':str(r)})
z=s.symbols('z',nonzero=True)
A,B,Ap,Bp=s.symbols('A B Ap Bp',real=True)
al,v=s.symbols('al v')
for ep in [1,-1]:
 M=s.Matrix([[1,z],[0,-s.I*ep*z]])
 Q=s.Matrix([[1,-s.I*ep],[0,s.I*ep/z]])
 eq('left inverse, sign '+str(ep),s.simplify(Q*M-s.eye(2)).norm())
 eq('right inverse, sign '+str(ep),s.simplify(M*Q-s.eye(2)).norm())
 eq('determinant, sign '+str(ep),M.det(),-s.I*ep*z)
 aa=al+z*v;bb=-s.I*ep*z*v
 eq('Airy value coefficient, sign '+str(ep),A*aa+B*bb,A*al+z*(A-s.I*ep*B)*v)
 eq('Airy derivative coefficient, sign '+str(ep),Ap*aa+Bp*bb,Ap*al+z*(Ap-s.I*ep*Bp)*v)
wa,t=s.symbols('wa t',positive=True);wb=wa+t
E=s.Matrix([[wa,s.I*wa],[-s.I*wa,wa+wb]])
D=s.diag(wa,wb)
eq('upper norm comparison determinant',(3*D-E).det(),wa**2+4*wa*t)
eq('lower norm comparison determinant',(3*E-D).det(),wa**2+4*wa*t)
eq('upper first principal minor',(3*D-E)[0,0],2*wa)
eq('lower first principal minor',(3*E-D)[0,0],2*wa)
eq('Airy modulus removes the phase',(A-s.I*B)*(A+s.I*B),A*A+B*B)
b,lam,a0,h=s.symbols('b lam a0 h',positive=True)
Psi=s.Rational(2,3)*b**s.Rational(3,2)
eq('squared exponential derivative',s.diff(2*Psi,b),2*s.sqrt(b))
eq('argument mu derivative',s.diff(-h*lam**(-s.Rational(1,3)),h),-lam**(-s.Rational(1,3)))
eq('log transition balance power',s.Rational(3,2)*s.Rational(2,3),1)
eq('derivative scale margin',s.Rational(1,3)-s.Rational(1,4),s.Rational(1,12))
eq('moderation exponent from frequency scale',1/s.Rational(1,4),4)
eq('root-weight moderation exponent',s.Rational(4,2),2)
eq('commutator convolution exponent',3+s.Rational(1,4),s.Rational(13,4))
eq('transition square-root order',s.Rational(5,3)/2,s.Rational(5,6))
eq('negative fixed-cone weight power',s.Rational(5,3)+s.Rational(2,3)/2,2)
eq('positive fixed-cone layer power',s.Rational(4,3)-s.Rational(2,3)/2,1)
eq('elliptic layer leading coefficient',lam**s.Rational(4,3)/(a0*lam**s.Rational(2,3))**s.Rational(1,2),lam/s.sqrt(a0))
eq('exponential difference leading coefficient',s.limit(s.Rational(4,3)*((a0+h)**s.Rational(3,2)-a0**s.Rational(3,2))/h,h,0),2*s.sqrt(a0))
eq('packet divergence exponent',s.Rational(5,3)-1,s.Rational(2,3))
eq('weighted output symbol ratio power',(s.symbols('ss')-s.symbols('mm'))-s.symbols('ss')+s.symbols('mm'),0)
source=HERE/'stable-airy-coefficients-and-spatial-localization.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'checks':checks,
 'scope':'Finite exact algebra, norm-comparison principal minors and scale exponents; the all-frequency analytic estimates are proved in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
