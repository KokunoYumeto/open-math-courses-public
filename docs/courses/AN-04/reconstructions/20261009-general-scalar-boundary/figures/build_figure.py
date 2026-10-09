"""Exact slices of GS46; no solution intensity or numerical PDE estimate."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
eps=Fraction(1,8);delta=Fraction(1,64)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none','svg.hashsalt':'an04-general-scalar-boundary-20261009'})
fig,axs=plt.subplots(1,2,figsize=(12,5.8))
fig.subplots_adjust(top=.77,bottom=.25,left=.065,right=.985,wspace=.19)
blue='#386f91';green='#5b9a7e';orange='#dd8c52'
for ax in axs:
 ax.set_xlim(-2.2,1.32);ax.axvline(0,color='#aab6bf',lw=.6)
 ax.set_xlabel(r'Gliding clock coordinate $T=N/\delta$')
 ax.grid(alpha=.16);ax.set_xticks([-2,-1,0,1,float(1+eps)])
 ax.set_xticklabels(['−2','−1','0','1','9/8'])
 ax.tick_params(axis='x',labelsize=9)
for av,color,alpha,label in [(1,blue,.18,r'$W_1$'),(.5,green,.45,r'$W_{1/2}$')]:
 T=np.linspace(-1-av,1+av*float(eps),600)
 ymax=1+av+T
 axs[0].fill_between(T,0,ymax,color=color,alpha=alpha,label=label)
 axs[0].plot(T,ymax,color=color,lw=1.5)
 axs[0].plot([T[-1]]*2,[0,ymax[-1]],color=color,lw=1.5,ls='--')
 bound=np.sqrt(np.maximum(ymax,0))
 axs[1].fill_between(T,-bound,bound,color=color,alpha=alpha)
 axs[1].plot(T,bound,color=color,lw=1.5);axs[1].plot(T,-bound,color=color,lw=1.5)
 axs[1].plot([T[-1]]*2,[-bound[-1],bound[-1]],color=color,lw=1.5,ls='--')
Tin=np.linspace(1,1+float(eps),100)
axs[0].fill_between(Tin,0,2+Tin,color=orange,alpha=.65)
axs[1].fill_between(Tin,-np.sqrt(2+Tin),np.sqrt(2+Tin),color=orange,alpha=.65)
axs[0].set_ylim(-.12,3.48);axs[0].set_ylabel(r'Normal position $X=x/(\varepsilon\delta)$')
axs[1].set_ylim(-2.04,2.04);axs[1].set_ylabel(r'Transverse coordinate $V=v_1/(\varepsilon\delta)$')
axs[0].set_title(r'Normal slice $V=0$:  $0\leq X<1+a+T$',fontsize=11)
axs[1].set_title(r'Boundary slice $X=0$:  $V^2<1+a+T$',fontsize=11)
for ax in axs:
 ax.scatter([0],[0],c='black',s=18,zorder=5)
 ax.annotate('anchor',xy=(0,0),xytext=(-.9,.38),arrowprops={'arrowstyle':'-','lw':.7},fontsize=9)
 ax.annotate('',xy=(.08,0),xytext=(.94,0),arrowprops={'arrowstyle':'->','color':'#263b48','lw':1.8})
 ax.text(.68,.93,'Incoming support:\n'+r'$1<T<9/8$',transform=ax.transAxes,fontsize=9,ha='center',va='top',
         bbox={'facecolor':'white','alpha':.88,'edgecolor':'none','pad':2})
axs[0].legend(loc='upper left',frameon=False)
fig.suptitle('A fixed glancing window while the damping parameter changes',fontsize=15,fontweight='bold',y=.96)
fig.text(.5,.875,r'$\delta=1/64,\ \varepsilon=1/8,\ \varepsilon\delta=1/512.$  Outer: $a=1$; inner: $a=1/2$; orange: incoming $e_1$ strip.',
 ha='center',fontsize=11)
fig.text(.5,.12,r'$p=\rho^2-\eta_1^2-\eta_2^2+\eta_3^2,\quad \eta=(1,0,1),\quad z_3=-2\delta T,\quad z_1=\varepsilon\delta V+2\delta T,\quad z_2=0.$',
 ha='center',fontsize=10)
fig.text(.5,.065,'The arrow follows boundary gliding. Boundaries shown are excluded except for the physical face X = 0.\nExact support sections; no solution amplitude or numerical propagation claim. Proof: C5–C8 and Exercise 1.',
 ha='center',fontsize=9)
svg=P/'glancing-window-supports.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'AN-04 independent reproducible mathematical figure'})
plt.close(fig)
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
report={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'exact_parameters':{'delta':'1/64','epsilon':'1/8','normal_and_transverse_scale':'1/512','outer_a':'1','inner_a':'1/2'},
 'support':'X >= 0, T < 1 + a epsilon, X + V^2 < 1 + a + T',
 'omitted_coordinates':'eta=(1,0,1), z3=-2 delta T, z1=epsilon delta V+2 delta T, z2=0',
 'not_a_solution_intensity':True,'actually_inspected':False,'exact_coordinate_review_complete':False}
(P.parent/'figure-check.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps(report))
