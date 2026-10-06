"""Original illustration for OA-MOD-NC-25, Problem 1. CC0-1.0.

GPT-6.1 Sol (OpenAI), Ultra effort, October 2026.
Run with Python, NumPy and Matplotlib; writes the PNG beside this source.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

points=np.array([[-1,-2],[-1,3],[2,-2],[2,3]])
mass=np.array([3.,1.,.25,.75])
differences=(points[:,0]-points[:,1])**2
crossed=(points[:,0]>=0)!=(points[:,1]>=0)
assert np.isclose(mass.sum(),5)
assert np.isclose(mass@differences,95/4)
assert np.isclose(mass@crossed,5/4)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(12,9))
grid=fig.add_gridspec(2,2,height_ratios=[2,1],hspace=.55,wspace=.35)
ax=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1])]
fig.subplots_adjust(left=.09,right=.97,bottom=.12,top=.86)
fig.suptitle('Joint spectral measures and the cutoff exponent',fontsize=20,y=.975)
fig.text(.5,.925,r'$\xi=\mathrm{diag}(2,1)$; left spectrum $s\in\{-1,2\}$, right spectrum $t\in\{-2,3\}$',ha='center',fontsize=13)
colors=['#286A91','#BD6538','#718D32','#8669A4']
ax[0].scatter(points[:,0],points[:,1],s=mass*500,c=colors,alpha=.83,edgecolors='white',linewidths=2)
for (s,t),label in zip(points,['3','1','1/4','3/4']):
    ax[0].annotate('mass '+label,(s,t),xytext=(0,23),textcoords='offset points',ha='center',fontsize=12)
ax[0].set(xlim=(-2,3),ylim=(-3.5,4.5),xticks=[-1,2],yticks=[-2,3],xlabel='s: eigenvalue of h',ylabel='t: eigenvalue of k',title='Joint atoms; area ∝ mass')
ax[0].grid(alpha=.2);ax[0].set_axisbelow(True)
bottom=np.zeros(2)
for m,d,c,color,label in zip(mass,differences,crossed,colors,['(-1, -2)','(-1, 3)','(2, -2)','(2, 3)']):
    vals=np.array([m*d,m*c]);ax[1].bar([0,1],vals,bottom=bottom,width=.48,color=color,label=label)
    for i,value in enumerate(vals):
        if value>=1.5:
            ax[1].text(i,bottom[i]+value/2,f'{value:g}',ha='center',va='center',color='white',fontsize=11,fontweight='bold')
        elif value>0:
            label={.75:'3/4',.25:'1/4',1.:'1'}[value]
            height=bottom[i]+value/2
            target=height if value!=.25 else 3.1
            ax[1].annotate(label,(i+.23,height),xytext=(i+.33,target),ha='left',va='center',fontsize=11,color=color,fontweight='bold',arrowprops={'arrowstyle':'-','color':color,'lw':1.2})
    bottom+=vals
ax[1].text(0,95/4+.6,'95/4',ha='center',fontsize=14,fontweight='bold')
ax[1].text(1,5/4+.6,'5/4',ha='center',fontsize=14,fontweight='bold')
ax[1].set(ylim=(0,28),xticks=[0,1],xticklabels=['hξ − ξk','p₊ξ − ξq₊'],ylabel='Squared Hilbert–Schmidt norm',title='Sum of weighted differences')
ax[1].legend(title='Atom (s, t)',loc='upper right',fontsize=10,title_fontsize=10)
chain=fig.add_subplot(grid[1,:]);j=np.arange(17)
chain.plot(j,np.ones(17),color='#286A91',lw=3)
chain.plot([0,1],[1,1],color='#BD6538',lw=5)
chain.scatter(j[1:],np.ones(16),s=85,color='#718D32',zorder=3)
chain.scatter([0],[1],s=85,color='white',edgecolors='#286A91',lw=2,zorder=3)
chain.axvline(.5,color='#BD6538',ls='--',lw=1.5)
chain.set(xlim=(-.5,16.5),ylim=(.4,1.75),xticks=j,yticks=[],xlabel='Coordinate j; x has eigenvalue j/16',title='The best nonzero cutoff excludes coordinate zero (NC-25, Problem 4)')
chain.text(8,1.48,r'$\xi=I+\frac{1}{4}T$: each neighbouring matrix entry is $1/4$',ha='center',fontsize=12)
chain.text(8,.58,r'$A_k=1/8$,  $B_k\leq287/8$,  $\varepsilon^2=1/1667$:  $A_k/B_k\geq1/287>4/1667$',ha='center',fontsize=12)
chain.spines['left'].set_visible(False);chain.spines['bottom'].set_visible(False)
fig.text(.5,.04,'Exact joint calculation: NC-25, Problem 1. Complete exponent disproof: NC-25, Problem 4.',ha='center',fontsize=11)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180,metadata={'Software':'Original mathematical illustration; GPT-6.1 Sol (OpenAI), Ultra, October 2026; CC0-1.0'})
plt.close(fig)
