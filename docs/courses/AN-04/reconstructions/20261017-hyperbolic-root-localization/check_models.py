"""Finite symbolic and numerical controls for the written root/localization proofs."""
from pathlib import Path
import hashlib,json,re,itertools
import sympy as s
import numpy as np
ROOT=Path(__file__).resolve().parent
src=ROOT/'hyperbolic-roots-stability-and-quadratic-localization.md'
text=src.read_text('utf-8-sig');checks=[]
z,eta,R,w,t,x,j=s.symbols('z eta R w t x j',real=True)
assert s.expand(((z-eta)**2+eta).subs(z,eta-s.I*s.sqrt(eta)))==0
checks.append({'name':'Exact quadratic root splitting at positive tangential frequency','passed':True})
u=s.exp(s.I*j*j*(x+t)+j*t)
Dt=lambda f:-s.I*s.diff(f,t)
Dx=lambda f:-s.I*s.diff(f,x)
assert s.simplify(Dt(Dt(u)-Dx(u))-Dx(Dt(u)-Dx(u))+Dx(u))==0
assert s.simplify(Dt(u)-(j*j-s.I*j)*u)==0
checks.append({'name':'Exact growing plane wave and both initial Cauchy jets','passed':True})
for k in range(2,8):
 for extra in [0,2]:
  eps=s.Rational(1,100);poly=s.expand(w**k*(1+eps*w/3)**extra+1)
  coeff=[float(c) for c in s.Poly(poly,w).all_coeffs()]
  roots=np.roots(coeff)
  candidates=[np.exp(1j*(np.pi+2*np.pi*n)/k) for n in range(k)]
  target=min(candidates,key=lambda q:q.imag)
  assert np.count_nonzero(np.abs(roots-target)<.04)==1
checks.append({'name':'Twelve scaled multiple-root perturbations, including separated extra factors','passed':True,
 'scope':'Finite root-count samples; R5 supplies the general coefficient-limit proof.'})
for freq in [0,.1,1,10,100,1000,10000]:
 roots=np.roots([1,5+2j,-freq*freq+(3-1j)*freq+17])
 assert max(abs(r.imag) for r in roots)<20
checks.append({'name':'A strict two-root principal polynomial with fixed complex lower terms','passed':True,
 'scope':'Seven frequency samples; R1--R3 supply the uniform strip proof.'})
for k in range(1,6):
 roots=s.symbols('r0:'+str(k))
 moments={i:sum(r**i for r in roots) for i in range(1,k+1)}
 e={0:s.Integer(1)}
 for n in range(1,k+1):
  e[n]=s.expand(sum((-1)**(i-1)*e[n-i]*moments[i] for i in range(1,n+1))/n)
  direct=sum(s.prod(c) for c in itertools.combinations(roots,n))
  assert s.expand(e[n]-direct)==0
checks.append({'name':'Newton moment recursion through clusters of size five','passed':True})
param=s.symbols('param',real=True)
cluster=(z-param)*(z-2*param)*(z+3*param)
assert s.expand(cluster-(z**3-7*param**2*z+6*param**3))==0
assert param**2+(2*param)**2+(-3*param)**2==14*param**2
full=s.expand(cluster*(z-5))
assert all(s.diff(full,a,b).subs({param:0,z:0})==0 for a in [param,z] for b in [param,z])
checks.append({'name':'Three-root variance, cubic localization and zero full Hessian','passed':True})
ww,ee,rr,cc,ss=s.symbols('ww ee rr cc ss',real=True)
A=ee**2-rr**2;B=ww*ee-cc*rr;C=ww**2-ss
assert s.expand(B**2-A*C-((rr*ww-cc*ee)**2+A*(ss-cc**2)))==0
assert s.expand((ww*ee)**2-ee**2*(ww**2-ss)-ee**2*ss)==0
checks.append({'name':'Full quadratic discriminant identity and the zero-seminorm branch','passed':True})
y1,y2,tt=s.symbols('y1 y2 tt',real=True)
quad=(z+2*y2)**2-y1**2
assert s.expand(quad.subs(y2,y2+tt)-(z+2*y2+2*tt-y1)*(z+2*y2+2*tt+y1))==0
checks.append({'name':'Degenerate sheared cone and exact changed-direction roots','passed':True})
p=z**3-t*z*eta**2
point={t:0,eta:1,z:0}
assert all(s.diff(p,a).subs(point)==0 for a in [t,eta,z])
H=s.hessian(p,[t,eta,z]).subs(point);v=s.Matrix(s.symbols('dt deta dz'))
assert s.expand((v.T*H*v)[0]/2+v[0]*v[2])==0
checks.append({'name':'One-sided cubic genuine characteristic and nonnormal hyperbolic Hessian','passed':True})
quartic=(z*z-t)*(z*z-2*t)
H=s.hessian(quartic,[t,z]).subs({t:0,z:0})
v=s.Matrix(s.symbols('dt dz'))
assert s.expand((v.T*H*v)[0]/2-2*v[0]**2)==0
checks.append({'name':'One-sided quartic with a nonzero rank-one quadratic localization','passed':True})
zz,zp,zm=s.symbols('zz zp zm')
assert s.simplify((zz-zm)/(zp-zm)+(zz-zp)/(zm-zp)-1)==0
checks.append({'name':'Exact distributional two-root ODE projections','passed':True})
assert [int(k) for k in re.findall(r'\\tag\{RL(\d+)\}',text)]==list(range(1,33))
assert text.count('**Solution.**')==4
checks.append({'name':'Equation-label order and four complete solution bodies','passed':True,
 'scope':'Structural control; neither counts nor symbolic samples certify the analytic arguments.'})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'passed':all(c['passed'] for c in checks),'finite_groups':len(checks),'checks':checks,
 'source_hashes':{src.name:sha(src)},'script_sha256':sha(Path(__file__)),
 'finite_checks_replace_written_proofs':False,'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                             }
(ROOT/'model-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':record['passed'],'finite_groups':len(checks),'solutions':4}))
