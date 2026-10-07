"""Reproduce the exact L134 kernel caps and moving logarithmic wells."""
from pathlib import Path
from fractions import Fraction
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

OWN=Path(__file__).resolve().parent
OUT=OWN/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                    'mathtext.fontset':'dejavusans','svg.fonttype':'none',
                    'svg.hashsalt':'AN02-L134-subharmonic-convergence',
                    'text.usetex':False,'axes.spines.top':False,'axes.spines.right':False})
BLUE,ORANGE,GREEN,RED='#2166ac','#df7c24','#188557','#b2182b'
def finish(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=180,metadata={'Software':'Matplotlib; original L134 diagram, CC0-1.0'})
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,
                'Creator':'GPT-6.1 Sol (OpenAI), Ultra; original L134 diagram, CC0-1.0',
                'Description':'Exact formulas and coordinates in geometry.json; proof in SC4 and SC9.'})
    plt.close(fig)

delta=.4
fig,axes=plt.subplots(1,3,figsize=(13.8,4.6),layout='constrained')
r=np.linspace(.055,1.2,800)
axes[0].plot(r,-1/(4*np.pi*r),color='#555555',lw=2,label=r'$E_3(r)=-1/(4\pi r)$')
axes[0].plot(r,-1/(4*np.pi*np.maximum(r,delta)),color=BLUE,lw=2.6,label=r'$E_3^\delta(r)$')
axes[0].axvline(delta,color=ORANGE,ls=':',lw=1.6)
axes[0].annotate(r'$\delta=0.4$',xy=(delta,-1/(4*np.pi*delta)),xytext=(.65,-.43),
                 arrowprops={'arrowstyle':'->','color':ORANGE},color=ORANGE)
axes[0].annotate(r'$E_3(r)\to-\infty$',xy=(.07,-1/(4*np.pi*.07)),xytext=(.32,-1.15),
                 arrowprops={'arrowstyle':'->','color':'#555555'})
axes[0].set(xlabel='radius r',ylabel='kernel value',title='Keep a continuous cap',xlim=(0,1.2),ylim=(-1.5,.03))
axes[0].legend(loc='upper right',fontsize=9); axes[0].grid(alpha=.14)
rr=np.linspace(0,delta,400); density=rr-rr**2/delta
axes[1].plot(rr,density,color=GREEN,lw=2.4); axes[1].fill_between(rr,0,density,color=GREEN,alpha=.17)
axes[1].axvline(delta,color=ORANGE,ls=':')
axes[1].text(.025,.113,r'$\int_0^\delta(r-r^2/\delta)\,dr=\delta^2/6$',fontsize=11)
axes[1].set(xlabel='radius r',ylabel=r'$4\pi r^2|E_3-E_3^\delta|$',
            title='The small-ball error has small mass',xlim=(0,.45),ylim=(0,.135))
axes[1].grid(alpha=.14)
ds=np.logspace(-3,0,240)
axes[2].loglog(ds,ds**2/6,color=BLUE,lw=2.4,label=r'3D: $L^1=\delta^2/6$')
axes[2].loglog(ds,np.sqrt(ds/(12*np.pi)),color=ORANGE,lw=2.4,label=r'3D: $L^2=(\delta/(12\pi))^{1/2}$')
axes[2].loglog(ds,ds**2/4,color=GREEN,lw=2.1,ls='--',label=r'2D: $L^1=\delta^2/4$')
axes[2].set(xlabel=r'cap radius $\delta$',ylabel='exact error norm',title='Remove the cap after the sequence limit')
axes[2].legend(fontsize=9,loc='upper left'); axes[2].grid(which='both',alpha=.13)
finish(fig,'kernel-cap-and-norms')

observation=(Fraction(37,100),Fraction(61,100)); levels=[]
for m,N in enumerate([3,8,21,55,149,404,1097,2981],1):
    assert math.ceil(math.exp(m))==N
    indices=tuple(round(float(x)*N) for x in observation)
    point=tuple(Fraction(k,N) for k in indices)
    squared=sum((x-a)**2 for x,a in zip(observation,point))
    distance=math.sqrt(float(squared)); radius=math.exp(-m); bound=math.sqrt(2)/(2*N)
    assert 0<distance<=bound<radius
    far_squared=sum((x-a)**2 for x,a in zip(observation,(Fraction(1),Fraction(0))))
    near_value=math.log(distance)/m; far_value=math.log(math.sqrt(float(far_squared)))/m
    assert near_value<=-1
    levels.append({'m':m,'N':N,'block_terms':(N+1)**2,'nearest_indices':list(indices),
        'nearest_point_exact':[str(x) for x in point],'distance_squared_exact':str(squared),
        'nearest_distance':distance,'distance_bound':bound,'well_radius':radius,
        'nearest_value':near_value,'fixed_far_corner':[1,0],'far_value':far_value})

