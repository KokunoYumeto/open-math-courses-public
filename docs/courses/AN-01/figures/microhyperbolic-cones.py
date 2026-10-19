"""Exact sections for AN01-U093, Theorem 7 and Proposition 8. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.titlesize':15,'axes.labelsize':13,'svg.fonttype':'none'})
fig,ax=plt.subplots(1,2,figsize=(12.5,5.6))
blue='#136a91';green='#31936e';orange='#b65a1d';ink='#172334'
fig.patch.set_facecolor('#f8fafc')
for a in ax:
 a.set_facecolor('#f8fafc');a.set_aspect('equal');a.spines[['top','right']].set_visible(False)
 a.grid(alpha=.15);a.set_axisbelow(True)

a=ax[0]
a.add_patch(Polygon([(-2.1,2.1),(0,0),(2.1,2.1)],closed=True,facecolor=blue,alpha=.15,edgecolor='none'))
a.plot([-2.1,0,2.1],[2.1,0,2.1],color=blue,ls='--',lw=2)
a.annotate('',(0,1),(0,0),arrowprops={'arrowstyle':'->','lw':2.5,'color':ink})
a.plot(0,1,'o',color=ink,ms=5)
a.text(.12,1.03,r'$e$',color=ink,fontsize=15)
a.text(-.65,1.65,r'$y_0>|y_1|$',color=blue,fontsize=15)
a.text(.5,1.01,r'Section $y_2=y_3=0$',transform=a.transAxes,ha='center',fontsize=11)
a.set(xlim=(-2.2,2.2),ylim=(-.65,2.25),xlabel=r'$y_1$',ylabel=r'$y_0$')
a.set_title('Imaginary approach cone',pad=14)
a.text(.03,.04,'Dashed boundary excluded',transform=a.transAxes,color=blue,fontsize=11)

a=ax[1]
a.add_patch(Circle((0,0),1,facecolor=green,alpha=.16,edgecolor='none'))
t=np.linspace(0,2*np.pi,721)
a.plot(np.cos(t),np.sin(t),color=orange,lw=3,label='Actual wavefront section')
a.plot([-1,1],[0,0],'o',color=orange,ms=7)
a.plot(0,0,'o',color=ink,ms=6)
a.annotate('Midpoint: in convex bound\nbut outside the wavefront',(0,0),(-.95,-.68),
           arrowprops={'arrowstyle':'->','color':ink},fontsize=9.5,color=ink)
a.text(-.60,.44,r'$\xi_1^2+\xi_2^2\leq1$',fontsize=14,color=green)
a.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel=r'$\xi_1$',ylabel=r'$\xi_2$')
a.set_title('Vertex covectors in four dimensions',pad=14)
a.text(.5,1.01,r'Section $\xi_0=1,\ \xi_3=0$',transform=a.transAxes,ha='center',fontsize=11)
a.legend(loc='upper center',bbox_to_anchor=(.5,-.17),frameon=False,fontsize=10)
fig.suptitle('A convex bound can contain directions absent from the wavefront',fontsize=16,y=.98,color=ink)
fig.subplots_adjust(top=.80,bottom=.20,left=.07,right=.97,wspace=.28)
fig.savefig(out/'microhyperbolic-cones.svg',bbox_inches='tight')
svg_path=out/'microhyperbolic-cones.svg'
svg_path.write_bytes(('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
fig.savefig(out/'microhyperbolic-cones.png',dpi=160,bbox_inches='tight')
plt.close(fig)
