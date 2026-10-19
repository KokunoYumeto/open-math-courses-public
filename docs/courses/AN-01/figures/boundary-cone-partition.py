"""Original figure for AN01-U079; CC0. Requires numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN01-U079'})
fig,axes=plt.subplots(1,2,figsize=(12,6),layout='constrained')
colors=['#226aab','#9c3f8e','#338564']
for ax in axes:
 ax.set_aspect('equal');ax.set_xlim(-1.5,1.5);ax.set_ylim(-1.45,1.5)
 ax.axhline(0,color='#a5abb3',lw=.7);ax.axvline(0,color='#a5abb3',lw=.7)
 ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax=axes[0];ax.set_title('One direction, one opposite boundary point',pad=16)
disk=Circle((0,0),1,facecolor='#edf4fa',edgecolor='#226aab',lw=1.7);ax.add_patch(disk)
theta=np.array([.6,.8]);p=-theta
cap=Circle(p,.30,facecolor='#f4b66a',alpha=.75,edgecolor='none');cap.set_clip_path(disk);ax.add_patch(cap)
ax.annotate('',theta,(0,0),arrowprops=dict(arrowstyle='->',color='#226aab',lw=2.5,linestyle='--'))
ax.plot(*p,'o',color='#a14c00',ms=7)
ax.annotate(r'$\theta=(3/5,4/5)$',theta,xytext=(.05,1.17),arrowprops=dict(arrowstyle='-',color='#226aab'),fontsize=12)
ax.annotate(r'$-\theta=(-3/5,-4/5)$',p,xytext=(-1.4,-1.3),arrowprops=dict(arrowstyle='-',color='#a14c00'),fontsize=12)
ax.text(-.85,.58,r'$|y|<1$',color='#226aab');ax.set_xlabel(r'Imaginary coordinate $y_1$ (covector overlaid)');ax.set_ylabel(r'$y_2$')
ax=axes[1];ax.set_title('Closed cover and first-membership partition',pad=16)
for j,center in enumerate([0,120,240]):
 ax.add_patch(Wedge((0,0),.94,center-75,center+75,facecolor=colors[j],alpha=.18,edgecolor=colors[j],lw=1.2))
 t=np.deg2rad(center);ax.plot([0,.9*np.cos(t)],[0,.9*np.sin(t)],color=colors[j],lw=1.8)
 ax.text(.64*np.cos(t),.64*np.sin(t)+.07,r'$\Gamma_'+str(j+1)+'$',ha='center',color=colors[j])
for lo,hi,j in [(-75,75,0),(75,195,1),(195,285,2)]:
 t=np.deg2rad(np.linspace(lo,hi,350));ax.plot(1.12*np.cos(t),1.12*np.sin(t),color=colors[j],lw=8,solid_capstyle='butt')
 mid=np.deg2rad((lo+hi)/2);ax.text(1.35*np.cos(mid),1.35*np.sin(mid),r'$E_'+str(j+1)+'$',ha='center',va='center',color=colors[j])
 # Endpoint membership is shown on separated radii so both adjacent limits remain visible.
 for angle,closed in [(lo,j==0),(hi,j!=2)]:
  t=np.deg2rad(angle);rad=1.12+(j-1)*.035
  ax.plot(rad*np.cos(t),rad*np.sin(t),'o',ms=6,mec=colors[j],mfc=colors[j] if closed else 'white',mew=1.6,zorder=10)
ax.set_xlabel(r'Covector directions; half-width $5\pi/12$');ax.set_ylabel(r'$\xi_2$')
fig.suptitle('Boundary regularity and finite conic decomposition',fontsize=17)
out=Path(__file__).resolve().parent
fig.savefig(out/'boundary-cone-partition.png',dpi=180)
fig.savefig(out/'boundary-cone-partition.svg',metadata={'Date':None,'Creator':'Original AN01-U079 figure; CC0'})
p=out/'boundary-cone-partition.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
