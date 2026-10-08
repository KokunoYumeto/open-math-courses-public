"""Original Figure10.26, individual factorial-preserving scalar bounds. CC0.
OpenAI Codex, GPT-6.1 Sol, Ultra effort. See TR-BAKER-10 Section38
for the complete positive-series proof and free human mathematical sources.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial, lcm, log
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = (HERE.parent/'figures/individual-clearing-euler.png'
       if HERE.name == 'figure_sources' else HERE/'individual-clearing-euler.png')
k, L, D, R, m, O = 4, 2, 8, 15, 17, 10
v = lcm(*range(1, k+1)); z = Q(1, 13)
orders = list(range(9))
actual = [Q(v**u*comb(D,u)*R**(D-u)*comb(m+O-u,O-u),factorial(k)**L)
          for u in orders]
fixed = [Q(comb(D,u)*R**(D-u),factorial(k)**L)*z**(-O)*(1-z)**(-m-1)
         for u in orders]
uniform = Q((R+1)**D,factorial(k)**L)*z**(-O)*(1-z)**(-m-1)
assert max(orders,key=lambda u:actual[u]) == 1
assert actual[1] == 88976443359375
assert all(a <= b <= uniform for a,b in zip(actual,fixed))
plt.rcParams.update({'font.size':14,'axes.titlesize':16,'axes.labelsize':14,
                     'axes.spines.top':False,'axes.spines.right':False})
fig, axes = plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
axes[0].plot(orders,[log(float(x)) for x in actual],'o-',color='#217a87',
             label='Actual scalar (10.240)')
axes[0].plot(orders,[log(float(x)) for x in fixed],'s--',color='#a45435',
             label='Fixed-order bound (10.312)')
axes[0].axhline(log(float(uniform)),color='#785f97',ls=':',lw=2,
                label='Uniform bound (10.312)')
axes[0].scatter([1],[log(float(actual[1]))],s=110,facecolors='none',
                edgecolors='#344451',linewidths=2,zorder=5)
axes[0].set(xlabel='Additive order u; Euler order = 10 - u',
            ylabel='Natural logarithm of the scalar bound',
            title='Each individual allocation\nretains the factorial denominator')
axes[0].legend(fontsize=10,loc='lower left')
axes[0].text(.98,.66,'k = 4, L = 2, D = 8\nR = 15, m = 17\nv(4) = 12, z = 1/13',
             transform=axes[0].transAxes,ha='right',fontsize=10)
ranks = list(range(2,16))
for I,color in [(0,'#217a87'),(1,'#a45435'),(2,'#785f97')]:
    values=[Q(1000,999)*Q(3,8)*Q(r-1,15*(r+1)**2*2**I) for r in ranks]
    axes[1].plot(ranks,list(map(float,values)),'o-',color=color,
                 label=f'q = 2, depth I = {I}')
axes[1].axhline(1/300,color='#344451',ls='--',lw=1.5,label='Bound 1/300 at depth 0')
axes[1].set(xlabel='Rank r',ylabel='Remainder divided by Z, before the extra term',
            title='Uniform individual remainder\nproved at every field and prime',
            ylim=(0,.0041))
axes[1].text(.03,.94,'Additional remainder: (r - 1)/999\nis retained separately.',
             transform=axes[1].transAxes,va='top',fontsize=10)
axes[1].legend(fontsize=10,loc='upper right')
for ax in axes:ax.grid(alpha=.17)
fig.savefig(OUT,dpi=180,facecolor='white')
plt.close(fig)
