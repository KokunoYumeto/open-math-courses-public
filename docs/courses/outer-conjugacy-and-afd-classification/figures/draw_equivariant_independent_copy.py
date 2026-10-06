"""Original CC0 orbit-algebra schematic; actual operators are defined in Sec. 9."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams['svg.hashsalt']='oa-classify-independent-orbit-copy-v1'
fig,ax=plt.subplots(figsize=(6.5,7.5));fig.patch.set_facecolor('#faf8f4')
ax.set_facecolor('#faf8f4');ax.set_xlim(0,6.5);ax.set_ylim(0,7.5);ax.axis('off')
ax.text(3.25,7.03,'Copy the orbit algebra;\nkeep its internal relations',
        ha='center',fontsize=15,weight='bold')
xs=[1.2,3.25,5.3]
for y,color,positions in [(5.3,'#dce7ea',[r'$n-1$',r'$n$',r'$n+1$']),
                          (2.8,'#f2dfca',[r'$3n-1$',r'$3n$',r'$3n+1$'])]:
    for x,label in zip(xs,positions):
        ax.add_patch(FancyBboxPatch((x-.58,y-.4),1.16,.8,
                     boxstyle='round,pad=.04',facecolor=color,edgecolor='#344d5a'))
        ax.text(x,y,r'$X,\ Z$',ha='center',va='center',fontsize=14)
        ax.text(x,y-.69,label,ha='center',fontsize=13)
    for x0,x1 in zip(xs,xs[1:]):
        ax.annotate('',xy=(x1-.7,y+.08),xytext=(x0+.7,y+.08),
                    arrowprops={'arrowstyle':'->','lw':1.8,'color':'#11647d'})
        ax.text((x0+x1)/2,y+.28,r'$\gamma$',ha='center',fontsize=13,color='#11647d')
ax.text(.6,6.12,'Fixed algebra A',fontsize=14,weight='bold')
ax.text(.6,3.62,'Independent copy of B',fontsize=14,weight='bold')
ax.annotate('',xy=(3.25,3.47),xytext=(3.25,4.33),
            arrowprops={'arrowstyle':'->','lw':2,'color':'#af5e15'})
ax.text(3.57,3.99,r'$T$',fontsize=15,color='#af5e15')
ax.text(3.25,1.6,r'$XZ=-ZX$ within each site',ha='center',fontsize=14)
ax.text(3.25,1.14,r'$[a,T(b)]=0$',ha='center',fontsize=14)
ax.text(3.25,.7,r'$\tau(aT(b))=\tau(a)\tau(b)$',ha='center',fontsize=14)
ax.text(3.25,.28,'Offsets are exact; the gaps are schematic.',ha='center',fontsize=12)
fig.tight_layout(pad=.6)
out=Path(__file__).resolve().parent
meta={'Date':'2026-10-02','Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 diagram'}
fig.savefig(out/'equivariant-independent-copy.svg',metadata=meta)
fig.savefig(out/'equivariant-independent-copy.png',dpi=160,metadata={'Creator':meta['Creator']})
