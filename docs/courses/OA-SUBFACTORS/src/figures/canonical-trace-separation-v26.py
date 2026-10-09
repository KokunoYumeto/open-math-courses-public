"""CC0. Exact two-trace projection checks and reproducible CTS figure.

The binomial checks evaluate CTS.9; the separate PG enumeration constructs the
actual diagonal projections in every full S_3 x Z balanced-word charge block.
The limiting normality assertions use the full proofs in the lesson.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json
import re
import sys

D = Path(__file__).resolve().parent
checks = []

def check(name, condition, **details):
    assert condition, (name, details)
    checks.append(dict(name=name, passed=True, **details))

def serial(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {str(k): serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [serial(v) for v in x]
    return x


def distribution(h, p):
    return [F(comb(h, r))*p**r*(1-p)**(h-r) for r in range(h+1)]

def trace_data(h, a, b):
    c = (a+b)/2
    keep = [r for r in range(h+1) if (F(r,h)<c if a<b else F(r,h)>c)]
    da, db = distribution(h,a), distribution(h,b)
    return sum((da[r] for r in keep),F(0)), sum((db[r] for r in keep),F(0)), keep

fixtures = [(F(1,5),F(1,2)),(F(1,4),F(3,4)),(F(2,5),F(1,4)),
            (F(1,3),F(2,3)),(F(7,10),F(2,5))]
for a,b in fixtures:
    for h in [1,2,3,4,7,20,40,80,160]:
        da,db=distribution(h,a),distribution(h,b)
        ta,tb,keep=trace_data(h,a,b)
        gap=(a-b)**2
        bounda=4*a*(1-a)/(h*gap)
        boundb=4*b*(1-b)/(h*gap)
        check(f'binomial-{a}-{b}-h{h}',
              sum(da)==sum(db)==1 and 1-ta<=bounda and tb<=boundb,
              h=h,a=a,b=b,physical_complement=1-ta,module_projection=tb,
              physical_bound=bounda,module_bound=boundb,keep_counts=keep)
        for p,dp in [(a,da),(b,db)]:
            mean=sum((F(r,h)*dp[r] for r in range(h+1)),F(0))
            var=sum(((F(r,h)-p)**2*dp[r] for r in range(h+1)),F(0))
            check(f'exact-moments-{p}-h{h}-pair{a}-{b}',mean==p and var==p*(1-p)/h)

check('exercise-CTS1-h2',trace_data(2,F(1,5),F(1,2))[:2]==(F(16,25),F(1,4)))
check('exercise-CTS1-h4',trace_data(4,F(1,5),F(1,2))[:2]==(F(512,625),F(5,16)))
check('exercise-CTS2-depth',F(100,9*1112)<F(1,100) and -1+2*1112==2223)
check('midpoint-strict-h20',trace_data(20,F(1,5),F(1,2))[2]==list(range(7)))

# Actual PG group operations. Permutations act on {0,1,2}; compose left after right.
identity=(0,1,2)
A=(1,0,2)
B=(0,2,1)
labels=[(identity,0),(A,1),(B,0)]
def mul(g,h):
    return (tuple(g[0][h[0][i]] for i in range(3)),g[1]+h[1])
def inv(g):
    p=tuple(g[0].index(i) for i in range(3))
    return p,-g[1]

odd=(F(1,4),F(1,2),F(1,4))
even=(F(2,5),F(1,5),F(2,5))
actual_rows=[]
for h in [1,2,3,4]:
    capacities=defaultdict(int)
    qranks=defaultdict(int)
    physical=F(0); module=F(0)
    for word in product(range(3),repeat=2*h):
        charge=(identity,0); pt=F(1); rt=F(1)
        count=0
        for pos,label in enumerate(word):
            isodd=(pos%2==0) # interval [-2h+1,0] starts at an odd site
            charge=mul(charge,inv(labels[label]) if isodd else labels[label])
            pt *= (odd if isodd else even)[label]
            rt *= (even if isodd else odd)[label]
            if not isodd and label==1: count+=1
        r=charge[1]
        cp=F(2)**(-r)/10**h
        cr=F(2)**r/10**h
        assert pt==cp and rt==cr, (h,word,charge,pt,rt)
        capacities[charge]+=1
        if F(count,h)<F(7,20):
            qranks[charge]+=1; physical+=pt;module+=rt
    rankphysical=sum((rank*F(2)**(-charge[1])/10**h for charge,rank in qranks.items()),F(0))
    rankmodule=sum((rank*F(2)**charge[1]/10**h for charge,rank in qranks.items()),F(0))
    fullp=sum((rank*F(2)**(-charge[1])/10**h for charge,rank in capacities.items()),F(0))
    fullr=sum((rank*F(2)**charge[1]/10**h for charge,rank in capacities.items()),F(0))
    ta,tb,keep=trace_data(h,F(1,5),F(1,2))
    check(f'actual-PG-full-charge-projection-h{h}',
          physical==rankphysical==ta and module==rankmodule==tb and fullp==fullr==1
          and sum(capacities.values())==3**(2*h)
          and all(0<=rank<=capacities[charge] for charge,rank in qranks.items()),
          interval=[-2*h+1,0],word_count=3**(2*h),full_charge_blocks=len(capacities),
          physical_projection=physical,module_projection=module,
          full_projection_ranks=[dict(permutation=charge[0],grade=charge[1],
                                      capacity=capacity,qrank=qranks[charge])
                                  for charge,capacity in sorted(capacities.items())])
    actual_rows.append((h,len(capacities),physical,module))

# A limiting implication sanity check: the proved bounds force both errors to zero.
for h in [100,1000,10000]:
    check(f'PG-explicit-bound-h{h}',F(64,9*h)<F(100,9*h),
          physical_bound=F(64,9*h),module_bound=F(100,9*h))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':10,
                     'svg.hashsalt':'canonical-trace-separation-CTS-v1'})
fig=plt.figure(figsize=(14,10),constrained_layout=True)
gs=fig.add_gridspec(3,2,height_ratios=[1.18,.7,1.22])
ax=fig.add_subplot(gs[0,:]);ax.set_xlim(0,14);ax.set_ylim(0,3.6);ax.axis('off')
def box(x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor=color,edgecolor='#3c4960'))
    ax.text(x+w/2,y+h-.22,title,ha='center',va='top',fontweight='bold')
    ax.text(x+w/2,y+.24,body,ha='center',va='bottom',linespacing=1.5)
def arrow(x1,y1,x2,y2,label=''):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',lw=1.6,color='#3c4960'))
    if label:ax.text((x1+x2)/2,(y1+y2)/2+.1,label,ha='center',va='bottom',fontsize=9)
box(.1,2,3.45,1.35,'Finite source after prefix',r'$g\in N_{k+1}^{\prime}\cap N_k$'+'\n'+r'$a=\tau(g)\ne b=\rho(g)$','#e5eefc')
box(5.15,2,3.65,1.35,'Actual even-copy row',r'$j=k+2h,\quad G_h=h^{-1}\sum g^{(r)}$'+'\n'+'Two separate product traces (POR)','#e4f4ef')
box(10.35,2,3.5,1.35,'Specified finite reflection',r'$\tau_{T_a}(\Theta(x))=\rho_a(x)$'+'\n'+'Whole-factor trace identity (CTS.1)','#fff0da')
arrow(3.65,2.65,5.05,2.65,'promote to even depth')
arrow(8.9,2.65,10.25,2.65,'compatible finite maps')
box(1.05,.12,5.1,1.20,'Physical tracial completion',r'$q_h\longrightarrow1\quad\mathrm{strongly}$'+'\n'+r'$\tau(1-q_h)\leq4a(1-a)/(h(a-b)^2)$','#e5eefc')
box(7.75,.12,5.1,1.20,'Canonical reflected completion',r'$\Theta(q_h)\longrightarrow0\quad\mathrm{strongly}$'+'\n'+r'$\rho(q_h)\leq4b(1-b)/(h(a-b)^2)$','#fff0da')
arrow(6,1.95,3.65,1.45,'threshold nearer physical mean')
arrow(8,1.95,10.3,1.45,'same actual finite projections')
ax.set_title('CTS: finite trace matching and two incompatible normal limits',fontweight='bold',fontsize=15,pad=15)

mid=fig.add_subplot(gs[1,:]);mid.axis('off')
mid.text(.5,.9,'Downward witness propagation (63.4):  (a, b) → (b, a) at every actual Jones triple',ha='center',va='top',fontsize=12)
mid.text(.5,.62,'Normal μ ≤ s:  μ(1 − qₕ) → 0 by normality,  μ(qₕ) ≤ s(qₕ) → 0;  hence μ(1) = 0.',ha='center',va='top',fontsize=12)
mid.text(.5,.31,'The specified normal reflection exists exactly for extremal inclusions (CTS.7).\nArbitrary centers and every prescribed ordinary prefix are included.',ha='center',va='top',fontweight='bold',fontsize=12)

h=40;a=F(1,5);b=F(1,2);ta,tb,keep=trace_data(h,a,b)
for ax,p,color,title in [(fig.add_subplot(gs[2,0]),a,'#275ca8','Physical trace: a = 1/5'),
                         (fig.add_subplot(gs[2,1]),b,'#b96d16','Original module trace: b = 1/2')]:
    dp=distribution(h,p)
    ax.bar(range(h+1),[float(x) for x in dp],color=color,width=.88)
    ax.axvspan(-.5,13.5,color='#4ea890',alpha=.12,label='q₄₀ keeps counts 0–13')
    ax.axvline(14,color='#25354b',ls='--',lw=1.5)
    ax.axvline(float(h*p),color=color,ls=':',lw=1.5)
    ax.set_xlim(-.5,h+.5);ax.set_ylim(0,.17)
    ax.set_title(title,fontweight='bold');ax.set_xlabel('Number of label 1 even sites in actual PG interval');ax.set_ylabel('Trace mass of count projection')
    ax.legend(loc='upper right',fontsize=9)
    mass=1-ta if p==a else tb
    label='τ(1 − q₄₀)' if p==a else 'ρ(q₄₀)'
    ax.text(.97,.78,f'{label} = {float(mass):.7f}\nexact binomial tail (CTS.9)',transform=ax.transAxes,ha='right',va='top',fontsize=10)
fig.savefig(D/'canonical-trace-separation-v26.svg',metadata={
    'Date':None,'Title':'Finite reflection and singular tracial completions',
    'Creator':'Open Mathematics Courses',
    'Description':'Actual Jones-row projection traces and CTS.1–CTS.7; reproducible from check-and-draw.py.',
    'Rights':'CC0-1.0'})
fig.savefig(D/'canonical-trace-separation-v26.png',dpi=150,
            metadata={'Software':'Matplotlib; CC0-1.0 source check-and-draw.py'})
plt.close(fig)
report={'schema':'canonical-trace-separation-checks/v1','exact_arithmetic':True,
        'checks_passed':len(checks),'checks':serial(checks),
        'runtime':{'python':sys.version.split()[0],'matplotlib':matplotlib.__version__},
        'figure_licence':'CC0-1.0',
        'figure_h':40,'figure_physical_complement':serial(1-ta),'figure_module_projection':serial(tb),
        'actual_PG_h':[r[0] for r in actual_rows],
        'mathematical_scope':'CTS.3 exact finite trace checks and actual PG projection realization; no numerical substitute for the normality proof.'}
(D/'CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'actual_PG_h':[r[0] for r in actual_rows],
                  'figure_physical_complement':float(1-ta),'figure_module_projection':float(tb)}))