fig,axes=plt.subplots(1,3,figsize=(13.8,4.8),layout='constrained'); ax=axes[0]
for k in range(4):
    for ell in range(4):
        ax.add_patch(Circle((k/3,ell/3),math.exp(-1),facecolor=BLUE,edgecolor=BLUE,lw=.7,alpha=.07))
        ax.plot(k/3,ell/3,'o',color=BLUE,markersize=3)
ax.add_patch(Rectangle((0,0),1,1,fill=False,color='#222222',lw=1.9))
ax.plot(float(observation[0]),float(observation[1]),'x',color=RED,ms=9,mew=2)
ax.annotate(r'$x_0=(0.37,0.61)$',xy=tuple(map(float,observation)),xytext=(.055,1.15),
            arrowprops={'arrowstyle':'->','color':RED},fontsize=10,color=RED)
ax.text(.02,-.24,r'$N_1=3$; radius $e^{-1}$; 16 terms',fontsize=10)
ax.set(xlabel=r'$x_1$',ylabel=r'$x_2$',title='Every block has a nearby well',xlim=(-.29,1.29),ylim=(-.30,1.29),aspect='equal')
ax.set_xticks([0,1/3,2/3,1],['0','1/3','2/3','1']); ax.set_yticks([0,.5,1])
ms=np.array([1,2,3]); width=.23
axes[1].bar(ms-width,[a['nearest_distance'] for a in levels[:3]],width,color=BLUE,label='actual nearest distance')
axes[1].bar(ms,[a['distance_bound'] for a in levels[:3]],width,color=GREEN,label=r'bound $\sqrt{2}/(2N_m)$')
axes[1].bar(ms+width,[a['well_radius'] for a in levels[:3]],width,color=ORANGE,label=r'well radius $e^{-m}$')
axes[1].set(xlabel='block level m',ylabel='distance from observation point',title='Nearest distance < well radius',xticks=ms,ylim=(0,.43))
axes[1].legend(fontsize=9); axes[1].grid(axis='y',alpha=.14)
ms=np.arange(1,9)
axes[2].plot(ms,[a['nearest_value'] for a in levels],'o-',color=BLUE,lw=2,label='one nearest-center term')
axes[2].plot(ms,[a['far_value'] for a in levels],'s-',color=ORANGE,lw=2,label='corner (1,0) term')
axes[2].axhline(-1,color=GREEN,ls=':',label='deep-well threshold'); axes[2].axhline(0,color='#555555',lw=.8)
axes[2].set(xlabel='block level m',ylabel=r'$m^{-1}\log|x_0-a|$',title='Different subsequences at the same point',xticks=[1,2,4,6,8],ylim=(-2.9,.12))
axes[2].legend(fontsize=9,loc='lower right'); axes[2].grid(alpha=.14)
finish(fig,'moving-logarithmic-wells')
geometry={'schema':'AN02-L134-original-diagram-geometry/v1',
    'kernel_convention':'Delta E_n=delta_0; E3=-1/(4*pi*r); E2=log(r)/(2*pi)',
    'cap':{'delta_exact':'2/5','capped_kernel':'E_n(max(r,delta))',
           'three_dimensional_L1_error':'delta^2/6','three_dimensional_L2_error_squared':'delta/(12*pi)',
           'two_dimensional_L1_error':'delta^2/4',
           'radial_three_dimensional_L1_error_density':'r-r^2/delta for 0<r<delta; zero otherwise',
           'proof_locators':['SC4.1-SC4.3','SC5.2','SC11 Exercise1']},
    'moving_wells':{'domain':'(0,1)^2','observation_exact':['37/100','61/100'],
        'level_definition':'N_m=ceil(exp(m)); all (k/N_m,l/N_m), 0<=k,l<=N_m',
        'value_definition':'log(|x-a|)/m; log(0)=-infinity','finite_block_terms':'(N_m+1)^2',
        'universal_nearest_bound':'sqrt(2)/(2*N_m)<exp(-m)',
        'limits':'limsup=0 and liminf<=-1 everywhere in the open square',
        'plotted_levels':levels,'proof_locators':['SC9 Example2','SC9.1-SC9.4','SC11 Exercise6']},
    'author':'GPT-6.1 Sol (OpenAI), Ultra; original diagram content CC0-1.0',
    'figure_font_terms':'DejaVu-font-license.txt'}
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figures':2,'first_level':levels[0],'last_level':levels[-1]},indent=2))
