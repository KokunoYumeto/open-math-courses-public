"""Original frequency geometry and exact ordered-word counts for microlocal ellipticity."""
from pathlib import Path
from functools import lru_cache
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'microlocal-ellipticity',
                     'font.size':12,'figure.facecolor':'white'})
def save(fig,name,title):
    fig.savefig(OUT/(name+'.png'),dpi=150,metadata={'Software':'Matplotlib; original mathematical course diagram'})
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Title':title})
    plt.close(fig)

fig,ax=plt.subplots(figsize=(9.5,7.5),layout='constrained')
ax.fill([0,6,6],[0,6,-6],color='#dce7f7',label=r'Forcing cone $\Gamma$')
ax.fill([0,6,6],[0,3,-3],color='#c5e1ce',label=r'Smaller output cone $\Gamma^\prime$')
ax.plot([0,6],[0,6],color='#7394c3',ls='--')
ax.plot([0,6],[0,-6],color='#7394c3',ls='--')
ax.plot([0,6],[0,3],color='#52916a',ls=':')
ax.plot([0,6],[0,-3],color='#52916a',ls=':')
theta=np.linspace(0,2*np.pi,1025)
ax.plot(2*np.cos(theta),2*np.sin(theta),color='#7b7b7b',ls='--',label=r'Length threshold $|\eta|=|\xi|/2=2$')
ax.axvline(0,color='#303030',lw=1.2,ls=':',label=r'Characteristic set $\eta_1=0$')
points=[(4,0,r'$\xi=(4,0)$','#184b35',(4.12,-.65)),
        (3,1,r'Good $\eta=(3,1)$','#215fa5',(3.25,1.18)),
        (1,3,r'Angular region $(1,3)$','#a2393b',(1.25,3.2)),
        (1,0,r'Small-length region $(1,0)$','#a46b16',(.15,-1.0))]
for x,y,label,color,pos in points:
    ax.scatter([x],[y],s=55,color=color,zorder=5)
    ax.annotate(label,xy=(x,y),xytext=pos,color=color,
                arrowprops={'arrowstyle':'-','color':color},
                bbox={'facecolor':'white','edgecolor':'none','alpha':.94})
ax.annotate('',xy=(4,0),xytext=(1,3),arrowprops={'arrowstyle':'->','lw':2,'color':'#a2393b'})
ax.text(2.7,2.05,r'$\xi-\eta$',color='#a2393b',bbox={'facecolor':'white','edgecolor':'none','alpha':.94})
ax.set(xlim=(-1.25,6),ylim=(-3.6,3.9),xlabel=r'First frequency coordinate',ylabel=r'Second frequency coordinate',
       title='Fourier convolution: regular input or a separated tail\n'+r'$p_m(\xi)=\xi_1$, $\xi=(4,0)$')
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.16)
ax.legend(loc='lower right',fontsize=9,framealpha=.96)
save(fig,'noncharacteristic-frequency-cones','Noncharacteristic frequency cones and separated tails')

m=3;J=5
@lru_cache(None)
def words(q):
    if q==0:return ((),)
    if q<0:return ()
    return tuple((j,)+tail for j in range(1,m+1) for tail in words(q-j))
retained=tuple(w for q in range(J+1) for w in words(q))
remainder=tuple((j,)+w for w in retained for j in range(1,m+1) if sum(w)+j>J)
assert len(retained)==28 and len(remainder)==57 and len(set(remainder))==57
counts=[sum(sum(w)==q for w in retained) if q<=J else sum(sum(w)==q for w in remainder) for q in range(J+m+1)]
assert counts==[1,1,2,4,7,13,24,20,13]
fig,ax=plt.subplots(figsize=(9.5,5.2),layout='constrained')
q=np.arange(J+m+1);colors=['#3e74aa' if k<=J else '#b77e31' for k in q]
ax.bar(q,counts,color=colors,width=.72)
for k,count in zip(q,counts):ax.text(k,count+.45,str(count),ha='center',fontsize=12)
ax.axvline(J+.5,color='#555555',ls='--')
ax.text(2.2,26.7,'Retained: 28 ordered words',ha='center',color='#285d91')
ax.text(7,26.7,'Remainder: 57',ha='center',color='#8e5c1e')
ax.set(xlim=(-.6,8.6),ylim=(0,29),xticks=q,xlabel=r'Total weight $q$',ylabel='Number of ordered words',
       title='Finite adjoint inverse and first-crossing remainder\n'+r'$m=3$, $J=N+\mu=5$, $(I-\mathcal{R})w_J=\chi-E_J$')
ax.grid(axis='y',alpha=.18)
save(fig,'weighted-adjoint-word-counts','Exact retained and first-crossing ordered-word counts')

data={'license':'CC0-1.0','frequency_model':{'symbol':'p_m(xi)=xi_1',
      'forcing_cone':'eta_1>0 and abs(eta_2)<eta_1',
      'output_cone':'xi_1>0 and abs(xi_2)<xi_1/2','output_frequency':[4,0],
      'good_input':[3,1],'angular_input':[1,3],'small_length_input':[1,0],
      'length_threshold':2,'angular_gap':'pi/4-atan(1/2)',
      'exact_separation_constant':'min(1/3,sin((pi/4-atan(1/2))/2))',
      'actual_wavefront_of_a_particular_forcing_plotted':False},
      'ordered_words':{'maximum_part':m,'N':4,'distribution_order_mu':1,'retained_weight_limit':J,
      'counts_by_weight':counts,'retained_count':28,'remainder_count':57,
      'remainder_definition':'prefix j in1..m to retained tail;keep only total weight>J',
      'commutativity_assumed':False}}
(ROOT/'microlocal-ellipticity-figures.json').write_bytes((json.dumps(data,indent=2,sort_keys=True)+'\n').encode())
