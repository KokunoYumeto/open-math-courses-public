"""Finite algebra and high-precision checks for the Airy energy-space proof.

Independent code: CC0-1.0. These checks do not replace the uniform proofs.
"""
from pathlib import Path
import hashlib,json
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=55
groups=[]
def group(name,kind,cases):
 assert cases and all(cases)
 groups.append({'name':name,'kind':kind,'cases':len(cases),'passed':True})
t,q,k,b=s.symbols('t q k b',real=True)
f,g=s.Function('f')(t),s.Function('g')(t)
rules={s.diff(f,t,2):t*f,s.diff(g,t,2):t*g}
p0=t*f*g-s.diff(f,t)*s.diff(g,t)
p1=(s.diff(f,t)*g+f*s.diff(g,t)+t*s.diff(f,t)*s.diff(g,t)-t*t*f*g)/3
group('Airy equation, energy primitives and Wronskian', 'exact algebra',[
 s.expand(-k*k*(b-k*q)-(q*k**3-b*k*k))==0,
 s.simplify(s.diff(p0,t).subs(rules)-f*g)==0,
 s.simplify(s.diff(p1,t).subs(rules)-s.diff(f,t)*s.diff(g,t))==0,
 s.simplify(s.diff(f*s.diff(g,t)-s.diff(f,t)*g,t).subs(rules))==0])
I=s.I
C=s.Matrix([[1,1],[-I,I]])
group('Stable and normalized two-mode coefficient conversion','exact matrix algebra',[
 C.det()==2*I,
 C.conjugate().T*C==2*s.eye(2),
 C.inv()==s.Matrix([[s.Rational(1,2),I/2],[s.Rational(1,2),-I/2]])])
E=s.Matrix([[0,1],[0,0]]);S=s.eye(2)+q*E;Sinv=s.eye(2)-q*E
group('Nonunitary matrix gauge and boundary sign','exact matrix algebra',[
 E*E==s.zeros(2),
 S*Sinv==s.eye(2),
 s.simplify(S*(-I*s.diff(Sinv,q)))==I*E,
 s.simplify(-(-I*s.diff(S,q))*Sinv)==I*E,
 2*I*E==2*S*(-I*s.diff(Sinv,q))])
# A complex scalar polynomial checks the actual linear-first boundary form.
u=(1+I)*q*q+(2-I)*q+3
w=(1-q)**2*(1+I*q);m=(2+3*I)*(1-q)
D=lambda z:-I*s.diff(z,q)
extra=-m*D(u)*s.conjugate(w)+m*u*s.conjugate(D(w))-D(m)*u*s.conjugate(w)
group('Robin weak form retains derivative-on-test terms','exact polynomial integration',[
 s.simplify(s.integrate(s.expand(extra),(q,0,1))+I*m.subs(q,0)*u.subs(q,0)*s.conjugate(w.subs(q,0)))==0,
 s.simplify(s.diff(u,q).subs(q,0)-I*D(u).subs(q,0))==0])

def vals(x):
 return mp.airyai(x),mp.airybi(x),mp.airyai(x,1),mp.airybi(x,1)
def primitives(x):
 a,d,ap,dp=vals(x)
 v=[a,d];dv=[ap,dp]
 return (mp.matrix([[x*v[i]*v[j]-dv[i]*dv[j] for j in range(2)] for i in range(2)]),
         mp.matrix([[(dv[i]*v[j]+v[i]*dv[j]+x*dv[i]*dv[j]-x*x*v[i]*v[j])/3 for j in range(2)] for i in range(2)]))
def gram(lam,bval,Q=mp.mpf(1)):
 kval=lam**(mp.mpf(2)/3)
 hi0,hi1=primitives(bval);lo0,lo1=primitives(bval-kval*Q)
 return lam**2/kval*(hi0-lo0)+kval*(hi1-lo1)
def weights(lam,bval):
 pos=max(bval,mp.mpf(0))
 wa=lam**(mp.mpf(5)/3)
 return wa,wa+lam**(mp.mpf(4)/3)*mp.exp(mp.mpf(4)/3*pos**mp.mpf('1.5'))/mp.sqrt(1+pos*pos)
def eigenvalues(lam,bval):
 gg=gram(lam,bval);wa,wb=weights(lam,bval)
 z=mp.matrix([[gg[0,0]/wa,gg[0,1]/mp.sqrt(wa*wb)],[gg[1,0]/mp.sqrt(wa*wb),gg[1,1]/wb]])
 return list(mp.eigsy(z,eigvals_only=True))
eigen_records=[];checks=[]
for lam in map(mp.mpf,[8,64,512]):
 for v in map(mp.mpf,['-0.1','-0.02','0','0.02','0.1']):
  bv=v*lam**(mp.mpf(2)/3);ev=eigenvalues(lam,bv)
  checks.append(ev[0]>0 and ev[1]>=ev[0])
  eigen_records.append({'lambda':str(lam),'b_over_k':str(v),'eigenvalues':[mp.nstr(x,24) for x in ev]})
group('Exact-primitive energy Gram matrices are positive on sampled modes','55-digit numerical checks',checks)
quadrature=[];checks=[]
for lam,bv in [(mp.mpf(8),mp.mpf('-0.4')),(mp.mpf(8),mp.mpf('0.4')),(mp.mpf(64),mp.mpf('1.6'))]:
 kval=lam**(mp.mpf(2)/3);lo=bv-kval;hi=bv
 intervals=[lo+(hi-lo)*j/32 for j in range(33)]
 gg=gram(lam,bv);error=mp.mpf(0)
 for i,j in [(0,0),(0,1),(1,1)]:
  def integrand(x):
   aa,bb,ap,bp=vals(x);v=[aa,bb];dv=[ap,bp]
   return lam**2/kval*v[i]*v[j]+kval*dv[i]*dv[j]
  val=mp.quad(integrand,intervals)
  error=max(error,abs(val-gg[i,j])/(1+abs(val)))
 checks.append(error<mp.mpf('1e-40'))
 quadrature.append({'lambda':str(lam),'b':str(bv),'max_relative_entry_error':mp.nstr(error,8)})
group('Primitive formulas agree with independently integrated energy entries','55-digit numerical quadrature',checks)
alpha=s.symbols('alpha',positive=True)
group('Transition and hyperbolic energy exponents','exact exponent algebra',[
 s.Rational(5,3)-1==s.Rational(2,3),
 s.Rational(5,3)+s.Rational(1,3)==2,
 s.Rational(4,3)-s.Rational(1,3)==1,
 s.Rational(5,3)-2*s.Rational(5,6)==0])
result={'passed':True,'groups':groups,'total_cases':sum(x['cases'] for x in groups),
 'exact_cases':sum(x['cases'] for x in groups if x['kind'].startswith('exact')),
 'numerical_cases':18,'gram_samples':eigen_records,'quadrature':quadrature,
 'scope':'Finite algebra, signs, sampled positivity and quadrature only; uniform estimates and weak completeness are proved in the lesson.',
 'source_sha256':hashlib.sha256((ROOT/'airy-energy-spaces-and-weak-boundary-data.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['gram_samples','quadrature','groups']}))

