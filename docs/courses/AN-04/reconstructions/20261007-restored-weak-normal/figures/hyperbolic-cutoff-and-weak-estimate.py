"""Exact projected support of HN17–HN19, and the orders of HN26–HN39."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':12, 'svg.fonttype':'none'})
out = Path(__file__).resolve().parent
beta = .75
alpha = np.linspace(-(1+beta), 1+beta, 601)
height = np.sqrt(np.maximum(1+beta-alpha,0))
fig, (ax, panel) = plt.subplots(1,2,figsize=(14,6), constrained_layout=True,
                              gridspec_kw={'width_ratios':[1.02,1.22]})
ax.fill_between(alpha, 0, height, color='#e2edf7')
incoming = alpha <= -beta
ax.fill_between(alpha[incoming], 0, height[incoming], color='#f5d8af')
ax.plot(alpha,height,color='#165e91',lw=2.5)
ax.axvline(-(1+beta),color='#a15a13',lw=2)
ax.axvline(-beta,color='#a15a13',ls='--',lw=1.5)
ax.axvline(0,color='#52606c',ls=':',lw=1.5)
ax.add_patch(Rectangle((-2,0),4,2,fill=False,ec='#777',ls='--',lw=1))
ax.scatter([0],[0],s=70,color='#16324f',zorder=5)
ax.annotate('anchor', (0,0), xytext=(.24,.22), arrowprops={'arrowstyle':'->'})
ax.annotate(r'exit: $\alpha+z^2=1+\beta$',(.6,np.sqrt(1.15)),
            xytext=(-.16,1.81),arrowprops={'arrowstyle':'->'},fontsize=12)
ax.text(-1.25,.65,'incoming\nderivative\nstrip',ha='center',color='#773e08')
ax.text(.62,.56,'positive\ncutoffs',ha='center',color='#165e91')
ax.text(-1.9,2.12,r'outer envelope: $|\alpha|\leq2,\ 0\leq z\leq2$',fontsize=11)
ax.set(xlim=(-2.15,2.12),ylim=(-.1,2.34),xlabel=r'$\alpha=\eta/\delta$',
       ylabel=r'$z=\sqrt{\Omega}/(\epsilon\delta)\geq0$',
       title=r'Exact support projection, $\beta=3/4$')
ax.set_xticks([-1.75,-.75,0,1.75])
ax.tick_params(axis='x',labelsize=10)
ax.grid(alpha=.13)

panel.axis('off')
boxes = [(.79,'Commutant A: order s + 1/2',
          'Original compact weak test A* A u\nFull complex lower form is retained'),
         (.48,'Positive L2 output B: order s + 1',
          'Normalize: W = T B has energy order s\nCharacteristic multiple is −4 Re q₀(u, W* W u)'),
         (.17,'Forcing: natural-dual order s + 1',
          'Left half-order parametrix and minus residual\nLower energy s − 1/2; incoming energy s')]
for y,title,body in boxes:
    panel.text(.04,y,title,fontsize=14,fontweight='bold',color='#16324f',
               bbox={'boxstyle':'round,pad=.55','fc':'#edf3f8','ec':'#b9cddd'},
               transform=panel.transAxes)
    panel.text(.04,y-.09,body,fontsize=11.6,color='#16324f',linespacing=1.6,
               transform=panel.transAxes,va='top')
for y in (.61,.30):
    panel.annotate('',xy=(.93,y-.025),xytext=(.93,y+.025),
                   xycoords='axes fraction',arrowprops={'arrowstyle':'->','color':'#165e91','lw':2})
panel.set_title('Weak estimate preserves the chosen energy domain')
fig.suptitle('Hyperbolic proof mechanism: exact cutoff support and sharp source trade',fontsize=17)
for suffix in ('.png','.svg'):
    fig.savefig(out/('hyperbolic-cutoff-and-weak-estimate'+suffix),dpi=160)
plt.close(fig)
