"""CC0: reproducible Euclidean root/coroot diagrams for the course.

Coordinates: alpha=(1,0); beta=(-1/2,sqrt(3)/2) in A2,
(-1,1) in B2, (-3/2,sqrt(3)/2) in G2. Coroots use the
Euclidean identification r^vee=2*r/(r.r). This realization does not
identify the integral character and cocharacter lattices.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

out=Path(__file__).resolve().parent.parent/'assets'
out.mkdir(exist_ok=True)
systems=[('A₂',np.array([-.5,np.sqrt(3)/2]),[(1,0),(0,1),(1,1)],30),
         ('B₂',np.array([-1.,1.]),[(1,0),(0,1),(1,1),(2,1)],45),
         ('G₂',np.array([-1.5,np.sqrt(3)/2]),[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)],60)]
fig,axes=plt.subplots(2,3,figsize=(11,7.3),layout='constrained')
fig.patch.set_facecolor('#fbfaf7')
for j,(name,beta,pairs,start) in enumerate(systems):
    alpha=np.array([1.,0.])
    positive=[i*alpha+k*beta for i,k in pairs]
    for row in range(2):
        ax=axes[row,j]
        vectors=positive if row==0 else [2*v/np.dot(v,v) for v in positive]
        extent=2.35
        ax.set_facecolor('#fbfaf7')
        ax.add_patch(Wedge((0,0),extent,start,90,facecolor='#d9efe9',edgecolor='none',zorder=0))
        for v in vectors:
            perpendicular=np.array([-v[1],v[0]])/np.linalg.norm(v)*extent
            ax.plot([-perpendicular[0],perpendicular[0]],[-perpendicular[1],perpendicular[1]],color='#dedbd3',lw=.7,zorder=1)
        for idx,v in enumerate(vectors):
            color=['#b74236','#315eaa'][idx] if idx<2 else '#d18a32'
            for sign in [1,-1]:
                w=v*sign
                ax.annotate('',xy=w,xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':color if sign==1 else '#8d969b','lw':1.7},zorder=3)
            if idx<2:
                label=['α','β'][idx]+('∨' if row else '')
                p=v*1.10
                ax.text(p[0],p[1],label,fontsize=13,color=color,ha='center',va='center',fontweight='bold')
        ax.scatter([0],[0],s=12,color='#263b44',zorder=4)
        ax.plot([.8,1.8],[-2.1,-2.1],color='#8d969b',lw=1)
        ax.text(1.3,-2.23,'1 unit',fontsize=8,color='#677780',ha='center')
        ax.set_aspect('equal')
        ax.set_xlim(-extent,extent);ax.set_ylim(-extent,extent)
        ax.set_xticks([]);ax.set_yticks([])
        for spine in ax.spines.values():spine.set_visible(False)
        ax.set_title(name+(' roots' if row==0 else ' coroots'),fontsize=15,color='#263b44')
fig.suptitle('Root lengths reverse under duality',fontsize=20,color='#263b44')
fig.supxlabel('Green sector: the chamber where both simple-root pairings are positive.\nGrey lines: reflecting hyperplanes. Arrow lengths use the same Euclidean metric within each pair.',fontsize=11,color='#263b44')
fig.savefig(out/'rank-two-roots.svg',metadata={'Title':'Roots and coroots of types A2, B2 and G2','Creator':'GPT-6.1 Sol (OpenAI), Ultra setting','Description':'CC0; exact reproducible coordinates in the accompanying Python source.'})
fig.savefig(out/'rank-two-roots.png',dpi=180,metadata={'Title':'Roots and coroots of types A2, B2 and G2','Author':'GPT-6.1 Sol (OpenAI), Ultra setting','Copyright':'CC0'})
plt.close(fig)
print('Rendered rank-two-roots.svg and rank-two-roots.png')
