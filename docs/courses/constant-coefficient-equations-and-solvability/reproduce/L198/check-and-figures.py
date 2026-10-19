"""Exact polynomial examples and the finite-part illustration.

GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original code: CC0 1.0.
The examples supplement the complete general argument in the accompanying text.
"""
from pathlib import Path
import itertools,json,math
import numpy as np
import sympy as S
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures';FIG.mkdir(exist_ok=True)
checks=[]
def check(name,result):
 if not bool(result):raise AssertionError(name)
 checks.append(name)
def multi(n,k):
 return [a for a in itertools.product(range(k+1),repeat=n) if sum(a)<=k]
def monomial(xs,a):
 return S.prod(x**j for x,j in zip(xs,a))
def derivative(p,xs,a):
 for x,j in zip(xs,a):p=S.diff(p,x,j)
 return S.expand(p)
for n,ks in [(1,range(5)),(2,range(3))]:
 xs=S.symbols('x:'+str(n))
 for k in ks:
  inputs=multi(n,k);outputs=multi(n,2*k);ops=[(a,b) for a in multi(n,k) for b in multi(n,k) if sum(a)+sum(b)<=k]
  cols=[]
  for a,b in ops:
   col=[]
   for g in inputs:
    q=S.Poly(monomial(xs,a)*derivative(monomial(xs,g),xs,b),*xs)
    col.extend(q.coeff_monomial(z) for z in outputs)
   cols.append(S.Matrix(col))
  rank=S.Matrix.hstack(*cols).rank()
  check(f'faithful truncated Weyl action,n={n},k={k}',rank==len(ops)==math.comb(k+2*n,2*n))
x=S.symbols('x',positive=True);s=S.symbols('s')
for d in [1,2,4,5]:
 lhs=S.diff(x**(d*(s+1)),x,d)
 rhs=S.prod(d*s+j for j in range(1,d+1))*x**(d*s)
 check('power functional equation,d='+str(d),S.simplify(lhs-rhs)==0)
F=x*x+1;a=(s+2)*x**3/(s*s+1)+1/F
for j in [0,1,2]:
 shifted=a.subs(s,s-j)
 lhs=S.diff(shifted*F**(-j),x)+s*shifted*F**(-j)*S.diff(F,x)/F
 rhs=(S.diff(a,x)+s*a*S.diff(F,x)/F).subs(s,s-j)*F**(-j)
 check('semilinear parameter shift,j='+str(j),S.cancel(lhs-rhs)==0)
x,y=S.symbols('x y')
F=x*x*y*y+x+y+1;degree=S.Poly(F,x,y).total_degree()
for beta in [(1,0),(0,1),(2,0),(1,1),(0,2),(3,1)]:
 r=S.Integer(1);q=0
 for var,num in zip([x,y],beta):
  for _ in range(num):
   r=S.expand(F*S.diff(r,var)+(s-q)*r*S.diff(F,var));q+=1
 check('formal derivative numerator bound,beta='+str(beta),S.Poly(r,x,y).total_degree()<=q*(degree-1))
for k in [1,2,5,9]:
 count=sum(not(i>=2 or(i>=1 and j>=1)) for i,j in multi(2,k))
 check('standard monomials of (x^2,xy),k='+str(k),count==k+2)
z=S.symbols('z')
Q=z*z*S.Symbol('p')+3*z*S.Symbol('p')**2+5
comm=S.diff(-S.diff(Q,S.Symbol('p')),z,2)
check('triple commutator scalar',comm==-2)
xi=S.symbols('xi',real=True)
quot=(S.exp(-xi*xi)-1)/(xi*xi)
check('finite-part quotient at zero',S.limit(quot,xi,0)==-1)
check('finite-part Gaussian integration by parts',S.integrate(-2*S.exp(-xi*xi),(xi,-S.oo,S.oo))==-2*S.sqrt(S.pi))
epsilon=S.symbols('epsilon',positive=True)
check('two-dimensional residue normalization',S.limit((s+1)*2*S.pi/(2*s+2),s,-1)==S.pi)
check('quadratic reciprocal multiplier kills delta-prime',S.diff(xi*xi,xi).subs(xi,0)==0)
check('quadratic reciprocal multiplier detects delta-double-prime',S.diff(xi*xi,xi,2).subs(xi,0)==2)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'path'})
t=np.linspace(-3,3,1201);phi=np.exp(-t*t)
ratio=np.full_like(t,-1.0);np.divide(np.expm1(-t*t),t*t,out=ratio,where=t!=0)
fig,axes=plt.subplots(1,3,figsize=(12.3,3.5),constrained_layout=True)
data=[(phi,r'$\phi(\xi)=e^{-\xi^2}$','#1e5a9a'),
      (phi-1,r'$\phi(\xi)-1$','#b35a1d'),
      (ratio,r'$(\phi(\xi)-1)/\xi^2$','#6847a6')]
for ax,(values,title,color) in zip(axes,data):
 ax.plot(t,values,color=color,lw=2.2);ax.axvline(0,color='#777777',lw=.7,ls='--');ax.axhline(0,color='#aaaaaa',lw=.6)
 ax.set(xlim=(-3,3),xlabel=r'frequency $\xi$',title=title);ax.grid(alpha=.18)
axes[0].plot([0],[1],'o',color=data[0][2]);axes[1].plot([0],[0],'o',color=data[1][2])
axes[2].plot([0],[-1],'o',color=data[2][2]);axes[2].annotate(r'value at $0$: $-1$',(0,-1),xytext=(.35,-.84),arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=10)
fig.savefig(FIG/'finite-part-test-subtraction.png',dpi=170)
fig.savefig(FIG/'finite-part-test-subtraction.svg')
plt.close(fig)
(FIG/'figure-data.json').write_text(json.dumps({'test':'exp(-xi^2)','frequency_interval':[-3,3],'samples':1201,'subtracted_value_at_zero':0,'quotient_continuous_value_at_zero':-1,'finite_part_pairing':'-2*sqrt(pi)','meaning':'The plotted functions illustrate Taylor subtraction in the exact finite-part formula;the plot is not a representation of a distribution.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'checks':checks,'scope':'Finite exact examples supplement the complete general proof;they do not establish the general theorem by themselves.'}))
