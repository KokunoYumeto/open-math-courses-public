from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
s=np.linspace(0,1,1601)
t=4
ht=np.where(s<1/(t+1),0,np.where(s<1/t,(s-1/(t+1))/(1/t-1/(t+1)),np.where(s<=1-1/t,1,np.where(s<=1-1/(t+1),(1-1/(t+1)-s)/(1/t-1/(t+1)),0))))
fig,ax=plt.subplots(3,1,figsize=(7.0,9.3))
for a,end,color in [(ax[0],0,'#155fa0'),(ax[1],1,'#b34529')]:
    a.plot(s,ht,color='#788493',lw=2,label=r'$h_4(s)$')
    lo,hi=(.2,.25) if end==0 else (.75,.8)
    mask=(s>=lo)&(s<=hi)
    a.fill_between(s[mask],0,ht[mask],color=color,alpha=.23)
    a.annotate('',xy=(hi,.54),xytext=(lo,.54),arrowprops={'arrowstyle':'->','lw':2,'color':color})
    a.set(xlim=(0,1),ylim=(-.04,1.27),xlabel=r'Increasing suspension coordinate $s$',ylabel=r'Ideal approximate identity $h_4(s)$')
    a.set_xticks([0,.2,.25,.75,.8,1],['0','1/5','1/4','3/4','4/5','1'])
    a.tick_params(axis='x',labelsize=8)
    a.spines[['top','right']].set_visible(False)
    a.text(.5,1.17,'Only the shaded ramp survives the section',ha='center',fontsize=9)
ax[0].set_title(r'Cone vanishes at 1; evaluate at 0',fontsize=11)
ax[0].text(.5,.12,r'Raw $\epsilon=1_S$: winding $+1$'+'\n'+r'Native $\partial=-b$; $e^{2\pi i(1-s)}$',ha='center',fontsize=10,color='#155fa0')
ax[1].set_title(r'Cone vanishes at 0; evaluate at 1',fontsize=11)
ax[1].text(.5,.12,r'Raw $\epsilon=\rho$: winding $-1$'+'\n'+r'Native $\partial=+b$; $e^{2\pi i s}$',ha='center',fontsize=10,color='#b34529')
a=ax[2]
a.plot([0,1,1,0],[0,0,1,1],color='#26364a',lw=3)
a.scatter([0,0],[0,1],s=40,c='#26364a')
a.text(.5,-.12,r'$h=0$: both unitaries equal 1',ha='center',fontsize=9)
a.text(.5,1.11,r'$h=1$: $U=e^{2\pi iu}$, $W=1$',ha='center',fontsize=9)
a.text(1.09,.5,r'$u=1$'+'\n'+r'$U=1$'+'\n'+r'$W=e^{-2\pi ih}$',va='center',fontsize=9)
a.text(.05,.45,r'$X:\ (1-u)h(1-h)=0$',fontsize=10)
a.set(xlim=(-.12,1.65),ylim=(-.3,1.35),xlabel=r'$u$',ylabel=r'$h$')
a.set_xticks([0,1]);a.set_yticks([0,1]);a.spines[['top','right']].set_visible(False)
a.set_title('The joint spectrum in Proposition 8.3',fontsize=11)
fig.suptitle('Boundary signs for the two cone endpoints',fontsize=14,y=.98)
fig.tight_layout(rect=[0,0,1,.93])
for ext in ['svg','png']:
    fig.savefig(out/f'KT-KK-21-cone-signs.{ext}',dpi=170,bbox_inches='tight',metadata={'Creator':'Original mathematical figure; CC0'})
print('Rendered KT-KK-21-cone-signs.svg and .png')
