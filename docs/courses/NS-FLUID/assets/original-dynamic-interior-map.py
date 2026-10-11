"""Exact sample snapshot of the original period-two interior-cylinder map."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,ConnectionPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,10),facecolor='#f7f9fc')
gs=fig.add_gridspec(2,2,height_ratios=[1,0.86],hspace=.30,wspace=.28)
ax=fig.add_subplot(gs[0,0]);bx=fig.add_subplot(gs[0,1]);cx=fig.add_subplot(gs[1,:]);cx.axis('off')
fig.suptitle('The entire interior cylinder keeps its axis and its moving period',fontsize=20,x=.5,y=.965)
fig.text(.5,.915,r'Exact snapshot: $b=\frac{1}{2}$;  $z=by_1$,  $r=R=1-by_2$.  Dynamic clock: $dt/d\sigma=a>0$.',ha='center',fontsize=14)
ax.add_patch(Rectangle((-1,0),2,1,facecolor='#dfeaf5',edgecolor='none'))
ax.add_patch(Rectangle((-1,.75),2,.25,facecolor='#c4e5d7',edgecolor='none'))
ax.plot([-1,1],[1,1],color='#176c55',lw=3);ax.plot([-1,1],[0,0],color='#70429b',lw=3)
for z in [-1,1]:ax.plot([z,z],[0,1],color='#24649b',lw=2,ls='--')
ax.set(xlim=(-1.2,1.2),ylim=(-.13,1.16),xlabel=r'Original axial coordinate $z$',ylabel=r'Original radius $r$',
       xticks=[-1,0,1],yticks=[0,.5,1])
ax.set_title('Physical meridional period',pad=16,fontsize=15)
ax.text(0,1.035,r'Wall $r=1$: $u_r=0$',ha='center',color='#176c55')
ax.text(0,-.09,r'Axis $r=0$: Cartesian smoothness',ha='center',color='#70429b',fontsize=11)
ax.annotate('',xy=(.3,.33),xytext=(.3,.65),arrowprops=dict(arrowstyle='->',color='#b44823',lw=2))
ax.text(.4,.47,r'$-u_r$',color='#b44823')
ax.text(0,.84,r'$3/4\leq r\leq1$',ha='center',color='#176c55')
ax.text(0,.1,r'$z=-1\ \sim\ z=1$',ha='center',color='#24649b')
bx.add_patch(Rectangle((-2,0),4,2,facecolor='#dfeaf5',edgecolor='none'))
bx.add_patch(Rectangle((-2,0),4,.5,facecolor='#c4e5d7',edgecolor='none'))
bx.plot([-2,2],[0,0],color='#176c55',lw=3);bx.plot([-2,2],[2,2],color='#70429b',lw=3)
for x in [-2,2]:bx.plot([x,x],[0,2],color='#24649b',lw=2,ls='--')
bx.set(xlim=(-2.4,2.4),ylim=(2.26,-.32),xlabel=r'Profile axial coordinate $y_1=z/b$',ylabel=r'Inward coordinate $y_2=(1-r)/b$',
       xticks=[-2,0,2],yticks=[0,1,2])
bx.set_title('Profile period: exact height and endpoint identification',pad=16,fontsize=14)
bx.text(0,-.11,r'Wall $y_2=0$: $U_2=0$',ha='center',color='#176c55')
bx.text(0,2.18,r'Axis $y_2=1/b=2$',ha='center',color='#70429b',fontsize=11)
bx.annotate('',xy=(.6,1.34),xytext=(.6,.7),arrowprops=dict(arrowstyle='->',color='#b44823',lw=2))
bx.text(.8,1,r'$U_2=-au_r/b$',color='#b44823',fontsize=11)
bx.text(0,.29,r'$0\leq y_2\leq1/2$',ha='center',color='#176c55')
bx.text(0,1.8,r'$y_1=-1/b\ \sim\ y_1=1/b$',ha='center',color='#24649b')
for p in [ax,bx]:
 p.spines[['top','right']].set_visible(False);p.grid(alpha=.12)
cx.add_patch(Rectangle((0,0),1,1,transform=cx.transAxes,facecolor='white',edgecolor='#c9d5e2',lw=1))
lines=[
(r'$U=\frac{a}{b}(u_z,-u_r),\quad W=\frac{a}{\sqrt{b}}ru_\vartheta,\quad \Theta=W^2,\quad \Pi=\frac{a^2}{b^2}P$',16),
(r'$\Omega=a\omega_\vartheta=\partial_{y_2}U_1-\partial_{y_1}U_2=RQ,\qquad Q=a\omega_\vartheta/r$',16),
(r'$\mathcal{D}\Omega=c_\omega\Omega+R^{-3}\Phi-bU_2\Omega/R,\qquad \mathcal{D}Q=c_\omega Q+R^{-4}\Phi$',16),
(r'$\operatorname{div}_yU=bU_2/R,\qquad \phi=a\varphi^\vartheta/b^2,\qquad \psi=R\phi$',16),
(r'$\mathcal{D}=\partial_\sigma+(c_l y+U)\cdot\nabla_y,\quad \Phi=\partial_{y_1}\Theta,\quad R=1-by_2$',14),
]
for yy,(txt,size) in zip([.84,.65,.46,.27,.08],lines):cx.text(.5,yy,txt,ha='center',va='center',fontsize=size)
fig.text(.065,.027,'Proof: DR15–DR30, DR36–DR41. The green strips are exact corresponding subsets at the stated sample scale.',fontsize=11)
fig.text(.065,.008,'Source: Chen–Hou, arXiv:2210.07191v4, original author TeX 10167–10285. This is a coordinate diagram, not a singular flow.',fontsize=10)
fig.subplots_adjust(top=.855,bottom=.075,left=.075,right=.96)
for ext in ['png','svg']:fig.savefig(R/('original-dynamic-interior-map.'+ext),dpi=170,facecolor=fig.get_facecolor())

