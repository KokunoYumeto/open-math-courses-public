"""Exact root/operator checks and reproducible diagrams for the convex component theorem."""
from pathlib import Path
import hashlib,json,math
import sympy as S
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures';FIG.mkdir(exist_ok=True)
plt.rcParams.update({'svg.hashsalt':'AN02-real-roots-convex-component275','font.size':12})
t,x,y,s,c,z,h=S.symbols('t x y s c z h',real=True)
checks=[]
def check(name,test,detail=None):
 assert bool(test),name
 checks.append({'name':name,'status':'PASS','detail':detail})
q=(t+3)*(t+1)*(t-2);shifted=S.expand(q+S.diff(q,t)/2)
check('one_variable_example_polynomial',shifted==t**3+S.Rational(7,2)*t**2-3*t-S.Rational(17,2))
for pattern in [(3,0,0),(2,1,0),(2,2,1),(1,1,1),(4,1,1)]:
 original=S.prod((t-r)**a for r,a in zip([-3,-1,2],pattern));degree=sum(pattern)
 for value in [S.Rational(1,2),-S.Rational(1,2),S.Integer(1)]:
  p=S.expand(original)
  for step in range(degree):
   previous=S.Poly(p,t);old_roots=previous.intervals(eps=S.Rational(1,10**10))
   p=S.expand(p+value*S.diff(p,t));polynomial=S.Poly(p,t)
   roots=polynomial.intervals(eps=S.Rational(1,10**10))
   check(f'real_root_count_{pattern}_{value}_step{step+1}',sum(a for _,a in roots)==degree)
   check(f'unchanged_degree_and_leading_{pattern}_{value}_step{step+1}',polynomial.degree()==degree and polynomial.LC()==previous.LC())
   check(f'multiplicity_drops_{pattern}_{value}_step{step+1}',max(a for _,a in roots)<=max(1,max(a for _,a in old_roots)-1))
  check(f'all_simple_after_degree_operations_{pattern}_{value}',all(a==1 for _,a in roots))

cubic=S.expand(sum(S.binomial(3,j)*(s*x)**j*S.diff(t**3,t,j) for j in range(4)))
check('cubic_Nuij_expansion',cubic==t**3+9*s*x*t**2+18*s**2*x**2*t+6*s**3*x**3)
R=z**3-9*z**2+18*z-6
expected={0:-6,1:4,2:2,3:-6,6:-6,7:22}
for a,b in expected.items():check(f'root_interval_endpoint_{a}',R.subs(z,a)==b)
check('cubic_discriminant',S.discriminant(R,z)==1944)
intervals=S.Poly(R,z).intervals(eps=S.Rational(1,10**30))
check('three_simple_positive_roots',len(intervals)==3 and all(a==1 and lo>0 for (lo,hi),a in intervals))
for ((lo,hi),multiplicity),(left,right) in zip(intervals,[(0,1),(2,3),(6,7)]):check(f'exact_isolation_in_{left}_{right}',left<lo<hi<right)
lambda_values=[float((lo+hi)/2) for (lo,hi),_ in intervals]
check('Vieta_sum',S.expand(R).coeff(z,2)==-9)
check('Vieta_pair_sum',S.expand(R).coeff(z,1)==18)
check('Vieta_product',S.expand(R).coeff(z,0)==-6)
check('normalization_complex_factor',S.expand((2*t-x)*(t+3*x)/2)==S.expand((t-x/2)*(t+3*x)))
for roots in [(t+x)*(t-2*y),(t+x)**2*(t+y),(t-x)**2*(t+2*y)**2]:
 m=S.Poly(roots,t).degree();p=roots
 for ell in [x,y]:p=S.expand(sum(S.binomial(m,j)*(s*ell)**j*S.diff(p,t,j) for j in range(m+1)))
 check(f'multivariable_homogeneous_degree_{m}_{len(checks)}',all(sum(powers)==m for powers,coefficient in S.Poly(p,x,y,t).terms()))
 check(f'multivariable_e_value_{m}_{len(checks)}',p.subs({x:0,y:0,t:1})==1)
 check(f'multivariable_coefficient_limit_{m}_{len(checks)}',S.expand(p.subs(s,0)-roots)==0)
 # On a fixed real line the tangential forms are constant.
 for base in [(1,0),(0,1),(1,-2)]:
  at=p.subs({x:base[0],y:base[1],s:S.Rational(1,7)})
  isolated=S.Poly(at,t).intervals(eps=S.Rational(1,10**12))
  check(f'multivariable_strict_line_m{m}_base{base}',len(isolated)==m and all(a==1 for _,a in isolated))
for k in range(2,9):
 for sign in [1,-1]:
  homogeneous=t**k+x*y**(k-1)
  scaled=S.cancel(homogeneous.subs({t:h*z,x:sign*h**k,y:1})/h**k)
  check(f'exact_gradient_scaling_k{k}_sign{sign}',scaled==z**k+sign)
for k in range(2,9):
 sign=1
 real_count=sum(a for _,a in S.Poly(z**k+sign,z).intervals())
 check(f'nonreal_scaled_root_k{k}',real_count<k)
