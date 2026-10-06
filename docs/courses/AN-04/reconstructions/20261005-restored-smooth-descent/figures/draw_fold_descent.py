"""Exact one-dimensional normal slice for the U014 fold and descent proofs."""
import hashlib,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
dest=Path(__file__).resolve().parent
dest.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':18,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(6.3,5.2),layout='constrained')
s=np.linspace(-1.45,1.45,401)
ax.plot(s[s<=0],s[s<=0]**2,color='#28677e',lw=2.5)
ax.plot(s[s>=0],s[s>=0]**2,color='#a53b35',lw=2.5)
ax.axhspan(-.4,0,color='#dedbd4',alpha=.7)
ax.axvline(0,color='#6a7074',lw=1,alpha=.45)
ax.axhline(0,color='#6a7074',lw=1,alpha=.6)
ax.scatter([-1,1],[1,1],color=['#28677e','#a53b35'],s=40,zorder=5)
ax.scatter([0],[0],color='#272d33',s=35,zorder=5)
ax.annotate('',(1,1),(-1,1),arrowprops={'arrowstyle':'<->','color':'#272d33','lw':1.5})
ax.text(0,1.13,'sheet exchange',ha='center',fontsize=16)
ax.text(-1.08,.72,r'$-s$',ha='center',color='#28677e')
ax.text(1.08,.72,r'$s$',ha='center',color='#a53b35')
ax.text(0,2.2,r'$r=s^2$',ha='center',fontsize=21)
ax.text(0,-.27,'unattained values',ha='center',fontsize=16,color='#555a60')
ax.annotate('fold point',(0,0),(0,.35),fontsize=15,ha='center',
             arrowprops={'arrowstyle':'->','color':'#555a60','lw':1})
ax.set(xlim=(-1.6,1.6),ylim=(-.4,2.45),xlabel=r'$s$',ylabel=r'$r$')
ax.set_title('One normal slice of a fold',fontsize=18,pad=14)
ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2])
ax.spines[['top','right']].set_visible(False)
ax.grid(alpha=.12)
figure=dest/'fold-and-smooth-descent.svg'
fig.savefig(figure,metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Date':None})
qa=dest/'fold-and-smooth-descent-qa.png'
fig.savefig(qa,dpi=170);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'schema':'original-mathematical-figure/v1','figure':'figures/'+figure.name,
 'sha256':sha(figure),'script':'draw_fold_descent.py','script_sha256':sha(Path(__file__)),
 'qa_image':qa.name,'qa_image_sha256':sha(qa),
 'visual_inspection':'pending','coordinates':'Exact graph r=s^2 with the other normal-form variables z fixed.',
 'objects':'Two graph points at s=-1 and s=1 have the same output r=1; the double arrow represents sheet exchange, not a trajectory. The origin is the fold point. Shading marks r<0, which has no source preimage.',
 'proof_locator':'U014 Theorem 1.2, Proposition 2.1 and Theorem 5.1',
 'license':'CC0-1.0','source':'Original exact normal-form diagram; no source illustration copied.',
 'mathematical_certification':False}
(dest/'figure-record.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':report['figure'],'sha256':report['sha256']}))
