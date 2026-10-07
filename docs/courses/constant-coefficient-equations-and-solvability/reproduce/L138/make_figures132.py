"""Reproduce two exact-formula Carleman-necessity diagrams."""
from pathlib import Path
from fractions import Fraction
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OWN=Path(__file__).resolve().parent
FIG=OWN/'figures';FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11.5,
                     'axes.titlesize':13,'axes.labelsize':11.5,
                     'legend.fontsize':10,'svg.fonttype':'none',
                     'svg.hashsalt':'AN02-L138-original132','text.usetex':False})
BLUE='#176d9c';ORANGE='#c55c18';GREEN='#278254';GREY='#444b52'
credit='GPT-6.1 Sol (OpenAI), Ultra, October 2026; original diagrams CC0-1.0.'
def save(fig,name,description):
    fig.savefig(FIG/(name+'.png'),dpi=170,metadata={'Author':credit,'Description':description})
    fig.savefig(FIG/(name+'.svg'),metadata={'Creator':credit,'Description':description,'Date':None})
    plt.close(fig)
def budget(r,alpha):
    m=np.floor(r**(1/alpha)).astype(int)
    return np.array([count*math.log(float(value))-alpha*math.lgamma(count+1)
                     for value,count in zip(r,m)])

r=np.linspace(1,32,500)
t1=budget(r,1);t2=budget(r,2)
indices=np.arange(1,81)
harmonic=[];quadratic=[];h=Fraction(0);q=Fraction(0)
exact_rows=[]
for j in indices:
    integer=int(j);h+=Fraction(1,integer);q+=Fraction(1,integer*integer)
    harmonic.append(float(h));quadratic.append(float(q))
    if integer in [1,2,4,8,16,32,64,80]:
        exact_rows.append({'N':integer,'sum_1_over_j_exact':str(h),
                           'sum_1_over_j_squared_exact':str(q)})
fig,axes=plt.subplots(1,3,figsize=(15.6,5.1),layout='constrained')
axes[0].plot(r,t1,color=ORANGE,label=r'$M_j=j$')
axes[0].plot(r,t2,color=BLUE,label=r'$M_j=j^2$')
axes[0].set(title='Thresholds accumulate logarithmic loss',xlabel=r'frequency $r$',ylabel=r'$T(r)$')
axes[0].legend(loc='upper left');axes[0].grid(alpha=.22)
axes[0].text(.98,.04,'All active thresholds included\nCN6.2 and CN9.1',
             transform=axes[0].transAxes,ha='right',va='bottom',fontsize=9.5)
axes[1].semilogy(r,np.exp(-t1),color=ORANGE,label=r'$M_j=j$')
axes[1].semilogy(r,np.exp(-t2),color=BLUE,label=r'$M_j=j^2$')
axes[1].set(title='Normalized algebraic envelopes',xlabel=r'frequency $r$',ylabel=r'$e^{-T(r)}$  ($C=1$)')
axes[1].legend(loc='lower left');axes[1].grid(alpha=.22)
axes[1].text(.98,.96,'Bounds, not asserted transforms\nCN6.3',
             transform=axes[1].transAxes,ha='right',va='top',fontsize=9.5)
axes[2].plot(indices,harmonic,color=ORANGE,label=r'$\sum_{j=1}^N 1/j$')
axes[2].plot(indices,quadratic,color=BLUE,label=r'$\sum_{j=1}^N 1/j^2$')
axes[2].axhline(2,color=GREY,linestyle='--',linewidth=1.3,label='proved upper bound 2')
axes[2].set(title='Exact finite reciprocal budgets',xlabel=r'number of thresholds $N$',ylabel=r'$\int_1^\infty T_N(r)\,dr/r^2$',ylim=(.8,6.8))
axes[2].legend(loc='upper left');axes[2].grid(alpha=.22)
axes[2].text(.98,.04,'Finite sums shown; the proof\nhandles the infinite limit (CN7.3)',
             transform=axes[2].transAxes,ha='right',va='bottom',fontsize=9.5)
fig.suptitle('One derivative threshold contributes exactly its reciprocal',fontsize=16)
save(fig,'frequency-budget','Exact T(r), algebraic envelopes and finite reciprocal-budget identities; CN6.2, CN6.3, CN7.3, CN9.1.')

y_levels=[Fraction(1,2),Fraction(1,4),Fraction(1,16)]
x=np.linspace(-1,1,801)
ys=np.geomspace(1e-4,1,240)
trace_error=2*np.log1p(ys*ys)+4*ys*np.arctan(1/ys)
trace_bound=2*np.pi*ys
bump_x=np.linspace(-1.35,1.35,801)
bump=np.zeros_like(bump_x);inside=np.abs(bump_x)<1
bump[inside]=np.exp(-2/(1-bump_x[inside]**2))
fig,axes=plt.subplots(1,3,figsize=(15.6,5.1),layout='constrained')
colors=[BLUE,GREEN,ORANGE]
for y,color in zip(y_levels,colors):
    axes[0].plot(x,np.log(x*x+float(y)**2),color=color,label=r'$y='+str(y)+r'$')
