from pathlib import Path
import sympy as s
import json,hashlib,math
checks=[]
t,y,eta,x,xi=s.symbols('t y eta x xi',real=True)
z=s.exp(t)*s.sinh(y);W=s.sqrt(1+z*z);X=s.asinh(z)
J=s.exp(t)*s.cosh(y)/W;Xi=eta/J
assert s.simplify(s.diff(X,y)-J)==0
assert s.simplify(s.diff(X,t)-z/W)==0
assert s.simplify(s.diff(Xi,t)+Xi/(W*W))==0
M=s.Matrix([X,Xi]).jacobian([y,eta]);Om=s.Matrix([[0,-1],[1,0]])
assert s.simplify(M.det()-1)==0
assert s.simplify(M.T*Om*M-Om)==s.zeros(2)
assert s.simplify(Xi.subs(y,0)-s.exp(-t)*eta)==0
E,h=s.symbols('E h',positive=True);jj=E*E*(1+h*h)/(1+E*E*h*h)
assert s.factor(jj-1)==(E-1)*(E+1)/(E*E*h*h+1)
assert s.factor(E*E-jj)==E*E*h*h*(E-1)*(E+1)/(E*E*h*h+1)
checks.append({'name':'Complete variable-speed cotangent flow','passed':True,'scope':'Actual arsinh base map, complete two-by-two Jacobian, symplectic pullback, Hamilton equations, radial scaling and marked covector e^-t eta. Exact Jacobian inequalities reduce to positive factors for E>=1; no sampled substitute for the general flow proof.'})

Y=s.asinh(s.exp(-t)*s.sinh(x));V=s.sqrt(1+s.exp(-2*t)*s.sinh(x)**2)
Eta=s.exp(t)*V*xi/s.cosh(x)
def transport(v):return s.diff(v,t)+s.tanh(x)*s.diff(v,x)-xi/s.cosh(x)**2*s.diff(v,xi)
assert s.simplify(transport(Y))==0
assert s.simplify(transport(Eta))==0
q=s.exp(-Y*Y)*Eta**2
assert s.simplify(transport(q))==0
q0=s.exp(-Y*Y);qm1=q0/Eta
assert s.simplify(transport(q0))==0
assert s.simplify(transport(qm1))==0
checks.append({'name':'Full leading-symbol characteristic transport','passed':True,'scope':'Both inverse-flow coordinate equations and three entire composite tests of degrees0,-1,2 satisfy the exact Hamilton transport equation. The degree minus1 case uses the positive-frequency cone; the degree2 case is a diagnostic, not the order-zero teaching commutant.'})

lam=s.symbols('lam',positive=True);r=s.symbols('r',positive=True)
norms=[]
for p in [1,2,4,8]:
 integral=s.integrate(s.exp(-p*lam*r/2),(r,0,s.oo))
 assert s.simplify(integral-2/(p*lam))==0
 assert s.simplify(lam*integral/2-s.Rational(1,p))==0
 norms.append({'p':p,'kernel_integral':str(integral),'normalized_norm':f'{p}^(-1/{p}) <= 1'})
norms.append({'p':'infinity','kernel_norm':1,'normalized_norm':1,'lambda_prefactor':False})
c,L=s.symbols('c L',real=True)
assert s.simplify((c-L)-(-L/2))==c-L/2
checks.append({'name':'Every-p weighted convolution constants','passed':True,'scope':'Exact half-line kernel integrals at p=1,2,4,8 and exact infinity maximum convention; the common threshold lambda>max(0,2c) is kept strict. General Minkowski/energy proof is written separately.','values':norms})

gamma,cv,sv=s.symbols('gamma cv sv',real=True)
symbol=s.I*cv*xi+gamma
weight=(1+xi*xi)**(sv/2)
assert s.simplify(weight*symbol/weight-symbol)==0
C=t+t*t/2;G=gamma*t
u=s.exp(-G)*s.exp(-(x-C)**2)
assert s.simplify(s.diff(u,t)+(1+t)*s.diff(u,x)+gamma*u)==0
t0,t1,t2=s.symbols('t0 t1 t2',real=True);Cfun=lambda z:z+z*z/2
assert s.expand((Cfun(t2)-Cfun(t1))+(Cfun(t1)-Cfun(t0))-(Cfun(t2)-Cfun(t0)))==0
assert s.expand(Cfun(t+t1)-Cfun(t)-Cfun(t1))==t*t1
checks.append({'name':'All-real-order multiplier and nonautonomous solution','passed':True,'scope':'Exact arbitrary-real Sobolev multiplier conjugation, complete translated Gaussian solution including damping, two-time cocycle and explicit failure of the autonomous one-time group formula.'})

