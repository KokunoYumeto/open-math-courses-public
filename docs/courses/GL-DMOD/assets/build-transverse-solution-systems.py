"""Original reproducible diagrams of CS.7 and CS.19--CS.26."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
 'svg.hashsalt':'transverse-solution-systems-CS','axes.spines.top':False,'axes.spines.right':False})
r=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(8,11.8),constrained_layout=True)
ax=axes[0];w=np.linspace(-1.4,1.4,1401)
for b,c,label in [(4/3,'#9ac7d0','4/3'),(12/5,'#5294ac','12/5'),(24/7,'#225c83','24/7')]:
 t=b/np.sqrt(1+b*b)
 h=np.where(np.abs(w)<=t,np.sqrt(np.maximum(0,1-w*w)),np.maximum(0,np.sqrt(1+b*b)-b*np.abs(w)))
 h=np.where(np.abs(w)<=np.sqrt(1+b*b)/b,h,np.nan)
 ax.fill_between(w,0,h,color=c,alpha=.4)
 ax.plot(w,h,color=c,lw=2,label=r'$b='+label+'$')
h=np.sqrt(np.maximum(0,1-w*w));h=np.where(np.abs(w)<=1,h,np.nan)
ax.plot(w,h,'--',color='#202a35',lw=1.5,label=r'$K$: limiting carrier')
ax.plot([1.2],[0],'o',color='#c65335',ms=7)
ax.annotate(r'$S_*:t=6i/5$',xy=(1.2,0),xytext=(.45,1.07),arrowprops={'arrowstyle':'->','color':'#c65335'},color='#a53c29')
ax.set(xlim=(-1.4,1.4),ylim=(-.07,1.2),xlabel=r'$w=\operatorname{Im}t$',ylabel=r'$u=-\operatorname{Re}t$',
 title='Closed carriers under cone erosion')
ax.set_aspect('equal');ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=11)
ax=axes[1];x=np.linspace(-.42,.42,1201);e=1/8;radius=1/4
ax.axhspan(-e,e,color='#eff0e9',label=r'$|\operatorname{Re}t|<e$')
ax.axhspan(-.3,-e,color='#cbdbe9',alpha=.65,label=r'$E:\operatorname{Re}t<-e$')
for a,c in [(3,'#225c83'),(4,'#438f92')]:
 y=a*(radius-np.abs(x))-e
 ax.plot(x,y,color=c,lw=2,label=r'$a='+str(a)+'$')
 ax.fill_between(x,-.3,np.maximum(-.3,y),where=y>-.3,color=c,alpha=.12)
ax.axhline(e,color='#697583',ls=':',lw=1);ax.axhline(-e,color='#697583',ls=':',lw=1)
ax.axvline(radius-2*e/3,color='#c65335',ls='--',lw=1)
ax.text(.177,.22,r'$d=r-2e/a$',rotation=90,fontsize=11,color='#a53c29')
xx=.22;yy=3*(radius-xx)-e
ax.arrow(xx,yy,.06,.02,head_width=.013,length_includes_head=True,color='#c65335')
ax.annotate(r'$(\tau,\xi)=(1,3)$',xy=(xx+.05,yy+.017),xytext=(.13,-.22),arrowprops={'arrowstyle':'->'},fontsize=12)
ax.set(xlim=(-.42,.42),ylim=(-.3,.4),xlabel=r'$x-x_0$ (real section)',ylabel=r'$\operatorname{Re}t$',
 title=r'$V(a,r)$: $e=1/8$, $r=1/4$')
ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=10)
fig.suptitle('Supports and transverse noncharacteristic funnels',fontsize=18)
fig.savefig(r/'transverse-solution-systems.png',dpi=170,metadata={'Software':'Original mathematical course diagram'})
fig.savefig(r/'transverse-solution-systems.svg',metadata={'Date':None,'Creator':'Original mathematical course diagram'})
plt.close(fig)
data={'upper_panel':{'coordinates':'t=-u+iw','original_support':'0<=u, u^2+w^2<=1',
 'b':['4/3','12/5','24/7'],'excluded_complex_point':'t=6i/5',
 'central_contact':'|w|=b/sqrt(1+b^2)','tangent_line':'u=sqrt(1+b^2)-b|w|',
 'carrier_endpoint':'|w|=sqrt(1+b^-2)'},
 'lower_panel':{'coordinates':['Re(x-x0)','Re(t)'],'imaginary_coordinates':0,
 'e':'1/8','r':'1/4','apertures':[3,4],'boundary':'Re(t)=a(r-|x-x0|)-e',
 'complex_covector_order':['tau','xi'],'labelled_normal':[1,3]},
 'proof_locators':['CS.6--CS.9','CS.19--CS.26','CS.35--CS.38'],
 'source':'https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf'}
(r/'transverse-solution-systems-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
