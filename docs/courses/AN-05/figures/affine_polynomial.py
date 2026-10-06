"""Reproducible original diagram of the exact admissible polynomial countermodel."""
from pathlib import Path
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import hashlib,json
T=np.linspace(-1,1,1201)
P=sum(T**j/float(__import__('math').factorial(j)) for j in range(5))
derivatives=[sum(T**j/float(__import__('math').factorial(j)) for j in range(5-r)) for r in range(5)]
J=np.max(np.abs(np.stack(derivatives)),axis=0)
root=-T**9/P
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.labelsize':14,
                    'axes.titlesize':17,'legend.fontsize':12})
fig,axs=plt.subplots(1,2,figsize=(15,8.8),dpi=140)
fig.patch.set_facecolor('#fcfcf9')
for ax in axs:
    ax.set_facecolor('#fcfcf9')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.17)
    ax.set_xlabel(r'Normalized time $T$')
    ax.set_xlim(-1.04,1.04)
axs[0].plot(T,P,color='#176887',lw=3,label=r'$P(T)=\sum_{j=0}^4 T^j/j!$')
axs[0].plot(T,J,color='#454545',lw=2,ls=(0,(4,3)),
            label=r'$J(T)=\max_{0\leq j\leq9}|P^{(j)}(T)|$')
axs[0].axhline(2,color='#a33828',ls=':',lw=2,label='Stated pointwise upper bound: 2')
axs[0].scatter([.75],[4331/2048],color='#a33828',s=48,zorder=5)
axs[0].annotate(r'$P(3/4)=4331/2048>2$',xy=(.75,4331/2048),xytext=(-.91,2.95),
               arrowprops={'arrowstyle':'->','color':'#a33828','lw':1.5},color='#a33828')
axs[0].set_ylim(0,3.13)
axs[0].set_ylabel('Exact coefficient / absolute jet maximum')
axs[0].set_title('A center maximum of one can exceed two')
axs[0].text(-.94,2.56,r'$P(T)=\sum_{j=0}^4 T^j/j!$',color='#176887',fontsize=12)
axs[0].text(-.94,2.31,r'$J(T)=\max_{0\leq j\leq9}|P^{(j)}(T)|$',color='#454545',fontsize=12)
axs[0].text(-.94,1.83,'Stated pointwise upper bound = 2',color='#a33828',fontsize=11)
axs[1].plot(T,root,color='#176887',lw=3)
axs[1].axhline(0,color='#454545',lw=.8)
axs[1].set_ylim(-.55,2.9)
axs[1].set_ylabel(r'$9!\,\eta_{\mathrm{zero}}/\rho=-T^9/P(T)$')
axs[1].set_title('The cancellation frequency is nonincreasing')
axs[1].annotate('Positive coefficient at every real time:\n'
                'an earlier positive value cannot become negative.',
                xy=(-.68,float(-(-.68)**9/sum((-.68)**j/float(__import__('math').factorial(j)) for j in range(5)))),
                xytext=(-.91,1.72),
                arrowprops={'arrowstyle':'->','color':'#176887','lw':1.4},fontsize=12)
for ax,values in [(axs[0],P),(axs[1],root)]:
    ax.scatter([-1,1],[values[0],values[-1]],facecolors='#fcfcf9',edgecolors='#176887',s=55,lw=1.6,zorder=5)
fig.suptitle('Exact case-II model: k = 9, any fixed ρ ≥ 1',fontsize=20,y=.975)
fig.subplots_adjust(left=.078,right=.972,bottom=.29,top=.87,wspace=.34)
fig.text(.078,.155,'The curves use the open model interval |T| < 1; hollow endpoints show limiting values.\n'
         'Left: the unregularized coefficient. For G = P + D/M with D ≥ 0, G(3/4) ≥ P(3/4).\n'
         'Right: the exactly scaled affine zero. Positivity of P and the proved derivative formula fix its direction.',
         fontsize=12,color='#333333',linespacing=1.5)
fig.text(.078,.038,'Original diagram by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. CC0.\n'
         'Self-checked draft; no independent review. Proof locators: lesson Sections 7–8, (7.4)–(7.10), (8.3).',
         fontsize=10,color='#454545')
out=Path(__file__).with_name('affine-polynomial.png')
fig.savefig(out,dpi=140,metadata={'Software':'Matplotlib; original CC0 diagram'})
plt.close(fig)
