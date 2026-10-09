from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(13,8.2),facecolor='white')
grid=fig.add_gridspec(2,2,height_ratios=[1.1,1],width_ratios=[1.1,1],
                     left=.065,right=.965,top=.87,bottom=.14,wspace=.18,hspace=.4)
fig.suptitle('A ramified chart retains the central tangent',fontsize=22,fontweight='bold',y=.965)
fig.text(.5,.905,'CS3 constructs one convergent family; CS4 passes coisotropy to its limit.',
         ha='center',fontsize=12,color='#415064')
a=fig.add_subplot(grid[0,0]);a.set(xlim=(0,1),ylim=(0,1));a.axis('off')
box=dict(boxstyle='round,pad=.6',fc='#f0f5fa',ec='#70859b',lw=1.4)
for x,y,t in [(.14,.79,r'$P\times\Delta_u$'),(.83,.79,r'$Y$'),
              (.14,.14,r'$P\times\Delta_t$'),(.83,.14,r'$P\times\Delta_t$')]:
    a.text(x,y,t,ha='center',va='center',bbox=box,fontsize=17)
def arrow(ax,p,q,label,xy):
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=1.8,color='#263b53'))
    ax.text(*xy,label,ha='center',va='center',fontsize=13,
            bbox=dict(facecolor='white',edgecolor='none',pad=3))
arrow(a,(.28,.79),(.75,.79),r'$\phi(z,u)$',(.50,.90))
arrow(a,(.14,.65),(.14,.30),r'$t=u^k$',(.14,.47))
arrow(a,(.83,.65),(.83,.30),r'$F=(z,h)$',(.83,.47))
arrow(a,(.30,.14),(.65,.14),r'$\mathrm{id}$',(.49,.24))
b=fig.add_subplot(grid[0,1]);b.axis('off')
b.text(.02,.92,'The derivatives do not lose rank',fontsize=16,fontweight='bold')
b.text(.02,.68,r'$dz\circ d_z\phi=I_{r-1},\qquad dh\circ d_z\phi=0$',fontsize=17)
b.text(.02,.40,r'$\operatorname{span}(d_z\phi(z,u))$',fontsize=18,color='#205d91')
b.annotate('',xy=(.63,.38),xytext=(.55,.38),
           arrowprops=dict(arrowstyle='->',lw=1.7,color='#263b53'))
b.text(.65,.4,r'$T_{\phi(z,0)}E$',fontsize=18,color='#874117')
b.text(.02,.12,r'As $u\to0$: annihilators converge, so $\Pi(\alpha,\beta)=0$ persists.',
       fontsize=12)
c=fig.add_subplot(grid[1,0])
u=np.linspace(-1,1,501)
c.plot(u[u<0]**2,u[u<0]**3,color='#b55c27',lw=2.8,label=r'$u<0$ (real trace)')
c.plot(u[u>=0]**2,u[u>=0]**3,color='#236ba1',lw=2.8,label=r'$u>0$ (real trace)')
c.axhline(0,color='#a8b2bf',lw=.8);c.axvline(0,color='#a8b2bf',lw=.8)
c.plot([.49,.49],[-.343,.343],color='#8b949f',ls='--',lw=1.2)
c.scatter([.49,.49],[.343,-.343],s=36,c=['#236ba1','#b55c27'],zorder=3)
c.scatter([0],[0],s=42,color='#263b53',zorder=3)
c.annotate('central point',xy=(0,0),xytext=(.16,.03),fontsize=11)
c.set(xlim=(-.08,1.08),ylim=(-1.06,1.06),xlabel=r'$t=u^2$',ylabel=r'$a=u^3$')
c.set_title(r'Example: $Y=\{a^2=t^3\}\times\mathbb{C}_z$',loc='left',fontsize=14,pad=12)
c.spines[['top','right']].set_visible(False);c.legend(loc='upper left',fontsize=10,frameon=False)
d=fig.add_subplot(grid[1,1]);d.axis('off')
d.text(.02,.91,r'$\phi(z,u)=(z,u^3,u^2)$',fontsize=21)
d.text(.02,.68,r'$F(z,a,t)=(z,t)$',fontsize=19)
d.text(.02,.43,r'$d_z\phi=(1,0,0)$ for every $u$',fontsize=18)
d.text(.02,.23,'The z-direction is suppressed in the real cusp plot.\n'
       'The parameter spaces and tangent planes are complex.\n'
       'This example illustrates the chart, not a Poisson tensor.',
       fontsize=11.5,linespacing=1.6,color='#415064',va='top')
fig.text(.065,.035,'Exact proof: CS1–CS4. Original programme diagram, GPT-6 Astra (OpenAI), Ultra · CC0',
         fontsize=10,color='#647184')
fig.savefig(OUT/'casimir-ramified-chart.svg')
fig.savefig(OUT/'casimir-ramified-chart.png',dpi=150)