negative=np.linspace(-1,-.003,350);positive=-negative[::-1]
axes[0].plot(negative,2*np.log(-negative),color=GREY,linestyle='--',label=r'trace $2\log|x|$')
axes[0].plot(positive,2*np.log(positive),color=GREY,linestyle='--')
axes[0].set(title=r'Local zero factor: $F(z)=z^2$',xlabel=r'$x$',ylabel=r'$\log|F(x+iy)|$',ylim=(-9,1))
axes[0].legend(loc='lower left',fontsize=9.5);axes[0].grid(alpha=.22)
axes[0].annotate(r'trace is $-\infty$ at zero',xy=(0,-8.8),xytext=(.22,-7.2),
                 arrowprops={'arrowstyle':'->','color':GREY},fontsize=9)
axes[1].loglog(ys,trace_error,color=BLUE,label='exact interval error')
axes[1].loglog(ys,trace_bound,color=ORANGE,linestyle='--',label=r'proved bound $2\pi y$')
axes[1].set(title=r'Integral trace error on $[-1,1]$',xlabel=r'height $y$',ylabel=r'$L^1$ error')
axes[1].legend(loc='upper left');axes[1].grid(alpha=.22,which='both')
axes[1].text(.98,.04,r'$2\log(1+y^2)+4y\arctan(1/y)$'+'\nCN4.3; local model only',
             transform=axes[1].transAxes,ha='right',va='bottom',fontsize=9.5)
axes[2].plot(bump_x,bump,color=GREEN,linewidth=2)
axes[2].fill_between(bump_x,0,bump,color=GREEN,alpha=.12)
for endpoint in [-1,1]:axes[2].axvline(endpoint,color=GREY,linestyle=':',linewidth=1)
axes[2].scatter([0],[math.exp(-2)],color=GREEN,s=28,zorder=4)
axes[2].annotate(r'$u(0)=e^{-2}>0$',xy=(0,math.exp(-2)),xytext=(.28,.119),
                 arrowprops={'arrowstyle':'->','color':GREY},fontsize=10)
axes[2].set(title='An actual compact smooth bump',xlabel=r'$x$',ylabel=r'$u(x)$',ylim=(-.005,.155))
axes[2].grid(alpha=.22)
axes[2].text(.02,.94,r'$\|u^{(k)}\|_\infty\leq18^k(k!)^2$'+'\n'+r'$M_j=18j^2$; CN9.3–CN9.6',
             transform=axes[2].transAxes,ha='left',va='top',fontsize=9.5,
             bbox={'facecolor':'white','edgecolor':'none','alpha':.95,'pad':2})
fig.suptitle('A logarithmic zero has an integrable trace; a compact bump needs faster derivatives',fontsize=15)
save(fig,'trace-and-bump','Local multiplicity-two zero trace, exact interval logarithmic error and an actual compact bump with proved 18^k(k!)^2 bounds; CN4.3 and CN9.3–CN9.6.')

geometry={'schema':'AN02-L138-original-figure-geometry132/v1','credit':credit,
    'frequency_budget':{
        'models':{'linear':'M_j=j','quadratic':'M_j=j^2'},
        'frequency_interval':[1,32],'frequency_samples':500,
        'T_formula':'m*log(r)-alpha*log(m!), m=floor(r^(1/alpha))',
        'envelope':'exp(-T(r)); normalized C=1; algebraic bounds only',
        'finite_budget_identity':'integral_1^infinity T_N(r)/r^2 dr=sum_{j<=N}1/M_j',
        'plotted_budget_indices':[1,80],'selected_exact_finite_budgets':exact_rows,
        'quadratic_sum_proved_bound':2,'proof_locators':['CN6.2','CN6.3','CN7.3','CN9.1']},
    'trace_and_bump':{
        'local_zero_model':'F(z)=z^2; local factor only, not the global half-plane class',
        'multiplicity':2,'trace_interval':[-1,1],
        'plotted_heights_exact':[str(y) for y in y_levels],
        'interval_error':'2*log(1+y^2)+4*y*atan(1/y)',
        'whole_line_bound':'2*pi*y',
        'bump':'exp(-2/(1-x^2)) for |x|<1, else0',
        'support_exact':[-1,1],'value_at_zero':'exp(-2)',
        'derivative_bound':'18^k*(k!)^2, k>=1',
        'thresholds':'M_j=18*j^2','reciprocal_sum_proved_bound':'1/9',
        'proof_locators':['CN4.2','CN4.3','CN9.3','CN9.4','CN9.5','CN9.6']}}
(FIG/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Wrote two PNG/SVG pairs and exact figure geometry.')
