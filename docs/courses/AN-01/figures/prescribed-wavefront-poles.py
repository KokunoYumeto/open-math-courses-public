"""Exact two-pair illustration for AN01-U080; original, CC0.

Requires numpy and matplotlib. Curves are numerical samples of proved formulas.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN01-U080'})
fig,axes=plt.subplots(1,3,figsize=(15,5.2),layout='constrained')
blue='#226aab';orange='#be5f14';green='#23815d'
ax=axes[0];ax.set_title('Prescribed covector rays')
ax.axhline(0,color='#9fa8b3',lw=1)
ax.annotate('',(0,1.55),(0,0),arrowprops=dict(arrowstyle='->',lw=2.4,color=blue))
ax.annotate('',(2,-1.55),(2,0),arrowprops=dict(arrowstyle='->',lw=2.4,color=orange))
ax.plot(0,1,'o',color=blue);ax.plot(2,-1,'o',color=orange)
ax.text(.12,1.03,r'$(0,+1)$',color=blue);ax.text(1.1,-1.15,r'$(2,-1)$',color=orange)
ax.set(xlim=(-.5,2.7),ylim=(-1.7,1.7),xlabel=r'Base point $x$',ylabel=r'Covector $\xi$')
ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax=axes[1];ax.set_title('Opposite tube boundary points')
ax.axhspan(-1,1,color='#eaf2f8');ax.axhline(1,color='#7c899b');ax.axhline(-1,color='#7c899b')
ax.axhline(0,color='#abb5c1',lw=.7)
ax.plot(0,-1,'o',color=blue,ms=7);ax.plot(2,1,'o',color=orange,ms=7)
ax.annotate('',(0,-.94),(0,0),arrowprops=dict(arrowstyle='->',color=blue,lw=2,linestyle=':'))
ax.text(.12,-.55,r'$z=-it$',color=blue);ax.text(.12,-1.32,r'$0-i$',color=blue);ax.text(1.85,1.2,r'$2+i$',color=orange)
ax.text(.8,.45,r'$|\operatorname{Im}z|<1$')
ax.set(xlim=(-.5,2.7),ylim=(-1.7,1.7),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax=axes[2];ax.set_title('A singularity that survives the sum')
t=np.linspace(0,.98,650)
K=lambda z:1/(4*np.cosh(np.pi*z/2))
A=1/(4*np.cos(np.pi*(1+t)/4));R=K(-1+1j*(1-t)/2)/16
U=A/4+R;lower=A/4-np.abs(R)
assert np.all(lower>0) and np.all(np.abs(U)+1e-12>=lower)
ax.semilogy(t,np.abs(U),color=blue,lw=2.3,label=r'$|U(-it)|$')
ax.semilogy(t,A/4,color=orange,lw=1.6,ls='--',label=r'$A(t)/4$')
ax.semilogy(t,lower,color=green,lw=1.7,ls=':',label=r'$A(t)/4-|R(t)|$')
ax.set(xlabel=r'$t$',ylabel='Magnitude (logarithmic scale)',xlim=(0,1))
ax.grid(alpha=.2);ax.legend(loc='upper left',frameon=False,fontsize=11);ax.spines[['top','right']].set_visible(False)
fig.suptitle('One distribution, two chosen singular directions',fontsize=18)
out=Path(__file__).resolve().parent
fig.savefig(out/'prescribed-wavefront-poles.png',dpi=180)
fig.savefig(out/'prescribed-wavefront-poles.svg',metadata={'Date':None,'Creator':'Original AN01-U080 figure; CC0'})
p=out/'prescribed-wavefront-poles.svg';p.write_bytes(('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n').encode())
