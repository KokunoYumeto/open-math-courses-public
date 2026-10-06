"""Exact coordinate slice of U012 Exercise 7.9; original reproducible figure."""
import hashlib,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

dest=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':18,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(6.4,5.6),layout='constrained')
blue='#28677e';red='#a53b35'
for xi1 in [-1.5,-.75,0,.75,1.5]:
    color=red if xi1==0 else blue
    ax.plot([xi1,xi1],[.09,2.6],color=color,lw=2)
    ax.annotate('',(xi1,1.9),(xi1,1.25),arrowprops={'arrowstyle':'->','color':color,'lw':2})
    ax.scatter([xi1],[1.],s=22,color=color)
    # These arrows are positive multiples of R=(xi1,xi2), at xi2=1.
    ax.annotate('',(1.24*xi1,1.24),(xi1,1.),
                arrowprops={'arrowstyle':'->','color':'#272d33','lw':1.7})
ax.text(0,2.72,'conic',ha='center',color=red,weight='bold')
ax.text(-1.3,2.72,'transverse',ha='center',color=blue)
ax.text(1.3,2.72,'transverse',ha='center',color=blue)
ax.set(xlim=(-2.05,2.05),ylim=(0,3.05),xlabel=r'$\xi_1$',ylabel=r'$\xi_2>0$')
ax.set_title('Characteristic leaves and dilation\n'+r'$x_2=0,\ \xi_2>0$; fixed $x_1=0$',pad=16,fontsize=16)
ax.set_xticks([-1.5,-.75,0,.75,1.5]);ax.set_yticks([0,1,2,3])
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y',alpha=.15)
fig.savefig(dest/'characteristic-leaves-and-dilation.svg',metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Date':None})
qa=dest/'characteristic-leaves-and-dilation-qa.png'
fig.savefig(qa,dpi=170);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'original-mathematical-figure/v1','figure':'figures/characteristic-leaves-and-dilation.svg',
 'sha256':sha(dest/'characteristic-leaves-and-dilation.svg'),'script':'draw_characteristic_leaves.py',
 'script_sha256':sha(Path(__file__)),'qa_image':qa.name,
 'qa_image_sha256':sha(qa),'visual_inspection':'pending',
 'coordinates':'Actual 2-dimensional coordinate slice x1=0 of the 3-dimensional hypersurface x2=0, xi2>0.',
 'objects':'Vertical characteristic leaves at fixed xi1; colored arrows are positive characteristic tangents. Black arrows at xi2=1 are 0.24 times R=(xi1,xi2). Central xi1=0 leaf is conic; all others have a nonzero radial transverse component.',
 'proof_locator':'U012 Exercise 7.9 and Theorem 4.1','license':'CC0-1.0',
 'source':'Original coordinate diagram derived from the complete course example; no external image copied.',
 'mathematical_certification':False}
(dest/'figure-record.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':record['figure'],'sha256':record['sha256']}))
