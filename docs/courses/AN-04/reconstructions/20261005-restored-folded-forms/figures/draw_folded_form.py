"""Exact signed patch integrals under (x,s)->(x,s^2/2)."""
import hashlib,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
dest=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(5.5,7.8),constrained_layout=True)
red='#a43d36';blue='#21677d';ink='#28343e'
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.spines['bottom'].set_position('zero');ax.spines['left'].set_position('zero')
    ax.grid(alpha=.12);ax.tick_params(labelsize=12)
    ax.set_xlim(-.2,.95);ax.set_xticks([.5]);ax.set_xticklabels([r'$1/2$'])
    ax.set_xlabel(r'$x$',loc='right',fontsize=15)
ax=axes[0];ax.set_ylim(-1.3,1.3)
ax.set_yticks([-1,-.5,.5,1]);ax.set_yticklabels([r'$-1$',r'$-1/2$',r'$1/2$',r'$1$'])
ax.set_ylabel(r'$s$',loc='top',rotation=0,fontsize=15)
ax.add_patch(Rectangle((0,.5),.5,.5,facecolor=red,edgecolor=red,alpha=.22,lw=2))
ax.add_patch(Rectangle((0,-1),.5,.5,facecolor=blue,edgecolor=blue,alpha=.22,lw=2))
ax.text(.59,.69,r'$\int \sigma=3/16$',fontsize=14,color=red)
ax.text(.59,-.84,r'$\int \sigma=-3/16$',fontsize=14,color=blue)
ax.text(.57,.08,r'$s=0$',fontsize=13,color=ink)
ax.set_title('Source normal slice: '+r'$s\,ds\wedge dx$',fontsize=13,pad=14)
ax=axes[1];ax.set_ylim(-.17,.75)
ax.set_yticks([.125,.5]);ax.set_yticklabels([r'$1/8$',r'$1/2$'])
ax.set_ylabel(r'$r$',loc='top',rotation=0,fontsize=15)
ax.axhspan(-.17,0,color='#b7b0a7',alpha=.3)
ax.add_patch(Rectangle((0,.125),.5,.375,facecolor='#6c7880',edgecolor=ink,alpha=.25,lw=2))
ax.text(.57,.3,r'$\int \Theta=3/16$',fontsize=14,color=ink)
ax.text(.33,-.12,'unattained',fontsize=13,color='#5e5853')
ax.text(.03,.61,r'$r=s^2/2$',fontsize=15,color=ink)
ax.set_title('Both sheets have this target image: '+r'$dr\wedge dx$',fontsize=12,pad=14)
svg=dest/'folded-form-and-square-quotient.svg'
qa=dest/'folded-form-and-square-quotient-qa.png'
plt.rcParams['svg.fonttype']='path'
fig.savefig(svg,metadata={'Date':None,'Creator':'AN-04 exact-coordinate figure'})
fig.savefig(qa,dpi=170);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'exact-folded-form-figure/v1','figure':'figures/folded-form-and-square-quotient.svg',
 'sha256':sha(svg),'script':'draw_folded_form.py','script_sha256':sha(Path(__file__)),
 'qa_image':qa.name,'qa_image_sha256':sha(qa),
 'coordinates':{'x_interval':['0','1/2'],'positive_s':['1/2','1'],
 'negative_s':['-1','-1/2'],'target_r':['1/8','1/2'],'map':'r=s^2/2',
 'source_orientation':'ds wedge dx','target_orientation':'dr wedge dx',
 'signed_integrals':['3/16','-3/16','3/16']},
 'scope':'Exact normal slice with spectator coordinates held fixed; signed differential-form integrals, not Euclidean source areas.',
 'visual_inspection':'Pending author visual inspection.'}
(dest/'figure-record.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':str(svg),'qa':str(qa),'sha256':record['sha256']}))

