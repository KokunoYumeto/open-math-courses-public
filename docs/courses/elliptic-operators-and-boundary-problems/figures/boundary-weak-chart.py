"""Draw the exact two-dimensional weak boundary chart in BR1--BR3 and BR7."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
HERE=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,7.5),facecolor='#fffdf8')
gs=GridSpec(1,3,width_ratios=[1,1,1.35],left=.055,right=.975,bottom=.21,top=.76,wspace=.32)
flat=fig.add_subplot(gs[0,0]);curved=fig.add_subplot(gs[0,1]);text=fig.add_subplot(gs[0,2])
for ax in [flat,curved]:
 ax.set_facecolor('#fffdf8');ax.spines[['top','right']].set_visible(False)
 ax.set_xlabel(r'$z$',fontsize=14);ax.tick_params(labelsize=11)
flat.set_xlim(-1.12,1.12);flat.set_ylim(-.15,2.2);flat.set_ylabel(r'$t$',fontsize=14)
curved.set_xlim(-1.12,1.12);curved.set_ylim(-1.25,3.25);curved.set_ylabel(r'$x_2$',fontsize=14)
flat.fill_between([-1.1,1.1],0,2.2,color='#e7f0e9')
z=np.linspace(-1,1,801);h=z*np.abs(z)
curved.fill_between(z,h,3.25,color='#e7f0e9')
for level in [0,.5,1,1.5,2]:
 flat.plot(z,np.full_like(z,level),color='#839daf',lw=1)
 curved.plot(z,level+h,color='#839daf',lw=1)
for point in [-1,-.5,0,.5,1]:
 flat.plot([point,point],[0,2],color='#839daf',lw=1)
 curved.plot([point,point],[point*abs(point),2+point*abs(point)],color='#839daf',lw=1)
flat.axhline(0,color='#315f78',lw=2.8)
for interval in [np.linspace(-1,0,401),np.linspace(0,1,401)]:
 curved.plot(interval,interval*np.abs(interval),color='#315f78',lw=2.8)
curved.plot([0],[0],'o',color='#ad613e',ms=6)
flat.set_title('Half-space coordinates',fontsize=14,pad=14)
curved.set_title('The same grid after F',fontsize=14,pad=14)
flat.text(0,1.72,r'$t>0$',ha='center',fontsize=15,color='#315f78')
curved.text(-.83,2.6,r'$x_2>h(z)$',fontsize=14,color='#315f78')
curved.annotate('No classical second\nderivative at zero',xy=(0,0),xytext=(-.96,-.91),
 fontsize=10.5,color='#885033',arrowprops=dict(arrowstyle='->',color='#ad613e'))
text.axis('off')
labels=[
 (.98,'The entire transformed operator',15,'#173750'),
 (.85,r'$h(z)=z|z|,\quad h^\prime(z)=2|z|$',14,'#173750'),
 (.73,r'$h^{\prime\prime}(z)=2\,\operatorname{sgn}z\quad\mathrm{a.e.}$',14,'#173750'),
 (.61,r'$A_{11}=1,\quad A_{12}=A_{21}=-2|z|$',13,'#173750'),
 (.52,r'$A_{22}=1+4z^2$',13,'#173750'),
 (.44,r'$\det A=1$',14,'#173750'),
 (.34,r'$\xi^T A\xi=(\xi_z-2|z|\xi_t)^2+\xi_t^2$',13,'#173750'),
 (.18,'Lipschitz leading coefficients;\nbounded weak first-order coefficient.',12,'#405163'),
 (.04,r'$u\in H^1,\ \gamma u=0,\ Pu=f\in L^2$'+'\n'+
       r'$\Longrightarrow\ H^2\ \mathrm{locally\ up\ to\ the\ wall}$',12,'#173750')
]
for y,label,size,color in labels:text.text(0,y,label,transform=text.transAxes,va='top',fontsize=size,color=color,linespacing=1.5)
fig.text(.5,.94,r'A $C^{1,1}$ boundary chart retains the full weak equation',ha='center',fontsize=22,color='#173750',weight='bold')
fig.text(.5,.855,r'$F(z,t)=(z,t+z|z|),\qquad F^{-1}(x)=(x_1,x_2-x_1|x_1|),\qquad\det DF=1$',ha='center',fontsize=17,color='#315f78')
fig.text(.5,.135,r'$-\partial_z^2+4|z|\partial_z\partial_t-(1+4z^2)\partial_t^2+2\operatorname{sgn}z\,\partial_t'
 '=-\\operatorname{div}(A\\nabla)$',ha='center',fontsize=15,color='#173750')
fig.text(.5,.075,'Grid curves are samples of the exact map F. The value of the weak second derivative at zero does not affect the operator.',ha='center',fontsize=11,color='#405163')
fig.text(.5,.029,'Proof: Section 8, BR1--BR3, BR7 and B29.',ha='center',fontsize=11,color='#405163')
for suffix in ['svg','png']:fig.savefig(HERE/f'boundary-weak-chart.{suffix}',dpi=170,facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered boundary-weak-chart.svg and boundary-weak-chart.png')
