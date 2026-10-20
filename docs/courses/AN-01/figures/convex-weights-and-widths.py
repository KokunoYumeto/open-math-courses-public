"""Exact log-convex weights and paired smoothing widths; CC0."""
from pathlib import Path
from math import lgamma,log
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN01-U151'})
fig,ax=plt.subplots(1,2,figsize=(13.8,5.5),layout='constrained')
j=np.arange(9)
c=np.array([2*lgamma(k+1) if k%2==0 else lgamma(k)+lgamma(k+2) for k in j])
b=c+3*(j%2)
ax[0].plot(j,c,color='#145d91',lw=2.5,label=r'$\log M_j^*$')
ax[0].scatter(j,b,color='#ab3b19',s=48,zorder=3,label=r'$\log M_j$')
for k in j[j%2==1]:
    ax[0].plot([k,k],[c[k],b[k]],color='#ab3b19',ls=':',lw=1.5)
ax[0].annotate('Odd allowances: +3',xy=(3,b[3]),xytext=(.4,14),
               arrowprops={'arrowstyle':'->','color':'#ab3b19'},color='#80331c')
ax[0].set(xlabel='Derivative order j',ylabel='Logarithmic weight',xticks=j,
          title='Convex boundary and contact orders')
ax[0].legend(loc='upper left')
k=np.arange(1,25)
r=(k-1)//2
a=1/((2*r+1)*(2*r+2))
ax[1].step(k,a,where='mid',color='#145d91',lw=2,label=r'$a_j$')
ax[1].scatter(k,a,color='#145d91',s=18)
ax[1].set(xlabel='Derivative order j',ylabel='Width $a_j$',ylim=(0,.58),
          title='Paired widths and their finite sum')
ay=ax[1].twinx()
ay.plot(k,np.cumsum(a),color='#a5411f',lw=2,label=r'$\sum_{j\leq m}a_j$')
ay.axhline(2*log(2),color='#a5411f',ls='--',lw=1.4)
ay.set(ylabel='Cumulative width',ylim=(0,1.6))
ay.text(11,2*log(2)+.045,r'$2\log 2$',color='#a5411f')
ax[1].legend(loc='upper left')
ay.legend(loc='center right')
for axy in ax:
    axy.grid(alpha=.17)
fig.savefig(out/'convex-weights-and-widths.png',dpi=160)
fig.savefig(out/'convex-weights-and-widths.svg',metadata={'Date':None})
p=out/'convex-weights-and-widths.svg'
p.write_text('\n'.join(x.rstrip() for x in p.read_text().splitlines())+'\n')
