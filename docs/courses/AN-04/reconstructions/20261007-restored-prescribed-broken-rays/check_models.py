"""Finite exact algebra checks, supplementing rather than certifying the full proof."""
from pathlib import Path
import hashlib,json,sympy as S
c=Path(__file__).resolve().parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
t,z,L,omega=S.symbols('t r L omega',real=True);F=S.Function('c')
u=F(t+z)-F(t-z)
assert S.simplify(S.diff(u,t,2)-S.diff(u,z,2))==0
assert u.subs(z,0)==0 and S.simplify(-S.I*S.diff(u,z).subs(z,0)+2*S.I*S.diff(F(t),t))==0
checks=[{'name':'Exact flat paired wave and intrinsic trace','passed':True,'equations':['P(c(t+r)-c(t-r))=0','gamma0=0','gamma1=-2i c-prime'],'comparison':'BG33-BG35; normal trace sign fixed by ordering.'}]
pieces=[(S.Rational(1,2)+t,-1,0,S.Rational(1,2)),(S.Rational(3,2)-t,1,S.Rational(1,2),S.Rational(3,2)),(t-S.Rational(3,2),-1,S.Rational(3,2),S.Rational(5,2)),(S.Rational(7,2)-t,1,S.Rational(5,2),3)]
polys=[]
for radius,rho,a,b in pieces:
    assert S.diff(radius,t)==-rho
    assert 0<=radius.subs(t,a)<=1 and 0<=radius.subs(t,b)<=1
    polys.append(S.expand(radius*(1-radius)*rho))
for j in range(3):assert pieces[j][0].subs(t,pieces[j][3])==pieces[j+1][0].subs(t,pieces[j+1][2]) and pieces[j][1]==-pieces[j+1][1]
assert polys==[t*t-S.Rational(1,4),-t*t+2*t-S.Rational(3,4),t*t-4*t+S.Rational(15,4),-t*t+6*t-S.Rational(35,4)]
checks.append({'name':'Three exact strip reflections and two-wall compression','passed':True,'radii':[str(p[0]) for p in pieces],'compressed_quadratics':list(map(str,polys)),'Hamilton_reversal':'s=-t/2 implies dt/ds=-2 and dr/ds=2rho','comparison':'BG31-BG32 and exact SVG.'})
x,lam=S.symbols('x lambda',real=True,positive=True);chi=S.Function('chi');v=S.symbols('v',real=True)
a=chi(x**3*lam)
for j in range(4):
 for k in range(4):
    derivative=S.diff(a,x,j,lam,k).subs(x,v*lam**(-S.Rational(1,3)))
    normalized=S.simplify(derivative*lam**(-S.Rational(j,3)+k))
    assert not normalized.has(lam)
checks.append({'name':'Cubic mixed derivative scaling','passed':True,'finite_mixed_pairs':16,'scaling':'partial_s^j partial_lambda^k = lambda^(j/3-k) F_jk(v), v=lambda^(1/3)(s-b)','Fourier_gain_per_integration':'lambda^(-2/3) for abs(sigma)>=epsilon lambda','comparison':'BG36-BG39; full induction and compact support estimates supplied in solution.'})
m=S.symbols('m',integer=True,positive=True);w=S.pi/L
for q in range(1,6):
 mode=S.exp(S.I*q*w*(t+z))-S.exp(S.I*q*w*(t-z))
 assert S.simplify(S.diff(mode,t,2)-S.diff(mode,z,2))==0
 assert S.simplify(mode.subs(z,0))==0 and S.simplify(S.expand_complex(mode.subs(z,L)))==0
checks.append({'name':'Periodic strip modes','passed':True,'positive_modes_checked':5,'period':'2L','two_exact_Dirichlet_values':True,'comparison':'BG40-BG43; full distribution convergence, smoothness and single-positive wavefront proved in solution, not inferred from finite modes.'})
s,K,k=S.symbols('s K k',real=True);beta=(k+2)/4
exponent=S.simplify(2*s+2*K-2*beta+k/2)
assert exponent==2*s+2*K-1
checks.append({'name':'Gaussian derivative Sobolev exponent','passed':True,'exponent':str(exponent),'convergence_condition':'s<-K; equality exponent=-1 diverges','fixed_order':'M>K','comparison':'BG44-BG45; full positive and negative real-weight comparison supplied in solution.'})
record={'schema':'an04-prescribed-broken-rays-model-checks/v1','source_sha256':sha(c/'prescribed-broken-rays-preparation.md'),'checks':checks,'passed':True,'general_theorem_certified':False,'script_sha256':sha(Path(__file__))}
(c/'model-check.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print({'passed':True,'finite_model_groups':len(checks),'general_theorem_certified':False})
