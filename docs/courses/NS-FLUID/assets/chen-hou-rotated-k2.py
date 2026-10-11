"""Original physical coordinates and exact proved bounds, RV1–RV22."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

P=Path(__file__).resolve()
a=13/10; c=7/10; M=12/5; R=6
plt.rcParams.update({'font.size':11, 'axes.titlesize':13, 'axes.labelsize':11})
fig,axs=plt.subplots(2,2,figsize=(14,10),layout='constrained')
blue='#176c9c'; red='#b24b35'; green='#21785c'; purple='#7353a6'
ax=axs[0,0]
ax.axhspan(0,5,color='#e9f4f7');ax.axhspan(-.8,0,color='#f5e6e3')
ax.axhline(0,color='black',lw=1)
ax.plot([c,c],[M-a,M+a],color=blue,lw=2)
ax.scatter([c,c],[M-a,M+a],color=[blue,red],s=60,zorder=3)
ax.scatter([c],[M],color='black',s=25)
ax.annotate(r'$x=(c,M-a)=(0.7,1.1)$',(c,M-a),xytext=(.95,.9))
ax.annotate(r'$z=(c,M+a)=(0.7,3.7)$',(c,M+a),xytext=(.95,3.75))
ax.text(-1.6,2.4,r'$|z-x|=2a=2.6$',color=blue)
ax.text(-1.6,4.55,r'$y=(c+t,M-s),\quad \det=1$')
ax.text(-1.6,-.48,'Odd extension below the physical boundary')
ax.annotate('',xy=(c+.65,M),xytext=(c,M),arrowprops={'arrowstyle':'->','color':green})
ax.text(c+.4,M+.15,r'$+t$',color=green)
ax.annotate('',xy=(c,M-.6),xytext=(c,M),arrowprops={'arrowstyle':'->','color':purple})
ax.text(c+.1,M-.48,r'$+s$',color=purple)
ax.set(xlim=(-1.8,4.1),ylim=(-.8,5),xlabel='Original horizontal coordinate',ylabel='Original height',
       title='Physical pair and exact displacement map  ·  RV1–RV2')
ax.set_aspect('equal',adjustable='box')

ax=axs[0,1]
ax.add_patch(Rectangle((-R+a,-R),2*(R-a),2*R,color='#e0eee7'))
ax.add_patch(Rectangle((-R-a,-R),2*a,2*R,color='#e7dff2'))
ax.add_patch(Rectangle((R-a,-R),2*a,2*R,color='#f5dcd4'))
ax.add_patch(Rectangle((-a-R,-R),2*R,2*R,fill=False,ec=blue,lw=2))
ax.add_patch(Rectangle((a-R,-R),2*R,2*R,fill=False,ec=red,lw=2,ls='--'))
ax.scatter([-a,a],[0,0],c=[red,blue],s=35,zorder=4)
for v in [-a,a]:ax.add_patch(Circle((v,0),.32,fill=False,ec='black',lw=1))
ax.text(0,3.6,'Both kernels in the core',ha='center')
ax.text(0,2.3,r'$|s|\leq R-a,\quad |t|\leq R$',ha='center')
ax.text(-R,-4.6,'One kernel',ha='center',rotation=90)
ax.text(R,-4.6,'One kernel',ha='center',rotation=90)
ax.text(0,-4.8,r'Band area $8aR$; density $\leq 2/R^2$',ha='center')
ax.text(-a,-.9,r'$-a$',ha='center');ax.text(a,-.9,r'$a$',ha='center')
ax.set(xlim=(-R-a-.5,R+a+.5),ylim=(-R-.6,R+.6),xlabel=r'$s$',ylabel=r'$t$',
       title='Both original square cutoffs, R = 6  ·  RV5')
ax.set_aspect('equal',adjustable='box')

ax=axs[1,0];ax.axis('off')
ax.set_title('Exact local corrections  ·  RV6–RV9',pad=12)
rows=[
 [r'$S_{\rm in}$',r'$I_{\rm in}-\pi d_\eta/4$'],
 [r'$S_{\rm mid}$',r'$I_{\rm mid}-\pi d_\eta/4$'],
 [r'$S_{\rm mid}+S_{\rm out}$',r'$J_{\rm rest}+\pi d_\eta/4$'],
 [r'$\mathscr{D}_u$',r'$-(I_{\rm in}+I_{\rm mid}+S_{\rm out})/\pi$'],
 [r'$\mathscr{D}_v$',r'$-(I_{\rm in}+J_{\rm rest})/\pi+d_\eta/2$'],
]
table=ax.table(cellText=rows,colLabels=['Original quantity','Complete signed formula'],
               loc='center',colWidths=[.30,.70],bbox=[0,.23,1,.67],cellLoc='center')
table.auto_set_font_size(False);table.set_fontsize(12)
for (i,j),cell in table.get_celld().items():
 cell.set_edgecolor('#c6d2dc');cell.set_facecolor('#dce9f1' if i==0 else '#f8fafc')
ax.text(.5,.13,r'$d_\eta=\omega(x)-\omega(z),\qquad M>a>0$',ha='center',transform=ax.transAxes)
ax.text(.5,.02,'Radial principal values and coordinate strips retain their distinct terms.',
        ha='center',transform=ax.transAxes,fontsize=10)

ax=axs[1,1]
ms=np.linspace(a,a+3,401)
lower=np.pi/2*np.sqrt(2*a)*np.ones_like(ms)
upper=np.pi/2*np.sqrt(2*ms)+4*np.sqrt(ms-a)*(np.pi/2-np.pi/(2*np.sqrt(2)))
old=upper+(ms-a)**2/(4*a*a)*np.sqrt(2*ms)
ax.fill_between(ms,lower,upper,color='#e5f1e9',label='Proved enclosure of the full cost')
ax.plot(ms,old,color=red,ls='--',label='Complete source upper coefficient')
ax.plot(ms,upper,color=green,lw=2,label='Stronger upper bound, RV17')
ax.plot(ms,lower,color=blue,lw=1.5,label='Lower bound from the residual mass')
ax.scatter([a],[lower[0]],facecolors='white',edgecolors=blue,s=65,zorder=5)
ax.scatter([a],[0],color='black',s=40,zorder=5)
ax.annotate(r'Literal $M=a$: cost $0$',(a,0),xytext=(a+.3,.4),fontsize=10)
ax.annotate(r'Limit: $\pi\sqrt{2a}/2$',(a,lower[0]),xytext=(a+.25,lower[0]+.6),fontsize=10,
            arrowprops={'arrowstyle':'->','color':blue})
ax.set(xlim=(a-.1,a+3.05),ylim=(-.35,old[-1]+.6),xlabel=r'Original midpoint height $M$',
       ylabel=r'Cost coefficient, $a=13/10$',title='Complete middle-cost bounds  ·  RV17–RV18')
ax.legend(loc='upper left',fontsize=8.5)
ax.grid(alpha=.18)
fig.suptitle('Original vertical velocity increments: geometry, signs and retained boundary mass',fontsize=16)
for ext in ['png','svg']:fig.savefig(P.with_suffix('.'+ext),dpi=160)
plt.close(fig)
meta=dict(at=datetime.now(timezone.utc).isoformat(),source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),
          parameters=dict(a=a,c=c,M=M,R=R),locators='RV1–RV22; KX13–KX14; PV3',
          scope='Exact proof formulas sampled for illustration; curves are bounds, not evaluated integral values.',
          human_sources=['Chen–Hou Part I arXiv:2210.07191v4','Chen–Hou Part II arXiv:2305.05660v3'],
          visual_inspection='pending')
P.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figure':str(P.with_suffix('.png'))}))
