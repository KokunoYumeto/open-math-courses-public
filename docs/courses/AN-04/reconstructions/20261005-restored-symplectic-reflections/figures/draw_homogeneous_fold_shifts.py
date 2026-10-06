"""Exact shift/coefficient diagram for the homogeneous simultaneous fold."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
here=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'svg.fonttype':'path','font.family':'DejaVu Sans'})
t=np.linspace(-1,1,801)
fig,axes=plt.subplots(2,1,figsize=(5.8,7.5),gridspec_kw={'height_ratios':[1,1]})
blue='#176f91';red='#b14a35';grey='#747474'
for ax in axes:
    ax.axhline(0,color=grey,lw=.7);ax.axvline(0,color=grey,lw=.7)
    ax.set_xlim(-1.05,1.05);ax.set_xticks([-1,-.5,0,.5,1])
    ax.grid(alpha=.12);ax.set_xlabel(r'Ratio $t=\xi_1/\rho$',labelpad=6)
    ax.spines[['top','right']].set_visible(False)
axes[0].plot(t,2*t,color=blue,lw=2.5,label=r'$V(t)=2t$')
axes[0].plot(t,-2*t**3/3,color=red,lw=2.5,label=r'$W(t)=-2t^3/3$')
axes[0].set_title('Position shifts at fixed frequencies',pad=14)
axes[0].set_ylabel('Position shift');axes[0].set_ylim(-2.25,2.65)
axes[0].legend(loc='upper left',frameon=False,fontsize=12)
axes[0].plot([.5],[1],'o',color=blue,ms=5)
axes[0].plot([.5],[-1/12],'o',color=red,ms=5)
axes[0].annotate(r'$(1/2,1)$',(.5,1),xytext=(.55,1.55),fontsize=11,
                 arrowprops={'arrowstyle':'-','color':blue})
axes[0].annotate(r'$(1/2,-1/12)$',(.5,-1/12),xytext=(.07,-1.25),fontsize=11,
                 arrowprops={'arrowstyle':'-','color':red})
axes[1].plot(t,2*t*t,color=blue,lw=2.5,label=r'$t^2V^\prime=2t^2$')
axes[1].plot(t,-2*t*t,color=red,lw=2.5,label=r'$W^\prime=-2t^2$')
axes[1].plot(t,np.zeros_like(t),color=grey,lw=2,ls='--')
axes[1].set_title('Two-form coefficients cancel exactly',pad=14)
axes[1].set_ylabel('Coefficient of '+r'$d\rho\wedge dt$')
axes[1].set_ylim(-2.65,2.65)
axes[1].legend(loc='upper center',frameon=False,fontsize=12)
axes[1].text(-.98,-2.5,r'$t^2V^\prime+W^\prime=0$',fontsize=13,
             bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
fig.subplots_adjust(left=.18,right=.97,top=.95,bottom=.08,hspace=.6)
dest=here/'homogeneous-fold-shifts.svg'
fig.savefig(dest,metadata={'Title':'Exact homogeneous fold shifts and two-form cancellation',
 'Description':'Exact model V=2t, W=-2t^3/3 with fixed spectators and positive frequency; not flow trajectories.',
 'Creator':'AN-04 course author'})
qa=here/'homogeneous-fold-shifts-qa.png';fig.savefig(qa,dpi=170)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'figure':'figures/'+dest.name,'sha256':sha(dest),'script':Path(__file__).name,
 'script_sha256':sha(Path(__file__)),'qa_image':qa.name,'qa_image_sha256':sha(qa),
 'visual_inspection':'pending','exact_geometry':'t in [-1,1], V=2t, W=-2t^3/3; cancellation contributions 2t^2 and -2t^2, sum zero; marked values t=1/2,V=1,W=-1/12.',
 'mathematical_scope':'Fixed spectator/positive-frequency coordinate shifts and differential-form coefficients. Full proof locators (6.1)-(6.3),(7.3), Exercise 8.8.',
 'license':'CC0 original vector diagram'}
(here/'figure-record.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':dest.name,'sha256':sha(dest)}))
