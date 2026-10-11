"""Exact counterexample geometry and a labelled sample of the proved primitive map."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.optimize import brentq

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.titlesize':13})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13,6.3),gridspec_kw={'width_ratios':[1.1,1]})
ax.add_patch(Rectangle((0,0),3,1.5,facecolor='#deebfa',edgecolor='#2166ac',label=r'$D_0=[0,3]\times[0,3/2]$'))
ax.add_patch(Rectangle((0,1.5),3,1.5,facecolor='#fbe5bd',edgecolor='#b06c00',label=r'Additional data in $D_{\rm ref}$'))
ax.add_patch(Rectangle((1,-3),2,4.5,fill=False,edgecolor='#8a3ea0',lw=2,label=r'$Q(x)=[1,3]\times[-3,3/2]$'))
ax.add_patch(Rectangle((0,-3),2,4.5,fill=False,edgecolor='#337b69',lw=2,linestyle='--',label=r'$Q(z)=[0,2]\times[-3,3/2]$'))
for u,v,sgn in [(2.5,2.5,'+'),(-2.5,2.5,'−'),(2.5,-2.5,'−'),(-2.5,-2.5,'+')]:
    ax.add_patch(Rectangle((u-.125,v-.125),.25,.25,facecolor='#c54136' if sgn=='+' else '#164c82',edgecolor='black'))
    ax.text(u,v+.27,sgn,ha='center',va='bottom',fontsize=16,weight='bold')
ax.plot([1,2],[1,1],'ko',ms=5)
ax.text(.87,.74,r'$z=(1,1)$',ha='right');ax.text(2.1,.72,r'$x=(2,1)$')
ax.annotate('',xy=(2.5,-2.24),xytext=(2.5,2.2),arrowprops={'arrowstyle':'->','color':'#b06c00','lw':1.7})
ax.axhline(0,color='black',lw=.8);ax.axvline(0,color='black',lw=.8)
ax.set(xlim=(-3.3,3.6),ylim=(-3.4,3.55),xlabel=r'Original coordinate $y_1$',ylabel=r'Original coordinate $y_2$',title='Reflected data omitted by the printed domain')
ax.set_aspect('equal');ax.legend(loc='upper center',bbox_to_anchor=(.5,-.13),fontsize=9,frameon=False,ncol=1)

h=1.5;d=h/2;a=1.;t=2/3
P=lambda r:h*t*r/(((r-d)**2+t*t)*((r+d)**2+t*t))
Pa=lambda r:np.where(r<=a-d,P(r),np.where(r<=a+d,t/2*(1/((r-d)**2+t*t)-1/(a*a+t*t)),0))
F=np.sqrt((d*d-t*t+2*np.sqrt(d**4+d*d*t*t+t**4))/3)
c=min(F,max(d,a-d));r0=.2
T=brentq(lambda r:P(r)-P(r0),F,12)
Ta=brentq(lambda r:float(Pa(r))-float(Pa(r0)),c,a+d)
rs=np.linspace(0,4,900)
bx.plot(rs,P(rs),color='#2166ac',lw=2,label=r'Full $P_{h,t}$ (NL11)')
bx.plot(rs,Pa(rs),color='#a95800',lw=2,label=r'Rectangular $P_{a,h,t}$ (NL16)')
bx.axhline(P(r0),color='#667',ls=':',lw=1)
for point,label,col,xytext in [(r0,r'$r$', 'black',(.20,.29)),(Ta,r'$T_{a,h,t}(r)$','#a95800',(.93,.30)),(T,r'$T_{h,t}(r)$','#2166ac',(2.18,.25))]:
    bx.plot(point,P(r0),'o',color=col)
    bx.annotate(label,xy=(point,P(r0)),xytext=xytext,ha='center',fontsize=10,color=col,arrowprops={'arrowstyle':'-','color':col,'lw':.8})
for point,label in [(a-d,r'$a-\delta$'),(a+d,r'$a+\delta$')]:
    bx.axvline(point,color='#888',lw=.8,ls='--');bx.text(point,.98,label,transform=bx.get_xaxis_transform(),ha='center',va='top')
bx.set(xlim=(0,4),ylim=(0,1.25*P(F)),xlabel=r'Original horizontal distance $r$',ylabel='Full primitive value',title='The rectangle moves the matched point closer')
bx.text(.51,.75,r'$h=3/2,\ a=1$'+'\n'+r'$t=2/3,\ r=1/5$'+'\nNumerical plot of exact\nformulas NL11–NL20',transform=bx.transAxes,fontsize=10)
bx.legend(loc='upper center',bbox_to_anchor=(.5,-.13),frameon=False,fontsize=10)
fig.suptitle('Chen–Hou horizontal kernel: domain correction and exact cost comparison',y=1.01,fontsize=15)
fig.tight_layout(w_pad=3)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-rectangular-reflection.'+ext),dpi=170,bbox_inches='tight')
(R/'chen-hou-rectangular-samples.json').write_text(json.dumps(dict(geometry='Exact rational endpoints in NL6–NL8',primitive_sample=dict(h=h,a=a,t=t,r=r0,threshold=F,local_threshold=c,full_partner=T,local_partner=Ta),numerical_plot_only=True,proof='NL1–NL30'),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(full_partner=T,local_partner=Ta,figure='chen-hou-rectangular-reflection.png')))
