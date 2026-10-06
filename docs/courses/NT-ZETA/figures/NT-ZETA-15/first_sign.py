"""Original CC0 figure and rigorous finite sign checks for psi(x)-x."""
from pathlib import Path
import math, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flint import arb, ctx

ctx.dps = 60
here = Path(__file__).resolve().parent
lcms, values, balls = {}, {}, []
integer = 1
for n in range(1, 32):
    integer = math.lcm(integer, n)
    enclosed = arb(integer).log()
    lcms[n], values[n] = integer, float(enclosed)
    if n <= 18:
        assert enclosed < n
    if n == 19:
        assert enclosed > n and integer == 232792560
    balls.append({'n': n, 'lcm': str(integer), 'psi': enclosed.str(55),
                  'error': (enclosed-n).str(55)})
(here/'sign-certificate.json').write_text(json.dumps({'license':'CC0-1.0',
    'decimal_precision':60,'first_positive_jump':19,'rows':balls},indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.size':24,'axes.titlesize':28,'axes.labelsize':26,
                     'xtick.labelsize':24,'ytick.labelsize':24})
fig, axes = plt.subplots(1, 2, figsize=(12, 5.3), layout='constrained')
for ax, limits, title in zip(axes, [(1,30),(18,20)],
                            ['Prime-power error','First positive jump']):
    ax.axhline(0,color='#555555',lw=1.4)
    for n in range(1,31):
        ax.plot([n,n+1],[values[n]-n,values[n]-(n+1)],color='#153f68',lw=2.7)
        if n>1:
            ax.plot([n,n],[values[n-1]-n,values[n]-n],color='#153f68',lw=1.5,alpha=.55)
        ax.plot(n,values[n]-n,'o',color='#153f68',ms=4)
    upper = values[19]
    xs = np.linspace(19,upper,100)
    ax.fill_between(xs,0,upper-xs,color='#209574',alpha=.4)
    ax.plot(19,upper-19,'o',color='#209574',ms=9)
    ax.set_xlim(*limits)
    ax.set_title(title)
    ax.set_xlabel('$x$')
    ax.set_ylabel(r'$\psi(x)-x$')
    ax.grid(alpha=.16)
axes[0].set_ylim(-4,1)
axes[0].set_xticks([5,15,25])
axes[1].set_ylim(-1.8,.75)
axes[1].set_xticks([18,19,20])
axes[1].annotate('$x=19$',(19,values[19]-19),xytext=(18.08,.5),
                 arrowprops={'arrowstyle':'->','color':'#209574'},color='#146b53',fontsize=24)
axes[1].plot(values[19],0,'o',color='#aa493f',ms=7)
axes[1].annotate(r'$19.265658\ldots$',(values[19],0),xytext=(19.04,-1.25),
                 arrowprops={'arrowstyle':'->','color':'#aa493f'},color='#aa493f',fontsize=23)
fig.savefig(here/'first_sign.png',dpi=180)
