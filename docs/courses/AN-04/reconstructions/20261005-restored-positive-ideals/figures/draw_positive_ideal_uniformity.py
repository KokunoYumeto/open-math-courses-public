"""Exact model curves for U028 Exercise17, plus its singular real-zero comparison."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
here=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'AN04-positive-ideal-uniformity-v1','axes.titlesize':14,'axes.labelsize':13})
fig,axes=plt.subplots(3,1,figsize=(6.5,13))
fig.subplots_adjust(top=.88,bottom=.17,hspace=.85,left=.16,right=.95)
fig.suptitle('Positive ideals: real zeros and uniform symbols',fontsize=15,y=.985)
ax=axes[0];t=np.linspace(-.55,.55,1101)
ax.plot(t,np.zeros_like(t),color='#176b8d',lw=2.5,label=r'$w=0$')
ax.plot(np.zeros_like(t),t,color='#b6592c',lw=2.5,label=r'$z=0$')
ax.plot([0],[0],'o',color='#222222',ms=5)
ax.set(xlabel=r'$z/r$',ylabel=r'$w/r$',xlim=(-.6,.6),ylim=(-.6,.6))
ax.set_aspect('equal',adjustable='box');ax.legend(loc='upper right',fontsize=11)
ax.set_title('A. Exact angular real zeros, r = 1\n'+r'$H=-i z^2w^2/r^3$'+'\nRank 1 on each arm; rank 0 at the crossing')
ax.grid(alpha=.18)
s=np.linspace(.001,.46,2001)
colors=['#176b8d','#b6592c','#6d4894','#497534'];samples=[]
for lam,col in zip([12.,24.,48.,72.],colors):
 q=s*np.sqrt(lam);u=(q-1)/.4;psi=np.zeros_like(s);inside=np.abs(u)<1
 psi[inside]=np.exp(1-1/(1-u[inside]**2))
 logG=lam-1/s**2
 G=np.exp(np.minimum(logG,700));damp=np.exp(-G)
 axes[1].plot(s,psi,color=col,lw=2,label=r'$\log r='+str(int(lam))+'$')
 axes[2].plot(s,psi*damp,color=col,lw=2)
 point=1/np.sqrt(lam)
 axes[1].plot([point],[1],'o',color=col,ms=4)
 axes[2].plot([point],[np.exp(-1)],'o',color=col,ms=5)
 samples.append({'log_radius':lam,'sample_count':len(s),'path_angle':point,'damping_on_path':float(np.exp(-1))})
axes[1].set_title('B. Moving support of a symbol in the smooth ideal\n'+r'$r^{1/2}v=\psi(s\sqrt{\log r}),\quad s=z/r$')
axes[1].set(xlabel=r'Angular coordinate $s=z/r$',ylabel=r'$r^{1/2}v$',xlim=(0,.46),ylim=(-.02,1.08))
handles,labels=axes[1].get_legend_handles_labels()
fig.legend(handles,labels,fontsize=9.5,ncol=4,loc='upper center',bbox_to_anchor=(.5,.96),frameon=False)
axes[1].grid(alpha=.18)
axes[2].set_title('C. Damping on the same moving support\n'+r'$H=-ir e^{-1/s^2},\quad r^{1/2}e^{-iH}v$')
axes[2].set(xlabel=r'Angular coordinate $s=z/r$',ylabel='Normalized damped symbol',xlim=(0,.46),ylim=(-.02,1.08))
axes[2].axhline(np.exp(-1),color='#444444',lw=1,ls='--')
axes[2].text(.285,.42,r'Path values $e^{-1}$',fontsize=11)
axes[2].grid(alpha=.18)
fig.text(.12,.082,r'Marked path: $s=(\log r)^{-1/2}$, so $-\operatorname{Im}H=1$.',fontsize=12)
fig.text(.12,.059,r'Along it: $e^{-iH}v=e^{-1}r^{-1/2}$, which is not rapid decay.',fontsize=12)
fig.text(.12,.034,'Exact models: U028 (11.3), Sections 8–9 and Exercise 17.\nCurves are numerical samples; the all-order proofs remain in the text.',fontsize=10)
p=here/'positive-ideal-uniformity.svg';fig.savefig(p,metadata={'Date':None,'Creator':'Original AN-04 mathematical figure'})
qa=here/'positive-ideal-uniformity.png';fig.savefig(qa,dpi=150);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'schema':'exact-positive-ideal-model-figure/v1','figure':'figures/'+p.name,'sha256':sha(p),'script':'draw_positive_ideal_uniformity.py','script_sha256':sha(Path(__file__)),'qa_image':qa.name,'qa_image_sha256':sha(qa),'proof_locators':'U028 (11.3), Sections8-9 and Exercise17','exact_objects':'PanelA exact crossing of axes on r=1; panelsB/C psi(q)=exp(1-1/(1-((q-1)/0.4)^2)) for |q-1|<0.4, zero otherwise. This fixes the bump of Exercise17; angular cutoff equals1 for |s|<=0.5 and frequency cutoff equals1 for r>=exp(12). All plotted samples lie in those unit regions.','samples':samples,'visual_inspection':'Pending complete author inspection of rendered figure.','source':'Original reproducible drawing; outlined DejaVu/STIX glyph licences retained; no source images copied.'}
(here/'positive-ideal-uniformity-figure.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'figure':str(p),'sha256':sha(p),'samples':4*2001+2*1101}))
