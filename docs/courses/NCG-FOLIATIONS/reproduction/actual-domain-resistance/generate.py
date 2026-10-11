# BEGIN LG_FIGURE_SOURCE
import base64, io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams['svg.fonttype']='none'
plt.rcParams['svg.hashsalt']='ncg-actual-domain-normal-20261010'
from matplotlib.patches import Circle, FancyArrowPatch

fig = plt.figure(figsize=(15, 5.8), facecolor='white')
gs = fig.add_gridspec(1, 3, width_ratios=(1.4, 1, 1.25))
ax = fig.add_subplot(gs[0, 0])
ax.set_aspect('equal')
ax.set_xlim(-3.25, 3.25); ax.set_ylim(-2.75, 2.75)
ax.axis('off')
for cx, name in ((-1.65, 'negative sheet'), (1.65, 'positive sheet')):
    ax.add_patch(Circle((cx, .45), 1.38, facecolor='#e4f2e7', edgecolor='#183d31', lw=1.5))
    ax.add_patch(Circle((cx, .45), .92, facecolor='#f3efdf', edgecolor='#877440', lw=.8))
    ax.add_patch(Circle((cx, .45), .46, facecolor='#e7eafa', edgecolor='#56639a', lw=.8))
    ax.text(cx, 2.02, name, ha='center', fontsize=12)
    ax.text(cx, .65, 'k = 0', ha='center', fontsize=11)
    ax.text(cx, -.70, 'k = 3', ha='center', fontsize=11)
    ax.plot(cx, .45, 'o', markerfacecolor='white', markeredgecolor='#a33231', ms=7, mew=1.6)
    ax.plot(cx+.19, .45, 'o', color='#183d31', ms=4)
ax.add_patch(FancyArrowPatch((-1.46, .45), (1.84, .45), arrowstyle='->',
    mutation_scale=14, lw=1.4, color='#183d31', connectionstyle='arc3,rad=-.40'))
ax.text(0, 1.12, 'actual cross arrow at z != 0', ha='center', fontsize=10)
ax.text(0, -1.23, 'cross arrow at z = 0 is absent', ha='center', fontsize=11, color='#a33231')
ax.text(0, -1.64, 'original q = 2; r < 3; metric incomplete', ha='center', fontsize=10)
ax.text(0, -2.02, 'interpolation 1 < r < 2: rank unspecified', ha='center', fontsize=10)
ax.text(0, -2.42, 'LG.3-LG.6: module fibre is zero along escaping arrows',
    ha='center', fontsize=9)
ax.set_title('Original geometry and actual domains', fontsize=13, pad=15)

ax2 = fig.add_subplot(gs[0, 1])
ax2.set_aspect('equal'); ax2.set_xlim(-.3, 2.3); ax2.set_ylim(-1.55, 2.2); ax2.axis('off')
points = {1:(0, 0), 2:(2, 0), 3:(1, 1.7)}
for a, b, col, label, xy in ((1,2,'#183d31','c12 = 1',(1,-.25)),
        (1,3,'#ae5737','c13 = a(t)',(.13,1.02)),
        (2,3,'#ae5737','c23 = a(t)',(1.87,1.02))):
    p,q = points[a],points[b]
    ax2.plot((p[0],q[0]),(p[1],q[1]),color=col,lw=2.3)
    ax2.text(*xy,label,ha='center',fontsize=10,
        bbox=dict(facecolor='white',edgecolor='none',pad=1))
for number, p in points.items():
    ax2.plot(*p,'o',color='#263c68',ms=13)
    ax2.text(p[0],p[1]+.19,str(number),ha='center',fontsize=12)
ax2.text(1,-.66,'a(t) = t+^2 / (1 + t+^2)',ha='center',fontsize=11)
ax2.text(1,-1.00,'t <= 0: class {1,2}; class {3}',ha='center',fontsize=10)
ax2.text(1,-1.34,'cut conductance -> 0 gives resistance -> infinity',ha='center',fontsize=9)
ax2.set_title('One actual class split: LG.23',fontsize=13,pad=15)

ax3 = fig.add_subplot(gs[0, 2])
t = np.geomspace(.01, 2, 600)
a = t*t/(1+t*t)
r12 = 2/(2+a)
r13 = (1+a)/(a*(2+a))
ax3.loglog(t,r13,color='#ae5737',lw=2,label='R13 = R23: disappearing arrows')
ax3.loglog(t,r12,color='#183d31',lw=2,label='R12: persistent arrow')
ax3.loglog(t,.5/t**2,ls='--',color='#8d8d8d',lw=1,label='1 / (2 t^2): asymptotic')
ax3.set_xlabel('t > 0 (original arrow domain)')
ax3.set_ylabel('effective resistance = squared Hilbert distance')
ax3.grid(True,which='both',alpha=.20)
ax3.legend(fontsize=8,loc='upper right',framealpha=1)
ax3.set_title('Exact formulas; numerical plot',fontsize=13,pad=15)
fig.suptitle('Domain-sensitive CND kernels retain every original admitted arrow',fontsize=16,y=.995)
fig.subplots_adjust(left=.025,right=.985,bottom=.16,top=.83,wspace=.30)
fig.text(.5,.055,'LG.13 proves CND. LG.15 proves the cut bound. LG.18 makes the increment cost independent of every actual multiplier.',
    ha='center',fontsize=11)
fig.text(.5,.017,'Infinite recurrent fibres require a separate label feature: the inverse-Laplacian feature on Z^3 is bounded (LG.24).',
    ha='center',fontsize=10,color='#7d4030')
fig.savefig(Path(__file__).resolve().parents[2]/'figures'/'actual-domain-resistance.svg',format='svg',metadata={'Date':None})
buf = io.BytesIO()
fig.savefig(buf,format='png',dpi=140,facecolor='white')
plt.close(fig)
(Path(__file__).resolve().parents[2]/'figures'/'actual-domain-resistance.png').write_bytes(buf.getvalue())
# END LG_FIGURE_SOURCE