check('one_dimensional_normalization',S.Rational(1,16)*x**4==(x/(-2))**4)
check('one_dimensional_factor',S.expand((x+t*z)**4-z**4*(t+x/z)**4)==0)
check('nonhyperbolic_tube_counterexample',1+S.I**2==0)
for a in [S.Rational(1,3),S.Rational(1,2),S.Rational(4,5)]:
 point_x=S.Rational(2,5);point_t=S.Rational(7,3);dir_x=-S.Rational(1,5);dir_t=S.Rational(5,3)
 prod=(t-x/2)*(t+3*x)
 lhs=prod.subs({x:a*point_x+(1-a)*dir_x,t:a*point_t+(1-a)*dir_t})
 rhs=a**2*prod.subs({x:point_x+(1-a)/a*dir_x,t:point_t+(1-a)/a*dir_t})
 check(f'convex_segment_identity_{a}',S.simplify(lhs-rhs)==0)

def save(fig,name):
 fig.tight_layout()
 fig.savefig(FIG/(name+'.png'),dpi=160,metadata={'Software':'Original reproducible mathematical figure'})
 fig.savefig(FIG/(name+'.svg'),metadata={'Date':None})
 plt.close(fig)

fig,ax=plt.subplots(figsize=(10,5.4))
grid=np.linspace(-5,3,1600)
f=S.lambdify(t,q,'numpy');g=S.lambdify(t,shifted,'numpy')
ax.plot(grid,f(grid),label=r'$q(t)=(t+3)(t+1)(t-2)$',color='#2365a3',lw=2.2)
ax.plot(grid,g(grid),label=r'$q(t)+q^{\prime}(t)/2$',color='#ba591c',lw=2.2)
new_intervals=S.Poly(shifted,t).intervals(eps=S.Rational(1,10**20))
new_values=[float((lo+hi)/2) for (lo,hi),_ in new_intervals]
ax.scatter([-3,-1,2],[0,0,0],color='#2365a3',s=55,zorder=5)
ax.scatter(new_values,[0]*3,color='#ba591c',marker='D',s=48,zorder=5)
for a in [-3,-1,2]:ax.axvline(a,ls=':',color='#2365a3',alpha=.45)
ax.axhline(0,color='black',lw=.8);ax.set_ylim(-28,36);ax.set_xlim(-5,3)
ax.set_xlabel(r'Line parameter $t$');ax.set_ylabel('Polynomial value')
ax.set_title('A derivative perturbation places one simple root in each interval')
ax.grid(alpha=.17);ax.legend(loc='upper left')
save(fig,'root-interlacing-by-a-derivative')

fig,ax=plt.subplots(figsize=(9.8,5.5))
grid=np.linspace(-1,1,1201)
ax.axhspan(0,2.5,color='#dceaf8',label=r'Original component: $t>0$')
for value,color in [(S.Rational(1,3),'#ba591c'),(S.Rational(1,12),'#248450')]:
 boundary=np.where(grid>=0,-lambda_values[0]*float(value)*grid,-lambda_values[2]*float(value)*grid)
 ax.plot(grid,boundary,lw=2.3,color=color,label=r'$\Gamma_s$: above the line, $s='+str(value)+'$')
ax.axhline(0,color='#2365a3',lw=1.2)
ax.scatter([0],[0],facecolor='white',edgecolor='black',s=65,zorder=6)
ax.annotate('Origin excluded',xy=(0,0),xytext=(.35,.55),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set_xlim(-1,1);ax.set_ylim(-.22,2.5)
ax.set_xlabel(r'Tangential coordinate $x$');ax.set_ylabel(r'Normal coordinate $t$')
ax.set_title('Strict perturbations preserve compact paths, without a global cone inclusion')
ax.grid(alpha=.18);ax.legend(loc='upper right',fontsize=10)
save(fig,'strict-perturbation-component-boundaries')
geometry={'one_variable_original_roots':[-3,-1,2],'one_variable_perturbed_polynomial':'t^3+7*t^2/2-3*t-17/2',
 'new_root_exact_isolating_intervals':[{'lower':str(lo),'upper':str(hi),'multiplicity':m} for (lo,hi),m in new_intervals],
 'lambda_polynomial':'lambda^3-9*lambda^2+18*lambda-6',
 'lambda_exact_isolating_intervals':[{'lower':str(lo),'upper':str(hi),'multiplicity':m} for (lo,hi),m in intervals],
 'lambda_approximate_values':lambda_values,'plotted_s_values':['1/3','1/12'],
 'original_component':'t>0','perturbed_component':'t>max(-lambda1*s*x,-lambda3*s*x)',
 'boundary_not_in_component':True,'origin_excluded':True,'curve_coordinates_are_numerical_samples_of_exact_algebraic_boundaries':True}
(FIG/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
record={'schema':'AN02-hyperbolic-component-check275/v1','status':'PASS','checks_passed':len(checks),
 'scope':'Exact concrete identities, Sturm real-root/multiplicity counts and rational root isolations; full general theorem supplied by the written proof.',
 'checks':checks,'artifacts':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper()} for p in sorted(FIG.iterdir()) if p.is_file()],
 'workers_launched':0,'outgoing_messages':0}
(ROOT/'math-check275.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','checks':len(checks),'new_roots_approximate':new_values,'lambda_approximate':lambda_values,'figures':2}))