rr,rr0=s.symbols('rr rr0',real=True);U=s.Function('U')(x)
coeff=s.tanh(x)
assert s.simplify(s.diff(coeff,x)-1/s.cosh(x)**2)==0
# For a real scalar test, Re(c u' u)=1/2 c (u^2)'; after integration this is -c'/2.
assert s.expand(coeff*s.diff(U,x)*U-coeff*s.diff(U**2,x)/2)==0
positive_a=s.I*coeff*xi
assert s.re(positive_a)==0
checks.append({'name':'Symbol real part versus operator energy','passed':True,'scope':'Entire integration-by-parts identity for tanh(x) d_x and exact negative half-divergence energy term, while the scalar left symbol has zero real part. No skew-adjointness is inferred from the principal symbol.'})

# A fixed Gaussian has a rapidly vanishing translated-window mass, while a translated input does not.
from math import erf, sqrt, pi
ww,center=s.symbols('ww center',real=True)
assert s.integrate(s.exp(-ww*ww)/s.sqrt(s.pi),(ww,-s.oo,s.oo))==1
assert s.simplify(s.integrate(s.exp(-ww*ww)/s.sqrt(s.pi),(ww,center-1,center+1))-(s.erf(center+1)-s.erf(center-1))/2)==0
windows=[]
for R in [0.,2.,4.,8.]:
 mass=(erf(R+1)-erf(R-1))/2
 assert 0<=mass<=1
 windows.append({'window_center':R,'fixed_normalized_gaussian_mass':mass})
assert windows[0]['fixed_normalized_gaussian_mass']>windows[1]['fixed_normalized_gaussian_mass']>windows[2]['fixed_normalized_gaussian_mass']>=windows[3]['fixed_normalized_gaussian_mass']
fixed_mass=(erf(1)-erf(-1))/2
assert fixed_mass>0
checks.append({'name':'Escaped-window strong versus norm continuity','passed':True,'scope':'Exact complete normalized Gaussian window integral formula and four numeric evaluations (the largest-center value rounds to zero); a translated input has a fixed nonzero window mass. Written isometry/range argument, not these samples, proves the exact H1-to-L2 operator norm equals the fixed cutoff supremum.','samples':windows,'translated_input_window_mass':fixed_mass})

freq=s.symbols('freq',positive=True)
for sign in [-1,1]:
 sol=s.exp(-sign*t*freq)
 assert s.simplify(s.diff(sol,t)+sign*freq*sol)==0
assert s.limit((t*freq-s.sqrt(freq))/freq,freq,s.oo)==t
sample=[{'time':tt,'frequency':ff,'growth_log':tt*ff-math.sqrt(ff)} for tt in [.25,.5,1.] for ff in [16,64,256]]
checks.append({'name':'Forward smoothing and forbidden negative growth','passed':True,'scope':'Exact Fourier ODE with both real-principal signs, whole exponential rate relative to subexponentially decaying smooth data, and nine explicitly labelled growth samples. Temperedness obstruction and wavefront smoothing require the written distribution proof.','samples':sample})

# Complete finite degree enumeration in the scalar commutator through j=7.
terms=[]
for j in range(8):
 allterms=[(k,l,q) for k in range(j+1) for l in range(j+1) for q in range(1,j+2) if k+l+q==j+1]
 leading=(0,j,1);assert leading in allterms
 lower=[v for v in allterms if v!=leading]
 assert all(l<j and 1-k-l-q==-j for k,l,q in lower)
 terms.append({'degree':-j,'leading':list(leading),'lower_terms':[list(v) for v in lower]})
