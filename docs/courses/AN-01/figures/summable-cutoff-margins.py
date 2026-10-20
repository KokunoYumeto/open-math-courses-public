"""Exact support intervals and geometric width budget for Theorem 3.
Original figure: GPT-6 Astra (OpenAI), 2026. CC0.
Run with numpy and matplotlib; writes PNG and SVG beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,(left,right)=plt.subplots(1,2,figsize=(12.8,5.1),gridspec_kw={'width_ratios':[1.35,1]})
segments=[(-2,2,'Domain X', '#64748b'),(-1.75,1.75,'Support bound', '#7c3aed'),(-1.5,1.5,'Averaged set $K_a$', '#db7c20'),(-1.25,1.25,'Plateau: $\\chi=1$', '#168787'),(-1,1,'Compact set K', '#1d4f91')]
for i,(a,b,label,color) in enumerate(segments):
    y=4-i
    left.plot([a,b],[y,y],color=color,lw=7,solid_capstyle='butt')
    left.scatter([a,b],[y,y],s=48,facecolor='white' if i in [0,2,3] else color,edgecolor=color,zorder=4)
    left.text(0,y+.2,label,ha='center',fontsize=10,color=color)
left.set(xlim=(-2.2,2.2),ylim=(-.4,4.65),yticks=[],xlabel='Original spatial coordinate x',
         xticks=[-2,-1.75,-1.25,-1,0,1,1.25,1.75,2])
left.set_xticklabels(['−2','−7/4','−5/4','−1','0','1','5/4','7/4','2'],rotation=45,ha='right')
left.set_title('A positive margin on both sides',pad=16)
N=np.arange(0,9)
tail=2.0**(-N-2)
right.plot(N,tail,'o-',color='#168787',lw=2)
right.set_yscale('log',base=2)
right.set(xlabel='Number N of interval averages',ylabel='Remaining translation radius',
          xticks=N,yticks=[2.**(-j) for j in [2,4,6,8,10]])
right.set_yticklabels(['1/4','1/16','1/64','1/256','1/1024'])
right.grid(axis='y',alpha=.2)
right.set_title(r'Exact tail: $\frac{1}{2}\sum_{j>N}d_j=2^{-N-2}$',pad=16)
fig.suptitle('Summable smoothing: support geometry and a vanishing tail',fontsize=15,y=.99)
fig.text(.5,.012,r'$d_j=2^{-j-1}$, $S=1/2$, $a=1/2$. Support bounds and budgets, not values of a cutoff.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.065,1,.93),w_pad=3)
for ext in ['png','svg']:
    p=root/('summable-cutoff-margins.'+ext)
    fig.savefig(p,dpi=190,facecolor='white')
    if ext=='svg':
        p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
assert all(tail==.25*2.**(-N))
print('Exact dyadic tail and support margins rendered.')
