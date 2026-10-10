"""Exact checks of the displayed models; these do not certify the analytic proof."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
rows=[]
def check(name,actual,expected=0):
 diff=s.simplify(actual-expected);assert diff==0,(name,diff)
 rows.append({'name':name,'passed':True,'kind':'exact algebra'})
t,h,beta=s.symbols('t h beta',real=True)
x=t**2;z=-s.Rational(2,3)*t**3;xi=t
check('UD29 normal Hamilton equation',s.diff(x,t),2*xi)
check('UD29 normal covector equation',s.diff(xi,t),1)
check('UD29 tangential Hamilton equation',s.diff(z,t),-2*x)
check('UD29 characteristic identity',xi**2-x)
check('UD29 compressed covector',x*xi,t**3)
for a in [-1,1]:
 tt=s.Rational(a,4)
 check(f'UD29 cap x sign {a}',x.subs(t,tt),s.Rational(1,16))
 check(f'UD29 cap z sign {a}',z.subs(t,tt),-s.Rational(a,96))
 check(f'UD29 cap compressed covector sign {a}',(x*xi).subs(t,tt),s.Rational(a,64))
eta,xx,zz=s.symbols('eta x z',real=True)
r=xx*eta**2
check('stationary boundary field base coefficient',s.diff(r.subs(xx,0),eta))
check('stationary boundary field covector coefficient',-s.diff(r.subs(xx,0),zz))
check('strict normal derivative',s.diff(r,xx),eta**2)
check('UD30 characteristic family',xi**2-((xi**2-beta)+beta))
check('UD30 time, interior turn',s.integrate(1,(t,-s.sqrt(h+beta),s.sqrt(h+beta))),2*s.sqrt(h+beta))
check('UD30 displacement, interior turn',s.integrate(-2*t**2,(t,-s.sqrt(h+beta),s.sqrt(h+beta))),-s.Rational(4,3)*(h+beta)**s.Rational(3,2))
bp,hp=s.symbols('beta_positive h_positive',positive=True)
check('UD30 time, reflected arcs',s.integrate(1,(t,-s.sqrt(hp+bp),-s.sqrt(bp)))+s.integrate(1,(t,s.sqrt(bp),s.sqrt(hp+bp))),2*(s.sqrt(hp+bp)-s.sqrt(bp)))
check('UD30 displacement, reflected arcs',s.integrate(-2*t**2,(t,-s.sqrt(hp+bp),-s.sqrt(bp)))+s.integrate(-2*t**2,(t,s.sqrt(bp),s.sqrt(hp+bp))),-s.Rational(4,3)*((hp+bp)**s.Rational(3,2)-bp**s.Rational(3,2)))
check('UD30 tangent travel time',2*s.sqrt(s.Rational(1,16)),s.Rational(1,2))
check('UD30 tangent displacement',-s.Rational(4,3)*s.Rational(1,16)**s.Rational(3,2),-s.Rational(1,48))
check('UD30 lower cap root bound squared',s.Rational(1,16)-s.Rational(1,64),(s.sqrt(3)/8)**2)
check('UD30 right continuity of travel time',s.limit(2*(s.sqrt(hp+bp)-s.sqrt(bp)),bp,0,dir='+'),2*s.sqrt(hp))
check('UD30 right continuity of displacement',s.limit(-s.Rational(4,3)*((hp+bp)**s.Rational(3,2)-bp**s.Rational(3,2)),bp,0,dir='+'),-s.Rational(4,3)*hp**s.Rational(3,2))
d=s.Rational(1,64);M=2
R=lambda q:1/(2*q)+M/(1-M*q)
check('UD31 first slope',R(d),s.Rational(1056,31))
check('UD31 second slope',R(d/2),s.Rational(4160,63))
check('UD31 slope difference',R(d/2)-R(d),s.Rational(62432,1953))
check('UD31 first square coefficient',1/d-M,62)
check('UD31 second square coefficient',2/d-M,126)
check('UD31 damping factor',9*M*d,s.Rational(9,32))
check('UD31 first incoming gap',d*d,s.Rational(1,4096))
check('UD31 second incoming gap',(d/2)**2,s.Rational(1,16384))
f=s.Function('f')(xx);v=s.Function('v')(xx);A=s.Function('A')(xx)
D=lambda q:-s.I*s.diff(q,xx)
check('UD9 exact opposite-root product',D(D(v)-A*v)+A*(D(v)-A*v),D(D(v))-(A*A-s.I*s.diff(A,xx))*v)
# The stated residual is A^2 - i A' - R: product (D+A)(D-A)=D^2+i A'-A^2.
check('UD11 positive-i primitive',D(s.I*s.integrate(f,xx)),f)
source=ROOT/'uniform-strict-diffraction-with-an-interior-observation.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'scope':'Exact Hamilton models, cap integrals, symbol row coefficients and operator signs. The analytic proof is in the lesson.','checks':rows}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))
