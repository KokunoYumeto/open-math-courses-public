"""Draw the exact ordinary two-involution model; no numerical trajectory."""
import hashlib,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
dest=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(5.2,8.5),constrained_layout=True)
blue='#21677d';red='#a43d36';ink='#28343e'
for ax in axes:
    ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
    ax.spines['bottom'].set_position('zero');ax.spines['left'].set_position('zero')
    ax.tick_params(labelsize=12);ax.set_xlabel(r'$t$',loc='right',fontsize=14)
    ax.set_ylabel(r'$s$',loc='top',rotation=0,fontsize=14)
    ax.grid(alpha=.1);ax.axhline(0,color=ink,lw=1)
ax=axes[0]
s=np.linspace(-1.25,1.25,101)
ax.plot(np.zeros_like(s),s,color=blue,lw=2.7)
ax.plot(-s/2,s,color=red,lw=2.7)
ax.scatter([0],[0],color=ink,s=28,zorder=5)
ax.annotate(r'$L_f=\mathbb{R}\partial_s$',xy=(0,.82),xytext=(.18,.88),
            fontsize=14,color=blue)
ax.annotate(r'$L_g=\mathbb{R}(\partial_s-\frac{1}{2}\partial_t)$',
            xy=(-.43,.86),xytext=(-1.18,1.37),fontsize=14,color=red,
            arrowprops=dict(arrowstyle='->',color=red,lw=1))
ax.text(.48,.06,r'$S:\ s=0$',fontsize=14,color=ink)
ax.set_xlim(-1.3,1.3);ax.set_ylim(-1.4,1.65)
ax.set_xticks([-1,1]);ax.set_yticks([-1,1])
ax.set_title('The two reflection lines at the fixed point',fontsize=12,pad=12)
ax=axes[1]
P=np.array([.15,.9]);gP=np.array([1.05,-.9]);fgP=np.array([1.05,.9])
ax.scatter([P[0],gP[0],fgP[0]],[P[1],gP[1],fgP[1]],color=ink,s=30,zorder=5)
def arrow(start,end,color,label,textpos):
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',lw=1.8,color=color,shrinkA=5,shrinkB=5))
    ax.text(*textpos,label,fontsize=14,color=color,ha='center',
            bbox=dict(facecolor='white',edgecolor='none',alpha=.94,pad=2))
arrow(P,gP,red,r'$g$',(.83,-.25))
arrow(gP,fgP,blue,r'$f$',(1.18,.05))
arrow(P,fgP,ink,r'$\delta=f\circ g:\ t\mapsto t+s$',(.59,1.23))
ax.annotate(r'$P$',xy=P,xytext=(.04,1.02),fontsize=14)
ax.annotate(r'$gP$',xy=gP,xytext=(.97,-1.15),fontsize=14)
ax.annotate(r'$f(gP)$',xy=fgP,xytext=(.94,1.03),fontsize=14)
ax.text(-.16,.12,r'$S:\ s=0$',fontsize=14,color=ink)
ax.set_xlim(-.2,1.5);ax.set_ylim(-1.4,1.65)
ax.set_xticks([.5,1]);ax.set_yticks([-1,1])
ax.set_title('The exact product on one normal slice',fontsize=12,pad=12)
svg=dest/'two-reflections-and-shear.svg'
qa=dest/'two-reflections-and-shear-qa.png'
svg.parent.mkdir(parents=True,exist_ok=True);qa.parent.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.fonttype']='path'
fig.savefig(svg,metadata={'Date':None,'Creator':'AN-04 exact-coordinate figure'})
fig.savefig(qa,dpi=170);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec={'schema':'exact-two-reflections-figure/v1','figure':'figures/two-reflections-and-shear.svg',
 'sha256':sha(svg),'script':'draw_two_reflections.py','script_sha256':sha(Path(__file__)),
 'qa_image':qa.name,'qa_image_sha256':sha(qa),
 'coordinates':{'P':P.tolist(),'gP':gP.tolist(),'fgP':fgP.tolist(),
                'reflection_vectors':[[0,1],[-.5,1]]},
 'scope':'Exact two-dimensional slice and minus-one eigenlines of the simultaneous model, not a flow or a symplectic normal-form proof.',
 'visual_inspection':'Pending author visual inspection.'}
(dest/'figure-record.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':str(svg),'qa':str(qa),'sha256':rec['sha256']}))
