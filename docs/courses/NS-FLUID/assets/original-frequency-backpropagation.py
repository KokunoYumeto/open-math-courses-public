"""FB12–FB28: exact time/space nesting and physical dyadic frequency regions."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(ax,bx)=plt.subplots(1,2,figsize=(14,7.4),layout='constrained',gridspec_kw={'width_ratios':[1.1,1]})
t1=4.;N1=2.;D=8.;L=2048.;R=256.
rows=[('Local $L^{3/2}$ norm',t1-D/N1**2,L/N1),
      ('Local $L^1$ norm',t1-D/(2*N1**2),L/(2*N1)),
      ('Local $L^2$ gain',t1-D/(4*N1**2),L/(4*N1))]
for i,(label,left,radius) in enumerate(rows):
 y=3-i
 ax.broken_barh([(left,t1-left)],(y-.15,.3),facecolors='#2d7196')
 ax.text(t1 if i==2 else left,y+.23,f't = {left:g}; ball radius {radius:g}',fontsize=10,ha='right' if i==2 else 'left')
 ax.text(-.1,y,label,ha='right',va='center',fontsize=10)
ax.scatter([t1],[0],color='#b64745',s=50,zorder=4)
ax.text(-.1,0,'Final point',ha='right',va='center',fontsize=10)
ax.annotate(f't = {t1:g}; receiving ball radius {R/N1:g}',(t1,0),xytext=(-4,-28),textcoords='offset points',ha='right',fontsize=10)
ax.axvline(t1-2*D/N1**2,color='#777777',ls=':',label='First Duhamel start')
ax.set(xlim=(-.02,4.15),ylim=(-.8,3.7),yticks=[],xlabel='Original physical time',title='The successive time margins and ball radii')
ax.grid(axis='x',alpha=.2)
ax.text(.04,-.65,'Geometry example: t1 = 4, N1 = 2, D = 8,\nL = 2048, R = 256. Analytic constants are not evaluated.',fontsize=9)
eta_power=-8
bands=[('Absent earlier amplitudes',1+3*eta_power,1-3*eta_power,'#d09b58'),
       ('Local $L^{3/2}$ norm',1+3*eta_power,28,'#9bbccf'),
       ('Local $L^1$ norm',1+3*eta_power+6,28,'#6e9fb9'),
       ('Local $L^2$ gain',1+eta_power,1-eta_power,'#2d7196')]
for i,(name,left,right,col) in enumerate(bands):
 y=3-i
 bx.broken_barh([(left,right-left)],(y-.15,.3),facecolors=col)
 if i in (1,2):bx.annotate('',xy=(29,y),xytext=(26,y),arrowprops={'arrowstyle':'->','color':col,'lw':3})
 bx.text(left,y+.23,name,fontsize=10)
bx.scatter([1],[-1],color='#b64745',s=50)
bx.text(1,-.77,'Original target N1 = 2',ha='center',fontsize=10)
ticks=[-23,-17,-7,1,9,25]
bx.set(xticks=ticks,xticklabels=[r'$2^{-23}$',r'$2^{-17}$',r'$2^{-7}$','2',r'$2^9$',r'$2^{25}$'],
       yticks=[],xlim=(-25,30),ylim=(-1.7,3.7),xlabel='Original frequency (base-two logarithmic axis)',
       title=r'Physical frequency bands for $N_1=2$, $\eta=2^{-8}$')
bx.grid(axis='x',alpha=.2)
bx.text(-23,-1.56,'Arrows retain every higher frequency.\nThe bands display support geometry, not a sampled solution.',fontsize=9)
fig.suptitle('The full backpropagation proof uses three different local norms',fontsize=16)
fig.savefig(ROOT/'original-frequency-backpropagation.png',dpi=170)
fig.savefig(ROOT/'original-frequency-backpropagation.svg')
plt.close(fig)
print('Saved original time/space and frequency geometry.')
