"""Diagram of the marked constraint encoding and its exact left inverse."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':12})
fig, ax = plt.subplots(figsize=(12,6.2))
fig.patch.set_facecolor('#f6fafc'); ax.set_facecolor('#f6fafc')
ax.set_xlim(0,12); ax.set_ylim(0,6.2); ax.axis('off')
ax.text(.4,5.85,'Recovering the entire fluid velocity',fontsize=20,weight='bold',color='#15354b')
ax.text(.4,5.4,'Four-dimensional constraint data with a marked Euclidean plane',fontsize=12,color='#466171')

def box(x,y,heading,formula):
    ax.add_patch(FancyBboxPatch((x,y),2.9,1.05,boxstyle='round,pad=.12',facecolor='white',edgecolor='#8ab8c8',linewidth=1.4))
    ax.text(x+1.45,y+.72,heading,ha='center',weight='bold',fontsize=12,color='#15354b')
    ax.text(x+1.45,y+.28,formula,ha='center',fontsize=13,color='#15354b')
def arrow(x1,y1,x2,y2,label,tx,ty):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':'#147991','lw':2})
    ax.text(tx,ty,label,ha='center',fontsize=11,color='#27566b')

box(.45,3.55,'Original velocity',r'$U(x),\quad \nabla\cdot U=0$')
box(4.55,3.55,'Coordinate pushforward',r'$V(\xi)=d\,U(\xi/d)$')
box(8.65,3.55,'Exact vacuum data',r'$(h,K),\quad \Lambda=-6/L^2$')
arrow(3.48,4.05,4.37,4.05,r'$\mathcal{P}_d$',3.92,4.4)
arrow(7.57,4.05,8.48,4.05,'TT lift +\nscalar solve',8.02,4.85)
box(.45,1.4,'Returned velocity',r'$d^{-1}V(dx)=U(x)$')
box(4.55,1.4,'Newton recovery',r'$V=2\Delta^{-1}\mathrm{div}\,S_V$')
box(8.65,1.4,'Strain at w = 0',r'$S_V=\beta_*^{-1}\phi^4\mathrm{TF}_E K^\sharp$')
arrow(10.1,3.4,10.1,2.6,'read at\n'+r'$w=0$',11.4,2.85)
arrow(8.48,1.92,7.57,1.92,r'$\mathcal{N}$',8.02,2.25)
arrow(4.38,1.92,3.48,1.92,r'$\mathcal{P}_d^{-1}$',3.92,2.25)
ax.text(.55,.66,r'$dV_h/dV_\delta=\phi^4$'+' is part of the decoder; the metric alone does not retain the velocity sign.',fontsize=11,color='#466171')
ax.text(.55,.22,r'$\mathcal{D}_{b,d}\mathcal{E}_{b,d}U=U$'+'  ·  Lesson V6a, equations (C12), (C17), (C29), (C37)–(C42)',fontsize=11,color='#466171')
fig.savefig(Path(__file__).with_suffix('.svg'),bbox_inches='tight',pad_inches=.15)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=150,bbox_inches='tight',pad_inches=.15)
plt.close(fig)
