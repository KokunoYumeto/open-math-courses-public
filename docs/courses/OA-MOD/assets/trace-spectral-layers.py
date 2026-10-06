"""Exact reproducible SL-05 illustration. Original October 2026; CC0."""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

out=Path(__file__).with_suffix('.png')
blue,orange,green,grey='#227896','#d1743e','#65934c','#969696'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,axs=plt.subplots(1,3,figsize=(18,7.5),dpi=120,gridspec_kw={'width_ratios':[1,1,1.15]})
fig.suptitle('Spectral layers retain both zero axes',fontsize=21,y=.97)
fig.text(.5,.91,r'$h=2p,\quad k=3q,\quad \mathrm{Tr}(pq)=3/4$ in $M_2(\mathbb{C})$ with ordinary trace',ha='center',fontsize=14)
ax=axs[0]
atoms=[(0,0,Fraction(3,4),grey),(2,0,Fraction(1,4),orange),(0,3,Fraction(1,4),green),(2,3,Fraction(3,4),blue)]
for s,t,m,c in atoms:
 ax.scatter(s,t,s=1050*float(m),c=c,alpha=.9,zorder=3)
 ax.annotate('mass '+str(m),(s,t),xytext=(0,27),textcoords='offset points',ha='center',fontsize=12,color=c)
ax.annotate('common origin omitted\nzero contribution',(0,0),xytext=(.7,.65),arrowprops={'arrowstyle':'->','color':grey},fontsize=10,color='#666666')
ax.set(xlim=(-.5,2.6),ylim=(-.55,3.9),xticks=[0,2],yticks=[0,3],xlabel='s: eigenvalue of h',ylabel='t: eigenvalue of k',title='Joint masses; disk area proportional to mass')
ax.grid(alpha=.15)
ax=axs[1];values=[Fraction(15,4),Fraction(1),Fraction(9,4)];bottom=0
for val,c in zip(values,[blue,orange,green]):
 ax.bar(.15,float(val),bottom=bottom,width=.65,color=c)
 ax.text(.15,bottom+float(val)/2,str(val),ha='center',va='center',color='white',fontweight='bold')
 bottom+=float(val)
ax.bar(1.25,np.sqrt(61),width=.6,color='#9299a3',alpha=.8)
ax.bar(2.35,2*np.sqrt(22),width=.6,color='#4b5360',alpha=.8)
for x,y,label in [(.15,7,'7'),(1.25,np.sqrt(61),r'$\sqrt{61}$'),(2.35,2*np.sqrt(22),r'$2\sqrt{22}$')]:
 ax.text(x,y+.2,label,ha='center',fontsize=14,fontweight='bold')
ax.set(xlim=(-.4,2.85),ylim=(0,11),xticks=[.15,1.25,2.35],xticklabels=[r'$\mathcal{D}(h,k)$',r'$\|h^2-k^2\|_1$',r'$\|h-k\|_2\|h+k\|_2$'],ylabel='Exact integral or norm',title='Three distinct quantities')
ax.tick_params(axis='x',labelsize=10)
ax=axs[2]
ax.fill_between([0,4],[.5,.5],color=blue,alpha=.22)
ax.fill_between([4,9],[1,1],color=orange,alpha=.22)
ax.plot([0,4],[.5,.5],color=blue,lw=3);ax.plot([4,9],[1,1],color=orange,lw=3);ax.plot([9,10],[0,0],color=grey,lw=3)
for x,y,c,closed in [(0,.5,blue,False),(4,.5,blue,True),(4,1,orange,False),(9,1,orange,True),(9,0,grey,False)]:
 ax.scatter(x,y,s=50,edgecolor=c,facecolor=c if closed else 'white',zorder=4)
ax.text(2,.25,'area 2',ha='center',va='center',color=blue,fontsize=14)
ax.text(6.5,.5,'area 5',ha='center',va='center',color=orange,fontsize=14)
ax.set(xlim=(-.2,10.2),ylim=(-.08,1.35),xticks=[0,4,9],yticks=[0,.5,1],yticklabels=['0','1/2','1'],xlabel=r'Threshold $a>0$',ylabel=r'$\|P_a(h)-P_a(k)\|_2^2$',title='Cutoff profile: total area 7')
for ax in axs:
 ax.spines[['top','right']].set_visible(False)
fig.text(.5,.11,'Both zero axes contribute: 1 + 9/4 = 13/4. The positive-positive atom contributes 15/4.',ha='center',fontsize=13)
fig.text(.5,.065,'Exact proof: SL-05; density norm: SL-06, Problem 2. Reference: Takesaki II, IX.2.14, pp. 180–182.',ha='center',fontsize=11)
fig.subplots_adjust(left=.055,right=.98,bottom=.23,top=.79,wspace=.42)
fig.savefig(out,metadata={'Author':'GPT-6.1 Sol (OpenAI), Ultra effort, October 2026','License':'CC0-1.0','Proof':'OA-MOD-SL-05; OA-MOD-SL-06, Problem 2'})
plt.close(fig)
assert sum(values)==7
print(out)
