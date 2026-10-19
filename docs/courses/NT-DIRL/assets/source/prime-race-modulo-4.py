"""Original CC0 exact finite prime-race illustration; no asymptotic inference."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
limit=100000
isprime=np.ones(limit+1,dtype=bool);isprime[:2]=False
for p in range(2,math.isqrt(limit)+1):
    if isprime[p]:isprime[p*p::p]=False
primes=np.flatnonzero(isprime);odd=primes[primes>2]
delta=np.cumsum(np.where(odd%4==3,1,-1))
first=next(int(p) for p,d in zip(odd,delta) if d<0)
assert first==26861 and delta[-1]==25
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path'})
fig,ax=plt.subplots(figsize=(11,5.7),layout='constrained')
fig.patch.set_facecolor('#faf9f4');ax.set_facecolor('#faf9f4')
ax.step(np.append(odd,limit),np.append(delta,delta[-1]),where='post',color='#173f4f',lw=1.6)
ax.axhline(0,color='#b65437',lw=1)
ax.plot(first,-1,'o',color='#b65437',ms=5)
ax.annotate('First negative value:\n'+f'{first:,}',xy=(first,-1),xytext=(1500,11),arrowprops={'arrowstyle':'->','color':'#b65437'},fontsize=11,color='#873d29')
ax.set_xscale('log');ax.set(xlim=(10,limit),xlabel=r'$x$ (logarithmic scale)',ylabel=r'$\pi(x;4,3)-\pi(x;4,1)$')
ax.set_title('A finite race between the two odd residue classes modulo 4',loc='left',fontweight='bold',pad=14)
ax.grid(axis='y',alpha=.15);ax.spines[['top','right']].set_visible(False)
dest=Path(__file__).resolve().parent.parent
fig.savefig(dest/'prime-race-modulo-4.png',dpi=170);fig.savefig(dest/'prime-race-modulo-4.svg')
print('Exact first negative value at',first,'; original CC0 finite-race plot saved.')