checks.append({'name':'Full recursive commutator order budget','passed':True,'scope':'All k,l,|alpha| triples through j=7, exact homogeneous degree and strictly lower Q-index after the leading Hamilton term is removed. Infinite-order remainder/summation proof remains a written obligation.','enumeration':terms})

t,x=s.symbols('t x',real=True);freq=s.symbols('freq',positive=True)
N=s.Matrix([[0,1],[0,0]]);A=freq*N;F=s.eye(2)-t*A
assert N*N==s.zeros(2)
assert s.diff(F,t)+A*F==s.zeros(2)
hermitian=(A+A.T)/2;assert hermitian.eigenvals()=={-freq/2:1,freq/2:1}
assert (s.Matrix([1,-1]).T*hermitian*s.Matrix([1,-1]))[0]==-freq
checks.append({'name':'Complete Jordan-system energy obstruction','passed':True,'scope':'Whole two-by-two propagator solves the exact system ODE; Hermitian spectrum and negative-form vector are exact, despite nonnegative entries and zero symbol eigenvalues. The written annular datum proves actual Sobolev loss.'})
Y=s.asinh(s.exp(-t)*s.sinh(x));Yx=s.diff(Y,x);half=s.sqrt(Yx)*s.exp(-Y*Y)
cvar=s.tanh(x)
assert s.simplify(s.diff(half,t)+cvar*s.diff(half,x)+s.diff(cvar,x)*half/2)==0
gamma=s.symbols('gamma',real=True);C=t+t*t/2
u=s.exp(-gamma*t)*(1+t**3/3)*s.exp(-(x-C)**2)
forcing=s.exp(-gamma*t)*t*t*s.exp(-(x-C)**2)
assert s.simplify(s.diff(u,t)+(1+t)*s.diff(u,x)+gamma*u-forcing)==0
ss,xi=s.symbols('ss xi',real=True);ww=(1+xi*xi)**(ss/2)
cprime=s.symbols('cprime',real=True)
correction=s.diff(ww,xi)*cprime*xi/ww
assert s.simplify(correction-ss*cprime*xi*xi/(1+xi*xi))==0
checks.append({'name':'Exact half-density generator, forcing and fractional correction','passed':True,'scope':'Entire normalized tanh half-density Gaussian solves the equation with plus half-divergence; complete nonautonomous forced Gaussian solves its equation; arbitrary-real Sobolev first correction has the displayed sign and radial factor.'})

# Exact finite polynomial composition: the temporal derivative occurs only for AB.
tt,xx,ta,xxi=s.symbols('tt xx ta xxi',real=True)
aa=ta**2+xxi**2;bb=tt*xx*xxi
ab=aa*bb+s.diff(aa,ta)*s.diff(bb,tt)/s.I+s.diff(aa,xxi)*s.diff(bb,xx)/s.I
ba=bb*aa
assert s.expand(ab-ba+2*s.I*(ta*xx*xxi+tt*xxi**2))==0
assert s.expand(ab-ba+2*s.I*tt*xxi**2)!=0
for degree in range(1,12):assert sum((-1)**j*math.comb(degree,j) for j in range(degree+1))==0
checks.append({'name':'Mixed multiplication order and adjoint cancellation','passed':True,'scope':'Finite polynomial diagnostic, not a symbol satisfying the conic hypothesis: AB has both temporal and spatial correction terms, BA has neither; omission of the temporal term is rejected. Full binomial adjoint cancellation through degree11.'})
DF=s.Matrix([[0],[1]]);tau,xi=s.symbols('tau xi',real=True)
assert DF.T*s.Matrix([tau,xi])==s.Matrix([xi])
checks.append({'name':'Slice normals and characteristic lift','passed':True,'scope':'Exact transpose of the time-slice embedding; its kernel is precisely xi=0. No reverse wavefront containment is inferred from this matrix test.'})
assert len(checks)==12 and all(c['passed'] for c in checks)
MOD=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'finite_groups':len(checks),'checks':checks,'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name:sha(p) for p in MOD.glob('*.md')},'original_solved_exercises':16,
 'limitation':'Finite controls supplement the full written owner proof review; they do not certify the general theorems.'}
(MOD/'model-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks),'original_solved_exercises':16}))
