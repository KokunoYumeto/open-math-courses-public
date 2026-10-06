"""Original illustration of Dirichlet's hyperbola decomposition; CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(7.4,6.4),layout='constrained')
blue='#22718a';gold='#a86119';purple='#71508a'
t=np.linspace(1,16,700);curve=16/t
ax.fill_between(t,1,np.minimum(curve,4),color=gold,alpha=.18)
left=np.linspace(1,4,300)
ax.fill_between(left,1,16/left,color=blue,alpha=.18)
ax.fill_between(left,1,4,color=purple,alpha=.18)
counts={'vertical':0,'horizontal':0,'overlap':0,'union':0}
for a in range(1,17):
    for b in range(1,17):
        if a*b<=16:
            counts['union']+=1;counts['vertical']+=a<=4;counts['horizontal']+=b<=4;counts['overlap']+=(a<=4 and b<=4)
            color=purple if a<=4 and b<=4 else blue if a<=4 else gold
            ax.scatter(a,b,c=color,s=23,zorder=4)
assert counts=={'vertical':33,'horizontal':33,'overlap':16,'union':50}
ax.plot(t,curve,color='#263e38',lw=2,label='ab = 16')
ax.axvline(4,color=blue,ls='--',lw=1.4);ax.axhline(4,color=gold,ls='--',lw=1.4)
ax.text(4.3,14.8,'a = 4',color=blue,fontsize=17)
ax.text(12.2,4.3,'b = 4',color=gold,fontsize=17)
ax.text(6.8,10.7,'a at most 4: 33',color=blue,fontsize=18)
ax.text(6.8,9.3,'b at most 4: 33',color=gold,fontsize=18)
ax.text(6.8,7.9,'Overlap: 16',color=purple,fontsize=18)
ax.text(6.8,6.4,'33 + 33 - 16 = 50',fontsize=18,color='#263e38')
ax.set(xlim=(.5,16.7),ylim=(.5,16.7),xlabel='a',ylabel='b')
ax.set_title('The hyperbola decomposition\n50 integer points with ab at most 16',fontsize=17)
ax.tick_params(labelsize=16);ax.xaxis.label.set_size(18);ax.yaxis.label.set_size(18)
ax.set_aspect('equal');ax.set_xticks([1,4,8,12,16]);ax.set_yticks([1,4,8,12,16]);ax.grid(alpha=.15);ax.legend(loc='upper right',fontsize=16)
fig.savefig(out/'hyperbola.png',dpi=180,metadata={'Software':None})
print(counts)
