"""Reproducible original diagram of CP.30--CP.34 and CP.50--CP.51."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
 'svg.hashsalt':'complex-propagation-CP50','axes.spines.top':False,'axes.spines.right':False})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(8,12.5),constrained_layout=True)
ax=axes[0]
theta=np.linspace(0,np.pi/2,401)
a=1-np.cos(theta);b=2-np.sin(theta)
points=[(-.35,-.1),(2.3,-.1),(2.3,1),*(zip(a[::-1],b[::-1])),(0,2.65),(-.35,2.65)]
ax.add_patch(Polygon(points,facecolor='#dfecf5',edgecolor='none'))
ax.plot([0,0],[2,2.65],color='#234f75',lw=2)
ax.plot(a,b,color='#234f75',lw=2)
ax.plot([1,2.3],[1,1],color='#234f75',lw=2)
ax.plot([1],[2],'o',color='#718096',ms=4)
ax.plot([0,1],[2,1],'o',color='#234f75',ms=5)
ax.annotate('outward',xy=(.33,2),xytext=(.55,2.25),arrowprops={'arrowstyle':'->'})
ax.arrow(0,2,.3,0,head_width=.055,length_includes_head=True,color='#c65335')
ax.arrow(1,1,0,.3,head_width=.055,length_includes_head=True,color='#c65335')
ax.text(1.07,2.08,'centre (1, 2)',fontsize=14)
ax.text(.25,.35,r'$U_\epsilon$ (scaled)',fontsize=16)
ax.text(.2,2.5,'excluded side',color='#6b7280')
ax.set(xlim=(-.35,2.3),ylim=(-.1,2.65),xlabel=r'$a/\epsilon$',ylabel=r'$b/\epsilon$',
 title='The rounded quadrant: exact joins')
ax.set_aspect('equal');ax.grid(alpha=.15)
ax=axes[1]
xx=np.linspace(0,1.25,501);yy=np.linspace(-.66,.66,501)
x,y=np.meshgrid(xx,yy);cone=x>2*np.abs(y)
ax.fill_between(xx,-xx/2,xx/2,color='#edf0f4')
for e,color,label in [(1/80,'#88bccc','1/80'),(1/40,'#488ca5','1/40'),(1/20,'#164f78','1/20')]:
 qx=x-16*e
 d=np.maximum(0,qx*qx+y*y-np.maximum.reduce([np.zeros_like(x),2*qx+y,2*qx-y])**2/5)
 d=np.where(qx>=2*np.abs(y),0,d)
 a=1-x
 cutoff=np.where(a<0,np.inf,np.where(a>=e,e,2*e-np.sqrt(np.maximum(0,2*e*a-a*a))))
 inside=cone & (np.sqrt(d)<cutoff)
 ax.contourf(x,y,inside.astype(float),levels=[.5,1.5],colors=[color],alpha=.45)
 ax.contour(x,y,inside.astype(float),levels=[.5],colors=[color],linewidths=1)
 ax.plot([],[],color=color,lw=3,label=r'$\epsilon='+label+'$')
ax.plot(xx,xx/2,color='#1f2937',lw=1.4);ax.plot(xx,-xx/2,color='#1f2937',lw=1.4)
ax.axvline(1,color='#374151',ls='--',lw=1)
ax.text(1.015,.48,r'$\ell=1$',fontsize=14)
ax.annotate(r'$v=(1,0)$',xy=(.4,-.52),xytext=(.08,-.52),arrowprops={'arrowstyle':'->'})
ax.set(xlim=(0,1.25),ylim=(-.66,.66),xlabel=r'$X=-\operatorname{Re}t$',ylabel=r'$Y=\operatorname{Im}t$',
 title=r'$K:\ X\geq2|Y|$, $1-s=16\epsilon$')
ax.legend(loc='upper left',fontsize=14);ax.set_aspect('equal');ax.grid(alpha=.15)
fig.suptitle('Rounded noncharacteristic fronts',fontsize=20)
fig.savefig(out/'complex-propagation.png',dpi=170,metadata={'Software':'Original mathematical course diagram'})
fig.savefig(out/'complex-propagation.svg',metadata={'Date':None,'Creator':'Original mathematical course diagram'})
plt.close(fig)
data={'coordinates':{'X':'-Re(t)','Y':'Im(t)'},
 'cone':'X >= 2 |Y|','linear_function':'ell(X,Y)=X','interior_vector':[1,0],
 'interior_radius':'1/sqrt(5)','exhaustion_constant':16,
 'epsilons':['1/20','1/40','1/80'],'translation':'(16 epsilon,0)',
 'rounded_boundary':{'centre_scaled':[1,2],'radius_scaled':1,
                     'joins_scaled':[[0,2],[1,1]]},
 'squared_distance_outside_cone':'qx^2+qy^2-max(0,2qx+qy,2qx-qy)^2/5',
 'plot_grid':{'X':[0,1.25,501],'Y':[-.66,.66,501]},
 'proof_locators':['CP.28--CP.34','CP.50--CP.51'],
 'sources':['https://perso.imj-prg.fr/pierre-schapira/wp-content/uploads/schapira-pub/Microhyp.pdf',
            'https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf']}
(out/'complex-propagation-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
