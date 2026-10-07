"""Reproduce the exact carrier geometry and qualified series/bound plots."""
from pathlib import Path
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
 'svg.hashsalt':'AN02-analytic-functional-151','axes.spines.top':False,
 'axes.spines.right':False})

def positive_series(x,tol=2e-15):
    if x==0:return 1.0
    term=total=1.0
    for m in range(1,10000):
        term*=x/(m*m);total+=term
        q=x/((m+2)**2);next_term=term*x/((m+1)**2)
        if q<1 and next_term/(1-q)<=tol*total:return total
    raise ArithmeticError('Positive series did not meet the tail criterion')

def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=170,facecolor='white')
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Open Mathematics Courses'},facecolor='white')
    plt.close(fig)

fig,(left,right)=plt.subplots(1,2,figsize=(12,6.2))
fig.subplots_adjust(left=.07,right=.97,top=.80,bottom=.31,wspace=.30)
fig.suptitle('A complex neighborhood supplies a distribution representative',y=.96,fontsize=17)
fig.text(.5,.885,r'$n=1,\quad K=[-1,1]\subset\mathbb{R},\quad\varepsilon=1/2$',ha='center',fontsize=13)
t1=np.linspace(-np.pi/2,np.pi/2,250)
t2=np.linspace(np.pi/2,3*np.pi/2,250)
boundary_x=np.concatenate([1+.5*np.cos(t1),-1+.5*np.cos(t2)])
boundary_y=np.concatenate([.5*np.sin(t1),.5*np.sin(t2)])
left.fill(boundary_x,boundary_y,color='#d9e8f4',zorder=1)
left.plot(np.r_[boundary_x,boundary_x[0]],np.r_[boundary_y,boundary_y[0]],color='#25618b',lw=2,zorder=2)
left.plot([-1,1],[0,0],color='#19232b',lw=4,zorder=4,label=r'real carrier $K$')
left.scatter([-1,1],[0,0],s=25,color='#19232b',zorder=5)
left.axhline(0,color='#687781',lw=.7,zorder=0);left.axvline(0,color='#687781',lw=.7,zorder=0)
left.annotate('',xy=(0,.5),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':'#25618b','lw':1.5})
left.text(.07,.26,r'$\varepsilon=1/2$',color='#25618b',fontsize=10)
left.text(0,-.36,r'$L_{1/2}=K+(1/2)\overline{B}_{\mathbb{R}^2}$',ha='center',fontsize=11)
left.set(xlim=(-1.8,1.8),ylim=(-.9,.9),xlabel=r'$x=\operatorname{Re}z$',ylabel=r'$y=\operatorname{Im}z$')
left.set_aspect('equal',adjustable='box')
left.set_title(r'Closed carrier thickening in $\mathbb{C}\simeq\mathbb{R}^2$',pad=14,fontsize=12)
left.set_xticks([-1.5,-1,0,1,1.5]);left.set_yticks([-.5,0,.5]);left.legend(loc='upper left',fontsize=9,frameon=False)
right.axhline(0,color='#687781',lw=.8);right.axvline(0,color='#687781',lw=.8)
right.plot([0,3],[0,4],color='#2d6d49',lw=1.8)
right.plot([3,3,0],[0,4,4],color='#95ae9f',ls='--',lw=1)
right.scatter([3],[4],s=45,color='#2d6d49',zorder=5)
right.annotate(r'$\zeta=3+4i$',xy=(3,4),xytext=(2.5,4.65),ha='center',fontsize=12,
               arrowprops={'arrowstyle':'-','color':'#2d6d49'})
right.text(1.10,2.05,r'$|\zeta|=5$',color='#2d6d49',rotation=53,fontsize=11)
right.set(xlim=(-.6,5),ylim=(-.6,5.2),xlabel=r'$\xi=\operatorname{Re}\zeta$',ylabel=r'$\eta=\operatorname{Im}\zeta$')
right.set_aspect('equal',adjustable='box');right.set_xticks([0,1,2,3,4]);right.set_yticks([0,1,2,3,4,5])
right.set_title('Parameter plane of the four-real-dimensional graph',pad=14,fontsize=11)
fig.text(.06,.19,r'Actual support: $\operatorname{supp}T_{1/2}\subset L_{1/2}$',fontsize=12)
fig.text(.54,.19,r'$W:\ (\xi,\eta)\mapsto(\xi,\eta,-\eta,\xi)$',fontsize=12)
fig.text(.54,.14,r'Imaginary block $(\eta,\xi)$; graph norm $\sqrt{2}|\zeta|$',fontsize=11)
fig.text(.06,.14,r'$h_{L_{1/2}}(\eta_1,\eta_2)=|\eta_1|+\frac{1}{2}\sqrt{\eta_1^2+\eta_2^2}$',fontsize=11)
fig.text(.54,.095,r'At $(3,4)$: $\Phi=4+\frac{1}{2}\sqrt{4^2+3^2}=13/2$',fontsize=11)
fig.text(.06,.035,'Original proof AF4–AF7. Human source: Hörmander II, Theorem 15.1.5, p. 276.',fontsize=10,color='#384a57')
save(fig,'complex-carrier-and-diagonal')

fig,ax=plt.subplots(figsize=(11.5,6.5))
fig.subplots_adjust(left=.09,right=.96,top=.84,bottom=.24)
x=np.linspace(0,144,650); f=np.array([positive_series(float(v)) for v in x])
ax.plot(x,np.log(f),color='#152b42',lw=2.8,label=r'actual $\log F_0(x)$, positive-series evaluation')
ax.plot(x,2*np.sqrt(x),color='#347858',lw=2,label=r'upper bound $2\sqrt{x}$')
for eps,color in [(.25,'#c57b21'),(.1,'#97528a')]:
    ax.plot(x,eps*x+1/eps,color=color,lw=1.7,ls='--',label=fr'upper bound $\varepsilon x+1/\varepsilon$, $\varepsilon={eps:g}$')
xx=x[x>=16]
ax.plot(xx,8*np.log(xx)-2*math.lgamma(9),color='#567c9c',lw=1.8,ls=':',
        label=r'lower bound from one term: $\log(x^8/(8!)^2)$')
ax.set(xlim=(0,144),ylim=(0,42),xlabel=r'positive real frequency $x$',ylabel='logarithmic magnitude / bound')
ax.grid(alpha=.16);ax.legend(loc='upper left',fontsize=10,framealpha=.95)
fig.suptitle('An infinite-order point functional has subexponential Fourier growth',y=.96,fontsize=16)
fig.text(.5,.89,r'$F_0(\zeta)=\sum_{m\geq0}\zeta^m/(m!)^2,\qquad K=\{0\}$',ha='center',fontsize=13)
fig.text(.09,.145,r'For every $\varepsilon>0$: $|F_0(\zeta)|\leq e^{1/\varepsilon}e^{\varepsilon|\zeta|}$. Constants may diverge as $\varepsilon\downarrow0$.',fontsize=11)
fig.text(.09,.10,r'For any proposed degree $N$, a term with $m>N$ proves $F_0(x)/(1+x)^N\to\infty$.',fontsize=11)
fig.text(.09,.05,'Original proof AF9, including the finite-jet obstruction. Human sources: Hörmander I, Definition 9.1.1, p. 326; II, Theorem 15.1.5, p. 276.',fontsize=9.3,color='#384a57')
save(fig,'infinite-order-point-growth')

geometry={'schema':'AN02-analytic-functional-geometry151/v1','carrier':{'n':1,'K_interval':[-1,1],'epsilon':.5,
 'L_closed_stadium':True,'x_extent':[-1.5,1.5],'y_extent':[-.5,.5],'distribution_real_dimension':2},
 'graph':{'complex_ambient_dimension':2,'complex_codimension':1,'real_parameter_map':['xi','eta','-eta','xi'],
 'imaginary_block':['eta','xi'],'norm_factor':'sqrt(2)','induced_volume_factor':2,'sample_parameter':[3,4],
 'sample_real_graph':[3,4,-4,3],'sample_phi':6.5,'growth_polynomial_exponent':5,
 'right_panel_is_parameter_plane':True,'four_dimensional_spatial_graph_not_claimed':True},
 'growth_plot':{'positive_real_range':[0,144],'series_relative_tail_tolerance':2e-15,
 'upper_bound_epsilons':[.25,.1],'lower_bound_single_term_degree':8,'lower_bound_plotted_from':16,
 'all_upper_bounds_identified_as_bounds':True,'series_values_numerical_not_a_proof':True},
 'proof_locators':['AF4–AF7','AF9'],'human_sources':['Hörmander II, Theorem 15.1.5, p. 276','Hörmander I, Definition 9.1.1, p. 326']}
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':['complex-carrier-and-diagonal','infinite-order-point-growth'],'pairs':2,'geometry':str(OUT/'geometry.json')}))
