"""Original CC0 diagrams for RT-LIE-08, Section 6 and Exercise 9.1.

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra, October 2026.
Run with Python, NumPy and Matplotlib: python rt_lie_08_figures.py OUTPUT_DIR.
Coordinates are the exact models proved in the lesson, evaluated numerically
only for rendering. No source illustration was copied or traced.
"""
from pathlib import Path
import sys, math, json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D

MODELS = [
    ('a1a1', r'$A_1\times A_1$', (1,0), (0,1), [(1,0),(0,1)],
     [r'$\alpha$',r'$\beta$'], 0, 90, 2, [(1.15,.08),(.08,1.14)]),
    ('a2', r'$A_2$', (1,0), (-.5,math.sqrt(3)/2), [(1,0),(0,1),(1,1)],
     [r'$\alpha$',r'$\beta$',r'$\alpha+\beta$'], 30, 90, 3,
     [(1.16,.08),(-.69,1.02),(.70,1.04)]),
    ('b2', r'$B_2$', (1,-1), (0,1), [(1,0),(0,1),(1,1),(1,2)],
     [r'$\alpha$',r'$\beta$',r'$\alpha+\beta$',r'$\alpha+2\beta$'], 0, 45, 4,
     [(1.18,-1.16),(-.18,1.20),(1.18,.08),(1.27,1.19)]),
    ('g2', r'$G_2$', (1,0), (-1.5,math.sqrt(3)/2),
     [(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)],
     [r'$\alpha$',r'$\beta$',r'$\alpha+\beta$',r'$2\alpha+\beta$',
      r'$3\alpha+\beta$',r'$3\alpha+2\beta$'], 60, 90, 6,
     [(1.18,-.12),(-1.69,1.05),(-.68,1.03),(.60,1.05),(1.76,1.04),(.05,1.96)]),
]

def render(output):
    output.mkdir(parents=True,exist_ok=True)
    receipts=[]
    for key,title,alpha,beta,pairs,labels,low,high,m,positions in MODELS:
        a=np.array(alpha,dtype=float); b=np.array(beta,dtype=float)
        positive=np.array([i*a+j*b for i,j in pairs])
        radius=2.35 if key=='g2' else 1.90
        limit=2.45 if key=='g2' else 2.05
        fig,ax=plt.subplots(figsize=(7.5,6.5),layout='constrained')
        theta=np.radians(np.linspace(low,high,100))
        sector=np.vstack([[0,0],np.column_stack([radius*np.cos(theta),radius*np.sin(theta)]),[0,0]])
        ax.add_patch(Polygon(sector,facecolor='#d5eee7',edgecolor='none',zorder=0))
        # One wall per opposite root pair, perpendicular to that root.
        walls=[]
        for v in positive:
            angle=(math.atan2(v[1],v[0])+math.pi/2)%math.pi
            if not any(abs(angle-t)<1e-10 for t in walls): walls.append(angle)
        for angle in walls:
            v=limit*np.array([math.cos(angle),math.sin(angle)])
            ax.plot([-v[0],v[0]],[-v[1],v[1]],'--',color='#8a9da0',lw=1.15,zorder=1)
        for sign in [-1,1]:
            for k,v in enumerate(positive):
                end=sign*v
                color='#bc5a11' if sign==1 and k<2 else '#2459a6' if sign==1 else '#697683'
                ax.annotate('',xy=end,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=color,lw=2.0,mutation_scale=15,shrinkA=0,shrinkB=0),zorder=3)
        for label,(x,y) in zip(labels,positions):
            ax.text(x,y,label,fontsize=15,ha='center',va='center',color='#26384b',zorder=5,
                    bbox=dict(facecolor='white',edgecolor='none',alpha=.75,pad=1))
        centre=math.radians((low+high)/2)
        ax.text(radius*.78*math.cos(centre),radius*.78*math.sin(centre),r'$C$',
                fontsize=19,color='#216953',ha='center',va='center',zorder=6)
        ax.set(xlim=(-limit,limit),ylim=(-limit,limit),aspect='equal',xlabel=r'$x_1$',ylabel=r'$x_2$')
        ax.set_title(title+f'   |   {2*len(pairs)} roots, {2*m} chambers',fontsize=18,pad=12)
        ax.tick_params(labelsize=11)
        ax.spines[['top','right']].set_visible(False)
        handles=[Line2D([0],[0],color='#bc5a11',lw=2,label='simple positive roots'),
                 Line2D([0],[0],color='#2459a6',lw=2,label='other positive roots'),
                 Line2D([0],[0],color='#697683',lw=2,label='negative roots'),
                 Line2D([0],[0],color='#8a9da0',lw=1.2,ls='--',label='reflecting walls')]
        ax.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,-.28),ncol=2,frameon=False,fontsize=11)
        target=output/f'rank2-{key}.png'
        fig.savefig(target,dpi=180,metadata={'Software':'Matplotlib; original RT-LIE-08 CC0 diagrams'})
        plt.close(fig)
        # Independent geometric checks bind the picture to its stated chamber.
        midpoint=np.array([math.cos(centre),math.sin(centre)])
        assert midpoint@a>0 and midpoint@b>0
        for t in walls:
            for ray in (math.degrees(t),math.degrees(t)+180):
                assert not low+1e-8<ray<high-1e-8
        assert len(walls)==len(pairs)==m
        receipts.append(dict(id=key,coordinates=positive.tolist(),wall_angles_degrees=[math.degrees(t) for t in sorted(walls)],
                             chamber_degrees=[low,high],sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
    return receipts

if __name__=='__main__':
    destination=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'assets/RT-LIE-08'
    print(json.dumps(render(destination),indent=2))
